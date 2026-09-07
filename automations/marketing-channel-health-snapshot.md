---
name: "marketing-channel-health-snapshot"
scope: hybrid
status: proposed
owner: "Marcos"
trigger: "manual user request"
frequency: "on demand; recurring only after approval"
permission_level: read-only
related_agents:
  - marketing-performance-analyst
related_skills:
  - analyze-marketing-performance
  - check-approval-needed
related_tools:
  - google-analytics-read-connector
  - google-ads-read-connector
  - instagram-read-connector
related_evals:
  - EV-0016-marketing-channel-integrations
created_at: 2026-09-07
updated_at: 2026-09-07
---

# Marketing Channel Health Snapshot

## Purpose

Create a repeatable read-only workflow for checking the health of a project's marketing channels.

## Scope

Hybrid.

The workflow is global. Account access, reports, raw exports, project goals, and findings remain project-local.

## Trigger

Manual requests such as:

```text
Checa a saude do marketing desse projeto.
Analisa Analytics, Ads e Instagram.
Me da um resumo semanal dos canais.
Ve se meus anuncios e conteudos estao funcionando.
```

Recurring execution requires explicit approval.

## Frequency

On demand by default.

Weekly or monthly only after approval, logs, storage rules, and stop conditions are defined.

## Workflow

1. Identify target project and read `.kora/binding.md`.
2. Confirm which channels are authorized.
3. Check whether approval is needed for account access, export storage, recurring sync, or new scopes.
4. Read authorized data using read-only connectors or user-provided exports.
5. Run `skills/analyze-marketing-performance.md`.
6. Report channel health, data quality, opportunities, risks, and next actions.
7. Store a local summary only when requested or when it supports recurring project work.

## Inputs

- Project profile.
- Authorized channels.
- Date range.
- Business goals and conversion definitions.
- Comparison baseline.

## Outputs

- Channel health summary.
- Metrics and trend highlights.
- Data quality warnings.
- Recommended actions.
- Optional local report.

## External Side Effects

Read-only API calls or connector reads.

No campaign changes, tracking changes, publishing, scheduling, or messaging.

## Approval Points

Approval is required before:

- connecting or renewing any account;
- changing scopes;
- storing raw exports;
- recurring execution;
- write operations to any external system.

## Stop Conditions

Stop when:

- account access is missing;
- requested data requires unapproved scope;
- data includes sensitive/private information beyond the task;
- a write operation is requested;
- attribution or tracking is too incomplete for the requested conclusion.

## Failure Handling

Use sanitized errors and fallback to exports/screenshots/manual summaries when APIs are unavailable.

Do not scrape platforms as a substitute for approved API access unless platform rules and KORA governance allow it.

## Evals

```text
evals/scenarios/EV-0016-marketing-channel-integrations.md
```

## Logging And Results

Project-local reports may live under:

```text
.kora/reports/marketing/
```

KORA Core stores only reusable definitions, evals, and non-sensitive learning.

## Learning Behavior

Recurring channel patterns may become local project knowledge or capability gaps after review.

Do not promote project-specific performance data into KORA Core knowledge.

## Related

- `agents/marketing-performance-analyst.md`
- `skills/analyze-marketing-performance.md`
- `tools/google-analytics-read-connector.md`
- `tools/google-ads-read-connector.md`
- `tools/instagram-read-connector.md`
- `integrations/google-analytics-data-api.md`
- `integrations/google-ads-api.md`
- `integrations/meta-instagram-platform.md`
- `evals/scenarios/EV-0016-marketing-channel-integrations.md`
- `architecture/decisions/DR-0028-marketing-channel-integration-layer.md`
