# Preparação de Ambiente para Utilização da Entrada de Notas Recebe Fácil

Configurações iniciais necessárias para liberar o uso da **Entrada de Notas Recebe Fácil** no ambiente do cliente.

Este procedimento orienta o usuário na preparação do sistema antes de iniciar a entrada das notas. A sequência abaixo acompanha a ordem dos prints e apresenta os principais pontos de configuração, validação e conferência.

## Regra de preparação do ambiente

Antes de utilizar a Entrada de Notas Recebe Fácil, é necessário validar algumas configurações da empresa e do módulo.

Essas configurações evitam bloqueios no primeiro acesso e garantem que o sistema saiba como tratar informações importantes da nota, como financeiro, plano financeiro padrão, centro de custo e parâmetros operacionais do módulo.

Além disso, existem dois requisitos obrigatórios para utilização do fluxo:

- o cliente precisa estar com o **Financeiro Novo**, também chamado de **Gestão Financeira**, ativo;
- o cliente precisa estar com o **Estoque Novo** habilitado, com a flag de Estoque Novo ativa no **Portal Gerencial**.

Caso esses requisitos não estejam atendidos, o cliente não deve seguir com a utilização do fluxo baseado no Estoque Novo.

## Objetivo e pré-requisitos

O objetivo deste material é preparar o ambiente para que o cliente consiga iniciar o uso da Entrada de Notas Recebe Fácil com segurança.

Antes de começar, confirme se:

- o usuário possui permissão para acessar as configurações da empresa;
- o ambiente utilizado é uma base de treinamento, homologação ou base preparada para demonstração;
- o cliente já utiliza o Financeiro Novo/Gestão Financeira;
- a flag de Estoque Novo está habilitada no Portal Gerencial;
- o Estoque Novo pode ser habilitado para a empresa;
- existe conta financeira cadastrada para uso no plano financeiro padrão;
- existe centro de custo cadastrado para vincular à configuração financeira;
- as regras financeiras foram validadas com o responsável administrativo, financeiro ou contábil;
- o usuário possui acesso às configurações do módulo.

> **Atenção:** para criação de Wiki, prints e vídeos, utilize preferencialmente uma base preparada para treinamento. Evite expor dados reais de clientes, fornecedores, valores sensíveis, documentos fiscais ou informações internas.

## Informações necessárias

- Acesso ao menu `Ferramentas > Empresa`.
- Permissão para alterar configurações da empresa.
- Financeiro Novo/Gestão Financeira ativo para o cliente.
- Flag de Estoque Novo habilitada no Portal Gerencial.
- Conta financeira previamente cadastrada.
- Centro de custo previamente cadastrado.
- Definição do percentual de distribuição financeira.
- Acesso ao menu `Configurações > Parametrização do Módulo`.
- Validação das mensagens exibidas no primeiro acesso ao módulo.

## Procedimento operacional

### 01. Acesse as configurações da empresa

No menu principal do sistema, acesse:

```text
Ferramentas > Empresa
```

Essa tela concentra configurações importantes da empresa e deve ser acessada antes de iniciar a preparação do módulo.

[imagem-01]

**Legenda:** acesso ao cadastro da empresa pelo menu `Ferramentas > Empresa`.

### 02. Habilite o Estoque Novo

Na tela de configurações da empresa, localize a opção relacionada ao **Estoque Novo** e habilite esse recurso.

Essa configuração é necessária para que o fluxo da Entrada de Notas Recebe Fácil funcione corretamente, pois o módulo depende das rotinas vinculadas ao novo modelo de estoque.

[imagem-02]

**Legenda:** habilitação da opção **Estoque Novo** nas configurações da empresa.

### 03. Abra o módulo e valide o primeiro aviso

Ao acessar a Entrada de Notas Recebe Fácil pela primeira vez, o sistema pode exibir avisos indicando configurações pendentes.

Leia a mensagem apresentada e utilize o conteúdo do aviso como orientação para concluir a configuração necessária.

[imagem-03]

**Legenda:** aviso de configuração financeira pendente.

**Texto do aviso:**

```text
Para utilizar a entrada de nota, selecione ou configure o meio de pagamento e a espécie de documento que serão usados no financeiro das notas de entrada.

No Controle de Entradas, acesse:
Fornecedor: Configurações > Configurações Financeiras > Plano Financeiro padrão e outras configurações por fornecedor.
Loja: Configurações > Configurações Financeiras > Configurações financeiras da empresa.
```

Esse aviso indica que a empresa ainda precisa ter as configurações financeiras definidas para que o processo de entrada consiga prosseguir corretamente.

### 04. Valide o aviso de plano financeiro sugerido

O sistema também pode apresentar um aviso informando que o plano financeiro sugerido ainda não foi configurado.

[imagem-04]

**Legenda:** aviso de plano financeiro sugerido pendente.

**Texto do aviso:**

```text
Para utilizar a entrada de nota, configure o plano financeiro sugerido para a operação ENTRADA_NOTAS.

No Controle de Entradas, acesse:
Configurações > Configurações Financeiras > Plano Financeiro padrão da empresa.
```

Esse aviso reforça que o plano financeiro padrão deve estar configurado antes de iniciar a utilização do módulo.

### 05. Valide o aviso de usuário master

Outro aviso possível é a ausência de um usuário master configurado para a loja logada.

[imagem-05]

**Legenda:** aviso informando que nenhum usuário master foi configurado para a loja.

**Texto do aviso:**

```text
Nenhum Usuário Master foi configurado para a loja logada.

Configure ao menos um usuário com a permissão 'Usuário Master' para liberar a administração completa das permissões.

Para liberar o Usuário Master, no Dashboard Inicial acesse Configurações > Permissões.
```

Esse aviso está relacionado à administração de permissões. Caso ele seja exibido, será necessário configurar ao menos um usuário master para permitir a gestão completa das permissões do módulo.

### 06. Acesse as configurações financeiras

Depois de validar os avisos iniciais, acesse as configurações financeiras da empresa.

O ideal é iniciar por essa etapa porque a entrada das notas pode gerar reflexos financeiros e gerenciais. Por isso, antes de lançar notas, o sistema precisa saber qual plano financeiro, conta financeira e centro de custo serão utilizados.

[imagem-06]

**Legenda:** acesso à área de configurações financeiras da empresa.

[imagem-07]

**Legenda:** campos financeiros que devem ser configurados antes de iniciar o uso do módulo.

### 07. Informe a configuração financeira da empresa

Preencha as configurações financeiras conforme a regra definida para o cliente.

Neste exemplo, será utilizada uma configuração previamente preparada na base de treinamento. Em ambiente real, os dados devem seguir a orientação da empresa, da contabilidade ou do responsável financeiro.

[imagem-08]

**Legenda:** exemplo de configuração financeira utilizada na base de treinamento.

### 08. Configure o plano financeiro padrão

Agora configure o **plano financeiro padrão** da empresa.

O plano financeiro padrão define como os valores relacionados às notas serão classificados no financeiro. Essa configuração ajuda a manter os lançamentos organizados e facilita a conferência posterior.

[imagem-09]

**Legenda:** configuração do plano financeiro padrão para a operação de entrada de notas.

### 09. Selecione a conta financeira

Selecione uma conta financeira previamente cadastrada.

Caso a conta financeira ainda não exista, será necessário realizar o cadastro antes de concluir esta etapa.

[imagem-10]

**Legenda:** seleção da conta financeira que será utilizada no plano financeiro padrão.

[imagem-11]

**Legenda:** conta financeira selecionada na configuração.

Material relacionado:

[Cadastro de Plano Financeiro](https://www.servicoweber.com.br/public/public_wiki_article.php?A=F62C559EE3664177A7411C193516064C&pidWeber=0&pidUsua=0&pnomeUsua=&showOptions=&fromAPI=true&sourceInternalWiki=true)

### 10. Selecione o centro de custo

Depois de selecionar a conta financeira, escolha o **centro de custo** que será utilizado no plano financeiro.

O centro de custo permite classificar gerencialmente os valores movimentados pela entrada das notas. Essa informação é importante para relatórios, controles internos e análises financeiras.

[imagem-12]

**Legenda:** seleção do centro de custo utilizado na configuração financeira.

Neste tutorial, foi utilizado um centro de custo previamente cadastrado.

Caso seja necessário cadastrar um novo centro de custo, consulte o material abaixo:

[Cadastro de Centro de Custos](https://www.servicoweber.com.br/public/public_wiki_article.php?A=F4DDAC48BF68475986277C5537FC27F5&pidWeber=0&pidUsua=0&pnomeUsua=&showOptions=&fromAPI=true&sourceInternalWiki=true)

### 11. Informe o percentual de distribuição

Informe o percentual que será aplicado à combinação de conta financeira e centro de custo.

No exemplo utilizado neste tutorial, foi informado o percentual de **100%**, indicando que todo o valor será direcionado para uma única configuração.

Quando a empresa trabalhar com mais de uma conta financeira ou mais de um centro de custo, é possível informar percentuais diferentes. Nesse caso, a soma das configurações deve fechar exatamente **100%**.

[imagem-13]

**Legenda:** percentual de distribuição financeira informado para compor o total da configuração.

> **Observação técnica:** se o percentual total ficar abaixo ou acima de 100%, a configuração pode ficar incompleta ou inconsistente. Antes de salvar, confira se a distribuição financeira está fechando corretamente.

### 12. Salve as configurações financeiras

Depois de preencher a conta financeira, o centro de custo e o percentual, revise as informações.

Se estiver tudo correto, clique em:

```text
Salvar Configurações
```

[imagem-14]

**Legenda:** salvamento das configurações financeiras da empresa.

### 13. Acesse a parametrização do módulo

Com as configurações financeiras definidas, acesse a parametrização específica da Entrada de Notas Recebe Fácil.

[imagem-15]

**Legenda:** acesso às configurações do módulo.

No menu do módulo, acesse:

```text
Configurações > Parametrização do Módulo
```

[imagem-16]

**Legenda:** caminho para abrir a tela de parametrização do módulo.

### 14. Revise os parâmetros relacionados ao custo e à desmontagem

Na tela de parametrização, revise as opções apresentadas pelo sistema.

Os parâmetros exibidos definem comportamentos importantes durante a entrada da nota, como atualização de custo dos produtos associados e tratamento de desmontagem automática.

[imagem-17]

**Legenda:** parâmetros de custo dos produtos associados e desmontagem de produtos.

**Texto exibido na tela:**

```text
Custo dos produtos associados

Atualizar o custo dos produtos associados à entrada

Quando configurado como 'Sim', o custo da loja da entrada será atualizado para os produto com código preço igual ao código do produto que esta sendo movimentado, alteração reflete para todas tabelas de preço.

Situação selecionada: Não (configuração ainda não salva)

Desmontagem de produtos

Ignorar desmontagem automática na entrada

Quando configurado como 'Sim', a entrada não realiza desmontagem automática, mesmo que o produto possua fórmula ativa. Use esta opção quando a desmontagem for realizada manualmente em outro momento.

Situação selecionada: Não
```

### 15. Grave a parametrização

Depois de selecionar as opções adequadas para a empresa, clique em:

```text
Gravar
```

Na base de treinamento, será utilizada a configuração demonstrada no exemplo.

[imagem-18]

**Legenda:** exemplo de parametrização final antes da gravação.

## Resultado esperado

Ao concluir este procedimento, o ambiente estará preparado com as configurações iniciais necessárias para utilização da Entrada de Notas Recebe Fácil.

A partir desse ponto, o usuário poderá seguir para os próximos tutoriais, como configurações prévias, permissões, notas disponíveis, entrada assistida, associação de produtos, cadastro por GTIN, conferência e auditoria das notas lançadas.

## Checklist de conferência

Antes de considerar esta etapa concluída, confirme se:

- o Estoque Novo foi habilitado;
- os avisos iniciais foram lidos e tratados;
- o plano financeiro padrão foi configurado;
- a conta financeira foi selecionada;
- o centro de custo foi informado;
- o percentual de distribuição financeira totaliza 100%;
- as configurações financeiras foram salvas;
- a parametrização do módulo foi revisada;
- a parametrização do módulo foi gravada;
- existe usuário master configurado quando o sistema exigir essa permissão.

## Possíveis dúvidas

### Posso usar uma conta financeira diferente da apresentada no exemplo?

Sim. A conta financeira deve seguir a regra definida pela empresa. O exemplo serve apenas como referência para demonstrar o preenchimento.

### É obrigatório configurar o plano financeiro padrão?

Sim. Se o plano financeiro padrão estiver pendente, o sistema poderá exibir aviso e impedir ou limitar a continuidade do processo.

### É obrigatório informar centro de custo?

Neste fluxo, o centro de custo faz parte da configuração financeira demonstrada. Caso a empresa tenha uma regra específica, valide com o responsável financeiro ou contábil antes de finalizar.

### Posso distribuir o percentual entre mais de uma conta ou centro de custo?

Sim. A distribuição pode ser feita entre mais de uma combinação, desde que a soma final seja 100%.

### O que fazer se o sistema continuar exibindo avisos de configuração pendente?

Revise as configurações financeiras, o plano financeiro padrão, a parametrização do módulo e as permissões. Se todas as informações estiverem preenchidas corretamente e o aviso persistir, acione o suporte ou o responsável técnico para avaliar a configuração da base.

## Próximo passo

Depois de preparar o ambiente, siga para o tutorial de configurações prévias da Entrada de Notas Recebe Fácil. Nele devem ser detalhados os ajustes necessários antes de iniciar efetivamente a entrada das notas.
