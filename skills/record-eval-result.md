---
name: "record-eval-result"
type: execution
scope: hybrid
status: draft
version: "0.1"
owner: "KORA Core"
domains:
  - agentic-systems
  - evals
related_agents:
  - agents/context-curator.md
  - agents/capability-router.md
related_skills:
  - skills/run-manual-eval.md
  - skills/review-capability-gaps.md
  - skills/record-learning.md
required_knowledge:
  - knowledge/agentic-systems/eval-driven-agentic-work.md
  - knowledge/agentic-systems/memory-and-learning-boundaries.md
required_tools: []
evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Record Eval Result

## Purpose

Record the result of a KORA eval in a consistent local or global result file.

For project work, eval results should normally be saved in the project binding under `.kora/evals/results/`.

## When To Use

- After running or simulating an eval.
- After a level 6 capability validation.
- Before promoting a local capability from draft to active.
- Before trusting a recurring workflow.
- When a review produces pass, fail, needs-revision, blocked, or not-applicable status.

## When Not To Use

- For trivial one-off checks.
- When the user has not approved saving the result.
- When the result contains secrets, customer data, private payloads, or raw transcripts.
- When the eval itself is unclear and should be reviewed first.

## Inputs

- Eval file.
- Project.
- Scope.
- Date.
- Evaluator.
- Result status.
- Summary.
- Evidence checked.
- Findings.
- Required fixes.
- Recommendations.
- Learning or capability-gap notes.
- Follow-up actions.

## Process

1. Confirm the eval and target project.
2. Confirm the result should be saved.
3. Remove secrets, credentials, private payloads, customer data, and raw transcripts.
4. Choose the destination:
   - project eval result -> `.kora/evals/results/`
   - reusable global eval result -> `evals/results/`
5. Use the eval result template.
6. Include evidence, findings, required fixes, recommendations, learning, and follow-up.
7. If a recurring pattern appears, pair with `review-capability-gaps`.

## Outputs

- Eval result file.
- Result summary.
- Follow-up actions.
- Optional capability gap recommendation.

## Required Knowledge

- `knowledge/agentic-systems/eval-driven-agentic-work.md`
- `knowledge/agentic-systems/memory-and-learning-boundaries.md`

## Optional Knowledge

- `evals/templates/eval-result-template.md`
- Project `.kora/templates/eval-result-template.md`

## Required Tools

None by default.

## Optional Tools

- Filesystem writer.
- Project file search.

## Evals

Review the recorded result for:

- clear status;
- evidence specificity;
- no sensitive data leakage;
- actionable required fixes;
- correct destination;
- learning destination recommendation.

## Approval Points

Human approval is required before saving eval results in a project repository or KORA Core.

## Boundaries

This skill records eval results. It does not automatically fix findings or promote learning without the appropriate follow-up skill.

## Related

- `skills/run-manual-eval.md`
- `skills/review-capability-gaps.md`
- `evals/templates/eval-result-template.md`
