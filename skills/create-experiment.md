# create-experiment

## Purpose

Create or propose a structured KORA experiment.

This skill helps KORA test hypotheses without confusing experiments with decisions, memory, knowledge, or automations.

## When To Use

- When the user wants to test a hypothesis.
- When comparing options before making a durable decision.
- When validating whether a skill, agent, tool, integration, or automation is worth creating.
- When trying a new marketing, product, software, operations, or business approach.
- When a capability plan recommends an experiment.

## When Not To Use

- When the user already made a clear decision.
- When direct execution is enough.
- When there is no hypothesis.
- When the experiment would require external access, publishing, spending, or automation without approval.

## Inputs

- User request or capability plan.
- Hypothesis.
- Project binding, if local or hybrid.
- Existing knowledge, context, decisions, evals, and capabilities.
- Experiment specification.
- Experiment template.

## Process

1. State the hypothesis.
2. Classify scope: global, local, or hybrid.
3. Identify the project, if relevant.
4. Define method.
5. Define inputs.
6. Define success criteria.
7. Define metrics or signals.
8. Define duration or stopping condition.
9. Identify risks and approval points.
10. Choose destination: KORA Core experiments or local `.kora/experiments/`.
11. Create or propose the experiment record.

## Outputs

- Experiment record or proposal.
- Scope classification.
- Success criteria.
- Metrics or signals.
- Approval points.
- Related evals or learning plan.

## Boundaries

This skill creates experiment definitions. It does not run experiments, publish content, access accounts, or change external systems by itself.

It should not store local experiments in KORA Core unless the experiment is reusable or architecture-level.
