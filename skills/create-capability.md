# create-capability

## Purpose

Create or propose the right KORA capability after a capability plan identifies what is needed.

This skill is a routing skill for capability creation. It does not replace specialized creation skills; it delegates to them.

## When To Use

- When a capability plan recommends creating or proposing a capability.
- When the user explicitly asks to create a capability but the type is not yet clear.
- When KORA needs to decide whether the new capability is an agent, skill, tool, integration, automation, eval, knowledge entry, project context, memory, or decision.

## When Not To Use

- When direct execution is enough.
- When no capability plan or clear user instruction exists for structural change.
- When the capability type is already clear and a specialized creation skill should be used directly.
- When the proposed capability would violate global/local boundaries.

## Inputs

- Capability plan.
- Task classification.
- Scope classification.
- Existing global capabilities.
- Existing local capabilities.
- User approval, when required.
- Related project binding, if local or hybrid.

## Process

1. Confirm the capability need and type.
2. Confirm scope: global, local, or hybrid.
3. Confirm destination path.
4. Check whether an existing capability already fits.
5. Identify the specialized creation skill to use:

```text
Agent -> create-agent
Skill -> create-skill
Knowledge -> create-knowledge-entry
Project context -> create-project-context
Decision -> record-decision
Learning/memory -> promote-learning
Project binding -> setup-kora-project or bind-project-to-kora
Tool -> future create-tool
Eval -> future create-eval
Integration -> future create-integration
Automation -> future create-automation
```

6. Ask for approval before creating files outside KORA Core, changing source-of-truth stores, creating integrations, automations, or accessing external systems.
7. Create or propose the capability using the correct specialized skill or template.
8. Recommend review using the matching review skill when available.

## Outputs

- Created capability or capability proposal.
- Capability type.
- Scope classification.
- Destination path.
- Specialized skill used or recommended.
- Approval notes.
- Follow-up review recommendation.

## Boundaries

This skill should not bypass specialized creation skills.

It should not create tools, integrations, evals, or automations until those models exist or the user explicitly approves a provisional structure.

It should not create project-specific capabilities inside KORA Core.
