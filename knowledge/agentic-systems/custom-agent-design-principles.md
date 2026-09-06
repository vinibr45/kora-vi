---
title: "Custom Agent Design Principles"
type: framework
domain: "agentic-systems"
subdomain: "agents"
status: draft
version: "0.1"
evidence_level: internal_framework
sources:
  - docs/agents/kora-agents-spec-v0.5.md
related:
  - agents/templates/agent-template.md
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Custom Agent Design Principles

## Summary

A custom agent should exist only when a recurring objective benefits from a stable role, specialized judgment, permission boundary, or named responsibility owner.

## Core Idea

Design an agent around responsibility, not around a prompt idea.

An agent should define:

- purpose;
- scope;
- responsibilities;
- non-responsibilities;
- context access;
- allowed skills;
- allowed tools;
- required evals;
- permission boundaries;
- approval points;
- handoff rules.

The agent contract should be clear enough to guide behavior without becoming a huge hidden prompt.

## When To Use

- A recurring objective needs a stable owner.
- Several skills need to be coordinated under one role.
- Specialized judgment is required.
- Risk justifies a reviewer or specialist.
- A local project needs a role tailored to its market, stack, audience, or workflow.

## When Not To Use

- Direct execution is enough.
- A skill alone is enough.
- A tool alone is enough.
- The role is vague.
- It duplicates an existing agent.
- It would place project-specific behavior inside KORA Core.

## How To Apply

Use this design prompt:

```text
What objective does this agent own?
What decisions can it make?
What must it never decide alone?
What context can it read?
What skills can it use?
What tools can it call?
What outputs must it produce?
What approvals are required?
When should it hand off?
Should it be global, local, or hybrid?
```

Then classify placement:

```text
Reusable across projects -> KORA Core
Specific to one project -> local .kora/agents/
Reusable pattern with local adaptation -> hybrid
```

## Examples

Good custom agent:

```text
Proposal Reviewer: reviews commercial proposals for buyer clarity, scope clarity, risk, unsupported promises, and next-step quality.
```

Weak custom agent:

```text
Business Genius Agent: helps with everything in the business.
```

## Limitations

Too many agents create routing overhead. Prefer a skill when the task is procedural and does not need a named judgment owner.

## Sources

- `docs/agents/kora-agents-spec-v0.5.md`

## Related

- `agents/templates/agent-template.md`
- `skills/create-agent.md`
- `skills/review-agent.md`

