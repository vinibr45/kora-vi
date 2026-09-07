# use-installed-kora

## Purpose

Use KORA from inside an operational repository that already has a local `.kora/` binding.

This skill defines how an agent should behave when the current repository is not KORA Core, but has KORA installed through a local project binding.

## When To Use

- When the current repository contains `.kora/binding.md`.
- When the user asks for work inside a KORA-connected project without mentioning KORA.
- When a local `AGENTS.md` says the repository uses KORA Core.
- When deciding whether to use KORA Core capabilities or local project capabilities.
- When the user asks "usa a KORA nesse projeto", "esse repo ja esta conectado?", or similar.

## When Not To Use

- When working directly inside KORA Core.
- When the repository has no `.kora/` binding and the user has not asked to connect it.
- When the task is a simple local edit that does not need KORA context or capabilities.

## Inputs

- Current repository path.
- Local `.kora/binding.md`.
- Local `.kora/context/`, if present.
- Local `AGENTS.md`, if present.
- KORA Core path from the binding.
- Installed-project registry entry in KORA Core, if available.
- Relevant KORA Core entry points, skills, agents, knowledge, tools, evals, and governance.

## Process

1. Detect whether the current repository has:

```text
.kora/binding.md
AGENTS.md
```

2. Read `.kora/binding.md` first.
3. Identify the KORA Core path from the binding.
4. Check whether the repository appears in `C:\KORA\projects\INSTALLED-KORA.md`.
5. Confirm the target scope:

```text
local project work
KORA Core improvement
hybrid reusable pattern
external system
unknown
```

6. Select local context before Core context when the task depends on project reality.
7. Use KORA Core capabilities when the task is generic and reusable.
8. Use local `.kora/` capabilities when the task depends on project identity, stack, audience, client, operations, or local decisions.
9. Keep outputs in the operational repository unless the task explicitly improves KORA Core.
10. If a local pattern appears reusable across projects, recommend promotion through KORA Core review instead of copying it directly.
11. Check approval before external actions, account access, publishing, deploys, spend, automation activation, or sensitive data handling.

## Outputs

- Installed-KORA context summary.
- Local-vs-Core scope decision.
- Selected local and/or Core capabilities.
- Execution plan or direct action.
- Optional promotion, learning, or capability-gap recommendation.

## Installed Repository Rules

```text
Read local .kora/binding.md before assuming project identity.
Local project reality beats generic Core assumptions.
KORA Core supplies reusable methods.
Local .kora/ supplies project-specific context and capabilities.
Do not copy KORA Core into the project.
Do not store project secrets or sensitive data in KORA Core.
Promote reusable learning only through review.
```

## Approval Points

Ask before:

- creating or changing local project `.kora/` files unless the user asked for setup or maintenance;
- changing KORA Core from a project repository;
- promoting local content into KORA Core;
- connecting external systems;
- publishing, sending, scheduling, deploying, spending, or activating automation.

## Boundaries

This skill uses an existing KORA installation. It does not install KORA into a repository by itself.

Use `skills/setup-kora-project.md` or `skills/bind-project-to-kora.md` when installation or binding is missing.

## Related

```text
skills/check-installed-kora.md
skills/setup-kora-project.md
skills/bind-project-to-kora.md
skills/select-context.md
skills/classify-scope.md
skills/check-approval-needed.md
projects/PROJECT-FLOW.md
projects/templates/local-agents-template.md
```
