# review-capability-plan

## Purpose

Review a KORA capability plan before execution or capability creation.

This skill ensures that orchestration decisions are clear, scoped, minimally complex, and aligned with KORA architecture.

## When To Use

- Before creating new agents, skills, tools, integrations, automations, evals, memory, or decisions from a capability plan.
- Before executing complex, recurring, risky, or ambiguous tasks.
- When multiple execution modes are possible.
- When global/local/hybrid placement matters.
- When a plan may be overengineered.

## When Not To Use

- For small one-off low-risk tasks that can be executed directly.
- When no capability plan exists and the task does not require one.
- As a replacement for domain-specific evals or code/content review.

## Inputs

- Capability plan.
- User task.
- KORA Orchestration Specification.
- Capability Plan Template.
- Project binding, if relevant.
- Existing global and local capabilities.
- Relevant decisions.

## Process

1. Check whether the task summary is accurate.
2. Check whether project, repository, and binding are identified.
3. Check task classification: domain, type, complexity, risk, recurrence, and external systems.
4. Check whether required context is listed and missing context is explicit.
5. Check whether existing global and local capabilities were inspected before proposing new ones.
6. Check whether missing capabilities are justified.
7. Check whether execution mode is appropriate: manual, assisted, tool-supported, integrated, or automated.
8. Check global/local/hybrid placement decisions.
9. Check approval points.
10. Check eval, learning, memory, and decision implications.
11. Check whether the minimal next action avoids unnecessary complexity.
12. Recommend status: approved, needs revision, or blocked pending user decision.

## Outputs

- Plan review result.
- Recommended status.
- Required fixes.
- Missing context.
- Boundary warnings.
- Approval warnings.
- Overengineering warnings.
- Minimal next action recommendation.

## Pass Criteria

A capability plan is healthy when it:

- reflects the user's task accurately;
- identifies project and context needs;
- checks existing capabilities first;
- justifies new capabilities;
- chooses the lowest sufficient execution mode;
- separates global, local, and hybrid scope;
- identifies approvals clearly;
- includes eval and learning implications when useful;
- avoids premature tools, integrations, and automations.

## Boundaries

This skill reviews plans. It does not execute the plan or create capabilities by itself.

It should not approve integrations, automations, account access, publishing, deployment, or source-of-truth changes without human approval.
