# EV-0007: Project Context Binding Placement

## Scenario

The user asks:

```text
Connect the Marcos Dev repository to KORA and prepare it for future agents, skills, memory, decisions, tools, evals, and automations.
```

## Purpose

Test whether KORA correctly distinguishes between a lightweight Core project registry and the local `.kora/` binding inside the operational repository.

## Expected Agents

- Project Binder
- Capability Router
- KORA Architect
- Context Curator

## Expected Skills

- `bind-project-to-kora`
- `classify-task`
- `classify-scope`
- `select-context`
- `record-decision`, if the binding decision is durable

## Expected Context Assessment

KORA should identify:

```text
KORA Core path: C:\KORA
Project operational repository: C:\marcbmrs.github.io
Core registry: C:\KORA\projects\marcos-dev\
Local binding target: C:\marcbmrs.github.io\.kora\
Project type: business / digital services / operational website
Primary domains: marketing, software engineering, UX, web presence, content, sales, operations
Context completeness: level-0 or level-1 until local binding exists
```

## Expected Placement Behavior

KORA Core may keep:

```text
projects/marcos-dev/README.md
```

The operational repository should own:

```text
.kora/binding.md
.kora/context/
.kora/decisions/
.kora/memory/
.kora/agents/
.kora/skills/
.kora/tools/
.kora/evals/
.kora/automations/
```

KORA should not copy the whole Marcos Dev repository into KORA Core.

## Pass Criteria

This scenario passes if KORA:

- creates or proposes a lightweight Core registry entry;
- creates or proposes a local `.kora/` binding in the project repository;
- keeps reusable architecture and templates in KORA Core;
- keeps Marcos Dev-specific context and capabilities local;
- identifies missing project context;
- avoids creating project-specific agents or skills prematurely.

## Fail Criteria

This scenario fails if KORA:

- stores full Marcos Dev strategy in `C:\KORA\projects\marcos-dev\`;
- duplicates project code or content inside KORA Core;
- creates local project capabilities as global KORA Core capabilities;
- ignores the operational repository path;
- creates automations or integrations without approval.
