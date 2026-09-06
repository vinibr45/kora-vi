---
name: "claude-design-file-generation"
type: tool
scope: hybrid
status: proposed
owner: "KORA Core"
permission_level: external-write
allowed_callers:
  - skills/generate-design-files-with-claude.md
related_agents:
  - agents/capability-router.md
  - agents/context-curator.md
related_skills:
  - skills/generate-design-files-with-claude.md
related_evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Claude Design File Generation

## Purpose

Generate or import design-related files through a Claude-based design workflow, with explicit support for PDF-ready document generation.

This tool represents the executable capability that may later call an API, use an MCP connector, drive an approved browser workflow, or process exported files from Claude Design. For PDFs, Claude should normally generate a renderable source format, and KORA should render, save, and verify the final PDF locally.

## Scope

Hybrid.

The tool definition is reusable in KORA Core, but actual file destinations, brand context, framework constraints, and approval rules belong to the target project.

## Inputs

- Project identifier or local project binding.
- Design brief.
- Target artifact types.
- Target framework or file format.
- PDF requirements when applicable: page size, orientation, margins, pagination, headers, footers, brand rules, language, and source format.
- Brand, product, and audience constraints.
- Output directory.
- Overwrite policy.
- External access mode: API, connector, browser-assisted, or manual export.

## Outputs

- Generated files.
- PDF-ready source files such as HTML/CSS, Markdown, LaTeX, or structured JSON.
- Rendered `.pdf` files when the workflow includes local rendering.
- Importable design specs.
- Implementation notes.
- Asset prompts or asset references.
- Review report describing what was generated and what still needs human decision.

## Allowed Callers

- `skills/generate-design-files-with-claude.md`
- Approved project-specific design or build skills.
- Approved automations that explicitly reference this tool.

## Required Permissions

- External service access if API, connector, or browser-assisted mode is used.
- Local project write access for generated files.
- Human approval for overwrites, paid usage, sensitive context transfer, and publication.

## Safety Constraints

- Do not send secrets or credentials to Claude.
- Do not write directly into production paths without review.
- Do not overwrite existing files unless the overwrite policy permits it.
- Keep generated files in the project repository, not in KORA Core.
- Prefer preview or staging directories for first-pass generations.

## Failure Modes

- Claude access is unavailable.
- API or connector support is missing.
- Generated output is incomplete or invalid.
- PDF rendering fails, pages overflow, fonts are missing, or visual layout does not match the brief.
- Returned code does not match the target framework.
- Exported files cannot be parsed.
- Local write path is missing or unsafe.

When failure occurs, the workflow should preserve the prompt, partial outputs when useful, and a concise failure note.

## Approval Points

- Account connection.
- API key use.
- Paid generation.
- Sensitive context sharing.
- File overwrite.
- Production deployment.

## Related

- `integrations/claude-design.md`
- `skills/generate-design-files-with-claude.md`
- `automations/claude-design-file-generation.md`
