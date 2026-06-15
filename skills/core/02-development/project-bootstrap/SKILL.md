---
name: project-bootstrap
description: Bootstrap a new project with the right structure, tooling, and initial configuration. Use when the user asks to create a new project, initialize a repo, scaffold an app, or set up a monorepo.
---

# Project Bootstrap

## Goal

Create a clean, production-ready project skeleton with consistent tooling.

## When to use

- "新建一个项目" / "初始化一个仓库" / "脚手架" / "create a new app"
- Starting a new service, package, or monorepo workspace

## Workflow

1. **Clarify the project type**: frontend, backend, full-stack, library, CLI, monorepo.
2. **Choose the tech stack** based on team standards or user request.
3. **Create directory structure** following conventions.
4. **Initialize package manager** and core dependencies.
5. **Set up tooling**: TypeScript, ESLint, Prettier, testing, Husky.
6. **Add configuration files**: `tsconfig.json`, `.gitignore`, `README.md`.
7. **Set up CI/CD template** from `workflows/github-actions/ci.yml`.
8. **Run initial validation**: install, lint, type-check, test.

## Output template

```markdown
# Bootstrap: <Project>

## Stack
- Language: ...
- Framework: ...
- Testing: ...

## Directory Structure
```
...
```

## Installed Tools
- ...

## Next Steps
1. ...
```

## Notes

- Do not over-engineer; start minimal and add complexity as needed.
- Use the team's existing `AGENTS.md` and `.cursorrules` if available.
- For monorepos, use Turborepo or Nx conventions.
