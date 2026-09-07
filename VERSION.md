# KORA Version

Current Version: 1.7.0

Date: 2026-09-07

Status: active

Stage: Marketing Channel Integration Layer

## Summary

KORA Core now includes a reusable marketing channel integration layer for read-only analysis of Google Analytics, Google Ads, Instagram, and future marketing connectors across connected projects.

## Versioning Policy

KORA uses semantic-style versioning for the architecture state:

```text
MAJOR.MINOR.PATCH
```

```text
MAJOR -> incompatible architecture or source-of-truth changes
MINOR -> new backward-compatible capability, workflow, eval, or entry point
PATCH -> clarification, correction, index fix, small documentation update
```

Version updates should be assessed with:

```text
skills/assess-kora-version-impact.md
```

When a change deserves versioning, release it with:

```text
skills/release-kora-version.md
```

## Current Release Highlights

- Human entry point: `COMECE-AQUI.md`
- Agent instructions: `AGENTS.md`
- Capability index: `CAPACIDADES.md`
- Natural request routing: `skills/route-user-request.md`
- Organic maintenance: `skills/maintain-kora-indexes.md`
- Maintenance automation definition: `automations/kora-index-maintenance.md`
- Health check: `skills/check-kora-health.md`
- Version impact assessment: `skills/assess-kora-version-impact.md`
- Version release workflow: `skills/release-kora-version.md`
- Practical examples: `examples/`
- Project flow guide: `projects/PROJECT-FLOW.md`
- Daily operating loop: `skills/run-daily-operating-loop.md`
- Loose idea capture: `skills/capture-loose-idea.md`
- Capability gap detection: `skills/detect-capability-gap.md`
- Approval checks: `skills/check-approval-needed.md`
- Maturity map: `MATURIDADE.md`
- Governance guide: `GOVERNANCA.md`
- Installed KORA usage: `skills/use-installed-kora.md`
- Installed KORA check: `skills/check-installed-kora.md`
- Local project AGENTS template: `projects/templates/local-agents-template.md`
- Local `.kora/README.md` template: `projects/templates/local-kora-readme-template.md`
- Installed project registry: `projects/INSTALLED-KORA.md`
- Installed project registration: `skills/register-installed-kora-project.md`
- Browser UX auditor: `agents/browser-ux-auditor.md`
- Chrome MCP UX audit skill: `skills/audit-ux-with-chrome-mcp.md`
- Chrome MCP browser integration definition: `integrations/chrome-mcp-browser-control.md`
- Browser page UX readiness eval: `evals/browser-page-ux-readiness.md`
- Image asset reviewer: `agents/image-asset-reviewer.md`
- Reviewed image generation skill: `skills/generate-reviewed-image-asset.md`
- Image generation provider integration template: `integrations/image-generation-provider.md`
- Reviewed image generation automation: `automations/reviewed-image-generation-loop.md`
- Reviewed image generation eval scenario: `evals/scenarios/EV-0015-reviewed-image-generation-loop.md`
- Governance and maturity notes for reviewed image generation: `GOVERNANCA.md`, `MATURIDADE.md`
- Marketing performance analyst: `agents/marketing-performance-analyst.md`
- Marketing performance analysis skill: `skills/analyze-marketing-performance.md`
- Google Analytics integration definition: `integrations/google-analytics-data-api.md`
- Google Analytics read connector definition: `tools/google-analytics-read-connector.md`
- Marketing channel health automation: `automations/marketing-channel-health-snapshot.md`
- Marketing channel integration eval: `evals/scenarios/EV-0016-marketing-channel-integrations.md`

## Related Decisions

```text
architecture/decisions/DR-0021-organic-maintenance-layer.md
architecture/decisions/DR-0022-organic-version-governance.md
architecture/decisions/DR-0023-operating-governance-and-maturity.md
architecture/decisions/DR-0024-installed-kora-project-usage.md
architecture/decisions/DR-0025-installed-project-registry.md
architecture/decisions/DR-0026-chrome-mcp-browser-ux-capability.md
architecture/decisions/DR-0027-reviewed-image-generation-pipeline.md
architecture/decisions/DR-0028-marketing-channel-integration-layer.md
```
