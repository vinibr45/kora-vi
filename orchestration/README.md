# Orchestration

This directory defines how KORA coordinates tasks, context, agents, skills, tools, evals, approvals, execution modes, and learning.

No automated runtime orchestration is implemented in v0.6.

## Specification

```text
docs/orchestration/kora-orchestration-spec-v0.6.md
```

## Core Documents

```text
orchestration/capability-management.md
orchestration/templates/capability-plan-template.md
```

## Core Rule

```text
Orchestration coordinates.
Agents own roles.
Skills own procedures.
Tools execute capabilities.
Knowledge provides reusable concepts.
Project Context provides local truth.
Evals assess quality.
Learning decides what should persist.
```
