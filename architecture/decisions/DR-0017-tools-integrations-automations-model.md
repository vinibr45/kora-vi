# DR-0017: Modelo de ferramentas, integracoes e automacoes da KORA

Status: accepted
Date: 2026-09-05
Scope: tools-integrations-automations
Owner: Marcos

## Context

KORA precisa diferenciar capacidades executaveis, conexoes externas e fluxos recorrentes.

Sem essa separacao, ferramentas podem virar permissoes implicitas, integracoes podem ser criadas cedo demais e automacoes podem executar efeitos externos sem controle suficiente.

## Decision

KORA adotara uma especificacao de Tools, Integrations and Automations em `docs/tools/kora-tools-integrations-automations-spec-v0.9.md`.

KORA tera templates em:

```text
tools/templates/tool-template.md
integrations/templates/integration-template.md
automations/templates/automation-template.md
```

KORA tambem tera skills para criar e revisar ferramentas, integracoes e automacoes.

## Reasoning

Ferramentas executam, integracoes conectam e automacoes repetem. Cada uma precisa de contrato, permissoes, limites, falhas e pontos de aprovacao.

## Consequences

- Tools globais ficam em `C:\KORA\tools\`.
- Integrations globais ficam em `C:\KORA\integrations\`.
- Automations globais ficam em `C:\KORA\automations\`.
- Versoes especificas de projeto ficam no `.kora/` local.
- Integracoes reais, credenciais, publicacao, deploy, gasto e automacoes recorrentes exigem aprovacao.
- v0.9 nao implementa conectores, scripts ou engine de automacao.
