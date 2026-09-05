# KORA Experiments and Learning Specification v0.8

## 1. Purpose

This specification defines how KORA runs experiments and converts outcomes into useful learning.

Experiments test hypotheses. Learning decides what should persist, change, or be ignored.

The goal of v0.8 is to formalize experimentation and learning loops without implementing automated analytics, background jobs, or self-modifying behavior.

## 2. Experiment Definition

An experiment is a structured test designed to learn something.

Examples:

- test a new content format;
- compare two offers;
- test a landing page headline;
- try a new project workflow;
- test whether a new skill improves consistency;
- compare manual versus automated execution;
- validate whether an integration is worth building.

An experiment is not:

- random trial and error;
- a permanent decision by itself;
- a guarantee of truth;
- a raw task result;
- a reason to silently update memory or knowledge.

## 3. Learning Definition

Learning is the process of interpreting results and deciding whether anything should persist.

Possible learning destinations:

- no persistence;
- local memory;
- global memory;
- local decision;
- architecture decision;
- knowledge entry;
- skill improvement;
- agent improvement;
- eval improvement;
- tool proposal;
- automation proposal;
- project context update.

## 4. Core Rule

```text
Experiments create evidence.
Learning interprets evidence.
Promotion changes source-of-truth stores only with criteria or approval.
```

## 5. Experiment Scope

Experiments can be global, local, or hybrid.

### Global Experiment

Tests something reusable across KORA or multiple projects.

Example: Does the capability plan template improve task routing quality?

### Local Experiment

Tests something specific to one project.

Example: Does Marcos Dev get better replies using carousel posts or single-image posts?

### Hybrid Experiment

Uses a global method but tests a local application.

Example: Use a reusable content experiment framework to test Marcos Dev Instagram content.

## 6. Experiment Contract

Each experiment should define:

- title;
- scope;
- status;
- owner;
- project, if local;
- hypothesis;
- reason;
- method;
- inputs;
- success criteria;
- metrics or signals;
- duration or stopping condition;
- risks;
- approval points;
- results;
- interpretation;
- learning recommendation;
- related knowledge, skills, agents, evals, tools, decisions, or memory.

## 7. Experiment Status

### proposed

The experiment is suggested but not approved.

### active

The experiment is currently running.

### completed

The experiment has results and interpretation.

### abandoned

The experiment was stopped before useful conclusions.

### superseded

The experiment was replaced by a better experiment or decision.

## 8. Evidence Strength

Learning should classify evidence strength.

### weak

Single observation, anecdote, incomplete data, or unclear signal.

### moderate

Useful pattern, repeated observation, or reasonable data with limitations.

### strong

Repeated results, good data quality, clear comparison, or strong external evidence.

### inconclusive

The result does not support a clear learning.

## 9. Promotion Rules

Promote learning only when useful.

Learning can become memory when:

- it is specific to future operation;
- it helps avoid repeated mistakes;
- it captures a durable preference or constraint;
- it preserves a meaningful result.

Learning can become knowledge when:

- it is reusable across projects;
- it is abstracted from one local case;
- evidence is sufficient or limitations are clear;
- it helps future agents or skills.

Learning can become a decision when:

- it changes policy, architecture, project direction, workflow, capability scope, permissions, or operating rules.

Learning can become a capability update when:

- a skill, agent, eval, tool, integration, or automation should be improved.

Learning should not persist when:

- it is noise;
- it is temporary;
- it is too uncertain;
- it is already captured elsewhere;
- it would clutter context selection.

## 10. Human Control

Human approval is required before:

- promoting local learning to global KORA knowledge;
- changing architecture decisions;
- creating or changing automations;
- changing memory policies;
- storing sensitive project/client data;
- treating weak evidence as stable truth;
- changing external systems based on experiment results.

## 11. Relationship With Evals

Evals assess quality. Experiments test hypotheses.

An eval result may trigger learning. An experiment may use evals as success criteria.

Example:

```text
Experiment: Try a new project binding workflow.
Eval: Run project binding checklist.
Learning: Update setup-kora-project skill if results improve.
```

## 12. Relationship With Memory

Memory stores operational learning, not raw experiment logs.

Experiment results should be summarized before becoming memory.

## 13. Relationship With Knowledge

Knowledge should receive only reusable, abstracted, useful learning.

Local project outcomes should remain local unless generalized.

## 14. Non-Goals For v0.8

Do not create:

- automated experiment runner;
- analytics dashboard;
- statistical testing engine;
- tracking pixels;
- background learning loops;
- silent memory writes;
- self-modifying agents;
- external integrations.

v0.8 defines the experiment and learning model first.
