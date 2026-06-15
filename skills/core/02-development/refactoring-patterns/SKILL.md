---
name: refactoring-patterns
description: Apply safe refactoring patterns to improve code structure without changing behavior. Use when the user asks to refactor, simplify, extract, or clean up code.
---

# Refactoring Patterns

## Goal

Improve code structure, readability, and maintainability while preserving behavior.

## When to use

- "重构这段代码" / "提取函数" / "简化逻辑" / "减少复杂度"
- A file or function is too large, duplicated, or hard to test

## Workflow

1. **Identify the smell**: long function, duplicated code, tight coupling, primitive obsession, etc.
2. **Ensure tests exist** for the current behavior; if not, add them first.
3. **Apply one refactoring at a time**:
   - Extract function / class / hook
   - Introduce parameter object
   - Replace conditional with polymorphism
   - Remove duplication
4. **Run tests after each change**.
5. **Verify no behavior change**.

## Common Patterns

| Smell | Pattern |
|-------|---------|
| Long function | Extract function |
| Duplicated code | Extract shared utility |
| Deep nesting | Early returns / guard clauses |
| Feature envy | Move method |
| Primitive obsession | Introduce value object |

## Notes

- Never refactor and change behavior in the same commit.
- If tests are missing, write characterization tests first.
- Keep commits small and reviewable.
