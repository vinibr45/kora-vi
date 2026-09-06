---
name: "review-capability-gaps"
type: review
scope: global
status: draft
version: "0.1"
owner: "KORA Core"
domains:
  - agentic-systems
  - orchestration
related_agents:
  - agents/capability-router.md
  - agents/kora-architect.md
related_skills:
  - skills/create-capability-plan.md
  - skills/review-capability-plan.md
required_knowledge:
  - knowledge/agentic-systems/capability-routing-heuristics.md
  - knowledge/agentic-systems/structural-decision-matrix.md
  - knowledge/agentic-systems/agent-vs-skill-vs-tool.md
required_tools: []
evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Review Capability Gaps

## Purpose

Review the result of a diagnosis, simulation, implementation, eval, or recurring workflow and identify missing KORA capabilities that should be proposed next.

This skill helps KORA notice when a repeated pattern deserves a new skill, agent, eval, tool, integration, automation, memory entry, decision record, or knowledge entry.

## When To Use

- After a level 5 capability diagnosis.
- After a level 6 local capability test or simulation.
- After a task reveals a repeated workflow.
- After an eval reveals missing quality criteria.
- After a project-specific pattern appears that could become a local skill, agent, or eval.
- After a reusable cross-project pattern appears that could improve KORA Core.

## When Not To Use

- When the task is tiny, one-off, and low risk.
- When the user asked for only a narrow answer and explicitly does not want recommendations.
- When the next capability is already approved and being created.
- When the workflow is too unclear to structure yet.

## Inputs

- Task or simulation summary.
- Capabilities used.
- Capabilities missing or improvised.
- Repetition likelihood.
- Risk level.
- Project scope: global, local, or hybrid.
- Existing agents, skills, tools, evals, integrations, and automations.
- User constraints.

## Process

1. Summarize what was done or simulated.
2. Identify repeated decision points, procedures, reviews, or execution steps.
3. Check whether existing KORA capabilities already cover the pattern.
4. Classify each gap by capability type: agent, skill, tool, integration, automation, eval, knowledge, memory, or decision.
5. Classify scope: global, local, or hybrid.
6. Recommend only capabilities justified by recurrence, risk, quality, reuse, or operational leverage.
7. Separate immediate recommendations from later recommendations.
8. State what should not be created yet.

## Outputs

- Capability gap review.
- Recommended new or improved capabilities.
- Suggested destination paths.
- Rationale for each suggestion.
- Items explicitly deferred.
- Minimal next action.

## Required Knowledge

- `knowledge/agentic-systems/capability-routing-heuristics.md`
- `knowledge/agentic-systems/structural-decision-matrix.md`
- `knowledge/agentic-systems/agent-vs-skill-vs-tool.md`

## Optional Knowledge

- Project `.kora/binding.md`.
- Project `.kora/context/`.
- Existing local agents, skills, tools, evals, automations, and memory.
- Recent eval results or experiments.

## Required Tools

None by default.

## Optional Tools

- File search.
- Project documentation inspection.
- Eval runner.

## Evals

Review for:

- no unnecessary capability creation;
- correct capability type;
- correct global/local/hybrid placement;
- clear justification;
- no project-specific facts placed in KORA Core;
- automation deferred until workflow stability is proven.

## Approval Points

Human approval is required before creating or modifying source-of-truth capabilities, project bindings, local agents, local skills, tools, integrations, automations, evals, or memory.

## Boundaries

This skill identifies and recommends capability gaps. It does not create the recommended artifacts unless paired with the appropriate creation skill and user approval.

## Related

- `skills/create-capability-plan.md`
- `skills/review-capability-plan.md`
- `knowledge/agentic-systems/capability-routing-heuristics.md`
