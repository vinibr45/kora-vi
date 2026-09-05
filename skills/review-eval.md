# review-eval

## Purpose

Review a KORA eval for clarity, scope, usefulness, risk coverage, and fit with the KORA Evals Specification.

## When To Use

- Before marking an eval as active.
- After creating or editing an eval.
- When an eval may be vague, duplicated, too broad, too narrow, or misplaced.
- When deciding whether a local eval should become global.
- When checking whether an eval should actually be a skill, agent, tool, decision, or knowledge entry.

## When Not To Use

- For running an eval; use `run-manual-eval`.
- For reviewing ordinary task outputs without an eval definition.

## Inputs

- Eval file or draft.
- KORA Evals Specification.
- Related agents, skills, knowledge, tools, decisions, and project binding.
- Artifact or behavior the eval targets.

## Process

1. Check whether the eval has a clear purpose and target.
2. Check whether the eval should exist or whether an existing eval fits.
3. Check whether the eval type is correct.
4. Check whether the scope is global, local, or hybrid.
5. Check whether the destination matches the scope.
6. Check whether expected agents, skills, tools, and context are listed when relevant.
7. Check whether pass and fail criteria are observable.
8. Check risk and approval checks.
9. Check whether result format is clear.
10. Recommend status: draft, active, deprecated, or needs revision.

## Outputs

- Review result.
- Recommended status.
- Required fixes.
- Scope or placement warnings.
- Missing criteria.
- Risk or approval gaps.
- Suggested improvements.

## Pass Criteria

An eval is healthy when it:

- has a clear target;
- has observable pass/fail criteria;
- is scoped correctly;
- includes risk and approval checks when relevant;
- is reusable enough for its intended scope;
- does not duplicate skills or agent responsibilities;
- defines result format.

## Boundaries

This skill reviews eval definitions. It does not run them or promote results into memory/knowledge by itself.
