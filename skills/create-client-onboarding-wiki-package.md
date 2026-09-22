---
name: "create-client-onboarding-wiki-package"
type: execution
scope: global
status: active
version: "0.1"
owner: "KORA Core"
domains: ["documentation", "customer-success", "training", "operations"]
related_agents: []
related_skills: ["classify-task", "classify-scope", "check-approval-needed", "maintain-kora-indexes"]
required_knowledge: []
required_tools: []
evals: []
created_at: 2026-09-10
updated_at: 2026-09-10
---

# Create Client Onboarding Wiki Package

## Purpose

Create a complete client-facing onboarding package for a product, module, feature, or workflow, pairing one short video per screen/process with a matching written wiki page.

This skill helps KORA transform a loose briefing, topic list, screen list, or implementation schedule into organized instructional material for first-time users.

## When To Use

- When a client needs to learn a tool, module, or workflow from zero.
- When each screen or process needs its own video and written wiki article.
- When the material must explain prerequisites, setup, execution, monitoring, and common follow-up actions.
- When a documentation effort has a deadline, daily production window, owners, blockers, and linked tasks.
- When a product team, support team, customer success team, or implementation team needs consistent wiki/video structure.

## When Not To Use

- When the request is only to answer one support question.
- When the user only needs a short internal note, not a full training package.
- When product behavior is unknown and no source material, screenshots, demo environment, or subject-matter input is available.
- When the material will include sensitive customer data, credentials, production financial data, or private documents that should not be stored in KORA Core.
- When the task is to publish, email, upload, or schedule content in an external system without explicit approval.

## Inputs

- Product, module, or workflow name.
- Target audience and experience level.
- List of screens, flows, topics, and expected outcomes.
- Required prerequisites and configuration steps.
- Demo environment status and sample data plan.
- Recording tool and setup constraints.
- Wiki platform or target format, if known.
- Video naming pattern, duration target, and narration style, if known.
- Schedule, deadlines, available production window, responsible people, and escalation contacts.
- Existing screenshots, recordings, notes, scripts, support cases, or product documentation.

## Process

1. Classify the documentation package:

```text
audience -> first-time client | internal support | implementation | mixed
scope -> full module | one screen | one workflow | release update
output -> wiki only | video only | video + wiki | checklist + wiki + video
risk -> low | medium | high
```

2. Protect project boundaries:

```text
Reusable structure -> KORA Core method
Product-specific wiki content -> project/local documentation
Customer data, credentials, screenshots, private examples -> local project or approved destination only
```

3. Convert the briefing into a documentation map:

```text
Section 1: product overview and value
Section 2: required setup before first use
Section 3: operating workflow
Section 4: monitoring, review, and management
Section 5: audit, statistics, exceptions, and maintenance
```

4. Turn each screen or process into a content unit with:

```text
ID
title
audience
goal
prerequisites
demo data needed
video objective
wiki objective
step-by-step outline
validation points
common errors or doubts
estimated effort
deadline
status
blockers
owner
reviewer
```

5. Build a production schedule around the available work window.

For each day or deadline, define the realistic output for the reserved time block. If the user provides a daily work window, treat it as a hard capacity constraint and avoid planning more work than can reasonably fit.

6. Prepare the recording environment checklist:

```text
recording tool configured
microphone and audio checked
screen resolution standardized
notifications disabled
test database or clean environment available
sample company configured
sample suppliers available
sample products available
sample documents available
no private customer data visible
repeatable reset procedure documented
```

7. Produce a script template for each video:

```text
opening: what the user will learn
context: when this screen/process is used
prerequisites: what must already be configured
demonstration: step-by-step action
validation: how to know it worked
exceptions: what to check if something is missing or wrong
closing: next screen/process in the learning path
```

8. Produce a wiki template for each article:

```text
title
objective
who should use this article
before you start
step-by-step
what to check before confirming
expected result
common problems
related articles
related video
last reviewed date
```

9. Define a review checklist before marking each item complete:

```text
client-first language
no internal-only assumptions
steps match the recorded screen
prerequisites are explicit
screenshots or video references are clear
expected result is stated
edge cases and blockers are captured
no sensitive data is exposed
next article/video is linked
```

10. Manage blockers:

If any blocker threatens the deadline, record:

```text
blocked item
reason
impact on schedule
decision needed
person to notify
latest safe notification time
proposed workaround
```

Then prepare a concise escalation message for the managers or stakeholders defined in the project briefing.

## Suggested Recebe Facil Topic Map

Use this as an example when the product is Recebe Facil or another invoice-entry workflow. Keep the final content in the project documentation, not in KORA Core.

```text
01 - Recording environment preparation
02 - Required configuration before invoice entry
03 - Invoice entry module parameters
04 - Permissions for invoice entry and analysis
05 - CFOP + CST combinations
06 - Company financial settings
07 - Product overview and guided commercial demo
08 - Entry control dashboard
09 - Invoices available for entry
10 - Assisted invoice entry
11 - Entry with products and conversions already configured
12 - Entry with products created by GTIN
13 - Product association and conversion
14 - Posted invoices and audit
15 - Suppliers pending review
16 - Products pending review
17 - CT-e 57 import, linking, and allocation
18 - CFOP analysis
19 - Supplier entry statistics
20 - Purchased product ranking
21 - Product association by supplier
22 - Purchase price variations
```

## Outputs

- Documentation map.
- Topic-by-topic wiki/video backlog.
- Recording environment checklist.
- Video script template.
- Wiki article template.
- Daily production plan based on available capacity.
- Blocker and escalation control.
- Review checklist for each completed wiki/video pair.

## Required Knowledge

None by default. Use project-specific product documentation, support notes, screenshots, recordings, and subject-matter input when available.

## Optional Knowledge

- Product onboarding principles.
- Technical documentation standards.
- Customer success enablement patterns.
- Support case patterns related to the documented module.

## Required Tools

None by default.

## Optional Tools

- Screen recorder, such as OBS or the approved company recording tool.
- Wiki editor or documentation platform.
- Task manager used by the team.
- Screenshot or annotation tool.
- Approved AI transcription or summarization tool, if allowed by the project.

## Evals

Apply these quality checks manually before delivery:

```text
First-time user can understand the goal without internal help.
Prerequisites are clear before the operational steps begin.
Video and wiki describe the same flow in the same order.
The expected result is visible or verifiable.
No private, customer-specific, credential-like, or production financial data appears.
Each article links to the previous and next relevant step.
Blockers and missing topics are converted into explicit tasks.
```

## Approval Points

Ask for explicit approval before:

- using customer or production data in videos, screenshots, or wiki pages;
- publishing, uploading, sending, or scheduling final material in an external system;
- connecting to external tools, accounts, plugins, APIs, or storage;
- changing official source-of-truth product documentation;
- activating recurring automations around task creation, reminders, or escalation.

Small local drafts, outlines, scripts, checklists, and wiki text requested by the user do not require separate approval.

## Boundaries

- This skill creates documentation structure and draft instructional material. It does not certify fiscal, accounting, legal, or tax correctness.
- Do not store client-specific data, credentials, production screenshots, or private business rules in KORA Core.
- Do not assume product behavior that has not been demonstrated, provided, or verified by the user.
- Do not replace stakeholder review when the content affects customer onboarding, financial entry, stock, tax, or audit processes.
- Do not create an autonomous publishing or escalation workflow without approval.

## Related

```text
skills/classify-task.md
skills/classify-scope.md
skills/check-approval-needed.md
skills/maintain-kora-indexes.md
knowledge/operations/workflow-design-principles.md
```
