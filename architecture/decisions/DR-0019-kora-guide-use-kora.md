# DR-0019: KORA Guide e skill de uso da KORA

Status: accepted
Date: 2026-09-05
Scope: agents-skills
Owner: Marcos

## Context

KORA ja possui muitos componentes, agentes, skills e especificacoes. Para ser util no dia a dia, ela precisa de uma capacidade explicita de orientacao: explicar como usar a arquitetura e indicar o proximo workflow correto.

## Decision

KORA tera um agente global chamado `KORA Guide` e uma skill global chamada `use-kora`.

O agente explica e orienta. A skill transforma perguntas ou tarefas em um caminho pratico de uso da KORA.

## Reasoning

Sem uma camada de orientacao, KORA pode parecer abstrata demais. O KORA Guide ajuda o usuario a entender quando usar Capability Router, Project Binder, KORA Architect, Context Curator, Knowledge Steward ou skills especificas.

## Consequences

- `agents/kora-guide.md` passa a ser o agente de orientacao da KORA.
- `skills/use-kora.md` passa a ser a skill de uso pratico da arquitetura.
- KORA Guide nao substitui Capability Router em tarefas reais.
- A skill `use-kora` nao cria arquivos nem altera fontes da verdade sozinha.
