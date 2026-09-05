# Components

KORA v0.1 defines these conceptual components:

1. Architecture
2. Knowledge Base
3. Project Context
4. Memory
5. Context Layer
6. Orchestration
7. Agents
8. Skills
9. Tools
10. Evaluation
11. Experiments and Learning

These components are not all runtime modules. Some are storage areas, some are policies, and some are responsibilities that may become code in later versions.


KORA should support business work by allowing each project to define its own context, identity, market, offers, operations, decisions, agents, skills, tools, evals, and learning records as needed.


## Capability Management

Capability Management is the decision layer that determines whether KORA should execute directly, reuse an existing capability, create or propose a new agent, create or propose a new skill, use or create a tool, add an automation, apply an eval, or record learning.

It is central to KORA because it turns tasks into reusable business capabilities without polluting KORA Core with project-specific details.
