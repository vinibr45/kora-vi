# capture-loose-idea

## Purpose

Capture a loose idea and decide what it should become in KORA.

This skill turns informal thoughts, observations, "maybe we should" ideas, and half-formed workflows into the right next container without over-structuring too early.

## When To Use

- When the user says "tive uma ideia", "percebi uma coisa", "isso poderia virar algo", or similar.
- When an idea may become knowledge, learning, a decision, an experiment, a skill, an automation, a project note, or no durable artifact.
- When the user wants to preserve an idea but is unsure where it belongs.

## When Not To Use

- When the user already knows the exact artifact to create.
- When the idea is private, sensitive, or project-specific and should stay local.
- When the idea is too vague to classify and the user only wants to brainstorm.

## Inputs

- The idea or observation.
- Source context.
- Project context, if any.
- Evidence strength.
- Recurrence or reuse expectation.
- Risk or approval concerns.

## Process

1. Restate the idea plainly.
2. Identify whether it is:

```text
raw note
learning
knowledge
decision
experiment
skill
agent
tool
integration
automation
project context
capability gap
```

3. Classify scope as global, local, hybrid, or none.
4. Check evidence strength:

```text
weak
moderate
strong
unknown
```

5. Recommend the smallest useful destination.
6. Create or update an artifact only when the idea is useful enough to persist.
7. If the idea may affect future behavior, recommend learning, decision, or version impact assessment.

## Outputs

- Idea classification.
- Recommended destination.
- Scope decision.
- Evidence strength.
- Next action.

## Boundaries

Do not promote loose ideas directly into KORA Core knowledge without evidence or review.

Do not create automations from ideas before the workflow is stable.

## Related

```text
skills/record-learning.md
skills/promote-learning.md
skills/create-experiment.md
skills/create-skill.md
skills/classify-scope.md
skills/detect-capability-gap.md
```
