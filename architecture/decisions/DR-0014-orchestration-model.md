# DR-0014: Modelo de orquestracao da KORA

Status: accepted
Date: 2026-09-05
Scope: orchestration
Owner: Marcos

## Context

KORA ja possui modelos para conhecimento, contexto de projeto, skills e agentes.

Agora precisa definir como esses componentes sao coordenados quando o usuario solicita uma tarefa.

## Decision

KORA adotara uma especificacao de orquestracao em `docs/orchestration/kora-orchestration-spec-v0.6.md`.

A orquestracao deve coordenar classificacao de tarefa, deteccao de projeto, selecao de contexto, discovery de capacidades, capability plan, aprovacoes, modo de execucao, agentes, skills, tools, evals, entrega de resultado e aprendizado.

KORA tambem tera um template de capability plan em:

```text
orchestration/templates/capability-plan-template.md
```

## Reasoning

A forca central da KORA esta em decidir como uma tarefa deve ser resolvida e quais capacidades devem ser usadas, criadas ou propostas.

Sem orquestracao, agentes e skills ficam soltos. Com orquestracao, KORA consegue escolher o menor nivel de complexidade que resolve bem a tarefa e preservar limites globais/locais.

## Consequences

- Capability Management passa a ser responsabilidade central da orquestracao.
- Tarefas complexas, recorrentes, arriscadas ou ambíguas devem gerar capability plan.
- KORA deve pedir aprovacao antes de integracoes, automacoes, acesso a contas, publicacao, deploy, memoria e mudancas em fontes da verdade.
- Nem toda tarefa precisa de capability plan; tarefas simples podem ser executadas diretamente.
- v0.6 nao implementa runtime automatico.
