# review-integration

## Purpose

Review a KORA integration definition for need, scope, access, permissions, privacy, safety, and fallback strategy.

## When To Use

- Before approving or implementing an integration.
- After creating an integration definition.
- When external account, API, MCP, plugin, or platform access is involved.

## Inputs

- Integration definition.
- Tools/integrations/automations specification.
- Capability plan.
- Related agents, skills, tools, evals, automations, and project binding.

## Process

1. Check whether the integration is necessary.
2. Check whether a simpler fallback can solve the task.
3. Check scope: global, local, or hybrid.
4. Check access requirements and permission level.
5. Check data read/write behavior.
6. Check privacy, security, credential, platform, and paid usage risks.
7. Check approval points.
8. Check whether official current documentation must be verified before implementation.
9. Recommend status: proposed, approved, active, paused, deprecated, or needs revision.

## Outputs

- Review result.
- Recommended status.
- Required fixes.
- Approval warnings.
- Security/privacy warnings.
- Fallback recommendation.

## Boundaries

This skill reviews integration definitions. It does not grant access, implement APIs, or use external accounts.
