# DR-0008: KORA usa capacidades por dominio

Status: accepted
Date: 2026-09-05
Scope: architecture
Owner: Marcos

## Context

KORA deve ajudar em diferentes tipos de trabalho, incluindo marketing, negocios e desenvolvimento de software.

Quando o owner estiver criando uma aplicacao, site, sistema ou automacao para um projeto, a arquitetura precisa considerar a stack, os riscos e as capacidades especializadas necessarias.

## Decision

KORA deve usar o conceito de domain capability packs.

Um domain capability pack e um agrupamento arquitetural de conhecimento, agentes, skills, ferramentas, evals e criterios de qualidade relacionados a um dominio.

Exemplos de dominios:

- marketing;
- software engineering;
- UX;
- security;
- product;
- finance;
- operations;
- sales.

## Reasoning

Diferentes dominios exigem diferentes tipos de cuidado. Um calendario de posts precisa de marketing e conteudo. Um sistema com login precisa de seguranca, privacidade, teste e revisao tecnica.

## Consequences

- Capability Management deve identificar o dominio da tarefa.
- KORA deve avaliar stack, risco, recorrencia e contexto antes de sugerir agentes, skills, ferramentas ou automacoes.
- Agentes e skills especificos devem ser criados apenas quando houver necessidade real.
- Conhecimento global reutilizavel deve ficar em KORA Core; regras especificas do projeto devem ficar no binding local.
