# AI Coding Toolkit

> 一个**自动同步**的 AI 编程 Skill 工具包。  
> 每天从多个上游仓库拉取优质编程 Skill，筛选后自动更新到本仓库。  
> 兼容 Kimi Code CLI、OpenAI Codex CLI、Claude Code、Cursor、OpenCode、Gemini CLI 等 Agent。

---

## 核心特性

- **自动同步**：每天从 `awesome-codex-skills`、`awesome-agent-skills`、`ok-skills` 等上游拉取更新
- **智能筛选**：只保留编程/开发/测试/审查/安全相关的 Skill
- **多 Agent 兼容**：一份 Skill，同时支持 Kimi / Codex / Claude / Cursor / OpenCode
- **跨机器复用**：任何电脑 `git pull` 后即可同步最新 Skill
- **质量门禁**：自动验证 SKILL.md 格式和元数据

---

## 仓库结构

```
ai-coding-toolkit/
├── sources.json                    # 上游 Skill 源配置
├── registry.json                   # 已收录 Skill 的元数据（来源、版本、同步时间）
├── skills/
│   ├── core/                       # 自研核心 Skill（ manually maintained ）
│   └── external/                   # 自动同步的外部 Skill
├── configs/                        # AGENTS.md / .cursorrules 模板
├── scripts/
│   ├── sync-from-sources.py       # 主同步脚本
│   ├── install-all.py             # 安装到本机所有 Agent
│   └── validate_skills.py         # Skill 格式校验
├── .github/workflows/sync-skills.yml  # 每日自动同步 CI
└── docs/
```

---

## 快速开始

### 1. 克隆本仓库

```bash
git clone https://github.com/ByronnX/ai-coding-toolkit.git
```

### 2. 安装到本机所有 Agent

```bash
cd ai-coding-toolkit
python scripts/install-all.py
```

只装到 Kimi：

```bash
python scripts/install-all.py --agents kimi
```

### 3. 每天获取更新

```bash
git pull origin main
python scripts/install-all.py
```

---

## 手动同步上游（可选）

如果你想立即拉取上游最新 Skill：

```bash
# 预览
python scripts/sync-from-sources.py --dry-run

# 执行同步
python scripts/sync-from-sources.py
```

---

## 添加新的上游源

编辑 `sources.json`：

```json
{
  "sources": [
    {
      "name": "my-source",
      "repo": "https://github.com/org/skills-repo.git",
      "enabled": true,
      "exclude_paths": ["deprecated"],
      "include_keywords": ["code", "review", "test"]
    }
  ]
}
```

---

## 核心 Skill 与外部 Skill

| 类型 | 位置 | 更新方式 |
|------|------|---------|
| **核心 Skill** | `skills/core/` | 手动维护，项目规范类 |
| **外部 Skill** | `skills/external/` | 每日自动同步 |

---

## 支持的 Agent

| Agent | 安装路径 |
|-------|---------|
| Kimi Code CLI | `~/.kimi/skills/` |
| Codex CLI | `~/.agents/skills/` |
| Claude Code | `~/.claude/skills/` |
| Cursor | `~/.cursor/skills/` |
| OpenCode | `~/.config/opencode/skills/` |
| Gemini CLI | `~/.gemini/skills/` |
| GitHub Copilot | `~/.copilot/skills/` |
| Windsurf | `~/.codeium/windsurf/skills/` |

---

## 安全提示

自动同步的 Skill 来自社区上游，**未经过完整安全审计**。建议：

1. 核心项目规范 Skill 自己维护，不依赖外部同步
2. 定期 review `registry.json` 的变更
3. 对异常 Skill 及时在 `sources.json` 中排除

---

## 许可

MIT
