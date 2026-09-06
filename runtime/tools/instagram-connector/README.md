# KORA Runtime: Instagram Connector

Read-only Instagram connector runtime for authorized Marcos Dev profile/media reads.

This runtime was migrated from the legacy MarcosOS connector on 2026-09-05. It contains executable scripts only. It does not contain tokens, account IDs, raw API responses, exports, or private Instagram data.

## Secret Location

Preferred KORA-owned local secret file:

```text
C:\KORA\.env
```

Required variables for Marcos Dev:

```dotenv
INSTAGRAM_MARCOS_DEV_ACCESS_TOKEN=<token-de-acesso>
INSTAGRAM_MARCOS_DEV_ACCOUNT_ID=<id-da-conta-profissional>
```

Optional API version override:

```dotenv
INSTAGRAM_MARCOS_DEV_API_VERSION=v26.0
```

Do not commit, print, copy into chat, or store real values in this runtime folder or in any public repository.

## Commands

Run from `C:\KORA`:

```powershell
py -3 .\runtime\tools\instagram-connector\health_check.py --profile marcos-dev
py -3 .\runtime\tools\instagram-connector\read_media.py --profile marcos-dev --limit 12
```

## Behavior

- Read-only.
- No publishing.
- No Direct messages.
- No comment management.
- No scraping.
- No media downloads.
- No recurring sync.

## Migration Note

The scripts load `.env` from `C:\KORA\.env` because `health_check.py` resolves the root as two parents above this runtime folder. To complete migration away from MarcosOS, create `C:\KORA\.env` through a secure/manual process controlled by Marcos.