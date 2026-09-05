# DR-0010: Modelo de conhecimento da KORA

Status: accepted
Date: 2026-09-05
Scope: knowledge
Owner: Marcos

## Context

KORA precisa armazenar conhecimento reutilizavel sem virar uma colecao de arquivos gigantes ou misturar teoria global com contexto local dos projetos.

Marketing sera o primeiro dominio de conhecimento priorizado.

## Decision

KORA usara Markdown como formato inicial para conhecimento, com YAML frontmatter quando metadados forem uteis.

Conhecimento reutilizavel ficara em `knowledge/`.

Aplicacoes especificas de projeto ficarao no `.kora/` local do projeto.

## Reasoning

Markdown mantem o sistema legivel e facil de evoluir. Metadados leves permitem futura busca, filtragem e selecao de contexto sem impor infraestrutura cedo demais.

## Consequences

- `docs/knowledge/kora-knowledge-spec-v0.2.md` define o modelo.
- `knowledge/templates/knowledge-entry-template.md` serve como ponto de partida.
- `knowledge/marketing/` e o primeiro dominio.
- KORA deve evitar criar uma enciclopedia de marketing antes de necessidade real.
