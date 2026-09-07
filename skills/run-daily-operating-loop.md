# run-daily-operating-loop

## Purpose

Run a simple daily operating loop with KORA.

This skill helps the user turn open projects, loose priorities, recurring work, and possible AI-assisted tasks into a focused plan for the day.

## When To Use

- When the user says "vamos rodar o dia", "organiza meu dia", "o que devo priorizar hoje", or similar.
- At the start of a work session.
- When multiple projects, ideas, or pending tasks compete for attention.
- When the user wants KORA to identify which tasks should be executed directly, planned, delegated to a skill, or turned into learning.

## When Not To Use

- When the user asks for one narrow task and no prioritization is needed.
- When calendar, email, task manager, or external account access is required but not available or approved.
- When the user needs a full business strategy review rather than a daily loop.

## Inputs

- User priorities or open loops.
- Active project context, if provided.
- Known KORA project registry.
- Recent decisions, learning, evals, or outputs, if relevant.
- Available time, deadlines, constraints, and energy level, if provided.

## Process

1. Identify today's intended outcome.
2. List active projects or workstreams mentioned by the user.
3. Select only the context needed for those workstreams.
4. Classify tasks:

```text
do now
plan
delegate to skill
needs context
needs approval
record learning
defer
```

5. Identify likely KORA routes for the top tasks.
6. Recommend a small execution sequence.
7. Capture any loose ideas or capability gaps that appear.
8. End with the next concrete action.

## Outputs

- Daily focus summary.
- Prioritized task list.
- Suggested KORA route for each important item.
- Approval or missing-context warnings.
- Next action.

## Boundaries

This skill does not read calendars, email, task managers, or external systems unless an approved integration is explicitly part of the task.

It should not turn every daily note into durable memory. Use `record-learning` only when future decisions benefit.

## Related

```text
skills/route-user-request.md
skills/select-context.md
skills/capture-loose-idea.md
skills/detect-capability-gap.md
skills/check-approval-needed.md
```
