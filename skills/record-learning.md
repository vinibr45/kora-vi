# record-learning

## Purpose

Record a structured learning recommendation from a task, eval, experiment, result, or user feedback.

This skill complements `promote-learning` by creating a concise learning record when persistence or future review is useful.

## When To Use

- After an experiment has results.
- After an eval produces findings.
- After repeated user feedback reveals a pattern.
- When a result may affect future decisions but should not be immediately promoted.
- When evidence is weak or moderate and needs review.

## When Not To Use

- For raw conversation logs.
- For facts that should go directly into project context.
- For accepted architectural decisions; use `record-decision`.
- For reusable knowledge entries; use `create-knowledge-entry`.
- For low-value noise.

## Inputs

- Source task, eval, experiment, or feedback.
- Learning statement.
- Scope classification.
- Evidence strength.
- Destination recommendation.
- Related files, decisions, memory, knowledge, agents, skills, tools, or evals.

## Process

1. Summarize what was learned.
2. Classify scope: global, local, hybrid, or none.
3. Classify evidence strength: weak, moderate, strong, or inconclusive.
4. Recommend destination: no persistence, memory, decision, knowledge, capability update, or project context update.
5. Identify limitations.
6. Identify approval requirements.
7. Create a learning record only if it will help future decisions.

## Outputs

- Learning record.
- Destination recommendation.
- Evidence strength.
- Approval requirement.
- Related references.

## Boundaries

This skill records learning recommendations. It does not automatically change source-of-truth stores.

Use `promote-learning` before converting learning into memory, knowledge, decisions, or capability changes.
