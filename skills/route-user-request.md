# route-user-request

## Purpose

Route a natural-language user request to the smallest useful KORA workflow.

This skill helps KORA understand what the user probably wants when they ask in plain language without naming agents, skills, folders, or architecture terms.

## When To Use

- When the user asks for something broad, informal, or ambiguous.
- When the user asks for an outcome but does not name the KORA capability to use.
- When a request may touch multiple areas such as project context, knowledge, tools, automations, evals, or learning.
- When the agent needs to decide whether to execute directly, classify first, or propose a capability plan.

## When Not To Use

- When the user already names the exact KORA skill, agent, file, or artifact to create or review.
- When the task is a simple direct edit with obvious scope.
- When a specialized skill clearly applies and no routing decision is needed.

## Inputs

- User request.
- Current repository path.
- Known project binding, if any.
- Existing `AGENTS.md` instructions.
- Existing KORA skills, agents, tools, integrations, automations, evals, knowledge, and project registry.

## Process

1. Restate the user's requested outcome in simple language.
2. Identify the target:

```text
KORA Core
local project .kora/
operational project repository
external system
unknown
```

3. Identify the likely task type:

```text
direct execution
context selection
project setup or binding
knowledge creation or review
skill creation or review
agent creation or review
tool or integration assessment
automation design
eval creation or execution
learning or decision record
```

4. Estimate ambiguity, recurrence, and risk:

```text
ambiguity: low | medium | high
recurrence: one-off | repeated | unknown
risk: low | medium | high
```

5. Choose one route:

```text
execute directly
use an existing skill
use an existing agent
select context first
classify task and scope first
create a capability plan
ask one clarifying question
```

6. If the request should create or change a durable KORA artifact, run scope classification before editing.
7. Execute the chosen route or explain the next step if human input is required.
8. If the task revealed a durable improvement, recommend whether to record learning, a decision, or a capability gap.

## Outputs

- Routed interpretation of the user's request.
- Recommended KORA workflow.
- Selected skill, agent, template, or file path.
- Scope recommendation when storage is involved.
- Smallest useful next action.

## Routing Examples

```text
"Quero melhorar meu Instagram"
-> classify task, select marketing context, assess whether manual analysis or Instagram integration is needed.

"Cria uma proposta para a cliente Ana"
-> use create-commercial-proposal; keep client specifics in the project context or output, not KORA Core.

"Esse processo acontece toda semana"
-> diagnose workflow; consider skill first, automation only after the workflow is stable.

"Aprendi que esse tipo de lead responde melhor a mensagem curta"
-> record-learning; later review before promoting to reusable sales knowledge.

"Isso deve ficar na KORA ou no projeto?"
-> use classify-scope.
```

## Required Knowledge

```text
knowledge/agentic-systems/capability-routing-heuristics.md
knowledge/agentic-systems/context-selection-principles.md
knowledge/agentic-systems/structural-decision-matrix.md
```

## Optional Knowledge

Domain knowledge relevant to the user's task.

## Required Tools

None.

## Optional Tools

External connectors, CLIs, scripts, or APIs may be used only after the route confirms they are needed.

## Evals

Useful eval scenarios:

```text
evals/scenarios/EV-0010-orchestration-flow.md
evals/scenarios/EV-0013-tool-integration-automation-decision.md
```

## Approval Points

Ask for human approval before:

- creating a new high-impact capability;
- moving project-specific content into KORA Core;
- connecting or using external accounts;
- designing an automation that may later act with reduced human intervention.

## Boundaries

This skill routes. It should not expand the task beyond the user's intended outcome.

Do not create agents, skills, integrations, or automations just because the request is interesting. Prefer the smallest useful path.

## Related

```text
skills/use-kora.md
skills/classify-task.md
skills/classify-scope.md
skills/create-capability-plan.md
agents/capability-router.md
agents/context-curator.md
agents/kora-guide.md
```
