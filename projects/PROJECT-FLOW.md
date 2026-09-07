# Project Flow

Este guia explica como projetos devem se conectar e trabalhar com a KORA.

## Ideia Central

```text
KORA Core define a arquitetura.
O projeto define a realidade local.
```

KORA Core deve guardar capacidades reutilizaveis. Um projeto deve guardar identidade, contexto, decisoes, memoria, regras locais e capacidades especificas.

## Quando Criar Um Projeto

Crie ou registre um projeto quando houver:

```text
repositorio operacional
cliente ou negocio especifico
produto especifico
contexto proprio
decisoes locais
rotinas recorrentes
necessidade de memoria por projeto
```

## Onde Cada Coisa Mora

```text
projects/<nome>/README.md
```
Registro leve do projeto dentro da KORA Core.

```text
<repositorio-do-projeto>/.kora/binding.md
```
Conexao local entre o projeto e a KORA.

```text
<repositorio-do-projeto>/.kora/README.md
```
Entrada local para explicar como a KORA funciona dentro daquele projeto.

```text
<repositorio-do-projeto>/AGENTS.md
```
Instrucoes para o agente reconhecer a instalacao local e usar KORA sem o usuario repetir o contexto.

```text
<repositorio-do-projeto>/.kora/context/
```
Contexto real do projeto: identidade, stack, publico, oferta, operacao, estrategia e restricoes.

```text
<repositorio-do-projeto>/.kora/skills/
```
Procedimentos recorrentes especificos do projeto.

```text
<repositorio-do-projeto>/.kora/agents/
```
Papeis especificos do projeto quando uma skill nao basta.

```text
<repositorio-do-projeto>/.kora/memory/
```
Aprendizados e memoria local do projeto.

```text
<repositorio-do-projeto>/.kora/decisions/
```
Decisoes locais de produto, negocio, operacao, arquitetura ou estrategia.

## Fluxo De Conexao

1. Identifique o projeto e o repositorio operacional.
2. Use `skills/setup-kora-project.md` para preparar o fluxo.
3. Use `skills/bind-project-to-kora.md` para criar ou revisar a camada `.kora/`.
4. Crie ou atualize `AGENTS.md` local com `projects/templates/local-agents-template.md`.
5. Crie `.kora/README.md` com `projects/templates/local-kora-readme-template.md`.
6. Crie contexto minimo em `.kora/context/`.
7. Registre apenas um resumo leve em `projects/<nome>/README.md`.
8. Registre ou atualize a instalacao em `projects/INSTALLED-KORA.md`.
9. Rode `skills/check-installed-kora.md` para validar a instalacao.
10. Crie skills, agentes, ferramentas, evals ou automacoes locais somente quando tarefas reais justificarem.
11. Rode ou registre evals quando a conexao precisar de garantia de qualidade.

## Fluxo De Trabalho Diario

Quando estiver dentro de um projeto conectado:

```text
1. Leia .kora/binding.md.
2. Leia AGENTS.md local quando existir.
3. Selecione o contexto local minimo.
4. Use skills/use-installed-kora.md para decidir Core vs local.
5. Use capacidades globais da KORA quando forem suficientes.
6. Crie capacidade local apenas para rotinas especificas daquele projeto.
7. Registre aprendizados locais em .kora/memory/.
8. Promova para KORA Core somente quando o aprendizado for reutilizavel em varios projetos.
```

## Exemplos

```text
"Cria uma proposta para cliente X"
-> a proposta e output ou contexto local; a estrutura reutilizavel fica na skill global.

"Nosso site usa Astro e Cloudflare"
-> isso pertence ao contexto local do projeto, nao a KORA Core.

"Toda proposta deve ter uma secao de riscos e proximos passos"
-> se vale para varios projetos, pode virar conhecimento ou skill global.

"Todo post desse cliente precisa seguir tom institucional"
-> regra local no .kora/context/ do projeto.
```

## Erros Comuns

- Colocar detalhes do cliente dentro da KORA Core.
- Criar agente local antes de existir uma rotina clara.
- Criar automacao antes de estabilizar o processo manual.
- Promover aprendizado local sem revisar evidencia e reutilidade.
- Esquecer que codigo de produto mora no repositorio do produto.

## Arquivos Relacionados

```text
projects/README.md
projects/INSTALLED-KORA.md
projects/templates/project-binding-template.md
projects/templates/project-context-template.md
projects/templates/project-registry-entry-template.md
skills/setup-kora-project.md
skills/bind-project-to-kora.md
skills/register-installed-kora-project.md
skills/use-installed-kora.md
skills/check-installed-kora.md
skills/classify-scope.md
projects/templates/local-agents-template.md
projects/templates/local-kora-readme-template.md
```
