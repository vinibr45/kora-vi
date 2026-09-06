---
name: "diagnose-business-workflow"
type: decision
scope: hybrid
status: draft
version: "0.1"
owner: "KORA Core"
domains:
  - operations
  - business-ai
related_agents:
  - agents/capability-router.md
  - agents/context-curator.md
related_skills:
  - skills/select-context.md
  - skills/create-automation.md
required_knowledge:
  - knowledge/operations/workflow-design-principles.md
  - knowledge/business-ai/ai-use-case-selection.md
required_tools: []
evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Diagnose Business Workflow

## Purpose

Diagnose a business workflow and identify bottlenecks, missing owners, unclear inputs, weak handoffs, quality risks, and automation opportunities.

## When To Use

- The user wants to improve a recurring business process.
- A workflow feels slow, confusing, inconsistent, or hard to delegate.
- The user is considering automation but the process is not yet clear.

## When Not To Use

- When the work is one-off and low risk.
- When the workflow is not understood well enough to document.
- When immediate execution is more important than diagnosis.

## Inputs

- Workflow name.
- Trigger.
- Owner or responsible roles.
- Inputs.
- Current steps.
- Tools used.
- Outputs.
- Known problems.
- Desired result.

## Process

1. Map the workflow from trigger to output.
2. Identify the owner, handoffs, inputs, and decision points.
3. Check where delays, rework, confusion, or quality failures occur.
4. Separate process issues from tool issues.
5. Identify whether the workflow is ready for skill, tool, automation, or agent support.
6. Recommend the smallest useful improvement.

## Outputs

- Workflow map.
- Bottleneck diagnosis.
- Missing context or ownership notes.
- Automation readiness assessment.
- Recommended next action.

## Required Knowledge

- `knowledge/operations/workflow-design-principles.md`
- `knowledge/business-ai/ai-use-case-selection.md`

## Optional Knowledge

- Project-specific SOPs.
- Project-specific team roles.
- Metrics or service history.

## Required Tools

None by default.

## Optional Tools

- Diagram generation.
- Spreadsheet analysis.
- Project file writer.

## Evals

Review for:

- clear trigger;
- clear owner;
- clear inputs and outputs;
- identified failure points;
- realistic automation recommendation;
- no private operational history placed in KORA Core.

## Approval Points

Human approval is required before changing live workflows, assigning responsibilities, or creating automations.

## Boundaries

This skill diagnoses and recommends. It does not modify operations or create automations without a separate approved workflow.

## Related

- `skills/create-automation.md`
- `knowledge/operations/workflow-design-principles.md`
