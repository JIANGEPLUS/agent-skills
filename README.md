<div align="center">

# agent-skills

**我实际采用的 Agent 技能集合 —— 生产级 `SKILL.md`，跨客户端通用**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Skills](https://img.shields.io/badge/skills-6-blue)
![Platform](https://img.shields.io/badge/Agent%20Skills-compatible-blueviolet.svg)

Qoder · OpenAI Codex · Claude Code · ChatGPT，以及任何兼容 [Agent Skills](https://agentskills.io/) 开放规范的 Agent

</div>

> **English**：A curated collection of the Agent Skills I actually keep installed. Six skills, two groups — one that sharpens the instruction before work starts, five that together form a UI-designer capability. Each is a plain `SKILL.md` folder, auto-discovered with zero configuration.

---

## 为什么是这两个方向

装了很多"什么都能干"的通用提示词，实际效果是每次都要重讲一遍约束。我的取舍是：**只留能被明确触发、职责单一、输出格式固定**的技能。于是收敛成两组：

1. **提示词增强** —— 干活之前先把话说清楚。需求模糊时返工成本最高，这个技能专职消除歧义，且**只增强不执行**。
2. **UI 设计师（像素君拆解）** —— 一个 UI Designer 专家角色拆成 5 个正交环节：令牌 → 组件 → 布局 → 无障碍 → 交付。每环节可单独调用，也能串成完整设计系统流水线。

## 📦 收录的技能

| Skill | 组 | 职责 | 输出 |
|---|---|---|---|
| [`enhance-prompt`](skills/enhance-prompt/) | 提示词 | 改写模糊指令，补全目标/范围/约束/输出格式，假设显式标注 | `<enhanced-prompt>` 单条增强指令 |
| [`design-token-crafter`](skills/design-token-crafter/) | UI | 品牌色 → 100–900 色阶、语义色、字体/间距/阴影/过渡令牌，含暗色主题 | `:root` + `[data-theme="dark"]` CSS |
| [`component-state-designer`](skills/component-state-designer/) | UI | 五类组件 × 变体/尺寸 × 完整状态矩阵（含 `:focus-visible`） | BEM 组件 CSS + 状态矩阵表 |
| [`responsive-layout-blueprint`](skills/responsive-layout-blueprint/) | UI | mobile-first 五档断点、12 列栅格、容器与组件跨端行为 | 栅格 CSS + 断点速查表 |
| [`wcag-accessibility-checker`](skills/wcag-accessibility-checker/) | UI | 六维 WCAG AA 审计，给出算过的对比度比值与可执行修复值 | 分级整改清单（阻断→严重→一般） |
| [`design-handoff-writer`](skills/design-handoff-writer/) | UI | 带测量的规格卡、令牌对照、使用边界、可勾选 QA 清单 | Markdown 交接文档 |

UI 五件套的依赖关系：

```
design-token-crafter ──┬──> component-state-designer ──┬──> design-handoff-writer
                       └──> responsive-layout-blueprint ┘
                                    ▲
                       wcag-accessibility-checker（横切，任一环节后都可插入）
```

## 🚀 安装

**整包装入某个客户端**（用户级，对该用户所有项目生效）：

```bash
git clone https://github.com/JIANGEPLUS/agent-skills.git
cp -r agent-skills/skills/* ~/.qoder/skills/      # Qoder
# cp -r agent-skills/skills/* ~/.codex/skills/    # Codex
# cp -r agent-skills/skills/* ~/.claude/skills/   # Claude Code
```

**只装单个技能**：`skills/` 下每个目录彼此独立，直接拷走即可。

新会话自动发现，无需注册、无配置文件改动、无重启。

**调用**：

```text
/enhance-prompt  帮我把这个需求说清楚
设计令牌：品牌主色 #7c3aed，要暗色模式
检查配色 #6b7280 放在 #f9fafb 上能不能过 WCAG AA
```

也可以不点名，直接描述任务，由 Agent 按各 `SKILL.md` 的 `description` 触发词隐式匹配。

## 🗂 仓库结构

```
agent-skills/
├── README.md
├── LICENSE                       # MIT, 覆盖全部技能
└── skills/
    ├── enhance-prompt/
    │   ├── SKILL.md              # 技能正文（Agent 读这个）
    │   └── README.md             # 面向人的说明
    ├── design-token-crafter/
    ├── component-state-designer/
    ├── responsive-layout-blueprint/
    ├── wcag-accessibility-checker/
    └── design-handoff-writer/
```

每个技能目录固定两文件：`SKILL.md`（规范正文）+ `README.md`（人读的安装与用法）。许可证集中在根目录，不做每技能一份。

## ✍️ SKILL.md 约定

frontmatter 只依赖 `name` 与 `description` 两个字段——这是跨客户端的最小公约集：

```yaml
---
name: design-token-crafter
description: "一句话职责 + 触发词列表 + 适用场景"
---
```

正文固定六节：**功能定位 / 触发条件 / 工作流程 / 输出格式 / 约束与注意事项 / 使用示例**。

三条硬规则，是我判断一个技能值不值得留的标准：

1. **职责单一** —— 明确写出"不负责什么"，避免技能之间互相抢活。
2. **输出格式写死** —— 不给格式的技能等于没给。
3. **约束可验证** —— 例如"对比度必须给出算过的比值，不接受'提高对比度'这类空话"。

部分技能带有 `description_zh` / `display_name` / `visibility` 等扩展字段，来自 WorkBuddy 与 Codex 的原始导出。Qoder 会忽略未知字段，不影响加载。

## 🧭 来源

- `enhance-prompt` —— 从 Codex 侧用户级技能目录收编。
- UI 五件套 —— 源专家「像素君 / UI Designer」的能力拆解产物，2026-09-18 定稿。原计划按 `PUBLISH-PLAN.md` 发成 5 个独立仓库，现合并为本仓库统一维护，`topics` 与关键词布局相应整合到本文件。

## ❓ FAQ

**Q：为什么不一个专家一个大技能？**
大技能里塞满子职责后，触发不精准、输出格式容易互相打架。拆开之后每个环节可单独调用、单独迭代，串起来仍是完整流水线。

**Q：这些技能会改我的代码吗？**
不会。六个技能全部只产出文本/CSS/Markdown，不执行命令、不写文件。`enhance-prompt` 更是明确禁止执行增强后的指令。

**Q：能商用吗？**
MIT，可自由用于个人与商业项目。

## 📄 License

MIT © [JIANGEPLUS](https://github.com/JIANGEPLUS) — 见 [LICENSE](LICENSE)
