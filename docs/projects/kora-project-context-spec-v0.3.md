# KORA Project Context Specification v0.3

## 1. Purpose

This specification defines how KORA represents project-specific context.

Project Context is the source of truth for information that belongs to one project, business, company, product, client, or implementation.

The goal of v0.3 is to define the project context model and the local `.kora/` binding pattern without implementing runtime automation.

## 2. Project Context Definition

Project Context is information that helps KORA understand a specific project.

Examples:

- project identity;
- business model;
- audience;
- positioning;
- offers;
- products or services;
- strategy;
- operations;
- stack and repository structure;
- brand rules;
- communication style;
- project-specific decisions;
- local constraints;
- local capabilities.

Project Context is not:

- reusable general knowledge;
- global KORA architecture;
- unfiltered memory;
- executable code by default;
- generic skills or agents that serve many projects.

## 3. Core Rule

```text
KORA Core defines the architecture.
Project Context defines the local reality.
```

Another useful rule:

```text
KORA knows how to think.
The project knows what is true here.
```

## 4. Project Binding

A project binding connects an operational repository to KORA.

Preferred local structure inside a project repository:

```text
<project-repository>/.kora/
  binding.md
  context/
  decisions/
  memory/
  agents/
  skills/
  tools/
  evals/
  automations/
```

This local `.kora/` layer stores project-specific context and capabilities.

KORA Core may keep a lightweight project registry or summary in:

```text
projects/<project-name>/
```

But detailed project context should live in the project's own `.kora/` binding when the project repository exists.

## 5. KORA Core Project Registry

`projects/` inside KORA Core should not become a duplicate of every project.

It may store:

- project name;
- external repository path;
- project type;
- project status;
- primary domains;
- relationship to KORA;
- links to local `.kora/` binding;
- high-level notes needed for routing.

It should not store:

- full project strategy;
- full content calendar;
- detailed execution memory;
- private client data;
- project-specific agents or skills that do not generalize.

## 6. Recommended Project Context Files

Inside a local `.kora/context/`, a project may define:

```text
overview.md
identity.md
audience.md
positioning.md
offers.md
products-or-services.md
strategy.md
operations.md
communication.md
brand.md
stack.md
constraints.md
```

Not every project needs every file. KORA should create context files only when useful.

## 7. Local Decisions

Project-specific decisions belong in:

```text
<project-repository>/.kora/decisions/
```

Examples:

- positioning decisions;
- offer decisions;
- stack decisions;
- campaign decisions;
- brand decisions;
- client-specific operating decisions;
- local agent or skill decisions.

Architecture-wide decisions belong in:

```text
C:\KORA\architecture\decisions\
```

## 8. Local Memory

Project-specific memory belongs in:

```text
<project-repository>/.kora/memory/
```

Examples:

- what worked for this project;
- user preferences for this project;
- approved content patterns;
- rejected directions;
- performance learnings;
- recurring project constraints.

Global reusable learning may be proposed for KORA Core, but should not be promoted without scope analysis.

## 9. Local Capabilities

Project-specific agents, skills, tools, evals, and automations belong inside the local `.kora/` binding.

Examples:

```text
<project-repository>/.kora/agents/
<project-repository>/.kora/skills/
<project-repository>/.kora/tools/
<project-repository>/.kora/evals/
<project-repository>/.kora/automations/
```

KORA Core should store only reusable capabilities.

## 10. Binding File

Each bound project should have:

```text
.kora/binding.md
```

The binding file should identify:

- project name;
- project type;
- repository path;
- KORA Core path;
- primary domains;
- local ownership;
- global dependencies;
- local context files;
- local capabilities;
- boundaries;
- missing context.

## 11. Context Completeness Levels

KORA should distinguish how mature a project's context is.

### level-0: registered

The project is known to KORA, but has little or no structured context.

### level-1: bound

The project has a `.kora/binding.md` or KORA Core registry entry.

### level-2: described

The project has basic overview, identity, audience, offer, and constraints.

### level-3: operational

The project has enough context, decisions, memory, and local capabilities to support recurring work.

### level-4: optimized

The project has evals, learning loops, refined local skills/agents, and possibly approved automations.

## 12. Relationship With Capability Management

Capability Router should inspect Project Context before deciding whether to use or create capabilities.

Project Binder should create or review the local binding.

Context Curator should select only the relevant project context for a task.

KORA Architect should resolve ambiguous global/local boundaries.

Knowledge Steward should prevent project context from being promoted to global knowledge without abstraction.

## 13. Marcos Dev Initial Registry

Marcos Dev is the first project/business context planned for KORA.

Current operational repository:

```text
C:\marcbmrs.github.io
```

KORA Core may maintain a lightweight registry entry in:

```text
projects/marcos-dev/
```

Detailed operational context should eventually live in:

```text
C:\marcbmrs.github.io\.kora\
```

## 14. Non-Goals For v0.3

Do not create:

- full Marcos Dev strategy;
- full local `.kora/` implementation without user approval;
- project-specific agents or skills before real tasks justify them;
- automations;
- integrations;
- private client data;
- duplicated project repository content inside KORA Core.

v0.3 defines the project context model first.
