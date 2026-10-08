# WEBER Sistemas - Gestao de Conhecimento

## Project

Name: WEBER Sistemas - Gestao de Conhecimento
Type: local knowledge-management workspace
Status: active context consolidation
Repository Path: C:\Kora\kora-vi\Projetos\Principais Alterações de Usabilidade de Nova Versão - Weber
KORA Core Path: C:\Kora\kora-vi
Local KORA README: C:\Kora\kora-vi\Projetos\Principais Alterações de Usabilidade de Nova Versão - Weber\.kora\README.md
Local AGENTS.md: not created yet
Context Completeness: level-4

## Purpose

Organizar o contexto, os prompts, os padroes editoriais e os materiais de wiki da WEBER Sistemas para apoiar a atualizacao da gestao de conhecimento da empresa.

Esta binding conecta as fontes operacionais e a pasta oficial de conteúdo da gestão de conhecimento:

```text
C:\Kora\kora-vi\Projetos\Principais Alterações de Usabilidade de Nova Versão - Weber
C:\Kora\kora-vi\Projetos\Projeto Wiki entrada de notas Recebe Fácil
C:\Kora\kora-vi\Projetos\Gestão de Conhecimento Weber Sistemas
```

## Primary Domains

- knowledge management;
- product documentation;
- support enablement;
- UX communication;
- release communication;
- training content.

## Local Owns

- contexto especifico da WEBER Sistemas;
- regras editoriais da wiki de versao;
- materiais do modulo Entrada de Notas Recebe Facil;
- fluxo Weber Patches;
- pasta oficial de conteúdo `Gestão de Conhecimento Weber Sistemas`;
- inventario de fontes dos dois projetos;
- prompts e procedimentos locais para gerar artigos, roteiros e materiais de treinamento;
- cuidados locais com dados sensiveis em prints, videos e textos.

## Uses From KORA Core

- `skills/route-user-request.md`;
- `skills/classify-task.md`;
- `skills/classify-scope.md`;
- `skills/maintain-kora-indexes.md`;
- `projects/PROJECT-FLOW.md`;
- `projects/templates/project-binding-template.md`;
- `projects/templates/project-context-template.md`.

## Installed KORA Behavior

Quando esta pasta estiver aberta, o agente deve:

```text
1. Ler .kora/binding.md primeiro.
2. Usar .kora/context/ como fonte local da realidade da WEBER.
3. Consultar as pastas-fonte e a pasta `Gestão de Conhecimento Weber Sistemas` antes de gerar novo conhecimento.
4. Manter detalhes da WEBER nesta camada local, nao em KORA Core.
5. Usar KORA Core apenas para metodos reutilizaveis.
6. Pedir aprovacao antes de publicar, acionar sistemas externos ou promover conhecimento local para Core.
7. Tratar prints, videos e documentos como potenciais fontes sensiveis.
```

## Local Context Files

```text
.kora/context/weber-knowledge-management-context.md
.kora/context/weber-sistemas-context.md
.kora/context/source-inventory.md
```

## Local Capabilities

```text
.kora/skills/create-weber-knowledge-article.md
.kora/skills/criar-demandas-weber.md
.kora/agents/weber-wiki-image-publisher.md
```

## Boundaries

Nao armazenar aqui:

- credenciais, tokens ou senhas;
- dados reais de clientes sem necessidade;
- CNPJ real quando nao for essencial;
- valores sensiveis;
- informacoes fiscais privadas;
- decisoes comerciais que ainda nao foram validadas;
- regras reutilizaveis de KORA Core sem revisao de escopo.

## Missing Context

- Definir onde a gestao de conhecimento final sera publicada alem da pasta local: wiki interna, sistema IOS, documentacao HTML, Word/PDF ou outro local.
- Confirmar responsaveis por revisao tecnica, revisao de suporte e aprovacao final.
- Confirmar quais materiais podem ser publicados para clientes e quais devem ficar internos.
- Criar um `AGENTS.md` local se este projeto passar a ser usado recorrentemente.

## Notes

Esta binding foi criada para consolidar o material existente e permitir que a KORA ajude a transformar os arquivos dispersos em base de conhecimento operavel.
