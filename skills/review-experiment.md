# review-experiment

## Purpose

Review a KORA experiment for clarity, scope, usefulness, risk, and learning potential.

## When To Use

- Before running an experiment.
- After drafting an experiment.
- When an experiment may be vague, risky, too broad, or misplaced.
- When deciding whether an experiment should be global, local, or hybrid.

## When Not To Use

- For running evals; use `run-manual-eval`.
- For promoting learning; use `promote-learning`.
- For direct task execution.

## Inputs

- Experiment draft or file.
- KORA Experiments and Learning Specification.
- Related project binding, knowledge, decisions, evals, agents, skills, tools, or automations.

## Process

1. Check whether the hypothesis is clear.
2. Check scope: global, local, or hybrid.
3. Check whether method, inputs, success criteria, metrics/signals, and stopping condition are defined.
4. Check risks and approval points.
5. Check whether the experiment is useful enough to run.
6. Check whether it is actually a decision, eval, skill, automation, or direct execution instead.
7. Recommend status: proposed, active, completed, abandoned, superseded, or needs revision.

## Outputs

- Review result.
- Recommended status.
- Required fixes.
- Scope warnings.
- Risk or approval warnings.
- Learning potential notes.

## Boundaries

This skill reviews experiments. It does not run them or promote results into memory, knowledge, decisions, or capability changes.
