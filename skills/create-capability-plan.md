# create-capability-plan

## Purpose

Create a structured plan before KORA uses or creates capabilities.

This skill is the bridge between a user task and the agents, skills, tools, evals, integrations, automations, memory, or decisions needed to handle it well.

## When To Use

- Before complex or recurring tasks.
- Before creating a new agent, skill, tool, integration, eval, or automation.
- When multiple execution modes are possible.
- When the task crosses KORA Core and a local project binding.

## Inputs

- User task.
- Task classification.
- Scope classification.
- Existing global capabilities.
- Existing local project capabilities.
- Available tools, integrations, subscriptions, and permissions.
- Relevant context selected by `select-context`, if already available.

## Process

1. Restate the task.
2. Identify the project and domain.
3. List existing global capabilities that may apply.
4. List existing local capabilities that may apply.
5. Identify missing capabilities.
6. Choose an execution mode: manual, assisted, tool-supported, integrated, or automated.
7. Recommend whether to execute directly, reuse, adapt, create, or propose capabilities.
8. Decide where any new capability should live: KORA Core or local `.kora/` binding.
9. Identify evals, memory, or decision records needed.
10. Identify approval points.

## Outputs

- Capability plan.
- Recommended execution mode.
- Capabilities to use.
- Capabilities to create or propose.
- Global/local/hybrid placement.
- Required approvals.
- Minimal next action.

## Boundaries

This skill plans capability usage. It should not create unnecessary complexity or assume integrations are available.
