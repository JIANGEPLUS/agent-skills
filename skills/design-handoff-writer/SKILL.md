---
name: design-handoff-writer
description: "设计交付规格 Skill。为开发团队生成设计交接（handoff）文档：带测量的组件规格、设计令牌对照表、组件使用指南与设计 QA 验收流程，确保实现还原度。触发词：设计交付、handoff、设计规格、开发交接、还原度、design spec、设计QA。适用场景：设计稿定稿后的开发交接、组件文档编写、实现还原度验收标准制定。"
description_zh: "生成带测量的设计交接文档：组件规格、令牌对照、使用指南与 QA 流程"
description_en: "Generate developer handoff documents: measured component specs, token references, usage guidelines, and design QA checklists"
version: 1.0.0
display_name: "设计交付文档生成器"
display_name_en: "design-handoff-writer"
visibility: "public"
---

# 设计交付文档生成器 Skill（design-handoff-writer）

## 功能定位

把设计决策转化为开发可直接执行的交接文档：测量规格、令牌对照、使用指南、QA 验收流程。只负责交付文档，不产出视觉设计。

## 触发条件

1. 用户要求设计交付 / 开发交接文档 / 组件规格说明。
2. 设计定稿后需要制定还原度验收标准。

## 工作流程

1. 收集输入：设计稿描述/截图/令牌表/组件清单；确认目标平台（Web/iOS/Android）。
2. 为每个组件输出规格卡：尺寸与间距标注（px，引用令牌名）、字体层级、颜色引用、圆角/阴影、状态差异。
3. 生成令牌对照表：设计值 ↔ CSS 变量/平台变量名，双端一致性核对。
4. 撰写使用指南：何时用/不用该组件、内容边界（字符长度、图片比例）、无障碍要求。
5. 制定设计 QA 清单：逐状态核对项（含 hover/focus/disabled/loading/empty）、响应式核对点、验收通过标准。

## 输出格式

Markdown 交接文档：规格卡（每组件一节，含测量表）→ 令牌对照表 → 使用指南 → QA 清单。测量值同时给出 px 与对应令牌名。

## 约束与注意事项

- 所有测量必须落到令牌引用，出现设计稿中的"魔法数字"时标注建议归档的令牌。
- QA 清单必须可勾选（checkbox 形式），按页面/组件分组。
- 平台差异（如 iOS 安全区、Web 滚动条宽度）单独列出，不混入通用规格。

## 使用示例

```text
用户：登录页设计定稿了，帮我写一份给前端的交接文档
输出：输入框/按钮/错误提示的规格卡（含测量与令牌引用）+ 令牌对照表 + 登录页 QA 清单
```
