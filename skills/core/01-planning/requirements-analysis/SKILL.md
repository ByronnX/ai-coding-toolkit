---
name: requirements-analysis
description: Analyze user requirements, identify ambiguities, and produce structured requirements documents. Use when the user describes a feature, product idea, user story, or business need and asks for analysis before design or implementation.
---

# Requirements Analysis

## Goal

Transform informal descriptions into clear, testable, and prioritized requirements.

## When to use

- User describes a feature idea, user story, or business problem
- Before architecture design or implementation planning
- Detecting scope creep or missing edge cases

## Workflow

1. **Restate the core problem** and target user in one sentence.
2. **List functional requirements** using Must/Should/Could.
3. **List non-functional requirements**: performance, security, scalability, accessibility.
4. **Identify user journeys** and edge cases.
5. **Flag ambiguous or missing information** as explicit questions.
6. **Prioritize** using MoSCoW.
7. **Suggest acceptance criteria** for each requirement.

## Output template

```markdown
# Requirements: <Feature>

## Problem Statement
...

## Target Users
- ...

## Functional Requirements
| ID | Requirement | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| FR1| ...         | Must     | ...                 |

## Non-Functional Requirements
| ID | Category | Requirement |
|----|----------|-------------|
| NFR1| Performance | ... |

## User Journeys
1. ...

## Edge Cases
- ...

## Open Questions
- ...

## Out of Scope
- ...
```

## Notes

- Distinguish user needs from proposed solutions.
- Ask clarifying questions rather than guessing.
