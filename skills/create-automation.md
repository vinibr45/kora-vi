# create-automation

## Purpose

Create or propose a KORA automation definition for a repeatable workflow.

## When To Use

- When a task is recurring and has a stable process.
- When a capability plan recommends automation.
- When manual or assisted execution is wasting repeated effort.
- When evals, approvals, stop conditions, and failure handling can be defined.

## When Not To Use

- When the workflow is still unclear.
- When direct, manual, assisted, or tool-supported execution is enough.
- When approval points, risks, or external side effects are unclear.
- When automation would publish, spend, access accounts, or modify external systems without approval.

## Inputs

- Capability plan.
- Workflow purpose.
- Trigger and frequency.
- Required agents, skills, tools, integrations, and evals.
- Inputs and outputs.
- Approval points.
- Stop conditions.
- Failure handling.

## Process

1. Confirm recurrence and operational value.
2. Check existing automations.
3. Classify scope: global, local, or hybrid.
4. Classify permission level.
5. Define trigger, frequency, workflow, inputs, outputs, side effects, approvals, stop conditions, failure handling, evals, logging, and learning behavior.
6. Use `automations/templates/automation-template.md`.
7. Ask approval before creating or activating recurring workflows.

## Outputs

- Automation definition or proposal.
- Scope classification.
- Permission level.
- Approval points.
- Stop conditions.
- Required evals.

## Boundaries

This skill creates automation definitions. It does not implement schedulers, background jobs, publishing, account access, or external writes by itself.
