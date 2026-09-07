# DR-0024: Uso da KORA instalada em outros repositorios

Status: accepted
Date: 2026-09-07
Scope: project-bindings-installed-kora
Owner: Marcos

## Context

KORA Core pode ser usada por outros repositorios por meio de uma camada local `.kora/`.

Esse modo precisa ser forte o bastante para que o usuario possa abrir um repositorio conectado e pedir trabalho normalmente, sem precisar mencionar KORA a cada pedido.

## Decision

KORA tera capacidades e templates especificos para uso em repositorios conectados:

```text
skills/use-installed-kora.md
skills/check-installed-kora.md
projects/templates/local-agents-template.md
projects/templates/local-kora-readme-template.md
```

Repositorios conectados devem ter uma `.kora/binding.md` e, quando util, um `AGENTS.md` local apontando para a KORA Core e para o contexto local.

## Reasoning

O projeto operacional deve continuar dono da sua realidade local, enquanto KORA Core oferece metodos reutilizaveis.

Essa separacao permite usar KORA em varios repositorios sem copiar a Core inteira e sem contaminar conhecimento global com detalhes de cliente, stack ou operacao local.

## Consequences

- Quando um repo tiver `.kora/binding.md`, o agente deve ler esse arquivo antes de assumir contexto.
- O agente deve preferir contexto local para trabalho do projeto.
- KORA Core deve ser usada como biblioteca de metodos reutilizaveis.
- Promocoes do local para Core exigem revisao.
- A instalacao pode ser checada com `skills/check-installed-kora.md`.
- O uso cotidiano pode ser orientado por `skills/use-installed-kora.md`.

## Related

```text
skills/use-installed-kora.md
skills/check-installed-kora.md
skills/setup-kora-project.md
skills/bind-project-to-kora.md
projects/PROJECT-FLOW.md
projects/templates/local-agents-template.md
projects/templates/local-kora-readme-template.md
```
