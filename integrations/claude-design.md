---
name: "Claude Design"
external_system: "Claude / Anthropic design-generation workflow"
scope: hybrid
status: proposed
owner: "KORA Core"
permission_level: external-write
related_tools:
  - tools/claude-design-file-generation.md
related_agents:
  - agents/capability-router.md
  - agents/context-curator.md
related_skills:
  - skills/generate-design-files-with-claude.md
related_evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Claude Design

## Purpose

Connect KORA to a Claude-based design-generation workflow so KORA can turn a project brief into design artifacts and implementation files.

The intended use is to automate generation of files such as PDF-ready document sources, HTML, CSS, component code, design specs, content drafts, asset prompts, and structured implementation notes, while keeping KORA responsible for context selection, review, storage, rendering, and project boundaries.

## External System

Claude / Anthropic design-generation workflow.

The exact product surface, API route, export format, and terms must be checked against current official Anthropic documentation before real implementation.

## Scope

Hybrid.

KORA Core defines the integration pattern, permissions, approval points, and fallback modes. Each bound project defines local design context, brand rules, output directories, target framework, and implementation constraints.

## Access Requirements

- Anthropic account or Claude account with access to the required design workflow.
- API key, MCP connector, browser session, export workflow, or another approved access method.
- Clear project brief and target output format.
- Local project write permissions for generated files.
- Human approval before storing credentials, spending API credits, publishing generated work, or overwriting project files.

## Data Behavior

KORA may send selected project context, briefs, brand constraints, screenshots, source snippets, and output requirements to Claude.

KORA may receive design specs, generated code, copy, structured JSON, PDF-ready HTML/CSS, Markdown, LaTeX, asset prompts, or exported files.

KORA should store generated outputs in the target project, not in KORA Core, unless the output is a reusable capability definition, eval, integration note, or learning record. For PDFs, KORA should preserve both the final `.pdf` and the source used to render it when practical.

## Permissions

External-write.

The integration may send data to an external service and may produce files that are written into a local project. It must not publish, deploy, purchase, subscribe, or change account settings without explicit approval.

## Platform Constraints

- Current official Claude / Anthropic documentation must be checked before implementation.
- Generated documents, code, and assets require review before production use.
- API availability, model support, export formats, file attachments, rate limits, and pricing may change.
- If the design workflow only exists in a UI, automation may require a browser-assisted or manual export mode.

## Fallback Mode

Assisted export mode:

1. KORA prepares a structured Claude Design prompt from selected project context.
2. The user runs it in Claude Design or an available Claude UI.
3. The user exports, copies, or downloads the result.
4. KORA imports the returned files or text.
5. KORA reviews, organizes, and writes approved files to the project.

## Security And Privacy

- Do not send secrets, private credentials, customer data, or unpublished sensitive business context unless explicitly approved.
- Redact environment variables, API keys, tokens, and private operational data.
- Store credentials only in an approved secret manager or environment variable, never in KORA markdown files.
- Record what categories of context are sent externally when the workflow becomes active.

## Approval Points

Human approval is required before:

- Connecting a Claude / Anthropic account.
- Storing or using an API key.
- Sending sensitive project context externally.
- Spending paid API credits.
- Writing generated files over existing project files.
- Publishing or deploying generated work.

## Related

- `tools/claude-design-file-generation.md`
- `skills/generate-design-files-with-claude.md`
- `automations/claude-design-file-generation.md`
