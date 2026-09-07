# DR-0021: Camada de manutencao organica da KORA

Status: accepted
Date: 2026-09-07
Scope: skills-automations-documentation
Owner: Marcos

## Context

KORA ganhou entradas praticas como `AGENTS.md`, `COMECE-AQUI.md`, `CAPACIDADES.md`, `projects/PROJECT-FLOW.md`, `examples/`, e a skill `route-user-request`.

Essas entradas tornam a KORA mais facil de usar, mas podem ficar desatualizadas quando novas skills, agentes, ferramentas, integracoes, automacoes, evals, projetos, exemplos, conhecimentos e decisoes forem criados.

## Decision

KORA tera uma camada global de manutencao organica composta por:

```text
skills/maintain-kora-indexes.md
automations/kora-index-maintenance.md
```

A skill define o procedimento de manutencao. A automacao define o loop recorrente e seus gatilhos.

## Reasoning

A KORA deve melhorar com o uso sem depender de memoria informal do operador.

Como a referencia atual e Markdown-first e nao executa processos em segundo plano, "organica" significa manutencao assistida por agente sempre que uma mudanca relevante ocorrer, ou quando o usuario pedir uma revisao de consistencia.

## Consequences

- Novas capacidades devem acionar uma revisao de indices e pontos de entrada.
- `CAPACIDADES.md` passa a ser tratado como indice vivo.
- `AGENTS.md` passa a instruir o agente a rodar a manutencao quando fizer sentido.
- `examples/` pode crescer a partir de casos reais recorrentes.
- `projects/PROJECT-FLOW.md` deve acompanhar mudancas no modelo de projeto.
- Isso nao cria execucao autonoma invisivel, scheduler, watcher de arquivos, nem alteracoes sem uma rodada de agente, script ou aprovacao humana.
