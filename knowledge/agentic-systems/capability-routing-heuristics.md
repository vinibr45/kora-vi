---
title: "Capability Routing Heuristics"
type: framework
domain: "agentic-systems"
subdomain: "orchestration"
status: draft
version: "0.1"
evidence_level: internal_framework
sources:
  - orchestration/capability-management.md
  - docs/orchestration/kora-orchestration-spec-v0.6.md
related:
  - agents/capability-router.md
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Capability Routing Heuristics

## Summary

Capability routing is the decision process for choosing whether KORA should execute directly, use an existing capability, create a skill, create an agent, use a tool, define an integration, create an automation, run an eval, or record learning.

## Core Idea

Do not create new structure just because it is possible. Create structure when it improves reuse, safety, consistency, quality, or operational leverage.

Routing options:

```text
Direct execution
Existing skill
Existing agent
New skill
New agent
Tool
Integration
Automation
Eval
Memory
Decision
Knowledge entry
```

## When To Use

- A task is complex, recurring, risky, ambiguous, or capability-changing.
- The user asks to expand KORA.
- The task may involve external systems, approvals, or automation.
- It is unclear where a new artifact belongs.

## When Not To Use

- The task is simple, low risk, one-off, and all context is available.

## How To Apply

Ask:

1. Can this be done directly?
2. Does an existing capability fit?
3. Is the task recurring?
4. Does it need specialized judgment?
5. Does it need a repeatable procedure?
6. Does it need external execution?
7. Does it need account access?
8. Does it need quality checks?
9. Should the result persist?
10. Should the capability be global, local, or hybrid?
After a diagnosis, simulation, eval, or implementation, ask a second question:

```text
Did this task reveal a capability gap?
```

A capability gap exists when KORA had to improvise a recurring procedure, repeat a structural judgment, mention the same missing review, or coordinate several capabilities in a pattern that is likely to happen again.

When a gap appears, KORA should name it explicitly:

```text
Capability gap detected:
[short description]

Recommended artifact:
[agent | skill | tool | integration | automation | eval | knowledge | memory | decision]

Suggested scope:
[global | local | hybrid]

Suggested path:
[path]

Why:
[recurrence, risk, quality, reuse, or leverage]
```

Do not create the artifact automatically unless the user asked for creation or approved the next step.

## Examples

Generate one PDF:

```text
Use direct execution plus PDF tool. Do not create automation unless this repeats.
```

Generate weekly business reports:

```text
Create skill, tool-supported workflow, eval, then automation after stable runs.
```

New dashboard indicator pattern:

```text
If adding indicators will repeat across Firebird query, extractor payload, API write, PostgreSQL migration, API read, dashboard, tests, and docs, suggest a local skill such as .kora/skills/plan-dashboard-indicator.md.
```
Create a project-specific Instagram agent:

```text
Use local .kora/agent if it depends on that project's voice, audience, offers, and content rules.
```

## Limitations

Routing depends on current context. If the task, project, or risk changes, the routing decision should be revisited.

## Sources

- `orchestration/capability-management.md`
- `docs/orchestration/kora-orchestration-spec-v0.6.md`

## Related

- `agents/capability-router.md`
- `skills/create-capability-plan.md`

