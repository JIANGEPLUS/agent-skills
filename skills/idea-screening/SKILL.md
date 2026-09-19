---
name: idea-screening
description: >
  Systematic stock screening and investment idea sourcing: value / growth /
  quality / short / special-situation screens, thematic value-chain sweeps, and
  one-page idea writeups. TRIGGER when: the user asks for new investment ideas,
  wants to run a screen, scan a theme (AI, reshoring, aging demographics), or
  asks "what looks interesting". DO NOT TRIGGER for: deep analysis of a
  specific named company (use fundamentals-analysis / valuation), or writing up
  an existing idea (use research-report).
  触发词：选股、筛选、stock screen、找标的、投资想法、idea generation、主题扫描、有什么可看的。
license: MIT
metadata:
  version: 1.0.0
  category: finance-equity-research
  origin: workbuddy-expert/equity-research
  language: zh-CN
---

# 选股与创意生成（Idea Screening）

从全市场筛出候选标的，输出"值得深挖"的短名单——**筛选产生候选，不产生结论**。

## Step 1：定义筛选条件

先向用户确认：方向（Long / Short / 两者）、市值（大/中/小/微）、行业（特定或跨行业）、风格（价值/成长/质量/特殊情形/事件驱动）、地域、主题（AI、回流、老龄化等）。

## Step 2：量化筛选

**价值筛选**
- P/E 低于行业中位数
- EV/EBITDA 低于历史均值
- 自由现金流收益率 >5%
- P/B <1.5x
- 近 90 天内部人买入
- 股息率高于市场平均

**成长筛选**
- 收入同比增速 >15%
- 盈利同比增速 >20%
- 增速加速（增速本身在上升）
- 利润率扩张
- ROIC >15%
- SaaS 净留存 >110%

**质量筛选**
- 收入连续 5 年以上增长
- 利润率稳定或扩张
- ROE >15%
- 低负债率
- 高自由现金流转化率
- 内部人持股 >5%

**做空筛选**
- 收入下滑或增速放缓
- 利润率压缩
- 应收/存货增速高于销售
- 内部人卖出
- 无理由的估值溢价
- 高空头持仓 + 基本面恶化
- 会计红旗（更换审计师、财报重述）

**特殊情形**
- 近期 IPO / SPAC 解禁
- 12 个月内分拆
- 刚走出重组的公司
- 积极主义投资者介入
- 落后公司换管理层

## Step 3：主题扫描

1. 定义主题论点（例："AI 基建支出在 2026 年前加速"）
2. 绘制价值链——直接受益 vs 间接受益
3. 区分纯标的与多元化标的
4. 判断哪些已被定价、哪些未被充分认识
5. 寻找市场尚未关联的**二阶受益者**

## Step 4：想法呈现

每个通过筛选的标的：

**[公司名] — [Long/Short] — [一句话论点]**

| 指标 | 数值 | vs 同业 |
|------|------|--------|
| 市值 | | |
| EV/EBITDA (NTM) | | |
| P/E (NTM) | | |
| 收入增速 | | |
| EBITDA 利润率 | | |
| FCF 收益率 | | |

- **论点（3-5 条）**：为什么被错误定价、市场忽略了什么、价值兑现的催化剂
- **关键风险**：什么会让这个判断错了
- **建议下一步**：建完整模型？深度尽调？专家访谈？

## Step 5：输出

- 5-10 个标的的一页纸短名单
- 筛选条件与方法论说明
- 横向对比表
- **优先级排序**：先研究哪些

## 纪律

- 筛出来的只是候选，每个都要接基本面工作
- 最好的想法常在交集处（例如"因短期逆风而以便宜价格买到的高质量公司"）
- 避开拥挤交易——查持仓结构、空头比例、覆盖分析师数量
- 逆向想法必须有催化剂——没有催化的抢跑等同于错误
- 跟踪想法的命中率，复盘哪类筛选最有效
- 做空想法需要更高信心：时点更难、风险不对称

> 本模块输出为研究参考，不构成个人投资建议。
