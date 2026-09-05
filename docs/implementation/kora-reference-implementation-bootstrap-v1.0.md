# KORA Reference Implementation Bootstrap v1.0

## 1. Purpose

This document records the first reference implementation bootstrap of KORA with a real project.

The first project connected to KORA is Marcos Dev.

## 2. Project

```text
Project: Marcos Dev
Operational Repository: C:\marcbmrs.github.io
KORA Core: C:\KORA
Local Binding: C:\marcbmrs.github.io\.kora\
```

## 3. What Was Implemented

The Marcos Dev repository received a local `.kora/` binding with:

```text
.kora/binding.md
.kora/context/overview.md
.kora/context/stack.md
.kora/decisions/DR-0001-kora-binding.md
.kora/memory/README.md
.kora/agents/README.md
.kora/skills/README.md
.kora/tools/README.md
.kora/evals/README.md
.kora/automations/README.md
.kora/experiments/README.md
```

## 4. What Was Not Implemented

This bootstrap did not create:

- project-specific agents;
- project-specific skills;
- integrations;
- automations;
- account access;
- publishing workflows;
- deployment workflows;
- full Marcos Dev strategy;
- full marketing knowledge base;
- changes to external systems.

## 5. Boundary

KORA Core keeps a lightweight registry of Marcos Dev.

The Marcos Dev repository owns its local project context and project-specific capabilities.

## 6. Next Work

Potential next steps:

- review Marcos Dev `.kora/` binding;
- decide whether to update `AGENTS.md` with KORA instructions;
- fill Marcos Dev local context files;
- identify first local skills or agents only after real recurring tasks justify them;
- run project binding eval.
