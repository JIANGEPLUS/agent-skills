# wcag-accessibility-checker

> Audit interfaces against WCAG AA — contrast ratios, keyboard navigation, ARIA, touch targets, motion preferences; output a prioritized remediation checklist. 无障碍合规检查：WCAG AA 六维度审计，输出可执行的分级整改清单。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Platform](https://img.shields.io/badge/Agent%20Skills-compatible-blueviolet.svg)

## ✨ Features / 功能特性

- **Contrast verification** — WCAG relative-luminance math: 4.5:1 body, 3:1 large text/UI 对比度实算
- **Six audit dimensions** — contrast / keyboard / screen reader / touch targets / motion / zoom 六维度审计
- **Prioritized findings** — blocker → severe → minor 阻断/严重/一般分级
- **Actionable fixes** — replacement color pairs and code changes, never vague advice 具体修复建议
- **Honest scoping** — runtime-only items flagged for manual verification 明确标注需运行时验证项

## 📦 Installation / 安装

将本目录整体放入 `~/.qoder/skills/<name>/`（Qoder）、`~/.codex/skills/<name>/`（Codex）或 `~/.claude/skills/<name>/`，新会话自动发现。
Copy this folder into the client's user-level skills directory; the skill is auto-discovered on the next session.

## 🚀 Usage / 使用

```text
检查这套配色 #6b7280 文字放在 #f9fafb 背景上能不能过 AA
```

输出对比度计算结果、判定与可替换的达标色值对。
Outputs contrast math, verdict, and compliant replacement pairs.

## 🔑 Keywords / 关键词

`accessibility` · `a11y` · `wcag` · `wcag-aa` · `contrast ratio` ·
`aria` · `keyboard navigation` · `inclusive design` · `无障碍` · `可访问性` · `对比度`

## ⚙️ Prerequisites / 前置条件

无需依赖；提供颜色组合、组件描述或 HTML/CSS 片段即可。No dependencies; bring colors, component specs, or HTML/CSS snippets.

## 🔒 Security / 安全说明

纯提示词型 skill，不含可执行脚本，无网络请求。Prompt-only skill: no scripts, no network calls.

## 📄 License

[MIT](./LICENSE) © 2026 JIANGEPLUS

## 🏷️ Topics

`accessibility` `wcag` `wcag-aa` `a11y` `inclusive-design` `ui-design` `frontend` `audit` `workbuddy` `skill`
