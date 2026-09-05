# select-context

## Purpose

Select the context needed for a task without loading everything.

This skill helps KORA remain context-efficient and source-of-truth aware.

## When To Use

- Before tasks requiring knowledge, project context, memory, or decisions.
- When multiple context sources may apply.
- When working across KORA Core and a local project binding.
- When outdated, missing, or conflicting context may affect output quality.

## Inputs

- User task.
- Task classification.
- Project binding.
- Available knowledge domains.
- Available project context.
- Memory records.
- Decision records.
- Relevant repository files.

## Process

1. Identify required context categories.
2. Locate candidate sources.
3. Separate primary sources from summaries or derived notes.
4. Select only context relevant to the task.
5. Note missing context, uncertainty, and limitations.
6. Produce a compact context pack for the acting agent or workflow.

## Outputs

- Context selection summary.
- Context pack.
- Sources used.
- Missing context questions.
- Reliability or limitation notes.

## Boundaries

This skill selects and summarizes context. It does not silently change knowledge, memory, or project context.
