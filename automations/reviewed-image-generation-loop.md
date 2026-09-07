---
name: "reviewed-image-generation-loop"
scope: hybrid
status: proposed
owner: "Marcos"
trigger: "manual user request"
frequency: "on demand"
permission_level: read-write
related_agents:
  - image-asset-reviewer
related_skills:
  - generate-reviewed-image-asset
  - generate-image-asset
  - check-approval-needed
related_tools:
  - image-generation
related_evals:
  - EV-0015-reviewed-image-generation-loop
created_at: 2026-09-07
updated_at: 2026-09-07
---

# Reviewed Image Generation Loop

## Purpose

Represent the repeatable workflow where KORA generates an image candidate, reviews it, revises the prompt if needed, and organizes the approved result.

## Scope

Hybrid.

The workflow definition is global. Project-specific context, references, prompts, candidates, approvals, and final assets stay in the connected project repository.

## Trigger

Manual natural-language request, such as:

```text
Gera uma imagem revisada para esse post.
Gera ate aprovar.
Cria uma imagem e avalia antes de separar.
Revisa essa imagem e, se reprovar, pede outra.
```

## Frequency

On demand.

This is not a background job by default.

## Workflow

1. Read the user request and target project context.
2. Check approval needs for provider access, paid credits, sensitive references, likenesses, or external writes.
3. Build the image brief and generation prompt.
4. Generate a candidate through `tools/image-generation.md` and the selected provider integration.
5. Store or identify the candidate in an iteration-safe location.
6. Review the candidate through `agents/image-asset-reviewer.md`.
7. If approved, organize the final asset and metadata.
8. If rejected, create a revision brief and repeat until approved, blocked, or max iterations reached.
9. Summarize the final status and paths.

## Inputs

- User request.
- Project binding and local visual context.
- Provider/integration availability.
- Generation constraints and destination requirements.
- Maximum iteration count, default 3.

## Outputs

- Approved asset or clear failure summary.
- Candidate and rejected iteration records.
- Metadata file or recommended metadata content.
- Review decision and revision notes.
- Optional eval result when the workflow is being tested.

## External Side Effects

May call external image generation services if approved.

May consume paid credits if approved.

May write files into a project repository if the user has authorized project work.

Does not publish, schedule, deploy, or send final images.

## Approval Points

Approval is required before:

- first use of a provider account;
- paid or credit-consuming generation;
- sensitive/private reference upload;
- likeness generation or editing;
- publishing, scheduling, sending, or deploying;
- running with more than the agreed iteration limit when cost is involved.

## Stop Conditions

Stop when:

- a candidate is approved;
- max iterations are reached;
- required context is missing;
- provider access fails;
- safety or permission risk appears;
- human review is required.

## Failure Handling

If generation fails, retry only when failure is transient and within approval/cost limits.

If image quality repeatedly fails, return a clear diagnosis and a recommended next prompt or provider change.

If local brand context is missing, ask for or create project-local visual context before continuing.

## Evals

```text
evals/scenarios/EV-0015-reviewed-image-generation-loop.md
```

## Logging And Results

Project-specific runs should be stored locally:

```text
.kora/image-generation-history.md
assets/images/generated/<asset-slug>/metadata/
```

Core eval results should be stored in `evals/results/` only when testing the capability itself.

## Learning Behavior

Successful prompt patterns, recurring failure modes, and useful review criteria may become learning records or project-local image rules after review.

Do not automatically promote one project's visual preference into KORA Core.

## Related

- `skills/generate-reviewed-image-asset.md`
- `agents/image-asset-reviewer.md`
- `tools/image-generation.md`
- `integrations/image-generation-provider.md`
- `evals/scenarios/EV-0015-reviewed-image-generation-loop.md`
- `architecture/decisions/DR-0027-reviewed-image-generation-pipeline.md`
