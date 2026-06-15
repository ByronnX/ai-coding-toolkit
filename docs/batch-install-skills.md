# 批量安装 Skill 到多个 Agent

> 把 awesomeskills.dev / GitHub 上的 Skill 批量装进 Kimi、Codex、Claude Code、Cursor、OpenCode 等 Agent。

---

## 一、各 Agent 的 Skill 路径

| Agent | 项目级路径 | 用户级（全局）路径 |
|-------|-----------|-------------------|
| **Kimi Code CLI** | `.kimi/skills/` | `~/.kimi/skills/` |
| **Codex CLI** | `.agents/skills/` | `~/.agents/skills/` |
| **Claude Code** | `.claude/skills/` | `~/.claude/skills/` |
| **Cursor** | `.cursor/skills/` | `~/.cursor/skills/` |
| **OpenCode** | `.opencode/skills/` | `~/.config/opencode/skills/` |
| **Gemini CLI** | `.gemini/skills/` | `~/.gemini/skills/` |
| **GitHub Copilot** | `.github/skills/` | `~/.copilot/skills/` |
| **Windsurf** | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |

> **Trae**：目前 Trae 主要走 IDE 插件体系，不一定支持标准 `SKILL.md`，暂不在列表中。

---

## 二、批量安装脚本

使用本工具包中的脚本：`scripts/install-skills-from-github.py`

### 安装所有 skills 到所有 Agent

```bash
python scripts/install-skills-from-github.py https://github.com/VoltAgent/awesome-agent-skills.git
```

### 只安装到 Kimi 和 Cursor

```bash
python scripts/install-skills-from-github.py https://github.com/VoltAgent/awesome-agent-skills.git \
  --agents kimi cursor
```

### 只安装名字含 code / review / test 的 skill

```bash
python scripts/install-skills-from-github.py https://github.com/VoltAgent/awesome-agent-skills.git \
  --filter "code|review|test"
```

### 先试跑，不真安装

```bash
python scripts/install-skills-from-github.py https://github.com/VoltAgent/awesome-agent-skills.git --dry-run
```

### 从本地目录安装

```bash
python scripts/install-skills-from-github.py ./awesome-agent-skills
```

---

## 三、手动安装（理解原理）

```bash
# 1. 克隆技能仓库
git clone --depth 1 https://github.com/VoltAgent/awesome-agent-skills.git
cd awesome-agent-skills

# 2. 找到含 SKILL.md 的目录，复制到目标 Agent
# 例如安装 code-review skill 到 Kimi
cp -r skills/code-review ~/.kimi/skills/

# 3. 重启 Agent CLI
```

---

## 四、awesomeskills.dev 的 `npx add-skill`

awesomeskills.dev 上很多 Skill 支持一键安装：

```bash
# 安装单个 skill（通常只装到当前目录对应的 Agent）
npx add-skill NeoLabHQ/code-review
npx add-skill floomhq/starter
```

**缺点**：`npx add-skill` 不一定同时装到 Kimi + Cursor + Claude，需要多次指定。

---

## 五、anbeime/skill 的 clawhub（中文生态）

```bash
npm install -g clawhub
clawhub login
clawhub search code-review
clawhub install <skill-slug>
```

特点：
- 中文 Skill 较多
- 自动抓取 awesome-agent-skills
- 主要服务 OpenCode/Claude，Kimi 支持需验证

---

## 六、安装后验证

```bash
# Kimi
ls ~/.kimi/skills/

# Codex
ls ~/.codex/skills/

# Claude
ls ~/.claude/skills/

# Cursor
ls ~/.cursor/skills/
```

重启 Agent CLI 后，新 Skill 的元数据才会被加载。

---

## 七、常见问题

### Q: Kimi 为什么不识别某些 Skill？

Kimi 目前**不支持递归加载嵌套 skill 目录**。如果 Skill 结构是 `skills/foo/skills/bar/SKILL.md`，Kimi 会忽略 `bar`。本脚本已做扁平化处理。

### Q: 装了太多 Skill 会不会卡？

会。每个 Skill 的 `name` + `description` 都会进入系统提示。建议每个 Agent 装 **20-50 个**高频 Skill 即可，不要全量安装 800+。

### Q: 同一个 Skill 能同时装到多个 Agent 吗？

可以。Skill 本质是 `SKILL.md` 文本文件，没有 Agent 绑定。但不同 Agent 的触发机制略有差异。

### Q: 怎么卸载？

```bash
rm -rf ~/.kimi/skills/<skill-name>
rm -rf ~/.claude/skills/<skill-name>
rm -rf ~/.cursor/skills/<skill-name>
```
