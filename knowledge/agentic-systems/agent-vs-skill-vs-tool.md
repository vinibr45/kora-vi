---
title: "Agent Vs Skill Vs Tool"
type: framework
domain: "agentic-systems"
subdomain: "capability-design"
status: draft
version: "0.1"
evidence_level: internal_framework
sources:
  - docs/agents/kora-agents-spec-v0.5.md
  - docs/skills/kora-skills-spec-v0.4.md
  - docs/orchestration/kora-orchestration-spec-v0.6.md
related:
  - orchestration/capability-management.md
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Agent Vs Skill Vs Tool

## Summary

KORA should distinguish agents, skills, and tools before creating new capabilities.

Confusing these three creates bloated agents, vague skills, unsafe tools, and unclear responsibilities.

## Core Idea

Use this separation:

```text
Agent = role and judgment.
Skill = repeatable procedure.
Tool = execution capability.
```

An agent decides and acts within a role. A skill defines how a task should be done. A tool performs an operation, such as reading a file, calling an API, generating an image, rendering a PDF, querying a database, or publishing externally.

## When To Use

- Before creating a new agent, skill, tool, integration, or automation.
- When a task feels complex but the right capability type is unclear.
- When an existing agent is becoming too large or procedural.
- When a skill is starting to include permissions or external execution details.

## When Not To Use

- When the user gave a tiny one-off task that can be executed directly.
- When a capability plan has already classified the needed structure.

## How To Apply

Ask:

1. Does this need a stable role with judgment and boundaries?
   - Create or use an agent.
2. Does this need a reusable step-by-step procedure?
   - Create or use a skill.
3. Does this need to execute an external or local capability?
   - Create or use a tool.
4. Does this need account access or a third-party system?
   - Define an integration.
5. Does this need repeated unattended execution?
   - Define an automation after the workflow is stable.

## Examples

Content Strategist:

```text
Agent: owns content strategy judgment.
Skill: create weekly content calendar.
Tool: generate image assets or schedule posts.
```

PDF Proposal Generator:

```text
Agent: proposal reviewer or sales specialist.
Skill: create commercial proposal.
Tool: render PDF.
```

## Limitations

Some capabilities are hybrid. In those cases, keep the reusable pattern in KORA Core and project-specific adaptation in the local `.kora/` binding.

## Sources

- `docs/agents/kora-agents-spec-v0.5.md`
- `docs/skills/kora-skills-spec-v0.4.md`
- `docs/orchestration/kora-orchestration-spec-v0.6.md`

## Related

- `knowledge/agentic-systems/custom-agent-design-principles.md`
- `knowledge/agentic-systems/capability-routing-heuristics.md`

