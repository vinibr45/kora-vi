# KORA Evals Specification v0.7

## 1. Purpose

This specification defines how KORA evaluates quality, correctness, usefulness, safety, boundaries, and architectural fit.

An eval is a structured way to assess a task, artifact, capability, process, or decision.

The goal of v0.7 is to formalize evals before building automated evaluation infrastructure.

## 2. Eval Definition

An eval defines criteria for judging whether something is good enough.

Examples:

- architecture boundary review;
- knowledge entry review;
- project context completeness review;
- skill quality review;
- agent permission review;
- capability plan review;
- content recommendation review;
- software security review;
- UX/accessibility review;
- deployment readiness review.

An eval is not:

- a task execution procedure;
- a general knowledge article;
- an agent role;
- a tool by itself;
- a guarantee of correctness;
- a silent source-of-truth updater.

## 3. Core Rule

```text
Evals assess quality.
They do not silently change source-of-truth stores.
```

Eval results may recommend changes to memory, knowledge, decisions, skills, agents, tools, or project context, but promotion requires the proper skill and approval policy.

## 4. Eval Scope

Evals can be global, local, or hybrid.

### Global Eval

A reusable eval stored in KORA Core:

```text
C:\KORA\evals\
```

Use when the criteria apply across projects.

### Local Eval

A project-specific eval stored in a project binding:

```text
<project-repository>\.kora\evals\
```

Use when the criteria depend on one project's goals, audience, brand, stack, clients, constraints, or operating rules.

### Hybrid Eval

A local adaptation of a global eval.

The reusable criteria belong in KORA Core. The project-specific adaptation belongs in the local `.kora/evals/` folder.

## 5. Eval Types

### scenario

Tests behavior through a realistic task.

Example: `evals/scenarios/EV-0010-orchestration-flow.md`.

### checklist

Defines pass/fail or review criteria.

Example: project context completeness checklist.

### rubric

Scores quality across dimensions.

Example: content recommendation quality rubric.

### regression

Ensures a previously accepted behavior still works.

Example: KORA must not place local project capabilities in KORA Core.

### safety

Checks risk, permission, privacy, source-of-truth, account access, or external side effects.

### acceptance

Defines whether an artifact is ready to be accepted.

## 6. Eval Contract

Each eval should define:

- name;
- purpose;
- type;
- scope;
- status;
- owner;
- target artifact or behavior;
- scenario or input;
- expected agents;
- expected skills;
- expected tools, if any;
- expected context;
- pass criteria;
- fail criteria;
- risk checks;
- approval checks;
- result format;
- related decisions.

## 7. Recommended Format

KORA evals use Markdown.

When useful, an eval may use YAML frontmatter:

```markdown
---
name: ""
type: scenario | checklist | rubric | regression | safety | acceptance
scope: global | local | hybrid
status: draft | active | deprecated
version: "0.1"
owner: ""
domains: []
targets: []
related_agents: []
related_skills: []
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
---
```

## 8. Result Status

Eval results should use simple statuses:

### pass

The artifact or behavior meets the criteria.

### fail

The artifact or behavior violates important criteria.

### needs-revision

The artifact or behavior is partially acceptable but needs changes.

### blocked

The eval cannot be completed because required context, access, or decision is missing.

### not-applicable

The eval does not apply to the current task.

## 9. When To Apply Evals

Apply evals when:

- the task is risky;
- the task is recurring;
- output quality matters;
- architecture boundaries may be affected;
- source-of-truth stores may change;
- agents, skills, tools, integrations, or automations may be created;
- project context may be changed;
- external publication, deployment, account access, or paid services are involved;
- user feedback suggests recurring quality issues.

Do not overuse evals for tiny low-risk one-off tasks.

## 10. Eval Results

Eval results may be stored in:

```text
evals/results/
```

for KORA Core evals, or in:

```text
<project-repository>\.kora\evals\results\
```

for local project evals.

Not every manual eval needs a permanent result file. Store results when they affect future decisions, learning, or quality baselines.

## 11. Relationship With Learning

Eval results can feed learning.

Possible follow-up actions:

- no persistence;
- revise artifact;
- record local memory;
- record global memory;
- record decision;
- update knowledge;
- update skill;
- update agent;
- update tool;
- update automation;
- create new eval.

Use:

```text
skills/promote-learning.md
```

before promoting eval results into persistent stores.

## 12. Initial Evals

KORA v0.7 already includes manual scenario evals in:

```text
evals/scenarios/
```

These validate architecture, capability routing, project binding, knowledge placement, skill creation, agent creation, and orchestration.

## 13. Non-Goals For v0.7

Do not create:

- automated eval runner;
- scoring database;
- dashboards;
- CI integration;
- external monitoring;
- model-based judge infrastructure;
- project-specific evals inside KORA Core unless reusable.

v0.7 defines the eval model first.
