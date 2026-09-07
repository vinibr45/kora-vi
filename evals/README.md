# Evals

This directory contains KORA Core evaluation definitions and manual evaluation scenarios.

Evals assess quality, correctness, usefulness, safety, boundaries, and architectural fit.

In v0.7, evals are structured definitions and manual scenarios, not automated runners.

## Specification

```text
docs/evals/kora-evals-spec-v0.7.md
```

## Templates

```text
evals/templates/eval-template.md
evals/templates/eval-result-template.md
```

## Scenarios

```text
evals/scenarios/
```

## Results

```text
evals/results/
```

Store eval results only when they affect future decisions, learning, or quality baselines.

## Core Evaluation Definitions

- `browser-page-ux-readiness.md`: rubric for page and flow readiness after browser-based UX inspection across mobile, tablet and desktop.

## Manual Scenarios

- `scenarios/EV-0015-reviewed-image-generation-loop.md`: validates reviewed image generation, revision loops, approval checks, and organized project outputs.
- `scenarios/EV-0016-marketing-channel-integrations.md`: validates read-only marketing channel analysis, account boundaries, approval checks, and project-local storage.
