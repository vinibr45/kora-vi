---
name: "create-cash-flow-snapshot"
type: analysis
scope: hybrid
status: draft
version: "0.1"
owner: "KORA Core"
domains:
  - finance
related_agents:
  - agents/context-curator.md
related_skills:
  - skills/select-context.md
required_knowledge:
  - knowledge/finance/cash-flow-basics.md
required_tools: []
evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Create Cash Flow Snapshot

## Purpose

Create a simple business cash flow snapshot from opening balance, expected receipts, expected payments, obligations, reserve needs, and risk notes.

## When To Use

- The user wants a high-level view of business cash movement.
- A decision depends on whether money arrives before expenses.
- The user wants a monthly management snapshot.

## When Not To Use

- As tax, accounting, investment, legal, or regulated financial advice.
- When reliable financial inputs are unavailable.
- When sensitive financial records should not be placed in KORA Core.

## Inputs

- Opening cash.
- Expected receipts.
- Expected payments.
- Fixed costs.
- Variable costs.
- Taxes or debt obligations.
- Minimum safe reserve.
- Time period.
- Risk notes.

## Process

1. Confirm the period and currency.
2. Separate confirmed and uncertain inflows.
3. Separate fixed, variable, and exceptional outflows.
4. Estimate closing cash and reserve gap.
5. Identify timing risks.
6. Produce decision-support notes, not formal financial advice.

## Outputs

- Cash flow snapshot.
- Closing cash estimate.
- Reserve gap or surplus.
- Timing risk notes.
- Questions for accountant or finance owner when needed.

## Required Knowledge

- `knowledge/finance/cash-flow-basics.md`

## Optional Knowledge

- Project-specific financial records.
- Sales pipeline.
- Accounts receivable and payable.

## Required Tools

None by default.

## Optional Tools

- Spreadsheet tool.
- CSV or XLSX analysis.

## Evals

Review for arithmetic consistency, explicit assumptions, clear uncertainty, and no overreach into formal financial advice.

## Approval Points

Human approval is required before using the output for major spending, hiring, debt, tax, or investment decisions.

## Boundaries

This skill creates a management snapshot. It does not replace accounting, tax, legal, or investment advice.

## Related

- `knowledge/finance/cash-flow-basics.md`
