# Google Ads Reader Runtime

Purpose: read authorized Google Ads account data and generate local Markdown diagnostics/proposals for human review.

Entrypoint:

```powershell
pwsh -ExecutionPolicy Bypass -File C:\KORA\runtime\tools\google-ads-reader\generate_proposal.ps1
```

Private configuration: `C:\KORA\.env`.

Required variables:

- `GOOGLE_ADS_DEVELOPER_TOKEN`
- `GOOGLE_ADS_LOGIN_CUSTOMER_ID`
- `GOOGLE_ADS_CUSTOMER_ID`
- `GOOGLE_ADS_SERVICE_ACCOUNT_KEY_PATH`
- `GOOGLE_ADS_API_VERSION` optional; defaults to `v25` in the script.

Allowed behavior:

- request OAuth access token from the configured service account;
- query Google Ads through `googleAds:searchStream`;
- save local Markdown reports in `plans/`;
- return a small JSON status object.

Prohibited behavior:

- no `:mutate` calls;
- no campaign, ad, budget, bid, keyword, asset, conversion, audience, or targeting changes;
- no publishing, scheduled automation, or spending changes;
- no secrets, account IDs, raw exports, or credentials in the public repository.

Related KORA records:

- `C:\KORA\tools\google-ads-read-connector.md`
- `C:\KORA\integrations\google-ads-api.md`
- `C:\marcbmrs.github.io\.kora\tools\google-ads-reader.md`
- `C:\marcbmrs.github.io\.kora\skills\collect-google-ads-campaign-intelligence.md`
