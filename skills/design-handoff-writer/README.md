# design-handoff-writer

> Generate developer handoff documents — measured component specs, token references, usage guidelines, and design QA checklists. 设计交付文档：带测量的组件规格卡、令牌对照表、使用指南与设计 QA 验收清单。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Platform](https://img.shields.io/badge/Agent%20Skills-compatible-blueviolet.svg)

## ✨ Features / 功能特性

- **Spec cards** — per-component measurements (px + token name), type hierarchy, color refs 规格卡与测量标注
- **Token mapping table** — design values ↔ CSS/platform variable names 令牌对照表
- **Usage guidelines** — when to use/avoid, content boundaries, a11y requirements 使用指南
- **QA checklists** — checkbox lists grouped by page/component, all states covered 可勾选 QA 清单
- **Platform notes** — iOS safe area, web scrollbar quirks kept separate 平台差异独立列出

## 📦 Installation / 安装

将本目录整体放入 `~/.qoder/skills/<name>/`（Qoder）、`~/.codex/skills/<name>/`（Codex）或 `~/.claude/skills/<name>/`，新会话自动发现。
Copy this folder into the client's user-level skills directory; the skill is auto-discovered on the next session.

## 🚀 Usage / 使用

```text
登录页设计定稿了，帮我写一份给前端的交接文档
```

输出 Markdown 交接文档：规格卡 → 令牌对照 → 使用指南 → QA 清单。
Outputs a handoff document: spec cards → token mapping → usage → QA checklist.

## 🔑 Keywords / 关键词

`design handoff` · `design spec` · `developer handoff` · `design qa` ·
`component documentation` · `design system` · `design to code` · `设计交付` · `开发交接` · `还原度`

## ⚙️ Prerequisites / 前置条件

输入设计稿描述/截图/令牌表即可；目标平台可指定 Web/iOS/Android。Bring design specs or screenshots; Web/iOS/Android supported.

## 🔒 Security / 安全说明

纯提示词型 skill，不含可执行脚本，无网络请求。Prompt-only skill: no scripts, no network calls.

## 📄 License

[MIT](./LICENSE) © 2026 JIANGEPLUS

## 🏷️ Topics

`design-handoff` `design-spec` `design-qa` `component-documentation` `design-system` `design-to-code` `ui-design` `workbuddy` `skill` `developer-experience`
