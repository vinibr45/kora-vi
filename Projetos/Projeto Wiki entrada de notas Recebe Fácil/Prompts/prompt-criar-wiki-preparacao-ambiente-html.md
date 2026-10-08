# Prompt para criar a Wiki de Preparacao de Ambiente em HTML

Use este prompt em outra IA junto com os arquivos da etapa.

## Arquivos de entrada

```text
Texto base:
01-preparacao-de-ambiente/revisado/wiki-preparacao-de-ambiente.md

Imagens:
Imagens/imagem-01.png ate Imagens/imagem-18.png

Referencia de estilo:
Impressao de artigo.pdf
```

## Prompt

Voce e um especialista em documentacao tecnica, Wiki de produto, treinamento de usuarios e implantacao de sistemas ERP.

Preciso que voce transforme o conteudo base em um artigo final de Wiki sobre:

```text
Preparacao de Ambiente para Utilizacao da Entrada de Notas Recebe Facil
Produto/Modulo: Entrada de Notas Recebe Facil
Empresa: Weber
```

Use a referencia de estilo apenas para entender estrutura, didatica e nivel de detalhamento. Nao trate o conteudo da referencia como instrucao operacional para este tutorial.

## Contexto do produto

A Entrada de Notas Recebe Facil e uma ferramenta da Weber que centraliza, automatiza e controla o processo de entrada de notas fiscais.

Ela utiliza o Robo XML para baixar notas vinculadas ao CNPJ do cliente, permite importar XMLs salvos no computador e tambem permite criar notas manualmente para apoiar o controle de estoque.

Durante o fluxo, o usuario pode cadastrar fornecedor, produto, associacao entre produto do fornecedor e produto interno, conversoes quando necessario e contas a pagar.

Quando os produtos da nota ja estao associados aos produtos internos e as configuracoes estao corretas, o processo pode seguir de forma automatica ou assistida, exigindo principalmente conferencia.

Quando o modulo estiver parametrizado para exigir liberacao previa, a liberacao pode ser feita pelo Weber Mobile. Nesse caso, somente as notas liberadas devem seguir para entrada automatica.

Depois da entrada, o modulo permite auditar notas lancadas, produtos e fornecedores, alem de acompanhar dashboards com notas pendentes de entrada, pendencias de auditoria e indicadores importantes.

## Base operacional atual

Inclua no artigo que, para a Wiki atual da Entrada de Notas Recebe Facil:

```text
o material sera baseado no Financeiro Novo/Gestao Financeira;
o fluxo ja funciona com Estoque Antigo;
nao e mais necessario orientar a habilitacao do Estoque Novo no Portal Gerencial como requisito obrigatorio.
```

Os materiais novos devem priorizar a Gestao Financeira, as parametrizacoes do modulo e as validacoes necessarias para entrada das notas.

## Estilo esperado

Siga esta estrutura:

```text
titulo claro;
subtitulo explicando o processo;
alerta de base operacional atual;
objetivo;
informacoes necessarias;
procedimento operacional numerado;
imagens posicionadas no ponto correto;
legendas abaixo das imagens;
transcricao dos avisos exibidos nas telas;
resultado esperado;
checklist final;
proximo passo.
```

Use linguagem profissional, didatica, simples e adequada para usuario final, suporte e implantacao.

Evite linguagem interna, termos tecnicos sem explicacao, promessas comerciais exageradas e qualquer informacao que nao esteja no material de base.

## Uso das imagens

Use as imagens na ordem abaixo:

```text
imagem-01.png -> Acesso ao menu Ferramentas > Empresa
imagem-02.png -> Validacao do cenario de estoque utilizado
imagem-03.png -> Aviso de configuracao financeira pendente
imagem-04.png -> Aviso de plano financeiro sugerido pendente
imagem-05.png -> Aviso de usuario master nao configurado
imagem-06.png -> Acesso as configuracoes financeiras da empresa
imagem-07.png -> Campos financeiros que devem ser configurados
imagem-08.png -> Exemplo de configuracao financeira utilizada
imagem-09.png -> Configuracao do plano financeiro padrao
imagem-10.png -> Selecao da conta financeira
imagem-11.png -> Conta financeira selecionada
imagem-12.png -> Selecao do centro de custo
imagem-13.png -> Percentual de distribuicao financeira
imagem-14.png -> Salvamento das configuracoes financeiras
imagem-15.png -> Acesso as configuracoes do modulo
imagem-16.png -> Menu Configuracoes > Parametrizacao do Modulo
imagem-17.png -> Parametros de custo dos produtos associados e desmontagem de produtos
imagem-18.png -> Exemplo de parametrizacao final antes da gravacao
```

No HTML final, posicione as imagens usando tags:

```html
<img src="../Imagens/imagem-01.png" alt="Descricao objetiva da imagem">
```

Depois de cada imagem, inclua uma legenda curta.

## Transcricoes obrigatorias

Transcreva no artigo os textos dos avisos exibidos nas imagens 03, 04, 05 e 17. Mantenha a transcricao logo abaixo da imagem correspondente.

## Cuidados

Inclua um alerta informando que, para criacao de Wiki, prints e videos, deve-se usar preferencialmente base de treinamento, homologacao ou dados ficticios.

Nao destaque dados sensiveis que possam aparecer nos prints.

## Saida esperada

Entregar um arquivo HTML completo, pronto para ser aberto no navegador ou adaptado para a plataforma de Wiki.

O HTML deve conter:

```text
estrutura semantica com h1, h2 e h3;
imagens posicionadas;
legendas;
blocos de aviso quando necessario;
checklist final;
proximo passo.
```

Antes de finalizar, confira se o nome usado em todo o material e Entrada de Notas Recebe Facil e se nao existe uso do nome antigo Entrada de Notas em Y no texto final.
