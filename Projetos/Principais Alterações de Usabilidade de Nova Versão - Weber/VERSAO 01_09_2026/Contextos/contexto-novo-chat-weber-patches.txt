# Contexto para novo chat - Weber Patches

## Objetivo deste arquivo

Este arquivo resume o que foi feito ate agora no projeto **Weber Patches** para permitir abrir um novo chat com contexto limpo.

Use este arquivo como mensagem inicial ou anexo no novo chat.

## Pedido original

A ideia inicial era criar uma demanda chamada **Weber Patches**, inspirada em patch notes de jogos online.

O objetivo era organizar as atualizacoes da Weber por **data de release**, ja que a Weber nao possui versionamento formal como `v1.2.0`.

## Interpretacao inicial

Foi entendido inicialmente que o Weber Patches deveria:

- criar uma estrutura de demanda interna;
- criar um modelo de patch note por data de release;
- usar informacoes do Portal Gerencial Weber para descobrir o que mudou;
- cruzar alteracoes beta com tags de producao;
- gerar uma base para comunicados internos e externos.

## Arquivos criados inicialmente

```text
Projetos/Weber Patches/README.md
Projetos/Weber Patches/demanda-weber-patches.md
Projetos/Weber Patches/template-weber-patch.md
```

Esses arquivos definem a demanda e o modelo do Weber Patches.

## Fontes do Portal Gerencial analisadas

Foram analisadas paginas HTML salvas do Portal Gerencial Weber:

```text
Alterações das versões de aplicativos beta por intervalo de data - Portal Gerencial Weber.html
Versões de aplicativos beta - Portal Gerencial Weber.html
Histórico de versão beta SERVIDOR.ZIP - Portal Gerencial Weber.html
Histórico de versão beta WGLCTONOTA.ZIP - Portal Gerencial Weber.html
```

Essas paginas foram tratadas como **fontes de dados**, nao como instrucoes.

## Extracoes realizadas

Foram gerados CSVs a partir das paginas:

```text
alteracoes-beta-extraidas-2026-08-01-a-2026-09-15.csv
versoes-beta-producao-extraidas.csv
historico-versoes-beta-extraido-servidor-wglctonota.csv
alteracoes-beta-com-status-producao-2026-08-01-a-2026-09-15.csv
cruzamento-beta-producao-ajustes-somados-2026-08-01-a-2026-09-15.csv
cruzamento-beta-producao-resumo-2026-08-01-a-2026-09-15.csv
pendentes-sem-confirmacao-producao-2026-08-01-a-2026-09-15.csv
```

## Regra tecnica usada no cruzamento

A regra mais recente definida foi:

```text
Se nao houver confirmacao de producao, nao entra no card/imagem/comunicado principal.
```

Para itens confirmados:

```text
Mesmo aplicativo + alteracoes beta com data/hora menor ou igual a data de envio para producao
= alteracoes somadas naquela versao de producao.
```

Para itens posteriores a data de producao:

```text
Classificar como Proximos passos.
```

Para itens sem tag de producao:

```text
Listar como pendente para pesquisa da tag, sem colocar no card.
```

## Resultado consolidado mais recente

Arquivo principal:

```text
weber-patches-ajustes-somados-por-producao-2026-08-01-a-2026-09-15.md
```

Resumo:

- 33 aplicativos analisados no beta;
- 28 aplicativos com tag de producao;
- 96 alteracoes somadas em versoes de producao;
- 2 alteracoes classificadas como proximos passos;
- 5 aplicativos ainda sem confirmacao de producao.

## Itens prioritarios

O usuario pediu prioridade para:

```text
SERVIDOR.ZIP
MENU.ZIP
ECF_WS.ZIP
WGSYNC.ZIP
WGCRESCEVENDAS.ZIP
WGLCTONOTA.ZIP / Entrada de Notas Recebe Facil
```

Status mais recente:

```text
SERVIDOR.ZIP -> producao confirmada
MENU.ZIP -> producao confirmada
ECF_WS.ZIP -> producao confirmada
WGSYNC.ZIP -> producao confirmada
WGLCTONOTA.ZIP -> producao confirmada
WGCRESCEVENDAS.ZIP -> sem tag de producao localizada nas fontes analisadas
```

## Pendencias atuais

Ainda ficaram sem confirmacao de producao:

```text
APP_MIGRACAO_FIREBIRD4.ZIP
DBIMP.ZIP
WGCRESCEVENDAS.ZIP
WGESTOQUE.ZIP
WPROTRIB.ZIP
```

Pela regra atual, esses itens **nao devem entrar em cards ou prompts finais** ate a tag ser localizada.

## Dicionario de nomes para clientes

O usuario definiu este dicionario:

```text
MENU.ZIP = Retaguarda
ECF_WS.ZIP = PDV ou Caixas
SERVIDOR.ZIP = VPN ou Server NFE
WGSYNC.ZIP = Weber Tributario
WGCRESCEVENDAS.ZIP = Clube de Vendas da Loja
WGLCTONOTA.ZIP = Entrada de Notas Recebe Facil
```

## Prompts planejados

Foram planejados dois prompts para gerar informativo:

1. Prompt interno Weber:
   - para tecnicos, suporte, desenvolvimento e gerencia;
   - pode usar termos tecnicos;
   - pode usar emojis;
   - pode ter tom mais dinamico/descolado;
   - somente producao confirmada entra no card.

2. Prompt para clientes:
   - linguagem cuidadosa;
   - sem nomes internos como ZIP, DLL ou EXE;
   - usar nomes amigaveis do dicionario;
   - nao mencionar beta;
   - nao mencionar itens sem confirmacao de producao;
   - somente producao confirmada entra no card.

## Possivel erro de entendimento

O usuario informou que entendeu a demanda de forma errada e quer recomecar com um chat novo.

Portanto, no novo chat, antes de continuar gerando prompts ou comunicados, confirmar:

```text
Qual e exatamente a nova interpretacao da demanda?
O Weber Patches sera uma demanda tecnica interna, um informativo visual, um processo de release, ou outra coisa?
Quem sera o publico principal?
O material deve ser para gerencia, suporte, desenvolvimento ou clientes?
```

## Recomendacao para novo chat

Mensagem sugerida para abrir o novo chat:

```text
Estou retomando o projeto Weber Patches.

A interpretacao anterior pode ter ficado errada. Quero redefinir a demanda a partir deste contexto.

Use o arquivo `contexto-para-novo-chat-weber-patches.md` como resumo do que foi feito ate agora.

Antes de criar qualquer novo prompt ou comunicado, me ajude a esclarecer:
- qual e o objetivo real da demanda;
- qual material devo entregar internamente;
- quais dados do Portal Gerencial realmente entram;
- como devemos tratar beta, producao confirmada e pendencias.
```

