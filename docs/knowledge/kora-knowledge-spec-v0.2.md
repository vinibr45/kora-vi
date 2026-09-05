# KORA Knowledge Specification v0.2

## 1. Purpose

This specification defines how KORA stores reusable knowledge.

KORA knowledge must be:

- modular;
- reusable across projects;
- readable by humans;
- selectable by agents;
- structured enough for future automation;
- separated from project-specific context and memory.

The goal of v0.2 is not to create a large knowledge base. The goal is to define the standard that future knowledge entries should follow.

## 2. Knowledge Definition

In KORA, knowledge is reusable information that can help multiple projects or tasks.

Examples:

- marketing principles;
- positioning frameworks;
- software engineering practices;
- UX heuristics;
- sales methods;
- security checklists;
- finance concepts;
- research summaries.

Knowledge is not:

- project identity;
- client-specific facts;
- temporary task context;
- raw conversation history;
- unreviewed personal preference;
- local repository implementation detail.

## 3. Source Of Truth Boundary

KORA Core knowledge belongs in:

```text
knowledge/
```

Project-specific application belongs in the local project binding:

```text
<project>/.kora/context/
<project>/.kora/memory/
<project>/.kora/decisions/
```

Rule:

```text
KORA knows the principle.
The project knows how the principle applies locally.
```

Example:

```text
KORA knowledge:
A strong offer clarifies audience, problem, transformation, mechanism, scope, proof, and next step.

Marcos Dev context:
The current offer is website creation for small businesses that need a trustworthy digital presence and WhatsApp leads.
```

## 4. Format

KORA uses Markdown as the initial knowledge format.

When useful, knowledge entries should use YAML frontmatter for structured metadata.

A knowledge entry should prefer this shape:

```markdown
---
title: ""
type: concept | framework | checklist | playbook | research-note | example | principle
domain: ""
subdomain: ""
status: draft | active | deprecated
version: "0.1"
evidence_level: low | medium | high | mixed | not_applicable
sources: []
related: []
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
---

# Title

## Summary

## Core Idea

## When To Use

## When Not To Use

## How To Apply

## Examples

## Limitations

## Sources

## Related
```

Not every section is mandatory for every entry. KORA should preserve usefulness over bureaucracy.

## 5. Knowledge Types

### Concept

Explains one idea.

Example: positioning, conversion, segmentation, cognitive load.

### Framework

Defines a reusable model or structure.

Example: offer structure, content pillars, funnel stages.

### Checklist

Defines review criteria.

Example: landing page review checklist, Instagram bio checklist.

### Playbook

Defines a repeatable process.

Example: create a landing page strategy, research a target audience.

### Research Note

Summarizes external research, source-backed information, or platform-specific facts.

### Example

Stores a reusable example, pattern, or reference.

### Principle

Defines a stable rule or heuristic.

## 6. Evidence Levels

### high

Supported by strong sources, repeated validation, or well-established practice.

### medium

Reasonable and useful, but context-dependent or supported by moderate evidence.

### low

Hypothesis, early observation, weak evidence, or untested belief.

### mixed

Supported in some contexts but limited or disputed in others.

### not_applicable

Used for internal frameworks, examples, templates, or purely operational conventions.

## 7. Lifecycle Status

### draft

Created but not yet trusted as stable reusable knowledge.

### active

Accepted for use by KORA agents, skills, and context selection.

### deprecated

No longer preferred, but preserved for history or compatibility.

## 8. Promotion Rules

Information can become KORA knowledge when it is:

- reusable across projects;
- abstracted away from one local case;
- useful for future agents or skills;
- clear enough to be selected as context;
- supported by evidence, repeated use, or explicit approval.

Information should stay local when it depends on:

- one project identity;
- one audience;
- one client;
- one repository;
- one campaign;
- one personal preference;
- one temporary situation.

## 9. Retrieval And Context Selection

Knowledge should be easy for Context Curator and Capability Router to find.

Useful metadata:

```text
title
type
domain
subdomain
status
evidence_level
related
```

Knowledge entries should be small enough to retrieve selectively. Avoid giant documents that combine many unrelated concepts.

## 10. Initial Domain: Marketing

Marketing is the first prioritized KORA knowledge domain because Marcos Dev depends on positioning, offers, presence, content, conversion, and client communication.

Initial marketing subdomains:

```text
positioning/
offers/
copywriting/
content/
funnels/
branding/
local-presence/
metrics/
research/
frameworks/
```

These folders do not all need to exist immediately. The taxonomy guides future growth.

## 11. Relationship With Skills And Agents

Agents and skills may reference knowledge, but should not duplicate entire bodies of theory.

Example:

```text
Skill: create-content-calendar
References: knowledge/marketing/content/content-pillars.md
```

The skill owns the procedure. The knowledge entry owns the reusable concept.

## 12. Non-Goals For v0.2

Do not create:

- a large marketing encyclopedia;
- hundreds of knowledge files;
- embeddings;
- databases;
- automatic retrieval infrastructure;
- strict schemas enforced by code;
- external source scraping;
- project-specific marketing strategy inside KORA Core.

v0.2 defines the model first.
