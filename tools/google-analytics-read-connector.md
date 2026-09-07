---
name: "google-analytics-read-connector"
type: tool
scope: hybrid
status: proposed
owner: "Marcos"
permission_level: read-only
allowed_callers:
  - analyze-marketing-performance
  - marketing-performance-analyst
related_agents:
  - marketing-performance-analyst
related_skills:
  - analyze-marketing-performance
related_evals:
  - EV-0016-marketing-channel-integrations
created_at: 2026-09-07
updated_at: 2026-09-07
---

# Google Analytics Read Connector

## Purpose

Provide a read-only execution capability for authorized Google Analytics property reporting in KORA workflows.

This tool definition represents the reporting capability. Runtime implementation may be an API script, MCP connector, plugin, export reader, or other approved mechanism.

## Scope

Hybrid.

The connector pattern is reusable, but each project needs isolated local configuration, property access, account approval, and data boundaries.

## Runtime

Not implemented yet.

Future runtime should live under:

```text
runtime/tools/google-analytics-reader/
```

Secrets and account configuration must stay outside public repositories.

## Integration

```text
integrations/google-analytics-data-api.md
```

## Inputs

- Project profile key.
- GA4 property ID from secure local config.
- Date range and comparison period.
- Requested metric/dimension set.
- Optional report preset: acquisition, landing pages, conversions, campaigns, content, devices, geography.

## Outputs

- Sanitized report summary.
- Aggregated metrics.
- Data quality notes.
- Query/report metadata.
- Optional local Markdown report path.

## Allowed Operations

- Authenticate with configured read-only access.
- Read aggregated GA4 reporting data.
- Compare periods.
- Aggregate and summarize metrics for analysis.
- Save sanitized local reports when approved by the user.

## Prohibited Operations

- No event, conversion, tag, data stream, property, user, or account changes.
- No Admin API write operations.
- No raw user-level export storage.
- No recurring sync without explicit approval.
- No secrets in public repositories.

## Approval Boundary

Read-only analysis may run only after the target project/account access is authorized.

Any action that changes Analytics, Tag Manager, Ads links, events, conversions, consent settings, or account configuration requires a separate capability, explicit approval, dry-run evidence, execution log, and rollback plan where applicable.

## Related

- `integrations/google-analytics-data-api.md`
- `agents/marketing-performance-analyst.md`
- `skills/analyze-marketing-performance.md`
- `automations/marketing-channel-health-snapshot.md`
- `evals/scenarios/EV-0016-marketing-channel-integrations.md`
