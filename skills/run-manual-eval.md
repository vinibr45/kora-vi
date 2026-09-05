# run-manual-eval

## Purpose

Run or simulate a manual KORA eval and produce a structured eval result.

This skill is for v0.7 manual evaluation. It is not an automated eval runner.

## When To Use

- When testing KORA behavior against a scenario.
- When reviewing an artifact using a checklist, rubric, scenario, regression, safety, or acceptance eval.
- Before accepting changes that affect architecture, source-of-truth stores, capabilities, permissions, integrations, automations, or project bindings.

## When Not To Use

- When no eval definition exists and criteria are unclear.
- When automated test infrastructure is required but unavailable.
- When the task is simple and low-risk.

## Inputs

- Eval definition.
- Artifact, behavior, plan, or output being evaluated.
- Relevant context and decisions.
- Project binding, if local.
- Eval result template.

## Process

1. Identify the eval file and target.
2. Gather only the context needed to evaluate.
3. Compare the target against pass criteria.
4. Check fail criteria.
5. Check risk and approval requirements.
6. Assign result status: pass, fail, needs-revision, blocked, or not-applicable.
7. Record evidence and findings.
8. Recommend required fixes or follow-ups.
9. Decide whether a result file should be stored.
10. Use `promote-learning` before turning eval findings into memory, knowledge, decisions, or capability changes.

## Outputs

- Eval result.
- Status.
- Evidence.
- Findings.
- Required fixes.
- Recommendations.
- Learning or persistence recommendation.

## Result Location

Global eval result:

```text
C:\KORA\evals\results\
```

Local eval result:

```text
<project-repository>\.kora\evals\results\
```

Store results only when they matter for future decisions, learning, or quality baselines.

## Boundaries

This skill does not silently change source-of-truth stores.

It does not replace automated tests when code-level verification is required.
