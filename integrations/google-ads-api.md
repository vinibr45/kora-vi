# Integration: Google Ads API

## Purpose

Connect KORA-approved tools to Google Ads account data for campaign performance analysis and optimization proposals.

## Official Documentation Checked

- Google Ads API onboarding: https://developers.google.com/google-ads/api/docs/get-started/onboarding
- Python client configuration: https://developers.google.com/google-ads/api/docs/client-libs/python/configuration
- Mutate method: https://developers.google.com/google-ads/api/rest/common/mutate
- Mutating resources overview: https://developers.google.com/google-ads/api/docs/mutating/overview

## Required Access

- Google Ads Manager Account or authorized account hierarchy.
- Developer token.
- Login customer ID when using a manager account.
- Customer ID for the account being queried.
- OAuth/service-account credentials authorized for Google Ads API access.

## Read Pattern

Use Google Ads Query Language requests through `googleAds:searchStream` for analysis and reporting.

## Write Pattern

External changes use `:mutate` endpoints with create, update, or remove operations. KORA does not treat write access as implied by read access.

## Safety Rules

- Default mode is read-only.
- Never call `:mutate` from a reader/proposal tool.
- Do not store developer tokens, customer IDs, private keys, refresh tokens, exported reports, or raw account data in public project repositories.
- Treat API version, authentication requirements, permissions, policy rules, and platform limits as current-information topics that must be checked against official documentation before changing integration behavior.
