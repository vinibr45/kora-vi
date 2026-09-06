---
title: "Skill Design Principles"
type: framework
domain: "agentic-systems"
subdomain: "skills"
status: draft
version: "0.1"
evidence_level: internal_framework
sources:
  - docs/skills/kora-skills-spec-v0.4.md
related:
  - skills/templates/skill-template.md
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Skill Design Principles

## Summary

A skill is a reusable procedure for doing a task, making a structured decision, reviewing an output, or creating a capability.

Skills improve consistency without requiring a new agent for every repeated task.

## Core Idea

Create a skill when a process is repeatable, useful, teachable, and reviewable.

A skill should define:

- purpose;
- when to use;
- when not to use;
- inputs;
- process;
- outputs;
- required knowledge;
- optional knowledge;
- tools;
- evals;
- approval points;
- boundaries.

The skill should reference knowledge instead of duplicating the full theory.

## When To Use

- A task repeats.
- The process needs consistency.
- Quality criteria matter.
- Multiple agents could reuse the same procedure.
- The skill can reduce repeated explanation.
- A local project needs a stable custom workflow.

## When Not To Use

- The task is tiny and unlikely to repeat.
- Direct execution is enough.
- The procedure is unclear.
- The task is really an agent, tool, eval, knowledge entry, or decision record.
- It duplicates an existing skill.

## How To Apply

Use this test:

```text
Can I explain the procedure in steps?
Will this happen again?
Can another agent or human reuse it?
Are inputs and outputs clear?
Are boundaries clear?
Can quality be evaluated?
```

If yes, create or improve a skill. If not, execute directly or create a capability plan.

## Examples

Good skill:

```text
create-commercial-proposal: turns buyer context, scope, offer, timeline, and investment into a proposal draft.
```

Weak skill:

```text
make-business-better: too vague, too broad, no clear input or output.
```

## Limitations

Too many narrow skills create clutter. Skills should be specific enough to guide work and broad enough to be reused.

## Sources

- `docs/skills/kora-skills-spec-v0.4.md`

## Related

- `skills/create-skill.md`
- `skills/review-skill.md`

