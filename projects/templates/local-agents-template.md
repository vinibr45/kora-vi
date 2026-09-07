# AGENTS.md Template For KORA-Connected Projects

Use this template as the starting point for:

```text
<project-repository>/AGENTS.md
```

## Project Agent Instructions

This repository is an operational project connected to KORA.

Before using KORA capabilities, read:

```text
.kora/binding.md
```

The binding points to KORA Core and defines what this project owns locally.

## Default Behavior

When the user asks for work in this repository, assume the work is project-local unless they explicitly ask to improve KORA Core.

Use this order:

```text
1. Read .kora/binding.md.
2. Select the smallest relevant local .kora/context/ files.
3. Use local .kora/ capabilities when project-specific.
4. Use KORA Core capabilities when reusable.
5. Keep project details inside this repository.
6. Promote reusable patterns to KORA Core only after review.
```

## Core Vs Local Rule

```text
Reusable method -> KORA Core
Project identity, stack, audience, client data, decisions -> local .kora/
Product/source code -> project repository
Secrets and credentials -> never store in KORA Core or .kora/
```

## Natural Requests

These requests should use the local KORA binding:

```text
Vamos rodar o dia.
Tive uma ideia.
Isso esta repetitivo.
Vamos checar a saude.
Precisa de aprovacao?
Cria uma proposta.
Registra esse aprendizado.
Cria uma skill local.
Isso deveria ir para a KORA Core?
```

## Approval Rules

Ask before:

```text
changing KORA Core
promoting local content to KORA Core
connecting external accounts
publishing, sending, scheduling, or deploying
spending money or using paid credits
storing sensitive data
activating automations
deleting or renaming durable artifacts
```

## KORA Core Reference

KORA Core path:

```text
<fill from .kora/binding.md>
```

Important Core files:

```text
AGENTS.md
COMECE-AQUI.md
CAPACIDADES.md
GOVERNANCA.md
skills/use-installed-kora.md
skills/check-installed-kora.md
projects/PROJECT-FLOW.md
```
