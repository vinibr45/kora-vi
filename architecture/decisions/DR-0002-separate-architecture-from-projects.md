# DR-0002: Separar arquitetura de projetos

Status: accepted
Date: 2026-09-05
Scope: architecture
Owner: Marcos

## Context

KORA precisa organizar tanto a arquitetura geral quanto os projetos e negocios que usarao essa arquitetura.

Se arquitetura e projetos forem misturados desde o inicio, a KORA corre o risco de virar apenas uma copia do primeiro negocio implementado.

## Decision

KORA deve separar arquitetura de projetos desde o inicio.

Arquitetura pertence a:

```text
architecture/
docs/architecture/
```

Projetos, negocios e implementacoes pertencem a:

```text
projects/
```

## Reasoning

Essa separacao preserva a capacidade de reutilizar a KORA em varios negocios e evita confundir metodologia com contexto operacional.

## Consequences

- Marcos Dev deve ser tratado como contexto de projeto, nao como a arquitetura KORA.
- Conhecimento geral reutilizavel deve ficar em `knowledge/`.
- Decisoes de projeto devem ficar dentro do projeto correspondente.
- Decisoes da arquitetura devem ficar em `architecture/decisions/`.
