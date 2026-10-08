# WEBER Sistemas - Contexto Consolidado de Gestao de Conhecimento

## Purpose

Consolidar o contexto operacional das duas pastas de projeto para que a KORA ajude a atualizar a gestao de conhecimento da WEBER Sistemas.

## Current Truth

A WEBER possui materiais dispersos em duas frentes principais:

1. Wiki de versao e principais alteracoes de usabilidade.
2. Wiki e treinamento do modulo Entrada de Notas Recebe Facil.

Esses materiais ja contem regras editoriais, prompts, modelos, contexto de produto, prints, GIFs, HTMLs, CSVs e documentos revisados. O trabalho agora e transformar esse material em uma base de conhecimento mais organizada, reutilizavel e facil de manter.

## Frente 1: Wiki De Versao E Weber Patches

A pasta `Principais Alterações de Usabilidade de Nova Versão - Weber` organiza materiais de versoes por data, especialmente:

```text
VERSAO 16_07_2026
VERSAO 01_09_2026
```

O padrao editorial identificado para a wiki de versao e:

- criar artigos claros para tecnicos orientarem clientes;
- evitar citar DLL, ZIP, executavel, beta ou detalhes internos no texto principal;
- usar nomes amigaveis para modulos e rotinas;
- separar rastreabilidade tecnica em aba ou secao tecnica;
- incluir imagens, prints ou GIFs no fluxo do texto;
- explicar o que mudou, onde aparece, como usar e quais cuidados tomar;
- incluir secao `Oriente o cliente da seguinte forma` quando o artigo precisar virar fala de atendimento.

O conceito local **Weber Patches** existe para registrar releases por data quando nao houver versionamento formal. Cada patch deve responder:

- o que mudou;
- qual modulo foi afetado;
- se foi correcao, melhoria, novo recurso ou ajuste tecnico;
- qual impacto existe para suporte, cliente ou usuario;
- quais evidencias, chamados, RAAs ou demandas estao relacionados;
- quais problemas conhecidos precisam ser acompanhados.

## Frente 2: Entrada De Notas Recebe Facil

O nome correto do modulo e:

```text
Entrada de Notas Recebe Facil
```

Nao usar mais:

```text
Entrada de Notas em Y
```

A Entrada de Notas Recebe Facil e uma ferramenta da WEBER para centralizar, automatizar e facilitar o processo de entrada de notas fiscais.

Ela permite:

- trabalhar com notas baixadas pelo Robo XML;
- importar XML salvo no computador;
- criar notas manualmente;
- cadastrar ou complementar fornecedor;
- cadastrar ou complementar produto;
- associar produto da nota ao produto interno;
- tratar conversoes;
- gerar ou apoiar contas a pagar;
- auditar notas lancadas;
- auditar produtos e fornecedores;
- acompanhar dashboards e pendencias.

Base operacional da Wiki atual:

- Financeiro Novo/Gestao Financeira como base financeira do material;
- fluxo funcionando com Estoque Antigo;
- Estoque Novo no Portal Gerencial nao deve mais ser tratado como requisito obrigatorio.

Os materiais novos devem focar na Gestao Financeira, nas parametrizacoes do modulo e nas validacoes necessarias para entrada das notas.

## Servico: Weber Tributario

O **Weber Tributario** e um servico da WEBER usado para atualizar o cadastro de produtos com base nas informacoes fiscais fornecidas pela **IMENDES**.

A **IMENDES** e a assistencia fiscal utilizada pela WEBER como referencia para apoiar a revisao e atualizacao das regras fiscais dos produtos.

Na gestao de conhecimento, tratar o Weber Tributario como um servico ligado a:

- atualizacao cadastral de produtos;
- revisao fiscal de produtos;
- regras fiscais;
- apoio tributario baseado na IMENDES;
- orientacao para suporte quando o cadastro ou a regra fiscal do produto precisar ser revisado.

Nao tratar o Weber Tributario apenas como um modulo operacional comum sem explicar sua relacao com a IMENDES.

## Topicos Planejados Para A Wiki Do Recebe Facil

```text
01 - Preparacao do ambiente para gravacao dos videos
02 - Configuracoes previas: o que precisa estar configurado antes de iniciar as entradas de nota
03 - Parametrizacao do modulo de entrada de notas
04 - Permissoes de entrada de notas e analises
05 - Combinacoes CFOP + CST
06 - Configuracoes financeiras da empresa
07 - O que e o Recebe Facil, objetivo da ferramenta e demonstracao rapida/comercial
08 - Controle das entradas: visao geral do painel inicial
09 - Notas disponiveis para entrada: como localizar e iniciar a entrada de uma nota
10 - Entrada de notas assistida: como realizar a entrada assistida
11 - Entrada de nota com produtos e conversoes ja configurados
12 - Entrada com produtos para cadastrar pelo GTIN
13 - Associacao de produto e conversao por correspondencia
14 - Notas lancadas: auditoria
15 - Fornecedores pendentes de revisao
16 - Produtos pendentes de revisao
17 - CT-e 57: importacao, vinculo e rateio
18 - Analise de CFOPs
19 - Estatisticas de fornecedor: entradas
20 - Ranking de produtos comprados
21 - Associacao de produtos por fornecedor
22 - Variacoes de preco de compra
```

## Etapa Atual Documentada

A etapa atual mais desenvolvida e:

```text
01 - Preparacao do ambiente
```

Ela cobre:

- acesso a `Ferramentas > Empresa`;
- validacao do cenario de estoque utilizado, considerando compatibilidade com Estoque Antigo;
- avisos de configuracao financeira pendente;
- plano financeiro sugerido pendente;
- usuario master nao configurado;
- configuracoes financeiras da empresa;
- plano financeiro padrao;
- conta financeira;
- centro de custo;
- percentual de distribuicao;
- salvamento das configuracoes financeiras;
- acesso a `Configuracoes > Parametrizacao do Modulo`;
- parametros de custo dos produtos associados;
- parametros de desmontagem;
- gravacao da parametrizacao.

## Padrao De Qualidade Para Materiais

Todo material novo deve:

- ser entendido por alguem que nunca usou o recurso;
- declarar objetivo, pre-requisitos, passo a passo e resultado esperado;
- ter linguagem profissional, didatica, simples e direta;
- explicar termos tecnicos quando forem necessarios;
- separar observacoes tecnicas do conteudo principal;
- evitar promessas comerciais exageradas;
- nao inventar comportamento sem fonte;
- indicar imagens, GIFs ou prints necessarios;
- incluir checklist final quando for tutorial;
- registrar duvidas, impedimentos e pontos de validacao.

## What This Affects

- wiki interna;
- artigos de versao;
- comunicacao de releases;
- treinamento de clientes;
- suporte e implantacao;
- roteiro de videos;
- organizacao de prints, GIFs e HTMLs;
- gestao de conhecimento do produto.

## Boundaries

Este contexto nao define:

- versionamento oficial da WEBER;
- publicacao automatica;
- comunicacao externa sem revisao;
- regras tecnicas que nao estejam nas fontes;
- decisao final sobre onde publicar a base de conhecimento.

## Open Questions

- Qual sera o repositorio oficial da gestao de conhecimento WEBER?
- Quem aprova artigo tecnico antes da publicacao?
- Quem aprova artigo para cliente?
- Quais materiais sao internos e quais podem ser externos?
- O Weber Patches sera somente documento manual ou sera implementado em ferramenta interna?
- Existe taxonomia oficial de modulos, rotinas e publicos?

## Related

```text
.kora/context/source-inventory.md
.kora/skills/create-weber-knowledge-article.md
VERSAO 01_09_2026/README.md
VERSAO 01_09_2026/Markdown/template-wiki-tecnica-com-imagens.md
VERSAO 01_09_2026/Markdown/demanda-weber-patches.md
Projeto Wiki entrada de notas Recebe Fácil/entrada-de-notas-recebe-facil-contexto-completo.md
Projeto Wiki entrada de notas Recebe Fácil/01-preparacao-de-ambiente/revisado/wiki-preparacao-de-ambiente.md
```
