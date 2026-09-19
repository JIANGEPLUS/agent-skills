# 完整说明（SPEC）

本文档定义「严估深」股票研究技能包的文件结构、字段规范、模块职责边界与维护方式。

---

## 1. 来源与拆解逻辑

源专家：`EquityResearchExpert`（严估深，股票研究专家，v2.1.0）

组成：1 个 agent 主文档 + 16 个内置 skill + 3 份规则文档

拆解原则：**按"一次调用要交付什么"划分职责边界**，而非按源 skill 数量一比一照搬。16 个源 skill 合并为 6 个模块，消除重叠（如 `earnings-preview` 已废弃，并入 `fundamentals-analysis`）。

| 模块 | 合并的源 skill | 保留的规则/参考 |
|------|--------------|----------------|
| `equity-research` | agent 主文档（15 项职责 + PM 七问） | `equity_research_rules`、`deliverable-framework` |
| `fundamentals-analysis` | `earnings-analysis`（含 preview/analysis）、`company-tearsheet`、`model-update` | earnings-analysis 的 3 篇 references |
| `valuation` | `dcf-model-builder`、`comps-valuation` | `equity-valuation-standard` |
| `research-report` | `initiating-coverage`、`memo-builder`、`long-short-pitch`、`sector-overview`、`morning-note` | initiating-coverage 的 6 篇 references + 2 份 assets |
| `risk-monitoring` | `portfolio-risk`、`thesis-tracker`、`catalyst-calendar`、`event-scenario-analyzer` | — |
| `idea-screening` | `idea-generation` | — |

---

## 2. 目录结构

本包遵循 `agent-skills` 仓库的扁平约定，每个模块是一个独立目录（`skills/<name>/SKILL.md`）。

```text
skills/
├── equity-research/                # 总纲 / 路由 + 包级文档
│   ├── SKILL.md
│   ├── README.md                   # 包总览与安装使用（简明说明）
│   ├── SPEC.md                     # 本文件（完整说明）
│   ├── agents/openai.yaml
│   └── references/
│       ├── data-timeliness.md      # 财务数据时效性规则
│       └── deliverable-framework.md  # 交付物规范
├── fundamentals-analysis/
│   ├── SKILL.md
│   ├── README.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── workflow.md             # Analysis 模式详细步骤
│       ├── report-structure.md     # 报告页面模板
│       └── best-practices.md       # 质量清单
├── valuation/
│   ├── SKILL.md
│   ├── README.md
│   ├── agents/openai.yaml
│   └── references/valuation-standard.md
├── research-report/
│   ├── SKILL.md
│   ├── README.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── task1-company-research.md
│       ├── task2-financial-modeling.md
│       ├── task3-valuation.md
│       ├── task4-chart-generation.md
│       ├── task5-report-assembly.md
│       ├── valuation-methodologies.md
│       ├── report-template.md
│       └── quality-checklist.md
├── risk-monitoring/
│   ├── SKILL.md
│   ├── README.md
│   └── agents/openai.yaml
└── idea-screening/
    ├── SKILL.md
    ├── README.md
    └── agents/openai.yaml
```

模块总数：6 个 `SKILL.md` + 6 个 `README.md` + 6 个 `openai.yaml` + 1 个 `SPEC.md` + 14 篇 references。

---

## 3. SKILL.md 字段定义

`SKILL.md` 顶部为 YAML frontmatter，Codex 仅强制要求 `name` 与 `description`，其余为标准可选字段。

| 字段 | 必需 | 说明 | 约束 |
|------|------|------|------|
| `name` | ✅ | 技能唯一标识，同时决定目录名与显式调用名（`$name`） | 小写字母 + 连字符，≤64 字符，与目录名一致 |
| `description` | ✅ | 触发判断依据：能力 + TRIGGER / DO NOT TRIGGER + 触发词 | 触发词前置；写清适用与不适用边界；会被截断时仍能命中 |
| `license` | 可选 | 分发许可 | 本项目统一 `MIT` |
| `metadata.version` | 可选 | 模块版本 | 语义化版本 |
| `metadata.category` | 可选 | 分类 | `finance-equity-research` |
| `metadata.origin` | 可选 | 来源标识 | `workbuddy-expert/equity-research` |
| `metadata.language` | 可选 | 主语言 | `zh-CN` |
| `metadata.modules` | 可选 | 关联模块（仅总纲使用） | 模块名数组 |

### 3.1 agents/openai.yaml

Codex CLI 专有，其他 Agent 忽略：

```yaml
display_name: "Equity Research"   # 选择器中的显示名
icon: "trending-up"                # 图标标识
```

### 3.2 正文结构约定

能力清单 → 工作流（分阶段 Step/Phase）→ 输出模板 → 注意事项/纪律 → 参考文档索引。

---

## 4. 模块职责边界

| 场景 | 使用模块 |
|------|---------|
| 不知道该用什么能力 | `equity-research`（路由） |
| 了解公司基本面 / 解读财报 / 更新估计 | `fundamentals-analysis` |
| 建模、算 WACC、做 DCF/Comps、算目标价 | `valuation` |
| 写覆盖报告、备忘录、推介、行业综述、晨报 | `research-report` |
| 定仓位、设止损、跟踪论点、排催化、算事件影响 | `risk-monitoring` |
| 从零找标的、跑筛选、扫主题 | `idea-screening` |

**避免越界**：`valuation` 不写完整报告；`research-report` 不重复建模；`risk-monitoring` 不重算估值（引用 `valuation` 的结果）。

---

## 5. 扩展方式

### 5.1 新增模块

1. 在 `skills/` 下新建目录，目录名 = `name`（小写连字符）
2. 编写 `SKILL.md`：`description` 中前置触发词、写清 DO / DO NOT 边界
3. 如需 Codex 显示名，加 `agents/openai.yaml`
4. 深度内容（>200 行）拆到 `references/`，在正文中用相对路径索引
5. 编写模块 `README.md`（职责边界、触发条件、输入输出、使用要点）
6. 更新 `skills/equity-research/README.md` 的模块表与调用示例

### 5.2 新增参考文档

放入模块 `references/` 目录，并在 `SKILL.md` 末尾建立索引表（主题 → 文件）。保持 SKILL.md 精简，让 Agent 按需加载 references。

### 5.3 跨模块复用

如需共享估值口径或模板，放进使用频率最高的模块，其余模块用相对路径引用，避免复制导致口径漂移。

---

## 6. 维护规范

- **版本**：模块内容实质变更时递增 `metadata.version`；结构调整同步更新本文件目录树
- **内容校验**：每次改动后确认 YAML frontmatter 可被解析、`name` 与目录名一致、相对链接有效
- **金融合规底线**（改动时不得删除）：
  1. 数据标注来源与日期，缺失 `[MISSING]`、陈旧 `[STALE]`
  2. 结论带评级 + 目标价 + 时间维度
  3. 论点带可证伪条件
  4. 多空双向呈现
  5. 末尾免责声明："本报告仅供研究参考，不构成个人投资建议"
- **上游同步**：源专家升级（新增 skill 或改动规则）时，评估是否需要新增模块或更新 references；保持 `metadata.origin` 记录来源版本

---

## 7. 推送与同步

仓库：`JIANGEPLUS/agent-skills`（默认分支 `main`）。

提交粒度建议：一个逻辑变更一个 commit，message 采用 `type(scope): subject`（如 `feat(skills): add valuation module`）。
