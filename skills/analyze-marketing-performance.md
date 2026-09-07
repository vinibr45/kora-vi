---
name: "analyze-marketing-performance"
type: decision
scope: hybrid
status: draft
version: "0.1"
owner: "Marcos"
domains:
  - marketing
  - analytics
  - paid-media
  - social-media
related_agents:
  - marketing-performance-analyst
related_skills:
  - check-approval-needed
  - assess-integration-need
  - use-installed-kora
  - select-context
required_knowledge:
  - knowledge/marketing/metrics/marketing-metrics-reading.md
  - knowledge/marketing/metrics/paid-media-api-read-only-analysis.md
required_tools:
  - google-analytics-read-connector
  - google-ads-read-connector
  - instagram-read-connector
evals:
  - EV-0016-marketing-channel-integrations
created_at: 2026-09-07
updated_at: 2026-09-07
---

# Analyze Marketing Performance

## Purpose

Analyze marketing data from authorized channels such as Google Analytics, Google Ads, Instagram, and future connectors for a KORA-connected project.

This skill creates a repeatable method for reading channel data, checking data quality, comparing performance, and producing practical recommendations without changing external accounts.

## When To Use

- When the user asks to analyze Google Analytics, Google Ads, Instagram, Meta, Search Console, CRM, email, or marketing channel performance.
- When a project needs a traffic, campaign, content, attribution, or funnel snapshot.
- When the user says "olha os dados", "analisa meus canais", "ve o que esta funcionando", or "o que eu faria no marketing desse projeto?".
- When multiple channel exports or connectors need to be interpreted together.

## When Not To Use

- When the user wants to change campaigns, budgets, tags, pixels, posts, comments, or messages.
- When account access has not been authorized and no export/screenshot was supplied.
- When the request is purely creative, such as generating posts or images without performance data.
- When the task is financial, product, or operational analysis with no marketing channel data.

## Inputs

- User request and target project.
- Project `.kora/binding.md`, if present.
- Period to analyze and comparison period.
- Channel list, such as Analytics, Ads, Instagram, Meta, Search Console, CRM, email, or others.
- Approved API/tool access or user-supplied exports/screenshots.
- Project business context: offer, target audience, conversion goals, funnel, geography, campaign objectives.

## Process

1. Identify the target project and read local `.kora/binding.md` when available.
2. Classify requested channels and whether each has an approved connector, export, screenshot, or missing access.
3. Run `skills/check-approval-needed.md` before account connection, new scopes, recurring sync, raw export storage, write operations, or spend changes.
4. Select only relevant context:

```text
project context
marketing goals
tracking setup
authorized channel data
reusable marketing metric knowledge
```

5. Collect or request data using read-only mode by default.
6. Assess data quality:

```text
period coverage
missing conversions
tracking gaps
small sample size
channel attribution limits
campaign naming quality
UTM consistency
```

7. Analyze each channel separately.
8. Compare channels only where metrics are comparable.
9. Separate:

```text
facts
interpretation
hypotheses
recommendations
risks or missing data
```

10. Recommend next actions, tests, or capability gaps.
11. Store project-specific summaries locally when the user asked for a durable record.

## Outputs

- Executive summary.
- Channel-by-channel findings.
- Cross-channel interpretation.
- Data quality warnings.
- Recommended next actions.
- Optional capability gap or integration need.
- Optional local report path.

## Required Knowledge

```text
knowledge/marketing/metrics/marketing-metrics-reading.md
knowledge/marketing/metrics/paid-media-api-read-only-analysis.md
```

## Optional Knowledge

```text
knowledge/marketing/funnels/funnel-stages-model.md
knowledge/marketing/offers/offer-clarity-checklist.md
knowledge/marketing/positioning/positioning-concept.md
knowledge/marketing/content/educational-content-framework.md
```

## Required Tools

Use only the tools needed for the requested and authorized channels:

```text
tools/google-analytics-read-connector.md
tools/google-ads-read-connector.md
tools/instagram-read-connector.md
```

## Optional Tools

Future read-only connectors may include:

```text
meta-ads-read-connector
google-search-console-read-connector
email-marketing-read-connector
crm-read-connector
```

## Evals

```text
evals/scenarios/EV-0016-marketing-channel-integrations.md
```

## Approval Points

Ask before:

- connecting or renewing external accounts;
- changing scopes or permissions;
- storing raw exports;
- creating recurring sync;
- using write APIs;
- changing budgets, bids, campaigns, audiences, posts, comments, messages, tags, events, or pixels.

## Boundaries

Default mode is read-only.

Do not store credentials or raw account data in KORA Core.

Do not infer exact attribution when tracking is incomplete.

Do not mix project-specific data into global KORA knowledge.

## Related

- `agents/marketing-performance-analyst.md`
- `integrations/google-analytics-data-api.md`
- `integrations/google-ads-api.md`
- `integrations/meta-instagram-platform.md`
- `tools/google-analytics-read-connector.md`
- `tools/google-ads-read-connector.md`
- `tools/instagram-read-connector.md`
- `automations/marketing-channel-health-snapshot.md`
- `evals/scenarios/EV-0016-marketing-channel-integrations.md`
- `architecture/decisions/DR-0028-marketing-channel-integration-layer.md`
