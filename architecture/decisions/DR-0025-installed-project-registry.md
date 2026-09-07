# DR-0025: Registro central de repositorios com KORA instalada

Status: accepted
Date: 2026-09-07
Scope: project-bindings-installed-kora
Owner: Marcos

## Context

KORA pode ser instalada em outros repositorios por meio de uma camada local `.kora/`.

Quando KORA Core evolui, alguns desses repositorios podem precisar atualizar `AGENTS.md`, `.kora/binding.md`, `.kora/README.md`, templates locais, regras de uso ou documentos operacionais.

Sem um registro central, a KORA Core nao sabe quais projetos conectados existem nem onde eles estao no filesystem.

## Decision

KORA Core manterá um registro central em:

```text
projects/INSTALLED-KORA.md
```

Toda instalacao ou atualizacao relevante da KORA em outro repositorio deve registrar:

```text
project name
repository path
local binding path
local KORA README path
local AGENTS.md path
KORA Core path
installed KORA version
installation status
context completeness
last checked date
Core registry path
update notes
```

A skill `skills/register-installed-kora-project.md` define como criar ou atualizar esse registro.

## Reasoning

O registro central permite rastrear quais projetos usam KORA e quais podem precisar de atualização local depois de uma melhoria na Core.

Ele guarda apenas ponteiros e status, não contexto sensível nem detalhes completos do projeto.

## Consequences

- `setup-kora-project` e `bind-project-to-kora` devem atualizar `projects/INSTALLED-KORA.md`.
- `check-installed-kora` deve verificar se o projeto está no registro central.
- `use-installed-kora` deve consultar o registro quando estiver disponível.
- Melhorias futuras da KORA Core podem listar projetos afetados antes de propor atualizações locais.
- O registro não deve conter segredos, dados pessoais, dados de aluno, dados de pagamento ou contexto completo do projeto.

## Related

```text
projects/INSTALLED-KORA.md
skills/register-installed-kora-project.md
skills/setup-kora-project.md
skills/bind-project-to-kora.md
skills/check-installed-kora.md
skills/use-installed-kora.md
```
