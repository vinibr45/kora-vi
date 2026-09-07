# assess-kora-version-impact

## Purpose

Decide whether KORA changes deserve a new version.

This skill evaluates the impact of improvements, maintenance, fixes, capability changes, project-flow changes, and architecture decisions before updating `VERSION.md` or `CHANGELOG.md`.

## When To Use

- After durable improvements to KORA Core.
- After `skills/maintain-kora-indexes.md` runs for meaningful changes.
- After adding, removing, renaming, or materially changing agents, skills, tools, integrations, automations, evals, examples, project flow, entry points, or architecture decisions.
- Before releasing or documenting a new KORA version.
- When the user asks whether a change deserves versioning.

## When Not To Use

- For temporary notes, drafts, generated outputs, or local project-only changes.
- For small wording edits that do not affect behavior, routing, structure, capability discovery, or user workflow.
- For changes inside an operational project repository unless they alter KORA Core or a reusable KORA pattern.

## Inputs

- Summary of changes.
- Current `git status` and relevant diffs.
- Current `VERSION.md`, if present.
- Current `CHANGELOG.md`, if present.
- Related decisions, skills, automations, evals, and entry points.

## Process

1. Identify changed artifact types:

```text
entry point
agent
skill
tool
integration
automation
eval
project flow
example
knowledge
decision
documentation
```

2. Classify impact:

```text
none
patch
minor
major
```

3. Use these rules:

```text
none -> typo, formatting, wording, non-durable note, local-only unpromoted change
patch -> small clarification, index correction, link fix, non-breaking documentation fix
minor -> new capability, new workflow, new entry point, new eval, new maintenance rule, backward-compatible architecture improvement
major -> breaking folder structure change, changed source-of-truth rule, incompatible scope rule, removed core capability, major architecture reset
```

4. Identify whether version files should change:

```text
none -> no version update
patch/minor/major -> update VERSION.md and CHANGELOG.md
```

5. Identify whether a decision record is needed.
6. If versioning is justified, recommend `skills/release-kora-version.md`.
7. Explain the reasoning in one short version-impact summary.

## Outputs

- Version impact classification.
- Recommended next version, if any.
- Reasoning.
- Files that should be updated.
- Whether to run `skills/release-kora-version.md`.

## Versioning Rules

KORA uses semantic-style versioning for the architecture state:

```text
MAJOR.MINOR.PATCH
```

Interpretation:

```text
MAJOR -> incompatible architecture or source-of-truth changes
MINOR -> new backward-compatible capability, workflow, eval, or entry point
PATCH -> clarification, correction, index fix, small documentation update
```

## Approval Points

Ask for human approval before:

- publishing or announcing a version externally;
- marking unstable work as a stable version;
- making a major version change;
- rewriting version history.

## Boundaries

This skill assesses impact. It does not update version files by itself unless paired with `skills/release-kora-version.md`.

Do not version every tiny edit. Versioning should preserve meaningful evolution, not create noise.

## Related

```text
skills/release-kora-version.md
skills/maintain-kora-indexes.md
skills/check-kora-health.md
automations/kora-index-maintenance.md
VERSION.md
CHANGELOG.md
architecture/decisions/
```
