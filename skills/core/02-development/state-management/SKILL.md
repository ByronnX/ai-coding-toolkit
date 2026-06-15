---
name: state-management
description: Choose and implement state management patterns for frontend or backend applications. Use when the user asks about global state, caching, server state, or how to manage shared data.
---

# State Management

## Goal

Choose the right state management approach and implement it consistently.

## When to use

- "怎么管理全局状态" / "用 Redux 还是 Zustand" / "server state 怎么处理"
- Adding shared state to a frontend app
- Designing caching or session management

## Workflow

1. **Categorize the state**: local UI, global shared, server/cache, URL, form.
2. **Choose the tool** based on scope and complexity.
3. **Define the store shape** and selectors.
4. **Define actions/reducers/hooks**.
5. **Handle async state** (loading, error, success).
6. **Add persistence or hydration** if needed.
7. **Write tests** for reducers and selectors.

## Output template

```markdown
# State Management: <Feature>

## State Categories
| Type | Tool | Example |
|------|------|---------|
| Local UI | useState | modal open |
| Global   | Zustand  | user session |
| Server   | TanStack Query | user list |

## Store Shape
```ts
interface Store {
  user: User | null;
  theme: "light" | "dark";
}
```

## Usage
```tsx
const user = useStore((s) => s.user);
```
```

## Notes

- Keep server state and client state separate.
- Avoid global state for purely local concerns.
- Prefer derived state over duplicated state.
