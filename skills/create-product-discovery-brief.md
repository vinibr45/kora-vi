---
name: "create-product-discovery-brief"
type: decision
scope: hybrid
status: draft
version: "0.1"
owner: "KORA Core"
domains:
  - product
related_agents:
  - agents/context-curator.md
  - agents/capability-router.md
related_skills:
  - skills/select-context.md
required_knowledge:
  - knowledge/product/product-discovery-basics.md
required_tools: []
evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Create Product Discovery Brief

## Purpose

Create a product discovery brief that clarifies user, problem, context, alternatives, assumptions, smallest useful solution, and success signal.

## When To Use

- Before building a product, feature, workflow, dashboard, or AI assistant.
- When a requested feature may hide a deeper user problem.
- When deciding what belongs in an MVP.

## When Not To Use

- When the task is a clear bug fix.
- When the user has already validated the exact requirement.
- When urgent execution matters more than discovery.

## Inputs

- User or audience.
- Problem statement.
- Current alternative.
- Desired outcome.
- Evidence.
- Constraints.
- Business goal.

## Process

1. Restate the product request as a user problem.
2. Identify assumptions and evidence.
3. Clarify the smallest useful solution.
4. Define success signals.
5. Recommend build, prototype, research, or discard.

## Outputs

- Product discovery brief.
- Assumption list.
- MVP recommendation.
- Success criteria.
- Open questions.

## Required Knowledge

- `knowledge/product/product-discovery-basics.md`

## Optional Knowledge

- Project roadmap.
- User research.
- Analytics or support data.

## Required Tools

None by default.

## Optional Tools

- Spreadsheet or analytics analysis.
- Design brief generator.

## Evals

Review for user clarity, problem clarity, evidence quality, scope discipline, and success signal.

## Approval Points

Human approval is required before turning the brief into implementation work.

## Boundaries

This skill creates a discovery brief. It does not implement the product change.

## Related

- `knowledge/product/product-discovery-basics.md`
