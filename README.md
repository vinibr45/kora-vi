# KORA

**KORA** means **Knowledge-Orchestrated Reasoning Architecture**.

KORA is a reusable architecture for agentic systems that organize knowledge, project context, memory, context selection, agents, skills, tools, orchestration, execution, evaluations, experiments, and learning.

KORA is not a single agent, a prompt collection, or a Markdown knowledge dump. It is an architecture and methodology that can later support many implementations, such as a personal system, a company-specific system, or a product-specific agentic environment.

KORA is private and proprietary by default. It is being designed first for the creator's own projects and businesses, with possible future use in company contexts.

## Current Version

The current version is:

```text
1.7.0
```

The current stage is:

```text
Marketing Channel Integration Layer
```

Version details are maintained in:

```text
VERSION.md
CHANGELOG.md
```

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
tools/               KORA Core tool definitions
integrations/        KORA Core external integration definitions
automations/         KORA Core automation definitions
evals/               Evaluation definitions, scenarios, and results
experiments/         Future experiment and learning records
config/              Future implementation configuration
```

## Start Here

For practical day-to-day use, start with:

```text
COMECE-AQUI.md
```

For a capability index, see:

```text
CAPACIDADES.md
```

For keeping indexes and entry points current, see:

```text
skills/maintain-kora-indexes.md
automations/kora-index-maintenance.md
```

For a KORA health check, use:

```text
skills/check-kora-health.md
evals/scenarios/EV-0014-kora-health-check.md
```

For version impact and releases, use:

```text
skills/assess-kora-version-impact.md
skills/release-kora-version.md
VERSION.md
CHANGELOG.md
```

For maturity and governance, see:

```text
MATURIDADE.md
GOVERNANCA.md
```

For using KORA inside connected project repositories, see:

```text
projects/INSTALLED-KORA.md
skills/use-installed-kora.md
skills/check-installed-kora.md
skills/register-installed-kora-project.md
projects/PROJECT-FLOW.md
projects/templates/local-agents-template.md
projects/templates/local-kora-readme-template.md
```

For realistic usage examples, see:

```text
examples/
```

For reviewed image generation workflows, see:

```text
skills/generate-reviewed-image-asset.md
agents/image-asset-reviewer.md
integrations/image-generation-provider.md
automations/reviewed-image-generation-loop.md
```

For marketing channel integrations, see:

```text
skills/analyze-marketing-performance.md
agents/marketing-performance-analyst.md
integrations/google-analytics-data-api.md
tools/google-analytics-read-connector.md
automations/marketing-channel-health-snapshot.md
```

For agent-facing repository instructions, see:

```text
AGENTS.md
```

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

Current agents specification:

```text
docs/agents/kora-agents-spec-v0.5.md
```

Current orchestration specification:

```text
docs/orchestration/kora-orchestration-spec-v0.6.md
```

Current evals specification:

```text
docs/evals/kora-evals-spec-v0.7.md
```

Current experiments and learning specification:

```text
docs/learning/kora-experiments-learning-spec-v0.8.md
```

Current tools, integrations, and automations specification:

```text
docs/tools/kora-tools-integrations-automations-spec-v0.9.md
```

Current reference implementation bootstrap:

```text
docs/implementation/kora-reference-implementation-bootstrap-v1.0.md
```
