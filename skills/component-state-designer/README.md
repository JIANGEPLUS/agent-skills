# component-state-designer

> Design base component variants and full state matrices — buttons, forms, navigation, feedback, and data display with hover/active/focus/disabled plus loading/error/empty states. 组件库与状态设计：五类基础组件 + 完整状态矩阵，输出可直接落地的组件 CSS。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Platform](https://img.shields.io/badge/Agent%20Skills-compatible-blueviolet.svg)

## ✨ Features / 功能特性

- **Five component families** — buttons, form elements, navigation, feedback (alert/toast/modal), data display (card/table/badge) 五类基础组件
- **Variant & size specs** — primary/secondary/tertiary × sm/md/lg 变体与尺寸规格
- **Full state matrices** — default/hover/active/focus-visible/disabled + loading/error/empty 完整状态矩阵
- **Token-driven CSS** — BEM naming, all values reference design tokens 令牌驱动、BEM 命名
- **Accessibility built-in** — visible focus rings, 44px touch targets, non-color-only state cues 无障碍内建

## 📦 Installation / 安装

将本目录整体放入 `~/.qoder/skills/<name>/`（Qoder）、`~/.codex/skills/<name>/`（Codex）或 `~/.claude/skills/<name>/`，新会话自动发现。
Copy this folder into the client's user-level skills directory; the skill is auto-discovered on the next session.

## 🚀 Usage / 使用

```text
给我们的设计系统补一个完整的按钮组件，各种状态都要有
```

输出组件 CSS + Markdown 状态矩阵表。
Outputs component CSS plus a state-matrix table.

## 🔑 Keywords / 关键词

`component library` · `ui components` · `component states` · `design system` ·
`bem` · `micro-interactions` · `ui design` · `组件库` · `组件设计` · `交互状态`

## ⚙️ Prerequisites / 前置条件

建议配合设计令牌使用（如 design-token-crafter 产物）；无令牌时自动内联默认值。Works standalone; pairs best with a design-token system.

## 🔒 Security / 安全说明

纯提示词型 skill，不含可执行脚本，无网络请求。Prompt-only skill: no scripts, no network calls.

## 📄 License

[MIT](./LICENSE) © 2026 JIANGEPLUS

## 🏷️ Topics

`component-library` `ui-components` `design-system` `states` `bem` `ui-design` `frontend` `micro-interactions` `workbuddy` `skill`
