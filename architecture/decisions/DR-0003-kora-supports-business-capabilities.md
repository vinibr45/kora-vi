# DR-0003: KORA organiza capacidades de negocio

Status: accepted
Date: 2026-09-05
Scope: architecture
Owner: Marcos

## Context

KORA nao deve ser apenas uma base para agentes isolados. Ela deve ajudar a construir capacidades reutilizaveis para negocios.

Essas capacidades podem incluir conhecimento, contexto, agentes, skills, ferramentas, evals, experimentos e aprendizados.

## Decision

KORA deve funcionar como uma arquitetura para criar capacidades que ajudam negocios.

Ela deve poder aprender e se estruturar conforme cada dominio solicitado, como marketing, financeiro, produto, vendas ou operacoes.

## Reasoning

Isso permite que KORA cresca de forma modular conforme necessidades reais, sem tentar prever todos os dominios desde o inicio.

## Consequences

- O primeiro dominio de conhecimento priorizado sera marketing.
- Novos dominios devem nascer apenas quando houver demanda real.
- Agentes, skills e ferramentas devem surgir a partir de necessidades concretas de negocio.
- A arquitetura deve evitar criar componentes vazios apenas por antecipacao.
