# EV-0006: Knowledge Placement

## Scenario

The user provides information about marketing and asks KORA to store it.

Example:

```text
A good offer should clarify the audience, problem, transformation, mechanism, scope, proof, and next step. For Marcos Dev, the offer is site creation for small local businesses that need a trustworthy digital presence.
```

## Purpose

Test whether KORA separates reusable marketing knowledge from Marcos Dev-specific application.

## Expected Agents

- Knowledge Steward
- KORA Architect, if scope is unclear
- Context Curator, if related project context is needed

## Expected Skills

- `classify-scope`
- `promote-learning`
- `record-decision`, only if a durable rule is created
- `select-context`, if related knowledge or project context must be reviewed

## Expected Knowledge Behavior

KORA should classify the reusable offer principle as global knowledge.

Expected destination:

```text
knowledge/marketing/offers/
```

KORA should classify the Marcos Dev offer as project-specific context.

Expected destination:

```text
<marcos-dev-repository>/.kora/context/
```

## Pass Criteria

This scenario passes if KORA:

- separates principle from application;
- stores reusable theory in KORA Core;
- keeps Marcos Dev-specific facts local;
- uses or proposes the knowledge entry template;
- avoids creating a large generic marketing document.

## Fail Criteria

This scenario fails if KORA:

- stores Marcos Dev's offer inside global marketing knowledge;
- stores reusable offer theory only inside Marcos Dev;
- creates a giant `marketing.md` file;
- omits metadata when metadata would help future retrieval.
