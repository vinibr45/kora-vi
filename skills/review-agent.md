# review-agent

## Purpose

Review a KORA agent for clarity, scope, permissions, boundaries, and fit with the KORA Agents Specification.

This skill helps keep agents focused, useful, permissioned, and separate from skills, knowledge, tools, evals, memory, and project context.

## When To Use

- Before marking an agent as active.
- After creating or editing an agent.
- When an agent may be too broad, vague, duplicated, overpowered, or misplaced.
- When deciding whether a local agent should become global.
- When checking whether an agent should actually be a skill, tool, eval, knowledge entry, decision, or automation.

## When Not To Use

- For reviewing ordinary task outputs directly.
- For reviewing skill definitions; use `review-skill` instead.
- For reviewing knowledge entries; use `review-knowledge-entry` instead.

## Inputs

- Agent file or draft.
- KORA Agents Specification.
- Related skills, knowledge, tools, evals, decisions, and project binding.
- User task or capability plan that motivated the agent.

## Process

1. Check whether the agent has a clear purpose.
2. Check whether the agent should exist or whether direct execution or a skill is enough.
3. Check whether the agent type is correct.
4. Check whether the scope is global, local, or hybrid.
5. Check whether the destination matches the scope.
6. Check whether responsibilities and non-responsibilities are clear.
7. Check context access, allowed skills, allowed tools, and required evals.
8. Check permissions and approval points.
9. Check whether the agent duplicates skill procedures, knowledge content, tool behavior, eval criteria, memory, or decisions.
10. Check handoff rules.
11. Recommend status: draft, active, deprecated, or needs revision.

## Outputs

- Review result.
- Recommended status.
- Required fixes.
- Scope or placement warnings.
- Permission warnings.
- Duplication warnings.
- Missing sections or metadata.
- Suggested improvements.

## Pass Criteria

An agent is healthy when it is:

- role-specific;
- clearly scoped;
- not too broad;
- permissioned;
- clear about approval points;
- connected to relevant skills and evals;
- not duplicating knowledge, tools, or skill procedures;
- placed correctly as global, local, or hybrid;
- clear about handoffs.

## Boundaries

This skill reviews agent definitions. It does not automatically grant tool access, create automations, or promote local agents to KORA Core without approval.
