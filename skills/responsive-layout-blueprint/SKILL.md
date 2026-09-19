---
name: responsive-layout-blueprint
description: "响应式布局框架 Skill。生成 mobile-first 的响应式布局方案：断点策略（320/640/768/1024/1280）、12 列栅格、容器宽度、间距适配，以及组件跨断点的行为规格。触发词：响应式设计、responsive、断点、栅格系统、grid布局、mobile first、自适应布局、breakpoints。适用场景：新项目响应式框架搭建、页面多端适配方案、栅格与容器规范制定。"
description_zh: "生成 mobile-first 响应式布局：断点/栅格/容器/组件行为规格"
description_en: "Generate mobile-first responsive layout frameworks: breakpoints, 12-column grid, container widths, and component behavior specs"
version: 1.0.0
display_name: "响应式布局蓝图"
display_name_en: "responsive-layout-blueprint"
visibility: "public"
---

# 响应式布局蓝图 Skill（responsive-layout-blueprint）

## 功能定位

为项目产出响应式布局基础设施：断点体系、栅格、容器与组件自适应行为规格。只负责布局框架，不产出具体页面视觉稿。

## 触发条件

1. 用户要求响应式方案 / 断点设计 / 栅格系统 / 多端适配。
2. 页面在移动端或大屏出现布局塌陷，需要系统性适配规范。

## 工作流程

1. 确认目标设备范围与内容形态；未指定时采用标准五档断点：base（320–639）、sm（640+）、md（768+）、lg（1024+）、xl（1280+）。
2. 生成 mobile-first 的 `.container`（宽度阶梯 + 水平内边距递增）与 12 列 `.grid` 栅格（`sm:grid-cols-2` 式类名）。
3. 为关键组件定义跨断点行为：导航折叠策略、卡片列数变化、表格在窄屏降级为卡片。
4. 输出断点速查表：每档宽度范围、典型设备、布局要点。
5. 全部尺寸引用间距令牌；媒体查询使用 `min-width` 单向递进。

## 输出格式

CSS 代码块（container/grid/媒体查询）+ Markdown 断点速查表（断点 | 范围 | 设备 | 布局策略）。

## 约束与注意事项

- 一律 mobile-first（min-width），禁止 max-width 混用造成覆盖混乱。
- 触控目标 ≥44px；窄屏下不隐藏核心操作入口。
- 不依赖具体 UI 框架，输出为可直接粘贴的原生 CSS。

## 使用示例

```text
用户：我们要支持手机、平板、桌面三端，帮我定一套响应式规范
输出：五档断点 CSS + 12 列栅格 + 组件行为说明 + 断点速查表
```
