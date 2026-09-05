---
name: "image-generation"
type: tool
scope: global
status: proposed
owner: "Marcos"
permission_level: read-only
allowed_callers:
  - generate-image-asset
related_agents: []
related_skills:
  - generate-image-asset
related_evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# image-generation

## Purpose

Provide an approved image generation or image editing capability for KORA workflows.

This tool definition represents the capability, not a specific provider lock-in.

## Scope

Global.

Project-specific prompts, brand rules, assets, and outputs should live in the local project context or project repository.

## Inputs

- Image generation prompt or editing instruction.
- Optional approved reference images.
- Output purpose.
- Aspect ratio or size requirements.
- Style and brand constraints.
- Destination notes.

## Outputs

- Generated or edited bitmap image.
- Optional prompt or brief used to generate it.
- Notes about limitations, review needs, or destination.

## Allowed Callers

- `skills/generate-image-asset.md`
- Future approved design, marketing, content, or web asset skills.

## Required Permissions

Depends on the implementation/provider.

KORA must check whether the selected image tool requires credits, paid account access, uploaded references, or external service permissions.

## Safety Constraints

- Do not use private likenesses without permission.
- Do not use sensitive personal data in prompts.
- Do not assume copyrighted or brand-protected references are allowed.
- Do not publish or schedule generated images without explicit approval.
- Do not store project-specific assets in KORA Core unless they are reusable examples and approved.

## Failure Modes

- Output does not match prompt.
- Text in generated image is distorted or unusable.
- Brand style is wrong.
- Aspect ratio or composition is wrong.
- Output is unsuitable for publication.
- Tool/provider is unavailable.
- Required reference image is missing.

Fallbacks:

```text
revise prompt
create image brief only
use existing project assets
use design tool manually
ask for reference images
switch provider/tool if available
```

## Approval Points

Ask before:

- using paid credits or external accounts;
- uploading sensitive/private images;
- editing likenesses;
- publishing, sending, scheduling, or deploying generated images;
- writing generated assets to external repositories when not already approved.

## Related

- `skills/generate-image-asset.md`
- `docs/tools/kora-tools-integrations-automations-spec-v0.9.md`
- `tools/templates/tool-template.md`
