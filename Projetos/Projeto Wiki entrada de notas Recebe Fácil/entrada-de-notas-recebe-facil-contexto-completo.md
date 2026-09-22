# Entrada de Notas Recebe Fácil - Contexto Completo

Este documento consolida tudo que foi levantado até agora sobre a **Entrada de Notas Recebe Fácil**, da Weber.

O objetivo é servir como base de contexto para criação de Wiki, roteiros de vídeo, prompts para IA, materiais de treinamento e organização dos próximos tópicos da documentação.

## Nome correto do módulo

O nome definido para o módulo é:

```text
Entrada de Notas Recebe Fácil
```

Não utilizar mais o nome:

```text
Entrada de Notas em Y
```

Esse nome antigo pode aparecer em arquivos originais, prints ou materiais anteriores, mas nos novos textos, Wikis, prompts e roteiros deve ser substituído por **Entrada de Notas Recebe Fácil**.

## O que é a Entrada de Notas Recebe Fácil

A **Entrada de Notas Recebe Fácil** é uma ferramenta da Weber criada para centralizar, automatizar e facilitar o processo de entrada de notas fiscais.

Ela foi pensada para reduzir digitação manual, padronizar o processo, melhorar o controle das notas recebidas e permitir que o usuário acompanhe pendências antes, durante e depois da entrada.

A ferramenta pode atuar de forma automática, assistida ou manual, dependendo das configurações da empresa e da situação da nota.

## Objetivo principal

O principal objetivo da Entrada de Notas Recebe Fácil é permitir que a entrada de notas seja realizada de forma mais automática quando os produtos da nota já estiverem corretamente associados aos produtos cadastrados no sistema.

Quando a base está bem configurada, o sistema consegue reconhecer os itens da nota, relacioná-los aos produtos internos e reduzir a necessidade de intervenção manual do usuário.

## Requisitos obrigatórios

Para utilizar a Entrada de Notas Recebe Fácil, o cliente precisa atender a dois requisitos obrigatórios:

- estar com o **Financeiro Novo**, também chamado de **Gestão Financeira**, ativo;
- estar com o **Estoque Novo** habilitado, com a flag de Estoque Novo ativa no **Portal Gerencial**.

Caso o cliente não atenda a esses requisitos, ele não deve seguir com a utilização do fluxo baseado no Estoque Novo.

## Configurações importantes antes do uso

Antes de iniciar a operação, algumas configurações precisam estar corretas:

- Financeiro Novo/Gestão Financeira ativo;
- Estoque Novo habilitado no Portal Gerencial;
- parametrização do módulo;
- permissões de entrada de notas e análises;
- configurações financeiras da empresa;
- plano financeiro padrão;
- conta financeira;
- centro de custo;
- combinações fiscais necessárias, como CFOP + CST;
- produtos cadastrados;
- fornecedores cadastrados;
- produtos associados ao fornecedor;
- conversões configuradas quando houver diferença de unidade ou embalagem;
- regra de liberação prévia, quando utilizada.

## Robô XML

A Entrada de Notas Recebe Fácil utiliza o **Robô XML** para baixar as notas fiscais vinculadas ao CNPJ do cliente.

Depois que as notas são baixadas, elas ficam disponíveis no sistema para acompanhamento, conferência e entrada.

Esse fluxo permite que o usuário visualize as notas recebidas sem precisar procurar manualmente cada XML, desde que o processo esteja configurado corretamente.

## Formas de entrada de notas

A ferramenta permite trabalhar com notas por diferentes métodos.

### 1. Notas baixadas pelo Robô XML

O Robô XML baixa as notas vinculadas ao CNPJ do cliente e disponibiliza essas notas no Recebe Fácil.

A partir disso, o usuário pode iniciar o processo de entrada, conferindo os dados e tratando pendências.

### 2. Importação manual de XML

Além das notas baixadas automaticamente, o usuário também pode importar manualmente um arquivo XML salvo no computador.

Esse recurso é útil quando o XML já foi baixado por outro meio ou quando o usuário precisa realizar a entrada de uma nota específica que está disponível localmente.

### 3. Criação manual de notas

O Recebe Fácil também permite criar notas manualmente.

Essa opção pode ser utilizada quando a empresa precisa registrar uma movimentação para melhorar o controle do estoque ou quando o processo exige uma entrada que não veio diretamente de um XML.

## Associação de produtos

A associação de produtos é uma das etapas mais importantes para o funcionamento da automação.

Ela relaciona o produto que vem na nota do fornecedor com o produto cadastrado internamente no sistema Weber.

Exemplo:

```text
Produto na nota do fornecedor -> Produto cadastrado no sistema Weber
```

Quando essa relação já existe, o sistema consegue identificar automaticamente o produto interno correspondente ao item da nota.

Quando essa relação não existe, o usuário pode precisar:

- associar o produto manualmente;
- cadastrar um novo produto;
- ajustar conversão;
- revisar GTIN/código de barras;
- validar informações fiscais ou cadastrais.

## Cadastro durante o fluxo

Dentro do próprio fluxo do Recebe Fácil, o usuário consegue cadastrar ou complementar informações necessárias para concluir a entrada.

Entre essas informações estão:

- fornecedor;
- produto;
- associação entre produto do fornecedor e produto interno;
- contas a pagar relacionado à nota.

Isso evita que o usuário precise sair do processo e navegar por várias rotinas diferentes para finalizar a entrada da nota.

## Cadastro de produto por GTIN

Um dos cenários previstos para a Wiki é a entrada de uma nota com produtos que precisam ser cadastrados pelo GTIN.

O objetivo desse tópico é mostrar a facilidade do cadastro quando a nota possui informações suficientes para identificar o produto, reduzindo esforço manual e ajudando a manter a base organizada.

## Associação por correspondência

Outro cenário importante é a entrada de uma nota com produtos ainda não associados.

Nesse caso, o usuário precisa associar o produto da nota ao produto interno correspondente, podendo também tratar conversões quando houver diferença entre a unidade da nota e a unidade utilizada pela empresa.

O objetivo desse material é mostrar a facilidade da associação por correspondência.

## Entrada automática

A entrada automática depende de alguns fatores:

- nota disponível no sistema;
- fornecedor reconhecido ou cadastrado;
- produtos cadastrados;
- produtos da nota associados aos produtos internos;
- conversões configuradas, quando necessário;
- configurações financeiras corretas;
- parâmetros do módulo definidos;
- regras fiscais compatíveis;
- liberação prévia realizada, quando exigida.

Quando esses pontos estão corretos, a entrada tende a exigir apenas conferência e validação do usuário.

## Entrada assistida

Quando existem informações pendentes, o processo pode ser assistido.

Nesse cenário, o sistema conduz o usuário pelas etapas necessárias, permitindo tratar pendências, cadastrar dados e revisar informações antes da conclusão da entrada.

## Integração com Weber Mobile

A Entrada de Notas Recebe Fácil possui integração importante com o **Weber Mobile**.

Quando a parametrização do módulo estiver configurada para exigir **liberação prévia para entrada de notas**, as notas precisam ser liberadas antes de entrarem automaticamente.

Essa liberação pode ser feita pelo Weber Mobile.

Fluxo resumido:

```text
1. A nota chega ao sistema.
2. A empresa revisa ou libera a nota pelo Weber Mobile.
3. Apenas as notas liberadas ficam autorizadas para entrada automática.
4. O Recebe Fácil executa a entrada automática somente das notas permitidas.
```

Esse recurso aumenta o controle da empresa sobre quais notas podem seguir para entrada automática.

## Auditoria após a entrada

Depois da entrada, independentemente do método utilizado, a ferramenta permite auditar as notas lançadas.

A auditoria serve para revisar informações, identificar pendências e ajustar pontos que possam ter ficado para trás durante a entrada.

O sistema também permite auditar:

- notas lançadas;
- produtos das notas;
- fornecedores vinculados às notas;
- pendências relacionadas ao processo.

Essa etapa é importante porque a entrada da nota pode envolver impactos em estoque, financeiro, fiscal, cadastro de produto, fornecedor e contas a pagar.

## Dashboards e acompanhamento

A Entrada de Notas Recebe Fácil possui dashboards com informações importantes para acompanhamento do processo.

Entre os indicadores e visões previstos, estão:

- notas pendentes de entrada;
- notas pendentes de auditoria;
- produtos pendentes de revisão;
- fornecedores pendentes de revisão;
- valor pendente de entrada;
- notas lançadas;
- valores de notas lançadas;
- itens/produtos distintos;
- auditoria fiscal;
- estatísticas de fornecedor;
- ranking de produtos comprados;
- variações de preço de compra.

Essas informações ajudam o usuário e a equipe técnica a acompanhar o que já foi tratado e o que ainda precisa de ação.

## Benefícios para o cliente

Com a Entrada de Notas Recebe Fácil, o cliente ganha:

- acesso centralizado às notas baixadas pelo Robô XML;
- possibilidade de importar XML salvo no computador;
- possibilidade de criar notas manualmente;
- redução de digitação manual;
- mais agilidade na entrada das notas;
- redução de retrabalho;
- padronização do processo;
- cadastro de fornecedor, produto e contas a pagar dentro do fluxo;
- associação de produtos da nota com produtos internos;
- apoio ao cadastro de produtos por GTIN;
- controle de notas liberadas para entrada automática;
- integração com Weber Mobile para liberação prévia;
- auditoria das notas lançadas;
- auditoria de produtos e fornecedores;
- dashboards para acompanhamento de pendências;
- melhor controle de estoque, financeiro e conferência operacional.

## Limites e cuidados

A automação não depende apenas da nota fiscal.

Ela depende de uma base bem preparada e de configurações corretas.

Se houver produtos sem associação, fornecedor pendente, conversão não configurada, plano financeiro ausente ou parametrização incompleta, o processo poderá exigir intervenção do usuário.

Também é importante que materiais de Wiki, prints e vídeos usem preferencialmente base de treinamento, homologação ou dados fictícios.

Evite expor:

- dados reais de clientes;
- CNPJ real quando não for necessário;
- valores sensíveis;
- fornecedores estratégicos;
- informações fiscais privadas;
- credenciais;
- senhas;
- dados de produção sem autorização.

## Tópicos planejados para a Wiki

O cronograma inicial da Wiki contempla os seguintes tópicos:

```text
01 - Preparação do ambiente para gravação dos vídeos
02 - Configurações prévias: o que precisa estar configurado antes de iniciar as entradas de nota
03 - Parametrização do módulo de entrada de notas
04 - Permissões de entrada de notas e análises
05 - Combinações CFOP + CST
06 - Configurações financeiras da empresa
07 - O que é o Recebe Fácil, objetivo da ferramenta e demonstração rápida/comercial
08 - Controle das entradas: visão geral do painel inicial
09 - Notas disponíveis para entrada: como localizar e iniciar a entrada de uma nota
10 - Entrada de notas assistida: como realizar a entrada assistida
11 - Entrada de nota com produtos e conversões já configurados
12 - Entrada com produtos para cadastrar pelo GTIN
13 - Associação de produto e conversão por correspondência
14 - Notas lançadas: auditoria
15 - Fornecedores pendentes de revisão
16 - Produtos pendentes de revisão
17 - CT-e 57: importação, vínculo e rateio
18 - Análise de CFOPs
19 - Estatísticas de fornecedor: entradas
20 - Ranking de produtos comprados
21 - Associação de produtos por fornecedor
22 - Variações de preço de compra
```

Caso sejam identificados novos tópicos durante a execução, eles devem ser adicionados ao cronograma e tratados como tarefas separadas.

## Etapa atual da documentação

A etapa trabalhada até agora é:

```text
01 - Preparação do ambiente
```

O tutorial dessa etapa aborda:

- acesso a `Ferramentas > Empresa`;
- habilitação do Estoque Novo;
- avisos de configuração financeira pendente;
- plano financeiro sugerido pendente;
- usuário master não configurado;
- configurações financeiras da empresa;
- plano financeiro padrão;
- conta financeira;
- centro de custo;
- percentual de distribuição;
- salvamento das configurações financeiras;
- acesso à parametrização do módulo;
- parâmetros de custo dos produtos associados;
- parâmetros de desmontagem de produtos;
- gravação da parametrização.

## Textos de aviso já transcritos

Durante a preparação do ambiente, alguns avisos foram transcritos para a Wiki.

### Configuração financeira pendente

```text
Para utilizar a entrada de nota, selecione ou configure o meio de pagamento e a espécie de documento que serão usados no financeiro das notas de entrada.

No Controle de Entradas, acesse:
Fornecedor: Configurações > Configurações Financeiras > Plano Financeiro padrão e outras configurações por fornecedor.
Loja: Configurações > Configurações Financeiras > Configurações financeiras da empresa.
```

### Plano financeiro sugerido pendente

```text
Para utilizar a entrada de nota, configure o plano financeiro sugerido para a operação ENTRADA_NOTAS.

No Controle de Entradas, acesse:
Configurações > Configurações Financeiras > Plano Financeiro padrão da empresa.
```

### Usuário master não configurado

```text
Nenhum Usuário Master foi configurado para a loja logada.

Configure ao menos um usuário com a permissão 'Usuário Master' para liberar a administração completa das permissões.

Para liberar o Usuário Master, no Dashboard Inicial acesse Configurações > Permissões.
```

### Custo dos produtos associados e desmontagem

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

## Resumo curto para uso em Wiki ou apresentação

A **Entrada de Notas Recebe Fácil** é uma ferramenta da Weber que centraliza, automatiza e controla o processo de entrada de notas fiscais.

Ela utiliza o Robô XML para baixar notas vinculadas ao CNPJ do cliente, permite importar XMLs salvos no computador e também possibilita criar notas manualmente para apoiar o controle de estoque.

Durante o fluxo, o usuário pode cadastrar fornecedor, produto, associação de produtos e contas a pagar. Quando os produtos da nota já estão associados aos produtos internos e as configurações estão corretas, o processo pode seguir de forma automática ou assistida.

O módulo também se integra ao Weber Mobile para liberação prévia de notas, quando essa regra estiver habilitada. Depois da entrada, permite auditar notas, produtos e fornecedores, além de acompanhar dashboards com pendências e indicadores importantes.

Para utilizar o Recebe Fácil, o cliente precisa estar com o **Financeiro Novo/Gestão Financeira** ativo e com o **Estoque Novo** habilitado no **Portal Gerencial**.
