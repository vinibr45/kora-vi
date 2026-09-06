"""Verificação mínima e segura do conector de leitura do Instagram."""

from __future__ import annotations

import json
import os
import re
import sys
from argparse import ArgumentParser
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass


BASE_DIR = Path(__file__).resolve().parents[3]
ENV_PATH = BASE_DIR / ".env"
VERSION_PATTERN = re.compile(r"^v\d+\.\d+$")
DEFAULT_API_VERSION = "v26.0"
PROFILES = {
    "marcos-dev": "INSTAGRAM_MARCOS_DEV",
    "marcar-hora": "INSTAGRAM_MARCAR_HORA",
}


def load_env(path: Path) -> dict[str, str]:
    """Carrega pares simples KEY=VALUE sem imprimir nenhum conteúdo."""
    values: dict[str, str] = {}
    if not path.exists():
        return values

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def result(**values: object) -> None:
    print(json.dumps(values, ensure_ascii=False))


def main(profile: str) -> int:
    env = {**load_env(ENV_PATH), **os.environ}
    prefix = PROFILES[profile]
    token = env.get(f"{prefix}_ACCESS_TOKEN", "")
    account_id = env.get(f"{prefix}_ACCOUNT_ID", "")
    api_version = env.get(f"{prefix}_API_VERSION", DEFAULT_API_VERSION)

    if not token or not account_id or not VERSION_PATTERN.fullmatch(api_version):
        result(profile=profile, authorized=False, reason="configuração_local_incompleta")
        return 2

    query = urlencode({"fields": "id,account_type", "access_token": token})
    url = f"https://graph.instagram.com/{api_version}/{account_id}?{query}"

    try:
        with urlopen(url, timeout=15) as response:
            payload = json.loads(response.read().decode("utf-8"))
        if not payload.get("id"):
            raise ValueError("resposta_sem_identidade")
    except HTTPError as error:
        result(profile=profile, authorized=False, reason="api_rejeitou_a_consulta", http_status=error.code)
        return 1
    except (URLError, TimeoutError, ValueError, json.JSONDecodeError):
        result(profile=profile, authorized=False, reason="falha_de_conexao_ou_resposta")
        return 1

    result(profile=profile, authorized=True, scope="leitura_minima_de_perfil")
    return 0


if __name__ == "__main__":
    parser = ArgumentParser(description="Verifica autorização de leitura de um perfil do Instagram.")
    parser.add_argument("--profile", choices=PROFILES, default="marcos-dev")
    sys.exit(main(parser.parse_args().profile))
