# release-kora-version

## Purpose

Update KORA version records when a change deserves versioning.

This skill writes or updates `VERSION.md` and `CHANGELOG.md` after `skills/assess-kora-version-impact.md` determines that the change is patch, minor, or major.

## When To Use

- When `assess-kora-version-impact` recommends a version update.
- When the user asks to close, tag, document, or release a KORA version.
- After meaningful KORA Core improvements that changed usage, routing, maintenance, health checks, capabilities, or architecture behavior.

## When Not To Use

- When version impact is `none`.
- When changes are local to a project and were not promoted to KORA Core.
- When the repository is in an unclear or partially failed state.
- When a major version bump is proposed but not approved.

## Inputs

- Version impact assessment.
- Current version.
- Target version.
- Date.
- Summary of changes.
- Related files.
- Related decisions.
- Health check status, if available.

## Process

1. Confirm the version impact:

```text
patch
minor
major
```

2. Determine target version from `VERSION.md` or the latest changelog entry.
3. Update `VERSION.md` with:

```text
current version
date
stage
status
summary
versioning policy
related files
```

4. Add a new top entry to `CHANGELOG.md` with:

```text
version
date
impact
added
changed
why it matters
related decisions
```

5. Run `skills/maintain-kora-indexes.md` if versioning added new discoverable capabilities or entry points.
6. Recommend `skills/check-kora-health.md` when the release affects routing, entry points, or maintenance behavior.
7. Report the version update clearly.

## Outputs

- Updated `VERSION.md`.
- Updated `CHANGELOG.md`.
- Release summary.
- Follow-up recommendation, if needed.

## Approval Points

Ask before:

- major version bumps;
- changing historical changelog entries;
- marking a proposed automation as active;
- announcing or publishing outside the repository.

## Boundaries

This skill records version state. It does not create git tags, commits, releases, or external announcements unless the user explicitly asks.

It should not inflate version numbers for trivial changes.

## Related

```text
skills/assess-kora-version-impact.md
skills/maintain-kora-indexes.md
skills/check-kora-health.md
VERSION.md
CHANGELOG.md
architecture/decisions/
```
