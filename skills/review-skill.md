# review-skill

## Purpose

Review a KORA skill for clarity, scope, usefulness, boundaries, and fit with the KORA Skills Specification.

This skill helps keep KORA skills reusable, focused, and separate from agents, knowledge, tools, evals, decisions, and project-specific context.

## When To Use

- Before marking a skill as active.
- After creating or editing a skill.
- When a skill may be too broad, vague, duplicated, or misplaced.
- When deciding whether a local skill should become global.
- When checking if a skill should actually be an agent, tool, eval, knowledge entry, decision, memory entry, or automation.

## When Not To Use

- For reviewing business outputs directly.
- For reviewing code implementation directly unless the artifact being reviewed is a skill definition.
- For tasks that need `review-knowledge-entry` or `review-project-context` instead.

## Inputs

- Skill file or draft.
- KORA Skills Specification.
- Related agents, skills, knowledge, tools, evals, decisions, or project binding.
- User task or capability plan that motivated the skill.

## Process

1. Check whether the skill has a clear purpose.
2. Check whether the skill should exist or whether direct execution is enough.
3. Check whether the skill type is correct.
4. Check whether the scope is global, local, or hybrid.
5. Check whether the destination matches the scope.
6. Check whether the skill duplicates knowledge, agent responsibilities, tool behavior, eval criteria, memory, or decisions.
7. Check whether inputs, process, and outputs are specific enough to guide repeatable use.
8. Check whether required knowledge, tools, evals, and approval points are listed when relevant.
9. Check whether boundaries prevent misuse.
10. Recommend status: draft, active, deprecated, or needs revision.

## Outputs

- Review result.
- Recommended status.
- Required fixes.
- Scope or placement warnings.
- Duplication warnings.
- Missing sections or metadata.
- Suggested improvements.

## Pass Criteria

A skill is healthy when it is:

- repeatable;
- clearly scoped;
- useful;
- not too broad;
- not duplicative;
- placed correctly as global, local, or hybrid;
- clear about inputs, process, and outputs;
- clear about boundaries and approval points;
- connected to relevant agents, knowledge, tools, and evals.

## Boundaries

This skill reviews skill definitions. It does not automatically rewrite them unless the user asks for edits.

It should not promote a local skill into KORA Core without scope analysis and approval.
