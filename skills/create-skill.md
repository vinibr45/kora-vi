# create-skill

## Purpose

Create or propose a KORA skill using the KORA Skills Specification.

This skill helps KORA turn repeatable procedures into structured global, local, or hybrid skills.

## When To Use

- When a task is recurring enough to justify a reusable procedure.
- When a capability plan recommends creating a skill.
- When the user explicitly asks to create a skill.
- When a process needs consistency, quality criteria, approval points, or reusable structure.
- When a local project needs a custom repeatable workflow.

## When Not To Use

- When direct execution is enough.
- When the task should be an agent, tool, eval, knowledge entry, memory entry, decision record, or automation instead.
- When an existing skill already fits.
- When the process is too unclear to define.

## Inputs

- User request or capability plan.
- Task classification.
- Scope classification.
- Existing skills.
- Skill specification.
- Skill template.
- Related agents, knowledge, tools, evals, or decisions.
- Target project binding, if local or hybrid.

## Process

1. Confirm why a new skill is needed.
2. Check existing global and local skills for overlap.
3. Classify the skill type: decision, creation, review, execution, planning, integration, or automation.
4. Classify the skill scope: global, local, or hybrid.
5. Choose the correct destination:

```text
Global -> C:\KORA\skills\
Local -> <project-repository>\.kora\skills\
Hybrid -> reusable base in KORA Core, local adaptation in project `.kora/skills/`
```

6. Define purpose, when to use, when not to use, inputs, process, outputs, required knowledge, optional knowledge, required tools, optional tools, evals, approval points, boundaries, and related references.
7. Apply `skills/templates/skill-template.md` when a full structured skill is useful.
8. Ask for approval before creating local project files, integrations, automations, or skills with significant behavioral impact.

## Outputs

- New skill file or skill proposal.
- Scope classification.
- Destination path.
- Related capability notes.
- Approval points.
- Overlap or duplication warning, if relevant.

## Required Skills

- `classify-task`
- `classify-scope`
- `create-capability-plan`
- `select-context`

## Required Knowledge

- `docs/skills/kora-skills-spec-v0.4.md`
- `skills/templates/skill-template.md`

## Boundaries

This skill creates skill definitions. It does not implement tools, integrations, or automations by itself.

It should not create project-specific skills inside KORA Core.

It should not duplicate knowledge content inside the skill when the skill can reference KORA knowledge instead.
