---
title: "Workflow Design Principles"
type: framework
domain: "operations"
subdomain: "workflow-design"
status: draft
version: "0.1"
evidence_level: internal_framework
sources: []
related: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Workflow Design Principles

## Summary

A workflow describes how work moves from trigger to result, including responsibilities, inputs, steps, tools, quality checks, and stop conditions.

## Core Idea

Good workflows make repeatable work visible, teachable, improvable, and safer to delegate or automate.

A workflow should define:

- trigger;
- owner;
- inputs;
- steps;
- tools;
- outputs;
- quality checks;
- exceptions;
- handoffs;
- stop conditions.

## When To Use

- Documenting repeated business processes.
- Preparing a workflow for automation.
- Diagnosing delays, rework, missed handoffs, or unclear ownership.
- Creating SOPs, checklists, onboarding materials, or operational dashboards.

## When Not To Use

- When the work is one-off and low risk.
- When experimentation matters more than standardization.
- When the process is still too unstable to formalize.

## How To Apply

Use this structure:

```text
Trigger:
Owner:
Input:
Steps:
Output:
Quality check:
Exception path:
Stop condition:
Improvement signal:
```

Then ask where the workflow breaks: missing input, unclear owner, slow handoff, weak tool, no review, or no feedback loop.

## Examples

Weak workflow:

```text
Post content every week.
```

Better workflow:

```text
Every Monday, select 3 topics from the content backlog, draft posts, review for offer alignment, schedule approved posts, and record performance every Friday.
```

## Limitations

Over-documentation can slow small teams. Match workflow detail to frequency, risk, and delegation needs.

## Sources

Internal KORA business framework.

## Related

- `automations/README.md`
- `skills/create-automation.md`

