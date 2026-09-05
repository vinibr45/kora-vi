# Experiments

This directory stores KORA Core experiment definitions and templates.

Experiments test hypotheses. Learning decides what should persist.

In v0.8, experiments are structured records, not automated runners.

## Specification

```text
docs/learning/kora-experiments-learning-spec-v0.8.md
```

## Templates

```text
experiments/templates/experiment-template.md
experiments/templates/learning-record-template.md
```

## Boundary

Project-specific experiments should live in the project's local `.kora/experiments/` folder when they depend on local project context.
