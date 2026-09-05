# KORA Architecture Specification v0.1

## 1. Purpose

KORA, **Knowledge-Orchestrated Reasoning Architecture**, is a modular architecture for building reusable agentic systems.

Its purpose is to define how knowledge, project context, memory, context selection, agents, skills, tools, orchestration, evaluation, experiments, and learning relate to each other without prematurely implementing a runtime framework.

KORA is private and proprietary by default. It is being designed first for the creator's own projects and businesses, with possible future use in company contexts.

KORA should be usable by different implementations. For example:

- KORA is the architecture and methodology.
- MarcosOS is a prior personal brain/operating concept that may inform KORA.
- Marcos Dev is the first intended business context managed through KORA.
- A company could create its own KORA-based implementation.

This v0.1 specification defines the architectural foundation only.

## 1.1 Current Governance Assumption

KORA v0.1 assumes a lightweight governance model:

- Owner: the creator of KORA.
- Future partner/co-owner: the creator's brother.
- Future managers: people with limited scope over specific projects, companies, or operating areas.

Role-based permissions should not be overbuilt in v0.1. They should become concrete only when a real implementation needs them.

## 2. Non-Goals

KORA v0.1 does not implement:

- real agents;
- real skills;
- automations;
- external integrations;
- APIs;
- databases;
- a CLI;
- a server;
- runtime orchestration;
- automatic memory writing;
- automated eval pipelines;
- a full knowledge base;
- a concrete implementation such as MarcosOS.

The priority of v0.1 is:

```text
architectural clarity > number of components > automation
```

## 3. Architectural Principles

### Single Source of Truth

Important information should have a primary authoritative location. Duplicates should be avoided or clearly marked as summaries, derived views, or references.

Examples:

- Architecture decisions belong in Architecture.
- Business-specific decisions belong in Project Context.
- Reusable theory belongs in Knowledge Base.
- Operational learnings belong in Memory.

### Separation of Concerns

Knowledge, project context, memory, execution behavior, procedures, and tools should not be mixed unless there is a clear reason.

### Composability

Knowledge modules, skills, agents, tools, and context policies should be reusable across implementations.

### Context Efficiency

An agent should not receive the entire knowledge base by default. It should receive only the relevant context for the task.

### Modularity

Components should be replaceable without requiring the whole architecture to be rebuilt.

### Model Independence

KORA should not depend structurally on a specific AI model.

### Tool Independence

KORA should avoid structural dependency on Codex, Claude, ChatGPT, or any single tool environment.

### Evidence-Based Knowledge

External knowledge should support sources, references, evidence level, confidence, and limitations when relevant.

### Organizational Memory

Decisions, results, experiments, and important learnings should be preservable.

### Continuous Improvement

Execution results should be able to inform future decisions, memory, knowledge, skills, evals, and orchestration.

### YAGNI

KORA should not introduce complexity without a current architectural purpose.

### Human Control

Important changes to knowledge, memory, rules, decisions, or architecture should not happen silently. They require explicit criteria, review, or approval.

## 4. Component Model

KORA v0.1 defines eleven conceptual components:

1. Architecture
2. Knowledge Base
3. Project Context
4. Memory
5. Context Layer
6. Orchestration
7. Agents
8. Skills
9. Tools
10. Evaluation
11. Experiments and Learning

Some of these are concrete storage areas. Others are conceptual responsibilities that may later become code, schemas, policies, or runtime services.

## 5. Component Definitions

### 5.1 Architecture

Architecture defines the principles, components, boundaries, contracts, and information flow of KORA.

Architecture is normative: it explains how the system should be structured and how future implementations should preserve separation of concerns.

Architecture is not runtime execution logic.

### 5.2 Knowledge Base

Knowledge Base stores general reusable knowledge.

Examples:

- marketing;
- psychology;
- software engineering;
- product;
- business;
- methodologies;
- frameworks;
- research;
- references.

Knowledge Base should be modular and recoverable. It should avoid giant files such as `marketing.md` when a topic can be decomposed into smaller concepts.

When applicable, knowledge entries should support:

- title;
- concept;
- application;
- when to use;
- when not to use;
- limitations;
- examples;
- sources;
- evidence level;
- related concepts.

Knowledge Base should not store project-specific positioning, personal preferences, client history, or implementation decisions.

### 5.3 Project Context

Project Context stores information specific to a project, company, product, person, or implementation.

Example:

```text
projects/marcos-os/
```

Possible contents:

- vision;
- audience;
- positioning;
- identity;
- products;
- strategy;
- decisions;
- history.

Project Context may also organize business management information, including positioning, offers, content direction, sales context, operations, products, and audience-specific decisions.

Project Context should not duplicate general theory from the Knowledge Base.

### 5.4 Memory

Memory stores knowledge generated by the operation of a KORA-based system.

Examples:

- important decisions;
- user preferences;
- recurring patterns;
- execution outcomes;
- lessons learned;
- accepted changes;
- rejected changes;
- relevant historical facts.

Memory is not the same as Knowledge Base. Knowledge Base stores reusable external or formalized knowledge. Memory stores operational learning and history.

Memory should not become an unfiltered transcript archive. Writing to memory requires criteria.

Architectural and project decisions should be recorded when they affect future decisions, reduce ambiguity, or change how KORA should behave. Not every conversation or temporary preference should become memory.

### 5.5 Context Layer

The Context Layer selects, assembles, compresses, and prepares task-specific context.

It may read from:

- Knowledge Base;
- Project Context;
- Memory;
- task input;
- prior execution state.

It should not own the source information it selects. It produces a contextual working set for agents or orchestration.

### 5.6 Orchestration

Orchestration coordinates the execution of a task.

Depending on implementation maturity, it may decide:

- which agent should handle a task;
- which context should be loaded;
- which skills are relevant;
- which tools are available;
- whether a task should be decomposed;
- whether human approval is required;
- how results should be evaluated.

Orchestration should coordinate responsibilities without becoming a hidden knowledge base or a monolithic prompt.

### 5.7 Agents

Agents are goal-oriented entities operating within a defined context, role, scope, and permission boundary.

An agent may:

- consult selected context;
- use skills;
- call tools;
- produce outputs;
- request evaluation;
- propose memory or knowledge updates.

Agents should not contain all knowledge, all procedures, or unrestricted tool access.

### 5.8 Skills

Skills are reusable procedures for performing tasks.

A skill may define:

- objective;
- inputs;
- process;
- required or optional knowledge;
- required or optional project context;
- tools it may use;
- quality criteria;
- expected output.

A skill should not duplicate full theory from the Knowledge Base. It should reference knowledge modules when needed.

### 5.9 Tools

Tools are external or executable capabilities.

Examples:

- scripts;
- APIs;
- filesystem;
- databases;
- browser;
- image generation;
- Git;
- GitHub.

Tools execute capabilities. They should not decide strategic intent or own architectural policy.


### 5.10 Capability Management

Capability Management is the architectural responsibility for deciding whether a task should be handled directly, routed to an existing capability, or turned into a new capability.

A capability may be:

- an agent;
- a skill;
- a tool;
- an automation;
- an eval;
- a project-specific process;
- a reusable knowledge module;
- a documented decision or memory entry.

Capability Management should answer questions such as:

- Is this task simple enough to execute directly?
- Is this task likely to repeat?
- Does an existing global skill or agent already solve it?
- Does a local project-specific skill or agent already solve it better?
- Should a new skill be created?
- Should a new agent be created?
- Should a new tool, integration, or automation be created?
- Should the new capability live in KORA Core or in the local project binding?
- Does this task require evaluation?
- Did the result create learning that should become memory or a decision?

Capability Management should not create complexity automatically. It should prefer existing capabilities when they fit, create new capabilities when recurrence or specialization justifies it, and ask for human approval before important structural changes.

Capability Management should also distinguish execution modes: manual, assisted, tool-supported, integrated, and automated. When multiple modes are reasonable, KORA should present options and ask about available accounts, subscriptions, permissions, and desired automation level before creating integrations or recurring automations.

Capability Management should reason by domain. For software work, it should inspect project type, stack, risk, UX needs, security needs, testing needs, deployment context, existing capabilities, and missing capabilities before suggesting agents, skills, tools, evals, integrations, or automations.

Before creating a capability, KORA should classify its scope as global, local, or hybrid. Project-specific capabilities belong in the local project binding, not in KORA Core. KORA Core should stay clean and reusable.
### 5.11 Evaluation

Evaluation defines mechanisms for judging quality, correctness, completeness, safety, or usefulness.

Evaluation can include:

- checklists;
- rubrics;
- tests;
- assertions;
- examples;
- human review criteria;
- automated evals in later versions.

Evaluation should assess outputs or processes. It should not directly rewrite knowledge or memory without a defined learning policy.

### 5.12 Experiments and Learning

Experiments are structured tests of hypotheses.

Learning is the process of converting results into improvements.

Possible outputs:

- memory updates;
- knowledge update proposals;
- skill revisions;
- orchestration improvements;
- eval improvements;
- architectural changes.

Learning should distinguish weak observations from validated knowledge.

## 6. Information Flow

The preferred conceptual flow is:

```text
User / Task
    ↓
Orchestration
    ↓
Context Layer
    ├── reads Knowledge Base
    ├── reads Project Context
    └── reads Memory
    ↓
Agent
    ├── uses Skills
    ├── calls Tools
    └── produces Output / Actions
    ↓
Evaluation
    ↓
Result
    ↓
Experiments and Learning
    ├── may update Memory
    ├── may propose Knowledge changes
    └── may propose Architecture / Skill / Eval improvements
```

This flow is conceptual, not mandatory runtime code.

## 7. Read and Write Boundaries

### Knowledge Base

Can be read by:

- Context Layer;
- Agents through selected context;
- Skills through references;
- Evaluation criteria;
- humans.

Can be changed by:

- humans;
- approved learning processes;
- reviewed knowledge maintenance procedures.

Should not be silently changed by:

- agents;
- tools;
- evals;
- experiments without review.

### Project Context

Can be read by:

- Context Layer;
- Orchestration;
- Agents through selected context;
- Skills through references.

Can be changed by:

- humans;
- approved project decisions;
- reviewed learning processes.

Should not be used for:

- general theory;
- reusable cross-project knowledge.

### Memory

Can be read by:

- Context Layer;
- Orchestration;
- Agents through selected context.

Can be changed by:

- explicit human instruction;
- approved memory policies;
- reviewed learning outputs.

Should not store:

- raw logs without filtering;
- unstable assumptions as facts;
- external theory that belongs in Knowledge Base.

### Context Layer

Can read from many sources but should write only context artifacts, indexes, or selection metadata in later implementations.

It should not become an authority for the underlying facts.

### Orchestration

Can coordinate agents, context, skills, tools, and evals.

It should not directly mutate core knowledge stores except through explicit policies.

### Agents

Can act within assigned scope.

They may propose changes, but important writes require defined criteria or approval.

### Skills

Can define procedure.

They should not own knowledge, memory, or unrestricted tool behavior.

### Tools

Can execute capabilities.

They must be permissioned through orchestration, agent policy, or implementation configuration.

### Evaluation

Can assess and report.

It may produce recommendations, but should not directly rewrite source-of-truth stores.

### Experiments and Learning

Can produce learning artifacts and recommendations.

Promotion from observation to memory or knowledge requires review criteria.

## 8. Repository Structure

The minimum v0.1 repository structure is:

```text
KORA/
├── README.md
├── docs/
│   └── architecture/
│       └── kora-architecture-spec-v0.1.md
├── architecture/
│   ├── principles.md
│   ├── components.md
│   ├── information-flow.md
│   └── boundaries.md
├── knowledge/
│   └── README.md
├── projects/
│   └── README.md
├── memory/
│   └── README.md
├── context/
│   └── README.md
├── orchestration/
│   └── README.md
├── agents/
│   └── README.md
├── skills/
│   └── README.md
├── tools/
│   └── README.md
├── evals/
│   └── README.md
├── experiments/
│   └── README.md
└── config/
    └── README.md
```

## 9. Minimal Roadmap

### v0.1 Architecture

Define principles, components, responsibilities, boundaries, information flow, and minimum repository structure.

### v0.2 Knowledge

Define knowledge entry schema, topic taxonomy, source metadata, evidence levels, and retrieval assumptions.

### v0.3 Project Context

Define project context schema, project decision records, identity files, and implementation-specific boundaries.

### v0.4 Skills

Define skill contract, skill metadata, dependencies, inputs, outputs, quality criteria, and composition rules.

### v0.5 Agents

Define agent contract, role boundaries, permissions, context access, skill access, and output responsibilities.

### v0.6 Orchestration

Define task routing, context selection policy, agent selection, skill availability, tool permissions, and verification flow.

### v0.7 Evals

Define evaluation rubrics, manual checklists, examples, and initial automated eval strategy.

### v0.8 Experiments and Learning

Define experiment records, hypothesis tracking, result interpretation, memory update rules, and knowledge promotion criteria.

### v0.9 Tooling

Add schemas, validation scripts, generators, or indexing helpers only where the architecture has stabilized enough to justify them.

### v1.0 Reference Implementation

Create the first usable implementation based on KORA, such as MarcosOS or another concrete environment.






