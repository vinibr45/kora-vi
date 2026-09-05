# bind-project-to-kora

## Purpose

Connect a project repository to KORA through a local `.kora/` binding.

This skill lets a project use KORA without copying the entire architecture or contaminating KORA Core with project-specific details.

## When To Use

- When connecting a new repository to KORA.
- When a project should start using KORA for agents, skills, context, memory, decisions, tools, evals, or automations.
- When reviewing whether an existing project has a clean KORA binding.

## Inputs

- Project repository path.
- Project name.
- Project type: business, software, content, client project, personal project, or other.
- Existing repository documentation.
- KORA Core path.
- User-provided project description.

## Process

1. Inspect the repository purpose and structure.
2. Identify whether `.kora/` already exists.
3. Define project identity and operational boundary.
4. Create or propose `.kora/binding.md`.
5. Recommend local folders only when useful.
6. Record what the project owns locally.
7. Record what should remain global in KORA Core.
8. Identify missing context that should be filled later.

## Outputs

- Local `.kora/` binding proposal or files.
- Project summary.
- Local/global boundary list.
- Missing context checklist.
- Recommended next project context files.

## Boundaries

This skill does not migrate the whole project into KORA.

It creates a link and a local operating layer, not a duplicate architecture.
