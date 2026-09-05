# record-decision

## Purpose

Record important decisions in a structured way.

This skill preserves architectural and project continuity without turning every conversation into memory.

## When To Use

- When a decision affects future work.
- When a decision changes architecture, scope, project direction, capability placement, tools, permissions, or operating rules.
- When the user explicitly says something should be remembered as a decision.
- When ambiguity would likely return later without a written decision.

## Inputs

- Decision statement.
- Context for the decision.
- Scope: architecture, project, knowledge, memory, agent, skill, tool, eval, automation, or governance.
- Owner.
- Date.
- Consequences.
- Related files or decisions.

## Process

1. Classify the decision scope.
2. Choose destination: `architecture/decisions/` or local `.kora/decisions/`.
3. Assign the next decision number.
4. Write context, decision, reasoning, consequences, and related references.
5. Mark status: proposed, accepted, superseded, or rejected.

## Outputs

- Decision record.
- Decision location.
- Status.
- Related references.

## Recommended Format

```text
Title
Status
Date
Scope
Owner

Context
Decision
Reasoning
Consequences
Related
```

## Boundaries

This skill does not decide everything by itself. Important decisions require user approval or clear user instruction.
