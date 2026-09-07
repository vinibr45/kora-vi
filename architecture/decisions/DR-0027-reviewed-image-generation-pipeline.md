# DR-0027: Esteira revisada de geracao de imagem

Status: accepted
Date: 2026-09-07
Scope: agents-skills-tools-integrations-automations-evals
Owner: Marcos

## Context

KORA ja possui uma capacidade global de geracao de imagem, mas a necessidade real e maior do que gerar um arquivo.

O usuario quer poder solicitar a outra IA, via API, MCP, plugin ou outro mecanismo, a criacao de uma imagem. Depois disso, KORA deve avaliar a imagem, rejeitar quando necessario, explicar o que precisa melhorar, pedir nova versao, e separar corretamente o resultado aprovado.

## Decision

KORA tera uma esteira revisada de geracao de imagem composta por:

```text
agents/image-asset-reviewer.md
skills/generate-reviewed-image-asset.md
integrations/image-generation-provider.md
automations/reviewed-image-generation-loop.md
evals/scenarios/EV-0015-reviewed-image-generation-loop.md
```

A tool global `tools/image-generation.md` continua sendo a definicao generica da capacidade tecnica de gerar ou editar imagens.

## Reasoning

Geracao de imagem tem risco de baixa qualidade, desalinhamento visual, texto distorcido, custo, uso de conta externa, direitos de uso e contexto de marca.

Separar geracao, revisao, integracao, automacao e eval permite que KORA:

- continue independente de provedor;
- use contexto local de cada projeto;
- nao trate imagens candidatas como finais;
- repita o processo com limite claro;
- mantenha aprovacao humana nos pontos de risco;
- organize candidatos, rejeitados, aprovados e metadados.

## Consequences

- Pedidos como "gera uma imagem revisada" ou "gera ate aprovar" devem usar `skills/generate-reviewed-image-asset.md`.
- `agents/image-asset-reviewer.md` passa a ser o papel responsavel pela decisao de qualidade visual.
- Integracoes com provedores de imagem devem seguir `integrations/image-generation-provider.md`.
- A automacao fica proposta e sob demanda, nao como job autonomo permanente.
- Projeto especifico deve armazenar regras visuais e outputs no repositorio local ou `.kora/` local.
- KORA Core pode guardar exemplos e definicoes reutilizaveis, mas nao assets finais especificos de projeto por padrao.

## Storage Guidance

Para projetos conectados, usar estrutura local semelhante a:

```text
.kora/image-rules.md
.kora/brand-visual-context.md
.kora/image-generation-history.md
assets/images/generated/<asset-slug>/
  candidates/
  rejected/
  approved/
  metadata/
```

## Approval Requirements

Aprovacao humana e necessaria antes de:

- usar creditos pagos;
- conectar conta externa;
- enviar referencias privadas;
- usar imagem de pessoa privada;
- usar referencias protegidas por marca ou copyright;
- publicar, agendar, enviar ou fazer deploy do asset final.

## Related

```text
tools/image-generation.md
skills/generate-image-asset.md
agents/image-asset-reviewer.md
skills/generate-reviewed-image-asset.md
integrations/image-generation-provider.md
automations/reviewed-image-generation-loop.md
evals/scenarios/EV-0015-reviewed-image-generation-loop.md
```
