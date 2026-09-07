# bind-project-to-kora

## Purpose

Connect a project repository to KORA through a local `.kora/` binding.

This skill lets a project use KORA without copying the entire architecture or contaminating KORA Core with project-specific details.

## When To Use

- When connecting a new repository to KORA.
- When a project should start using KORA for agents, skills, context, memory, decisions, tools, evals, or automations.
- When reviewing whether an existing project has a clean KORA binding.
- When making a repository usable with KORA without requiring the user to mention KORA in every request.

## Inputs

- Project repository path.
- Project name.
- Project type: business, software, content, client project, personal project, or other.
- Existing repository documentation.
- Existing `AGENTS.md`, if any.
- Existing `.kora/README.md`, if any.
- KORA Core path.
- User-provided project description.

## Process

1. Inspect the repository purpose and structure.
2. Identify whether `.kora/` already exists.
3. Define project identity and operational boundary.
4. Create or propose `.kora/binding.md`.
5. Create or propose `.kora/README.md` using `projects/templates/local-kora-readme-template.md`.
6. Create or propose local `AGENTS.md` instructions using `projects/templates/local-agents-template.md`.
7. Register or update the installation in `projects/INSTALLED-KORA.md` using `skills/register-installed-kora-project.md`.
8. Recommend local folders only when useful.
9. Record what the project owns locally.
10. Record what should remain global in KORA Core.
11. Identify missing context that should be filled later.
12. Recommend `skills/check-installed-kora.md` after setup.

## Outputs

- Local `.kora/` binding proposal or files.
- Local `.kora/README.md` proposal or file.
- Local `AGENTS.md` KORA usage instructions.
- Installed project registry entry in `projects/INSTALLED-KORA.md`.
- Project summary.
- Local/global boundary list.
- Missing context checklist.
- Recommended next project context files.

## Boundaries

This skill does not migrate the whole project into KORA.

It creates a link and a local operating layer, not a duplicate architecture.

Use `skills/use-installed-kora.md` for day-to-day work after the binding exists.
