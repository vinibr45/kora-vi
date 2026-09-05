# DR-0006: KORA gerencia capacidades

Status: accepted
Date: 2026-09-05
Scope: architecture
Owner: Marcos

## Context

KORA precisa decidir como uma tarefa deve ser resolvida, nao apenas armazenar conhecimento ou executar pedidos isolados.

Ao receber uma tarefa em qualquer projeto, KORA deve ajudar a decidir se deve executar diretamente, usar uma capacidade existente ou criar/propor uma nova capacidade.

## Decision

KORA tera uma responsabilidade arquitetural chamada Capability Management.

Essa responsabilidade decide entre:

- executar diretamente;
- usar agente existente;
- criar ou propor novo agente;
- usar skill existente;
- criar ou propor nova skill;
- usar ferramenta existente;
- criar ou propor ferramenta, integracao ou automacao;
- aplicar eval;
- registrar memoria ou decisao.

## Reasoning

Esse e o mecanismo que transforma KORA em uma arquitetura evolutiva para negocios, em vez de uma colecao estatica de documentos.

## Consequences

- Orquestracao deve incluir roteamento de capacidades.
- KORA Core deve guardar capacidades reutilizaveis.
- Bindings locais devem guardar capacidades especificas do projeto.
- Novas capacidades devem ser criadas por necessidade real, recorrencia, especializacao ou ganho operacional claro.
