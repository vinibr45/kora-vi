# review-tool

## Purpose

Review a KORA tool definition for clarity, scope, permissions, safety, and fit.

## When To Use

- Before approving or activating a tool.
- After creating or editing a tool definition.
- When a tool may be unsafe, too broad, duplicated, or misplaced.

## Inputs

- Tool definition.
- Tools specification.
- Related agents, skills, evals, integrations, automations, and project binding.

## Process

1. Check purpose and capability boundary.
2. Check scope: global, local, or hybrid.
3. Check permission level.
4. Check allowed callers.
5. Check inputs and outputs.
6. Check safety constraints, failure modes, and approval points.
7. Check whether the item should be a skill, integration, automation, or eval instead.
8. Recommend status: proposed, approved, active, paused, deprecated, or needs revision.

## Outputs

- Review result.
- Recommended status.
- Required fixes.
- Permission warnings.
- Safety warnings.
- Scope warnings.

## Boundaries

This skill reviews tool definitions. It does not run tools or grant permissions.
