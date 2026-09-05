# classify-scope

## Purpose

Decide where information or capability should live.

This skill protects KORA Core from project-specific contamination.

## When To Use

- Before creating agents, skills, tools, evals, automations, memory, decisions, or knowledge.
- When deciding whether something is global, local, or hybrid.
- When a project-specific request may produce reusable knowledge or capability.

## Inputs

- Proposed content or capability.
- Task classification.
- Project binding, if any.
- Existing KORA Core structure.
- Existing local `.kora/` structure, if any.

## Process

1. Determine whether the item is reusable across projects.
2. Determine whether it depends on a specific project identity, audience, stack, repository, client, service, or operating rule.
3. Classify scope as global, local, or hybrid.
4. Recommend the storage location.
5. Identify whether human approval is needed before creating or moving the item.

## Outputs

- Scope classification: global, local, or hybrid.
- Recommended location.
- Reasoning.
- Boundary warnings if needed.

## Scope Rules

```text
Reusable across projects -> KORA Core
Specific to one project -> local .kora binding
Published/runtime code -> project repository
```

## Boundaries

This skill decides placement. It does not decide whether the work should be done at all.
