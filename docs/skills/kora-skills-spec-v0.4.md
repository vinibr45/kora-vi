# KORA Skills Specification v0.4

## 1. Purpose

This specification defines how KORA represents skills.

A skill is a reusable procedure for performing a task, making a structured decision, reviewing an output, or creating a capability.

The goal of v0.4 is to formalize the skill contract, lifecycle, scope rules, and relationship between skills, agents, knowledge, tools, evals, and project bindings.

## 2. Skill Definition

A skill defines how to do something repeatably.

Examples:

- classify a task;
- select context;
- create a capability plan;
- bind a project to KORA;
- create a knowledge entry;
- review a project context;
- generate a content calendar;
- review frontend accessibility;
- create an Instagram post briefing;
- inspect a deployment checklist.

A skill is not:

- a full agent identity;
- a general knowledge article;
- a raw prompt dump;
- a tool implementation by itself;
- project-specific strategy unless stored in a local project binding;
- an automation unless it has executable support.

## 3. Core Rule

```text
Knowledge explains what is true or useful.
A skill explains how to do a task.
An agent decides and acts using skills.
A tool executes an external capability.
An eval checks quality.
```

## 4. Skill Scope

Skills can be global, local, or hybrid.

### Global Skill

A reusable skill stored in KORA Core:

```text
C:\KORA\skills\
```

Use when the procedure can help multiple projects.

### Local Skill

A project-specific skill stored in a project binding:

```text
<project-repository>\.kora\skills\
```

Use when the procedure depends on one project's identity, stack, audience, workflow, client, offer, repository, or operating rules.

### Hybrid Skill

A local adaptation of a global skill.

The reusable pattern belongs in KORA Core. The project-specific adaptation belongs in the local `.kora/` binding.

## 5. Skill Contract

Each skill should define:

- name;
- purpose;
- scope;
- status;
- owner;
- when to use;
- when not to use;
- inputs;
- process;
- outputs;
- required knowledge;
- optional knowledge;
- required tools;
- optional tools;
- evals;
- boundaries;
- approval points;
- related agents;
- related skills;
- related decisions.

Not every section needs to be long. Clarity matters more than ceremony.

## 6. Recommended Format

KORA skills use Markdown.

When useful, a skill may use YAML frontmatter:

```markdown
---
name: ""
type: decision | creation | review | execution | planning | integration | automation
scope: global | local | hybrid
status: draft | active | deprecated
version: "0.1"
owner: ""
domains: []
related_agents: []
related_skills: []
required_knowledge: []
required_tools: []
evals: []
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
---
```

## 7. Skill Types

### decision

Helps choose between options.

Example: `classify-scope`.

### creation

Creates or proposes a structured artifact.

Example: `create-knowledge-entry`.

### review

Reviews an artifact or output.

Example: `review-project-context`.

### execution

Performs a repeatable task.

Example future skill: `generate-content-calendar`.

### planning

Produces a plan before execution.

Example: `create-capability-plan`.

### integration

Defines how to connect or use external systems.

Example future skill: `connect-instagram-metrics`.

### automation

Defines a repeatable workflow that may later be executed with minimal human intervention.

Example future skill: `weekly-content-report`.

## 8. Lifecycle Status

### draft

The skill is proposed or new and not yet trusted as a stable procedure.

### active

The skill is accepted for regular use.

### deprecated

The skill should not be used for new work unless there is a compatibility reason.

## 9. Creation Rules

Create or propose a new skill when at least one condition is true:

- the task is recurring;
- the process needs consistency;
- the process has quality criteria;
- the process should be reused across agents;
- the task has enough complexity to justify a procedure;
- the process can reduce repeated explanation;
- the skill can serve more than one project;
- a local project needs a stable custom workflow.

Do not create a skill when:

- the task is tiny and unlikely to repeat;
- direct execution is enough;
- the procedure is still too unclear;
- the task is really a tool, agent, knowledge entry, eval, or decision record;
- it would duplicate an existing skill.

## 10. Relationship With Agents

Agents use skills.

Agents should not duplicate full procedures when a skill can own the process.

Example:

```text
Agent: Capability Router
Skill: create-capability-plan
```

The agent owns judgment and role. The skill owns the reusable procedure.

## 11. Relationship With Knowledge

Skills may reference knowledge, but should not duplicate entire knowledge modules.

Example:

```text
Skill: generate-content-calendar
Knowledge: knowledge/marketing/content/
```

The skill owns the process. Knowledge owns the theory or reusable concept.

## 12. Relationship With Tools

A skill may require or optionally use tools.

Tools should be listed explicitly when they are required for execution.

Example:

```text
Skill: analyze-instagram-performance
Required tool: approved Instagram metrics access
Fallback: manual screenshots or exported metrics
```

## 13. Relationship With Evals

A skill should define evals or quality criteria when outputs need review.

Example:

```text
Skill: create-project-context
Eval: project context completeness and boundary review
```

## 14. Approval Points

A skill should identify when human approval is required.

Approval is especially important before:

- creating integrations;
- creating automations;
- changing source-of-truth stores;
- promoting local learning to global knowledge;
- accessing accounts or external services;
- publishing, deploying, or sending content externally.

## 15. Setup Skill

KORA v0.4 introduces `setup-kora-project` as a skill contract.

This skill should not yet be treated as a fully automated script. It defines the assisted workflow for connecting a project to KORA.

Future versions may turn it into a tool or automation after it is tested on real projects.

## 16. Non-Goals For v0.4

Do not create:

- a runtime skill engine;
- automatic skill execution;
- integrations;
- automations;
- large domain-specific skill libraries;
- project-specific skills inside KORA Core.

v0.4 defines the skill model first.
