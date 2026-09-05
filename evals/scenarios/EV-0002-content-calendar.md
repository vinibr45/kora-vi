# EV-0002: Weekly Content Calendar

## Scenario

The user asks:

```text
Generate a posting calendar for this week for project X.
```

## Purpose

Test whether KORA can determine whether to execute directly, use existing content capabilities, create a reusable skill, use image generation, propose scheduling integration, or suggest automation.

## Expected Agents

- Capability Router
- Context Curator
- Knowledge Steward
- Project Binder, if project X is not connected to KORA

Possible future domain agents:

- Content Strategist
- Visual Direction Agent
- Social Media Operations Agent

## Expected Skills

- `classify-task`
- `select-context`
- `create-capability-plan`
- `classify-scope`
- `bind-project-to-kora`, only if no binding exists
- `promote-learning`, after user feedback or performance data

## Expected Capability Assessment

KORA should identify:

```text
Domain: marketing / content
Project: project X
Required local context: audience, positioning, offer, tone, content goals
Reusable knowledge: marketing, content strategy, copywriting
Possible tools: image generation, design tools, spreadsheet, scheduler, browser
Possible integration: social scheduling platform, Meta tools, calendar tool, MCP/plugin if available
Execution mode: manual, assisted, tool-supported, integrated, or automated
```

## Expected Decision Behavior

KORA should offer options when the automation level is unclear:

```text
Option A: Generate manually from available context.
Option B: Use/create a content calendar skill.
Option C: Add image brief generation.
Option D: Add design/image generation workflow.
Option E: Add scheduling/publishing integration.
Option F: Design recurring automation.
```

## Expected Scope Behavior

Generic content calendar method should belong in KORA Core.

Project-specific calendar, brand tone, offers, post decisions, and performance learnings should belong in the local `.kora/` binding.

## Pass Criteria

This scenario passes if KORA:

- identifies whether project X has a KORA binding;
- requests or selects project-specific context;
- does not over-automate prematurely;
- distinguishes content planning from publishing automation;
- identifies possible missing capabilities;
- recommends global or local placement correctly.

## Fail Criteria

This scenario fails if KORA:

- creates a generic calendar without project context;
- creates automations before asking about accounts, subscriptions, permissions, or desired workflow;
- stores project-specific strategy in KORA Core;
- ignores image or design workflow needs when requested.
