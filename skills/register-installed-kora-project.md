# register-installed-kora-project

## Purpose

Register or update a project repository in KORA Core's installed-project registry.

This skill ensures KORA Core knows which external repositories have KORA installed, where they live, and whether they may need local updates after KORA Core changes.

## When To Use

- Every time KORA is installed in a new project repository.
- After updating a project's local `.kora/` binding, `.kora/README.md`, or `AGENTS.md`.
- After KORA Core changes in a way that may affect installed repositories.
- When the user asks which projects currently have KORA installed.
- When checking whether installed repositories need upgrades.

## When Not To Use

- For repositories that do not use KORA.
- For temporary folders or one-off outputs.
- For project-specific details that should remain in the local `.kora/` binding.

## Inputs

- Project name.
- Project repository path.
- Local `.kora/binding.md` path.
- Local `.kora/README.md` path, if present.
- Local `AGENTS.md` path, if present.
- KORA Core path.
- Installed KORA version.
- Installation status.
- Context completeness.
- Last checked date.
- Core registry path.
- Update notes.

## Process

1. Check whether `projects/INSTALLED-KORA.md` exists.
2. If it does not exist, create it with the installed-project registry format.
3. Check whether the project is already listed.
4. Add or update the project entry with:

```text
Project
Repository Path
Local Binding
Local KORA README
Local AGENTS.md
KORA Core Path
Installed KORA Version
Installation Status
Context Completeness
Last Checked
Core Registry
Update Notes
```

5. Keep the entry lightweight. Do not duplicate local project context.
6. If KORA Core changes may affect installed projects, identify which listed projects need review.
7. Update `projects/README.md` when this registry becomes a main project entry point.

## Outputs

- Updated `projects/INSTALLED-KORA.md`.
- Installed project entry.
- List of projects needing local update, when relevant.
- Boundary warning if sensitive or local-only data appears.

## Approval Points

Ask before:

- writing to an external project repository;
- changing local project behavior;
- removing a project from the installed registry;
- promoting local project details into KORA Core.

## Boundaries

This registry stores pointers and status only.

It must not store secrets, account details, private data, customer/student/payment data, or full local project context.

## Related

```text
projects/INSTALLED-KORA.md
skills/setup-kora-project.md
skills/bind-project-to-kora.md
skills/check-installed-kora.md
skills/use-installed-kora.md
projects/PROJECT-FLOW.md
```
