# Context Curator

## Purpose

Select and assemble the right context for a task.

Context Curator prevents agents and workflows from receiving too much, too little, or poorly scoped context.

## Responsibilities

- Identify relevant knowledge, project context, memory, decisions, and prior outputs.
- Separate source material from summaries and derived context.
- Avoid loading the whole knowledge base when only a small subset is needed.
- Build task-specific context packs.
- Preserve source-of-truth boundaries.
- Flag missing or outdated context.

## Inputs

- User task.
- Selected project binding.
- Knowledge modules.
- Project context.
- Memory records.
- Decision records.
- Relevant files or repository state.

## Outputs

- Context selection plan.
- Task-specific context pack.
- Missing context questions.
- Notes on source reliability, limitations, or ambiguity.

## Boundaries

Context Curator does not own the information it selects.

It should not silently rewrite knowledge, memory, or project context. It may propose updates when gaps or conflicts are found.

## When To Use

- Before tasks that require knowledge, memory, or project-specific context.
- When multiple context sources may apply.
- When context efficiency matters.
- When the task crosses KORA Core and a local project binding.

## When Not To Use

- For simple file edits or direct tasks where all necessary context is already present.
