---
name: "generate-design-files-with-claude"
type: execution
scope: hybrid
status: proposed
version: "0.1"
owner: "KORA Core"
domains:
  - design
  - software
  - content
related_agents:
  - agents/capability-router.md
  - agents/context-curator.md
related_skills:
  - skills/select-context.md
  - skills/assess-integration-need.md
  - skills/review-tool.md
required_knowledge: []
required_tools:
  - tools/claude-design-file-generation.md
evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Generate Design Files With Claude

## Purpose

Help KORA turn a project brief into design, implementation, and PDF-ready document files through a Claude-based design workflow.

The skill keeps KORA responsible for context selection, prompt structure, file placement, PDF rendering, review, and learning, while Claude handles design generation when approved access exists.

## When To Use

- The user wants to generate design files, page layouts, interface drafts, or implementation-ready artifacts with Claude.
- The user wants Claude to generate documents that become finished PDF files.
- A project needs HTML, CSS, component code, copy, design specs, or asset prompts from a design brief.
- The workflow should be repeatable and eventually automatable.

## When Not To Use

- The task can be completed directly inside the local project without external design generation.
- The user has not approved sending project context to an external system.
- The project contains sensitive material that cannot be safely summarized or redacted.
- The desired output requires a different design tool, such as Canva, Figma, or a local renderer.

## Inputs

- User design goal.
- Bound project context.
- Brand, audience, offer, and product constraints.
- Target file types.
- PDF requirements when applicable: document type, page size, orientation, margins, headers, footers, pagination, language, brand rules, and whether source should be HTML/CSS, Markdown, LaTeX, or another renderable format.
- Output path.
- Access mode: API, connector, browser-assisted, or manual export.
- Approval for external context transfer when needed.

## Process

1. Classify the task and confirm the target project.
2. Select only the context required for the design task.
3. Redact secrets, credentials, and sensitive operational data.
4. Build a structured Claude Design prompt with project context, design requirements, PDF requirements when applicable, file requirements, and acceptance criteria.
5. Use `tools/claude-design-file-generation.md` if an approved access mode exists.
6. If no access mode exists, use assisted export mode and ask the user to provide the Claude output.
7. Validate the returned files against the requested format and project conventions.
8. For PDF requests, render the approved source into a PDF and visually review page layout, overflow, margins, and readability.
9. Write approved source files and final PDFs to the target project.
10. Record useful learning, prompt improvements, or capability gaps when appropriate.

## Outputs

- Structured Claude Design prompt.
- Generated or imported design files.
- PDF-ready source and final `.pdf` output when requested.
- Review notes.
- List of files created or modified.
- Follow-up recommendations for implementation or evaluation.

## Required Knowledge

None by default. Project-specific brand, product, and audience context should come from the project binding.

## Optional Knowledge

- Reusable design principles.
- Marketing positioning knowledge.
- Project-specific UI conventions.

## Required Tools

- `tools/claude-design-file-generation.md`

## Optional Tools

- Image generation tools for visual assets.
- Browser or screenshot tools for visual QA.
- Local test or build commands for generated code.
- Local PDF rendering and inspection tools.

## Evals

Apply relevant project evals when available. At minimum, review:

- File validity.
- PDF layout quality when applicable.
- Visual fit with the project.
- Brand consistency.
- Accessibility basics.
- No secret leakage.
- No unapproved external writes.

## Approval Points

Human approval is required before:

- Sending sensitive context externally.
- Using paid API credits.
- Connecting accounts.
- Overwriting existing project files.
- Publishing or deploying generated outputs.

## Boundaries

This skill does not grant Claude account access, store credentials, publish generated work, or bypass project review.

## Related

- `integrations/claude-design.md`
- `tools/claude-design-file-generation.md`
- `automations/claude-design-file-generation.md`
