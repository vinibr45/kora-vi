---
name: "review-service-response"
type: review
scope: hybrid
status: draft
version: "0.1"
owner: "KORA Core"
domains:
  - customer-service
related_agents:
  - agents/context-curator.md
related_skills:
  - skills/select-context.md
required_knowledge:
  - knowledge/customer-service/service-recovery-framework.md
required_tools: []
evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Review Service Response

## Purpose

Review or draft a customer service response for clarity, empathy, ownership, next action, and service recovery quality.

## When To Use

- A customer complaint, delay, confusion, or support issue needs a response.
- The user wants to improve the tone or usefulness of a support message.
- A business needs a service recovery template.

## When Not To Use

- When the issue requires legal, medical, safety, financial, or compliance review.
- When account-specific private information is missing.
- When the correct action depends on technical investigation.

## Inputs

- Customer issue summary.
- Current draft response, if any.
- Known facts.
- What the business can do next.
- Deadline or expected update time.
- Channel and tone requirements.

## Process

1. Identify the customer's experience and practical problem.
2. Separate known facts from assumptions.
3. Check whether the response acknowledges, clarifies, owns, resolves, and prevents.
4. Remove blame, vagueness, overpromising, and empty apology.
5. Produce an improved response with a clear next action.

## Outputs

- Reviewed response.
- Improved response draft.
- Notes about missing facts or escalation needs.

## Required Knowledge

- `knowledge/customer-service/service-recovery-framework.md`

## Optional Knowledge

- Project-specific tone of voice.
- Support policy.
- SLA or escalation rules.

## Required Tools

None by default.

## Optional Tools

- CRM or helpdesk integration.

## Evals

Review for empathy, factual accuracy, clear next step, appropriate ownership, and no unsupported promises.

## Approval Points

Human approval is required before sending the response to the customer.

## Boundaries

This skill does not resolve the issue inside external systems or make compensation decisions without approval.

## Related

- `knowledge/customer-service/service-recovery-framework.md`
