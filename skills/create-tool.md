# create-tool

## Purpose

Create or propose a KORA tool definition.

## When To Use

- When a capability plan recommends a tool.
- When a task needs an executable or external capability.
- When a repeated workflow would benefit from a script, command, API client, browser action, database operation, or local utility.

## When Not To Use

- When a skill, agent, eval, integration, or automation is the better abstraction.
- When direct execution is enough.
- When required permissions or safety constraints are unclear.

## Inputs

- Capability plan.
- Tool purpose.
- Scope classification.
- Required permissions.
- Expected inputs and outputs.
- Allowed callers.
- Related skills, agents, evals, integrations, or automations.

## Process

1. Confirm why a tool is needed.
2. Check existing global and local tools.
3. Classify scope: global, local, or hybrid.
4. Classify permission level.
5. Define inputs, outputs, allowed callers, permissions, safety constraints, failure modes, approval points, and related references.
6. Use `tools/templates/tool-template.md`.
7. Ask approval before creating tools that can write, publish, spend, delete, move, overwrite, expose data, or access accounts.

## Outputs

- Tool definition or proposal.
- Scope classification.
- Permission level.
- Destination path.
- Approval points.

## Boundaries

This skill creates tool definitions. It does not implement or run tools by itself.
