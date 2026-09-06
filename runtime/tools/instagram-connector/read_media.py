"""Leitura paginada e sanitizada de mídias próprias do Instagram."""

from __future__ import annotations

import json
import os
import sys
import time
from argparse import ArgumentParser
from datetime import datetime, timezone
from math import ceil
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

from health_check import ENV_PATH, PROFILES, VERSION_PATTERN, load_env


MEDIA_FIELDS = "id,caption,media_type,media_product_type,permalink,timestamp,like_count,comments_count"
MAX_PAGE_SIZE = 25
MAX_RETRIES = 2

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass


def request_json(url: str) -> dict:
    for attempt in range(MAX_RETRIES + 1):
        try:
            with urlopen(url, timeout=20) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as error:
            if error.code in {429, 500, 502, 503, 504} and attempt < MAX_RETRIES:
                time.sleep(2**attempt)
                continue
            raise
        except URLError:
            if attempt < MAX_RETRIES:
                time.sleep(2**attempt)
                continue
            raise


def clean_item(item: dict) -> dict:
    caption = (item.get("caption") or "").strip()
    return {
        "type": item.get("media_type"),
        "format": item.get("media_product_type"),
        "published_at": item.get("timestamp"),
        "caption": caption[:500],
        "caption_truncated": len(caption) > 500,
        "permalink": item.get("permalink"),
        "likes": item.get("like_count"),
        "comments": item.get("comments_count"),
    }


def main(profile: str, limit: int) -> int:
    env = {**load_env(ENV_PATH), **os.environ}
    prefix = PROFILES[profile]
    token = env.get(f"{prefix}_ACCESS_TOKEN", "")
    account_id = env.get(f"{prefix}_ACCOUNT_ID", "")
    api_version = env.get(f"{prefix}_API_VERSION", "v26.0")

    if not token or not account_id or not VERSION_PATTERN.fullmatch(api_version):
        print(json.dumps({"profile": profile, "ok": False, "reason": "configuração_local_incompleta"}, ensure_ascii=False))
        return 2

    pages_allowed = ceil(limit / MAX_PAGE_SIZE)
    query = urlencode({"fields": MEDIA_FIELDS, "limit": min(limit, MAX_PAGE_SIZE), "access_token": token})
    next_url = f"https://graph.instagram.com/{api_version}/{account_id}/media?{query}"
    media: list[dict] = []

    try:
        for _ in range(pages_allowed):
            payload = request_json(next_url)
            media.extend(clean_item(item) for item in payload.get("data", []))
            next_url = payload.get("paging", {}).get("next")
            if not next_url or len(media) >= limit:
                break
    except HTTPError as error:
        print(json.dumps({"profile": profile, "ok": False, "reason": "api_rejeitou_a_leitura", "http_status": error.code}, ensure_ascii=False))
        return 1
    except (URLError, TimeoutError, ValueError, json.JSONDecodeError):
        print(json.dumps({"profile": profile, "ok": False, "reason": "falha_de_conexao_ou_resposta"}, ensure_ascii=False))
        return 1

    print(json.dumps({
        "profile": profile,
        "ok": True,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "returned": len(media[:limit]),
        "has_more": bool(next_url),
        "media": media[:limit],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    parser = ArgumentParser(description="Lista mídias próprias sem alterar o Instagram.")
    parser.add_argument("--profile", choices=PROFILES, required=True)
    parser.add_argument("--limit", type=int, default=12, choices=range(1, 51))
    args = parser.parse_args()
    sys.exit(main(args.profile, args.limit))
