# Agents

This directory contains KORA Core agent definitions.

An agent is a goal-oriented entity with a defined role, scope, context access, skill access, tool permissions, and output responsibilities.

In v0.1, these are architectural definitions, not executable automations.

## Initial Core Agents

- `kora-architect.md`: protects and evolves the KORA architecture.
- `capability-router.md`: decides whether to execute directly, use a capability, or create/propose a new one.
- `project-binder.md`: connects project repositories to KORA through local `.kora/` bindings.
- `context-curator.md`: selects and assembles relevant context for a task.
- `knowledge-steward.md`: organizes reusable knowledge and protects knowledge boundaries.
