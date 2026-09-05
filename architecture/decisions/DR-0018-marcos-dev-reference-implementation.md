# DR-0018: Marcos Dev como primeira implementacao de referencia

Status: accepted
Date: 2026-09-05
Scope: implementation
Owner: Marcos

## Context

KORA ja possui modelos para arquitetura, conhecimento, contexto de projeto, skills, agentes, orquestracao, evals, experimentos, aprendizado, ferramentas, integracoes e automacoes.

O proximo passo e validar a arquitetura conectando um projeto real sem sujar KORA Core.

## Decision

Marcos Dev sera a primeira implementacao de referencia da KORA.

O binding local foi criado em:

```text
C:\marcbmrs.github.io\.kora\
```

KORA Core manterá apenas um registro leve em:

```text
C:\KORA\projects\marcos-dev\
```

## Reasoning

Marcos Dev e um projeto real com contexto de negocio, marketing, web, clientes, conteudo e operacao. Ele e suficiente para testar a arquitetura de binding local.

## Consequences

- Marcos Dev agora esta em nivel `level-1 bound`.
- Contexto e capacidades especificas devem ficar em `C:\marcbmrs.github.io\.kora\`.
- KORA Core nao deve copiar a estrategia, memoria ou capacidades locais do Marcos Dev.
- Nenhum agente, skill, integracao ou automacao local foi criado nesta decisao.
- `AGENTS.md` do Marcos Dev nao foi alterado nesta etapa para evitar conflito com mudancas existentes.
