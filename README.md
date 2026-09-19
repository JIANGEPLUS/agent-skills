<div align="center">

# agent-skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Skills](https://img.shields.io/badge/skills-8-blue)
![Platform](https://img.shields.io/badge/Agent%20Skills-compatible-blueviolet.svg)

</div>

---

## 1. 简介

**我实际采用的 Agent 技能集合 —— 生产级 `SKILL.md`，跨客户端通用。**

适用客户端：Qoder · OpenAI Codex · Claude Code · ChatGPT，以及任何兼容 [Agent Skills](https://agentskills.io/) 开放规范的 Agent。

> **English**: Two general-purpose skills and a six-module equity-research pack, all single entry points. One sharpens the instruction before work starts; another carries a full UI-designer workflow — tokens, component states, responsive layout, WCAG AA audit, developer handoff — behind one name; the remaining six cover equity research end to end. Plain `SKILL.md` folders, auto-discovered with zero configuration.

---

## 2. 收录的技能

### 2.1 通用技能

| Skill | 职责 | 输出 |
|---|---|---|
| [`enhance-prompt`](skills/enhance-prompt/) | 改写模糊指令：消除歧义指代、补全目标/范围/约束/输出格式、假设显式标注、只增强不执行 | `<enhanced-prompt>` 单条增强指令 |
| [`ui-designer`](skills/ui-designer/) | 像素君 UI 设计师：设计令牌 → 组件状态矩阵 → 响应式布局 → WCAG AA 审计 → 开发交付，五阶段可全跑也可单点调用 | 令牌 CSS / BEM 组件 CSS + 状态矩阵 / 栅格 CSS + 断点表 / 分级整改清单 / 规格卡 + QA 清单 |

`ui-designer` 内部结构：

```text
ui-designer
├── 1 设计令牌 ──┬── 2 组件与状态 ──┬── 5 开发交付
│               └── 3 响应式布局 ──┘
└── 4 WCAG AA 审计（横切，任一阶段后均可插入；问题回灌 1–3 修正后才进 5）
```

### 2.2 Equity Research Pack（股票研究专家「严估深」）

由股票研究专家「严估深」拆解而来的 6 个模块，每个都是可独立调用的入口，也可由 `equity-research` 总纲路由：

| Skill | 职责 |
|-------|------|
| [`equity-research`](skills/equity-research/SKILL.md) | 总纲 / 路由、PM 七问、数据与评级纪律 |
| [`fundamentals-analysis`](skills/fundamentals-analysis/SKILL.md) | 公司速览卡、业绩前瞻与解读、模型更新 |
| [`valuation`](skills/valuation/SKILL.md) | 三表建模、WACC、DCF、可比估值、敏感性、目标价 |
| [`research-report`](skills/research-report/SKILL.md) | 首次覆盖、投资备忘录、多空推介、行业综述、晨会纪要 |
| [`risk-monitoring`](skills/risk-monitoring/SKILL.md) | 仓位与对冲、论点跟踪、催化剂日历、事件情景分析 |
| [`idea-screening`](skills/idea-screening/SKILL.md) | 量化筛选、主题价值链扫描、一页纸想法卡 |

包级说明见 [`skills/equity-research/README.md`](skills/equity-research/README.md)，完整规范见 [`skills/equity-research/SPEC.md`](skills/equity-research/SPEC.md)。

> 金融类技能输出均为研究参考，不构成个人投资建议。

---

## 3. 安装

**整包装入某个客户端**（用户级，对该用户所有项目生效）：

```bash
git clone https://github.com/JIANGEPLUS/agent-skills.git
cp -r agent-skills/skills/* ~/.qoder/skills/      # Qoder
# cp -r agent-skills/skills/* ~/.codex/skills/    # Codex
# cp -r agent-skills/skills/* ~/.claude/skills/   # Claude Code
```

**只装单个技能**：`skills/` 下每个目录彼此独立，直接拷走即可。

新会话自动发现，无需注册、无配置文件改动、无重启。

---

## 4. 使用与调用示例

### 4.1 调用方式

显式点名（推荐，行为最可控），或不点名、直接描述任务，由 Agent 按各 `SKILL.md` 的 `description` 触发词隐式匹配。

### 4.2 通用技能

```text
/enhance-prompt  帮我把这个需求说清楚

从品牌色 #0ea5e9 开始，把设计系统整套做出来并交给前端    # ui-designer 全五阶段
品牌主色 #7c3aed，生成一套设计令牌，要暗色模式            # ui-designer 仅阶段 1
检查 #6b7280 放在 #f9fafb 上能否过 WCAG AA                # ui-designer 仅阶段 4
```

### 4.3 Equity Research Pack

```text
$equity-research       帮我研究宁德时代，给出评级、目标价和关键催化
$fundamentals-analysis 做一份贵州茅台 2026Q2 业绩点评
$valuation            给比亚迪建 DCF 模型，做 WACC × 永续增速敏感性
$research-report      写一份立讯精密首次覆盖报告（Task 1）
$risk-monitoring      仓位该给多大？如何对冲？止损怎么设
$idea-screening       筛一批 AI 基建主题的中盘股
```

---

## 5. 仓库结构

```text
agent-skills/
├── README.md
├── LICENSE                       # MIT，覆盖全部技能
└── skills/
    ├── enhance-prompt/
    │   ├── SKILL.md              # 技能正文（Agent 读这个）
    │   └── README.md             # 面向人的说明
    ├── ui-designer/
    │   ├── SKILL.md
    │   └── README.md
    ├── equity-research/          # Equity Research Pack 总纲 + 包级文档
    │   ├── SKILL.md
    │   ├── README.md
    │   ├── SPEC.md
    │   ├── agents/openai.yaml
    │   └── references/
    ├── fundamentals-analysis/
    ├── valuation/
    ├── research-report/
    ├── risk-monitoring/
    └── idea-screening/
```

每个技能目录固定两文件：`SKILL.md`（规范正文）+ `README.md`（人读的安装与用法）。许可证集中在根目录，不做每技能一份。

`Equity Research Pack` 的模块目录在此基础上另有 `agents/openai.yaml`（Codex 显示名）与 `references/`（深度参考文档），详见 [`SPEC.md`](skills/equity-research/SPEC.md)。

---

## 6. SKILL.md 约定

### 6.1 frontmatter

只依赖 `name` 与 `description` 两个字段——这是跨客户端的最小公约集：

```yaml
---
name: ui-designer
description: "一句话职责 + 触发词列表 + 适用场景"
---
```

### 6.2 正文结构

固定六节：**功能定位 / 触发条件 / 工作流程 / 输出格式 / 约束与注意事项 / 使用示例**。

### 6.3 三条硬规则

判断一个技能值不值得留的标准：

1. **边界清晰** —— 明确写出"不负责什么"，避免技能之间互相抢活。
2. **输出格式写死** —— 每个阶段各自的产出规范都定死，不给格式的技能等于没给。
3. **约束可验证** —— 例如"对比度必须给出算过的比值，不接受'提高对比度'这类空话"。

### 6.4 扩展字段

部分技能带有 `description_zh` / `display_name` / `visibility` 等扩展字段，来自 WorkBuddy 与 Codex 的原始导出。Qoder 会忽略未知字段，不影响加载。

---

## 7. 设计取舍：一个入口，还是拆成多个

这里有过一次反复，值得记下来。

`ui-designer` 最初被拆成 5 个独立技能（`design-token-crafter`、`component-state-designer`、`responsive-layout-blueprint`、`wcag-accessibility-checker`、`design-handoff-writer`），理由是职责单一、便于单独迭代。用下来发现两个实际问题：

- **记名字成本高**。五个环节各自都要手动点名，而真实任务常常横跨其中三四个。
- **触发词互相抢**。五份 `description` 里都含 `ui-design`、`design-system`、`frontend`，只说"帮我做 UI"时命中哪个是随机的，且单个技能不会自己往下游走，链路断在手里。

所以 2.0.0 合并为单入口，**但把"职责单一"从技能层下沉到阶段层**：内部仍是五个边界清晰的阶段，各自的约束和输出格式逐条保留、一字未减；要单点调用只说那一件事即可。

判断标准也随之改写：拆分的依据不是"职责要不要单一"，而是**这些职责是否会被独立且高频地调用**。会——拆成多个技能；总是连着用——合成一个技能，内部分阶段。

`enhance-prompt` 是前者的例子：它只改指令、从不执行，与任何实施技能都不连着触发，所以保持独立。

---

## 8. 来源

- `enhance-prompt` —— 从 Codex 侧用户级技能目录收编。
- `ui-designer` —— 源专家「像素君 / UI Designer」的能力拆解产物（2026-09-18 定稿为 5 个技能），2026-09-20 合并为单入口 v2.0.0。原 `PUBLISH-PLAN.md` 规划的"5 个独立仓库"方案一并作废，统一由本仓库承载。
- `Equity Research Pack` —— 源专家「严估深 / EquityResearchExpert」专家插件（v2.1.0：1 个 agent + 16 个内置 skill + 3 份规则）按职责重构为 6 个模块。

---

## 9. 常见问题

**Q：合并成一个技能，会不会又变回"什么都能干"的大技能？**

不会。`ui-designer` 依然只产出设计规格与 CSS，不碰业务逻辑与后端；五个阶段各有固定输出格式和硬约束。合并的是入口，不是边界。

**Q：我只想要无障碍检查，会被强推整套流程吗？**

不会。技能正文明确写了"用户只要求某一阶段时，只跑该阶段，不要顺带产出其它阶段"。

**Q：这些技能会改我的代码吗？**

不会。两个技能全部只产出文本与 CSS，不执行命令、不写文件。`enhance-prompt` 更是明确禁止执行增强后的指令。

**Q：能商用吗？**

MIT，可自由用于个人与商业项目。

---

## 10. 许可

MIT © [JIANGEPLUS](https://github.com/JIANGEPLUS) — 见 [LICENSE](LICENSE)


## Algorithm Engineer Pack（高级算法工程师「小算」）

由高级算法工程师「小算」拆解而来的 6 个模块，每个都是可独立调用的入口，也可由 `algorithm-engineer` 总纲路由：

| Skill | 职责 |
|-------|------|
| [algorithm-engineer](skills/algorithm-engineer/SKILL.md) | 总纲 / 路由、核心职责、能力栈、主线流程与决策准则 |
| [algorithm-modeling](skills/algorithm-modeling/SKILL.md) | 问题契约、建模与基线、算法选型方向表 |
| [algorithm-proof](skills/algorithm-proof/SKILL.md) | 正确性证明义务、复杂度账本、保证范围界定 |
| [algorithm-domain-checks](skills/algorithm-domain-checks/SKILL.md) | 图/树、字符串、数论组合、几何的易错前提核查 |
| [algorithm-applied](skills/algorithm-applied/SKILL.md) | 数值与约束优化、机器学习/推荐/检索、调度与分布式 |
| [algorithm-implementation](skills/algorithm-implementation/SKILL.md) | 代码契约、分层验证、对拍与可复现性能记录 |

包级说明见 [skills/algorithm-engineer/README.md](skills/algorithm-engineer/README.md)，完整规范见 [skills/algorithm-engineer/SPEC.md](skills/algorithm-engineer/SPEC.md)。
