# assess-integration-need

## Purpose

Assess whether a task truly needs an external integration, or whether a simpler execution mode is enough.

This skill helps KORA avoid premature integrations while still recognizing when APIs, MCP connectors, plugins, accounts, or external services would materially improve a workflow.

## When To Use

- Before `create-integration`.
- When a task requires external data, accounts, platforms, APIs, plugins, MCP connectors, or services.
- When the user asks for something involving Instagram, Google, GitHub, calendars, email, design tools, analytics, schedulers, payments, CRM, or other external systems.
- When a capability plan identifies possible integration or automation.
- When there may be manual, assisted, exported-file, screenshot, browser, tool-supported, integrated, or automated alternatives.

## When Not To Use

- When the task is fully local and does not need external data or actions.
- When an approved integration already exists and clearly fits.
- When the user explicitly asks only for a manual workflow.
- When direct execution is enough.

## Inputs

- User task.
- Capability plan, if available.
- Target project and binding, if relevant.
- External system or platform involved.
- Required data or action.
- Existing tools and integrations.
- Available accounts, subscriptions, plugins, MCP connectors, APIs, or exports, if known.
- Risk and permission constraints.

## Process

1. Identify the external system involved.
2. Identify what is needed from the external system:

```text
read data
write data
publish
schedule
send
modify settings
delete
spend money
trigger workflow
```

3. Check whether the need can be met through a simpler mode:

```text
manual input
screenshots
CSV/exported files
copy/paste data
browser-assisted inspection
local files
existing tool
existing integration
```

4. Check whether integration would materially improve recurrence, accuracy, speed, scale, or reliability.
5. Classify permission level:

```text
read-only
write-local
write-external
publish
spend
```

6. Identify risks:

```text
account access
credentials
privacy
sensitive data
platform policy
rate limits
paid usage
external side effects
maintenance burden
```

7. Identify whether current official documentation must be checked before implementation.
8. Recommend one of these outcomes:

```text
No integration needed
Use manual fallback
Use browser/tool-supported workflow
Use existing integration
Propose read-only integration
Propose write-capable integration
Propose automation after integration is validated
Blocked pending account/subscription/permission info
```

9. Ask for approval before proposing implementation that touches accounts, external writes, publishing, scheduling, paid services, credentials, or recurring automation.

## Outputs

- Integration need assessment.
- Recommended execution mode.
- Simpler fallback options.
- Permission level.
- Risks and approval points.
- Existing integration/tool fit, if any.
- Recommendation: do not integrate, use fallback, use existing integration, propose new integration, or defer.

## Example

Task:

```text
Analyze Marcos Dev Instagram performance and recommend next posts.
```

Possible assessment:

```text
External system: Instagram/Meta
Need: read performance data
Initial mode: manual screenshots or exported insights
Integration need: not required for first test
Future integration: read-only metrics integration if task becomes recurring
Automation: only after metrics workflow is validated and approved
```

## Boundaries

This skill assesses need. It does not create or implement integrations by itself.

It should prefer the simplest sufficient mode before recommending external connection.

It should not assume account access, subscriptions, APIs, plugins, or MCP connectors are available unless verified.
