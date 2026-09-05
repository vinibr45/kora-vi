# create-agent

## Purpose

Create or propose a KORA agent using the KORA Agents Specification.

This skill helps KORA define global, local, or hybrid agents only when a stable role is justified.

## When To Use

- When a capability plan recommends creating an agent.
- When the user explicitly asks to create an agent.
- When recurring work needs a stable role.
- When specialized judgment or a distinct permission boundary is needed.
- When several skills need to be coordinated under a named role.
- When a local project needs a custom agent.

## When Not To Use

- When direct execution is enough.
- When a skill alone is enough.
- When a tool alone is enough.
- When an existing agent already fits.
- When the role is vague or premature.
- When the agent would place project-specific behavior inside KORA Core.

## Inputs

- User request or capability plan.
- Task classification.
- Scope classification.
- Existing agents.
- Agent specification.
- Agent template.
- Related skills, knowledge, tools, evals, decisions, and project binding.

## Process

1. Confirm why a new agent is needed.
2. Check existing global and local agents for overlap.
3. Classify the agent type: architect, router, binder, curator, steward, specialist, reviewer, or operator.
4. Classify scope: global, local, or hybrid.
5. Choose destination:

```text
Global -> C:\KORA\agents\
Local -> <project-repository>\.kora\agents\
Hybrid -> reusable base in KORA Core, local adaptation in project `.kora/agents/`
```

6. Define purpose, responsibilities, non-responsibilities, inputs, outputs, context access, allowed skills, allowed tools, required evals, permissions, approval points, boundaries, and handoffs.
7. Apply `agents/templates/agent-template.md` when a full structured agent is useful.
8. Ask for approval before creating local project files, tools, integrations, automations, or agents with significant behavioral impact.

## Outputs

- New agent file or agent proposal.
- Scope classification.
- Destination path.
- Permission and approval notes.
- Related skill/tool/eval notes.
- Duplication warning, if relevant.

## Required Skills

- `classify-task`
- `classify-scope`
- `create-capability-plan`
- `select-context`

## Required Knowledge

- `docs/agents/kora-agents-spec-v0.5.md`
- `agents/templates/agent-template.md`

## Boundaries

This skill creates agent definitions. It does not create autonomous runtime workers.

It should not create project-specific agents inside KORA Core.

It should not use an agent to store knowledge, project context, or tool implementation details.
