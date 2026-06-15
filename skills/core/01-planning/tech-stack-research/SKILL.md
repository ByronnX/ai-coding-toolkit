---
name: tech-stack-research
description: Research and compare technology options for a project or feature. Use when the user asks which framework, library, database, tool, or service to choose.
---

# Tech Stack Research

## Goal

Provide an evidence-based comparison of technology options with a clear recommendation.

## When to use

- "应该用哪个框架" / "选 A 还是 B" / "这个库怎么样"
- Starting a new project or adding a new dependency
- Evaluating migration targets

## Workflow

1. **Clarify requirements**: functional needs, non-functional constraints, team expertise.
2. **Identify 3–5 candidate options**.
3. **Compare across dimensions**:
   - Maturity & community
   - Learning curve
   - Performance & scalability
   - Ecosystem & integrations
   - Licensing & cost
   - Operational complexity
4. **Highlight deal-breakers** for each option.
5. **Give a ranked recommendation** with rationale.
6. **List migration/implementation risks** if applicable.

## Output template

```markdown
# Tech Stack Research: <Decision>

## Requirements
- ...

## Options
| Option | Maturity | Performance | Ecosystem | Cost | Notes |
|--------|----------|-------------|-----------|------|-------|
| A      | ...      | ...         | ...       | ...  | ...   |
| B      | ...      | ...         | ...       | ...  | ...   |

## Deal-breakers
- Option X: ...

## Recommendation
**Recommended:** ...
**Why:** ...

## Risks & Next Steps
- ...
```

## Notes

- Use recent data when possible; note the date of the research.
- Avoid fanboyism; be honest about trade-offs.
