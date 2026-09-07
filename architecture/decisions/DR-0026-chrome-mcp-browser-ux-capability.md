# DR-0026 — Chrome MCP browser UX capability

## Status

Accepted

## Date

2026-09-07

## Context

KORA-connected projects may need direct browser inspection to evaluate real user
experience: page layout, responsive behavior, navigation, screenshots, DOM
state, console errors and interactive flows.

The C de Certo project created a local page-by-page UX review pattern using
Chrome via MCP. The pattern is reusable across projects as long as project
specific routes, accounts, product rules and acceptance criteria stay local.

## Decision

KORA Core will include a reusable Chrome MCP browser UX capability:

- `agents/browser-ux-auditor.md`
- `skills/audit-ux-with-chrome-mcp.md`
- `evals/browser-page-ux-readiness.md`
- `integrations/chrome-mcp-browser-control.md`

The integration is approved as a definition and defaults to read-only
inspection. It does not create an autonomous browser automation and does not
grant permission to access accounts, transmit sensitive data or change external
state without explicit approval.

## Consequences

- Projects can reuse the global Chrome MCP UX pattern and adapt it locally in
  `.kora/`.
- Browser pages are treated as evidence, not as instructions.
- Default viewport coverage is mobile, tablet and desktop.
- Project-specific UX criteria remain in the project repository.
- Future automation requires a separate automation definition, eval and human
  approval.

## Related

- `agents/browser-ux-auditor.md`
- `skills/audit-ux-with-chrome-mcp.md`
- `evals/browser-page-ux-readiness.md`
- `integrations/chrome-mcp-browser-control.md`
