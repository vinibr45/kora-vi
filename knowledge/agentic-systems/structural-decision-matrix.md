---
title: "Structural Decision Matrix"
type: decision-framework
domain: "agentic-systems"
subdomain: "architecture-decisions"
status: draft
version: "0.1"
evidence_level: internal_framework
sources:
  - architecture/boundaries.md
  - orchestration/capability-management.md
related:
  - knowledge/agentic-systems/agent-vs-skill-vs-tool.md
  - knowledge/agentic-systems/capability-routing-heuristics.md
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Structural Decision Matrix

## Summary

This matrix helps KORA decide where a new idea, process, rule, capability, or artifact should live.

It exists to prevent KORA Core from absorbing local project reality and to prevent project bindings from duplicating reusable architecture.

## Core Idea

Choose placement by asking what the artifact owns.

```text
Reusable principle -> knowledge/
Recurring procedure -> skills/
Stable role -> agents/
Executable capability -> tools/
External system access -> integrations/
Repeatable run -> automations/
Quality check -> evals/
Operational lesson -> memory/
Chosen direction -> decisions/
Project truth -> project .kora/context/
Runtime code or published file -> project repository
```

## When To Use

- Before creating a new KORA file.
- Before moving local learning into KORA Core.
- Before creating agents, skills, integrations, tools, evals, or automations.
- When the user asks to expand KORA.

## When Not To Use

- When the file destination is already obvious and low risk.
- When the task is simple execution with no new structure.

## How To Apply

Use this decision table:

| Question | Destination |
| --- | --- |
| Is this a reusable concept? | `knowledge/` |
| Is this a repeatable procedure? | `skills/` |
| Is this a responsibility owner? | `agents/` |
| Is this an executable operation? | `tools/` |
| Does it connect to an external system? | `integrations/` |
| Does it run repeatedly by trigger or schedule? | `automations/` |
| Does it judge quality? | `evals/` |
| Is it a learning from operations? | `memory/` |
| Is it a chosen architecture or project direction? | `decisions/` |
| Is it true only for one project? | project `.kora/` |
| Is it source code or shipped artifact? | project repository |

After using the table, check whether the task revealed a missing capability:

| Signal | Likely next artifact |
| --- | --- |
| Same multi-step workflow will repeat | `skills/` |
| Same specialized judgment will repeat | `agents/` |
| Same external/local operation will repeat | `tools/` |
| Same quality risk needs checking | `evals/` |
| Same external account/service is needed | `integrations/` |
| Same stable workflow should run repeatedly | `automations/` |
| Same reusable principle appeared | `knowledge/` |
| Same operational lesson should persist | `memory/` |
| Same direction was chosen | `decisions/` |
Then classify scope:

```text
Global -> reusable across projects.
Local -> specific to one project.
Hybrid -> reusable pattern plus local adaptation.
```

## Examples

Claude PDF workflow:

```text
Integration: Claude Design access.
Tool: file generation or PDF rendering operation.
Skill: procedure for generating PDF-ready documents.
Automation: repeatable workflow after stable runs.
Eval: PDF quality and safety check.
```

Business proposal:

```text
Knowledge: proposal structure.
Skill: create commercial proposal.
Project context: actual pricing, client, offer, and scope.
Output: final proposal file in the project repository.
```

## Limitations

Some artifacts can seem to fit several places. In those cases, split responsibilities instead of creating one overloaded file.

## Sources

- `architecture/boundaries.md`
- `orchestration/capability-management.md`

## Related

- `knowledge/agentic-systems/agent-vs-skill-vs-tool.md`
- `knowledge/agentic-systems/capability-routing-heuristics.md`
