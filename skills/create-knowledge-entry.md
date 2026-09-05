# create-knowledge-entry

## Purpose

Create or propose a reusable KORA knowledge entry from an idea, source, learning, concept, framework, checklist, playbook, research note, example, or principle.

This skill helps KORA turn useful information into structured knowledge without mixing it with project-specific context.

## When To Use

- When the user asks to add knowledge to KORA.
- When a repeated learning may become reusable across projects.
- When a source, concept, or framework should be formalized.
- When building a domain knowledge base such as marketing, software engineering, UX, security, finance, operations, sales, or product.

## Inputs

- Raw idea, note, source, learning, or concept.
- Intended domain and subdomain, if known.
- Related project context, if any.
- Evidence or source information, if available.
- Existing knowledge taxonomy.
- Knowledge entry template.

## Process

1. Identify whether the information is reusable across projects.
2. Separate reusable knowledge from project-specific application.
3. Classify the knowledge type: concept, framework, checklist, playbook, research-note, example, or principle.
4. Classify domain and subdomain.
5. Estimate evidence level: low, medium, high, mixed, or not_applicable.
6. Choose status: usually draft unless explicitly accepted.
7. Select or propose a file path under `knowledge/`.
8. Apply the knowledge entry template.
9. Include sources, limitations, and related entries when useful.
10. Ask for approval before creating or promoting uncertain knowledge when needed.

## Outputs

- Proposed or created knowledge entry.
- File path recommendation.
- Metadata recommendation.
- Scope classification.
- Evidence and limitation notes.
- Local context separated from global knowledge, if relevant.

## Boundaries

This skill should not create project-specific strategy inside KORA Core.

It should not turn weak, one-off, local observations into global knowledge without abstraction, evidence, or explicit approval.

It should not create large encyclopedic documents when smaller modular entries would be better.
