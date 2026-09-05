# Information Flow

Conceptual flow:

```text
User / Task
    ↓
Orchestration
    ↓
Context Layer
    ├── reads Knowledge Base
    ├── reads Project Context
    └── reads Memory
    ↓
Agent
    ├── uses Skills
    ├── calls Tools
    └── produces Output / Actions
    ↓
Evaluation
    ↓
Result
    ↓
Experiments and Learning
    ├── may update Memory
    ├── may propose Knowledge changes
    └── may propose Architecture / Skill / Eval improvements
```

This is an architectural model, not a required implementation sequence.

