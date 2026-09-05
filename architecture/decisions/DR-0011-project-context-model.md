# DR-0011: Modelo de contexto de projeto

Status: accepted
Date: 2026-09-05
Scope: project-context
Owner: Marcos

## Context

KORA precisa organizar varios projetos e negocios sem misturar a arquitetura central com detalhes locais.

Cada projeto pode ter identidade, publico, ofertas, stack, decisoes, memoria, agentes, skills, ferramentas, evals e automacoes proprias.

## Decision

KORA adotara um modelo de Project Context com duas camadas:

```text
C:\KORA\projects\<project-name>\
```

Para registro leve em KORA Core.

```text
<project-repository>\.kora\
```

Para contexto e capacidades locais do projeto.

## Reasoning

Essa divisao permite que KORA saiba que o projeto existe e consiga roteá-lo, sem duplicar o repositorio operacional nem contaminar KORA Core com detalhes especificos.

## Consequences

- `docs/projects/kora-project-context-spec-v0.3.md` define o modelo.
- `projects/templates/` guarda templates de binding, contexto e registro.
- Marcos Dev permanece registrado em `projects/marcos-dev/`.
- O binding operacional real do Marcos Dev deve ser criado em `C:\marcbmrs.github.io\.kora\` quando aprovado.
- KORA Core deve evitar armazenar estrategia completa, historico ou capacidades locais dos projetos.
