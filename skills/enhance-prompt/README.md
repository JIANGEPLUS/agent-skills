# enhance-prompt

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Platform](https://img.shields.io/badge/Agent%20Skills-compatible-blueviolet.svg)

---

## 1. 简介

增强提示词（Prompt Enhancement）：把模糊、有歧义或缺要素的指令改写得更清晰、更具体、更可执行。

> Rewrite ambiguous instructions into clear, specific, actionable prompts.

---

## 2. 功能特性

- **Ambiguity removal** — resolves dangling references like "这个 / 那个" into explicit objects 消除歧义指代
- **Slot completion** — fills in goal, scope, constraints and expected output format 补全缺失要素
- **Correctness pass** — fixes factual slips, misused terms and internal contradictions 纠正事实与逻辑错误
- **Code-block safe** — fenced examples in the input are preserved verbatim, never rewritten 代码块原样保留
- **Assumption tagging** — anything inferred is marked inline as `（假设：…）` instead of being silently invented 假设显式标注
- **No execution** — outputs the improved prompt only; it never starts doing the task 只增强、不执行

---

## 3. 安装

将本目录整体放入 `~/.qoder/skills/enhance-prompt/`（Qoder）、`~/.codex/skills/enhance-prompt/`（Codex）或 `~/.claude/skills/enhance-prompt/`，新会话自动发现。

> Copy this folder into the client's user-level skills directory; the skill is auto-discovered on the next session.

---

## 4. 使用与示例

```text
/enhance-prompt 帮我做一个登录功能
```

输出：

```text
### 以下是原指令的增强版本，更加具体和清晰：
<enhanced-prompt>实现一个用户登录功能：包含邮箱+密码登录表单、前端输入校验、登录接口
调用与错误提示（密码错误/账号不存在），登录成功后跳转到首页。技术栈沿用当前项目现有
框架，UI 风格与现有页面保持一致。（假设：暂不需要第三方 OAuth 登录和记住我功能）</enhanced-prompt>
```

也可以在自然语言里触发：「帮我把这段需求描述改清楚，先不要执行」。

---

## 5. 注意事项

本仓库中负责"把活干完"的技能（`design-token-crafter`、`component-state-designer` 等）会执行任务；`enhance-prompt` 只负责在执行前把指令本身打磨清楚。两者互补，不要混用。

---

## 6. 许可

MIT © [JIANGEPLUS](https://github.com/JIANGEPLUS)
