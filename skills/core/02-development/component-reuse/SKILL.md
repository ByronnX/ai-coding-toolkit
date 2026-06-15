---
name: component-reuse
description: Check for existing internal components, design-system elements, or shared utilities before creating new code. Use when the user asks to build a UI component, page, or feature that might already exist in the codebase.
---

# Component Reuse

## Goal

Avoid duplicating existing components and ensure consistency with the project's design system.

## When to use

- User asks to build a UI component, page section, or form
- Before writing any frontend code that could reuse an existing abstraction
- Onboarding to a project with an established design system

## Workflow

1. **Identify the design system location** (e.g., `packages/ui`, `src/components/ui`, `design-system/`).
2. **Search for existing components** matching the requirement:
   - `find . -type d -name "button" -o -name "modal" -o -name "input"`
   - `rg "export.*Button" packages/ui`
3. **Check Storybook / docs** if available.
4. **Compare the user's need** against existing variants.
5. **Recommend**: reuse, extend, or create new.
6. **If creating new**, place it in the correct package and follow naming conventions.

## Output template

```markdown
# Component Reuse Check: <Component>

## Existing Matches
| Component | Location | Match | Action |
|-----------|----------|-------|--------|
| Button    | packages/ui/button | High  | Reuse |

## Recommendation
...

## Usage Example
```tsx
import { Button } from "@repo/ui/button";
```
```

## Notes

- Prefer extending an existing component over creating a new one.
- If a component is 90% the same, add a variant prop rather than forking.
