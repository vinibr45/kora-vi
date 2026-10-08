# create-weber-knowledge-article

## Purpose

Criar ou revisar um artigo, roteiro ou material de treinamento da WEBER Sistemas usando os contextos locais da KORA.

## When To Use

- Quando o usuario pedir para criar artigo de wiki da WEBER.
- Quando o usuario pedir para transformar uma alteracao tecnica em explicacao para suporte ou cliente.
- Quando o usuario pedir para atualizar gestao de conhecimento da WEBER.
- Quando o usuario pedir material do Recebe Facil.
- Quando o usuario pedir Weber Patch por data de release.
- Quando houver prompt antigo nas pastas e for melhor transformar em procedimento consistente.

## Inputs

- Pedido do usuario.
- `.kora/binding.md`.
- `.kora/context/weber-knowledge-management-context.md`.
- `.kora/context/source-inventory.md`.
- Arquivo fonte da alteracao, modulo, tutorial, CSV, HTML, prompt, print ou GIF.
- Publico-alvo: interno, tecnico, suporte, implantacao, cliente ou usuario final.

## Process

1. Identifique o tipo de entrega:

```text
wiki de versao
Weber Patch
wiki/tutorial do Recebe Facil
roteiro de video
orientacao para suporte
checklist
resumo para cliente
```

2. Selecione somente as fontes necessarias no inventario.
3. Confirme o nome correto de produtos, modulos e rotinas.
4. Separe informacao publica de rastreabilidade interna.
5. Nao mencione beta, ZIP, DLL ou executavel no texto para cliente.
6. Quando houver dado tecnico bruto, traduza para impacto operacional.
7. Marque como `precisa confirmar` qualquer comportamento nao comprovado.
8. Planeje imagens, GIFs ou prints no ponto exato do fluxo em que ajudam a explicar.
9. Crie sempre um `Índice` no início de qualquer artigo de Wiki WEBER estruturado, antes da primeira seção de conteúdo.
10. Inclua resultado esperado, alertas e checklist quando for tutorial.
11. Revise riscos de exposicao de dados sensiveis.
12. Nao inclua secao `Proximo passo` em artigos de Wiki WEBER.
13. Quando houver video relacionado, trate-o como um unico link do video completo, nao como marcadores de video por etapa.
14. Quando o usuario pedir para gerar HTML de Wiki WEBER ou Recebe Facil e houver prints/imagens locais relacionados ao artigo, inclua tambem a publicacao dessas imagens no GitHub publico do usuario, salvo se ele disser o contrario.
15. Para imagens publicadas no GitHub, entregue os links em formato HTML pronto para incorporar no corpo da Wiki:

```html
<img src="https://raw.githubusercontent.com/<usuario>/<repositorio>/<branch>/<caminho-da-imagem>.png">
```

16. Siga o padrao ja usado no projeto quando aplicavel:

```text
wiki-assets/weber/<slug-da-wiki>/imagens/<arquivo>
```

17. Antes de publicar imagens, use somente a pasta de imagens relacionada ao artigo atual. Nao publique imagens de outras etapas, materiais temporarios, folhas de contato ou arquivos gerados apenas para apoio, a menos que o usuario peca.
18. Se o repositorio, branch ou slug de destino nao estiver claro, prefira o padrao existente do projeto `vinibr45/kora-vi`, branch `master`, em `wiki-assets/weber/<slug-da-wiki>/imagens/`, e informe o caminho usado.
19. Quando essa publicacao de imagens fizer parte da entrega, use o agente local `.kora/agents/weber-wiki-image-publisher.md` como referencia operacional para selecionar a pasta correta, publicar apenas os assets da Wiki atual e devolver os links embedded.
20. Em artigos HTML de Wiki WEBER, nao incluir a linha ou rotulo `Arquivo sugerido:` antes ou depois dos placeholders de imagem. Use apenas o placeholder `[imagem x]`, o embed real quando ja houver link publicado, e a descricao do que a imagem demonstra.

## Output Structure For Version Wiki

```text
Titulo da pagina:
Principais Mudancas - Versao DD.MM.AAAA

Titulo da mudanca:
[Nome amigavel] - [Modulo ou rotina]

Índice:

O que mudou?

Pontos afetados:

[Imagem inicial recomendada]

Como usar / liberar / validar / orientar?

Passo a passo:

[Imagens no fluxo]

IMPORTANTE:

Contexto adicional:

Exemplos, se fizer sentido:

Resumo:

Artigo tecnico / rastreabilidade interna:
```

## Output Structure For Recebe Facil Tutorial

```text
Titulo:

Objetivo:

Pre-requisitos:

Informacoes necessarias:

Procedimento operacional:

Resultado esperado:

Checklist de conferencia:

Possiveis duvidas:
```

## Quality Checklist

- [ ] O publico-alvo esta claro.
- [ ] O texto esta simples, didatico e profissional.
- [ ] O material nao inventa comportamento.
- [ ] O nome `Entrada de Notas Recebe Facil` foi usado corretamente.
- [ ] Detalhes internos ficaram separados da explicacao principal.
- [ ] Itens sem confirmacao foram marcados como pendentes.
- [ ] Prints, GIFs ou imagens foram planejados.
- [ ] Dados sensiveis foram evitados ou sinalizados para revisao.
- [ ] Existe orientacao pratica para tecnico, suporte ou cliente.

## Boundaries

Esta skill local nao publica material, nao acessa sistemas externos e nao aprova conteudo sozinha.

Publicacao, envio ao cliente ou uso de dados reais exige revisao humana.
