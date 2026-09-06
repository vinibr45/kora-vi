---
title: "AI Use Case Selection"
type: framework
domain: "business-ai"
subdomain: "use-case-selection"
status: draft
version: "0.1"
evidence_level: internal_framework
sources: []
related:
  - knowledge/operations/workflow-design-principles.md
created_at: 2026-09-05
updated_at: 2026-09-05
---

# AI Use Case Selection

## Summary

AI should be applied where it improves speed, quality, consistency, insight, or leverage without creating unacceptable risk.

## Core Idea

Good AI use cases tend to have:

- repeated work;
- clear input and output;
- available context;
- reviewable results;
- meaningful time savings;
- tolerable error risk;
- human approval for high-stakes decisions;
- measurable success criteria.

Avoid automating work that is rare, unclear, high-risk, poorly documented, or impossible to verify.

## When To Use

- Deciding whether a task should become a skill, tool, automation, or agent workflow.
- Prioritizing AI projects for a business.
- Reviewing whether a proposed automation is safe and useful.

## When Not To Use

- When the user has already requested a narrow implementation and risk is low.
- When legal, medical, financial, or safety decisions require expert judgment.
- When there is no way to verify output quality.

## How To Apply

Score the use case:

```text
Frequency:
Time cost:
Input clarity:
Output clarity:
Context availability:
Reviewability:
Risk level:
Business value:
Automation readiness:
```

Start with assisted workflows before full automation. Move from manual to skill, then tool, then automation only when the process is stable.

## Examples

Good early AI use case:

```text
Draft weekly content ideas from approved positioning and offer context, then review before publishing.
```

Risky AI use case:

```text
Automatically approve refunds or contracts without human review.
```

## Limitations

AI usefulness depends on context quality, review discipline, user trust, and operational fit. Model capability alone is not a business case.

## Sources

Internal KORA business framework.

## Related

- `knowledge/operations/workflow-design-principles.md`
- `automations/README.md`

