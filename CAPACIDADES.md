# Capacidades Da KORA

Este e o indice vivo das capacidades atuais da KORA Core.

Use quando quiser descobrir rapidamente qual agente, skill, ferramenta, integracao, automacao ou avaliacao combina com uma tarefa.

## Entrada Mais Rapida

```text
Pedido natural -> skills/route-user-request.md
Checagem de saude -> skills/check-kora-health.md
Impacto de versao -> skills/assess-kora-version-impact.md
Fechar versao -> skills/release-kora-version.md
Rodar o dia -> skills/run-daily-operating-loop.md
Capturar ideia -> skills/capture-loose-idea.md
Detectar lacuna -> skills/detect-capability-gap.md
Checar aprovacao -> skills/check-approval-needed.md
Usar KORA instalada -> skills/use-installed-kora.md
Checar instalacao KORA -> skills/check-installed-kora.md
Registrar instalacao KORA -> skills/register-installed-kora-project.md
Gerar imagem revisada -> skills/generate-reviewed-image-asset.md
Analisar canais de marketing -> skills/analyze-marketing-performance.md
Duvida sobre uso -> skills/use-kora.md
Tarefa complexa -> skills/classify-task.md
Duvida de local correto -> skills/classify-scope.md
```

## Agentes

```text
agents/kora-guide.md
```
Explica a KORA e ajuda o usuario a escolher o proximo caminho.

```text
agents/capability-router.md
```
Decide se uma tarefa deve ser executada diretamente, usar uma capacidade existente ou gerar uma nova capacidade.

```text
agents/context-curator.md
```
Seleciona o contexto minimo necessario sem carregar tudo.

```text
agents/kora-architect.md
```
Protege a arquitetura, escopo, limites e evolucao da KORA Core.

```text
agents/project-binder.md
```
Conecta repositorios de projeto a KORA por meio de uma camada local `.kora/`.

```text
agents/knowledge-steward.md
```
Organiza conhecimento reutilizavel e protege fronteiras entre conhecimento, memoria, decisao e contexto.

```text
agents/browser-ux-auditor.md
```
Revisa aplicacoes web pagina a pagina usando Chrome via MCP, com evidencias por mobile, tablet e desktop.

```text
agents/image-asset-reviewer.md
```
Avalia imagens geradas, decide aprovacao/reprovacao, cria instrucoes de revisao e recomenda organizacao do asset final.

```text
agents/marketing-performance-analyst.md
```
Analisa canais de marketing autorizados, como Google Analytics, Google Ads e Instagram, preservando limites read-only e contexto local do projeto.

## Skills De Navegacao

```text
skills/route-user-request.md
skills/check-kora-health.md
skills/maintain-kora-indexes.md
skills/assess-kora-version-impact.md
skills/release-kora-version.md
skills/run-daily-operating-loop.md
skills/capture-loose-idea.md
skills/detect-capability-gap.md
skills/check-approval-needed.md
skills/use-installed-kora.md
skills/check-installed-kora.md
skills/register-installed-kora-project.md
skills/generate-reviewed-image-asset.md
skills/analyze-marketing-performance.md
skills/use-kora.md
skills/classify-task.md
skills/classify-scope.md
skills/select-context.md
skills/create-capability-plan.md
skills/create-capability.md
```

Use quando o pedido ainda precisa ser entendido, roteado ou dividido antes da execucao.

Use `skills/maintain-kora-indexes.md` depois de mudancas duraveis para manter entradas, indices e exemplos alinhados.

Use `skills/assess-kora-version-impact.md` e `skills/release-kora-version.md` quando uma melhoria da KORA talvez mereca nova versao.

Use `skills/run-daily-operating-loop.md`, `skills/capture-loose-idea.md`, `skills/detect-capability-gap.md` e `skills/check-approval-needed.md` para operar a KORA no dia a dia com controle.

Use `skills/use-installed-kora.md` e `skills/check-installed-kora.md` quando estiver dentro de outro repositorio conectado por `.kora/binding.md`.

Use `skills/register-installed-kora-project.md` para manter `projects/INSTALLED-KORA.md` atualizado com nome, caminho, binding, AGENTS local, versao instalada e status.

## Skills De Projeto

```text
skills/setup-kora-project.md
skills/bind-project-to-kora.md
skills/create-project-context.md
skills/review-project-context.md
skills/setup-kora-operational-loop.md
```

Use quando um projeto precisa se conectar a KORA, ganhar contexto local ou melhorar sua camada `.kora/`.

## Skills De Conhecimento, Memoria E Decisao

```text
skills/create-knowledge-entry.md
skills/review-knowledge-entry.md
skills/record-learning.md
skills/review-learning.md
skills/promote-learning.md
skills/record-decision.md
```

Use quando uma ideia, observacao, aprendizado ou escolha precisa persistir.

## Skills De Capacidades

```text
skills/create-skill.md
skills/review-skill.md
skills/create-agent.md
skills/review-agent.md
skills/create-tool.md
skills/review-tool.md
skills/create-integration.md
skills/review-integration.md
skills/create-automation.md
skills/review-automation.md
```

Use quando a KORA precisa ganhar, revisar ou amadurecer uma capacidade.

## Skills De Qualidade E Aprendizado Experimental

```text
skills/create-eval.md
skills/review-eval.md
skills/run-manual-eval.md
skills/record-eval-result.md
skills/create-experiment.md
skills/review-experiment.md
skills/review-capability-plan.md
skills/review-capability-gaps.md
```

Use quando a qualidade, risco ou aprendizado de uma capacidade precisa ser testado.

## Skills De Negocio

```text
skills/create-commercial-proposal.md
skills/create-sales-follow-up.md
skills/review-service-response.md
skills/diagnose-business-workflow.md
skills/select-ai-use-case.md
skills/create-product-discovery-brief.md
skills/create-cash-flow-snapshot.md
```

Use para trabalho pratico de vendas, atendimento, operacoes, produto, IA aplicada e gestao.

## Skills De Criacao Visual

```text
skills/generate-image-asset.md
skills/generate-reviewed-image-asset.md
skills/generate-design-files-with-claude.md
```

Use quando a tarefa envolve imagens, design files ou assets visuais.

Use `skills/generate-reviewed-image-asset.md` quando o pedido envolver gerar, avaliar, reprovar, pedir nova versao e separar imagens aprovadas.

## Skills De Marketing E Canais

```text
skills/analyze-marketing-performance.md
```

Use quando a tarefa envolve Google Analytics, Google Ads, Instagram, trafego, campanhas, conteudo, conversoes, atribuicao ou leitura de canais de marketing.

## Skills De UX E Browser

```text
skills/audit-ux-with-chrome-mcp.md
```

Use para auditar paginas e fluxos de aplicacoes web em Chrome via MCP, com screenshots, DOM, console e checagem responsiva em mobile, tablet e desktop.

## Ferramentas

```text
tools/image-generation.md
tools/instagram-read-connector.md
tools/google-ads-read-connector.md
tools/claude-design-file-generation.md
tools/google-analytics-read-connector.md
```

Ferramentas executam capacidades. Elas nao decidem sozinhas quando devem ser usadas.

## Integracoes

```text
integrations/meta-instagram-platform.md
integrations/google-ads-api.md
integrations/claude-design.md
integrations/chrome-mcp-browser-control.md
integrations/image-generation-provider.md
integrations/google-analytics-data-api.md
```

Integracoes conectam a KORA a sistemas externos. Avalie necessidade, permissao, privacidade e fallback antes de usar.

## Automacoes

```text
automations/claude-design-file-generation.md
automations/kora-index-maintenance.md
automations/reviewed-image-generation-loop.md
automations/marketing-channel-health-snapshot.md
```

Automacoes representam workflows repetiveis que podem ganhar menos intervencao humana depois de aprovados.

## Evals

```text
evals/scenarios/
evals/results/
evals/browser-page-ux-readiness.md
evals/scenarios/EV-0015-reviewed-image-generation-loop.md
evals/scenarios/EV-0016-marketing-channel-integrations.md
```

Evals testam qualidade, limites, utilidade e fit arquitetural. Use especialmente antes ou depois de mudancas em capacidades.

## Governanca, Maturidade E Versao

```text
GOVERNANCA.md
MATURIDADE.md
VERSION.md
CHANGELOG.md
```

Use para entender limites de aprovacao, estado de maturidade e historico de evolucao da KORA.

## Regra De Escolha

```text
Se e simples -> execute diretamente.
Se e confuso -> route-user-request.
Se pediu saude -> check-kora-health.
Se e complexo -> classify-task.
Se cria artefato duravel -> classify-scope.
Se vira rotina -> skill antes de automacao.
Se usa sistema externo -> assess-integration-need.
Se precisa medir qualidade -> eval.
Se ensinou algo -> record-learning.
Se mudou a KORA -> maintain-kora-indexes.
Se a melhoria foi duravel -> assess-kora-version-impact.
Se e rotina do dia -> run-daily-operating-loop.
Se e ideia solta -> capture-loose-idea.
Se esta repetitivo ou faltando suporte -> detect-capability-gap.
Se envolve risco ou permissao -> check-approval-needed.
Se esta em outro repo com .kora -> use-installed-kora.
Se a instalacao local parece incerta -> check-installed-kora.
Se instalou KORA em um repo -> register-installed-kora-project.
Se quer gerar imagem e so aceitar quando passar na avaliacao -> generate-reviewed-image-asset.
Se quer analisar Analytics, Ads, Instagram ou canais de marketing -> analyze-marketing-performance.
```
