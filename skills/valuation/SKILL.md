---
name: valuation
description: >
  Equity valuation modeling: three-statement linked financial model, WACC, DCF,
  comparable-company multiples, sensitivity and scenario grids, and target price
  derivation. TRIGGER when: the user asks to build a DCF or financial model,
  calculate WACC, run comps / relative valuation, do sensitivity or scenario
  analysis, or derive a price target. DO NOT TRIGGER for: earnings commentary
  (use fundamentals-analysis), writing the report itself (use research-report),
  or position sizing (use risk-monitoring).
  触发词：DCF、现金流折现、WACC、财务建模、三表模型、可比估值、comps、相对估值、敏感性分析、目标价推导。
license: MIT
metadata:
  version: 1.0.0
  category: finance-equity-research
  origin: workbuddy-expert/equity-research
  language: zh-CN
---

# 估值测算（Valuation）

从收入驱动到估值输出的完整链条：三表联动建模 → WACC → DCF → 可比估值 → 敏感性/情景 → 目标价。

---

## Phase 1：业务理解与收入驱动

1. 拆解业务结构与收入驱动因子（量×价、用户数×ARPU、门店数×坪效等）
2. 建立 3-5 年预测框架
3. 每个增长假设都要标注依据和来源

## Phase 2：三表联动建模

**利润表**：收入预测 → 成本结构（固定/可变）→ COGS 与毛利率 → 销售/管理/研发费用率 → 营业利润 → 税前利润 → 净利润

**资产负债表**：营运资金（应收/存货/应付周转天数）、Capex、固定资产与无形资产、债务结构、股东权益

**现金流量表**：经营（间接法）、投资、筹资
- FCFF = EBIT×(1−T) + D&A − Capex − ΔWC
- FCFE = FCFF − 利息×(1−T) + 净借款

**硬约束**：三表必须闭合——资产 = 负债 + 权益，现金变动一致。

## Phase 3：WACC 与 DCF

**WACC**
- Ke = Rf + β × ERP（+ 规模溢价）
- Kd = 借款利率/债券收益率 × (1−T)
- WACC = Ke × E/(D+E) + Kd × (1−T) × D/(D+E)

**DCF**
- 预测期 FCF 折现
- 终值：永续增长 TV = FCF_n×(1+g)/(WACC−g)，或退出倍数法
- EV = PV(FCF) + PV(TV)
- 股权价值 = EV − 净债务 − 少数股东权益 + 联营投资
- 每股价值 = 股权价值 / 稀释后股份数

## Phase 4：可比估值（Comps）

1. **定位**：行业/子行业、增速、规模、盈利能力、地域、业务纯度 → 确定适用指标集
2. **选 comp**：同子行业 + 类似模式；收入规模 0.3x–3x；增速与市场可比；盈利阶段一致；最终 5-10 家，逐家写选入理由
3. **计算**：市值、EV（= 市值 + 净债务 + 少数股东权益）、收入/EBITDA/净利润/FCF、增速、利润率、ROE/ROIC；历史倍数（CY、前一年）与前瞻倍数（NTM、次年）；均值/中位数/25/75 分位
4. **推导**：选 2-3 个最适用倍数 → 确定合理区间（考虑增速溢价/折价）→ 得出估值区间 → 对比市值算隐含空间
5. **判断**：溢价/折价的合理性；comp 组的局限性

**Comp 表**

```
公司 | 代码 | 市值 | EV | Rev Growth | EBITDA Margin | P/E(NTM) | EV/EBITDA(NTM) | P/S | 选入理由
均值 / 中位数
目标公司 | ... | 隐含溢/折 +/-XX%
```

## Phase 5：敏感性与情景

1. 双变量敏感性表（WACC × 永续增长率，或收入增速 × 利润率），5×5 矩阵，标注基本情景
2. 情景分析：牛市 / 基本 / 熊市（概率 + 目标价）
3. **终值占比检查**：>75% 必须警示

## 输出

**假设表**

| 假设项 | 来源/依据 | 预测值 |
|--------|----------|-------|
| 收入增速 Y1-Y3 | | |
| 长期利润率 | | |
| Capex/Revenue | | |
| WACC | 计算得出 | |
| 永续增长率 | | |

**估值总结**

| | 熊市 | 基本 | 牛市 |
|--|------|------|------|
| 每股价值 | ¥XX | ¥XX | ¥XX |
| 隐含上行/下行 | XX% | XX% | XX% |
| 终值占比 | XX% | XX% | XX% |

**目标价推导**：DCF 与 Comps（必要时加权）→ 目标价 → 相对现价空间 → 评级含义

## 注意事项

- 终值假设影响巨大，永续增长率通常不超过 GDP 增速
- WACC 各组成部分须有明确来源论证
- 周期性行业使用中周期正常化盈利
- 亏损公司不用 P/E，改用 EV/Revenue 或 P/S
- 注意会计准则差异（IFRS / GAAP / 中国准则）对倍数的影响
- 高增长溢价需量化（PEG 或增速差调整）
- 所有假设区分事实数据与分析师判断，标注来源

估值口径与披露标准详见 `references/valuation-standard.md`。

> 本模块输出为研究参考，不构成个人投资建议。
