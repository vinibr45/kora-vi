# KORA

**KORA** means **Knowledge-Orchestrated Reasoning Architecture**.

KORA is a reusable architecture for agentic systems that organize knowledge, project context, memory, context selection, agents, skills, tools, orchestration, execution, evaluations, experiments, and learning.

KORA is not a single agent, a prompt collection, or a Markdown knowledge dump. It is an architecture and methodology that can later support many implementations, such as a personal system, a company-specific system, or a product-specific agentic environment.

KORA is private and proprietary by default. It is being designed first for the creator's own projects and businesses, with possible future use in company contexts.

## Current Version

The current stage is:

```text
KORA Skills Specification v0.4
```

This stage extends KORA with the v0.4 skills model. It defines how reusable procedures are written, scoped, reviewed, and connected to agents, knowledge, tools, evals, and project bindings.

## Repository Map

```text
docs/architecture/   Formal architecture specifications
architecture/        Core principles, components, boundaries, and information flow
knowledge/           Reusable knowledge base structure
projects/            Project-specific, business-specific, and implementation-specific context
memory/              Operational memory and learning records
context/             Context selection and assembly rules
orchestration/       Coordination model for tasks, agents, skills, and tools
agents/              KORA Core agent definitions
skills/              KORA Core skill definitions
tools/               Future external tool contracts and integrations
evals/               Future evaluation criteria and mechanisms
experiments/         Future experiment and learning records
config/              Future implementation configuration
```

## Start Here

Read the initial specification:

```text
docs/architecture/kora-architecture-spec-v0.1.md
```


## Initial Direction

KORA should support both:

- agentic systems for business work;
- business management context such as positioning, offers, content, operations, products, and decisions.

The first intended business context is:

```text
projects/marcos-dev/
```

MarcosOS is treated as a prior personal brain/operating concept. KORA is the cleaner and more modular architecture that may absorb lessons from MarcosOS without becoming a copy of it.

Current knowledge specification:

```text
docs/knowledge/kora-knowledge-spec-v0.2.md
```


Current project context specification:

```text
docs/projects/kora-project-context-spec-v0.3.md
```

Current skills specification:

```text
docs/skills/kora-skills-spec-v0.4.md
```
