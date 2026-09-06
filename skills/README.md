# Skills

This directory contains KORA Core skill definitions.

A skill is a reusable procedure for performing a task or making a structured decision.

In v0.4, these are structured skill contracts, not executable automations.

## Initial Core Skills

- `classify-task.md`: classify task domain, project, risk, recurrence, and needed capability types.
- `classify-scope.md`: decide whether something belongs in KORA Core, a local `.kora` binding, or the operational project repository.
- `create-capability-plan.md`: produce a structured plan before using or creating agents, skills, tools, evals, integrations, or automations.
- `bind-project-to-kora.md`: connect a project repository to KORA through a local `.kora/` layer.
- `select-context.md`: select relevant context without loading everything.
- `record-decision.md`: record important architecture or project decisions in a reusable format.
- `promote-learning.md`: decide whether an outcome should become memory, knowledge, a decision, or a capability improvement.
- `create-knowledge-entry.md`: create or propose a reusable knowledge entry from an idea, source, or learning.
- `review-knowledge-entry.md`: review a knowledge entry for clarity, reuse, evidence, structure, and boundaries.
- `create-project-context.md`: create or propose local project context files for a KORA-bound project.
- `review-project-context.md`: review project context for clarity, completeness, freshness, boundaries, and usefulness.
- `setup-kora-project.md`: assisted setup workflow for connecting a project repository to KORA.
- `setup-kora-operational-loop.md`: set up the local operational loop for eval results, experiments, memory, decisions, and capability gaps.
- `create-skill.md`: create or propose a global, local, or hybrid KORA skill.
- `review-skill.md`: review a skill for clarity, scope, usefulness, boundaries, and specification fit.
- `create-agent.md`: create or propose a global, local, or hybrid KORA agent.
- `review-agent.md`: review an agent for clarity, scope, permissions, boundaries, and specification fit.
- `create-capability.md`: create or propose the right capability by delegating to specialized creation skills.
- `review-capability-plan.md`: review a capability plan before execution or capability creation.
- `review-capability-gaps.md`: review diagnostics, simulations, evals, and executions to identify missing KORA capabilities that should be proposed next.
- `create-eval.md`: create or propose a KORA eval definition.
- `review-eval.md`: review an eval for clarity, scope, usefulness, risk coverage, and specification fit.
- `run-manual-eval.md`: run or simulate a manual eval and produce a structured result.
- `record-eval-result.md`: record KORA eval results consistently in local or global result files.
- `create-experiment.md`: create or propose a structured KORA experiment.
- `review-experiment.md`: review an experiment for clarity, scope, usefulness, risk, and learning potential.
- `record-learning.md`: record a structured learning recommendation from a task, eval, experiment, or feedback.
- `review-learning.md`: review learning before promotion into memory, knowledge, decisions, context, or capability changes.
- `create-tool.md`: create or propose a KORA tool definition.
- `review-tool.md`: review a tool definition for clarity, scope, permissions, and safety.
- `create-integration.md`: create or propose an external integration definition.
- `review-integration.md`: review an integration definition for need, access, permissions, privacy, and fallback strategy.
- `create-automation.md`: create or propose a repeatable workflow automation definition.
- `review-automation.md`: review an automation definition for recurrence, value, permissions, safety, and stop conditions.
- `assess-integration-need.md`: assess whether a task truly needs an external integration or can use a simpler mode.
- `use-kora.md`: guide a user through the practical use of KORA for a task or project.
- `generate-image-asset.md`: generate or propose image assets using an approved image generation tool.
- `create-commercial-proposal.md`: create a buyer-friendly commercial proposal from sales, offer, scope, timeline, and next-step context.
- `diagnose-business-workflow.md`: diagnose recurring business workflows and identify bottlenecks, ownership gaps, and automation readiness.
- `select-ai-use-case.md`: decide whether a business task is a good candidate for AI assistance, skill creation, tooling, automation, or agent support.
- `create-sales-follow-up.md`: draft respectful, clear sales follow-up messages for leads, proposals, objections, and stalled opportunities.
- `review-service-response.md`: review or draft customer service responses for empathy, clarity, ownership, and next action.
- `create-product-discovery-brief.md`: create a product discovery brief before building features, products, dashboards, workflows, or AI assistants.
- `create-cash-flow-snapshot.md`: create a simple business cash flow snapshot for management decision support.

## Template

```text
skills/templates/skill-template.md
```

## Specification

```text
docs/skills/kora-skills-spec-v0.4.md
```

