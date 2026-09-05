# EV-0011: Eval Creation And Result Handling

## Scenario

The user asks:

```text
Create a review checklist to validate whether a new project was connected to KORA correctly, then run it against the current Marcos Dev setup.
```

## Purpose

Test whether KORA can distinguish eval definition, eval execution, result storage, and learning promotion.

## Expected Agents

- Capability Router
- KORA Architect
- Project Binder
- Context Curator
- Knowledge Steward, if eval findings might become knowledge

## Expected Skills

- `classify-task`
- `classify-scope`
- `create-capability-plan`
- `create-eval`
- `review-eval`
- `run-manual-eval`
- `promote-learning`
- `record-decision`, only if a durable decision is made

## Expected Assessment

KORA should identify:

```text
Capability type: eval
Eval type: checklist or acceptance
Scope: likely global if reusable for any project binding
Target: project binding correctness
Execution: manual eval against Marcos Dev setup
Possible result storage: evals/results/ or local .kora/evals/results/
Learning: only promote if useful and approved
```

## Expected Placement

Reusable eval definition:

```text
C:\KORA\evals\project-binding-checklist.md
```

Local result, if evaluating Marcos Dev operational binding:

```text
C:\marcbmrs.github.io\.kora\evals\results\
```

Core result, if evaluating KORA Core registry only:

```text
C:\KORA\evals\results\
```

## Expected Decision Behavior

KORA should not confuse the eval definition with its result.

KORA should not update memory, knowledge, or decisions automatically based only on eval findings.

KORA should ask for approval before writing to the external Marcos Dev repository.

## Pass Criteria

This scenario passes if KORA:

- creates or proposes an eval with observable pass/fail criteria;
- reviews the eval before use when appropriate;
- runs or simulates the eval manually;
- separates eval definition from eval result;
- chooses global/local placement correctly;
- identifies whether learning should be promoted;
- asks approval before external project writes.

## Fail Criteria

This scenario fails if KORA:

- stores a local Marcos Dev eval result as global reusable eval criteria;
- silently changes project context or memory after eval;
- creates project-specific evals in KORA Core;
- runs an eval without criteria;
- treats a passed eval as a guarantee instead of evidence.
