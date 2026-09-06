# setup-kora-project

## Purpose

Set up or propose a KORA project binding for an operational repository.

This skill turns the Project Context model into an assisted setup workflow.

## When To Use

- When the user says to connect, integrate, bind, or set up a project with KORA.
- When opening a repository that should use KORA.
- When a project needs a local `.kora/` layer.
- When KORA needs a lightweight Core registry entry for a project.

## When Not To Use

- For projects that should not use KORA.
- For simple one-off file edits in a repository.
- When the user has not approved creating files in the target project repository.
- When the target repository path is unknown.

## Inputs

- Project name.
- Project repository path.
- KORA Core path.
- Existing project documentation.
- Existing `AGENTS.md`, if any.
- Existing `.kora/`, if any.
- User-provided project purpose.
- Desired setup level.

## Setup Levels

```text
Level 1: Core registry only
Level 2: Local binding file
Level 3: Initial local context files
Level 4: AGENTS.md connection instructions
Level 5: Capability diagnosis
Level 6: Approved local capabilities
Level 7: Operational loop for eval results, experiments, memory, decisions, and capability gaps
Level 8: Tool-supported execution
Level 9: Integrated execution
Level 10: Safe automation
```

## Process

1. Confirm or detect the project repository path.
2. Inspect project documentation and existing local instructions.
3. Check whether `.kora/` already exists.
4. Create or update lightweight KORA Core registry entry under `projects/<project-name>/`.
5. Create or propose local `.kora/binding.md` using the project binding template.
6. Create only useful local folders or files for the requested setup level.
7. Create or propose a local decision record for the KORA binding.
8. Update or propose `AGENTS.md` instructions so Codex knows to consult KORA Core and local `.kora/` context.
9. Run a capability diagnosis using `create-capability-plan`.
10. Ask for approval before creating integrations, automations, or project-specific agents/skills.
11. For Level 7, create the local operational loop structure, templates, and result-recording instructions.
12. Treat Levels 8 to 10 as advanced phases that require stable workflows, evals, approvals, and explicit user consent.

## Outputs

- KORA Core project registry entry.
- Local `.kora/binding.md`.
- Optional local context files.
- Optional local decision record.
- Optional `AGENTS.md` integration instructions.
- Capability diagnosis.
- Missing context checklist.
- Optional operational loop structure for eval results, experiments, memory, decisions, and capability gaps.

## Required Skills

- `bind-project-to-kora`
- `classify-task`
- `classify-scope`
- `create-project-context`
- `review-project-context`
- `create-capability-plan`
- `record-decision`

## Required Knowledge

- KORA Project Context Specification v0.3
- KORA Skills Specification v0.4

## Approval Points

Ask before:

- writing to an external project repository;
- changing `AGENTS.md`;
- creating local agents or skills;
- creating tools, integrations, or automations;
- touching deployment, publishing, accounts, or credentials.

## Boundaries

This skill should not copy KORA Core into the project.

It should not store full project strategy in KORA Core.

It should not create project-specific capabilities globally.

It is an assisted workflow in v0.4, not a fully automated setup script.
