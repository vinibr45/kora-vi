---
name: "image-generation-provider"
external_system: "Image generation API, MCP connector, plugin, or local provider"
scope: hybrid
status: proposed
owner: "Marcos"
permission_level: read-write
related_tools:
  - image-generation
related_agents:
  - image-asset-reviewer
related_skills:
  - generate-image-asset
  - generate-reviewed-image-asset
related_evals:
  - EV-0015-reviewed-image-generation-loop
created_at: 2026-09-07
updated_at: 2026-09-07
---

# Image Generation Provider

## Purpose

Define how KORA can connect to an external or local image generation provider without locking the architecture to one vendor.

This integration can represent an API, MCP server, plugin, browser-assisted tool, CLI, or local runtime that creates or edits bitmap images.

## External System

Provider-specific.

Examples:

```text
OpenAI image API
Runway
Ideogram
Stability
Midjourney through an approved workflow
local image model
custom MCP image generator
```

## Scope

Hybrid.

The integration definition is reusable in KORA Core. Credentials, provider-specific account settings, project prompts, references, generated files, and approval records belong in the local project or secure runtime configuration.

## Access Requirements

- Provider account or local runtime, if needed.
- API key, OAuth connection, MCP server, plugin connection, or approved browser workflow.
- Permission to use any reference image supplied.
- Spending limit or credit policy when the provider is paid.

## Data Behavior

May send:

- prompt;
- negative constraints;
- aspect ratio or dimensions;
- approved reference images;
- editing instructions;
- model/provider options.

May receive:

- generated or edited bitmap image;
- provider metadata;
- seed or generation id when available;
- safety/filter status;
- usage or cost metadata when available.

## Permissions

Read-write capability for image generation only after provider access is approved.

This integration does not grant publishing, scheduling, sending, or deployment permission.

## Platform Constraints

Each provider may have different:

- content policy;
- model strengths and weaknesses;
- rate limits;
- cost/credit behavior;
- commercial use terms;
- reference image restrictions;
- output resolution and file format constraints.

When provider documentation is required, use official docs or the provider's active connector instructions.

## Fallback Mode

If provider access is missing or unavailable:

```text
create image brief only
prepare prompt for manual generation
use an already approved project asset
switch to another approved provider
pause for user approval
```

## Security And Privacy

- Do not store secrets in KORA Core.
- Do not upload private or sensitive references without approval.
- Do not send private customer, personal, financial, medical, or confidential project data unless explicitly authorized and necessary.
- Store project-specific output in the project repository, not in KORA Core.

## Approval Points

Ask before:

- connecting a provider account;
- using paid credits;
- uploading reference images;
- using protected brand or copyrighted assets;
- generating or editing private likenesses;
- writing outputs into external repositories if not already authorized.

## Related

- `tools/image-generation.md`
- `skills/generate-image-asset.md`
- `skills/generate-reviewed-image-asset.md`
- `agents/image-asset-reviewer.md`
- `automations/reviewed-image-generation-loop.md`
- `evals/scenarios/EV-0015-reviewed-image-generation-loop.md`
- `architecture/decisions/DR-0027-reviewed-image-generation-pipeline.md`
