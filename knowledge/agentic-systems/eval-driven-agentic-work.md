---
title: "Eval Driven Agentic Work"
type: framework
domain: "agentic-systems"
subdomain: "evals"
status: draft
version: "0.1"
evidence_level: internal_framework
sources:
  - docs/orchestration/kora-orchestration-spec-v0.6.md
related:
  - evals/README.md
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Eval Driven Agentic Work

## Summary

Eval driven work means defining how quality will be judged before trusting a recurring agentic workflow.

Evals are especially important when agents create knowledge, write files, use tools, touch external systems, or produce business-critical outputs.

## Core Idea

An eval should check whether an output is useful, safe, correct enough for its purpose, within scope, and aligned with the relevant source of truth.

Eval criteria may include:

- completeness;
- accuracy;
- boundary fit;
- source awareness;
- privacy;
- permission safety;
- format validity;
- user usefulness;
- project convention fit;
- no unsupported claims.

## When To Use

- Before promoting a capability from draft to active.
- Before automating a workflow.
- When a task affects source-of-truth stores.
- When outputs are reused across projects.
- When external tools or account access are involved.

## When Not To Use

- When the task is tiny, low risk, and one-off.
- When quality can be assessed immediately by the user without reusable criteria.

## How To Apply

Use this eval outline:

```text
Artifact under review:
Purpose:
Required inputs:
Pass criteria:
Fail criteria:
Risk checks:
Manual review steps:
Result format:
Learning destination:
```

Run evals after output creation and before promotion, publication, automation, or memory updates.

## Examples

Knowledge entry eval:

```text
Checks if the entry is reusable, not project-specific, source-aware, clear, and connected to related skills.
```

PDF eval:

```text
Checks rendering, pagination, readability, margins, source preservation, and no sensitive data leakage.
```

## Limitations

Evals do not guarantee truth. They structure review and improve consistency. Human approval still matters for high-risk work.

## Sources

- `docs/orchestration/kora-orchestration-spec-v0.6.md`

## Related

- `skills/create-eval.md`
- `skills/run-manual-eval.md`
- `skills/review-eval.md`

