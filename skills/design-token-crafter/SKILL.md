---
name: design-token-crafter
description: "设计令牌系统生成 Skill。根据品牌色与排版需求，生成完整的设计令牌（Design Tokens）CSS 变量体系：颜色梯度、字体族与字号阶梯、间距（4px 基准）、阴影、过渡时长，并附暗色主题令牌与基础组件样式。触发词：设计令牌、design tokens、生成token、颜色体系、CSS变量、暗色主题变量、design token system。适用场景：搭建设计系统基础、统一跨平台视觉一致性、初始化新项目样式基础。"
description_zh: "生成完整设计令牌系统：颜色/字体/间距/阴影/过渡 CSS 变量 + 暗色主题令牌"
description_en: "Generate complete design token systems: CSS variables for color, typography, spacing, shadows, transitions, plus dark theme tokens"
version: 1.0.0
display_name: "设计令牌生成器"
display_name_en: "design-token-crafter"
visibility: "public"
---

# 设计令牌生成器 Skill（design-token-crafter）

## 功能定位

将品牌输入转化为可落地的 Design Token CSS 变量体系，保证跨页面、跨平台的视觉一致性。只负责令牌系统本身，不负责具体页面布局。

## 触发条件

1. 用户要求生成设计令牌 / token 体系 / CSS 变量 / 颜色体系。
2. 新项目初始化样式基础，或需要统一明暗双主题变量。

## 工作流程

1. 收集输入：品牌主色（hex）、辅助色、中性色偏好、字体族；缺省时采用蓝色主色（#3b82f6）+ Inter/system-ui 兜底。
2. 按色阶规律（100→900）扩展主色与辅助色梯度，校验文本-背景对比度满足 WCAG AA（普通文本 4.5:1，大字 3:1）。
3. 生成语义色令牌：success / warning / error / info。
4. 以 4px 为基准生成间距阶梯（4/8/12/16/24/32/48/64px），字号阶梯 12→36px，阴影三级，过渡三档。
5. 生成 `[data-theme="dark"]` 暗色令牌覆盖，保持语义名不变、仅换值。
6. 附最小基础组件样式（.btn / .form-input / .card）演示令牌消费方式。

## 输出格式

单个 `:root { … }` + `[data-theme="dark"] { … }` CSS 代码块，分区注释（Color Tokens / Typography / Spacing / Shadow / Transition），紧随一段不超过 5 行的使用说明。

## 约束与注意事项

- 颜色一律 hex，间距/字号同时注释 px 换算；命名使用 `--color-*`、`--font-*`、`--space-*`、`--shadow-*`、`--transition-*` 前缀。
- 对比度不达标的组合必须调整后输出，不得带病交付。
- 不引入任何运行时依赖，输出纯 CSS。

## 使用示例

```text
用户：品牌主色是 #7c3aed，帮我生成一套设计令牌，要支持暗色模式
输出：:root 颜色梯度/语义色/字体/间距/阴影/过渡令牌 + [data-theme="dark"] 覆盖
     + .btn/.form-input/.card 示例样式 + 对比度校验说明
```
