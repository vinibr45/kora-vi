---
name: "create-sales-follow-up"
type: execution
scope: hybrid
status: draft
version: "0.1"
owner: "KORA Core"
domains:
  - sales
  - marketing
related_agents:
  - agents/context-curator.md
related_skills:
  - skills/select-context.md
required_knowledge:
  - knowledge/sales/consultative-sales-process.md
  - knowledge/marketing/offers/offer-clarity-checklist.md
  - knowledge/marketing/branding/brand-voice-principles.md
required_tools: []
evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Create Sales Follow Up

## Purpose

Create clear follow-up messages after a sales conversation, proposal, lead form, WhatsApp inquiry, or stalled opportunity.

## When To Use

- A lead has not responded.
- A proposal was sent and needs follow-up.
- A sales conversation needs a summary and next step.
- A buyer raised an objection that should be answered clearly.

## When Not To Use

- When follow-up would violate consent, platform rules, or relationship boundaries.
- When the buyer has clearly declined.
- When the message requires legal, financial, or sensitive claims.

## Inputs

- Buyer context.
- Conversation summary.
- Offer or proposal context.
- Current stage.
- Main objection or pending decision.
- Desired next step.
- Brand voice.
- Channel: WhatsApp, email, DM, CRM note, or call script.

## Process

1. Identify the buyer's stage and likely decision barrier.
2. Choose the message goal: clarify, summarize, remind, answer objection, or ask for decision.
3. Use buyer language and a single clear next step.
4. Keep the tone aligned with brand voice and relationship context.
5. Avoid pressure, false urgency, or unsupported promises.
6. Produce one primary message and optional variations.

## Outputs

- Follow-up message.
- Optional short and long variants.
- Optional objection-specific response.
- Optional internal CRM note.

## Required Knowledge

- `knowledge/sales/consultative-sales-process.md`
- `knowledge/marketing/offers/offer-clarity-checklist.md`
- `knowledge/marketing/branding/brand-voice-principles.md`

## Optional Knowledge

- Project-specific offer.
- Project-specific tone of voice.
- Proposal or pricing context.

## Required Tools

None by default.

## Optional Tools

- CRM integration.
- Email or messaging integration.

## Evals

Review for:

- clear next step;
- respectful tone;
- correct buyer context;
- no false urgency;
- no unsupported claims;
- channel fit.

## Approval Points

Human approval is required before sending messages through external systems.

## Boundaries

This skill drafts follow-ups. It does not send messages, change CRM records, or make binding promises without approval.

## Related

- `knowledge/sales/consultative-sales-process.md`
- `knowledge/documents-proposals/commercial-proposal-structure.md`
