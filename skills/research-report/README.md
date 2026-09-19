# research-report — 研报与推介撰写

股票研究技能包的一个模块，负责**把分析结论写成机构级交付物**。可独立调用，也可由 `equity-research` 总纲路由而来。

## 职责边界

| 做什么 | 不做什么 |
|--------|---------|
| 首次覆盖报告、投资备忘录、多空推介、行业综述、晨会纪要 | 建模估值（→ `valuation`，本模块引用其结果）、财报数据测算（→ `fundamentals-analysis`）、仓位规则（→ `risk-monitoring`） |

## 触发条件

首次覆盖 / initiating coverage / 投资备忘录 / IC memo / 多空推介 / pitch / 行业综述 / sector overview / 晨会纪要 / morning note / bull-bear case。

## 五种交付形态

| 形态 | 产出 | 关键要求 |
|------|------|---------|
| 首次覆盖 | 5 任务流水线：研究 → 建模 → 估值 → 图表 → 组装，30-50 页 docx | Task 1&2 可并行，3→4→5 串行；4 张必备图 |
| 投资备忘录 | 投委会决策材料 | 情景概率合计 100%；证伪条件可量化；执行计划具体 |
| 多空推介 | 摘要卡 + 7 段式推介 | 必须有变异认知；催化剂带日期；风险回报比 <2:1 需额外论证 |
| 行业综述 | 5-30 页行业报告 | TAM 必须溯源；竞争矩阵与估值散点图必备 |
| 晨会纪要 | 1 页、2 分钟可读 | 必须有观点；区分可行动事件与噪音 |

## 输入

公司/行业名；研究素材或已有分析结论（若缺失会先建议调用 `fundamentals-analysis` / `valuation`）；指定形态与时间维度。

## 使用要点

- 数字必带来源与截至日期；`[MISSING]` / `[STALE]` 标注
- 正式文档默认 Times New Roman；正文每 200-300 字配图
- 多空双向呈现；结论带评级 + 目标价 + 时间维度
- 末尾统一免责声明

## 目录

```
research-report/
├── SKILL.md
├── README.md
├── agents/openai.yaml
└── references/
    ├── task1-company-research.md      # 公司研究
    ├── task2-financial-modeling.md    # 财务建模
    ├── task3-valuation.md             # 估值分析
    ├── task4-chart-generation.md      # 图表生成
    ├── task5-report-assembly.md       # 报告组装
    ├── valuation-methodologies.md     # 估值方法论
    ├── report-template.md             # 报告结构模板
    └── quality-checklist.md           # 质检清单
```
