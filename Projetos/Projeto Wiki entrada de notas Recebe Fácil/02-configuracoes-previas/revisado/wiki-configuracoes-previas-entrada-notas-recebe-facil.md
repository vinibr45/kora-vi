# Configurações Prévias da Entrada de Notas Recebe Fácil

Configurações iniciais que devem ser revisadas antes de iniciar a entrada de notas pelo módulo **Entrada de Notas Recebe Fácil**.

## Índice

1. Objetivo
2. Público-alvo
3. Antes de começar
4. Informações necessárias
5. Procedimento operacional
6. Resultado esperado
7. Checklist de conferência
8. Possíveis dúvidas

## Objetivo

Este tutorial orienta a configuração dos principais pontos exigidos no primeiro acesso à Entrada de Notas Recebe Fácil.

Ao abrir o módulo, o sistema pode apresentar avisos indicando pendências de configuração financeira, plano financeiro sugerido e usuário master. Essas mensagens ajudam a identificar o que precisa ser ajustado antes de iniciar a entrada das notas.

Neste procedimento, serão revisadas as configurações de:

- plano financeiro padrão da empresa;
- conta financeira;
- centro de custo;
- percentual de distribuição;
- configurações financeiras da empresa;
- parametrização do módulo;
- permissões do usuário master e módulos de análise.

## Público-alvo

Este material foi criado para usuários finais, suporte, implantação e equipe técnica que precisam preparar o ambiente para utilizar a Entrada de Notas Recebe Fácil.

## Antes de começar

Antes de realizar as configurações, confirme se:

- o usuário tem permissão para acessar o módulo **Controle das entradas**;
- o usuário tem acesso ao menu `Configurações`;
- a empresa já utiliza o **Financeiro Novo/Gestão Financeira**, que será a base financeira desta Wiki;
- o fluxo será utilizado considerando compatibilidade com **Estoque Antigo**;
- existe uma conta financeira adequada para entrada de notas;
- existe um centro de custo definido para a operação;
- a regra financeira foi validada com o responsável administrativo, financeiro ou contábil.

> **Atenção:** os prints desta etapa podem conter dados de loja, CNPJ, usuário, valores ou informações internas. Antes de publicar para cliente, revise se as imagens precisam ser recortadas, borradas ou substituídas por imagens de uma base de treinamento.

## Informações necessárias

- Caminho para abrir o módulo **Controle das entradas**.
- Acesso ao menu `Configurações`.
- Conta financeira que será usada na entrada de notas.
- Centro de custo que será vinculado à entrada.
- Percentual de distribuição financeira.
- Meio de pagamento padrão.
- Espécie de documento padrão.
- Usuário que receberá a permissão de usuário master, quando aplicável.

## Procedimento operacional

### 01. Valide o aviso de configuração financeira pendente

Ao acessar a Entrada de Notas Recebe Fácil, o sistema pode exibir a mensagem **Configuração financeira pendente**.

![Aviso de configuração financeira pendente](<../../Imagens/Configurações prévias da Entrada de Notas/print_1 _aviso1.png>)

**Legenda:** aviso informando que ainda é necessário configurar o meio de pagamento e a espécie de documento usados no financeiro das notas de entrada.

**Mensagem exibida:**

```text
Para utilizar a entrada de nota, selecione ou configure o meio de pagamento e a espécie de documento que serão usados no financeiro das notas de entrada.

No Controle de Entradas, acesse:
Fornecedor: Configurações > Configurações Financeiras > Plano Financeiro padrão e outras configurações por fornecedor.
Loja: Configurações > Configurações Financeiras > Configurações financeiras da empresa.
```

Essa mensagem indica que o sistema ainda precisa saber quais configurações financeiras serão usadas na entrada das notas. Depois de ler o aviso, clique em **OK** e siga para as configurações financeiras.

### 02. Valide o aviso de plano financeiro sugerido pendente

O sistema também pode exibir o aviso **Plano financeiro sugerido pendente**.

![Aviso de plano financeiro sugerido pendente](<../../Imagens/Configurações prévias da Entrada de Notas/print_2 _aviso2.png>)

**Legenda:** aviso informando que o plano financeiro sugerido da operação `ENTRADA_NOTAS` ainda precisa ser configurado.

**Mensagem exibida:**

```text
Para utilizar a entrada de nota, configure o plano financeiro sugerido para a operação ENTRADA_NOTAS.

No Controle de Entradas, acesse:
Configurações > Configurações Financeiras > Plano Financeiro padrão da empresa.
```

Esse aviso indica que a operação de entrada de notas precisa de uma sugestão de plano financeiro padrão. Clique em **OK** e siga para a configuração do plano financeiro padrão da empresa.

### 03. Valide o aviso de usuário master

Outro aviso possível é a ausência de usuário master configurado para a loja logada.

![Aviso de usuário master não configurado](<../../Imagens/Configurações prévias da Entrada de Notas/print_3 _aviso3.png>)

**Legenda:** aviso informando que nenhum usuário master foi configurado para a loja.

**Mensagem exibida:**

```text
Nenhum Usuário Master foi configurado para a loja logada.

Configure ao menos um usuário com a permissão 'Usuário Master' para liberar a administração completa das permissões.

Para liberar o Usuário Master, no Dashboard Inicial acesse Configurações > Permissões.
```

Essa permissão é importante porque libera a administração completa das permissões do módulo. Depois de ler a mensagem, clique em **OK**. A configuração da permissão será feita mais adiante neste tutorial.

### 04. Acesse o plano financeiro padrão da empresa

No painel do **Controle das entradas**, acesse:

```text
Configurações > Configurações Financeiras > Plano Financeiro padrão da empresa
```

![Caminho para plano financeiro padrão da empresa](<../../Imagens/Configurações prévias da Entrada de Notas/print_4 _caminho1.png>)

**Legenda:** caminho para acessar o plano financeiro padrão da empresa.

Essa tela será usada para informar a conta financeira, o centro de custo e o percentual que serão sugeridos para a operação de entrada de notas.

### 05. Selecione a conta financeira

Na tela **Sugestão de Plano Financeiro - Configuração**, localize a seção **Entrada de notas (CP)**.

No campo **Conta Financeira**, clique em **Selecionar**.

![Seleção da conta financeira](<../../Imagens/Configurações prévias da Entrada de Notas/print_5 _configuracao_CONTA FINANCEIRA.png>)

**Legenda:** seleção da conta financeira que será utilizada para a entrada de notas.

Na janela de ajuda, escolha a conta financeira correspondente à regra da empresa. No exemplo do print, foi selecionada uma conta relacionada a despesas e produtos para revenda.

> **Importante:** a conta financeira exibida no print é apenas um exemplo da base utilizada. Em ambiente real, selecione a conta definida pela empresa ou pelo responsável financeiro.

### 06. Selecione o centro de custo

Depois de selecionar a conta financeira, clique em **Selecionar** no campo **Centro de Custo**.

![Seleção do centro de custo](<../../Imagens/Configurações prévias da Entrada de Notas/print_6 _configuracao_CENTRO DE CUSTO.png>)

**Legenda:** seleção do centro de custo que será vinculado à operação de entrada de notas.

Na janela de ajuda, escolha o centro de custo adequado. No exemplo, foi selecionado o centro de custo **Loja**.

### 07. Informe o percentual de distribuição

Com a conta financeira e o centro de custo preenchidos, informe o percentual de distribuição.

![Percentual de distribuição financeira](<../../Imagens/Configurações prévias da Entrada de Notas/print_7 _configuracao_PLANO FINANCEIRO.png>)

**Legenda:** preenchimento do percentual de distribuição para a sugestão do plano financeiro.

No exemplo, foi informado **100%**, indicando que todo o valor da operação será direcionado para uma única combinação de conta financeira e centro de custo.

Se a empresa utilizar mais de uma conta financeira ou mais de um centro de custo, a distribuição pode ser dividida. Nesse caso, a soma dos percentuais deve fechar exatamente **100%**.

Depois de preencher o percentual, clique em **Incluir**.

### 08. Salve a configuração do plano financeiro

Após incluir a combinação, confirme se a operação `ENTRADA_NOTAS` aparece na grade com a conta financeira, o centro de custo e o percentual correto.

![Gravação do plano financeiro padrão](<../../Imagens/Configurações prévias da Entrada de Notas/print_8 _configuracao_GRAVA_PLANO_FINANCEIRO.png>)

**Legenda:** gravação da sugestão de plano financeiro da operação `ENTRADA_NOTAS`.

Depois de conferir as informações, clique em **Salvar configuração**.

### 09. Acesse as configurações financeiras da empresa

Depois de configurar o plano financeiro padrão, retorne ao menu:

```text
Configurações > Configurações Financeiras > Configurações financeiras da empresa
```

![Caminho para configurações financeiras da empresa](<../../Imagens/Configurações prévias da Entrada de Notas/print_9 _caminho2.png>)

**Legenda:** caminho para acessar as configurações financeiras da empresa.

Essa tela define informações financeiras usadas pela loja, incluindo configurações de entrada de notas.

### 10. Configure a espécie de documento e o meio de pagamento

Na tela **Configurações Financeiras da empresa**, localize a seção **Entrada de notas**.

![Configurações financeiras da empresa](<../../Imagens/Configurações prévias da Entrada de Notas/print_10 _configuracao_CONTA_CORRENTE E MEIO DE PAGAMENTO..png>)

**Legenda:** configuração da espécie de documento padrão e do meio de pagamento padrão para entrada de notas.

Preencha:

- **Espécie do documento padrão**;
- **Meio de pagamento padrão**.

No exemplo do print, a espécie de documento foi configurada como **DM - Duplicata Mercantil** e o meio de pagamento como **Boleto**.

Depois de revisar as informações, clique em **Salvar**.

> **Atenção:** este print contém identificação de empresa e CNPJ. Antes de publicar para cliente, revise a imagem.

### 11. Acesse a parametrização do módulo

Após configurar os dados financeiros, acesse:

```text
Configurações > Parametrização do módulo
```

![Caminho para parametrização do módulo](<../../Imagens/Configurações prévias da Entrada de Notas/print_11 _caminho3.png>)

**Legenda:** caminho para abrir a parametrização do módulo de entrada de notas.

Essa tela define comportamentos importantes da Entrada de Notas Recebe Fácil.

### 12. Revise os parâmetros do módulo

Na tela **Parametrização do módulo de entrada de notas**, revise os parâmetros apresentados.

![Parametrização do módulo de entrada de notas](<../../Imagens/Configurações prévias da Entrada de Notas/print_12 _coinfiguracao_PARAMETROS_DO_MODULO.png>)

**Legenda:** parametrização do módulo, incluindo liberação prévia, atualização de custo do produto da entrada e atualização de custo dos produtos associados.

No exemplo do print, aparecem parâmetros como:

- **Exigir liberação prévia para entrada automática**;
- **Atualizar o custo do produto após a entrada**;
- **Atualizar o custo dos produtos associados à entrada**.

Quando a opção de liberação prévia estiver marcada, o sistema somente realizará a entrada automática das notas previamente liberadas. A liberação pode ser feita pelo Weber Mobile.

Quando as opções de custo estiverem configuradas como **Sim**, o sistema poderá atualizar custos conforme a regra descrita na própria tela.

Revise as opções de acordo com a regra da empresa e clique em **Salvar**.

> **Precisa confirmar:** se a empresa deve usar todos os parâmetros marcados como **Sim** em produção ou se essa configuração é apenas o exemplo da base de treinamento.

### 13. Acesse as permissões

Depois de revisar a parametrização, acesse:

```text
Configurações > Permissões
```

![Caminho para permissões](<../../Imagens/Configurações prévias da Entrada de Notas/print_13 _caminho4.png>)

**Legenda:** caminho para abrir a tela de permissões da Entrada de Notas Recebe Fácil.

Essa etapa é necessária para tratar o aviso de usuário master e liberar os acessos necessários ao módulo.

### 14. Configure o usuário master e as permissões de análise

Na tela **Permissões de Entrada de Notas e Análises**, selecione a loja e o usuário que receberá as permissões.

Depois, clique em **Carregar**.

![Configuração de permissões do usuário master](<../../Imagens/Configurações prévias da Entrada de Notas/print_14 _configuracao_permissao_usuario_master.png>)

**Legenda:** configuração do usuário master e das permissões de análise.

Na seção **Funcionalidades de entrada e configurações**, marque a permissão **Usuário Master** quando esse usuário for responsável por administrar as permissões do módulo.

A própria tela informa que a permissão **Usuário Master** concede acesso às demais ferramentas/permissões e também autoriza conceder permissões aos demais usuários.

Na seção **Módulos de análise**, marque os módulos que o usuário poderá consultar, como:

- análise de CFOPs das entradas;
- associações de produtos por fornecedor;
- estatísticas de fornecedores nas entradas;
- ranking de produtos comprados;
- variações de preço de compra.

Depois de revisar as permissões, clique em **Salvar**.

> **Atenção:** conceda a permissão de usuário master somente para usuários autorizados, pois ela permite administrar permissões de outros usuários.

## Resultado esperado

Ao concluir este procedimento, o ambiente estará com as configurações prévias necessárias para iniciar o uso da Entrada de Notas Recebe Fácil.

O sistema deve estar com:

- plano financeiro padrão configurado para a operação `ENTRADA_NOTAS`;
- conta financeira definida;
- centro de custo definido;
- percentual de distribuição fechando 100%;
- espécie de documento padrão configurada;
- meio de pagamento padrão configurado;
- parametrização do módulo revisada;
- usuário master configurado, quando necessário;
- permissões de análise liberadas para o usuário adequado.

## Checklist de conferência

Antes de considerar a etapa concluída, confirme se:

- os avisos iniciais foram lidos e entendidos;
- o plano financeiro padrão da empresa foi acessado;
- a conta financeira foi selecionada;
- o centro de custo foi selecionado;
- o percentual de distribuição foi informado;
- a sugestão da operação `ENTRADA_NOTAS` foi incluída;
- a configuração do plano financeiro foi salva;
- a espécie de documento padrão foi configurada;
- o meio de pagamento padrão foi configurado;
- as configurações financeiras da empresa foram salvas;
- a parametrização do módulo foi revisada e salva;
- o usuário master foi configurado quando o sistema exigiu essa permissão;
- os módulos de análise necessários foram liberados;
- os prints foram revisados para evitar exposição de dados sensíveis.

## Possíveis dúvidas

### O aviso de configuração financeira sempre aparece?

Ele pode aparecer quando o sistema identifica que ainda existem configurações financeiras pendentes para a entrada de notas. Após configurar os campos necessários, o aviso tende a deixar de ser exibido.

### O plano financeiro precisa fechar 100%?

Sim. Quando houver distribuição entre conta financeira e centro de custo, a soma dos percentuais deve fechar 100%.

### Posso usar outra conta financeira ou outro centro de custo?

Sim. Os exemplos dos prints servem apenas como referência visual. Em ambiente real, use a conta financeira e o centro de custo definidos pela empresa.

### Todo usuário deve ser usuário master?

Não. A permissão de usuário master deve ser liberada apenas para usuários autorizados a administrar permissões. Para os demais usuários, libere somente as permissões necessárias ao trabalho deles.

### A liberação prévia pelo Weber Mobile é obrigatória?

Depende da parametrização escolhida pela empresa. Quando a opção **Exigir liberação prévia para entrada automática** estiver marcada, somente notas previamente liberadas devem seguir para entrada automática.
