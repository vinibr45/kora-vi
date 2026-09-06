---
title: "Subagent Delegation Patterns"
type: framework
domain: "agentic-systems"
subdomain: "subagents"
status: draft
version: "0.1"
evidence_level: internal_framework
sources:
  - docs/agents/kora-agents-spec-v0.5.md
  - docs/orchestration/kora-orchestration-spec-v0.6.md
related:
  - knowledge/agentic-systems/custom-agent-design-principles.md
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Subagent Delegation Patterns

## Summary

Subagents are useful when a larger task can be divided into bounded responsibilities that benefit from parallel work, specialized review, or isolated context.

In KORA, a subagent pattern should be explicit even if the runtime implementation is manual, assisted, or tool-supported.

## Core Idea

Use subagents to isolate responsibility:

- researcher;
- planner;
- implementer;
- reviewer;
- tester;
- critic;
- context curator;
- domain specialist.

A subagent should receive a narrow objective, selected context, expected output format, permission limits, and handoff instructions.

## When To Use

- The task has separable workstreams.
- Specialized judgment improves quality.
- Review should be independent from creation.
- Context should be isolated to reduce confusion.
- Parallel execution would save time without increasing risk.

## When Not To Use

- The task is simple.
- The subagent would need broad unrestricted context.
- The work requires tight sequential reasoning.
- Delegation creates more coordination cost than value.
- Human approval is required before any meaningful progress.

## How To Apply

Define the delegation contract:

```text
Subagent role:
Objective:
Allowed context:
Forbidden context:
Allowed actions:
Expected output:
Quality criteria:
Handoff target:
Stop conditions:
```

Use independent review for risky outputs:

```text
Creator subagent -> produces artifact
Reviewer subagent -> checks quality and risks
Orchestrator -> decides final action
```

## Examples

Landing page task:

```text
Context Curator -> selects brand and offer context.
Copy Specialist -> drafts message hierarchy.
UX Reviewer -> checks layout and accessibility.
Implementation Agent -> edits files.
```

Knowledge expansion task:

```text
Researcher -> collects concepts.
Knowledge Steward -> structures entries.
Reviewer -> checks boundaries and duplication.
```

## Limitations

Subagents increase coordination overhead and can produce conflicting recommendations. Orchestration must decide how outputs are merged.

## Sources

- `docs/agents/kora-agents-spec-v0.5.md`
- `docs/orchestration/kora-orchestration-spec-v0.6.md`

## Related

- `knowledge/agentic-systems/context-selection-principles.md`
- `knowledge/agentic-systems/eval-driven-agentic-work.md`

