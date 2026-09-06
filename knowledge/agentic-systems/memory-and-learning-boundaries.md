---
title: "Memory And Learning Boundaries"
type: framework
domain: "agentic-systems"
subdomain: "memory-learning"
status: draft
version: "0.1"
evidence_level: internal_framework
sources:
  - architecture/boundaries.md
  - docs/orchestration/kora-orchestration-spec-v0.6.md
related:
  - skills/promote-learning.md
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Memory And Learning Boundaries

## Summary

Memory and learning help KORA improve over time, but they must not become unfiltered transcripts or a dumping ground for every observation.

## Core Idea

Different persistence targets have different meanings:

```text
Memory = operational learning.
Knowledge = reusable concept or framework.
Decision = chosen direction with rationale.
Project context = local truth.
Skill improvement = better procedure.
Agent improvement = better role or boundary.
Eval improvement = better quality check.
No persistence = useful once, not worth storing.
```

Learning should be promoted only when it has value, scope, and destination.

## When To Use

- After completing a task with reusable lessons.
- After an eval reveals a repeated quality issue.
- After a workflow becomes clearer.
- When a local project insight should remain local.
- When a broader pattern may belong in KORA Core.

## When Not To Use

- For raw chat transcripts.
- For sensitive data.
- For unverified assumptions.
- For one-off observations with no future value.
- To move project-specific facts into global knowledge.

## How To Apply

Classify the learning:

```text
What happened?
Why does it matter?
Is it reusable?
Is it local or global?
Is it evidence-backed?
What should change?
Where should it live?
Who should approve it?
```

Then choose destination:

```text
Local project fact -> project .kora/context/
Local operational lesson -> project .kora/memory/
Reusable concept -> knowledge/
Architecture direction -> architecture/decisions/
Procedure update -> skills/
Role update -> agents/
Quality rule -> evals/
```

## Examples

PDF generation learning:

```text
Reusable: preserve source and render PDF locally before delivery.
Destination: knowledge or skill improvement.
```

Project offer insight:

```text
Local: buyers respond better to a specific service package.
Destination: project .kora/context/ or project memory, not KORA Core.
```

## Limitations

Over-recording creates noise. Under-recording loses valuable improvement. The discipline is choosing what will actually help future work.

## Sources

- `architecture/boundaries.md`
- `docs/orchestration/kora-orchestration-spec-v0.6.md`

## Related

- `skills/record-learning.md`
- `skills/promote-learning.md`
