# Changelog

All meaningful KORA Core version changes are recorded here.

## 1.9.0 - 2026-09-17

Impact: minor

## Added

- `skills/create-version-change-wiki.md` for creating client-facing and technician-led wikis that explain version changes with a consistent index, HTML output, image placement, and support-oriented wording.

## Changed

- `COMECE-AQUI.md`, `CAPACIDADES.md`, `skills/README.md`, and `VERSION.md` now list the version-change wiki capability.

## Why It Matters

KORA can now preserve a repeatable documentation pattern for release/change wikis, including separate language for clients and technicians, while keeping internal implementation details out of client-facing articles.

## Related Decisions

```text
None.
```

## 1.8.0 - 2026-09-10

Impact: minor

## Added

- `skills/create-client-onboarding-wiki-package.md` for creating client-facing wiki and video packages, with one wiki article and one recording plan per screen or workflow.

## Changed

- `COMECE-AQUI.md`, `CAPACIDADES.md`, `skills/README.md`, and `VERSION.md` now list the client onboarding documentation package capability.

## Why It Matters

KORA can now help turn a loose product training request into a structured documentation backlog, recording checklist, script template, wiki template, review checklist, schedule, and blocker escalation flow while keeping product-specific content local.

## Related Decisions

```text
None.
```

## 1.7.0 - 2026-09-07

Impact: minor

## Added

- `agents/marketing-performance-analyst.md` for read-only marketing channel analysis across connected projects.
- `skills/analyze-marketing-performance.md` for analyzing authorized Analytics, Ads, Instagram, and future channel data.
- `integrations/google-analytics-data-api.md` for Google Analytics Data/Admin API boundaries.
- `tools/google-analytics-read-connector.md` as the proposed read-only GA4 reporting connector.
- `automations/marketing-channel-health-snapshot.md` for on-demand or approved recurring marketing health checks.
- `evals/scenarios/EV-0016-marketing-channel-integrations.md`.
- `architecture/decisions/DR-0028-marketing-channel-integration-layer.md`.

## Changed

- Existing Google Ads and Instagram definitions now link into the broader marketing channel layer.
- `AGENTS.md`, `COMECE-AQUI.md`, `CAPACIDADES.md`, folder READMEs, `README.md`, `VERSION.md`, `GOVERNANCA.md`, and `MATURIDADE.md` now recognize marketing-channel requests.

## Why It Matters

KORA can now support project-level marketing analysis from external channels without mixing credentials, storing raw account data in Core, or treating read access as permission to change campaigns, posts, tags, events, budgets, or messages.

## Related Decisions

```text
architecture/decisions/DR-0028-marketing-channel-integration-layer.md
```

## 1.6.0 - 2026-09-07

Impact: minor

## Added

- `agents/image-asset-reviewer.md` for reviewing generated image candidates and deciding approval, rejection, revision, or human-review need.
- `skills/generate-reviewed-image-asset.md` for the full request -> generation -> review -> revision -> approval -> organization loop.
- `integrations/image-generation-provider.md` as a provider-neutral API/MCP/plugin/local provider integration definition.
- `automations/reviewed-image-generation-loop.md` for the repeatable reviewed generation workflow.
- `evals/scenarios/EV-0015-reviewed-image-generation-loop.md`.
- `architecture/decisions/DR-0027-reviewed-image-generation-pipeline.md`.
- Governance and maturity notes for external provider use, paid credits, private references, and reviewed image approval.

## Changed

- `tools/image-generation.md` now recognizes the reviewed image generation workflow as an allowed caller.
- `AGENTS.md`, `COMECE-AQUI.md`, `CAPACIDADES.md`, folder READMEs, `README.md`, and `VERSION.md` now list the reviewed image generation capability.

## Why It Matters

KORA can now support image generation as a quality-controlled pipeline instead of a one-shot request. It can generate candidates through approved providers, evaluate them, request better versions when needed, and keep project-specific outputs organized locally.

## Related Decisions

```text
architecture/decisions/DR-0027-reviewed-image-generation-pipeline.md
```

## 1.5.0 - 2026-09-07

Impact: minor

## Added

- `agents/browser-ux-auditor.md` for reusable browser-based UX review.
- `skills/audit-ux-with-chrome-mcp.md` for page-by-page Chrome MCP UX audits.
- `integrations/chrome-mcp-browser-control.md` as the reusable integration definition for Chrome MCP browser control.
- `evals/browser-page-ux-readiness.md` for mobile, tablet and desktop UX readiness checks.
- `architecture/decisions/DR-0026-chrome-mcp-browser-ux-capability.md`.

## Changed

- `CAPACIDADES.md`, `agents/README.md`, `skills/README.md`, `integrations/README.md`, `evals/README.md` and `VERSION.md` now list the Chrome MCP browser UX capability.

## Why It Matters

KORA can now carry a reusable method for inspecting real web pages through Chrome MCP across projects, while keeping project-specific routes, credentials and product rules local.

## Related Decisions

```text
architecture/decisions/DR-0026-chrome-mcp-browser-ux-capability.md
```

## 1.4.0 - 2026-09-07

Impact: minor

## Added

- `projects/INSTALLED-KORA.md` as the central registry of repositories where KORA is installed.
- `skills/register-installed-kora-project.md` for registering or updating installed project entries.
- `architecture/decisions/DR-0025-installed-project-registry.md`.

## Changed

- `setup-kora-project` and `bind-project-to-kora` now require updating the installed-project registry.
- `check-installed-kora` now checks whether the project appears in `projects/INSTALLED-KORA.md`.
- `use-installed-kora` now checks the central installed-project registry when available.
- `AGENTS.md`, `COMECE-AQUI.md`, `CAPACIDADES.md`, `projects/README.md`, and `projects/PROJECT-FLOW.md` now point to the registry.

## Why It Matters

When KORA Core changes, there is now a central place to see which connected repositories may need local `.kora/`, `AGENTS.md`, or project documentation updates.

## Related Decisions

```text
architecture/decisions/DR-0025-installed-project-registry.md
```

## 1.3.0 - 2026-09-07

Impact: minor

## Added

- `skills/use-installed-kora.md` for using KORA from inside operational repositories that already have `.kora/binding.md`.
- `skills/check-installed-kora.md` for validating whether a repository is correctly connected to KORA.
- `projects/templates/local-agents-template.md` for local project `AGENTS.md` setup.
- `projects/templates/local-kora-readme-template.md` for local `.kora/README.md` setup.
- `examples/installed-kora-project.md` for realistic use from another repository.
- `architecture/decisions/DR-0024-installed-kora-project-usage.md`.

## Changed

- `setup-kora-project` and `bind-project-to-kora` now include local `AGENTS.md`, `.kora/README.md`, and installed-KORA checks.
- `projects/PROJECT-FLOW.md` now explains how connected repositories should use `.kora/binding.md`, local `AGENTS.md`, and KORA Core.
- `AGENTS.md`, `COMECE-AQUI.md`, and `CAPACIDADES.md` now route requests such as "usa a KORA nesse projeto" and "verifica a instalacao da KORA".
- `MATURIDADE.md` and `GOVERNANCA.md` now include installed-KORA usage and project-to-Core safety boundaries.

## Why It Matters

KORA can now be used more naturally inside other repositories after installation. A connected project can keep its own reality local while still using KORA Core as a reusable method library.

## Related Decisions

```text
architecture/decisions/DR-0024-installed-kora-project-usage.md
```

## 1.2.0 - 2026-09-07

Impact: minor

## Added

- `skills/run-daily-operating-loop.md` for natural daily work sessions.
- `skills/capture-loose-idea.md` for classifying informal ideas before over-structuring them.
- `skills/detect-capability-gap.md` for noticing when KORA needs a missing capability.
- `skills/check-approval-needed.md` for human-control and approval decisions.
- `MATURIDADE.md` as a maturity map for KORA capabilities.
- `GOVERNANCA.md` as a practical approval and safety guide.
- Examples for daily operating loops, loose idea capture, capability gaps, and approval checks.
- `architecture/decisions/DR-0023-operating-governance-and-maturity.md`.

## Changed

- `AGENTS.md` now recognizes natural requests such as "vamos rodar o dia", "tive uma ideia", "isso esta repetitivo", and "precisa de aprovacao?".
- `COMECE-AQUI.md` now includes daily operation, idea capture, gap detection, approval checks, maturity, and governance.
- `CAPACIDADES.md` now lists the new operating and governance capabilities.
- Maintenance guidance now includes maturity and governance files.
- Health-check guidance now includes version, maturity, and governance files.

## Why It Matters

KORA can now support everyday use more naturally, turn loose thinking into the right artifact, notice missing capabilities, and protect human approval boundaries before actions become risky.

## Related Decisions

```text
architecture/decisions/DR-0023-operating-governance-and-maturity.md
```

## 1.1.0 - 2026-09-07

Impact: minor

## Added

- `AGENTS.md` for agent-facing repository behavior.
- `COMECE-AQUI.md` as the human-facing practical entry point.
- `CAPACIDADES.md` as the living capability index.
- `skills/route-user-request.md` for natural-language request routing.
- `skills/maintain-kora-indexes.md` for organic maintenance of indexes, entry points, examples, and project guides.
- `automations/kora-index-maintenance.md` as the proposed recurring maintenance loop.
- `skills/check-kora-health.md` for KORA Core health checks.
- `evals/scenarios/EV-0014-kora-health-check.md` for validating health-check behavior.
- `skills/assess-kora-version-impact.md` for deciding whether changes deserve versioning.
- `skills/release-kora-version.md` for updating version records.
- `VERSION.md` for current KORA version state.
- `CHANGELOG.md` for durable version history.
- `projects/PROJECT-FLOW.md` for Core-vs-project workflow guidance.
- `examples/` with realistic usage examples.
- `architecture/decisions/DR-0021-organic-maintenance-layer.md`.
- `architecture/decisions/DR-0022-organic-version-governance.md`.

## Changed

- `README.md` now points to practical entry points, health checks, maintenance, versioning, examples, and agent instructions.
- `AGENTS.md` now instructs the agent to route natural requests, maintain indexes after durable changes, check KORA health, and assess version impact.
- `COMECE-AQUI.md` now includes quick routes for maintenance, health checks, and versioning.
- `CAPACIDADES.md` now includes maintenance, health, and version governance capabilities.
- Folder README files now list new durable skills, automations, evals, and project-flow references.

## Why It Matters

KORA is easier to use without naming internal concepts, easier to keep current as it evolves, easier to audit for consistency, and now has a lightweight governance loop for deciding when improvements deserve a new version.

## Related Decisions

```text
architecture/decisions/DR-0021-organic-maintenance-layer.md
architecture/decisions/DR-0022-organic-version-governance.md
```
