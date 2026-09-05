# Manual Evaluation Scenarios

This directory contains manual evaluation scenarios for KORA v0.1.

These scenarios test whether KORA's initial agents and skills make good architectural decisions before executable automation exists.

## Scenario Index

- `EV-0001-instagram-analysis.md`: analyze an Instagram profile and recommend content direction.
- `EV-0002-content-calendar.md`: generate a weekly content calendar for a project.
- `EV-0003-project-binding.md`: connect a repository to KORA through a local `.kora/` binding.
- `EV-0004-software-build.md`: plan capabilities for building an application with technical risk.
- `EV-0005-learning-promotion.md`: decide whether feedback or an outcome should become memory, knowledge, decision, or capability improvement.

## Manual Pass Criteria

A scenario passes when KORA correctly identifies:

- relevant agents;
- relevant skills;
- required context;
- global versus local scope;
- missing capabilities;
- execution mode;
- approval points;
- eval or learning needs.
