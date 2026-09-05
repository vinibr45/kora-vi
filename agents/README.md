# Agents

This directory contains KORA Core agent definitions.

An agent is a goal-oriented entity with a defined role, scope, context access, skill access, tool permissions, and output responsibilities.

In v0.5, these are structured agent contracts, not autonomous runtime workers.

## Initial Core Agents

- `kora-architect.md`: protects and evolves the KORA architecture.
- `capability-router.md`: decides whether to execute directly, use a capability, or create/propose a new one.
- `project-binder.md`: connects project repositories to KORA through local `.kora/` bindings.
- `context-curator.md`: selects and assembles relevant context for a task.
- `knowledge-steward.md`: organizes reusable knowledge and protects knowledge boundaries.
- `kora-guide.md`: explains how to use KORA and routes users to the right workflow.

## Template

```text
agents/templates/agent-template.md
```

## Specification

```text
docs/agents/kora-agents-spec-v0.5.md
```

