---
name: wcag-accessibility-checker
description: "无障碍合规检查 Skill。按 WCAG AA 标准审计界面设计：颜色对比度（4.5:1 / 3:1）、键盘可达性、ARIA 标注、触控目标尺寸、动效偏好、文本缩放兼容，输出分级的通过/整改清单与修复建议。触发词：无障碍、accessibility、a11y、WCAG、对比度检查、屏幕阅读器、键盘导航、可访问性审计。适用场景：上线前无障碍验收、设计评审合规检查、修复无障碍问题。"
description_zh: "按 WCAG AA 审计界面：对比度/键盘/ARIA/触控目标，输出整改清单"
description_en: "Audit interfaces against WCAG AA: contrast, keyboard navigation, ARIA, touch targets; output a prioritized remediation checklist"
version: 1.0.0
display_name: "无障碍合规检查器"
display_name_en: "wcag-accessibility-checker"
visibility: "public"
---

# 无障碍合规检查器 Skill（wcag-accessibility-checker）

## 功能定位

对设计稿、界面描述或前端代码执行 WCAG AA 合规审计，输出可执行的整改清单。只负责无障碍审计，不负责整体视觉设计。

## 触发条件

1. 用户要求无障碍检查 / WCAG 合规 / 对比度审计。
2. 上线前验收、或有用户反馈可访问性问题。

## 工作流程

1. 收集审计对象：颜色组合、组件描述或 HTML/CSS 片段。
2. 逐项核对六大维度：
   - 对比度：正文 4.5:1、大字（≥24px 或 ≥18.66px bold）3:1、UI 组件边界 3:1；
   - 键盘：全部功能可 Tab 触达，焦点顺序合理，焦点环可见；
   - 屏幕阅读器：语义化标签、图片 alt、表单 label 关联、必要 ARIA；
   - 触控目标：≥44×44px 且间距充足；
   - 动效：尊重 `prefers-reduced-motion`，无非必要自动动画；
   - 缩放：200% 文本缩放不破版。
3. 每项判定 通过 / 不通过 / 无法判定（需运行时验证），不通过的给出具体修复建议（如替换后的色值对）。
4. 按严重程度排序：阻断（无法操作）→ 严重（难以使用）→ 一般（体验降级）。

## 输出格式

Markdown 审计报告：结果汇总表（维度 | 判定 | 问题 | 修复建议）+ 按严重度分组的整改清单 + 兜底说明（需真机/读屏验证项）。

## 约束与注意事项

- 对比度计算基于 WCAG 相对亮度公式，给出计算后的比值而非仅结论。
- 不凭空断言运行时行为；无法静态判定的项明确标注"需运行时验证"。
- 修复建议必须可执行（给出具体色值/代码改法），不接受"提高对比度"这类空话。

## 使用示例

```text
用户：检查这套配色 #6b7280 文字放在 #f9fafb 背景上能不能过 AA
输出：对比度计算结果 + 判定 + 不达标时给出可替换的达标色值对
```
