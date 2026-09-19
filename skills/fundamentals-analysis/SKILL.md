---
name: fundamentals-analysis
description: >
  Company fundamentals and earnings analysis. Produces one-page tearsheets,
  pre-earnings previews (consensus, scenarios, catalysts), post-earnings deep
  dives (beat/miss, estimate revisions, thesis impact), and model updates after
  new actuals or guidance. TRIGGER when: the user asks for a company tear-sheet
  or overview, earnings analysis/preview, quarterly results interpretation,
  plugging earnings into a model, or refreshing estimates. DO NOT TRIGGER for:
  valuation-only requests (use valuation), report writing (use research-report),
  or position sizing (use risk-monitoring).
  触发词：公司速览、tearsheet、财报分析、业绩前瞻、季报解读、业绩点评、模型更新、更新预测。
license: MIT
metadata:
  version: 1.0.0
  category: finance-equity-research
  origin: workbuddy-expert/equity-research
  language: zh-CN
---

# 基本面与盈利分析（Fundamentals & Earnings）

覆盖三种交付形态：**公司速览卡**、**盈利分析（前瞻/深度）**、**模型更新**。

---

## A. 公司速览卡（Tearsheet）

5 分钟建立认知，不做深度分析，适合作为深度工作的前置步骤。

### 采集清单
1. **基础信息**：公司名、代码、交易所、行业；成立/上市日期、总部、员工数；CEO/CFO
2. **业务**：一句话商业模式；收入结构（业务线/产品/区域）；护城河与竞争对手
3. **财务**：最新报告期收入/增速、毛利率、净利率、ROE、ROIC、资产负债率、经营现金流；3-5 年趋势
4. **估值**：市值/EV；P/E、EV/EBITDA、P/B、P/S；3-5 年估值区间与当前分位
5. **股东与流动性**：前十大股东、机构/散户比例、日均成交额
6. **催化与风险**：未来 3 个月关键事件；Top 3 亮点；Top 3 风险

### 输出格式
```
┌─────────────────────────────────────────────────┐
│  [公司名称] ([代码])  |  [行业]                   │
│  市值: ¥XXX亿  |  EV: ¥XXX亿  |  股价: ¥XX      │
├─────────────────────────────────────────────────┤
│  一句话: [做什么，怎么赚钱]                       │
├─────────────────────────────────────────────────┤
│  关键财务 (最新报告期: YYYY-Qx)                   │
│  收入: ¥XXX亿 (YoY +XX%)  | 净利润: ¥XX亿        │
│  毛利率 XX% | 净利率 XX% | ROE XX%               │
├─────────────────────────────────────────────────┤
│  估值: P/E XXx | EV/EBITDA XXx | P/B XXx         │
│  3Y PE 区间: XXx-XXx (当前分位 XX%)              │
├─────────────────────────────────────────────────┤
│  催化剂            │  风险                        │
│  • [事件]-[日期]   │  • [风险1-3]                 │
│  亮点: [1-3]       │                              │
├─────────────────────────────────────────────────┤
│  数据截至: YYYY-MM-DD | 仅供研究参考              │
└─────────────────────────────────────────────────┘
```
未获取数据标注 `[未披露]`；追求快速，不是深度。

---

## B. 盈利分析（Preview / Analysis 双模式）

**模式判断**：确认公司与报告季度 → 搜索该季业绩是否已发布 → 已发布走 Analysis，未发布走 Preview。

### Preview 模式（业绩前瞻）
1. **采集共识**：收入/EPS 共识、关键分部指标、上季管理层指引、业绩日期（盘前/盘后）
2. **观测框架**：财务（收入/EPS vs 共识、毛利率/营业利润率、FCF、指引）+ 运营（行业 KPI：SaaS 看 ARR/NRR，零售看同店，工业看订单簿）
3. **情景表**：

| 情景 | 收入 | EPS | 关键驱动 | 股价反应预估 |
|------|------|-----|---------|------------|
| 牛市 | | | | |
| 基本 | | | | |
| 熊市 | | | | |

4. **催化清单**：3-5 个决定股价反应的因素；期权隐含波动率 vs 历史业绩日波动
5. **输出**：一页纸（共识表 + 观测排序 + 情景表 + 催化清单 + 交易设置）

### Analysis 模式（业绩深度）
**数据时效检查**：确认今日日期 → 搜索最新业绩 → 验证发布日在 3 个月内（否则标 `[STALE]`）

1. **Beat/Miss 判定**：收入/EPS vs 共识（金额+百分比）、关键 KPI、指引 vs 共识
2. **深度拆解**：分部/区域/产品；毛利率与费用率变动原因；电话会关键表态；一次性项目 vs 可持续趋势
3. **估计修正**：更新前瞻 EPS/收入，展示旧 vs 新 + 变动原因，说明对目标价的影响
4. **论点影响**：原逻辑强化还是弱化？是否调整评级？下一个关键验证点？
5. **输出**：8-12 页报告（摘要 → 业绩详解 → KPI 与指引 → 论点更新 → 估值与估计修正），含 8-12 张图表；文件名 `[Company]_Q[X]_[Year]_Earnings_Update.docx`

详细步骤见 `references/workflow.md`，页面模板见 `references/report-structure.md`，质量清单见 `references/best-practices.md`。

**引用标准**：每个数据点标注来源与日期；必须引用业绩公告、10-Q、电话会纪录、投资者材料、共识来源；引用须为可点击链接。

---

## C. 模型更新（Model Update）

**Step 1 识别触发源**：财报 / 指引变化 / 估计修正 / 宏观变化（利率、汇率、商品）/ 事件（并购、重组、管理层变动）

**Step 2 填入实际值**

| 科目 | 原估计 | 实际 | 差异 | 说明 |
|------|-------|------|------|------|
| 收入 | | | | |
| 毛利率 | | | | |
| 营业费用 | | | | |
| EBITDA | | | | |
| EPS | | | | |
| 关键指标 1/2 | | | | |

同步更新分部收入与利润率、现金与债务、股份数（回购/稀释）、Capex、营运资金。

**Step 3 修正前瞻估计**

| | 旧 FY | 新 FY | 变动 | 旧次年 | 新次年 | 变动 |
|---|------|------|------|-------|-------|------|
| 收入 | | | | | | |
| EBITDA | | | | | | |
| EPS | | | | | | |

明确写出：改了什么假设、为什么改（增速 old→new、利润率 old→new、新增一次性项目）。

**Step 4 估值影响**

| 方法 | 原值 | 更新后 | 变动 |
|------|------|-------|------|
| DCF 公允价值 | | | |
| P/E（NTM EPS × 目标倍数） | | | |
| EV/EBITDA（NTM × 目标倍数） | | | |
| **目标价** | | | |

**Step 5 结论**：一段话说明"变了什么、为什么、意味着什么"；是否论点级事件；维持或调整评级；新目标价与推导方法。

**纪律要点**：先与公司披露口径核对再外推；区分 GAAP 与调整后；保留估计修正历史；季度噪音要区分信号；更新后与 Street 共识对比；股份数（SBC、可转债、回购）对 EPS 影响重大。

---

## 通用纪律

- 每个数字标注来源、报告期与获取日期
- 缺失数据标 `[MISSING]`，超 90 天标 `[STALE]`
- 区分事实、管理层声明、共识、模型输出、假设、判断
- 结论末尾附："本报告仅供研究参考，不构成个人投资建议"
