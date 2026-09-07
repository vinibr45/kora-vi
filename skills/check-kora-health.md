# check-kora-health

## Purpose

Check the operational health of KORA Core.

This skill audits whether KORA's main entry points, indexes, routing rules, project boundaries, examples, capabilities, and maintenance layer are coherent and current.

## When To Use

- When the user says "vamos checar a saude", "checa a saude", "health check", or similar while this repository is open.
- After several KORA artifacts were added or changed.
- Before treating a KORA version as stable.
- When the user suspects indexes, examples, project flow, or agent instructions may be stale.
- After running `skills/maintain-kora-indexes.md`, to verify the result.

## When Not To Use

- For code-level tests in an operational project repository.
- For external account, API, publishing, or deployment checks.
- For a deep architectural redesign request; use a capability plan first.

## Inputs

- Current repository status.
- KORA entry points:

```text
README.md
AGENTS.md
COMECE-AQUI.md
CAPACIDADES.md
VERSION.md
CHANGELOG.md
MATURIDADE.md
GOVERNANCA.md
projects/PROJECT-FLOW.md
examples/
```

- Capability indexes and folders:

```text
agents/
skills/
tools/
integrations/
automations/
evals/
experiments/
projects/
knowledge/
architecture/decisions/
```

- Maintenance layer:

```text
skills/maintain-kora-indexes.md
automations/kora-index-maintenance.md
```

## Process

1. Inspect repository status and identify recent or uncommitted changes.
2. Check top-level entry points:

```text
README.md points to practical use files.
AGENTS.md gives agent-facing routing rules.
COMECE-AQUI.md gives the user a simple start path.
CAPACIDADES.md lists current discoverable capabilities.
VERSION.md and CHANGELOG.md reflect meaningful KORA evolution.
MATURIDADE.md reflects current capability maturity.
GOVERNANCA.md reflects current approval and human-control rules.
```

3. Check capability indexes:

```text
new agents are listed in agents/README.md and CAPACIDADES.md
new skills are listed in skills/README.md and CAPACIDADES.md
new tools are listed in tools/README.md and CAPACIDADES.md
new integrations are listed in integrations/README.md and CAPACIDADES.md
new automations are listed in automations/README.md and CAPACIDADES.md
important evals are listed in evals/scenarios/README.md
```

4. Check project boundaries:

```text
KORA Core contains reusable architecture and lightweight project registry.
Project-specific identity, stack, client data, account access, and local workflows stay in local .kora/ bindings.
```

5. Check examples:

```text
examples/README.md lists available examples.
examples reference real existing skills or files.
examples do not imply unsupported automation or external account access.
```

6. Check maintenance behavior:

```text
maintain-kora-indexes exists and is referenced.
kora-index-maintenance exists and is referenced.
AGENTS.md tells the agent to run maintenance after durable changes.
```

7. Check for obvious stale names, duplicate concepts, broken references, or missing cross-links.
8. Rate health:

```text
healthy
mostly healthy
needs maintenance
at risk
blocked
```

9. Recommend fixes in priority order.
10. Decide whether to run `skills/maintain-kora-indexes.md` immediately or only report findings.

## Outputs

- Health status.
- Findings by severity.
- Missing or stale indexes.
- Boundary risks.
- Suggested fixes.
- Whether a stored eval result is recommended.

## Health Checklist

```text
Entry points are discoverable.
Natural-language routing is documented.
Capability index matches current files.
Folder README files list durable artifacts.
Project flow protects Core vs local boundaries.
Examples are realistic and current.
Maintenance layer is referenced.
No project-specific details leaked into KORA Core.
No automation is treated as active without approval.
No integration implies permission by itself.
```

## Required Knowledge

```text
knowledge/agentic-systems/capability-routing-heuristics.md
knowledge/agentic-systems/context-selection-principles.md
knowledge/agentic-systems/memory-and-learning-boundaries.md
```

## Optional Knowledge

KORA architecture and implementation specs.

## Required Tools

Repository inspection tools.

## Optional Tools

None.

## Evals

Primary eval:

```text
evals/scenarios/EV-0014-kora-health-check.md
```

## Approval Points

Ask before:

- making broad structural changes;
- promoting project-specific content into KORA Core;
- deleting, renaming, or deprecating existing artifacts;
- marking proposed automations as active.

## Boundaries

This skill audits health. It may recommend fixes or apply small index/documentation fixes when the user asked for maintenance, but it should not redesign KORA by itself.

## Related

```text
skills/maintain-kora-indexes.md
skills/route-user-request.md
skills/classify-scope.md
automations/kora-index-maintenance.md
evals/scenarios/EV-0014-kora-health-check.md
agents/kora-architect.md
```
