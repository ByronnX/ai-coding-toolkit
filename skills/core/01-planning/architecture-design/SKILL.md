---
name: architecture-design
description: Design system architecture, choose patterns, and produce architecture decision records. Use when the user asks for architecture, system design, tech stack decisions, module boundaries, or how to structure a project or feature.
---

# Architecture Design

## Goal

Produce pragmatic, maintainable architecture decisions and diagrams.

## When to use

- "怎么设计这个系统" / "架构上怎么选型" / "这个项目应该怎么分层"
- Starting a new service, module, or major feature
- Evaluating trade-offs between technologies

## Workflow

1. **Gather context**: scale, team size, existing stack, constraints.
2. **Identify core entities**, data flow, and boundaries.
3. **Propose 2–3 architecture options** with pros/cons.
4. **Recommend one option** with rationale.
5. **Define module/package boundaries** and interfaces.
6. **Identify risks** and mitigation strategies.
7. **Output architecture overview** + ADR if requested.

## Output template

```markdown
# Architecture: <System>

## Context
...

## Goals & Constraints
- ...

## Options Considered
| Option | Pros | Cons |
|--------|------|------|
| A      | ...  | ...  |
| B      | ...  | ...  |

## Recommendation
...

## Component Diagram
```text
[Client] -> [API Gateway] -> [Service A] -> [Database]
                      -> [Service B] -> [Cache]
```

## Data Flow
1. ...

## Interfaces & Contracts
- ...

## Risks & Mitigations
- Risk: ... → Mitigation: ...
```

## Notes

- Prefer boring technology unless there is a clear reason.
- Keep diagrams text-based (Mermaid/ASCII) for version control.
- Save ADR to `docs/adr/ADR-XXX-<title>.md` if requested.
