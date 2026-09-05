# KORA Orchestration Specification v0.6

## 1. Purpose

This specification defines how KORA coordinates work.

Orchestration is the layer that turns a user task into a controlled flow involving context, agents, skills, tools, evals, approvals, execution, memory, decisions, and learning.

The goal of v0.6 is to formalize orchestration and capability management without implementing an automated runtime engine.

## 2. Orchestration Definition

Orchestration is responsible for deciding how work should proceed.

It may coordinate:

- task classification;
- project binding detection;
- context selection;
- capability routing;
- agent selection;
- skill selection;
- tool selection;
- integration or automation proposals;
- approval points;
- execution mode;
- evaluation;
- learning promotion;
- memory or decision recording.

Orchestration is not:

- a single giant agent;
- a hidden knowledge base;
- a prompt dump;
- unrestricted automation;
- a replacement for human approval;
- a place to store project-specific facts.

## 3. Core Rule

```text
Orchestration coordinates.
Agents own roles.
Skills own procedures.
Tools execute capabilities.
Knowledge provides reusable concepts.
Project Context provides local truth.
Evals assess quality.
Learning decides what should persist.
```

## 4. Capability Management

Capability Management is the central decision responsibility inside orchestration.

It decides whether KORA should:

- execute directly;
- use an existing skill;
- create or propose a new skill;
- use an existing agent;
- create or propose a new agent;
- use an existing tool;
- create or propose a tool;
- use or propose an integration;
- use or propose an automation;
- apply an eval;
- record memory;
- record a decision;
- promote learning.

## 5. Orchestration Flow

Preferred conceptual flow:

```text
User Task
  ↓
Task Classification
  ↓
Project Binding Detection
  ↓
Context Selection
  ↓
Capability Discovery
  ↓
Capability Plan
  ↓
Approval Check
  ↓
Execution Mode Selection
  ↓
Agent / Skill / Tool Execution
  ↓
Evaluation
  ↓
Result Delivery
  ↓
Learning / Memory / Decision
```

Not every task needs every step. Simple one-off tasks may be executed directly.

## 6. Task Classification

Orchestration should classify:

- task domain;
- target project;
- task type;
- complexity;
- recurrence;
- risk;
- required external systems;
- likely capabilities.

Primary skill:

```text
skills/classify-task.md
```

## 7. Project Binding Detection

If the task belongs to a project, orchestration should determine whether the project is bound to KORA.

If not, orchestration may invoke or recommend:

```text
skills/setup-kora-project.md
skills/bind-project-to-kora.md
```

## 8. Context Selection

Orchestration should select only relevant context.

Context may come from:

- task input;
- KORA knowledge;
- KORA decisions;
- project binding;
- project context;
- project memory;
- repository files;
- prior results.

Primary skill:

```text
skills/select-context.md
```

Primary agent:

```text
agents/context-curator.md
```

## 9. Capability Discovery

Before creating anything new, orchestration should inspect:

- global KORA agents;
- local project agents;
- global KORA skills;
- local project skills;
- available tools;
- available integrations;
- available automations;
- relevant evals;
- missing capabilities.

## 10. Capability Plan

A capability plan should be created when a task is complex, recurring, risky, ambiguous, or may require new capabilities.

The capability plan should define:

- task summary;
- project;
- domain;
- existing capabilities;
- missing capabilities;
- recommended execution mode;
- global/local/hybrid placement;
- required approvals;
- evals;
- learning or memory implications;
- minimal next action.

Primary skill:

```text
skills/create-capability-plan.md
```

## 11. Execution Modes

KORA recognizes five execution modes:

### Manual

The user provides inputs and KORA produces the output without integration.

### Assisted

KORA uses context, knowledge, agents, and skills, while the user handles external steps.

### Tool-Supported

KORA uses scripts, local tools, files, browser actions, or available integrations.

### Integrated

KORA connects to external systems through approved APIs, MCP connectors, plugins, or other controlled integrations.

### Automated

KORA runs a repeatable workflow with minimal human intervention, subject to approval and safety rules.

## 12. Approval Policy

Orchestration should ask for approval before:

- writing to external project repositories;
- creating local project bindings;
- changing `AGENTS.md`;
- creating project-specific agents or skills;
- creating tools, integrations, or automations;
- accessing accounts;
- using paid services or subscriptions;
- publishing, deploying, sending, scheduling, or modifying external systems;
- writing memory;
- changing source-of-truth knowledge;
- promoting local learning into global KORA Core.

## 13. Direct Execution Rule

Not every task needs a capability plan.

KORA may execute directly when:

- the task is small;
- the risk is low;
- the output is one-off;
- all required context is already available;
- no new capability, tool, integration, automation, memory, or decision is needed.

## 14. Creation Rule

KORA should create or propose new capabilities only when justified by:

- recurrence;
- risk;
- specialization;
- consistency;
- quality criteria;
- operational leverage;
- reuse across projects;
- local project complexity;
- explicit user request.

## 15. Scope Rule

```text
Reusable across projects -> KORA Core
Specific to one project -> local .kora binding
Published/runtime code -> project repository
```

Hybrid capabilities may reference KORA Core but should store project-specific adaptations locally.

## 16. Evaluation

Orchestration should apply evals when:

- output quality matters;
- the task is risky;
- the task affects architecture;
- the task affects knowledge, memory, permissions, tools, integrations, or automations;
- recurring workflows need quality consistency.

## 17. Learning

After execution, orchestration should decide whether anything should persist.

Possible destinations:

- no persistence;
- local memory;
- global memory;
- local decision;
- architecture decision;
- knowledge entry;
- skill improvement;
- agent improvement;
- eval improvement;
- tool or automation proposal.

Primary skill:

```text
skills/promote-learning.md
```

## 18. Non-Goals For v0.6

Do not create:

- an automated runtime orchestrator;
- background workers;
- queue systems;
- integrations;
- automation engine;
- database-backed capability registry;
- account access;
- deployment workflows.

v0.6 defines orchestration logic first.
