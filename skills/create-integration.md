# create-integration

## Purpose

Create or propose a KORA integration definition for an external system.

## When To Use

- When a task requires external data or external actions.
- When a capability plan recommends API, MCP, plugin, account, or platform access.
- When manual or assisted workflows are no longer enough.

## When Not To Use

- When screenshots, exports, manual input, or browser-assisted inspection are enough.
- When account access, subscription, permission, or official platform constraints are unknown.
- When the user has not approved external connection planning.

## Inputs

- Capability plan.
- External system name.
- Purpose.
- Scope classification.
- Access requirements.
- Data read/write behavior.
- Permission level.
- Fallback mode.
- Security/privacy concerns.

## Process

1. Confirm why integration is needed.
2. Check simpler fallback modes.
3. Check existing integrations.
4. Classify scope and permission level.
5. Identify accounts, subscriptions, credentials, APIs, MCP connectors, plugins, or approvals needed.
6. Identify read/write behavior and external side effects.
7. Note that current official docs must be checked before real implementation.
8. Use `integrations/templates/integration-template.md`.
9. Ask approval before account access, paid usage, external writes, publishing, scheduling, or storing credentials.

## Outputs

- Integration definition or proposal.
- Access requirements.
- Permission level.
- Fallback mode.
- Approval points.
- Implementation readiness notes.

## Boundaries

This skill creates integration definitions. It does not connect accounts, fetch credentials, call APIs, or implement connectors by itself.
