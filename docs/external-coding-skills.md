# 外部代码能力 Skill / 工具资源清单

> 全网搜集、提升 AI 编程能力的 Skill、MCP Server、Cursor Rules 与多 Agent 框架。  
> 最后更新：2026-06-15

---

## 一、Skill 聚合市场 / Awesome 列表

| 名称 | 链接 | 规模 | 说明 |
|------|------|------|------|
| **Awesome Skills 市场** | https://awesomeskills.dev | 1000+ | 最完整的 SKILL.md 目录，支持 Claude / Codex / Cursor / Kimi 等平台 |
| **VoltAgent/awesome-agent-skills** | https://github.com/VoltAgent/awesome-agent-skills | 1000+ | 官方+社区 Skill 合集，按领域分类 |
| **kodustech/awesome-agent-skills** | https://github.com/kodustech/awesome-agent-skills | 数百 | 专注 Claude Code / Codex / Cursor，含测试/代码审查/安全 |
| **ComposioHQ/awesome-codex-skills** | https://github.com/ComposioHQ/awesome-codex-skills | 880+ | Codex 生态，含大量 Composio 应用自动化 |
| **mxyhi/ok-skills** | https://github.com/mxyhi/ok-skills | 精选 | 含 Kimi webbridge、浏览器自动化、前端技能 |
| **the911fund/skill-of-skills** | https://github.com/the911fund/skill-of-skills | 索引 | 跨 Claude / Codex / Gemini CLI / Cursor 的技能发现引擎 |
| **floomhq/starter** | https://github.com/floomhq/starter | 65 个 | 一键安装，支持 Claude / Codex / Cursor / Kimi / OpenCode |
| **rohitg00/awesome-claude-code-toolkit** | https://github.com/rohitg00/awesome-claude-code-toolkit | 135 agents + 35 skills | Claude Code 专用，但也兼容其他 Agent |
| **heilcheng/awesome-agent-skills** | https://github.com/heilcheng/awesome-agent-skills | 社区 | 简单文本型 Skill，适合非开发者使用 |

---

## 二、代码审查 / PR  Review 类 Skill

| Skill | 仓库/来源 | 能力 |
|-------|----------|------|
| **brooks-lint** | hyhmrright/brooks-lint | 基于 6 本经典软件工程书的 AI 代码审查，带风险等级和书籍引用 |
| **NeoLabHQ/code-review** | NeoLabHQ/code-review | 多 Agent 代码审查：bug-hunter、security-auditor、quality-reviewer、test-coverage-reviewer |
| **dyadmulti-pr-review** | kodustech/awesome-agent-skills | 3 个 Claude sub-agent 独立审查，共识投票降低排序偏见 |
| **review-and-refactor** | github/awesome-copilot | 按 `.github/instructions/` 和 `.github/copilot-instructions.md` 自动审查+重构 |
| **octocode-pr-review** | kodustech/awesome-agent-skills | PR review for bugs, security & quality |
| **alignment-review** | kodustech/awesome-agent-skills | 对照 OpenEnv 原则与 RFC 审查代码对齐度 |
| **pr-review-reply** | kodustech/awesome-agent-skills | 用 GitHub CLI 回复并解决 PR review comments |
| **fix-pr** | kodustech/awesome-agent-skills | 分析 CodeRabbit PR 评论并生成修复计划 |
| **code-quality-analysis-with-pmat** | kodustech/awesome-agent-skills | 用 PMAT 分析代码质量、复杂度、技术债 |

---

## 三、测试 / QA 类 Skill

| Skill | 来源 | 能力 |
|-------|------|------|
| **testdino-hq/playwright-skill** | awesomeskills.dev | 70+ Playwright E2E 模式：POM、CI/CD、迁移、CLI |
| **generating-end-to-end-tests** | kodustech/awesome-agent-skills | 用 Playwright/Cypress/Selenium 生成 E2E 测试 |
| **tdd-workflow** | kodustech/awesome-agent-skills | 强制 TDD：单元/集成/E2E，覆盖率 >80% |
| **simplify** | kodustech/awesome-agent-skills | Red-Green-Refactor 的 Refactor 阶段 |
| **LambdaTest/agent-skills** | VoltAgent/awesome-agent-skills | 生产级测试自动化 Skill |
| **webapp-testing** | ComposioHQ/awesome-codex-skills | 本地 web 应用测试 + Playwright |
| **omkamal/pypict-skill** | VoltAgent/awesome-agent-skills | 成对测试生成 |
| **resolve-conflicts** | kodustech/awesome-agent-skills | 合并冲突结构化处理（lock 文件、import、配置） |

---

## 四、开发流程 / 工作流类 Skill

| Skill | 来源 | 能力 |
|-------|------|------|
| **mattpocock/skills** | VoltAgent/awesome-agent-skills | 17 个开发流程 Skill：PRD、TDD、架构、git guardrails、issue triage、重构计划 |
| **obra/subagent-driven-development** | VoltAgent/awesome-agent-skills | 多 sub-agent 协作开发 |
| **obra/systematic-debugging** | VoltAgent/awesome-agent-skills | 系统化调试 |
| **obra/root-cause-tracing** | VoltAgent/awesome-agent-skills | 根因分析 |
| **obra/finishing-a-development-branch** | VoltAgent/awesome-agent-skills | 完成 Git 分支 |
| **obra/requesting-code-review** / **receiving-code-review** | VoltAgent/awesome-agent-skills | 代码审查发起与接收 |
| **obra/using-git-worktrees** | VoltAgent/awesome-agent-skills | Git worktree 管理 |
| **obra/verification-before-completion** | VoltAgent/awesome-agent-skills | 完成前验证 |
| **fvadicamo/dev-agent-skills** | VoltAgent/awesome-agent-skills | Git 与 GitHub 工作流 Skill |
| **sneg55/agent-starter** | awesomeskills.dev | Anthropic 工程模式，含 Skill 模板与指南 |
| **mcollina/skills** | VoltAgent/awesome-agent-skills | 11 个 Skill：Node.js、Fastify、TypeScript、OAuth、Git/GitHub、ESLint、文档 |
| **Kimi-ming/continuous-doc-dev** | awesomeskills.dev | 文档驱动开发 |
| **alinaqi/claude-bootstrap** | VoltAgent/awesome-agent-skills | 安全优先的项目初始化、spec-driven atomic todos |
| **changelog-orchestrator** | kodustech/awesome-agent-skills | 自动收集变更并生成 changelog PR |
| **deep-dive** | rohitg00/awesome-claude-code-toolkit | DAG 深度研究，并行 sub-agent，写带引用报告 |

---

## 五、架构 / 设计 / 规范类 Skill

| Skill | 来源 | 能力 |
|-------|------|------|
| **NeoLabHQ/sdd** | VoltAgent/awesome-agent-skills | Spec-Driven Development：提示词 → 生产实现 |
| **NeoLabHQ/ddd** | VoltAgent/awesome-agent-skills | 领域驱动开发 + Clean Architecture + SOLID |
| **NeoLabHQ/sadd** | VoltAgent/awesome-agent-skills | 独立 sub-agent 分派任务，中间设代码审查检查点 |
| **NeoLabHQ/kaizen** | VoltAgent/awesome-agent-skills | 持续改进方法论 |
| **Edison** | rohitg00/awesome-claude-code-toolkit | 设计决策 Skill：Check / Explore / Audit 三种模式 |
| **massimodeluisa/recursive-decomposition-skill** | VoltAgent/awesome-agent-skills | 长上下文任务递归分解 |
| **zscole/model-hierarchy-skill** | VoltAgent/awesome-agent-skills | 按任务复杂度成本优化路由模型 |
| **uucz/moyu** | VoltAgent/awesome-agent-skills | 反过度工程 Skill，10 平台 |
| **stride-analysis-patterns** | kodustech/awesome-agent-skills | STRIDE 威胁建模 |

---

## 六、安全类 Skill

| Skill | 来源 | 能力 |
|-------|------|------|
| **vibesec / BehiSecc/vibesec** | VoltAgent/awesome-agent-skills | Bug Hunter 视角防 IDOR、XSS、SQL 注入、SSRF、弱认证 |
| **mukul975/Anthropic-Cybersecurity-Skills** | VoltAgent/awesome-agent-skills | 753 个网络安全 Skill，38 领域 |
| **redhoundinfosec/redhound-arsenal** | awesomeskills.dev | 76 个 Kali Linux 安全 Skill |
| **sast-configuration** | kodustech/awesome-agent-skills | SAST 工具配置 |
| **wrsmith108/varlock-claude-skill** | VoltAgent/awesome-agent-skills | 环境变量安全管理，防泄漏 |

---

## 七、性能 / 前端 / 专项类 Skill

| Skill | 来源 | 能力 |
|-------|------|------|
| **web-performance-optimization** | kodustech/awesome-agent-skills | Web 性能优化：Core Web Vitals、包大小、缓存 |
| **profiling-application-performance** | kodustech/awesome-agent-skills | CPU/内存/执行时间性能分析 |
| **swiftui-performance-audit** | kodustech/awesome-agent-skills | SwiftUI 性能审计 |
| **davidme6/frontend-polish-skill** | awesomeskills.dev | 前端 UI 打磨、响应式、交互状态 |
| **Leonxlnx/taste-skill** | VoltAgent/awesome-agent-skills | 高审美前端，反“AI 味” |
| **prof-ramos/shadcn-ui-skill** | awesomeskills.dev | shadcn/ui 完整 Skill |
| **CloudAI-X/threejs-skills** | VoltAgent/awesome-agent-skills | Three.js 3D 开发 |
| **ZhangHanDong/makepad-skills** | VoltAgent/awesome-agent-skills | Rust Makepad UI 开发 |
| **efremidze/swift-patterns-skill** | VoltAgent/awesome-agent-skills | Swift/SwiftUI 最佳实践 |
| **meodai/skill.color-expert** | VoltAgent/awesome-agent-skills | 色彩科学专家，286K 字参考 |

---

## 八、多 Agent 编排 / 框架

| 名称 | 链接 | 能力 |
|------|------|------|
| **oh-my-kimi** | dmae97/oh-my-kimi | Kimi Code CLI 多 Agent 编排：worktree、DAG、质量门、图记忆 |
| **AuraKit** | smorky850612 | 46 模式、23 sub-agent、6 层 OWASP 安全、10 生命周期钩子 |
| **Vibe-Skills** | foryourhealth111-pixel | 阶段性测试驱动 Skill 编排 |
| **polywave** | blackwell-systems/polywave-codex | 并行 Agent 协调 + 结构化合并安全 |
| **Bernstein** | awesomeskills.dev | 多 Agent 在隔离 git worktree 中并行运行 |
| **Loki-mode** | kodustech/awesome-agent-skills | 100+ 专业 Agent 的创业系统 |
| **Emdash Skills** | ComposioHQ/awesome-codex-skills | 14 领域自动化产品构建 |

---

## 九、MCP Server（给 Agent 提供工具能力）

| Server | 链接 | 用途 |
|--------|------|------|
| **GitHub MCP Server** | github/github-mcp-server | 仓库、Issue、PR、Actions、代码分析 |
| **GitHub Code Review MCP** | mcpmarket.com/server/github-code-review | 只读代码审查 |
| **Code Review Server** | crazyrabbitLTC/mcp-code-review-server | Repomix + LLM 结构化代码审查 |
| **codemcp** | ezyang/codemcp | 基础读写命令行工具的 coding agent |
| **serena** | oraios/serena | 基于 language server 的符号代码操作 |
| **RepoMapper** | pdavis68/RepoMapper | 动态仓库地图 |
| **codegraphcontext** | shashankss1205/codegraphcontext | 本地代码图数据库 |
| **lsp-mcp** | Tritlo/lsp-mcp | 与 LSP server 交互 |
| **AWS MCP Servers** | awslabs/mcp | AWS 官方 MCP Server 套件 |
| **Augments MCP** | awesomeskills.dev | 90+ 框架文档查询 |
| **Gitingest** | claudedirectory.org | 任意 GitHub 仓库转文本摘要 |
| **Perseus** | claudedirectory.org | 编译前上下文预解析 |

---

## 十、Cursor Rules / 项目规则

| 资源 | 链接 | 说明 |
|------|------|------|
| **awesome-cursorrules** | PatrickJS/awesome-cursorrules | 大量 .cursorrules 文件 |
| **awesome-cursor-rules** | bmedi/awesome-cursor-rules | .cursorrules 精选 |
| **devin.cursorrules** | grapeot/devin.cursorrules | 把 Cursor 变成 Devin 风格 |
| **localskills.sh** | localskills.sh | 把 .cursorrules 变成可共享 Skill |
| **sbstjn/skills** | codeberg.org/sbstjn/skills | skills + rules + agents 三树结构 |

---

## 十一、如何选用？

### 如果你用 Kimi Code CLI

1. **优先找 awesomeskills.dev 上标注兼容 Kimi 的 Skill**
2. **复制 SKILL.md 到 `~/.kimi/skills/<name>/SKILL.md`**
3. **注意 Kimi 不支持递归嵌套目录**，扁平化 skill 结构
4. **Composio 强依赖的 Skill** 需要先安装 Composio CLI 并授权
5. **MCP Server** 是更通用的选择，Kimi 支持 MCP

### 如果你用 Cursor

1. 优先用 `.cursorrules` 和 `.cursor/rules/*.mdc`
2. Skill 放 `.cursor/skills/<name>/SKILL.md`
3. MCP server 配置在 `.cursor/mcp.json`

### 如果你用 Claude Code

1. Skill 放 `.claude/skills/<name>/SKILL.md`
2. 配合 MCP server 使用
3. `CLAUDE.md` 作为项目级规范

---

## 十二、推荐组合（按目标）

| 目标 | 推荐 Skill / 工具 |
|------|-------------------|
| 提升代码审查质量 | brooks-lint + NeoLabHQ/code-review + review-and-refactor |
| 提升测试能力 | tdd-workflow + testdino-hq/playwright-skill + generating-end-to-end-tests |
| 提升调试能力 | obra/systematic-debugging + obra/root-cause-tracing |
| 提升架构设计 | NeoLabHQ/sdd + NeoLabHQ/ddd + Edison |
| 提升安全 | vibesec + sast-configuration |
| 提升前端质量 | taste-skill + frontend-polish-skill + shadcn-ui-skill |
| 多 Agent 协作 | oh-my-kimi / AuraKit / Vibe-Skills |
| GitHub 集成 | github/github-mcp-server + gh CLI |
