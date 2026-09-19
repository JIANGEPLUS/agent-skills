# responsive-layout-blueprint

> Generate mobile-first responsive layout frameworks — breakpoints, 12-column grid, container widths, and component behavior specs. 响应式布局蓝图：mobile-first 断点策略、12 列栅格、容器规范与组件跨端行为。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Platform](https://img.shields.io/badge/Agent%20Skills-compatible-blueviolet.svg)

## ✨ Features / 功能特性

- **Five-tier breakpoints** — base 320 / sm 640 / md 768 / lg 1024 / xl 1280 五档断点体系
- **Mobile-first CSS** — `min-width` only, no max-width override chaos 纯 min-width 递进
- **12-column grid** — `sm:grid-cols-2` style utility classes 12 列栅格工具类
- **Container ladder** — width + padding per breakpoint 容器宽度阶梯
- **Component behavior specs** — nav collapse, card columns, table-to-card degradation 组件跨端行为规格
- **Breakpoint cheat sheet** — range / devices / strategy table 断点速查表

## 📦 Installation / 安装

将本目录整体放入 `~/.qoder/skills/<name>/`（Qoder）、`~/.codex/skills/<name>/`（Codex）或 `~/.claude/skills/<name>/`，新会话自动发现。
Copy this folder into the client's user-level skills directory; the skill is auto-discovered on the next session.

## 🚀 Usage / 使用

```text
我们要支持手机、平板、桌面三端，帮我定一套响应式规范
```

输出响应式 CSS 框架 + 断点速查表。
Outputs responsive CSS framework plus a breakpoint cheat sheet.

## 🔑 Keywords / 关键词

`responsive design` · `breakpoints` · `css grid` · `mobile first` ·
`layout system` · `adaptive layout` · `frontend` · `响应式设计` · `栅格系统` · `多端适配`

## ⚙️ Prerequisites / 前置条件

无框架依赖，原生 CSS 直接粘贴即用。Framework-free, copy-paste native CSS.

## 🔒 Security / 安全说明

纯提示词型 skill，不含可执行脚本，无网络请求。Prompt-only skill: no scripts, no network calls.

## 📄 License

[MIT](./LICENSE) © 2026 JIANGEPLUS

## 🏷️ Topics

`responsive-design` `breakpoints` `css-grid` `mobile-first` `layout` `frontend` `ui-design` `design-system` `workbuddy` `skill`
