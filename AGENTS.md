# KORA Agent Instructions

## Repository Identity

This repository is KORA Core.

KORA means Knowledge-Orchestrated Reasoning Architecture. It is a reusable architecture for organizing knowledge, project context, memory, context selection, agents, skills, tools, integrations, automations, evaluations, experiments, and learning.

When this repository is open, assume the user may be asking KORA to help with a task even if they do not mention KORA by name.

## Default Operating Rule

Turn the user's request into the smallest useful KORA workflow.

Before creating or changing files, identify whether the request is:

```text
understanding KORA
using KORA for a task
connecting a project
creating knowledge
creating project context
creating a skill
creating an agent
creating or reviewing a tool
creating an integration
creating an automation
running or recording an eval
recording or promoting learning
```

If the task is simple and low risk, execute directly.

If the task is ambiguous, recurring, architectural, cross-project, or high impact, classify it before execution using:

```text
skills/route-user-request.md
skills/classify-task.md
skills/classify-scope.md
```

After durable changes to KORA artifacts, run the maintenance layer:

```text
skills/maintain-kora-indexes.md
automations/kora-index-maintenance.md
```

This means checking whether `CAPACIDADES.md`, `COMECE-AQUI.md`, `README.md`, folder README files, `projects/PROJECT-FLOW.md`, or `examples/` should be updated.

After meaningful KORA Core improvements, assess whether the change deserves versioning:

```text
skills/assess-kora-version-impact.md
skills/release-kora-version.md
```

If the impact is `patch`, `minor`, or `major`, update `VERSION.md` and `CHANGELOG.md`. Major version changes require explicit approval.

## Scope Rules

Protect the separation between KORA Core and project reality.

```text
Reusable across projects -> KORA Core
Specific to one project -> local .kora/ binding
Published/runtime code -> project repository
```

Do not put client-specific, business-specific, or implementation-specific details in KORA Core unless the user explicitly wants to generalize them into reusable knowledge, skill, agent, eval, tool, integration, or automation.

## Practical Routing

Use these routes when the user asks in plain language:

```text
"Como uso isso?" -> skills/use-kora.md
"Nao sei por onde comecar" -> skills/route-user-request.md
"Cria uma proposta" -> skills/create-commercial-proposal.md
"Cria uma skill" -> skills/create-skill.md
"Melhora/revisa uma skill" -> skills/review-skill.md
"Cria um agente" -> skills/create-agent.md
"Melhora/revisa um agente" -> skills/review-agent.md
"Guarda esse aprendizado" -> skills/record-learning.md
"Promove esse aprendizado" -> skills/promote-learning.md
"Registra uma decisao" -> skills/record-decision.md
"Cria conhecimento" -> skills/create-knowledge-entry.md
"Revisa conhecimento" -> skills/review-knowledge-entry.md
"Conecta um projeto" -> skills/setup-kora-project.md or skills/bind-project-to-kora.md
"Precisa de ferramenta/API?" -> skills/assess-integration-need.md
"Cria automacao" -> skills/create-automation.md
"Cria avaliacao/teste" -> skills/create-eval.md
"Roda uma avaliacao" -> skills/run-manual-eval.md
"Atualiza os indices" -> skills/maintain-kora-indexes.md
"Revisa se a KORA ficou consistente" -> skills/maintain-kora-indexes.md
"Vamos checar a saude" -> skills/check-kora-health.md
"Checa a saude" -> skills/check-kora-health.md
"Isso merece versao?" -> skills/assess-kora-version-impact.md
"Fecha uma versao" -> skills/release-kora-version.md
"Vamos rodar o dia" -> skills/run-daily-operating-loop.md
"Tive uma ideia" -> skills/capture-loose-idea.md
"Isso esta repetitivo" -> skills/detect-capability-gap.md
"Precisa de aprovacao?" -> skills/check-approval-needed.md
"Usa a KORA nesse projeto" -> skills/use-installed-kora.md
"Verifica a instalacao da KORA" -> skills/check-installed-kora.md
"Registra a instalacao da KORA" -> skills/register-installed-kora-project.md
"Gera uma imagem revisada" -> skills/generate-reviewed-image-asset.md
"Gera ate aprovar" -> skills/generate-reviewed-image-asset.md
"Revisa essa imagem" -> agents/image-asset-reviewer.md or skills/generate-reviewed-image-asset.md
"Analisa meus canais de marketing" -> skills/analyze-marketing-performance.md
"Olha o Analytics" -> skills/analyze-marketing-performance.md
"Ve o Google Ads" -> skills/analyze-marketing-performance.md
"Analisa o Instagram" -> skills/analyze-marketing-performance.md
```

Prefer the existing skill, agent, template, or specification before inventing a new structure.

## Context Selection

Load only the context needed for the task.

Useful entry points:

```text
README.md
COMECE-AQUI.md
CAPACIDADES.md
VERSION.md
CHANGELOG.md
MATURIDADE.md
GOVERNANCA.md
projects/INSTALLED-KORA.md
examples/
projects/PROJECT-FLOW.md
docs/architecture/kora-architecture-spec-v0.1.md
docs/implementation/kora-reference-implementation-bootstrap-v1.0.md
skills/route-user-request.md
skills/check-kora-health.md
skills/maintain-kora-indexes.md
skills/assess-kora-version-impact.md
skills/release-kora-version.md
skills/run-daily-operating-loop.md
skills/capture-loose-idea.md
skills/detect-capability-gap.md
skills/check-approval-needed.md
skills/use-installed-kora.md
skills/check-installed-kora.md
skills/register-installed-kora-project.md
skills/use-kora.md
skills/classify-task.md
skills/classify-scope.md
projects/README.md
skills/generate-reviewed-image-asset.md
agents/image-asset-reviewer.md
tools/image-generation.md
skills/analyze-marketing-performance.md
agents/marketing-performance-analyst.md
integrations/google-analytics-data-api.md
```

For project-specific work, look for a local `.kora/` binding in the operational project repository. KORA Core may contain only a lightweight project registry.

When working inside another repository that has `.kora/binding.md`, treat that repository as a KORA-connected project and use `skills/use-installed-kora.md`. Read the local binding before selecting Core context.

When installing or updating KORA in another repository, update `projects/INSTALLED-KORA.md` with the project name, repository path, local binding path, local `AGENTS.md`, installed KORA version, status, and last checked date.

## Editing Rules

- Keep changes small and consistent with the existing Markdown-first architecture.
- Use templates from `*/templates/` when creating new KORA artifacts.
- Preserve numbered decision records and existing IDs.
- Do not rename or reorganize core folders unless the user asks for an architectural change.
- Add cross-links when a new artifact becomes an important entry point.
- After adding durable artifacts, update the relevant indexes and entry points using `skills/maintain-kora-indexes.md`.
- After meaningful KORA Core improvements, assess version impact and update `VERSION.md` and `CHANGELOG.md` when justified.
- Check `GOVERNANCA.md` and `skills/check-approval-needed.md` before actions involving external systems, publishing, spend, sensitive data, automation activation, major versioning, or source-of-truth changes.
- Record a decision or learning only when the request or change justifies durable memory.

## User Experience Goal

The user should be able to open this repository and ask natural requests such as:

```text
Cria uma skill para isso.
Registra esse aprendizado.
Me ajuda a transformar essa ideia em automacao.
Cria um contexto para esse projeto.
Revisa se isso deveria ser core ou local.
Gera uma imagem revisada para esse post.
Gera ate aprovar e separa o resultado.
Analisa Analytics, Ads e Instagram desse projeto.
```

In those cases, route the request through KORA without requiring the user to say "KORA" every time.
