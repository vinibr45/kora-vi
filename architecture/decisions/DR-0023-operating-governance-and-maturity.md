# DR-0023: Loops operacionais, maturidade e governanca de aprovacao

Status: accepted
Date: 2026-09-07
Scope: operations-governance
Owner: Marcos

## Context

KORA passou a ter entradas praticas, roteamento natural, manutencao organica, health check e versionamento organico.

O proximo passo e apoiar o uso cotidiano com loops simples e proteger a evolucao com governanca explicita de aprovacao, maturidade e lacunas de capacidade.

## Decision

KORA tera capacidades globais para:

```text
rodar um loop diario
capturar ideias soltas
detectar lacunas de capacidade
checar necessidade de aprovacao
mapear maturidade
```

Essas capacidades serao registradas em:

```text
skills/run-daily-operating-loop.md
skills/capture-loose-idea.md
skills/detect-capability-gap.md
skills/check-approval-needed.md
MATURIDADE.md
GOVERNANCA.md
```

## Reasoning

KORA precisa ser facil de usar no dia a dia, mas tambem precisa evitar excesso de estrutura, automacoes prematuras e acoes sem permissao.

Ideias soltas, rotinas diarias e sinais de friccao devem virar o tipo certo de artefato somente quando houver valor, recorrencia, evidencia ou risco suficiente.

## Consequences

- O usuario pode pedir "vamos rodar o dia" sem nomear a skill.
- Ideias informais podem ser classificadas antes de virar conhecimento, skill, experimento ou automacao.
- Lacunas de capacidade podem ser detectadas antes de criar artefatos novos.
- `GOVERNANCA.md` passa a concentrar regras praticas de aprovacao.
- `MATURIDADE.md` passa a mostrar o estado operacional da KORA.
- Essas melhorias representam uma evolucao minor da KORA Core.

## Related

```text
skills/run-daily-operating-loop.md
skills/capture-loose-idea.md
skills/detect-capability-gap.md
skills/check-approval-needed.md
MATURIDADE.md
GOVERNANCA.md
```
