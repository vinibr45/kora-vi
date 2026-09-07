# Example: Connect A Project

## User Request

```text
Conecta o repositorio do novo site da minha empresa a KORA.
```

## KORA Route

```text
skills/route-user-request.md
skills/setup-kora-project.md
skills/bind-project-to-kora.md
projects/PROJECT-FLOW.md
```

## Expected Handling

1. Identify the operational repository path.
2. Create or review the local `.kora/` binding.
3. Add minimal local context files.
4. Add only a lightweight registry entry in KORA Core.
5. Keep project-specific reality in the project repository.

## Scope Decision

```text
Project registry -> KORA Core projects/
Project identity, stack, audience, offers -> project .kora/context/
Product code -> project repository
```

## Realistic Follow-Up

```text
Agora cria o contexto inicial desse projeto com identidade, stack e objetivos.
```
