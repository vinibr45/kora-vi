# Contexto do Projeto para Outra IA

Use este prompt quando precisar explicar para outra IA o objetivo geral do projeto, o escopo da Wiki e em qual etapa estamos trabalhando.

## Prompt

Você vai me ajudar em um projeto de documentação do módulo **Entrada de Notas Recebe Fácil**, da empresa **Weber**.

> Definição de nomenclatura: a partir de agora, não utilize mais o nome "Entrada de Notas em Y". O nome correto do módulo é **Entrada de Notas Recebe Fácil**.

O objetivo do projeto é criar uma Wiki completa e didática para clientes que acessarão o Recebe Fácil pela primeira vez. O material também poderá apoiar técnicos, suporte e implantação, mas a linguagem principal deve ser simples, clara e orientada ao usuário final.

## O que é a Entrada de Notas Recebe Fácil

A **Entrada de Notas Recebe Fácil** é uma ferramenta da Weber criada para facilitar e automatizar o processo de entrada de notas fiscais.

A função principal dela é permitir que a entrada de notas seja realizada de forma automática quando os produtos da nota já estiverem associados aos produtos cadastrados no sistema.

Para utilizar a ferramenta, o cliente precisa atender a dois requisitos obrigatórios: estar com o **Financeiro Novo/Gestão Financeira** ativo e estar com o **Estoque Novo** habilitado por meio da flag de Estoque Novo no **Portal Gerencial**. Caso esses requisitos não estejam atendidos, o cliente não deve seguir com o uso do fluxo baseado no Estoque Novo.

Outro ponto importante é que a ferramenta utiliza o **Robô XML** para baixar as notas fiscais vinculadas ao CNPJ do cliente. Essas notas ficam disponíveis no Recebe Fácil, e o usuário consegue trabalhar nelas dentro do próprio fluxo.

Durante a entrada, o sistema também permite cadastrar ou complementar informações necessárias, como fornecedor, produto e contas a pagar.

Além do fluxo com notas baixadas pelo Robô XML, o Recebe Fácil também permite importar XMLs salvos no computador e criar notas manualmente quando a empresa precisar registrar movimentações para melhor controle do estoque.

Depois de qualquer método de entrada, o módulo permite auditar as notas lançadas para revisar informações e ajustar pendências. Também é possível auditar produtos e fornecedores vinculados às notas.

O módulo possui dashboards com informações importantes para acompanhamento, como notas pendentes de entrada, pendências de auditoria, produtos pendentes e fornecedores pendentes.

Ela também possui uma integração importante com o **Weber Mobile**. Quando a parametrização do módulo estiver marcada para exigir liberação prévia, as notas podem ser liberadas pelo Weber Mobile. Nesse cenário, a entrada automática deve considerar apenas as notas previamente liberadas.

## O que o projeto pretende entregar

O projeto pretende produzir um pacote completo de treinamento e documentação contendo:

```text
1. Wiki escrita com passo a passo para cada tela/processo.
2. Prints organizados e bem posicionados em cada etapa.
3. Roteiro de vídeo para cada tela/processo.
4. Vídeo específico demonstrando a funcionalidade correspondente.
5. Checklist de conferência ao final de cada tutorial.
6. Observações técnicas separadas do conteúdo principal, quando necessário.
7. Registro de dúvidas, impedimentos e pontos que precisem de validação.
```

Cada tela ou processo do Recebe Fácil deve ter um material próprio. A ideia é que o cliente consiga entender:

```text
o que precisa estar configurado antes de iniciar;
como realizar a entrada de notas;
como acompanhar as notas depois da entrada;
como revisar pendências, associações, auditorias e análises;
o que conferir antes de confirmar ou gravar uma ação.
```

## Público-alvo

O conteúdo deve atender:

```text
usuários finais;
equipe fiscal;
equipe administrativa;
técnicos;
implantadores;
suporte.
```

O texto deve ser escrito de forma acessível. Termos técnicos podem ser usados quando forem necessários, mas precisam ser explicados. Informações mais técnicas devem ficar em blocos separados, para que o usuário final não se perca durante o passo a passo.

## Forma de trabalho

O fluxo planejado é:

```text
1. Criar uma cópia ou base preparada para demonstração.
2. Usar dados fictícios ou controlados sempre que possível.
3. Tirar prints das telas.
4. Escrever um rascunho básico do que está sendo feito.
5. Revisar o texto para ficar mais didático e profissional.
6. Organizar imagens, legendas e passo a passo.
7. Usar a Wiki revisada como roteiro para gravação do vídeo.
8. Validar o material antes de publicar ou enviar para clientes.
```

## Cuidados importantes

Não devem ser expostos dados sensíveis em prints, vídeos ou textos, como:

```text
dados reais de clientes;
CNPJ real quando não for necessário;
valores sensíveis;
fornecedores estratégicos;
informações fiscais privadas;
credenciais;
senhas;
dados de produção sem autorização.
```

Sempre que possível, usar base de treinamento, homologação ou dados fictícios.

## Cronograma de tópicos da Wiki

Estes são os tópicos planejados para o projeto:

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

Caso surjam novos tópicos durante a execução, eles devem ser adicionados ao cronograma e tratados como tarefas separadas.

## Etapa atual

Estamos trabalhando no tópico:

```text
01 - Preparação do ambiente para gravação dos vídeos
```

Dentro desse tópico, o primeiro tutorial criado é:

```text
Preparação de Ambiente para Utilização da Entrada de Notas Recebe Fácil
```

Esse tutorial mostra:

```text
como acessar Ferramentas > Empresa;
como habilitar o Estoque Novo;
como validar mensagens exibidas no primeiro acesso;
como iniciar as configurações financeiras da empresa;
como configurar plano financeiro padrão;
como selecionar conta financeira;
como selecionar centro de custo;
como informar percentual de distribuição;
como salvar as configurações financeiras;
como acessar Configurações > Parametrização do Módulo;
como preencher e gravar os parâmetros obrigatórios.
```

## Arquivos da etapa atual

Os arquivos estão organizados nesta pasta:

```text
C:\Kora\kora-vi\Projetos\Projeto Wiki entrada de notas em Y\01-preparacao-de-ambiente
```

Principais arquivos:

```text
originais/
```

Contém o PDF e o ODT original recebidos como fonte.

```text
imagens-extraidas-odt/
```

Contém as imagens extraídas do ODT, numeradas de `imagem-01.png` até `imagem-18.png`.

```text
revisado/wiki-preparacao-de-ambiente.md
```

Contém a versão revisada em Markdown do tutorial.

```text
revisado/roteiro-video-preparacao-de-ambiente.md
```

Contém um roteiro curto para gravação do vídeo.

```text
prompt-para-gerar-wiki-com-outra-ia.md
```

Contém um prompt específico para outra IA gerar a Wiki final usando o Markdown e as imagens.

## Como a outra IA deve ajudar

A outra IA deve ajudar a:

```text
melhorar a didática;
organizar o texto final;
inserir as imagens na ordem correta;
criar legendas claras;
manter linguagem simples;
separar observações técnicas;
não inventar funcionalidades;
criar uma versão final pronta para Wiki, Word ou PDF;
gerar um roteiro de vídeo coerente com a Wiki.
```

## Critérios de qualidade

Antes de considerar um material pronto, verificar se:

```text
o tutorial pode ser entendido por alguém que nunca usou o Recebe Fácil;
o objetivo do processo está claro;
os pré-requisitos estão explícitos;
cada ação tem uma orientação objetiva;
cada imagem tem uma legenda;
o usuário sabe o que conferir antes de salvar/gravar;
há resultado esperado;
há checklist final;
há seção de possíveis dúvidas;
o próximo passo da Wiki está indicado;
não existem dados sensíveis expostos sem necessidade.
```

## Tom desejado

Use tom:

```text
profissional;
didático;
simples;
direto;
acolhedor;
adequado para documentação oficial de produto.
```

Evite:

```text
linguagem informal demais;
texto técnico sem explicação;
frases longas e confusas;
comentários internos;
promessas comerciais exageradas;
qualquer informação que não esteja baseada no material fornecido.
```
