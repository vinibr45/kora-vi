# use-kora

## Purpose

Guide a user through the practical use of KORA for a task or project.

This skill turns the KORA architecture into an understandable workflow.

## When To Use

- When the user asks how to use KORA.
- When the user is confused about what KORA does.
- When starting a new task and the user wants KORA-oriented guidance.
- When deciding whether to use KORA Core or a local `.kora/` project binding.
- When explaining which KORA agent or skill should be used next.

## When Not To Use

- When the user already gave a clear implementation task that can be handled directly.
- When a capability plan is already required; use `create-capability-plan`.
- When connecting a project; use `setup-kora-project` or `bind-project-to-kora`.
- When creating a specific capability; use the appropriate `create-*` skill.

## Inputs

- User question or task.
- Current repository path, if relevant.
- KORA Core path.
- Project binding, if relevant.
- Existing KORA specifications, agents, skills, and decisions.

## Process

1. Restate the user's goal in simple language.
2. Identify whether the user is asking about:

```text
understanding KORA
using KORA for a task
connecting a project
creating knowledge
creating project context
creating a skill
creating an agent
using tools/integrations/automations
running evals
recording learning
```

3. Identify scope:

```text
Global -> KORA Core
Local -> project `.kora/`
Hybrid -> KORA pattern plus local adaptation
```

4. Recommend the next KORA workflow:

```text
Simple task -> execute directly
Project setup -> setup-kora-project
Complex task -> create-capability-plan
Knowledge work -> create/review knowledge entry
Project context -> create/review project context
New procedure -> create/review skill
New role -> create/review agent
External system -> assess-integration-need
Quality check -> create/run/review eval
Learning -> record/review/promote learning
```

5. Explain which agent should help:

```text
KORA Guide -> explain and navigate
Capability Router -> decide capability path
KORA Architect -> protect architecture
Project Binder -> connect project
Context Curator -> select context
Knowledge Steward -> organize knowledge
```

6. Identify common mistakes to avoid.
7. Provide the smallest useful next step.

## Outputs

- Practical KORA usage explanation.
- Recommended workflow.
- Recommended agent or skill.
- Scope guidance.
- Next step.

## Common Mistakes To Avoid

- Putting project-specific details in KORA Core.
- Creating agents when a skill is enough.
- Creating integrations before checking manual or assisted options.
- Creating automations before the workflow is stable.
- Treating eval results as automatic truth.
- Promoting local learning into global knowledge without evidence or approval.
- Loading all knowledge instead of selecting relevant context.

## Required Agents

- `KORA Guide`

## Related Skills

- `classify-task`
- `classify-scope`
- `create-capability-plan`
- `setup-kora-project`
- `select-context`
- `assess-integration-need`
- `record-learning`
- `promote-learning`

## Boundaries

This skill teaches and routes. It does not replace specialized skills.

It should not create files or change source-of-truth stores unless paired with the appropriate creation skill and user approval.
