# detect-capability-gap

## Purpose

Detect when KORA is missing a capability needed to handle work well.

This skill identifies gaps during use, especially when tasks feel repetitive, unclear, risky, manually heavy, or improvised.

## When To Use

- When the user says "isso esta repetitivo", "esta faltando algo", "isso ficou trabalhoso", or similar.
- After a task required repeated manual judgment that could become a skill.
- After a health check, eval, experiment, or failed execution reveals missing support.
- Before creating a new capability, to decide what kind is actually needed.

## When Not To Use

- When an existing capability clearly covers the task.
- When the issue is just missing project context.
- When the user only wants direct execution and the gap is not blocking.

## Inputs

- Task or pain point.
- Capabilities already used.
- Existing agents, skills, tools, integrations, automations, evals, and knowledge.
- Recurrence likelihood.
- Risk level.
- Scope: global, local, hybrid, or unknown.

## Process

1. Describe the friction or failure.
2. Check whether missing context explains the issue.
3. Check whether an existing KORA capability already covers it.
4. Classify the gap:

```text
knowledge
project context
skill
agent
tool
integration
automation
eval
experiment
decision
```

5. Classify scope.
6. Decide urgency:

```text
now
soon
later
do not create
```

7. Recommend the smallest useful capability.
8. If justified, route to `create-capability-plan` or the specific `create-*` skill.

## Outputs

- Gap diagnosis.
- Existing capability check.
- Recommended capability type.
- Recommended location.
- Urgency.
- Next action.

## Boundaries

This skill detects and recommends gaps. It does not create new capabilities unless paired with the relevant creation skill.

Automation should be recommended only after the workflow is stable and approval points are clear.

## Related

```text
skills/review-capability-gaps.md
skills/create-capability-plan.md
skills/create-capability.md
skills/classify-scope.md
skills/check-approval-needed.md
```
