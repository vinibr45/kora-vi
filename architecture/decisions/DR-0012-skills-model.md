# DR-0012: Modelo de skills da KORA

Status: accepted
Date: 2026-09-05
Scope: skills
Owner: Marcos

## Context

KORA ja possui skills centrais para classificar tarefas, escopo, contexto, conhecimento, projetos, decisoes e aprendizado.

Antes de criar muitas skills de dominio, KORA precisa definir o contrato de uma skill e como decidir se ela deve ser global, local ou hibrida.

## Decision

KORA adotara uma especificacao de skills em `docs/skills/kora-skills-spec-v0.4.md`.

Skills serao procedimentos reutilizaveis escritos em Markdown, com metadados opcionais em YAML frontmatter quando isso ajudar busca, selecao, revisao ou automacao futura.

KORA tambem tera um template em:

```text
skills/templates/skill-template.md
```

A skill `setup-kora-project` sera criada como fluxo assistido para conectar repositorios a KORA.

## Reasoning

Skills sao o elo entre conhecimento, agentes, ferramentas e execucao. Sem um contrato claro, elas podem virar prompts soltos ou duplicar conhecimento.

## Consequences

- Skills globais reutilizaveis ficam em `C:\KORA\skills\`.
- Skills especificas ficam no `.kora/skills/` do projeto.
- Skills hibridas usam um padrao global, mas guardam adaptacoes locais no projeto.
- KORA deve criar novas skills apenas quando houver recorrencia, complexidade, necessidade de consistencia ou ganho operacional claro.
- `setup-kora-project` nao e automacao completa em v0.4; e um contrato de workflow assistido.
