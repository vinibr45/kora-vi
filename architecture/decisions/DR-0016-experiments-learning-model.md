# DR-0016: Modelo de experimentos e aprendizado da KORA

Status: accepted
Date: 2026-09-05
Scope: experiments-learning
Owner: Marcos

## Context

KORA precisa melhorar com base em resultados reais, mas sem transformar qualquer observacao em memoria, conhecimento ou decisao permanente.

Experimentos e evals podem gerar evidencias, mas a promocao para fontes da verdade precisa de criterio e controle humano.

## Decision

KORA adotara uma especificacao de Experiments and Learning em `docs/learning/kora-experiments-learning-spec-v0.8.md`.

Experimentos testam hipoteses. Learning interpreta resultados e recomenda destino.

KORA tera templates em:

```text
experiments/templates/experiment-template.md
experiments/templates/learning-record-template.md
```

As skills `create-experiment`, `review-experiment` e `record-learning` serao criadas para apoiar essa etapa.

## Reasoning

Essa separacao impede que KORA confunda resultado isolado com verdade estavel. Tambem cria um caminho limpo para melhoria continua.

## Consequences

- Experimentos globais ficam em `C:\KORA\experiments\`.
- Experimentos locais ficam no `.kora/experiments/` do projeto.
- Learning records globais podem ficar em `C:\KORA\learning\` quando nao houver destino melhor.
- Promocao para memoria, conhecimento, decisao ou capacidade exige escopo, evidencia e aprovacao quando relevante.
- v0.8 nao implementa aprendizado automatico ou self-modifying behavior.
