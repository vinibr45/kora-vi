# EV-0005: Learning Promotion

## Scenario

The user says:

```text
This decision format worked well. Use it from now on.
```

## Purpose

Test whether KORA can decide if user feedback should become memory, a decision, reusable knowledge, a skill update, or nothing.

## Expected Agents

- Knowledge Steward
- KORA Architect, if architecture or decision policy changes
- Capability Router, if the feedback affects capability behavior
- Context Curator, if prior context is needed

## Expected Skills

- `promote-learning`
- `record-decision`
- `classify-scope`
- `select-context`, if prior related decisions or templates must be reviewed

## Expected Capability Assessment

KORA should identify:

```text
Learning type: process preference / decision format
Scope: likely architecture or global KORA operating rule
Possible destination: architecture decision, skill update, README/template update, memory
Evidence: user approval
Approval: already explicit if the user says use it from now on
```

## Expected Decision Behavior

KORA should not store the entire conversation.

It should update only the useful durable rule or create a decision record describing the accepted format.

## Expected Scope Behavior

If the format applies to all KORA decisions, it belongs in KORA Core.

If it applies only to one project, it belongs in that project's `.kora/decisions/` or local instructions.

## Pass Criteria

This scenario passes if KORA:

- recognizes durable user preference;
- avoids storing noise;
- selects the right destination;
- updates a decision/template/skill only when useful;
- distinguishes local from global scope.

## Fail Criteria

This scenario fails if KORA:

- ignores the instruction;
- stores raw conversation as memory;
- promotes a local preference into global knowledge without scope analysis;
- updates unrelated files.
