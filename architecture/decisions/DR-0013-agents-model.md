# DR-0013: Modelo de agentes da KORA

Status: accepted
Date: 2026-09-05
Scope: agents
Owner: Marcos

## Context

KORA ja possui agentes centrais para arquitetura, roteamento de capacidades, binding de projetos, curadoria de contexto e stewardship de conhecimento.

Antes de criar agentes de dominio, KORA precisa definir o contrato de um agente e quando ele deve ser global, local ou hibrido.

## Decision

KORA adotara uma especificacao de agentes em `docs/agents/kora-agents-spec-v0.5.md`.

Agentes serao papeis orientados a objetivo, escritos em Markdown, com metadados opcionais em YAML frontmatter quando isso ajudar busca, selecao, revisao ou automacao futura.

KORA tambem tera um template em:

```text
agents/templates/agent-template.md
```

As skills `create-agent` e `review-agent` serao criadas para ajudar a KORA a criar e revisar agentes futuros.

## Reasoning

Agentes precisam ter papel, escopo, permissoes, limites, skills permitidas, ferramentas permitidas, evals e regras de handoff. Sem esse contrato, agentes podem virar prompts amplos demais ou misturar conhecimento, skills e ferramentas.

## Consequences

- Agentes globais reutilizaveis ficam em `C:\KORA\agents\`.
- Agentes especificos ficam no `.kora/agents/` do projeto.
- Agentes hibridos usam um padrao global, mas guardam adaptacoes locais no projeto.
- KORA deve criar novos agentes apenas quando houver recorrencia, julgamento especializado, fronteira de permissao, risco ou necessidade clara de papel.
- Agentes v0.5 sao definicoes arquiteturais, nao workers autonomos em runtime.
