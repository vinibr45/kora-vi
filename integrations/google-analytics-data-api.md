---
name: "google-analytics-data-api"
external_system: "Google Analytics Data API and Google Analytics Admin API"
scope: hybrid
status: proposed
owner: "Marcos"
permission_level: read-only
related_tools:
  - google-analytics-read-connector
related_agents:
  - marketing-performance-analyst
related_skills:
  - analyze-marketing-performance
related_evals:
  - EV-0016-marketing-channel-integrations
created_at: 2026-09-07
updated_at: 2026-09-07
---

# Google Analytics Data API

## Purpose

Connect KORA-approved workflows to authorized Google Analytics property data for traffic, acquisition, conversion, content, and funnel analysis.

## External System

Google Analytics Data API for reports and metrics.

Google Analytics Admin API only when property/account metadata or configuration review is explicitly needed and approved.

Official documentation checked on 2026-09-07:

```text
https://developers.google.com/analytics/devguides/reporting/data/v1
https://developers.google.com/analytics/devguides/config/admin/v1
```

## Scope

Hybrid.

The integration definition is reusable. Property IDs, credentials, business goals, event meanings, conversion definitions, exports, and reports belong to the local project or secure runtime configuration.

## Access Requirements

- Google account with authorized access to the target GA4 property.
- OAuth, service account, MCP connector, plugin, or approved export workflow.
- Property ID and project profile stored outside public repositories.
- Current official documentation review before changing scopes, fields, quotas, write behavior, or runtime implementation.

## Data Behavior

Read-only mode may fetch:

- sessions, users, views, engagement, events, conversions, revenue when configured;
- source/medium/campaign dimensions;
- landing pages and content performance;
- device, geography, and channel groupings;
- period comparisons and trend summaries.

Do not store raw reports in KORA Core.

## Permissions

Default permission level is read-only.

Admin/configuration access is not implied by reporting access.

Write/configuration changes are outside this integration's default scope.

## Platform Constraints

Google Analytics APIs, quotas, dimensions, metrics, attribution models, privacy thresholds, and Admin API stability can change.

Before runtime changes, verify current official Google documentation.

## Fallback Mode

If API access is unavailable, use:

```text
Google Analytics export supplied by the user
Looker Studio export
CSV snapshot
screenshots with visible date ranges
manual metric summary
```

## Security And Privacy

- Do not commit property IDs, tokens, refresh tokens, service-account keys, raw reports, or private customer data to KORA Core.
- Store credentials only in approved local secret locations.
- Persist summaries and decisions, not unnecessary raw user-level data.

## Approval Points

Ask before:

- connecting a Google account;
- adding or changing scopes;
- reading Admin/configuration data;
- storing raw exports;
- creating recurring sync;
- changing events, conversions, tags, properties, data streams, or account settings.

## Related

- `tools/google-analytics-read-connector.md`
- `agents/marketing-performance-analyst.md`
- `skills/analyze-marketing-performance.md`
- `automations/marketing-channel-health-snapshot.md`
- `evals/scenarios/EV-0016-marketing-channel-integrations.md`
- `architecture/decisions/DR-0028-marketing-channel-integration-layer.md`
