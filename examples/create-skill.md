# Example: Create A Skill

## User Request

```text
Esse processo de briefing comercial se repete toda semana. Cria uma skill para isso.
```

## KORA Route

```text
skills/route-user-request.md
skills/classify-task.md
skills/classify-scope.md
skills/create-skill.md
```

## Expected Handling

1. Identify whether the procedure is reusable across projects or specific to one business.
2. Check existing skills before creating a new one.
3. Use `skills/templates/skill-template.md`.
4. Define purpose, when to use, inputs, process, outputs, tools, approval points, and boundaries.
5. Add the skill to the relevant README if it becomes part of KORA Core.

## Scope Decision

```text
Reusable briefing method -> skills/
Project-specific briefing rules -> project .kora/skills/
One-time checklist -> output/ or project notes
```

## Realistic Follow-Up

```text
Agora cria uma avaliacao para testar se essa skill gera briefings bons.
```
