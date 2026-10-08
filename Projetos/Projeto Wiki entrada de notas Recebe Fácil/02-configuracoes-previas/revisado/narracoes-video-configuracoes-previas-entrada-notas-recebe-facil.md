# Narrações do Vídeo - Configurações Prévias da Entrada de Notas Recebe Fácil

## 01

Neste vídeo, vamos configurar os principais ajustes prévios para utilizar a Entrada de Notas Recebe Fácil.

Essas configurações ajudam o sistema a identificar qual plano financeiro, conta financeira, centro de custo, meio de pagamento, espécie de documento e permissões serão usados durante a entrada das notas.

Também vamos revisar as mensagens que podem aparecer no primeiro acesso ao módulo e mostrar onde cada configuração deve ser realizada.

## 02

Ao acessar a Entrada de Notas Recebe Fácil, o sistema pode apresentar o aviso de configuração financeira pendente.

Essa mensagem informa que, para utilizar a entrada de nota, é necessário selecionar ou configurar o meio de pagamento e a espécie de documento que serão usados no financeiro das notas de entrada.

O próprio aviso indica dois caminhos importantes dentro do Controle de Entradas: as configurações financeiras por fornecedor e as configurações financeiras da loja.

Depois de ler a mensagem, clique em OK para continuar.

## 03

O próximo aviso pode indicar que o plano financeiro sugerido ainda está pendente.

Nesse caso, o sistema está informando que a operação ENTRADA_NOTAS precisa de um plano financeiro padrão configurado.

Essa configuração será usada como sugestão financeira para a entrada das notas, ajudando a classificar corretamente os valores no financeiro.

Clique em OK para seguir.

## 04

Também pode aparecer um aviso informando que nenhum usuário master foi configurado para a loja logada.

O usuário master é importante porque libera a administração completa das permissões do módulo e também permite conceder permissões aos demais usuários.

Neste vídeo, vamos ver o caminho para configurar essa permissão mais adiante.

Depois de ler o aviso, clique em OK.

## 05

Para configurar o plano financeiro sugerido, acesse o menu Configurações.

Depois, passe o mouse sobre Configurações Financeiras e selecione a opção Plano Financeiro padrão da empresa.

É nessa tela que vamos indicar a conta financeira, o centro de custo e o percentual que serão usados como sugestão para a operação de entrada de notas.

## 06

Na tela de sugestão de plano financeiro, localize a seção Entrada de notas, identificada como CP.

No campo Conta Financeira, clique em Selecionar.

Na janela de ajuda, escolha a conta financeira que corresponde à regra da empresa.

No exemplo da tela, foi selecionada uma conta relacionada a produtos para revenda. Mas, em um ambiente real, a conta deve seguir a orientação da empresa ou do responsável financeiro.

## 07

Depois de selecionar a conta financeira, o próximo passo é selecionar o centro de custo.

Clique em Selecionar no campo Centro de Custo.

Na janela de ajuda, escolha o centro de custo que será usado na entrada das notas.

No exemplo, foi selecionado o centro de custo Loja. Em uma implantação real, use o centro de custo definido pela empresa.

## 08

Com a conta financeira e o centro de custo preenchidos, informe o percentual de distribuição.

Neste exemplo, vamos usar 100%, indicando que todo o valor da entrada será direcionado para essa única combinação.

Se a empresa trabalhar com mais de uma conta financeira ou mais de um centro de custo, os percentuais podem ser divididos. O ponto mais importante é que a soma final feche exatamente 100%.

Depois de informar o percentual, clique em Incluir.

## 09

Depois de incluir a configuração, confira se a operação ENTRADA_NOTAS aparece na grade.

Revise a conta financeira, o centro de custo e o percentual informado.

Se estiver tudo correto, clique em Salvar configuração.

Com isso, o sistema passa a ter uma sugestão de plano financeiro para a entrada das notas.

## 10

Agora vamos configurar os dados financeiros da empresa que serão usados na entrada de notas.

No menu Configurações, acesse Configurações Financeiras e selecione Configurações financeiras da empresa.

Essa tela permite definir informações como espécie de documento padrão e meio de pagamento padrão.

## 11

Na tela de configurações financeiras da empresa, localize a seção Entrada de notas.

Aqui devem ser informados dois campos principais: a espécie do documento padrão e o meio de pagamento padrão.

No exemplo, a espécie do documento está como DM, Duplicata Mercantil, e o meio de pagamento está como Boleto.

Esses dados devem seguir a regra financeira da empresa.

Depois de revisar as informações, clique em Salvar.

Antes de usar este print em um material público, revise se é necessário ocultar CNPJ ou dados da empresa.

## 12

Depois de salvar as configurações financeiras, volte ao menu Configurações.

Agora selecione Parametrização do módulo.

Essa tela reúne parâmetros que definem como a Entrada de Notas Recebe Fácil deve se comportar durante o processo de entrada.

## 13

Na parametrização do módulo, revise cada opção apresentada.

A primeira opção destacada é Exigir liberação prévia para entrada automática.

Quando essa opção está marcada como Sim, o sistema só realiza a entrada automática das notas que foram previamente liberadas. Essa liberação pode ser feita pelo Weber Mobile.

Também existem parâmetros relacionados à atualização de custo do produto após a entrada e à atualização de custo dos produtos associados à entrada.

Quando esses parâmetros estão configurados como Sim, o sistema pode atualizar os custos conforme a regra descrita na própria tela.

Revise essas opções de acordo com a regra da empresa. Depois, clique em Salvar.

## 14

Agora vamos tratar o aviso de usuário master e revisar as permissões do módulo.

No menu Configurações, clique em Permissões.

Essa tela permite liberar funcionalidades de entrada, configurações e módulos de análise para cada usuário.

## 15

Na tela de permissões, selecione a loja e o usuário que receberá as permissões.

Depois, clique em Carregar.

Na lista de funcionalidades, marque a permissão Usuário Master quando esse usuário for responsável por administrar as permissões do módulo.

A própria tela informa que essa permissão concede acesso às demais ferramentas e também autoriza conceder permissões para outros usuários.

Na parte inferior, revise os módulos de análise que o usuário poderá consultar, como análise de CFOPs, associações de produtos por fornecedor, estatísticas de fornecedores, ranking de produtos comprados e variações de preço de compra.

Depois de revisar tudo, clique em Salvar.

Essa permissão deve ser liberada apenas para usuários autorizados.

## 16

Pronto. Com essas configurações concluídas, o ambiente passa a ter as principais configurações prévias necessárias para utilizar a Entrada de Notas Recebe Fácil.

Neste tutorial, revisamos os avisos iniciais, configuramos o plano financeiro padrão, selecionamos conta financeira e centro de custo, definimos o percentual de distribuição, configuramos espécie de documento e meio de pagamento, revisamos a parametrização do módulo e liberamos as permissões necessárias.

No próximo material, podemos seguir para a entrada assistida, para a localização das notas disponíveis ou para uma explicação mais detalhada da parametrização do módulo.
