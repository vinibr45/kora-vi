# review-knowledge-entry

## Purpose

Review a KORA knowledge entry for clarity, reuse, structure, evidence, and boundary correctness.

This skill helps keep the knowledge base useful for humans, agents, skills, and future context selection.

## When To Use

- Before marking a knowledge entry as active.
- When editing or restructuring existing knowledge.
- When checking whether a document contains project-specific contamination.
- When verifying whether sources, limitations, or metadata are adequate.
- When a knowledge entry may be too broad, vague, duplicated, or hard to retrieve.

## Inputs

- Knowledge entry file or draft.
- Knowledge specification.
- Knowledge taxonomy.
- Related project context, if relevant.
- Sources or evidence, if available.

## Process

1. Check whether the entry is reusable across projects.
2. Check whether any project-specific information should be moved to local `.kora/` context, memory, or decisions.
3. Check whether the title, type, domain, subdomain, status, evidence level, sources, and related metadata are useful.
4. Check whether the entry is modular enough for context selection.
5. Check whether the core idea is clear.
6. Check when-to-use, when-not-to-use, application, examples, limitations, sources, and related sections.
7. Identify duplication or overlap with existing knowledge.
8. Recommend status: draft, active, deprecated, or needs revision.

## Outputs

- Review result.
- Required fixes.
- Suggested improvements.
- Scope or contamination warnings.
- Evidence or source gaps.
- Recommended lifecycle status.

## Pass Criteria

A knowledge entry is healthy when it is:

- reusable;
- clear;
- modular;
- easy to select as context;
- properly scoped;
- not contaminated by local project facts;
- honest about evidence and limitations;
- connected to related knowledge when useful.

## Boundaries

This skill reviews knowledge. It does not automatically promote entries to active status when evidence, scope, or approval is missing.
