# Example: Version Governance

## User Request

```text
Melhorei a KORA criando uma nova camada de manutencao. Isso merece versao?
```

## KORA Route

```text
skills/route-user-request.md
skills/maintain-kora-indexes.md
skills/assess-kora-version-impact.md
skills/release-kora-version.md
```

## Expected Handling

1. Inspect what changed.
2. Decide whether the change is temporary, patch, minor, or major.
3. If it is patch, minor, or major, update `VERSION.md` and `CHANGELOG.md`.
4. Record a decision if the change affects future governance.
5. Run or recommend a health check if routing, entry points, maintenance, or versioning behavior changed.

## Scope Decision

```text
Version policy -> KORA Core
Project release history -> local project .kora/ or project repository
Git tags or external releases -> only if explicitly requested
```

## Realistic Follow-Up

```text
Fecha uma versao nova e resume o que mudou.
```
