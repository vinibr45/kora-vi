# maintain-kora-indexes

## Purpose

Keep KORA entry points, indexes, examples, and project guides aligned with the real state of the repository.

This skill makes KORA easier to maintain organically as users create, edit, or retire agents, skills, tools, integrations, automations, evals, projects, examples, knowledge, decisions, and learning records.

## When To Use

- After creating, renaming, moving, or deprecating a KORA capability.
- After adding or changing agents, skills, tools, integrations, automations, evals, examples, or project flow files.
- After binding a new project to KORA.
- After promoting local learning into KORA Core.
- When `CAPACIDADES.md`, `COMECE-AQUI.md`, `AGENTS.md`, `README.md`, or folder README files may be stale.
- When a durable improvement may require `VERSION.md` or `CHANGELOG.md` updates.
- During a periodic KORA maintenance pass.

## When Not To Use

- For a small content edit that does not affect navigation, capability discovery, examples, or routing.
- For project-specific updates that remain entirely inside a local `.kora/` binding and do not change KORA Core.
- For experimental notes that have not been reviewed or promoted.

## Inputs

- Changed files or planned changes.
- Current `git status` and relevant diffs.
- Existing repository entry points:

```text
README.md
AGENTS.md
COMECE-AQUI.md
CAPACIDADES.md
VERSION.md
CHANGELOG.md
MATURIDADE.md
GOVERNANCA.md
projects/PROJECT-FLOW.md
examples/
```

- Relevant folder indexes:

```text
agents/README.md
skills/README.md
tools/README.md
integrations/README.md
automations/README.md
evals/README.md
experiments/README.md
projects/README.md
knowledge/README.md
```

## Process

1. Identify what changed:

```text
agent
skill
tool
integration
automation
eval
experiment
project
example
knowledge
decision
learning
entry point
```

2. Decide whether the change affects discovery, routing, examples, or project flow.
3. Update the nearest folder README when a new durable artifact was added or removed.
4. Update `CAPACIDADES.md` when a capability was added, removed, renamed, or materially changed.
5. Update `AGENTS.md` when agent-facing behavior, default routing, maintenance expectations, or repository rules changed.
6. Update `COMECE-AQUI.md` when the human entry flow changes or when a new common path should be easy to find.
7. Update `README.md` only for top-level entry points or major architecture milestones.
8. Update `projects/PROJECT-FLOW.md` when project binding, local `.kora/`, or core-vs-project rules change.
9. Add or update `examples/` when a repeated real-world request would help future use.
10. Update `MATURIDADE.md` when capability maturity changes.
11. Update `GOVERNANCA.md` when approval, safety, or human-control rules change.
12. If the maintenance change represents an architecture decision, create or update a decision record.
13. If the change is durable, assess version impact with `skills/assess-kora-version-impact.md`.
14. If versioning is justified, update `VERSION.md` and `CHANGELOG.md` with `skills/release-kora-version.md`.
15. Run a quick consistency check:

```text
missing links
stale names
unlisted new files
wrong core-vs-project placement
duplicate capability descriptions
```

16. Summarize what was updated and what was intentionally left alone.

## Outputs

- Updated indexes, entry points, examples, project flow docs, or folder READMEs.
- List of maintenance actions performed.
- List of files intentionally not updated, if relevant.
- Recommendation for learning, decision, or eval follow-up when needed.

## Maintenance Matrix

```text
New skill -> skills/README.md, CAPACIDADES.md, maybe AGENTS.md, maybe examples/
New agent -> agents/README.md, CAPACIDADES.md, maybe AGENTS.md
New tool -> tools/README.md, CAPACIDADES.md, maybe integration or approval notes
New integration -> integrations/README.md, CAPACIDADES.md, maybe assess-integration-need references
New automation -> automations/README.md, CAPACIDADES.md, maybe AGENTS.md
New eval -> evals/README.md or evals/scenarios/README.md, CAPACIDADES.md when important
New project -> projects/README.md, projects/<name>/README.md, maybe projects/PROJECT-FLOW.md
New installed project -> projects/INSTALLED-KORA.md, projects/README.md, maybe project local AGENTS.md and .kora/README.md
New example -> examples/README.md, maybe COMECE-AQUI.md if it becomes a main path
Promoted learning -> knowledge/README.md or specific knowledge index, maybe skill updates
Architecture decision -> architecture/decisions/, maybe README.md if top-level behavior changes
Health check route -> AGENTS.md, COMECE-AQUI.md, CAPACIDADES.md, evals/scenarios/README.md
Version governance -> VERSION.md, CHANGELOG.md, AGENTS.md, COMECE-AQUI.md, CAPACIDADES.md, README.md
Governance or maturity -> GOVERNANCA.md, MATURIDADE.md, AGENTS.md, COMECE-AQUI.md, CAPACIDADES.md
Installed KORA support -> projects/PROJECT-FLOW.md, projects/templates/, AGENTS.md, COMECE-AQUI.md, CAPACIDADES.md, projects/README.md
Installed project registry -> projects/INSTALLED-KORA.md, skills/register-installed-kora-project.md, skills/check-installed-kora.md
```

## Required Knowledge

```text
knowledge/agentic-systems/memory-and-learning-boundaries.md
knowledge/agentic-systems/context-selection-principles.md
knowledge/agentic-systems/capability-routing-heuristics.md
```

## Optional Knowledge

Domain knowledge related to the changed capability.

## Required Tools

Filesystem and repository inspection tools.

## Optional Tools

None.

## Evals

Useful eval scenarios:

```text
evals/scenarios/EV-0010-orchestration-flow.md
evals/scenarios/EV-0011-eval-creation-and-result-handling.md
evals/scenarios/EV-0012-experiment-learning-promotion.md
evals/scenarios/EV-0013-tool-integration-automation-decision.md
evals/scenarios/EV-0014-kora-health-check.md
```

## Approval Points

Ask for human approval before:

- promoting local project content into KORA Core;
- changing repository-wide operating rules;
- marking an automation as active;
- deleting, renaming, or deprecating a public entry point.

## Boundaries

This skill maintains KORA documentation and routing surfaces. It does not create autonomous runtime behavior by itself.

Organic maintenance means the agent should apply this skill during relevant work. It does not mean files update without an agent run, script, automation, or user-triggered maintenance pass.

## Related

```text
automations/kora-index-maintenance.md
skills/route-user-request.md
skills/classify-scope.md
skills/record-learning.md
skills/promote-learning.md
skills/assess-kora-version-impact.md
skills/release-kora-version.md
agents/kora-architect.md
agents/capability-router.md
agents/knowledge-steward.md
```
