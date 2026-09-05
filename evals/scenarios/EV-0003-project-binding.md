# EV-0003: Project Binding

## Scenario

The user asks:

```text
Connect this repository to KORA.
```

## Purpose

Test whether KORA can bind a project repository to KORA through a local `.kora/` layer without copying the entire architecture or polluting KORA Core.

## Expected Agents

- Project Binder
- KORA Architect
- Capability Router
- Context Curator

## Expected Skills

- `bind-project-to-kora`
- `classify-task`
- `classify-scope`
- `select-context`
- `record-decision`, if a durable binding decision is made

## Expected Capability Assessment

KORA should identify:

```text
Repository purpose
Project type
Primary domains
Existing documentation
Existing AGENTS.md or local instructions
Existing .kora folder, if any
Relationship to KORA Core
Local context that should be created later
```

## Expected Binding Structure

KORA may propose:

```text
.kora/
  binding.md
  context/
  decisions/
  memory/
  agents/
  skills/
  tools/
  evals/
```

But it should avoid creating empty folders unless there is a clear reason or the user approves the initial structure.

## Expected Scope Behavior

KORA Core remains in `C:\KORA`.

Project-specific context and capabilities live in the project's `.kora/` folder.

Operational code remains in the normal project repository structure.

## Pass Criteria

This scenario passes if KORA:

- creates or proposes a clear project binding;
- distinguishes KORA Core from local project context;
- does not copy all KORA files into the project;
- identifies what should be local;
- identifies missing context to fill later.

## Fail Criteria

This scenario fails if KORA:

- duplicates KORA Core inside the project;
- stores project-specific details in global architecture files;
- creates unrelated agents, skills, or tools prematurely;
- ignores existing project documentation.
