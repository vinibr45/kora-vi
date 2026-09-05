# Eval Result: EV-0007 Marcos Dev Binding Bootstrap

## Eval

Eval file: evals/scenarios/EV-0007-project-context-binding.md
Date: 2026-09-05
Evaluator: Codex
Project: Marcos Dev
Scope: implementation / project-binding

## Result

Status: needs-revision

## Summary

Marcos Dev now has a local `.kora/` binding and KORA Core has a lightweight project registry updated to `level-1 bound`.

The bootstrap satisfies the core placement rule, but remains `needs-revision` because `AGENTS.md` was not updated and detailed project context is intentionally incomplete.

## Evidence

Created in Marcos Dev operational repository:

```text
.kora/binding.md
.kora/context/overview.md
.kora/context/stack.md
.kora/decisions/DR-0001-kora-binding.md
.kora/memory/README.md
.kora/agents/README.md
.kora/skills/README.md
.kora/tools/README.md
.kora/evals/README.md
.kora/automations/README.md
.kora/experiments/README.md
```

Updated in KORA Core:

```text
projects/marcos-dev/README.md
docs/implementation/kora-reference-implementation-bootstrap-v1.0.md
architecture/decisions/DR-0018-marcos-dev-reference-implementation.md
```

## Findings

- KORA Core keeps only lightweight Marcos Dev registry information.
- Marcos Dev-specific context and future capabilities now have a local `.kora/` destination.
- No agents, skills, integrations, automations, account access, publishing, or deployment workflows were created.
- `AGENTS.md` was not changed because the Marcos Dev repository already had existing modifications.
- Marcos Dev local context is still minimal and should be expanded later.

## Required Fixes

- Decide whether and how to update Marcos Dev `AGENTS.md` with KORA connection instructions.
- Fill missing local context when ready: audience, offers, positioning, tone of voice, content strategy, and local capability needs.

## Recommendations

- Keep the bootstrap as level-1 until local context is filled.
- Run `review-project-context` after adding local context files.
- Create local agents or skills only after real recurring Marcos Dev tasks justify them.

## Learning

The KORA binding model is usable for a real project, but the setup should include an explicit AGENTS.md integration step once existing repository changes are safe to edit.

## Follow-Up

Possible next step: create a proposed KORA section for Marcos Dev `AGENTS.md` without applying it automatically.
