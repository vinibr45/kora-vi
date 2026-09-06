---
title: "Context Selection Principles"
type: framework
domain: "agentic-systems"
subdomain: "context"
status: draft
version: "0.1"
evidence_level: internal_framework
sources:
  - context/README.md
  - docs/orchestration/kora-orchestration-spec-v0.6.md
related:
  - skills/select-context.md
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Context Selection Principles

## Summary

Context selection is the discipline of choosing only the information needed for a task, from the right source of truth, at the right level of detail.

It prevents agents from loading everything, mixing local facts with global knowledge, or acting from stale assumptions.

## Core Idea

Context is not knowledge by itself. It is a task-specific working set assembled from:

- user input;
- reusable knowledge;
- architecture decisions;
- project context;
- project memory;
- repository files;
- previous outputs;
- external data when approved.

The context layer selects and assembles. It does not own the facts it selects.

## When To Use

- Before any complex task.
- Before using an agent or subagent.
- Before creating project-specific outputs.
- Before writing memory, knowledge, decisions, or files.
- Before connecting external systems.

## When Not To Use

- When the answer is tiny and all needed context is already in the current message.
- When the user explicitly asks for a quick answer and risk is low.

## How To Apply

Use this selection sequence:

1. Identify the task type.
2. Identify the project, if any.
3. Identify the decision or output required.
4. Select global knowledge only if it helps the task.
5. Select local project context only if the task belongs to that project.
6. Select memory only when operational history matters.
7. Select source files only when implementation or evidence requires them.
8. Exclude secrets, irrelevant data, and broad dumps.

## Examples

For a commercial proposal:

```text
Use: proposal structure, offer clarity, buyer context, scope, pricing rules.
Avoid: unrelated architecture docs, unrelated memory, all repository files.
```

For agent creation:

```text
Use: agent spec, capability plan, existing agents, task recurrence, permission needs.
Avoid: project-specific facts unless the agent is local or hybrid.
```

## Limitations

Under-selecting context can cause weak output. Over-selecting context can cause confusion, privacy risk, and slower reasoning.

## Sources

- `context/README.md`
- `docs/orchestration/kora-orchestration-spec-v0.6.md`

## Related

- `skills/select-context.md`
- `agents/context-curator.md`

