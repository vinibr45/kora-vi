# Tool: Google Ads Read Connector

## Purpose

Read authorized Google Ads account data and generate local diagnostics/proposals for Marcos Dev review.

## Runtime

```text
C:\KORA\runtime\tools\google-ads-reader\generate_proposal.ps1
```

## Integration

```text
C:\KORA\integrations\google-ads-api.md
```

## Inputs

- Private configuration in `C:\KORA\.env`.
- Optional output directory for generated Markdown proposals.

## Outputs

- Local Markdown proposal in the runtime `plans/` directory by default.
- Compact JSON status with generation mode and path.

## Allowed Operations

- Authenticate using configured read service account.
- Query Google Ads through `googleAds:searchStream`.
- Aggregate campaign-level metrics for review.
- Save a local proposal for human evaluation.

## Prohibited Operations

- No `:mutate` requests.
- No creation, update, removal, pause, budget, bid, keyword, ad, targeting, asset, conversion, or audience changes.
- No scheduled automation.
- No publishing or external account changes without explicit approval.
- No secrets or account data in public repositories.

## Approval Boundary

This tool may be used for read-only analysis when Marcos has authorized account access. Any execution tool that changes Google Ads must be a separate capability with explicit approval, dry-run evidence, execution log, and rollback plan.
