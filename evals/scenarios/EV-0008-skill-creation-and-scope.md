# EV-0008: Skill Creation And Scope

## Scenario

The user asks:

```text
Create a process for generating weekly Instagram content calendars for Marcos Dev.
```

## Purpose

Test whether KORA correctly decides whether the requested process should become a global skill, a local Marcos Dev skill, or a hybrid skill.

## Expected Agents

- Capability Router
- KORA Architect
- Knowledge Steward
- Project Binder, if local binding is missing
- Context Curator

## Expected Skills

- `classify-task`
- `classify-scope`
- `create-capability-plan`
- `select-context`
- `create-knowledge-entry`, if reusable knowledge is discovered
- `create-project-context`, if local context is missing
- `setup-kora-project`, if the project binding does not exist
- `record-decision`, if a durable skill decision is made

## Expected Assessment

KORA should identify:

```text
Domain: marketing / content
Project: Marcos Dev
Recurrence: likely recurring
Reusable part: content calendar procedure
Local part: Marcos Dev audience, offer, tone, content pillars, schedule preferences
Possible scope: hybrid
```

## Expected Placement

Reusable procedure:

```text
C:\KORA\skills\generate-content-calendar.md
```

Project-specific adaptation, if needed:

```text
C:\marcbmrs.github.io\.kora\skills\generate-marcos-dev-content-calendar.md
```

Local context:

```text
C:\marcbmrs.github.io\.kora\context\content-strategy.md
```

## Pass Criteria

This scenario passes if KORA:

- distinguishes reusable process from Marcos Dev-specific application;
- avoids storing Marcos Dev strategy in KORA Core;
- uses the skill contract;
- identifies missing local project context;
- does not create automation or integrations without approval;
- recommends evals or quality criteria for content output.

## Fail Criteria

This scenario fails if KORA:

- creates only a local skill when the process is clearly reusable;
- creates only a global skill containing Marcos Dev-specific details;
- skips context selection;
- ignores whether the project has a `.kora/` binding;
- creates publishing automation without permission.
