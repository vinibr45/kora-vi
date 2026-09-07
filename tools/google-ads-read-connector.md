# Tool: Google Ads Read Connector

## Purpose

Read authorized Google Ads account data and generate local diagnostics/proposals for Marcos Dev review.

This tool may also support future project-local marketing performance analysis through KORA's read-only marketing channel layer.

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

## Related

- `integrations/google-ads-api.md`
- `agents/marketing-performance-analyst.md`
- `skills/analyze-marketing-performance.md`
- `automations/marketing-channel-health-snapshot.md`
- `evals/scenarios/EV-0016-marketing-channel-integrations.md`
- `architecture/decisions/DR-0028-marketing-channel-integration-layer.md`
