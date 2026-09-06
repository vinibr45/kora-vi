---
name: "Claude Design File Generation"
scope: hybrid
status: proposed
owner: "KORA Core"
trigger: "manual"
frequency: "on demand"
permission_level: external-write
related_agents:
  - agents/capability-router.md
  - agents/context-curator.md
related_skills:
  - skills/generate-design-files-with-claude.md
related_tools:
  - tools/claude-design-file-generation.md
related_evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Claude Design File Generation

## Purpose

Automate the repeatable workflow of turning a design or document brief into generated project files and finished PDFs through Claude Design or a Claude-based design workflow.

## Scope

Hybrid.

KORA Core owns the repeatable workflow definition. The target project owns project context, output paths, framework rules, brand rules, and final acceptance.

## Trigger

Manual trigger from a user request such as:

- "Generate design files with Claude."
- "Generate a PDF document with Claude Design."
- "Use Claude Design to create this page."
- "Turn this brief into files."
- "Automate this design generation workflow."

## Frequency

On demand.

This should not run on a schedule until the access mode, cost model, context boundaries, and stop conditions are proven.

## Workflow

1. Receive the user brief and identify the target project.
2. Run context selection for only the files and project facts needed.
3. Redact sensitive information.
4. Produce a Claude-ready design prompt.
5. Run the approved access mode:
   - API or connector mode when available and approved.
   - Browser-assisted mode when explicitly approved.
   - Manual export mode when no direct connector exists.
6. Collect generated output.
7. Validate file structure and requested formats.
8. For PDF requests, render the returned source into a local PDF and inspect the result for pagination, overflow, margins, and readability.
9. Write files into a preview, draft, or approved project directory.
10. Summarize generated files, risks, and required human decisions.
11. Record learning when the workflow reveals reusable prompt or integration improvements.

## Inputs

- User brief.
- Target project.
- Output directory.
- Target artifact types.
- PDF requirements when applicable: page size, orientation, margins, headers, footers, pagination, language, source format, and final filename.
- Design constraints.
- Approved Claude access mode.
- Overwrite policy.

## Outputs

- Claude prompt.
- Generated files or imported export files.
- Rendered PDF files and source files when requested.
- Review report.
- File list.
- Optional learning record or capability improvement proposal.

## External Side Effects

This automation may send selected context to Claude and may spend API credits if API mode is enabled.

It must not publish, deploy, subscribe, purchase, or change external account settings.

## Approval Points

Approval is required before:

- Enabling API, connector, or browser-assisted access.
- Sending sensitive project context externally.
- Spending paid credits.
- Overwriting files.
- Deploying or publishing.

## Stop Conditions

Stop and request review when:

- Claude access fails.
- Output is incomplete or invalid.
- The requested output path is unsafe.
- Sensitive context would need to be sent.
- The generated result conflicts with project conventions.
- The run would incur unexpected cost.

## Failure Handling

Preserve the generated prompt and any useful partial output. Return a concise failure report with the next required human decision.

## Evals

Run or simulate relevant project evals when available. Minimum checks:

- No secrets in prompt or output.
- Generated files match requested formats.
- PDFs render successfully and preserve the intended layout.
- Generated code is structurally valid.
- Files are placed in the correct project location.
- Existing files are not overwritten without approval.

## Logging And Results

Log the prompt summary, access mode, file outputs, and review status in the target project when the project has a KORA binding.

## Learning Behavior

Successful runs may produce reusable prompt patterns, eval improvements, project context updates, or integration refinements. Promote them only through the normal KORA learning process.

## Related

- `integrations/claude-design.md`
- `tools/claude-design-file-generation.md`
- `skills/generate-design-files-with-claude.md`
