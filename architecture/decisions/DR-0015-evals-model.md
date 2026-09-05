# DR-0015: Modelo de evals da KORA

Status: accepted
Date: 2026-09-05
Scope: evals
Owner: Marcos

## Context

KORA precisa avaliar qualidade, limites, riscos e adequacao arquitetural antes e depois de tarefas importantes.

Ate agora, a KORA possui cenarios manuais de teste, mas ainda nao havia um contrato formal para evals.

## Decision

KORA adotara uma especificacao de evals em `docs/evals/kora-evals-spec-v0.7.md`.

Evals serao criterios estruturados para avaliar artefatos, processos, decisoes, capacidades ou comportamentos.

KORA tera templates em:

```text
evals/templates/eval-template.md
evals/templates/eval-result-template.md
```

As skills `create-eval`, `review-eval` e `run-manual-eval` serao criadas para definir, revisar e executar/simular evals manuais.

## Reasoning

Evals impedem que KORA apenas crie capacidades sem verificar qualidade, risco ou limites. Eles tambem criam uma ponte entre execucao e aprendizado.

## Consequences

- Evals globais reutilizaveis ficam em `C:\KORA\evals\`.
- Evals especificos ficam no `.kora/evals/` do projeto.
- Resultados de eval devem ser armazenados apenas quando afetarem decisoes futuras, aprendizado ou baseline de qualidade.
- Evals nao alteram memoria, conhecimento ou decisoes automaticamente.
- v0.7 nao implementa runner automatico.
