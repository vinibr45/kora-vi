# O que é a Entrada de Notas Recebe Fácil

## Explicação curta

A **Entrada de Notas Recebe Fácil** é uma ferramenta da Weber criada para facilitar e automatizar o processo de entrada de notas fiscais no sistema.

Seu principal objetivo é reduzir o trabalho manual do usuário durante o lançamento das notas, tornando o processo mais rápido, padronizado e seguro.

## Função principal

A função principal da Entrada de Notas Recebe Fácil é permitir que a entrada de notas seja realizada de forma automática quando os produtos da nota fiscal já estiverem corretamente associados aos produtos cadastrados no sistema.

Na prática, isso significa que, quando o fornecedor envia uma nota e os itens dessa nota já possuem associação com os produtos internos da empresa, o sistema consegue reconhecer esses produtos e avançar no processo de entrada com muito menos intervenção manual.

Além disso, a ferramenta utiliza o **Robô XML** para baixar as notas fiscais vinculadas ao CNPJ do cliente. Depois que essas notas ficam disponíveis no sistema, o usuário pode acessá-las pelo próprio fluxo do Recebe Fácil e realizar os cadastros necessários sem precisar sair do processo.

Dentro do fluxo de entrada, é possível cadastrar ou complementar informações como:

- fornecedor;
- produto;
- associação entre produto do fornecedor e produto interno;
- contas a pagar relacionado à nota.

O Recebe Fácil também permite outros métodos de entrada. Além das notas baixadas pelo Robô XML, o usuário pode importar manualmente um arquivo XML salvo no computador ou criar uma nota manualmente quando precisar registrar uma movimentação para melhor controle do estoque.

Depois da entrada, independentemente do método utilizado, a ferramenta permite auditar as notas lançadas para revisar informações, identificar pendências e ajustar pontos que possam ter ficado para trás.

## Como a automação funciona

De forma simplificada, o processo funciona assim:

```text
1. O Robô XML baixa as notas fiscais vinculadas ao CNPJ do cliente.
2. As notas ficam disponíveis para acompanhamento e entrada no Recebe Fácil.
3. O Recebe Fácil analisa os produtos existentes na nota.
4. O sistema verifica se os produtos da nota já estão associados aos produtos cadastrados internamente.
5. Se houver dados pendentes, o usuário pode cadastrar fornecedor, produto ou contas a pagar dentro do próprio fluxo.
6. Se os produtos estiverem associados e as configurações estiverem corretas, a entrada pode ser realizada de forma automática ou assistida.
7. O usuário também pode importar um XML salvo no computador ou criar uma nota manualmente, quando necessário.
8. Após a entrada, o usuário pode auditar a nota, os produtos e os fornecedores para revisar pendências e corrigir informações.
9. O usuário acompanha, confere e valida o processo conforme a regra da empresa.
```

Essa automação depende diretamente da qualidade das configurações e das associações existentes. Quanto mais completa estiver a base de produtos, fornecedores, conversões e parametrizações, mais simples será o processo de entrada.

## Associação de produtos

A associação de produtos é uma etapa essencial para o funcionamento da Entrada de Notas Recebe Fácil.

Ela relaciona o produto que vem na nota do fornecedor com o produto que já existe no cadastro interno da empresa.

Exemplo:

```text
Produto na nota do fornecedor -> Produto cadastrado no sistema Weber
```

Quando essa relação já existe, o sistema consegue identificar automaticamente qual produto interno corresponde ao item da nota.

Quando essa relação não existe, o usuário pode precisar associar o produto manualmente, cadastrar um novo produto ou ajustar a conversão, dependendo do caso.

## Integração com o Weber Mobile

A Entrada de Notas Recebe Fácil também possui uma interação importante com o **Weber Mobile**.

Quando a parametrização do módulo estiver configurada para **exigir liberação prévia para entrada de notas**, as notas precisam ser liberadas antes de entrarem automaticamente.

Essa liberação pode ser feita pelo Weber Mobile.

Com isso, o fluxo fica mais controlado:

```text
1. A nota chega ao sistema.
2. A empresa revisa ou libera a nota pelo Weber Mobile.
3. Apenas as notas liberadas ficam autorizadas para entrada automática.
4. O Recebe Fácil executa a entrada automática somente das notas permitidas.
```

## O que o cliente ganha usando a ferramenta

Com a Entrada de Notas Recebe Fácil, o cliente ganha:

- acesso centralizado às notas baixadas pelo Robô XML;
- possibilidade de importar XML baixado no computador;
- possibilidade de criar notas manualmente para controle do estoque;
- menos digitação manual;
- mais agilidade na entrada das notas;
- redução de retrabalho;
- maior padronização no processo;
- possibilidade de cadastrar fornecedor, produto e contas a pagar durante o próprio fluxo;
- auditoria das notas lançadas após qualquer método de entrada;
- auditoria de produtos e fornecedores vinculados às notas;
- dashboards com informações sobre notas pendentes de entrada, notas pendentes de auditoria e demais acompanhamentos importantes;
- melhor controle das notas que podem ou não entrar automaticamente;
- mais segurança quando a empresa utiliza liberação prévia;
- integração com o Weber Mobile para apoiar a aprovação das notas;
- facilidade para acompanhar pendências, produtos não associados e pontos que precisam de revisão.

## Ponto importante para a Wiki

Ao explicar a ferramenta na Wiki, deixe claro que a automação não depende apenas da nota fiscal. Ela depende também de uma base bem preparada.

Antes de esperar uma entrada automática, o cliente precisa entender que existem requisitos obrigatórios para utilização do Recebe Fácil.

Para utilizar a **Entrada de Notas Recebe Fácil**, o cliente precisa estar com:

- **Financeiro Novo**, também chamado de **Gestão Financeira**, ativo;
- **Estoque Novo** habilitado, com a flag de Estoque Novo ativa no **Portal Gerencial**.

Caso o cliente não atenda a esses requisitos, ele não deve seguir com a utilização do fluxo baseado no Estoque Novo.

Além desses requisitos, algumas configurações devem estar corretas, como:

- parametrização do módulo;
- permissões de uso;
- configurações financeiras;
- combinações fiscais necessárias;
- produtos cadastrados;
- produtos associados ao fornecedor;
- conversões configuradas quando houver diferença de unidade ou embalagem;
- regra de liberação prévia, quando utilizada.

## Texto sugerido para usar na Wiki

A **Entrada de Notas Recebe Fácil** é uma ferramenta da Weber que automatiza e simplifica o processo de entrada de notas fiscais.

Ela utiliza o Robô XML para baixar as notas vinculadas ao CNPJ do cliente, disponibiliza essas notas para entrada no sistema e permite que o usuário cadastre fornecedor, produto e contas a pagar durante o próprio fluxo.

Além das notas baixadas automaticamente, o Recebe Fácil também permite importar XMLs salvos no computador e criar notas manualmente para apoiar o controle do estoque.

Além disso, a ferramenta identifica os produtos da nota, verifica se eles já estão associados aos produtos cadastrados no sistema e, quando as configurações estão corretas, permite que a entrada seja realizada com pouca intervenção manual.

Nos casos em que a empresa utiliza liberação prévia, o processo pode ser integrado ao Weber Mobile. Assim, apenas as notas liberadas ficam autorizadas para entrada automática, garantindo mais controle e segurança para a operação.

Após a entrada, a ferramenta ainda permite auditar as notas, produtos e fornecedores, além de acompanhar dashboards com informações importantes sobre notas pendentes de entrada e pendências de auditoria.

Com isso, o Recebe Fácil ajuda a reduzir digitação, evitar retrabalho, padronizar o processo e tornar a entrada de notas mais rápida, controlada e confiável.
