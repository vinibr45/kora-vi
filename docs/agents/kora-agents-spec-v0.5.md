# KORA Agents Specification v0.5

## 1. Purpose

This specification defines how KORA represents agents.

An agent is a goal-oriented role that pursues objectives using selected context, skills, tools, evals, and boundaries.

The goal of v0.5 is to formalize the agent contract, scope rules, lifecycle, permissions, and relationship between agents, skills, knowledge, project context, memory, tools, evals, orchestration, and capability management.

## 2. Agent Definition

An agent is responsible for pursuing a class of objectives within a defined role and boundary.

Examples:

- KORA Architect;
- Capability Router;
- Project Binder;
- Context Curator;
- Knowledge Steward;
- future Content Strategist;
- future Security Reviewer;
- future UX Reviewer;
- future Instagram Analyst;
- future Automation Designer.

An agent is not:

- a prompt dump;
- a knowledge article;
- a tool by itself;
- a skill by itself;
- an unrestricted autonomous worker;
- a place to store project-specific facts unless local to a project binding;
- a substitute for human approval.

## 3. Core Rule

```text
An agent owns a role and judgment.
A skill owns a repeatable procedure.
Knowledge owns reusable concepts.
Project Context owns local truth.
A tool owns execution capability.
An eval owns quality assessment.
Orchestration owns coordination.
```

## 4. Agent Scope

Agents can be global, local, or hybrid.

### Global Agent

A reusable agent stored in KORA Core:

```text
C:\KORA\agents\
```

Use when the role can support multiple projects.

### Local Agent

A project-specific agent stored in a project binding:

```text
<project-repository>\.kora\agents\
```

Use when the role depends on one project's identity, stack, audience, market, clients, operational rules, or repository structure.

### Hybrid Agent

A local adaptation of a global agent.

The reusable role pattern belongs in KORA Core. The project-specific adaptation belongs in the local `.kora/agents/` folder.

## 5. Agent Contract

Each agent should define:

- name;
- purpose;
- scope;
- status;
- owner;
- domains;
- responsibilities;
- non-responsibilities;
- inputs;
- outputs;
- context access;
- memory access;
- knowledge access;
- skills it may use;
- tools it may use;
- evals it should apply;
- permissions;
- approval points;
- boundaries;
- handoff rules;
- related agents;
- related decisions.

Not every section needs to be long. Agents should be clear enough to guide behavior without becoming huge instructions.

## 6. Recommended Format

KORA agents use Markdown.

When useful, an agent may use YAML frontmatter:

```markdown
---
name: ""
type: architect | router | curator | steward | binder | specialist | reviewer | operator
scope: global | local | hybrid
status: draft | active | deprecated
version: "0.1"
owner: ""
domains: []
allowed_skills: []
allowed_tools: []
required_evals: []
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
---
```

## 7. Agent Types

### architect

Protects architecture and structural boundaries.

Example: KORA Architect.

### router

Routes tasks to capabilities.

Example: Capability Router.

### binder

Connects projects to KORA.

Example: Project Binder.

### curator

Selects and prepares context.

Example: Context Curator.

### steward

Maintains quality and integrity of knowledge, memory, or other source-of-truth areas.

Example: Knowledge Steward.

### specialist

Handles a specific domain or capability area.

Example future agents: Content Strategist, Security Reviewer, UX Reviewer.

### reviewer

Reviews outputs, risks, or artifacts.

Example future agents: Code Reviewer, Accessibility Reviewer.

### operator

Runs operational workflows under defined permissions.

Example future agents: Publishing Operator, Report Generator.

## 8. Lifecycle Status

### draft

The agent is proposed or new and not yet trusted as a stable role.

### active

The agent is accepted for regular use.

### deprecated

The agent should not be used for new work unless there is a compatibility reason.

## 9. Creation Rules

Create or propose a new agent when at least one condition is true:

- a recurring objective needs a stable role;
- the task requires specialized judgment;
- the role needs a distinct permission boundary;
- several skills need to be coordinated under one role;
- the work benefits from a named responsibility owner;
- risk justifies a reviewer or specialist;
- a local project needs a role tailored to its market, stack, workflow, or repository.

Do not create an agent when:

- direct execution is enough;
- a skill alone is enough;
- a tool alone is enough;
- the role is too vague;
- it duplicates an existing agent;
- it would create project-specific behavior inside KORA Core.

## 10. Permissions And Approval

Agents must have explicit boundaries.

An agent may be allowed to:

- read selected context;
- use selected skills;
- call selected tools;
- propose file changes;
- create capability plans;
- recommend decisions;
- request approval.

Agents should not silently:

- change source-of-truth knowledge;
- write memory;
- create integrations;
- create automations;
- access accounts;
- publish or deploy;
- send external communications;
- move local project facts into KORA Core.

## 11. Handoffs

Agents should hand off work when another agent owns the responsibility better.

Examples:

```text
Capability Router -> Project Binder
When a project is not connected to KORA.

Capability Router -> Context Curator
When task context must be selected.

Knowledge Steward -> KORA Architect
When a knowledge decision affects architecture.

KORA Architect -> Capability Router
When architecture approves a capability direction and execution planning is needed.
```

## 12. Relationship With Skills

Agents use skills to perform repeatable procedures.

A role should not duplicate the full process of a skill.

Example:

```text
Agent: Project Binder
Skill: setup-kora-project
```

## 13. Relationship With Knowledge And Context

Agents should receive selected context, not the entire knowledge base or project repository by default.

Context Curator and Capability Router help decide what the agent needs.

## 14. Relationship With Tools

Tools must be explicit.

If an agent needs an external system, API, MCP connector, plugin, script, browser, database, filesystem operation, or deployment command, that dependency should be named and permissioned.

## 15. Relationship With Evals

Agents should know when their outputs need evals.

Examples:

- Security-related work needs security review.
- UX-facing work needs UX/accessibility review.
- Knowledge creation needs knowledge review.
- Project binding needs project context review.

## 16. Initial Core Agents

KORA v0.5 includes these global Core agents:

- KORA Architect;
- Capability Router;
- Project Binder;
- Context Curator;
- Knowledge Steward.

These are architectural definitions, not autonomous runtime workers.

## 17. Non-Goals For v0.5

Do not create:

- an agent runtime;
- autonomous background agents;
- external account access;
- project-specific domain agents inside KORA Core;
- automated orchestration;
- integrations;
- automations.

v0.5 defines the agent model first.
