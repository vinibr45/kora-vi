# create-project-context

## Purpose

Create or propose project-specific context files for a KORA-bound project.

This skill helps a project define its local reality without storing project-specific details in KORA Core.

## When To Use

- When creating a new project context.
- When connecting a repository to KORA.
- When a project needs files such as overview, identity, audience, positioning, offers, services, operations, brand, stack, or constraints.
- When a task requires project context that does not exist yet.

## Inputs

- Project name.
- Project repository path.
- Project binding, if available.
- User-provided project description.
- Existing project documentation.
- Project context specification.
- Project context template.

## Process

1. Identify the project and its operational repository.
2. Confirm whether the project has a local `.kora/` binding.
3. Identify which context files are useful now.
4. Avoid creating every possible context file by default.
5. Separate local project facts from reusable KORA knowledge.
6. Draft or create context files using the project context template.
7. Mark unknowns as open questions instead of inventing answers.
8. Identify related decisions, memory, agents, skills, tools, or evals when relevant.

## Outputs

- Proposed or created project context files.
- Missing context checklist.
- Local/global boundary notes.
- Open questions.
- Related references.

## Recommended Files

Possible files inside a local `.kora/context/`:

```text
overview.md
identity.md
audience.md
positioning.md
offers.md
products-or-services.md
strategy.md
operations.md
communication.md
brand.md
stack.md
constraints.md
```

Create only what is useful for the current task or approved setup.

## Boundaries

This skill should not place full project context inside KORA Core.

It should not invent business strategy, audience, offers, or positioning when the source is missing.

It should not create local agents, skills, tools, or automations unless the Capability Router recommends them and the user approves important structural changes.
