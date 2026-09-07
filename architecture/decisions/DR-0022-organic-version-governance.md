# DR-0022: Governanca organica de versionamento da KORA

Status: accepted
Date: 2026-09-07
Scope: versioning-governance
Owner: Marcos

## Context

KORA passou a ter uma camada de manutencao organica para manter indices, pontos de entrada, exemplos e guias alinhados com mudancas duraveis.

Com esse crescimento, tambem e necessario decidir quando uma melhoria merece nova versao, para evitar tanto historico insuficiente quanto versionamento ruidoso para pequenas edicoes.

## Decision

KORA tera uma camada de governanca organica de versionamento composta por:

```text
skills/assess-kora-version-impact.md
skills/release-kora-version.md
VERSION.md
CHANGELOG.md
```

Depois de melhorias duraveis, a KORA deve avaliar impacto de versao. Se a mudanca for `patch`, `minor` ou `major`, a KORA deve atualizar `VERSION.md` e `CHANGELOG.md` usando `release-kora-version`.

## Reasoning

Versionamento deve acompanhar a evolucao real da arquitetura, mas nao deve ser acionado para qualquer typo ou nota temporaria.

A decisao de impacto separa:

```text
none -> sem versionamento
patch -> correcao ou esclarecimento pequeno
minor -> nova capacidade ou workflow compativel
major -> mudanca incompativel de arquitetura ou fonte da verdade
```

## Consequences

- `VERSION.md` passa a ser a fonte atual do estado versionado da KORA.
- `CHANGELOG.md` passa a preservar historico de mudancas significativas.
- `maintain-kora-indexes` deve considerar versionamento quando a mudanca for duravel.
- `AGENTS.md` deve instruir o agente a avaliar impacto de versao apos melhorias relevantes.
- Major versions exigem aprovacao explicita.
- Versionamento nao cria git tags, commits, releases externos ou publicacao sem pedido explicito.

## Related

```text
skills/assess-kora-version-impact.md
skills/release-kora-version.md
skills/maintain-kora-indexes.md
VERSION.md
CHANGELOG.md
```
