---
name: "kora-index-maintenance"
scope: global
status: proposed
owner: "Marcos"
trigger: "after durable KORA artifact changes or manual maintenance request"
frequency: "event-driven or periodic"
permission_level: repository-write
related_agents:
  - agents/kora-architect.md
  - agents/capability-router.md
  - agents/context-curator.md
  - agents/knowledge-steward.md
related_skills:
  - skills/maintain-kora-indexes.md
  - skills/route-user-request.md
  - skills/check-kora-health.md
  - skills/assess-kora-version-impact.md
  - skills/release-kora-version.md
  - skills/classify-scope.md
related_tools: []
related_evals:
  - evals/scenarios/EV-0010-orchestration-flow.md
  - evals/scenarios/EV-0013-tool-integration-automation-decision.md
  - evals/scenarios/EV-0014-kora-health-check.md
created_at: 2026-09-07
updated_at: 2026-09-07
---

# KORA Index Maintenance

## Purpose

Keep KORA's main entry points, indexes, examples, and project flow documentation aligned with repository changes.

This automation defines the maintenance loop that makes KORA feel organic over time.

## Scope

Global.

It applies to KORA Core and may inspect local project `.kora/` bindings when a project task explicitly includes them.

## Trigger

Run after durable changes to:

```text
agents/
skills/
tools/
integrations/
automations/
evals/
experiments/
projects/
knowledge/
architecture/decisions/
examples/
README.md
AGENTS.md
COMECE-AQUI.md
CAPACIDADES.md
VERSION.md
CHANGELOG.md
MATURIDADE.md
GOVERNANCA.md
```

Also run when the user asks:

```text
Atualiza os indices.
Revisa se a KORA ficou consistente.
Faz uma manutencao da KORA.
Deixa isso autoatualizavel.
```

## Frequency

Event-driven after relevant changes.

Periodic review may be done manually when the repository has accumulated several changes.

## Workflow

1. Inspect changed files with repository status and diffs.
2. Classify each change by artifact type and scope.
3. Use `skills/maintain-kora-indexes.md` as the operating procedure.
4. Update folder README files for newly added, removed, renamed, or materially changed artifacts.
5. Update `CAPACIDADES.md` for capability discovery.
6. Update `AGENTS.md` for agent-facing routing or maintenance behavior changes.
7. Update `COMECE-AQUI.md` for human-facing entry flow changes.
8. Update `README.md` only for top-level entry points or major changes.
9. Update `projects/PROJECT-FLOW.md` when project rules or binding flow changed.
10. Add or adjust examples when a repeated real-world request becomes clearer.
11. Update `MATURIDADE.md` when capability state changes.
12. Update `GOVERNANCA.md` when approval or safety rules change.
13. Identify whether a decision, learning record, eval, or capability gap should be recorded.
14. Assess whether the durable change deserves versioning with `skills/assess-kora-version-impact.md`.
15. Update `VERSION.md` and `CHANGELOG.md` with `skills/release-kora-version.md` when versioning is justified.
16. Report what changed and what did not need updating.

## Inputs

- Current repository status.
- Relevant diffs or changed files.
- Existing KORA entry points and folder README files.
- User request or maintenance trigger.

## Outputs

- Updated indexes and entry points.
- Updated examples or project flow docs when relevant.
- Maintenance summary.
- Optional recommendation for decision, learning, eval, or capability-gap follow-up.

## External Side Effects

None.

This automation writes only inside the repository unless the user explicitly includes an external project repository.

## Approval Points

Approval is required before:

- activating this automation as a scheduled or background process;
- modifying external repositories;
- promoting project-specific content into KORA Core;
- deleting or deprecating existing entry points;
- changing repository-wide rules that affect future agent behavior.

## Stop Conditions

Stop and ask for direction when:

- scope cannot be determined;
- user intent conflicts with KORA boundary rules;
- updates require external system access;
- the maintenance pass would require broad restructuring rather than index alignment.

## Failure Handling

If maintenance cannot be completed:

1. Report which files were updated.
2. Report which files remain stale or uncertain.
3. Identify the blocking reason.
4. Recommend the smallest follow-up action.

## Evals

Suggested manual checks:

```text
New durable artifact appears in its folder README.
Capability appears in CAPACIDADES.md when discoverable.
AGENTS.md contains current routing behavior.
COMECE-AQUI.md still gives a simple user path.
Project-specific content is not stored in KORA Core.
Examples match real workflows and do not invent unsupported capabilities.
```

## Logging And Results

Record a maintenance result only when it changes future behavior, fixes a meaningful inconsistency, or produces a reusable learning.

Possible locations:

```text
evals/results/
experiments/
memory/
architecture/decisions/
```

## Learning Behavior

Maintenance findings may feed:

```text
record-learning
promote-learning
record-decision
review-capability-gaps
```

Do not promote local or one-off findings without review.

## Related

```text
skills/maintain-kora-indexes.md
skills/route-user-request.md
skills/check-kora-health.md
skills/assess-kora-version-impact.md
skills/release-kora-version.md
CAPACIDADES.md
COMECE-AQUI.md
AGENTS.md
VERSION.md
CHANGELOG.md
MATURIDADE.md
GOVERNANCA.md
projects/PROJECT-FLOW.md
examples/
architecture/decisions/DR-0021-organic-maintenance-layer.md
architecture/decisions/DR-0022-organic-version-governance.md
architecture/decisions/DR-0023-operating-governance-and-maturity.md
architecture/decisions/DR-0024-installed-kora-project-usage.md
```
