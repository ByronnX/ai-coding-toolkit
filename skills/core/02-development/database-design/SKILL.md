---
name: database-design
description: Design database schemas, migrations, indexes, and query patterns. Use when the user asks to design a schema, add a table, create a migration, or optimize queries.
---

# Database Design

## Goal

Design consistent, performant, and maintainable database schemas.

## When to use

- "设计数据库" / "加张表" / "写个 migration" / "优化查询"
- Adding new entities or relationships
- Planning migrations for schema changes

## Workflow

1. **Identify entities and relationships** (1:1, 1:N, M:N).
2. **Choose IDs**: UUID, auto-increment, snowflake.
3. **Define tables, columns, types, and constraints**.
4. **Add indexes** for common query patterns.
5. **Plan migrations** with up/down scripts.
6. **Consider soft deletes, audit fields, and tenancy**.
7. **Review for normalization** and performance trade-offs.

## Output template

```markdown
# Database Design: <Feature>

## ER Diagram
```text
User ||--o{ Order : places
Order ||--|{ OrderItem : contains
```

## Schema
### users
| Column | Type | Constraints |
|--------|------|-------------|
| id     | uuid | PK          |
| email  | text | unique, not null |

## Migrations
- `20240101_create_users.up.sql`
- `20240101_create_users.down.sql`

## Indexes
- `idx_users_email` on users(email)

## Query Patterns
- List orders by user: `SELECT * FROM orders WHERE user_id = $1 ORDER BY created_at DESC`
```

## Notes

- Always write down migrations before applying.
- Avoid nullable foreign keys unless business requires it.
- Index high-cardinality columns used in WHERE/JOIN.
