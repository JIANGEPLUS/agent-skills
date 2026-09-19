# design-token-crafter

> Generate complete design token systems — CSS variables for color, typography, spacing, shadows, and dark theme. 设计令牌系统生成器：颜色、字体、间距、阴影全套 CSS 变量，自带暗色主题。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Platform](https://img.shields.io/badge/Agent%20Skills-compatible-blueviolet.svg)

## ✨ Features / 功能特性

- **Color scales** — extend one brand hex into a 100–900 gradient with semantic colors (success/warning/error/info) 颜色梯度与语义色
- **Typography tokens** — font families and a 12→36px type scale 字体与字号阶梯
- **Spacing system** — 4px-based spacing ladder (4/8/12/16/24/32/48/64) 间距体系
- **Dark theme** — `[data-theme="dark"]` overrides with unchanged semantic names 暗色主题令牌
- **WCAG AA contrast** — every text/background pair is verified 对比度校验
- **Base component styles** — `.btn` / `.form-input` / `.card` consumption examples 基础组件示例

## 📦 Installation / 安装

将本目录整体放入 `~/.qoder/skills/<name>/`（Qoder）、`~/.codex/skills/<name>/`（Codex）或 `~/.claude/skills/<name>/`，新会话自动发现。
Copy this folder into the client's user-level skills directory; the skill is auto-discovered on the next session.

## 🚀 Usage / 使用

```text
品牌主色是 #7c3aed，帮我生成一套设计令牌，要支持暗色模式
```

输出 `:root` + `[data-theme="dark"]` 完整 CSS 令牌与使用说明。
Outputs complete `:root` / dark-theme token CSS with usage notes.

## 🔑 Keywords / 关键词

`design tokens` · `css variables` · `dark mode` · `theming` · `design system` ·
`color palette` · `spacing scale` · `typography scale` · `设计令牌` · `设计系统` · `CSS 变量`

## ⚙️ Prerequisites / 前置条件

无运行时依赖，输出纯 CSS。No runtime dependencies — pure CSS output.

## 🔒 Security / 安全说明

纯提示词型 skill，不含可执行脚本，无网络请求。Prompt-only skill: no scripts, no network calls.

## 📄 License

[MIT](./LICENSE) © 2026 JIANGEPLUS

## 🏷️ Topics

`design-tokens` `css-variables` `dark-mode` `theming` `design-system` `ui-design` `frontend` `workbuddy` `skill` `ai-agent`
