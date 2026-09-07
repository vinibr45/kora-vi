# Example: Installed KORA In Another Repository

## User Request

```text
Cria uma proposta para esse cliente.
```

The current repository is not KORA Core, but it contains:

```text
.kora/binding.md
AGENTS.md
```

## KORA Route

```text
skills/use-installed-kora.md
skills/check-installed-kora.md, if installation health is uncertain
skills/select-context.md
skills/create-commercial-proposal.md
skills/check-approval-needed.md
```

## Expected Handling

1. Read local `.kora/binding.md`.
2. Identify project identity, local context, and KORA Core path.
3. Select local project context first.
4. Use KORA Core proposal skill as the reusable method.
5. Keep client-specific details and final output in the project repository.
6. Recommend promotion to KORA Core only if a reusable proposal pattern appears.

## Scope Decision

```text
Proposal method -> KORA Core
Client details -> local .kora/ or project output
Final proposal -> project repository or output folder
Reusable improvement -> review before promoting to KORA Core
```

## Realistic Follow-Up

```text
Isso que fizemos aqui deveria virar uma skill global ou uma skill local?
```
