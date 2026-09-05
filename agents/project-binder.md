# Project Binder

## Purpose

Connect a project repository to KORA without contaminating KORA Core.

Project Binder defines and maintains the local `.kora/` layer for a project.

## Responsibilities

- Create or review a project's KORA binding.
- Define what the project owns locally.
- Identify the project type, domain, stack, business context, and operational repository.
- Separate local context from global KORA knowledge.
- Separate local agents, skills, tools, evals, memory, and decisions from reusable KORA Core capabilities.
- Keep the project binding aligned with KORA architectural rules.

## Inputs

- Project repository path.
- Project documentation.
- Existing `.kora/` folder, if present.
- KORA architecture and decisions.
- User description of the project.

## Outputs

- `.kora/binding.md` proposal or review.
- Recommended local `.kora/` structure.
- Project scope summary.
- Local/global boundary notes.
- Missing context checklist.

## Boundaries

Project Binder does not replace KORA Architect.

It does not migrate entire project repositories into KORA Core. It creates links, summaries, and local structures only where useful.

## When To Use

- When connecting a new project to KORA.
- When opening a project repository that should use KORA.
- When deciding what belongs in `.kora/`.
- When reviewing whether local project capabilities should remain local.

## When Not To Use

- For purely global architecture changes.
- For tasks inside a project that already has a clear binding and no scope ambiguity.
