# review-automation

## Purpose

Review a KORA automation definition for clarity, recurrence, value, permissions, safety, stop conditions, and fit.

## When To Use

- Before approving or activating an automation.
- After creating an automation definition.
- When a recurring workflow may affect external systems, memory, knowledge, decisions, publishing, deployment, or paid services.

## Inputs

- Automation definition.
- Capability plan.
- Tools/integrations/automations specification.
- Related agents, skills, tools, integrations, evals, decisions, and project binding.

## Process

1. Check whether automation is justified by recurrence and value.
2. Check whether a lower execution mode is enough.
3. Check scope: global, local, or hybrid.
4. Check permission level and external side effects.
5. Check trigger, frequency, workflow steps, inputs, and outputs.
6. Check approval points.
7. Check stop conditions and failure handling.
8. Check evals and logging/results.
9. Check memory and learning behavior.
10. Recommend status: proposed, approved, active, paused, deprecated, or needs revision.

## Outputs

- Review result.
- Recommended status.
- Required fixes.
- Approval warnings.
- Safety warnings.
- Lower-complexity alternative, if appropriate.

## Boundaries

This skill reviews automation definitions. It does not activate automations or grant permissions.
