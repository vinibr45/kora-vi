# Comece Aqui

Este arquivo e a porta de entrada pratica da KORA.

Use quando voce abriu este repositorio e quer pedir alguma coisa sem precisar lembrar todas as pastas, agentes e skills.

## O Que E A KORA

KORA significa Knowledge-Orchestrated Reasoning Architecture.

Na pratica, ela e uma arquitetura para transformar trabalho com IA em um sistema organizado:

```text
contexto certo
conhecimento reutilizavel
skills para procedimentos
agentes para papeis
ferramentas e integracoes quando necessario
avaliacoes para qualidade
aprendizado para melhoria continua
```

## Como Pedir

Voce pode pedir em linguagem natural.

Exemplos:

```text
Cria uma proposta comercial para esse cliente.
Registra esse aprendizado.
Cria uma skill para esse processo.
Revisa se isso deveria ficar no core ou no projeto.
Conecta esse novo projeto a KORA.
Me ajuda a transformar esse fluxo em automacao.
Cria uma avaliacao para testar essa capacidade.
```

Com este repositorio aberto, o agente deve entender que pedidos assim podem ser roteados pela KORA mesmo quando voce nao menciona a KORA pelo nome.

## Fluxo Mais Simples

Quando voce tiver uma tarefa, pense assim:

```text
1. O que eu quero fazer?
2. Isso e uma tarefa unica ou algo recorrente?
3. Isso pertence ao core da KORA ou a um projeto especifico?
4. Ja existe uma skill, agente, ferramenta ou template para isso?
5. Depois da execucao, algo precisa virar aprendizado, decisao ou conhecimento?
```

Se voce nao souber responder, tudo bem. Peça do jeito natural:

```text
Me ajuda a decidir o caminho certo para isso.
```

## Caminhos Rapidos

```text
Pedido natural ou confuso -> skills/route-user-request.md
Checar saude da KORA -> skills/check-kora-health.md
Manter indices atualizados -> skills/maintain-kora-indexes.md
Avaliar impacto de versao -> skills/assess-kora-version-impact.md
Fechar nova versao -> skills/release-kora-version.md
Rodar o dia -> skills/run-daily-operating-loop.md
Capturar ideia solta -> skills/capture-loose-idea.md
Detectar lacuna de capacidade -> skills/detect-capability-gap.md
Checar aprovacao -> skills/check-approval-needed.md
Usar KORA instalada em outro repo -> skills/use-installed-kora.md
Checar instalacao em outro repo -> skills/check-installed-kora.md
Registrar instalacao em outro repo -> skills/register-installed-kora-project.md
Auditar UX com Chrome MCP -> skills/audit-ux-with-chrome-mcp.md
Gerar imagem revisada -> skills/generate-reviewed-image-asset.md
Analisar canais de marketing -> skills/analyze-marketing-performance.md
Criar wiki e videos de onboarding -> skills/create-client-onboarding-wiki-package.md
Criar wiki de mudancas de versao -> skills/create-version-change-wiki.md
Entender como usar -> skills/use-kora.md
Classificar uma tarefa -> skills/classify-task.md
Decidir onde algo deve morar -> skills/classify-scope.md
Criar conhecimento -> skills/create-knowledge-entry.md
Criar contexto de projeto -> skills/create-project-context.md
Conectar projeto -> skills/setup-kora-project.md
Criar skill -> skills/create-skill.md
Revisar skill -> skills/review-skill.md
Criar agente -> skills/create-agent.md
Revisar agente -> skills/review-agent.md
Criar ferramenta -> skills/create-tool.md
Criar integracao -> skills/create-integration.md
Criar automacao -> skills/create-automation.md
Criar avaliacao -> skills/create-eval.md
Registrar resultado de avaliacao -> skills/record-eval-result.md
Registrar aprendizado -> skills/record-learning.md
Promover aprendizado -> skills/promote-learning.md
Registrar decisao -> skills/record-decision.md
```

Para ver todas as capacidades em um so lugar:

```text
CAPACIDADES.md
```

Para exemplos realistas:

```text
examples/
```

Para maturidade e governanca:

```text
MATURIDADE.md
GOVERNANCA.md
```

Para fluxo de projetos:

```text
projects/PROJECT-FLOW.md
```

## Regra De Ouro

```text
KORA Core define a arquitetura.
O contexto do projeto define a realidade local.
```

Isso significa:

```text
Coisa reutilizavel em varios projetos -> KORA Core
Coisa especifica de um projeto -> .kora/ local do projeto
Codigo publicado ou produto final -> repositorio do projeto
```

## Quando Criar Algo Novo

Crie uma nova peca da KORA quando houver motivo real:

```text
skill -> existe um procedimento recorrente
agente -> existe um papel recorrente com julgamento proprio
conhecimento -> existe uma ideia reutilizavel e baseada em evidencia
ferramenta -> existe uma acao tecnica que precisa ser executada
integracao -> existe um sistema externo importante
automacao -> o fluxo ja e estavel o bastante para rodar com menos intervencao
eval -> existe comportamento que precisa ser testado ou comparado
aprendizado -> algo observado na pratica deve influenciar proximas execucoes
decisao -> uma escolha arquitetural ou operacional precisa ficar registrada
```

## Primeiro Passo Recomendado

Se estiver em duvida, comece com um pedido curto:

```text
Classifica essa tarefa e me diz o melhor caminho na KORA: [descreva a tarefa]
```

Se ja souber o que quer, peça direto. A KORA deve cuidar do roteamento por baixo.

Para uma auditoria rapida da KORA, peça:

```text
Vamos checar a saude.
```

Para saber se uma melhoria merece versionamento, peça:

```text
Isso merece versao?
```

## Como A KORA Se Mantem Viva

Quando uma mudanca duravel acontecer, como criar skill, agente, projeto, ferramenta, integracao, automacao, eval, conhecimento ou exemplo, use:

```text
skills/maintain-kora-indexes.md
automations/kora-index-maintenance.md
```

Isso nao roda sozinho em segundo plano. Significa que o agente deve revisar e atualizar os indices, guias e exemplos durante a propria conversa ou quando voce pedir uma manutencao.

## Como A KORA Versiona Melhorias

Depois de uma melhoria duravel, a KORA deve avaliar:

```text
sem versao nova
patch
minor
major
```

Se merecer versionamento, ela atualiza:

```text
VERSION.md
CHANGELOG.md
```

O fluxo natural e:

```text
melhoria -> manutencao dos indices -> checagem de saude se precisar -> avaliacao de impacto -> versionamento se merecer
```

## Pedidos Naturais Uteis

```text
Vamos rodar o dia.
Tive uma ideia: [ideia].
Isso esta repetitivo demais.
Precisa de aprovacao?
Usa a KORA nesse projeto.
Verifica a instalacao da KORA.
Gera uma imagem revisada para esse post.
Gera ate aprovar e separa o resultado.
Analisa Analytics, Ads e Instagram desse projeto.
Checa a saude do marketing desse projeto.
Cria uma wiki com videos para esse modulo.
Cria uma wiki das principais mudancas dessa versao.
```

## Usando A KORA Em Outros Repositorios

Quando um repositorio tiver KORA instalada, ele deve ter:

```text
.kora/binding.md
AGENTS.md
```

E a KORA Core deve registrar esse projeto em:

```text
projects/INSTALLED-KORA.md
```

O agente deve ler `.kora/binding.md`, usar o contexto local do projeto e buscar na KORA Core apenas os metodos reutilizaveis.

Use:

```text
skills/use-installed-kora.md
skills/check-installed-kora.md
skills/register-installed-kora-project.md
projects/templates/local-agents-template.md
projects/templates/local-kora-readme-template.md
```
