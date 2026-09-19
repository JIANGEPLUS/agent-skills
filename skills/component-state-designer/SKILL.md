---
name: component-state-designer
description: "组件库与状态设计 Skill。设计基础组件（按钮、表单、导航、反馈、数据展示）的变体规格与完整状态矩阵（默认/hover/active/focus/disabled + 加载/错误/空状态），输出可直接落地的组件 CSS 与状态清单。触发词：组件设计、组件库、component library、按钮样式、表单样式、组件状态、ui components、设计组件。适用场景：从令牌体系出发构建组件库、补全组件交互状态、统一组件视觉语言。"
description_zh: "设计基础组件变体与完整状态矩阵，输出组件 CSS 与状态清单"
description_en: "Design base component variants and full state matrices (hover/active/focus/disabled, loading/error/empty), outputting production-ready component CSS"
version: 1.0.0
display_name: "组件状态设计器"
display_name_en: "component-state-designer"
visibility: "public"
---

# 组件状态设计器 Skill（component-state-designer）

## 功能定位

在设计令牌体系之上，产出组件库规格：每个组件的变体、尺寸与完整状态矩阵，输出可直接使用的 CSS。不负责令牌生成与页面布局。

## 触发条件

1. 用户要求设计组件样式 / 组件库 / 组件状态。
2. 需要为既有组件补全 hover/active/focus/disabled 或加载/错误/空状态。

## 工作流程

1. 确认组件清单与优先级；未指定时默认覆盖五类：按钮、表单元素、导航、反馈（alert/toast/modal）、数据展示（card/table/badge）。
2. 为每个组件定义变体（primary/secondary/tertiary）与尺寸（sm/md/lg）。
3. 构建状态矩阵并逐一给出样式差异：交互四态 + focus-visible 焦点环 + disabled 降透明；反馈类组件补 loading/error/empty 三态。
4. 全部颜色、间距、圆角、阴影引用设计令牌变量；无令牌输入时内联合理默认值并标注可替换。
5. 触控目标 ≥44px，微动效控制在 150–300ms。

## 输出格式

组件 CSS 代码块（BEM 命名：`.btn--primary`），后附一张 Markdown 状态矩阵表（组件 × 状态 × 处理方式）。

## 约束与注意事项

- 必须包含 `:focus-visible` 焦点指示；禁止移除 outline 而不提供替代。
- 状态差异不依赖单一颜色传达（兼顾形状/图标/文字）。
- 保持组件间命名与层级一致，避免一次性内联魔法数字。

## 使用示例

```text
用户：给我们的设计系统补一个完整的按钮组件，各种状态都要有
输出：.btn 及变体/尺寸/状态 CSS + 状态矩阵表（default/hover/active/focus/disabled/loading）
```
