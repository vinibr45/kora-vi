# DR-0005: Marcos Dev como primeiro projeto

Status: accepted
Date: 2026-09-05
Scope: architecture
Owner: Marcos

## Context

Marcos Dev e o perfil/negocio inicial do owner para oferecer servicos como criacao de sites, criacao de sistemas e presenca digital.

O repositorio operacional atual fica em:

```text
C:\marcbmrs.github.io
```

Esse repositorio contem site institucional, paginas de campanha, prototipos, ativos, conteudo de Instagram, diagnostico de presenca digital, presenca local Google e projetos de clientes.

## Decision

Marcos Dev sera o primeiro contexto de projeto/negocio previsto na KORA.

Ele deve ficar em:

```text
projects/marcos-dev/
```

## Reasoning

Marcos Dev e um caso real suficiente para testar a arquitetura sem transformar a KORA em uma abstracao distante.

## Consequences

- Conteudo especifico do Marcos Dev deve ficar em `projects/marcos-dev/`.
- Conhecimento geral de marketing deve ficar em `knowledge/marketing/`.
- KORA pode consultar o repositorio local do Marcos Dev como referencia, mas nao deve copiar tudo automaticamente.
- A arquitetura KORA deve permanecer reutilizavel para outros negocios.
