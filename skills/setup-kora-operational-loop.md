---
name: "setup-kora-operational-loop"
type: automation
scope: hybrid
status: draft
version: "0.1"
owner: "KORA Core"
domains:
  - agentic-systems
  - orchestration
  - operations
related_agents:
  - agents/capability-router.md
  - agents/context-curator.md
  - agents/kora-architect.md
related_skills:
  - skills/setup-kora-project.md
  - skills/review-capability-gaps.md
  - skills/record-learning.md
  - skills/promote-learning.md
required_knowledge:
  - knowledge/agentic-systems/capability-routing-heuristics.md
  - knowledge/agentic-systems/eval-driven-agentic-work.md
  - knowledge/agentic-systems/memory-and-learning-boundaries.md
required_tools: []
evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Setup KORA Operational Loop

## Purpose

Set up the local operational loop that makes a KORA-bound project more plug and play after initial setup.

This skill creates or proposes the local structure for recording eval results, experiments, memory, decisions, capability gaps, and recurring KORA task outcomes.

## When To Use

- After a project reaches KORA level 6.
- When a project should start saving important KORA runs instead of only using KORA conversationally.
- When eval results, experiments, decisions, and learnings should become repeatable local artifacts.
- When the user wants KORA to feel plug and play across projects.

## When Not To Use

- Before a local `.kora/binding.md` exists.
- When the user has not approved writing local `.kora/` files.
- When the project does not need persistent KORA results yet.
- When the task only needs direct execution.

## Inputs

- Project repository path.
- Existing `.kora/binding.md`.
- Existing `.kora/context/`.
- Existing local agents, skills, evals, tools, automations, and experiments.
- User-approved setup level.

## Process

1. Confirm the project has a local `.kora/` binding.
2. Create local result directories when missing:
   - `.kora/evals/results/`
   - `.kora/experiments/results/`
   - `.kora/memory/`
   - `.kora/decisions/`
   - `.kora/capability-gaps/`
   - `.kora/templates/`
3. Add local templates for eval results, experiment results, learning records, decision records, and capability gap reviews.
4. Add or update local instructions so agents know when to save results.
5. Add or update local README files explaining what should and should not be recorded.
6. Preserve privacy boundaries: do not store secrets, credentials, raw transcripts, private payloads, or customer data.
7. Recommend next project-specific automation only after several manual successful runs.

## Outputs

- Local KORA operational directories.
- Local templates.
- Local README updates.
- Optional local skill for recording eval results.
- Summary of what should be saved and what should not be saved.

## Required Knowledge

- `knowledge/agentic-systems/eval-driven-agentic-work.md`
- `knowledge/agentic-systems/memory-and-learning-boundaries.md`
- `knowledge/agentic-systems/capability-routing-heuristics.md`

## Optional Knowledge

- Project `.kora/context/`.
- Project-specific evals and skills.
- Recent eval results or experiments.

## Required Tools

None by default.

## Optional Tools

- Filesystem writer.
- Git status.

## Evals

Review for:

- correct local placement;
- no sensitive data storage;
- templates are practical;
- project-specific records stay local;
- reusable knowledge stays in KORA Core;
- automations are not enabled prematurely.

## Approval Points

Human approval is required before creating or updating `.kora/` operational files in a project repository.

## Boundaries

This skill sets up local operational recording. It does not automatically run evals, create background jobs, access accounts, or publish results.

## Related

- `skills/setup-kora-project.md`
- `skills/review-capability-gaps.md`
- `skills/record-learning.md`
- `skills/promote-learning.md`
