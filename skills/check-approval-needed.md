# check-approval-needed

## Purpose

Decide whether a KORA action needs explicit human approval before proceeding.

This skill protects human control around external systems, money, publishing, sensitive data, structural changes, project boundaries, automation, and durable memory.

## When To Use

- Before connecting accounts, APIs, plugins, integrations, or external services.
- Before publishing, sending, scheduling, deploying, buying, deleting, or modifying external systems.
- Before storing sensitive, client-specific, or credential-like information.
- Before activating automations or recurring workflows.
- Before major version changes, broad architecture changes, or source-of-truth changes.
- When the user asks "pode fazer sozinho?", "precisa aprovar?", or similar.

## When Not To Use

- For simple low-risk local documentation edits.
- For read-only repository inspection.
- For direct work the user has clearly requested and that has no external side effects or durable governance impact.

## Inputs

- Proposed action.
- Target files, systems, accounts, or repositories.
- Data sensitivity.
- External side effects.
- Cost, publishing, deployment, deletion, or automation implications.
- Current user instruction.

## Process

1. Describe the proposed action.
2. Identify side effects:

```text
local file write
external write
publishing
deployment
scheduling
spend
account access
credential handling
sensitive data
source-of-truth change
automation activation
version governance
```

3. Classify approval level:

```text
no explicit approval needed
approval recommended
explicit approval required
do not proceed
```

4. Explain the reason.
5. If approval is required, ask a concise approval question.
6. If no approval is needed, proceed through the relevant skill.

## Outputs

- Approval classification.
- Reason.
- Required user decision, if any.
- Safe next action.

## Approval Rules

```text
Read-only local inspection -> no explicit approval needed
Small local Markdown update requested by user -> no explicit approval needed
New durable KORA artifact requested by user -> no explicit approval needed, but maintain indexes
Major version change -> explicit approval required
External account connection -> explicit approval required
Publishing/sending/scheduling/deploying -> explicit approval required
Paid usage or spend -> explicit approval required
Credentials or secrets -> do not store in KORA Core
Sensitive client/project data -> keep local and ask when uncertain
Automation activation -> explicit approval required
Deletion/deprecation/rename of core entry points -> explicit approval required
```

## Boundaries

This skill does not grant permission by itself. It classifies whether permission is needed.

When in doubt, preserve human control and choose the lower-risk path.

## Related

```text
GOVERNANCA.md
skills/assess-integration-need.md
skills/create-automation.md
skills/review-automation.md
skills/assess-kora-version-impact.md
```
