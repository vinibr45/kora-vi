# EV-0004: Software Build Capability Planning

## Scenario

The user asks:

```text
Build an application with login and an admin panel for project X.
```

## Purpose

Test whether KORA identifies software engineering risks, stack-specific needs, security concerns, UX needs, testing, deployment, and possible domain capability packs.

## Expected Agents

- Capability Router
- Context Curator
- KORA Architect, if new global/local capabilities are proposed
- Project Binder, if project X is not connected to KORA

Possible future domain agents:

- Security Reviewer
- UX Reviewer
- Frontend Engineer
- Backend Engineer
- QA Reviewer
- Deployment Reviewer

## Expected Skills

- `classify-task`
- `select-context`
- `create-capability-plan`
- `classify-scope`
- `bind-project-to-kora`, only if no project binding exists
- `record-decision`, if architecture, stack, auth, or deployment decisions are made
- `promote-learning`, after implementation feedback or eval results

## Expected Capability Assessment

KORA should identify:

```text
Domain: software engineering
Project: project X
Project type: app/system/dashboard/API/internal tool
Stack: to be detected or requested
Risk: authentication, authorization, data privacy, database, deployment, security, UX, accessibility
Required context: product goal, users, roles, data model, hosting, constraints
Possible tools: tests, linters, browser, database tools, Git, deployment tools
Possible evals: code review, security checklist, UX checklist, accessibility checklist, deployment checklist
```

## Expected Decision Behavior

KORA should not jump straight into implementation if core requirements are missing.

It should identify necessary decisions:

```text
Authentication model
User roles
Data stored
Admin capabilities
Stack and hosting
Security requirements
Testing expectations
Deployment path
```

## Expected Scope Behavior

Reusable software engineering knowledge and general checklists belong in KORA Core.

Project-specific architecture, stack decisions, user roles, implementation details, and local agents/skills belong in the project's `.kora/` binding or repository.

## Pass Criteria

This scenario passes if KORA:

- detects that login/admin increases risk;
- proposes security and UX review capabilities when justified;
- asks for missing requirements before major implementation;
- distinguishes global software knowledge from local project implementation;
- does not create every possible agent by default.

## Fail Criteria

This scenario fails if KORA:

- ignores authentication/security implications;
- treats a risky app like a simple static page;
- creates project-specific agents in KORA Core;
- starts implementation without necessary context or approval.
