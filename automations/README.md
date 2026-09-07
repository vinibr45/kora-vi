# Automations

This directory stores KORA Core automation definitions and templates.

Automations are repeatable workflows that may later run with reduced human intervention after approval.

In v0.9, automations are definitions, not active background jobs.

## Specification

```text
docs/tools/kora-tools-integrations-automations-spec-v0.9.md
```

## Template

```text
automations/templates/automation-template.md
```

## Core Automation Definitions

- `claude-design-file-generation.md`: generate design files with Claude after approved visual workflow setup.
- `kora-index-maintenance.md`: keep KORA indexes, entry points, examples, and project flow documentation aligned with repository changes.
- `reviewed-image-generation-loop.md`: generate, review, revise, and organize image assets through an approved provider workflow.
- `marketing-channel-health-snapshot.md`: read authorized marketing channels and summarize health, opportunities, risks, and data quality.
