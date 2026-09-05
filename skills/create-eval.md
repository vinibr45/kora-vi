# create-eval

## Purpose

Create or propose a KORA eval using the KORA Evals Specification.

This skill helps KORA define structured criteria for evaluating artifacts, tasks, capabilities, processes, or decisions.

## When To Use

- When a task is risky, recurring, or quality-sensitive.
- When a capability plan recommends an eval.
- When creating or reviewing agents, skills, tools, integrations, automations, knowledge, project context, memory, or decisions.
- When the user explicitly asks for a test, checklist, review criteria, or eval.
- When a repeated quality issue needs a reusable check.

## When Not To Use

- When the task is tiny, one-off, and low-risk.
- When an existing eval already fits.
- When the evaluation is really a skill, agent, tool, decision, or knowledge entry.
- When the criteria are too unclear to define.

## Inputs

- User request or capability plan.
- Artifact, behavior, or process to evaluate.
- Scope classification.
- Existing evals.
- Eval specification.
- Eval template.
- Related agents, skills, knowledge, tools, decisions, and project binding.

## Process

1. Confirm why an eval is needed.
2. Check existing global and local evals for overlap.
3. Classify eval type: scenario, checklist, rubric, regression, safety, or acceptance.
4. Classify scope: global, local, or hybrid.
5. Choose destination:

```text
Global -> C:\KORA\evals\
Local -> <project-repository>\.kora\evals\
Hybrid -> reusable base in KORA Core, local adaptation in project `.kora/evals/`
```

6. Define target, purpose, inputs, expected agents, expected skills, expected tools, expected context, pass criteria, fail criteria, risk checks, approval checks, result format, and related references.
7. Apply `evals/templates/eval-template.md` when useful.
8. Ask for approval before creating local project files or evals that affect source-of-truth stores, integrations, automations, publishing, deployment, or account access.

## Outputs

- New eval file or eval proposal.
- Eval type.
- Scope classification.
- Destination path.
- Pass/fail criteria.
- Approval and risk notes.

## Required Knowledge

- `docs/evals/kora-evals-spec-v0.7.md`
- `evals/templates/eval-template.md`

## Boundaries

This skill creates eval definitions. It does not run the eval unless paired with `run-manual-eval`.

It should not create project-specific evals inside KORA Core.
