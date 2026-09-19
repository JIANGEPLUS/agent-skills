---
name: research-report
description: >
  Institutional research writing: initiating coverage reports (5-task workflow),
  investment committee memos, long/short pitches, sector overviews, and morning
  notes. TRIGGER when: the user asks to write an initiation report, investment
  memo / IC memo, long or short pitch, sector/industry report, morning meeting
  note, or a bull/bear case writeup. DO NOT TRIGGER for: raw modeling work
  (use valuation), earnings data crunching (use fundamentals-analysis), or
  position sizing rules (use risk-monitoring).
  触发词：首次覆盖、initiating coverage、投资备忘录、IC memo、多空推介、pitch、行业综述、sector overview、晨会纪要、morning note。
license: MIT
metadata:
  version: 1.0.0
  category: finance-equity-research
  origin: workbuddy-expert/equity-research
  language: zh-CN
---

# 研报与推介撰写（Research Report Writing）

五种交付形态：**首次覆盖** / **投资备忘录** / **多空推介** / **行业综述** / **晨会纪要**。

---

## A. 首次覆盖（Initiating Coverage）

机构级标准（JPM / GS / MS 格式），5 个任务：

| Task | 内容 | 依赖 | 产出 |
|------|------|------|------|
| 1 | 公司研究 | 无 | 6-8K 词 .md |
| 2 | 财务建模 | 无 | Excel 模型（6 个 tab） |
| 3 | 估值分析 | Task 2 | 估值 .md + 4 个 Excel tab |
| 4 | 图表生成 | 1,2,3 | 25-35 张 PNG（300 DPI）+ 索引 |
| 5 | 报告组装 | 全部 | 30-50 页 .docx |

- **并行**：Task 1 与 2 可并行；3→4→5 严格串行
- **执行规则**：一次请求只做一个 Task；开始前校验前置产出；只交付规定产物；默认 Times New Roman
- **4 张必备图**：chart_03 收入按产品（堆叠面积）、chart_04 收入按地区（堆叠柱）、chart_28 DCF 敏感性（热力图）、chart_32 估值 football field（横向条形）
- **质量标准**：所有数字带来源与时间；`[STALE]`（>90 天）/ `[MISSING]` 标注；引用为可点击链接；正文中每 200-300 字配图，图表覆盖 60-80% 版面

详细流程见 `references/task1-company-research.md` ~ `references/task5-report-assembly.md`，估值方法见 `references/valuation-methodologies.md`，模板见 `references/report-template.md`，质检见 `references/quality-checklist.md`。

---

## B. 投资备忘录（Memo）

服务于投委会决策，**强调全面、平衡、可执行，而非推销观点**。

1. **定位**：新建仓 / 加减仓 / 退出 / 观察名单
2. **公司概况**：一句话业务；市值/EV、收入利润增速、行业 KPI；股东结构与治理；近期股价与催化
3. **投资论点**：核心论点 2-3 句 + 3-5 个论点支柱（陈述 + 定量证据 + 信心高/中/低）+ 市场认知差异
4. **估值与回报**：方法论 + 情景表（情景/概率/目标价/回报/关键假设）+ 概率加权期望回报 + 机会成本对比
5. **风险**：Top 5 风险（概率/影响/缓释）+ **证伪条件** + 最差情景最大损失
6. **执行计划**：建仓方式（一次性 vs 分批）、目标仓位、加减仓规则、止损纪律、持有期、流动性评估
7. **结论**：明确 Buy/Sell/Hold/Watchlist + 信心水平 + 待确认事项 + 下次复盘时间

**硬性要求**：情景概率权重合计 100%；证伪条件必须可观察、可量化、有时间约束；不接受"择机建仓"这类模糊表述；证据不足就写"低信心"。

---

## C. 多空推介（Long/Short Pitch）

1. **定位**：Long / Short；受众（Long-only PM / L-S HF / 卖方）；时间维度（<3 月事件 / 3-12 月论点 / >1 年结构性）
2. **变异认知**：市场共识是什么 → 我们哪里不同 → 信息边际 → 错误定价程度值多少 alpha
3. **论点支柱**（3-5 个）
   - Long：业务质量/护城河、增长驱动/拐点、估值吸引力、催化剂、管理层
   - Short：盈利质量/会计红旗、行业逆风、估值泡沫、负面催化、治理风险
4. **催化路径**：未来 3-12 个月具体事件 + 时间节点 + 影响 + 概率 + "如果-那么"路径图
5. **估值支撑**：至少两种方法；牛/基/熊三情景（概率 + 目标价）；风险回报比
6. **风险与证伪**：Top 3 风险（概率/影响/缓释）+ 明确认错条件（可观察指标 + 止损阈值）
7. **交易表达**：仓位%、入场时机方式、加减仓规则、止盈止损、对冲建议

**推介摘要卡**
```
┌─────────────────────────────────────┐
│ [LONG/SHORT] [公司] ([代码])         │
│ 当前价 ¥XX | 目标价 ¥XX (+XX%)      │
│ 止损价 ¥XX | 时间维度 X 个月         │
│ 仓位 X% | 风险回报比 X:1            │
│ 核心论点：[一句话]                   │
│ 变异认知：[市场错在哪里]             │
│ 关键催化：[最近催化]                 │
└─────────────────────────────────────┘
```
**纪律**：没有变异认知就不叫推介；区分"公司论点"与"股票论点"；催化剂必须有具体日期或窗口；风险回报比 <2:1 需额外论证；空头须考虑融券成本与挤空风险。

---

## D. 行业综述（Sector Overview）

1. **界定范围**：行业/子行业、用途、深度（5-10 页概览 vs 20-30 页深度）、角度（中立 vs 主题）、标的池
2. **市场概述**：TAM（带来源）、5 年 CAGR、预测增速与假设、细分（产品/地区/终端）、集中度 CR5、价值链、商业模式、进入壁垒
3. **趋势**：3-5 个长期顺风、逆风与风险、技术颠覆、监管、并购整合
4. **竞争格局**：Top 5-10 公司对比表（收入/增速/EBITDA 利润率/份额/差异化）+ 逐家简况 + 竞争动态（谁在抢份额、为什么）
5. **估值语境**：行业当前与历史倍数区间、溢价折价驱动、近期交易倍数、相对大盘
6. **投资含义**：最佳风险回报机会、可表达的主题、多空分歧、行业叙事拐点

**注意**：市场规模数据必须溯源；区分 TAM 炒作与真实可及市场；图表必备（市场规模瀑布、竞争定位矩阵、估值散点）。

---

## E. 晨会纪要（Morning Note）

2 分钟可读完，1 页上限，**必须有观点**。

1. **隔夜动态**：覆盖标的的财报/指引（beat-miss）、M&A、管理层变动、产品与监管、评级变动、宏观数据
2. **市场背景**：隔夜期货/盘前、行业 ETF、商品汇率、今日关键经济数据
3. **格式**
```
[日期] Morning Note — [分析师] / [覆盖行业]
Top Call：[一句话 - PM 最需要听到的]
  - 2-3 句：发生了什么、为什么重要
  - 影响：目标价、评级重申/调整
隔夜动态：
  - [公司A]：一句话 + 我们的观点
今日关键事件：[时间] [事件]
交易想法：[Long/Short] [公司]：1-2 句论点 + 催化；风险：什么会让这错了
```
4. **快速点评表**：指标 | 共识 | 实际 | Beat/Miss → 我们的观点（2-3 句）→ 行动（维持/上调/下调、调目标价）

**注意**：只汇总新闻无观点等于没写；"无重大事件"也是有效的晨报（说明维持仓位）；标注撰写时点；错了就在次日晨报认账。

---

## 通用规范

- 所有交付物结尾："本报告仅供研究参考，不构成个人投资建议"
- 数字必带来源与截至日期；缺失 `[MISSING]`，陈旧 `[STALE]`
- 输出语言与用户一致；正式文档默认 Times New Roman
