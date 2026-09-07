---
name: "generate-reviewed-image-asset"
type: decision
scope: hybrid
status: draft
version: "0.1"
owner: "Marcos"
domains:
  - visual-assets
  - image-generation
  - quality-review
related_agents:
  - image-asset-reviewer
related_skills:
  - generate-image-asset
  - check-approval-needed
  - select-context
  - use-installed-kora
  - record-eval-result
required_knowledge: []
required_tools:
  - image-generation
evals:
  - EV-0015-reviewed-image-generation-loop
created_at: 2026-09-07
updated_at: 2026-09-07
---

# Generate Reviewed Image Asset

## Purpose

Generate image assets through an approved image provider and review each candidate until KORA can approve, reject, revise, or escalate the result.

This skill turns a simple request such as "gera uma imagem revisada para esse post" into a controlled loop:

```text
request -> context -> prompt -> generation -> review -> revision or approval -> organized output
```

## When To Use

- When the user asks KORA to generate an image and make sure it is good before using it.
- When the request says or implies "gera ate aprovar", "gera uma imagem revisada", "avalia a imagem", "se reprovar pede outra", or "aprova e organiza".
- When visual quality, brand fit, publication readiness, or output organization matters.
- When a project connected to KORA needs image candidates saved into the right local folders.

## When Not To Use

- When the user only wants a visual brief, not generation.
- When the image is a simple one-off and review does not matter.
- When a project-specific design system, brand asset, likeness, or copyrighted reference is needed but permission/context is missing.
- When the output should be code-native SVG, UI implementation, or design file generation instead of bitmap image generation.
- When publishing, scheduling, or external upload is the real task; that requires a separate workflow and approval.

## Inputs

- User image request.
- Target project and `.kora/binding.md`, when working inside or for a connected repository.
- Intended use and destination: post, ad, hero, thumbnail, mockup, product image, story, presentation, internal reference.
- Format requirements: aspect ratio, dimensions, transparent background, file type, naming convention.
- Project visual context: `.kora/image-rules.md`, `.kora/brand-visual-context.md`, approved references, audience, offer, tone, constraints.
- Provider or integration preference, if the user named one.
- Maximum iteration count, defaulting to 3 unless the user requests otherwise.

## Process

1. Route the request and identify whether this is Core-level, project-local, or hybrid work.
2. If inside a connected project, read `.kora/binding.md` and use `skills/use-installed-kora.md` behavior.
3. Check approval requirements before external account use, paid credits, sensitive references, likeness editing, or external writes.
4. Select only the needed context:

```text
KORA Core: image-generation tool, image review workflow, governance
Project local: brand rules, audience, destination, assets, examples
User request: purpose, format, subject, constraints
```

5. Create a concise generation brief:

```text
purpose
audience
subject
composition
style
brand constraints
text/no-text rule
aspect ratio
destination
negative constraints
approval needs
```

6. Use `skills/generate-image-asset.md` and `tools/image-generation.md` through the selected provider/integration.
7. Save or identify the candidate as an iteration, not as a final asset.
8. Ask `agents/image-asset-reviewer.md` to review the candidate using:

```text
request fit
brand fit
composition
technical quality
text readability
destination fit
safety and permissions
```

9. If approved, move or recommend the asset into the approved destination and write metadata.
10. If rejected, create a revision brief and generate another candidate until the maximum iteration count or a stop condition is reached.
11. If review needs human judgment, stop and summarize what requires approval.
12. Record eval or learning only when the result changes future behavior, reveals a recurring failure, or defines a useful prompt pattern.

## Outputs

- Final decision: approved, rejected after max attempts, needs human review, or blocked.
- Approved image path or recommended path.
- Candidate history.
- Final prompt or brief.
- Reviewer notes and pass/fail checklist.
- Metadata record for the final asset.
- Revision brief when not approved.

## Recommended Project Storage

Use project-local storage for project-specific assets:

```text
assets/images/generated/<asset-slug>/
  candidates/
  rejected/
  approved/
  metadata/
```

Use project `.kora/` for visual context and history:

```text
.kora/image-rules.md
.kora/brand-visual-context.md
.kora/image-generation-history.md
```

Do not store project-specific generated assets in KORA Core unless they are explicitly reusable examples.

## Required Knowledge

None required.

## Optional Knowledge

Project-local brand, marketing, audience, product, and content knowledge may improve review quality.

## Required Tools

```text
tools/image-generation.md
```

## Optional Tools

Provider-specific API, MCP connector, plugin, local script, or design tool integration defined through:

```text
integrations/image-generation-provider.md
```

## Evals

```text
evals/scenarios/EV-0015-reviewed-image-generation-loop.md
```

## Approval Points

Ask before:

- spending paid image generation credits;
- connecting or using an external provider account;
- uploading private references;
- using protected brand or copyrighted references;
- generating or editing private likenesses;
- publishing, scheduling, sending, or deploying images;
- increasing the iteration limit when cost or account usage is involved.

## Boundaries

This skill organizes generation and review. It does not guarantee legal clearance, brand ownership, platform ad approval, or human creative approval.

It must not loop forever. Use a default maximum of 3 iterations unless the user defines another limit.

It must not hide rejected iterations when they matter for traceability.

## Related

- `agents/image-asset-reviewer.md`
- `skills/generate-image-asset.md`
- `tools/image-generation.md`
- `integrations/image-generation-provider.md`
- `automations/reviewed-image-generation-loop.md`
- `evals/scenarios/EV-0015-reviewed-image-generation-loop.md`
- `architecture/decisions/DR-0027-reviewed-image-generation-pipeline.md`
