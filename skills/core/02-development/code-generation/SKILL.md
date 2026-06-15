---
name: code-generation
description: Generate code from descriptions, examples, or schemas while following project conventions. Use when the user asks to implement a function, component, module, or feature.
---

# Code Generation

## Goal

Write correct, idiomatic, and well-tested code that fits the existing codebase.

## When to use

- "写一个函数" / "实现这个功能" / "生成一个组件"
- Implementing a feature, utility, or module

## Workflow

1. **Read relevant context**: `AGENTS.md`, existing similar files, shared packages.
2. **Check for reuse**: use `component-reuse` or scan for existing utilities.
3. **Clarify inputs, outputs, and edge cases**.
4. **Write the implementation** following project style.
5. **Add types, comments, and error handling**.
6. **Generate or update tests**.
7. **Run validation**: lint, type-check, tests.
8. **Report what was created and any risks**.

## Output template

```markdown
# Implementation: <Feature>

## Files changed
- `src/...`

## Summary
...

## Tests
- ...

## Risks
- ...
```

## Notes

- Do not change unrelated files.
- Prefer composition over inheritance.
- Handle errors explicitly; do not swallow exceptions silently.
