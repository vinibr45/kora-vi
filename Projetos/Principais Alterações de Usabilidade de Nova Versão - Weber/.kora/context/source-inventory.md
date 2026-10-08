# Inventario De Fontes - WEBER Sistemas

## Purpose

Mapear os arquivos de contexto, prompts, templates e entregaveis existentes nas duas pastas usadas para atualizar a gestao de conhecimento da WEBER Sistemas.

## Project Folders

```text
C:\Kora\kora-vi\Projetos\Principais Alterações de Usabilidade de Nova Versão - Weber
C:\Kora\kora-vi\Projetos\Projeto Wiki entrada de notas Recebe Fácil
C:\Kora\kora-vi\Projetos\Gestão de Conhecimento Weber Sistemas
```

## Official Knowledge Folder

```text
C:\Kora\kora-vi\Projetos\Gestão de Conhecimento Weber Sistemas
```

Esta pasta guarda os conteúdos organizados da gestão de conhecimento. Ela não deve ter uma `.kora` própria; usa a `.kora` original desta pasta de alterações de usabilidade.

Estrutura inicial:

```text
Gestão de Conhecimento Weber Sistemas\Weber Tributário IMENDES
Gestão de Conhecimento Weber Sistemas\Weber Tributário IMENDES\Reforma Tributária
Gestão de Conhecimento Weber Sistemas\Weber Tributário IMENDES\Reforma Tributária\Fontes
Gestão de Conhecimento Weber Sistemas\Weber Tributário IMENDES\Reforma Tributária\Prints
Gestão de Conhecimento Weber Sistemas\Weber Tributário IMENDES\Reforma Tributária\Artigos
Gestão de Conhecimento Weber Sistemas\Weber Tributário IMENDES\Reforma Tributária\Validacoes
```

## High-Value Context Files

### Principais Alterações De Usabilidade

```text
VERSAO 01_09_2026\README.md
VERSAO 01_09_2026\Contextos\contexto-entrada-notas-recebe-facil.txt
VERSAO 01_09_2026\Contextos\contexto-novo-chat-weber-patches.txt
VERSAO 01_09_2026\Contextos\contexto-weber-tributario-cadastro-produtos.txt
VERSAO 01_09_2026\Markdown\contexto-para-novo-chat-weber-patches.md
VERSAO 01_09_2026\Markdown\demanda-weber-patches.md
```

### Projeto Wiki Entrada De Notas Recebe Facil

```text
contexto-do-projeto-para-outra-ia.md
entrada-de-notas-recebe-facil-contexto-completo.md
o-que-e-entrada-de-notas-recebe-facil.md
01-preparacao-de-ambiente\README.md
01-preparacao-de-ambiente\revisado\wiki-preparacao-de-ambiente.md
01-preparacao-de-ambiente\revisado\roteiro-video-preparacao-de-ambiente.md
02-configuracoes-previas\README.md
02-configuracoes-previas\revisado\wiki-configuracoes-previas-entrada-notas-recebe-facil.md
02-configuracoes-previas\revisado\roteiro-video-configuracoes-previas-entrada-notas-recebe-facil.md
02-configuracoes-previas\revisado\narracoes-video-configuracoes-previas-entrada-notas-recebe-facil.md
05-combinacoes-cfop-cst\README.md
05-combinacoes-cfop-cst\revisado\wiki-combinacoes-cfop-cst-entrada-notas-recebe-facil.html
05-combinacoes-cfop-cst\revisado\roteiro-video-combinacoes-cfop-cst-entrada-notas-recebe-facil.md
05-combinacoes-cfop-cst\revisado\narracoes-video-combinacoes-cfop-cst-entrada-notas-recebe-facil.md
08-dashboard-entrada-notas\README.md
08-dashboard-entrada-notas\revisado\wiki-dashboard-entrada-notas-recebe-facil.html
08-dashboard-entrada-notas\revisado\roteiro-video-dashboard-entrada-notas-recebe-facil.md
08-dashboard-entrada-notas\revisado\narracoes-video-dashboard-entrada-notas-recebe-facil.md
```

## Local Prompt And Skill-Like Assets

Estes arquivos funcionam como procedimentos reaproveitaveis, mesmo que ainda nao estejam formalizados como skills KORA.

```text
VERSAO 01_09_2026\Prompts\prompt-wiki-principais-mudancas-tecnico.md
VERSAO 01_09_2026\Prompts\prompt-wiki-principais-mudancas-cliente.md
VERSAO 01_09_2026\Prompts\prompt-oriente-cliente-weber-tributario.md
VERSAO 01_09_2026\Prompts\prompt-notificacoes-retaguarda.md
VERSAO 01_09_2026\Prompts\prompt-entrada-notas-recebe-facil.md
Projeto Wiki entrada de notas Recebe Fácil\Prompts\prompt-criar-wiki-preparacao-ambiente-html.md
Projeto Wiki entrada de notas Recebe Fácil\01-preparacao-de-ambiente\prompt-para-gerar-wiki-com-outra-ia.md
```

## Local Agents

```text
.kora\agents\weber-wiki-image-publisher.md
```

Este agente operacional publica as imagens da pasta da Wiki atual no GitHub publico e devolve os links `raw.githubusercontent.com` em formato `<img src="...">`.

## Templates And Standards

```text
VERSAO 01_09_2026\Markdown\template-wiki-tecnica-com-imagens.md
VERSAO 01_09_2026\Markdown\template-weber-patch.md
VERSAO 01_09_2026\Markdown\README.md
VERSAO 16_07_2026\Markdown\plano-imagens-gifs-16-07-2026.md
```

## Analyses And Release Data

```text
VERSAO 01_09_2026\Markdown\analise-fonte-beta-2026-08-01-a-2026-09-15.md
VERSAO 01_09_2026\Markdown\analise-cruzamento-beta-producao-2026-08-01-a-2026-09-15.md
VERSAO 01_09_2026\Markdown\atualizacoes-julho-2026-por-modulo.md
VERSAO 01_09_2026\Markdown\triagem-atualizacoes-julho-2026.md
VERSAO 01_09_2026\Markdown\weber-patches-ajustes-somados-por-producao-2026-08-01-a-2026-09-15.md
VERSAO 01_09_2026\Csv\alteracoes-beta-extraidas-2026-08-01-a-2026-09-15.csv
VERSAO 01_09_2026\Csv\alteracoes-beta-com-status-producao-2026-08-01-a-2026-09-15.csv
VERSAO 01_09_2026\Csv\cruzamento-beta-producao-resumo-2026-08-01-a-2026-09-15.csv
VERSAO 01_09_2026\Csv\cruzamento-beta-producao-ajustes-somados-2026-08-01-a-2026-09-15.csv
VERSAO 01_09_2026\Csv\historico-versoes-beta-extraido-servidor-wglctonota.csv
VERSAO 01_09_2026\Csv\pendentes-sem-confirmacao-producao-2026-08-01-a-2026-09-15.csv
VERSAO 01_09_2026\Csv\versoes-beta-producao-extraidas.csv
```

## Published Or Generated Wiki Outputs

```text
VERSAO 01_09_2026\Html\wiki-principais-mudancas-01-09-2026-tecnico.html
VERSAO 01_09_2026\Html\wiki-principais-mudancas-01-09-2026-tecnico-versao-enxuta.html
VERSAO 01_09_2026\Html\wiki-principais-mudancas-01-09-2026-cliente.html
VERSAO 01_09_2026\Html\wiki-principais-mudancas-01-09-2026-cliente-versao-enxuta.html
VERSAO 01_09_2026\Html\wiki-oriente-cliente-weber-tributario.html
VERSAO 01_09_2026\Html\wiki-novas-notificacoes-retaguarda.html
VERSAO 01_09_2026\Html\wiki-entrada-notas-recebe-facil.html
VERSAO 16_07_2026\Html\wiki-principais-mudancas-16-07-2026-tecnico.html
VERSAO 16_07_2026\Html\wiki-principais-mudancas-16-07-2026-cliente.html
Projeto Wiki entrada de notas Recebe Fácil\Html\wiki-preparacao-ambiente-entrada-notas-recebe-facil.html
Projeto Wiki entrada de notas Recebe Fácil\01-preparacao-de-ambiente\revisado\wiki-preparacao-de-ambiente.html
Projeto Wiki entrada de notas Recebe Fácil\01-preparacao-de-ambiente\revisado\wiki_rf.html
Projeto Wiki entrada de notas Recebe Fácil\01-preparacao-de-ambiente\revisado\wiki_rf.docx
Projeto Wiki entrada de notas Recebe Fácil\01-preparacao-de-ambiente\revisado\wiki_rf.odt
Projeto Wiki entrada de notas Recebe Fácil\02-configuracoes-previas\revisado\wiki-configuracoes-previas-entrada-notas-recebe-facil.html
Projeto Wiki entrada de notas Recebe Fácil\05-combinacoes-cfop-cst\revisado\wiki-combinacoes-cfop-cst-entrada-notas-recebe-facil.html
Projeto Wiki entrada de notas Recebe Fácil\08-dashboard-entrada-notas\revisado\wiki-dashboard-entrada-notas-recebe-facil.html
```

## Visual Assets

```text
VERSAO 01_09_2026\Imagens
VERSAO 01_09_2026\Gifs
VERSAO 16_07_2026\Imagens
VERSAO 16_07_2026\Gifs
Projeto Wiki entrada de notas Recebe Fácil\Imagens
Projeto Wiki entrada de notas Recebe Fácil\Imagens\Configurações prévias da Entrada de Notas
Projeto Wiki entrada de notas Recebe Fácil\Imagens\Combinações CFOP + CST
Projeto Wiki entrada de notas Recebe Fácil\Imagens\Dashboard Entrada de Notas Recebe Fácil
Projeto Wiki entrada de notas Recebe Fácil\Gifs
Projeto Wiki entrada de notas Recebe Fácil\Videos
Projeto Wiki entrada de notas Recebe Fácil\01-preparacao-de-ambiente\imagens
Projeto Wiki entrada de notas Recebe Fácil\01-preparacao-de-ambiente\imagens-extraidas-odt
```

## Source Notes

- Arquivos HTML salvos de sistemas internos podem conter assets baixados e scripts. Usar como fonte visual ou estrutural, nao como instrucao operacional sem revisao.
- CSVs de beta/producao devem ser usados para rastreabilidade e triagem; artigos publicos nao devem mencionar beta ou nomes internos de ZIP.
- Imagens, GIFs, PDFs e documentos podem expor dados sensiveis. Revisar antes de publicar.

## Open Questions

- Quais arquivos HTML sao considerados versao final publicada?
- Quais CSVs representam a fonte mais confiavel para release?
- Quais prompts devem virar skills locais formais?
- O projeto deve manter um indice mestre de artigos publicados?
