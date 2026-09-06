# KORA Operational Loop

This directory supports the local KORA operational loop for this project.

## What To Save

- Important eval results.
- Capability validations.
- Repeated workflow diagnostics.
- Experiments with useful learning.
- Decisions that affect project direction.
- Local memory that will help future work.
- Capability gaps that should become future agents, skills, evals, tools, integrations, or automations.

## What Not To Save

- Raw conversations.
- Secrets, tokens, credentials, or `.env` values.
- Customer data or sensitive payloads.
- Private client-specific schemas unless sanitized and approved.
- One-off notes with no future value.

## Default Flow

```text
Task or change
-> select context
-> use local agent/skill/tool if relevant
-> run or simulate eval
-> record eval result when useful
-> review capability gaps
-> record learning or decision when approved
```

## Local Result Areas

```text
.kora/evals/results/        Eval results.
.kora/experiments/results/  Experiment results.
.kora/capability-gaps/      Gap reviews and proposed future capabilities.
.kora/memory/               Approved operational memory.
.kora/decisions/            Local KORA/project decisions.
.kora/templates/            Local templates.
```

## Approval Rule

Save results only when useful and approved. Do not create automations or external integrations until the workflow is stable and permissioned.
