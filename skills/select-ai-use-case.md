---
name: "select-ai-use-case"
type: decision
scope: hybrid
status: draft
version: "0.1"
owner: "KORA Core"
domains:
  - business-ai
  - operations
related_agents:
  - agents/capability-router.md
  - agents/kora-architect.md
related_skills:
  - skills/assess-integration-need.md
  - skills/create-capability-plan.md
required_knowledge:
  - knowledge/business-ai/ai-use-case-selection.md
  - knowledge/operations/workflow-design-principles.md
required_tools: []
evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Select AI Use Case

## Purpose

Decide whether a business task is a good candidate for AI assistance, skill creation, tool creation, automation, or agent support.

## When To Use

- The user wants to apply AI to a business process.
- Multiple possible automations or AI ideas need prioritization.
- A task may require external tools, sensitive data, or human approval.

## When Not To Use

- When the user already gave a narrow low-risk implementation task.
- When the task is high-stakes and requires professional judgment.
- When the output cannot be reviewed.

## Inputs

- Business task or process.
- Frequency.
- Time cost.
- Input and output clarity.
- Available context.
- Risk level.
- Review method.
- Expected value.
- Existing workflow maturity.

## Process

1. Describe the task in operational terms.
2. Score frequency, time cost, clarity, context availability, reviewability, risk, and business value.
3. Classify the best mode:
   - direct execution;
   - skill;
   - tool;
   - automation;
   - agent;
   - integration;
   - do not automate yet.
4. Identify missing context or controls.
5. Recommend the smallest safe next step.

## Outputs

- AI use-case assessment.
- Readiness score or qualitative rating.
- Recommended capability path.
- Risks and required approvals.
- Next experiment or implementation step.

## Required Knowledge

- `knowledge/business-ai/ai-use-case-selection.md`
- `knowledge/operations/workflow-design-principles.md`

## Optional Knowledge

- Project-specific process documentation.
- Existing automation definitions.
- Project evals.

## Required Tools

None by default.

## Optional Tools

- Spreadsheet analysis.
- Integration assessment tools.
- Evals.

## Evals

Review for:

- clear business value;
- reviewable output;
- acceptable risk;
- stable process;
- no unapproved sensitive data use;
- appropriate human oversight.

## Approval Points

Human approval is required before connecting accounts, using paid tools, storing credentials, processing sensitive data, or enabling automation.

## Boundaries

This skill selects and scopes AI use cases. It does not implement the selected capability by itself.

## Related

- `skills/create-capability-plan.md`
- `skills/assess-integration-need.md`
