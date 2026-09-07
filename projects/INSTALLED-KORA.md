# Installed KORA Projects

This is the central registry of repositories where KORA is installed through a local `.kora/` binding.

Use this file to know which project repositories may need local documentation updates when KORA Core changes.

## Registry Rule

Every KORA-connected repository should be listed here.

Minimum required fields:

```text
project name
repository path
local binding path
local AGENTS.md path
installed KORA version
installation status
last checked date
update notes
```

## Installed Projects

### C de Certo

```text
Project: C de Certo
Repository Path: C:\c_de_certo
Local Binding: C:\c_de_certo\.kora\binding.md
Local KORA README: C:\c_de_certo\.kora\README.md
Local AGENTS.md: C:\c_de_certo\AGENTS.md
KORA Core Path: C:\KORA
Installed KORA Version: 1.4.0
Installation Status: installed and operational
Context Completeness: level-7
Last Checked: 2026-09-07
Core Registry: projects/c-de-certo/README.md
Update Notes: upgraded to installed-KORA usage pattern and registered in the central installed-project registry
```

### Marcos Dev

```text
Project: Marcos Dev
Repository Path: C:\marcbmrs.github.io
Local Binding: C:\marcbmrs.github.io\.kora\binding.md
Local KORA README: C:\marcbmrs.github.io\.kora\README.md
Local AGENTS.md: C:\marcbmrs.github.io\AGENTS.md
KORA Core Path: C:\KORA
Installed KORA Version: 1.4.0
Installation Status: installed and operational
Context Completeness: level-7
Last Checked: 2026-09-07
Core Registry: projects/marcos-dev/README.md
Update Notes: upgraded to installed-KORA usage pattern and registered in the central installed-project registry
```

### Marcar Hora

```text
Project: Marcar Hora
Repository Path: C:\agendado
Local Binding: C:\agendado\.kora\binding.md
Local KORA README: C:\agendado\.kora\README.md
Local AGENTS.md: C:\agendado\AGENTS.md
KORA Core Path: C:\KORA
Installed KORA Version: 1.4.0
Installation Status: installed
Context Completeness: level-4
Last Checked: 2026-09-07
Core Registry: projects/marcar-hora/README.md
Update Notes: initial KORA local binding installed and registered
```

### Retail Data Platform

```text
Project: Retail Data Platform
Repository Path: C:\retail-data-platform
Local Binding: C:\retail-data-platform\.kora\binding.md
Local KORA README: C:\retail-data-platform\.kora\README.md
Local AGENTS.md: C:\retail-data-platform\AGENTS.md
KORA Core Path: C:\KORA
Installed KORA Version: 1.4.0
Installation Status: installed and operational
Context Completeness: level-7
Last Checked: 2026-09-07
Core Registry: projects/retail-data-platform/README.md
Update Notes: upgraded to installed-KORA usage pattern and registered in the central installed-project registry
```

## Update Workflow

When KORA Core changes:

1. Review `VERSION.md` and `CHANGELOG.md`.
2. Check whether the change affects installed repositories.
3. For each affected repository listed here, inspect:

```text
<repo>\.kora\binding.md
<repo>\.kora\README.md
<repo>\AGENTS.md
```

4. Update local KORA docs only when the Core change changes usage, routing, governance, project flow, health checks, or templates.
5. Record a local decision when the update changes project behavior.
6. Update this registry's `Installed KORA Version`, `Last Checked`, and `Update Notes`.

## What Not To Store Here

- Secrets, tokens, credentials, or `.env` values.
- Student, customer, payment, or sensitive data.
- Full project strategy.
- Full local context that belongs in the project `.kora/` binding.

## Related

```text
skills/register-installed-kora-project.md
skills/check-installed-kora.md
skills/use-installed-kora.md
skills/maintain-kora-indexes.md
projects/PROJECT-FLOW.md
```
