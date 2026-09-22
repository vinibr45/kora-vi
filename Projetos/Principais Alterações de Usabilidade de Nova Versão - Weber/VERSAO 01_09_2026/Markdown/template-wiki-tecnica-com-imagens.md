# Template de wiki de versao com imagens

Use este modelo para transformar uma alteracao confirmada em producao em um artigo da **Wiki de versao Weber Sistemas**, seguindo o padrao do arquivo:

```text
Wiki _De_versao_ Weber Sistemas.html
```

Este formato nao e um comunicado curto. Ele e uma base operacional: o tecnico deve conseguir ler, entender o impacto, ver as imagens e explicar a mudanca com seguranca.

## Padrao oficial da pagina

A wiki usa esta organizacao:

- Titulo do artigo: `Principais Mudancas - Versao DD.MM.AAAA`
- Categoria: `Infraestrutura e TI > Atualizacoes > Atualizacao de Versoes - Novidades`
- Aba 1: `Artigo geral`
- Aba 2: `Artigo tecnico`

No arquivo de referencia, o conteudo principal esta na aba **Artigo geral**. A aba **Artigo tecnico** existe, mas pode ficar vazia ou receber rastreabilidade tecnica quando necessario.

## Padrao editorial observado

O artigo geral segue este ritmo:

1. Titulo da mudanca com destaque visual.
2. Secao `O que mudou?`.
3. Explicacao objetiva do novo comportamento.
4. Lista de campos, opcoes, regras ou pontos afetados.
5. Imagem logo apos a explicacao inicial.
6. Secao de acao pratica, por exemplo `Como liberar...`, `Como utilizar...`, `Como validar...`.
7. Secao `Passo a passo`.
8. Prints entre os passos, especialmente antes/depois de uma confirmacao ou validacao.
9. Secao de alerta com `IMPORTANTE`.
10. Secoes explicativas adicionais quando o tecnico precisa contextualizar o cliente.
11. Exemplos concretos quando existe risco de interpretacao.
12. Fechamento em bloco de resumo quando a explicacao for longa.

O texto deve ser minucioso quando a mudanca afeta atendimento, comportamento fiscal, cadastro, validacao, permissao, mensagem, rotina operacional ou decisao do cliente.

## Regra de entrada

Antes de criar o artigo, confirme:

- A mudanca esta confirmada em producao.
- O aplicativo, modulo ou rotina foi identificado.
- A mudanca afeta comportamento, tela, rotina, validacao, processo ou atendimento ao cliente.
- Itens sem confirmacao de producao ficam fora da wiki principal.

## Estrutura do artigo geral

```text
Titulo do artigo na wiki:
Principais Mudancas - Versao DD.MM.AAAA

Titulo da mudanca:
[Nome amigavel da mudanca] - [Modulo ou rotina]

O que mudou?
Descrever o comportamento novo, em linguagem clara.

Pontos afetados:
Listar campos, telas, abas, botoes, regras ou mensagens impactadas.

[Imagem 1 - contexto da tela]

Como usar / liberar / validar / orientar?
Explicar a acao pratica que o tecnico deve orientar.

Passo a passo:
1. Caminho da tela.
2. Acao que o usuario deve executar.
3. Resultado esperado.
4. Cuidado ou mensagem que pode aparecer.

[Imagem 2 - acao principal]
[Imagem 3 - mensagem ou validacao]
[Imagem 4 - resultado final]

IMPORTANTE:
Explicar o cuidado operacional mais importante.

Contexto adicional:
Explicar o motivo da mudanca quando isso ajuda o tecnico a orientar o cliente.

Exemplos:
Usar exemplos concretos quando houver risco de interpretacao errada.

Resumo:
Fechar com um paragrafo ou bloco de resumo.
```

## Estrutura do artigo tecnico

Use a aba `Artigo tecnico` para informacao interna que nao precisa aparecer na explicacao geral, como rastreabilidade e confirmacao de producao.

```text
Origem da mudanca:
- Aplicativo interno:
- Nome amigavel:
- Data da alteracao:
- Data de producao:
- Fonte da confirmacao:
- Status:

Descricao original:
[colar descricao original]

Observacoes internas:
- Dependencias:
- Modulos relacionados:
- Cuidados de suporte:
- Pontos que precisam de validacao:

Imagens necessarias:
- Print 1: contexto da tela.
- Print 2: campo, botao ou flag alterada.
- Print 3: mensagem, validacao ou resultado esperado.
- Print 4 opcional: exemplo de antes/depois, quando existir.
```

## Prompt base para gerar artigo da wiki

```text
Voce e um redator tecnico da Weber Sistemas de Gestao.

Crie um artigo de wiki para orientar tecnicos a explicar para clientes uma mudanca que entrou na nova versao de producao.

Publico do artigo:
- Tecnicos, suporte e implantacao.
- O texto deve ajudar o tecnico a explicar a mudanca para o cliente.
- Pode conter detalhes operacionais, cuidados, alertas e passo a passo.
- Nao trate como marketing.
- Nao trate como patch note resumido.

Padrao desejado:
- Seguir o arquivo "Wiki _De_versao_ Weber Sistemas.html".
- O artigo fica na aba "Artigo geral".
- Se houver rastreabilidade, coloque na aba "Artigo tecnico", nao no corpo principal.
- Ser minucioso quando a mudanca exigir orientacao ao cliente.
- Explicar o que mudou, onde aparece, como usar e quais cuidados tomar.
- Usar linguagem clara, mas sem esconder informacao tecnica importante.
- Nao mencionar beta.
- Nao citar nomes internos de arquivos ZIP no texto principal.
- Nao transformar em lista curta de patch notes.

Dados da mudanca:
- Nome amigavel:
- Modulo/rotina:
- Aplicativo interno:
- Data da alteracao:
- Data de producao:
- Descricao original:
- Evidencias ou prints disponiveis:
- Publico afetado:
- Risco de atendimento:

Gere o artigo com esta estrutura:
1. Titulo da mudanca
2. O que mudou?
3. Pontos afetados
4. Imagem inicial recomendada
5. Como usar / liberar / validar / orientar
6. Passo a passo
7. Imagens no meio do passo a passo
8. IMPORTANTE
9. Contexto adicional
10. Exemplos, se fizer sentido
11. Resumo
12. Artigo tecnico separado, se houver rastreabilidade
```

## Prompt para transformar alteracao tecnica em linguagem de atendimento

```text
Reescreva a alteracao abaixo para uma wiki de suporte.

Objetivo:
O tecnico precisa entender a mudanca e conseguir explicar ao cliente em atendimento.

Regras:
- Preserve o significado tecnico.
- Explique o impacto pratico.
- Identifique termos que precisam virar nomes amigaveis.
- Separe "o que mudou" de "como explicar ao cliente".
- Aponte quais imagens ou prints devem ser capturados.
- Nao invente comportamento que nao esteja na descricao.
- Se faltar contexto, marque como "precisa confirmar".

Alteracao original:
[colar aqui]

Contexto adicional:
[colar aqui]
```

## Prompt para planejar imagens do artigo

```text
Com base nesta mudanca, liste quais imagens devem ser capturadas para a wiki tecnica.

Para cada imagem, informe:
- Nome sugerido do arquivo.
- Tela ou rotina.
- O que precisa aparecer no print.
- Qual parte destacar com caixa, seta ou marca visual.
- Legenda curta.
- Por que essa imagem ajuda o tecnico a explicar ao cliente.

Mudanca:
[colar aqui]

Artigo ou rascunho:
[colar aqui]
```

## Prompt para revisar se o artigo segue o padrao

```text
Revise este artigo de wiki tecnica.

Verifique:
- Se esta claro para um tecnico explicar ao cliente.
- Se o texto esta minucioso o suficiente.
- Se o artigo separa comportamento antigo, comportamento novo e orientacao.
- Se existem promessas indevidas ou inferencias nao comprovadas.
- Se faltam imagens.
- Se a rastreabilidade da mudanca esta preservada.
- Se ha termos internos que deveriam virar nomes amigaveis.
- Se algum item depende de confirmacao de producao.

Retorne:
1. Diagnostico geral.
2. Ajustes obrigatorios.
3. Ajustes recomendados.
4. Imagens faltantes.
5. Conferencia contra o padrao "Artigo geral" e "Artigo tecnico".
6. Versao revisada do texto, se necessario.

Artigo:
[colar aqui]
```

## Prompt para gerar artigo a partir do cruzamento beta x producao

```text
Crie um artigo de wiki tecnica para esta mudanca confirmada em producao.

Use a descricao tecnica como fonte principal, mas escreva para tecnicos explicarem ao cliente.

Nao mencione "beta" no texto principal.
Nao use o nome do ZIP como nome para cliente.
Use o nome amigavel do modulo quando existir.

Dicionario de nomes:
- MENU.ZIP = Retaguarda
- ECF_WS.ZIP = PDV ou Caixas
- SERVIDOR.ZIP = VPN ou Server NFE
- WGSYNC.ZIP = Weber Tributario
- WGCRESCEVENDAS.ZIP = Clube de Vendas da Loja
- WGLCTONOTA.ZIP = Entrada de Notas Recebe Facil

Dados:
- Aplicativo:
- Nome amigavel:
- Data da alteracao:
- Data de producao:
- Descricao original:
- Status de producao:

Estrutura obrigatoria:
- Titulo da mudanca
- O que mudou?
- Pontos afetados
- Como usar / liberar / validar / orientar
- Passo a passo
- Imagens recomendadas
- IMPORTANTE
- Contexto adicional
- Resumo
- Artigo tecnico separado
```

## Modelo de imagens por tipo de mudanca

### Campo bloqueado, liberado ou alterado

- Print da tela inteira para contexto.
- Print aproximado do campo.
- Print da mensagem de confirmacao ou alerta.
- Print do estado final depois da acao.

### Nova opcao de menu, botao ou atalho

- Print do caminho ate a rotina.
- Print da opcao destacada.
- Print da tela aberta pela opcao.
- Print do resultado esperado.

### Validacao nova

- Print do preenchimento que gera a validacao.
- Print da mensagem exibida.
- Print do preenchimento correto.
- Print da gravacao ou conclusao.

### Correcao de comportamento

- Print do fluxo atual funcionando.
- Print do ponto onde antes ocorria problema, se for possivel demonstrar.
- Print do resultado correto.

### Relatorio, grade ou ordenacao

- Print dos filtros.
- Print da grade ou relatorio.
- Print da coluna afetada.
- Print de exemplo comparavel, quando existir.

## Checklist antes de publicar artigo

- [ ] A mudanca tem producao confirmada.
- [ ] O titulo da pagina esta como `Principais Mudancas - Versao DD.MM.AAAA`.
- [ ] A categoria selecionada e `Atualizacao de Versoes - Novidades`.
- [ ] O conteudo principal esta na aba `Artigo geral`.
- [ ] A rastreabilidade, se usada, esta na aba `Artigo tecnico`.
- [ ] O titulo usa nome amigavel para tecnico e cliente.
- [ ] O artigo explica o que mudou.
- [ ] O artigo mostra onde a mudanca aparece.
- [ ] O artigo orienta como explicar ao cliente.
- [ ] O artigo lista prints necessarios.
- [ ] As imagens entram no meio do fluxo, nao apenas no final.
- [ ] O artigo nao promete comportamento nao comprovado.
- [ ] Termos internos ficaram no artigo tecnico, nao no artigo geral.
- [ ] Existe rastreabilidade da origem da mudanca.
- [ ] Itens pendentes ou proximos passos nao foram misturados como se ja estivessem em producao.
