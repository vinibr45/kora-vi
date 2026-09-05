# review-project-context

## Purpose

Review project-specific context for clarity, completeness, freshness, boundaries, and usefulness.

This skill checks whether a project has enough local context for KORA agents and skills to work well.

## When To Use

- After creating or editing project context.
- Before using a project context for recurring work.
- When a task produces poor output due to missing or unclear project information.
- When checking whether local project context is contaminated with global knowledge, memory, decisions, or implementation details.

## Inputs

- Project binding.
- Local `.kora/context/` files.
- Local decisions and memory, if relevant.
- KORA Project Context Specification.
- Existing project documentation.
- Current user task, if review is task-specific.

## Process

1. Check whether the project identity is clear.
2. Check whether audience, positioning, offers, services/products, communication, operations, stack, and constraints are defined where needed.
3. Identify missing or outdated context.
4. Check whether reusable knowledge was incorrectly stored locally.
5. Check whether project-specific facts were incorrectly stored in KORA Core.
6. Check whether decisions and memory are separated from stable context.
7. Check for sensitive information that should not be stored.
8. Determine context completeness level: level-0, level-1, level-2, level-3, or level-4.
9. Recommend focused improvements.

## Outputs

- Review summary.
- Context completeness level.
- Missing context list.
- Boundary issues.
- Sensitive information warnings.
- Recommended next context files or edits.

## Pass Criteria

Project context is healthy when it is:

- local to the project;
- clear enough for agents and skills;
- separated from global knowledge;
- separated from decisions and memory;
- honest about unknowns;
- free from unnecessary sensitive information;
- not duplicated inside KORA Core.

## Boundaries

This skill reviews project context. It does not rewrite project strategy without user approval.

It should not promote local project facts into global knowledge without `promote-learning` and `classify-scope`.
