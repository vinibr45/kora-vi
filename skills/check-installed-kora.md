# check-installed-kora

## Purpose

Check whether an operational repository is correctly connected to KORA.

This skill validates the local `.kora/` installation shape and whether the repository has enough instructions for an agent to use KORA without the user repeating the setup.

## When To Use

- When the user asks if KORA is installed in a repository.
- Before using KORA from inside another repository.
- After running `setup-kora-project` or `bind-project-to-kora`.
- When a connected project behaves inconsistently.
- When the user says "verifica a instalacao da KORA aqui" or similar.

## When Not To Use

- When working directly inside KORA Core.
- When the user only wants a simple file edit with no KORA involvement.
- When the repository path is unknown.

## Inputs

- Current repository path.
- Expected KORA Core path.
- Local `.kora/` files.
- Local `AGENTS.md`.
- KORA Core project registry entry, if available.
- KORA Core installed-project registry entry, if available.

## Process

1. Check for `.kora/binding.md`.
2. Check whether the binding records:

```text
project name
repository path
KORA Core path
purpose
local owns
uses from KORA Core
boundaries
missing context
```

3. Check for useful local folders:

```text
.kora/context/
.kora/decisions/
.kora/memory/
.kora/skills/
.kora/agents/
.kora/tools/
.kora/evals/
.kora/automations/
.kora/experiments/
```

4. Check whether local `AGENTS.md` tells the agent to read `.kora/binding.md` and use KORA Core.
5. Check whether KORA Core has a lightweight registry entry for the project.
6. Check whether `projects/INSTALLED-KORA.md` lists the project path, binding path, local `AGENTS.md`, installed KORA version, status, and last checked date.
7. Classify installation health:

```text
not installed
partial
installed
installed and operational
needs repair
```

8. Recommend the smallest repair or setup step.

## Outputs

- Installation status.
- Missing files or weak instructions.
- Core-vs-local boundary warnings.
- Recommended setup level.
- Next action.

## Boundaries

This skill checks installation. It does not create or repair files unless paired with `setup-kora-project`, `bind-project-to-kora`, or explicit user request.

## Related

```text
skills/use-installed-kora.md
skills/setup-kora-project.md
skills/bind-project-to-kora.md
projects/PROJECT-FLOW.md
projects/templates/local-agents-template.md
```
