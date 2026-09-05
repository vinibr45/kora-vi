# DR-0009: Capacidades especificas ficam no projeto

Status: accepted
Date: 2026-09-05
Scope: architecture
Owner: Marcos

## Context

KORA precisa continuar limpa e reutilizavel. Se cada agente, skill, ferramenta ou automacao especifica de um projeto for criada dentro de KORA Core, a arquitetura central ficara contaminada por detalhes locais.

## Decision

Capacidades especificas de um projeto devem ser criadas no binding local desse projeto, nao em KORA Core.

Exemplo:

```text
C:\KORA
```

Guarda arquitetura, conhecimento e capacidades reutilizaveis.

```text
C:\marcbmrs.github.io\.kora
```

Guarda contexto, memoria, decisoes, agentes, skills, ferramentas, evals e automacoes especificas do Marcos Dev.

## Reasoning

Essa separacao permite que KORA seja usada em varios negocios sem virar uma copia do primeiro projeto.

## Consequences

- Antes de criar uma capacidade, KORA deve classificar o escopo como global, local ou hibrido.
- Capacidades locais devem ficar no `.kora` do projeto.
- Capacidades globais devem ficar em KORA Core.
- Capacidades hibridas devem usar templates ou conhecimento global, mas guardar adaptacoes locais no projeto.
