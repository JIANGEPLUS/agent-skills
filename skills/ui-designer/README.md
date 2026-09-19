# ui-designer

> UI 设计师（像素君）单入口技能 —— 一条流水线覆盖设计令牌、组件状态、响应式布局、WCAG AA 无障碍审计与开发交付文档。A single-entry UI designer skill: tokens → components → responsive layout → accessibility audit → developer handoff.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)
![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![Platform](https://img.shields.io/badge/Agent%20Skills-compatible-blueviolet.svg)

## ✨ Features / 功能特性

- **Design tokens** — 品牌色扩展 100–900 色阶、语义色、字体/间距/阴影/过渡阶梯、`[data-theme="dark"]` 覆盖 令牌体系
- **Component states** — 五类组件 × 变体/尺寸 × 完整状态矩阵，含 `:focus-visible` 与 loading/error/empty 三态 组件状态矩阵
- **Responsive blueprint** — mobile-first 五档断点、12 列栅格、容器宽度、组件跨端行为规格 响应式蓝图
- **WCAG AA audit** — 六维度检查，给出算过的对比度比值与可执行修复值，按阻断/严重/一般分级 无障碍审计
- **Handoff docs** — 带测量的规格卡、令牌对照表、使用边界、可勾选 QA 清单 开发交接文档
- **Single entry** — 可全跑五阶段，也可只点其中一个阶段；不再需要记五个名字 单入口

## 📦 Installation / 安装

将本目录整体放入 `~/.qoder/skills/ui-designer/`（Qoder）、`~/.codex/skills/ui-designer/`（Codex）或 `~/.claude/skills/ui-designer/`，新会话自动发现。
Copy this folder into the client's user-level skills directory; the skill is auto-discovered on the next session.

## 🚀 Usage / 使用

**跑完整流水线：**

```text
从品牌色 #0ea5e9 开始，把设计系统整套做出来并交给前端
```

**只跑某一阶段：**

```text
品牌主色 #7c3aed，生成一套设计令牌，要支持暗色模式      → 阶段 1
补一个完整的按钮组件，各种状态都要有                    → 阶段 2
定一套手机/平板/桌面三端响应式规范                      → 阶段 3
检查 #6b7280 放在 #f9fafb 上能不能过 WCAG AA            → 阶段 4
登录页定稿了，写一份给前端的交接文档                    → 阶段 5
```

## 🧬 五个阶段

| # | 阶段 | 产出 |
|---|---|---|
| 1 | 设计令牌 | `:root` + `[data-theme="dark"]` CSS |
| 2 | 组件与状态 | BEM 组件 CSS + 状态矩阵表 |
| 3 | 响应式布局 | 栅格 CSS + 断点速查表 |
| 4 | 无障碍审计 | 分级整改清单（阻断→严重→一般） |
| 5 | 开发交付 | 规格卡 + 令牌对照 + QA 清单 |

阶段 4 是横切的，任一阶段后都可插入；审计发现的问题回灌到 1–3 修正后才进入阶段 5。

## 📝 版本说明

`2.0.0` 是本技能由 5 个独立子技能（`design-token-crafter`、`component-state-designer`、`responsive-layout-blueprint`、`wcag-accessibility-checker`、`design-handoff-writer`）合并为单入口的版本。五个子技能的全部约束逐条保留，未新增能力。

## 📄 License

MIT © [JIANGEPLUS](https://github.com/JIANGEPLUS)
