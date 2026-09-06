---
title: "Product Discovery Basics"
type: framework
domain: "product"
subdomain: "discovery"
status: draft
version: "0.1"
evidence_level: internal_framework
sources: []
related: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Product Discovery Basics

## Summary

Product discovery reduces the risk of building the wrong thing by clarifying the user, problem, context, desired outcome, alternatives, and evidence before implementation.

## Core Idea

Before building, answer:

1. Who has the problem?
2. What situation creates the problem?
3. What outcome do they want?
4. What do they do today instead?
5. How painful or frequent is the problem?
6. What evidence supports this?
7. What is the smallest useful solution?

Discovery should turn uncertainty into testable assumptions.

## When To Use

- Before creating a new product, feature, workflow, dashboard, automation, or AI assistant.
- When users request a solution but the underlying problem is unclear.
- When deciding what belongs in an MVP.

## When Not To Use

- When the task is a clear bug fix or already validated requirement.
- When discovery would delay an urgent operational fix.
- When no user or business decision depends on the output.

## How To Apply

Create a short discovery brief:

```text
User:
Situation:
Problem:
Current alternative:
Desired outcome:
Evidence:
Assumptions:
Smallest useful solution:
Success signal:
```

Use the brief to decide whether to build, research more, prototype, or discard.

## Examples

Weak product request:

```text
Add an AI dashboard.
```

Better discovery frame:

```text
Sales managers need to see which leads are stuck because follow-up is slow, so the first version should surface lead age, owner, last contact, and next action.
```

## Limitations

Discovery does not remove all risk. It reduces avoidable waste and makes assumptions explicit.

## Sources

Internal KORA business framework.

## Related

- `knowledge/business-ai/ai-use-case-selection.md`

