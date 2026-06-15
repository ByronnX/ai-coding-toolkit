---
name: api-design
description: Design RESTful or GraphQL APIs, define endpoints, request/response schemas, and error contracts. Use when the user asks to design an API, add an endpoint, or define data contracts.
---

# API Design

## Goal

Design clear, consistent, and evolvable APIs.

## When to use

- "设计一个 API" / "新增接口" / "定义前后端协议"
- Adding endpoints to a backend service
- Defining GraphQL schemas or RPC contracts

## Workflow

1. **Identify the resource** and operations (CRUD or custom).
2. **Choose the style**: REST, GraphQL, RPC, or event-based.
3. **Define endpoints/mutations/queries**.
4. **Design request/response schemas** with validation rules.
5. **Define error responses** using standard HTTP status codes or error codes.
6. **Add pagination, filtering, sorting** where applicable.
7. **Consider versioning, idempotency, and caching**.
8. **Document with OpenAPI / GraphQL schema** if applicable.

## Output template

```markdown
# API Design: <Resource>

## Endpoints
| Method | Path | Description |
|--------|------|-------------|
| GET    | /api/v1/users | List users |

## Request / Response
### GET /api/v1/users
**Query params:**
- `page` (number)
- `limit` (number, max 100)

**Response 200:**
```json
{ "data": [...], "meta": { "page": 1, "total": 100 } }
```

**Error 400:**
```json
{ "error": { "code": "INVALID_LIMIT", "message": "limit must be <= 100" } }
```

## Notes
- Pagination uses cursor/offset.
- All endpoints require authentication except health check.
```

## Notes

- Use nouns for resources, not verbs.
- Return structured errors; never leak internal stack traces.
- Version public APIs from day one.
