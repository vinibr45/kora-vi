# Capability Management

Capability Management is responsible for deciding what kind of capability is needed for a task.

A capability may be:

- direct execution;
- an agent;
- a skill;
- a tool;
- an integration;
- an automation;
- an eval;
- a knowledge module;
- a memory entry;
- a decision record.

## Core Questions

For each meaningful task, KORA should ask:

```text
Can this be executed directly?
Does an existing capability already fit?
Is the task likely to repeat?
Does it require specialization?
Should the capability be global or local?
Does it require a tool or integration?
Does it require evaluation?
Should the result become memory or a decision?
```

## Scope Rule

```text
Reusable across projects -> KORA Core
Specific to one project -> local .kora binding
Published/runtime code -> project repository
```

## Creation Rule

KORA should not create agents, skills, tools, or automations just because it can.

New capabilities should be created when at least one condition is true:

- the task is recurring;
- the task requires a specialized role;
- the process needs consistency;
- quality criteria need to be reusable;
- a tool or integration would materially reduce repeated work;
- the capability can serve more than one project;
- local project complexity justifies a project-specific capability.

Important structural changes should be proposed or approved, not silently created.

## Capability Discovery

Before executing a task that may involve repeatable business work, KORA should inspect the available capability layers:

```text
1. Global KORA capabilities
2. Local project capabilities
3. Existing tools and integrations
4. Available external services or subscriptions
5. Missing capabilities
```

Example questions:

```text
Do we already have a content calendar skill?
Do we already have a content strategist agent?
Do we already have an image generation workflow?
Do we have an automation for scheduling or publishing?
Do we have access to external services that could be integrated?
Is an MCP connector, API, script, or manual workflow the right path?
```

## Execution Modes

KORA should distinguish between execution modes before building new complexity:

```text
Manual
The user provides inputs and KORA produces the output without integration.

Assisted
KORA uses existing knowledge, agents, skills, or local files, but the user still handles external steps.

Tool-Supported
KORA uses scripts, local tools, files, browser actions, or available integrations.

Integrated
KORA connects to external systems through approved APIs, MCP connectors, plugins, or other controlled integrations.

Automated
KORA runs a repeatable workflow with minimal human intervention, subject to approval and safety rules.
```

## User Choice Points

When more than one execution mode is reasonable, KORA should present options instead of assuming the most complex path.

For example, for a weekly content calendar:

```text
Option A: Generate the calendar manually from current context.
Option B: Use existing local project context and reusable marketing skills.
Option C: Add image generation workflow.
Option D: Add scheduling/publishing integration.
Option E: Design a recurring automation.
```

KORA should ask about subscriptions, available accounts, permissions, and desired automation level before proposing integrations that depend on external services.

## Content Calendar Example

Task:

```text
Generate a posting calendar for this week for project X.
```

Capability Management should check:

```text
Project: Which project is X?
Domain: marketing / content / social media
Existing global knowledge: marketing, content strategy, copywriting
Existing global skills: content calendar, post ideation, image briefing
Existing local context: audience, positioning, offers, tone, services
Existing local skills: project-specific content formats or recurring campaigns
Existing tools: image generation, design tools, spreadsheet, scheduler, browser
Missing capabilities: agent, skill, eval, tool, integration, automation
Execution mode: manual, assisted, tool-supported, integrated, or automated
Approval needed: integration, publishing, account access, recurring automation
```

The output should not only be the calendar. When relevant, KORA should also report whether a reusable capability should be created or improved.

## Domain Capability Packs

KORA should be able to reason by domain. When a task belongs to a domain such as software engineering, marketing, finance, operations, product, sales, or design, Capability Management should identify which domain capabilities may be needed.

A domain capability pack is not necessarily a concrete folder or package in v0.1. It is an architectural grouping of likely knowledge, agents, skills, tools, evals, and safety checks for a domain.

## Software Engineering Example

Task:

```text
Build or modify an application for project X.
```

Capability Management should inspect:

```text
Project type: site, app, internal tool, automation, API, system, dashboard
Stack: HTML, CSS, JavaScript, Python, Django, PHP, database, hosting, etc.
Risk: security, privacy, payments, authentication, data loss, performance, accessibility
Existing local context: product goals, users, brand, UX rules, deployment rules
Existing global knowledge: software engineering, UX, accessibility, security, testing
Existing capabilities: agents, skills, tools, evals, scripts, templates
Missing capabilities: stack-specific security review, UX review, testing workflow, deployment checklist
```

Possible capabilities:

```text
Security reviewer for the relevant stack
UX reviewer for the interface type
Frontend implementation skill
Accessibility checklist
Performance checklist
Testing skill
Deployment review skill
Database migration review skill
Code review eval
```

KORA should not create all of these automatically. It should choose the capabilities justified by the project type, risk, stack, and task recurrence.

For example, a simple static landing page may need UX, accessibility, performance, and copy review. A system with login, payments, or private data may need security, privacy, auth, data model, and deployment review capabilities.

## Local Capability Layer

Project-specific capabilities should live in the project binding, not in KORA Core.

KORA Core should remain clean and reusable. It may define patterns, templates, global knowledge, reusable agents, reusable skills, reusable tools, and reusable evals.

A project binding should own capabilities that depend on that project's identity, stack, market, audience, services, clients, operational rules, or local repository structure.

Examples:

```text
Global reusable skill -> C:\KORA\skills\
Global reusable agent -> C:\KORA\agents\
Global reusable knowledge -> C:\KORA\knowledge\

Marcos Dev-specific skill -> C:\marcbmrs.github.io\.kora\skills\
Marcos Dev-specific agent -> C:\marcbmrs.github.io\.kora\agents\
Marcos Dev-specific memory -> C:\marcbmrs.github.io\.kora\memory\
Marcos Dev-specific decision -> C:\marcbmrs.github.io\.kora\decisions\
```

Before creating a capability, KORA should classify it:

```text
Global: reusable across projects
Local: useful only for this project
Hybrid: local adaptation of a global template or pattern
```

Hybrid capabilities may reference KORA Core but should store project-specific details locally.

## Capability Plan Template

For complex, recurring, risky, ambiguous, or capability-changing tasks, use:

```text
orchestration/templates/capability-plan-template.md
```

A capability plan should be created before adding new agents, skills, tools, integrations, automations, evals, memory, or decisions unless the user explicitly requests the change and the scope is already clear.
