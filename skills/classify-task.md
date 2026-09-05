# classify-task

## Purpose

Classify a user task before execution.

This skill helps KORA understand what kind of work is being requested and which capabilities may be needed.

## When To Use

- Before complex, recurring, risky, or ambiguous tasks.
- When the task may require agents, skills, tools, integrations, automations, evals, memory, or decisions.
- When the project, domain, or execution mode is unclear.

## Inputs

- User request.
- Current repository or project path.
- Known project binding, if available.
- Existing KORA architecture and decisions.
- Relevant local project instructions.

## Process

1. Identify the target project or confirm that the task is global.
2. Identify the domain: marketing, software engineering, UX, security, finance, operations, sales, product, or other.
3. Identify task type: one-off execution, recurring workflow, architectural change, knowledge work, project setup, integration, automation, or evaluation.
4. Estimate risk: low, medium, or high.
5. Identify whether external accounts, subscriptions, APIs, MCP connectors, plugins, or permissions may be needed.
6. Identify whether the task needs a capability plan before execution.

## Outputs

- Task classification.
- Domain classification.
- Risk level.
- Recurrence estimate.
- Possible capability types needed.
- Recommendation: execute directly or create a capability plan.

## Boundaries

This skill classifies the task. It does not execute the task, create files, or decide final architecture alone.
