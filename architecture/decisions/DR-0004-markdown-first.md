# DR-0004: Markdown como formato inicial

Status: accepted
Date: 2026-09-05
Scope: architecture
Owner: Marcos

## Context

KORA precisa ser legivel para humanos agora e automatizavel no futuro.

Formatos muito rigidos cedo demais podem atrapalhar a evolucao da arquitetura.

## Decision

Markdown sera o formato inicial para documentacao, conhecimento, contexto e decisoes.

Metadados estruturados poderao ser adicionados depois com YAML frontmatter quando houver ganho claro para busca, filtragem, selecao de contexto ou automacao.

## Reasoning

Markdown e simples, legivel, versionavel e facil de evoluir.

## Consequences

- A v0.1 pode continuar focada em clareza arquitetural.
- Schemas formais ficam para uma versao futura.
- Documentos importantes devem seguir modelos consistentes para facilitar leitura por humanos e por agentes.
