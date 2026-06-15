---
name: create-plan
description: Create a concise, actionable execution plan for a coding task. Use when the user asks for a plan, roadmap, execution steps, task breakdown, or how to implement a feature before writing code.
---

# Create Plan

## Goal

Turn a user request into a single, reviewable execution plan. Operate in read-only mode while planning.

## When to use

- User asks: "帮我做个计划" / "怎么实现" / "分几步" / "roadmap"
- Starting a non-trivial feature, refactor, migration, or bug fix
- A task touches multiple files or requires tests/validation

## Workflow

1. **Scan context quickly**
   - Read `README.md`, `AGENTS.md`, and any obvious docs (`docs/`, `CONTRIBUTING.md`).
   - Skim files most likely to be touched.
   - Identify constraints: language, frameworks, test commands, deployment shape.

2. **Ask follow-ups only if blocking**
   - Ask at most 1–2 questions.
   - Prefer multiple-choice answers.
   - If unsure but not blocked, make a reasonable assumption and state it.

3. **Create a plan using the template below**
   - Start with 1 short paragraph describing intent and approach.
   - Clearly call out what is **in scope** and **out of scope**.
   - Provide 6–10 atomic checklist items ordered: discovery → changes → tests → rollout.
   - Use verb-first phrasing: "Add…", "Refactor…", "Verify…", "Ship…".
   - Include at least one validation step and one edge-case/risk note.
   - Add an "Open questions" section (max 3) if unknowns remain.

4. **Output only the plan** — no meta explanations.

## Plan template

```markdown
# Plan: <Title>

<1–3 sentences: what, why, high-level approach.>

## Scope
- **In:** ...
- **Out:** ...

## Action items
- [ ] <Step 1>
- [ ] <Step 2>
- [ ] <Step 3>
- [ ] <Step 4>
- [ ] <Step 5>
- [ ] <Step 6>

## Validation
- ...

## Risks & edge cases
- ...

## Open questions
- ...
```

## Notes

- Keep plans reviewable; avoid tasks larger than one focused PR.
- Do not write code snippets in the plan.
- Save the plan to `plan.md` or `docs/plan-<feature>.md` if requested.
