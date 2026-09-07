# DR-0028: Camada de integracoes de canais de marketing

Status: accepted
Date: 2026-09-07
Scope: agents-skills-tools-integrations-automations-evals
Owner: Marcos

## Context

KORA precisa apoiar projetos que usam canais como Google Analytics, Google Ads, Instagram e futuros sistemas de marketing.

Algumas integracoes ja existiam de forma parcial, especialmente Google Ads e Instagram. Faltava uma camada reutilizavel que permitisse analisar canais de marketing em varios projetos conectados sem misturar credenciais, dados, contexto local ou permissoes.

## Decision

KORA tera uma camada global/hibrida de inteligencia de canais de marketing composta por:

```text
agents/marketing-performance-analyst.md
skills/analyze-marketing-performance.md
integrations/google-analytics-data-api.md
tools/google-analytics-read-connector.md
automations/marketing-channel-health-snapshot.md
evals/scenarios/EV-0016-marketing-channel-integrations.md
```

As definicoes existentes de Google Ads e Instagram continuam validas e passam a fazer parte dessa camada.

## Reasoning

Marketing exige leitura de dados externos, mas tambem exige limites claros:

- contas e credenciais sao locais/seguras;
- dados brutos de canal pertencem ao projeto;
- KORA Core guarda metodo, nao dados sensiveis;
- leitura e escrita devem ser separadas;
- recomendacao nao deve virar mudanca automatica de campanha, tag, post ou verba sem aprovacao.

## Consequences

- Pedidos como "analisa meus canais", "olha o Analytics", "ve o Ads" ou "compara Instagram e trafego" devem usar `skills/analyze-marketing-performance.md`.
- `agents/marketing-performance-analyst.md` passa a ser o papel responsavel por interpretar dados de marketing autorizados.
- Google Analytics ganha integracao e tool read-only propostas.
- Google Ads e Instagram continuam como conectores read-only existentes.
- Recorrencia semanal/mensal fica proposta em `automations/marketing-channel-health-snapshot.md`, nao ativa por padrao.

## Approval Requirements

Aprovacao humana e necessaria antes de:

- conectar contas externas;
- alterar scopes;
- armazenar exports brutos;
- criar sincronizacao recorrente;
- ler configuracoes administrativas quando isso amplia escopo;
- alterar campanhas, orcamentos, lances, audiencias, tags, eventos, conversoes, posts, comentarios ou mensagens.

## Related

```text
agents/marketing-performance-analyst.md
skills/analyze-marketing-performance.md
integrations/google-analytics-data-api.md
integrations/google-ads-api.md
integrations/meta-instagram-platform.md
tools/google-analytics-read-connector.md
tools/google-ads-read-connector.md
tools/instagram-read-connector.md
automations/marketing-channel-health-snapshot.md
evals/scenarios/EV-0016-marketing-channel-integrations.md
```
