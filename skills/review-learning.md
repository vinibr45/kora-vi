# review-learning

## Purpose

Review a learning record or learning recommendation before it is promoted into memory, knowledge, decisions, project context, or capability changes.

This skill helps KORA avoid storing noise, overgeneralizing weak evidence, or turning local outcomes into global truth too early.

## When To Use

- After `record-learning` creates a learning recommendation.
- Before `promote-learning` changes any source-of-truth store.
- After experiments or evals produce findings.
- When user feedback may become a durable rule.
- When a local project outcome may be proposed as reusable KORA knowledge.
- When evidence strength or destination is unclear.

## When Not To Use

- For raw task execution.
- For creating experiments; use `create-experiment`.
- For reviewing eval definitions; use `review-eval`.
- For reviewing knowledge entries; use `review-knowledge-entry`.
- For low-value observations that clearly should not persist.

## Inputs

- Learning record or recommendation.
- Source task, eval, experiment, result, or feedback.
- Scope classification.
- Evidence strength.
- Proposed destination.
- Related memory, knowledge, decisions, agents, skills, evals, tools, automations, or project context.

## Process

1. Check whether the learning statement is clear.
2. Check whether the learning is useful enough to persist.
3. Check scope: global, local, hybrid, or none.
4. Check evidence strength: weak, moderate, strong, or inconclusive.
5. Check whether the proposed destination fits the learning:

```text
Local project fact -> project context or local memory
Operational history -> memory
Policy or direction -> decision
Reusable concept -> knowledge
Procedure improvement -> skill update
Role improvement -> agent update
Quality improvement -> eval update
Execution capability -> tool/integration/automation proposal
Low-value noise -> no persistence
```

6. Check whether the learning is trying to overgeneralize from one local case.
7. Check whether sensitive data or private client/project information is involved.
8. Check whether approval is required.
9. Recommend: approve promotion, revise learning, keep as learning record, or discard.

## Outputs

- Learning review result.
- Recommended destination.
- Evidence assessment.
- Scope assessment.
- Approval requirement.
- Required fixes.
- Recommendation: promote, revise, keep, discard, or blocked.

## Pass Criteria

A learning recommendation is healthy when it:

- is clear;
- is useful;
- has appropriate scope;
- honestly states evidence strength;
- chooses the right destination;
- does not overgeneralize;
- protects sensitive information;
- identifies approval needs;
- avoids cluttering KORA with noise.

## Boundaries

This skill reviews learning. It does not promote learning by itself.

Use `promote-learning` after review when a source-of-truth store should change.
