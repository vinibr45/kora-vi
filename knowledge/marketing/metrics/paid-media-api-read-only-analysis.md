---
title: "Paid Media API Read-Only Analysis"
type: framework
domain: "marketing"
subdomain: "metrics"
status: draft
version: "0.1"
evidence_level: internal_framework
sources:
  - https://developers.google.com/google-ads/api/docs/get-started/onboarding
  - https://developers.google.com/google-ads/api/docs/client-libs/python/configuration
  - https://developers.google.com/google-ads/api/rest/common/mutate
  - https://developers.google.com/google-ads/api/docs/mutating/overview
related:
  - knowledge/marketing/metrics/marketing-metrics-reading.md
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Paid Media API Read-Only Analysis

## Summary

Paid media API access should be split into read-only intelligence and write execution.

A read-only capability can support diagnosis, reporting, prioritization, and proposal drafting. A write capability changes external account state and therefore requires separate approval, logging, rollback planning, and current platform documentation review.

## Core Idea

Treat paid media accounts as external production systems.

Read operations answer: what is happening, what might be wrong, what should be reviewed?

Write operations answer: what exactly was approved, what will change, how will it be logged, and how can it be reversed?

For Google Ads specifically, campaign and account analysis can use query/read patterns such as Google Ads API search or searchStream. External changes use mutate endpoints with create, update, or remove operations.

## When To Use

- Creating a KORA tool, skill, or agent that evaluates ads, campaigns, search terms, spend, CPC, CTR, conversions, or lead quality.
- Migrating legacy marketing tools into KORA.
- Reviewing whether an ads workflow should be an agent, skill, tool, eval, or automation.
- Preparing optimization recommendations before any account change.

## When Not To Use

- When the user explicitly needs manual UI guidance only.
- When there is no authorized account access.
- When current platform documentation cannot be checked for API behavior that may have changed.
- When the task is already an approved execution workflow with its own stronger controls.

## How To Apply

1. Define the campaign objective and business outcome.
2. Confirm whether the current task is read-only analysis or external execution.
3. Use read-only API access to collect metrics and context.
4. Interpret metrics as signals, not conclusions.
5. Separate facts, inferences, hypotheses, recommendations, and approval-required actions.
6. Check conversion tracking and lead quality before treating clicks as success.
7. Keep private credentials, account identifiers, raw exports, and generated private reports outside public repositories.
8. Require explicit approval before any budget, bid, keyword, ad, targeting, audience, conversion, or campaign-status change.

## Examples

A Google Ads reader can collect impressions, clicks, cost, conversion count, campaign strategy, and budget data, then generate a Markdown proposal for review.

That same reader must not pause keywords, change budgets, create ads, update bids, or call mutate endpoints.

## Limitations

Read-only data is often incomplete. Campaign metrics may not explain lead quality, sales outcomes, attribution reliability, or offline follow-up.

Platform behavior, API versions, permissions, rate limits, and policy rules change over time. Check official documentation before changing integration behavior.

## Sources

- Google Ads API onboarding: https://developers.google.com/google-ads/api/docs/get-started/onboarding
- Google Ads API client configuration: https://developers.google.com/google-ads/api/docs/client-libs/python/configuration
- Google Ads API mutate method: https://developers.google.com/google-ads/api/rest/common/mutate
- Google Ads API mutating resources overview: https://developers.google.com/google-ads/api/docs/mutating/overview

## Related

- `knowledge/marketing/metrics/marketing-metrics-reading.md`

## Local Implementation References

These are implementation references from the Marcos Dev KORA setup. They are examples of this pattern, not generic requirements for every project.

Project-local public records:

- `C:\marcbmrs.github.io\.kora\tools\google-ads-reader.md`
- `C:\marcbmrs.github.io\.kora\skills\collect-google-ads-campaign-intelligence.md`
- `C:\marcbmrs.github.io\.kora\agents\google-ads-performance-analyst.md`
- `C:\marcbmrs.github.io\.kora\evals\google-ads-proposal-quality.md`
- `C:\marcbmrs.github.io\.kora\decisions\DR-0007-google-ads-kora-access.md`

KORA root records:

- `C:\KORA\tools\google-ads-read-connector.md`
- `C:\KORA\integrations\google-ads-api.md`
- `C:\KORA\runtime\tools\google-ads-reader\README.md`
- `C:\KORA\runtime\tools\google-ads-reader\generate_proposal.ps1`
- `C:\KORA\config\google-ads-reader.env.example`

Private ignored runtime locations:

- `C:\KORA\.env`
- `C:\KORA\private\google-ads\google-ads-reader.json`
- `C:\KORA\runtime\tools\google-ads-reader\plans\`
