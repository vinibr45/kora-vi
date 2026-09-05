# generate-image-asset

## Purpose

Generate or propose image assets for KORA-supported projects using an approved image generation tool.

This skill helps KORA create images for content, websites, campaigns, mockups, thumbnails, illustrations, references, and visual concepts while preserving project-specific brand and approval boundaries.

## When To Use

- When the user asks to create, generate, edit, or propose an image.
- When a content, marketing, web, product, or design workflow needs visual assets.
- When a capability plan recommends image generation.
- When a project needs image ideas, image briefs, creative directions, or generated bitmap assets.

## When Not To Use

- When the task only needs text, strategy, or copy.
- When an existing project asset should be used without modification.
- When the required output is code-native SVG, HTML/CSS, icon system work, or vector editing better handled by project implementation.
- When the image would require using private likenesses, sensitive data, protected brand assets, or external copyrighted references without permission.
- When the user needs publishing or scheduling, which requires separate approval and workflow.

## Inputs

- User request.
- Target project and local `.kora/` binding, if relevant.
- Image purpose: post, story, website asset, mockup, ad, thumbnail, product image, illustration, etc.
- Format requirements: size, aspect ratio, transparency, style, quality, file type, destination.
- Project context: brand, audience, offer, tone, visual identity, constraints.
- Existing assets or references, if approved and available.
- Required approval points.

## Process

1. Classify the task and project.
2. Decide whether image generation is actually needed or whether an existing asset, screenshot, design tool, or manual brief is enough.
3. Select context:

```text
Global knowledge: design, marketing, content, UX, brand principles
Local context: project brand, audience, offer, tone, constraints, visual rules
Existing assets: approved references or source images
```

4. Identify whether the request is generation, editing, variation, upscaling, mockup, or visual direction.
5. Produce a concise image brief when needed:

```text
Purpose
Audience
Visual subject
Composition
Style
Brand constraints
Text/no-text requirement
Aspect ratio
Output destination
Negative constraints
Approval needs
```

6. Use the approved image generation tool only when generation or editing is appropriate.
7. Store or recommend storage location according to scope:

```text
Reusable generic asset or example -> KORA Core only if truly reusable
Project-specific generated asset -> project repository or local project asset folder
Project-specific image brief/context -> project `.kora/`
```

8. Apply evals or quality checks when image quality, brand fit, accessibility, readability, or publishing readiness matters.
9. Ask for approval before publishing, scheduling, external upload, paid generation, or account-connected workflows.

## Outputs

- Image brief, generated image asset, or image generation proposal.
- Recommended destination path.
- Context used.
- Tool used or recommended.
- Quality/eval notes.
- Approval notes.

## Required Tool

- `tools/image-generation.md`

## Related Skills

- `classify-task`
- `classify-scope`
- `select-context`
- `create-capability-plan`
- `assess-integration-need`
- `create-tool`
- `review-tool`
- `run-manual-eval`

## Approval Points

Ask before:

- using paid image generation credits when relevant;
- editing personal likenesses or sensitive images;
- using copyrighted or brand-protected references;
- publishing or scheduling generated images;
- writing assets into an external project repository when not already approved;
- connecting design, social, or publishing tools.

## Boundaries

This skill does not publish images, schedule posts, access social accounts, or create design-tool integrations by itself.

It should not store project-specific visual identity inside KORA Core.

It should not treat generated output as approved final creative without review.
