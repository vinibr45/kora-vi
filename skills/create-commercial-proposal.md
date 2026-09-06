---
name: "create-commercial-proposal"
type: execution
scope: hybrid
status: draft
version: "0.1"
owner: "KORA Core"
domains:
  - documents-proposals
  - sales
  - marketing
related_agents:
  - agents/capability-router.md
  - agents/context-curator.md
related_skills:
  - skills/select-context.md
required_knowledge:
  - knowledge/documents-proposals/commercial-proposal-structure.md
  - knowledge/sales/consultative-sales-process.md
  - knowledge/marketing/offers/offer-clarity-checklist.md
required_tools: []
evals: []
created_at: 2026-09-05
updated_at: 2026-09-05
---

# Create Commercial Proposal

## Purpose

Create a clear commercial proposal from buyer context, discovery notes, offer information, scope, timeline, investment, assumptions, and next step.

## When To Use

- The user wants a proposal, quote document, scope of work, PDF proposal, or sales follow-up document.
- A discovery conversation needs to become a buyer-friendly recommendation.
- A project needs a reusable proposal structure.

## When Not To Use

- When the document is a legal contract requiring legal review.
- When there is not enough buyer context to recommend scope.
- When the user only needs a simple price line.

## Inputs

- Buyer or audience.
- Buyer situation.
- Problem or desired outcome.
- Offer or recommended solution.
- Scope and deliverables.
- Timeline.
- Investment or pricing logic.
- Responsibilities, assumptions, exclusions, and next step.
- Target format: Markdown, DOCX, PDF-ready source, or PDF.

## Process

1. Confirm the target project and scope.
2. Select relevant project context and offer context.
3. Identify missing proposal inputs.
4. Structure the proposal using the commercial proposal framework.
5. Translate service language into buyer outcome language.
6. Clarify scope, exclusions, assumptions, and next step.
7. Review against offer clarity and consultative sales principles.
8. Produce the requested format or a source ready for rendering.

## Outputs

- Proposal outline.
- Full proposal draft.
- Optional PDF-ready source.
- Optional follow-up message to send with the proposal.
- Notes about missing decisions or risks.

## Required Knowledge

- `knowledge/documents-proposals/commercial-proposal-structure.md`
- `knowledge/sales/consultative-sales-process.md`
- `knowledge/marketing/offers/offer-clarity-checklist.md`

## Optional Knowledge

- Brand voice.
- Positioning.
- Local project pricing rules.

## Required Tools

None by default.

## Optional Tools

- PDF generation tool.
- Document generation tool.
- Project file writer.

## Evals

Review for:

- buyer clarity;
- scope clarity;
- next step clarity;
- no unsupported promises;
- no confidential pricing leakage into KORA Core;
- legal or financial claims flagged when needed.

## Approval Points

Human approval is required before sending, publishing, signing, or treating the proposal as a legal document.

## Boundaries

This skill creates proposal drafts and structures. It does not provide legal advice, bind terms, or approve pricing.

## Related

- `knowledge/documents-proposals/commercial-proposal-structure.md`
- `knowledge/sales/consultative-sales-process.md`
