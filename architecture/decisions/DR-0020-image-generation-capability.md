# DR-0020: Capacidade global de geracao de imagem

Status: accepted
Date: 2026-09-05
Scope: tools-skills
Owner: Marcos

## Context

KORA deve poder apoiar projetos com criacao de imagens para conteudo, marketing, sites, campanhas, mockups e materiais visuais.

Essa capacidade pode servir a varios projetos, mas prompts, identidade visual, referencias, assets finais e aprovacao criativa geralmente dependem de cada projeto.

## Decision

KORA tera uma skill global `generate-image-asset` e uma tool definition global `image-generation`.

A skill define o processo de gerar ou propor assets de imagem. A tool representa a capacidade de geracao/edicao de imagem sem acoplar a KORA a um provedor especifico.

## Reasoning

Geração de imagem e uma capacidade reutilizavel, mas deve respeitar limites de projeto, marca, permissao, privacidade, direitos de uso e aprovacao humana.

## Consequences

- A skill global fica em `skills/generate-image-asset.md`.
- A tool global fica em `tools/image-generation.md`.
- Identidade visual e outputs especificos de projetos devem ficar no projeto local ou no `.kora/` local.
- Publicacao, agendamento, uso de contas externas, creditos pagos e edicao de imagens sensiveis exigem aprovacao.
- KORA continua independente de provedor especifico de imagem.
