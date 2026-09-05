# KORA Tools, Integrations, and Automations Specification v0.9

## 1. Purpose

This specification defines how KORA represents tools, integrations, and automations.

Tools execute capabilities. Integrations connect KORA to external systems. Automations run repeatable workflows with reduced human intervention.

The goal of v0.9 is to define contracts, permissions, approval points, and boundaries before implementing real connectors, scripts, or automation engines.

## 2. Definitions

### Tool

A tool is an executable or external capability that can be used by an agent, skill, or workflow.

Examples:

- filesystem access;
- browser;
- Git;
- GitHub;
- image generation;
- script;
- database command;
- test runner;
- API client.

### Integration

An integration connects KORA to an external system, account, API, service, MCP connector, plugin, or platform.

Examples:

- Instagram/Meta metrics;
- Google Drive;
- GitHub;
- calendar tools;
- email tools;
- design tools;
- analytics services;
- scheduling platforms.

### Automation

An automation is a repeatable workflow that can run with minimal human intervention after approval.

Examples:

- weekly content calendar generation;
- recurring Instagram performance report;
- scheduled project context review;
- release checklist;
- recurring eval run;
- lead follow-up workflow.

## 3. Core Rule

```text
Tools execute.
Integrations connect.
Automations repeat.
Orchestration permits and coordinates.
Humans approve important external effects.
```

## 4. What Tools Are Not

A tool is not:

- an agent role;
- a skill procedure;
- a knowledge article;
- an eval;
- a decision record;
- unrestricted permission;
- automatic approval to access external systems.

## 5. What Integrations Are Not

An integration is not:

- proof that access is available;
- permission to use an account;
- permission to spend money;
- permission to publish or modify external systems;
- a replacement for platform-specific rules or official documentation.

## 6. What Automations Are Not

An automation is not:

- a vague intention;
- an uncontrolled background agent;
- silent publishing;
- silent memory writing;
- silent source-of-truth modification;
- a reason to skip evals or approval.

## 7. Scope

Tools, integrations, and automations can be global, local, or hybrid.

### Global

Reusable across projects and stored in KORA Core.

```text
C:\KORA\tools\
C:\KORA\integrations\
C:\KORA\automations\
```

### Local

Specific to one project and stored in the local project binding.

```text
<project-repository>\.kora\tools\
<project-repository>\.kora\integrations\
<project-repository>\.kora\automations\
```

### Hybrid

Uses a reusable global pattern with local project configuration or adaptation.

## 8. Tool Contract

A tool definition should include:

- name;
- purpose;
- scope;
- status;
- owner;
- capability type;
- inputs;
- outputs;
- allowed callers;
- required permissions;
- safety constraints;
- failure modes;
- approval points;
- related skills;
- related agents;
- related evals.

## 9. Integration Contract

An integration definition should include:

- name;
- external system;
- purpose;
- scope;
- status;
- owner;
- access requirements;
- account/subscription requirements;
- data read/write behavior;
- permissions;
- rate limits or platform constraints, when known;
- official documentation/source requirements;
- approval points;
- security/privacy notes;
- fallback mode;
- related tools, skills, agents, evals, or automations.

## 10. Automation Contract

An automation definition should include:

- name;
- purpose;
- scope;
- status;
- owner;
- trigger;
- frequency;
- workflow steps;
- agents/skills/tools involved;
- inputs;
- outputs;
- external side effects;
- approval points;
- stop conditions;
- failure handling;
- evals;
- logging or result storage;
- memory/learning behavior.

## 11. Status

### proposed

Suggested but not approved.

### approved

Approved for implementation or controlled use.

### active

Available for normal use.

### paused

Temporarily disabled.

### deprecated

Should not be used for new workflows.

## 12. Permission Levels

KORA should classify tools, integrations, and automations by permission level.

### read-only

Can inspect or fetch information but cannot modify external systems.

### write-local

Can write only to local project files or approved local paths.

### write-external

Can modify external systems or services.

### publish

Can publish, send, schedule, deploy, or make information visible externally.

### spend

Can trigger paid usage, ads, subscriptions, API costs, or purchases.

Higher-risk permission levels require explicit approval.

## 13. Approval Policy

Human approval is required before:

- connecting external accounts;
- using paid subscriptions or spend-capable systems;
- publishing, scheduling, sending, or deploying;
- writing to external systems;
- creating recurring automations;
- storing credentials or sensitive data;
- changing memory or source-of-truth stores automatically;
- creating tools that can delete, move, overwrite, or expose data.

## 14. Fallbacks

Before building an integration, KORA should consider simpler modes:

```text
Manual input
Uploaded/exported files
Screenshots
CSV exports
Browser-assisted inspection
Local script
Read-only integration
Full integration
Automation
```

## 15. External Facts

Information about platform APIs, pricing, policies, limits, or account requirements may change.

When implementing real integrations, KORA should verify current official documentation before relying on platform behavior.

## 16. Relationship With Capability Management

Capability Router should decide whether a tool, integration, or automation is needed.

`create-capability` should delegate to specialized creation skills where available.

A capability plan should exist before creating significant integrations or automations.

## 17. Non-Goals For v0.9

Do not create:

- real external integrations;
- API clients;
- automation engine;
- scheduler;
- credential store;
- background workers;
- paid service usage;
- publishing workflows;
- deployment workflows.

v0.9 defines the model first.
