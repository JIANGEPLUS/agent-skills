# equity-research — 股票研究技能包总览

---

## 1. 简介

「严估深」（Equity Research Expert）股票研究专家能力拆解而成的 **Codex 标准技能包**。按职责边界拆为 6 个可独立调用的模块，遵循 OpenAI Codex / Agent Skills 开放规范（SKILL.md），可被 Codex CLI、Codex IDE 扩展、ChatGPT、Qoder、Claude Code 及任何兼容 Agent Skills 标准的 Agent 加载使用。

---

## 2. 模块一览

| Skill | 职责 | 说明 |
|-------|------|------|
| `equity-research` | 总纲 / 路由 | 任务识别与模块调度、PM 七问、数据与评级纪律、免责声明 |
| `fundamentals-analysis` | 基本面与盈利 | 公司速览卡、业绩前瞻（Preview）、业绩深度解读（Analysis）、模型与估计更新 |
| `valuation` | 估值测算 | 三表联动建模、WACC、DCF、可比估值、敏感性/情景、目标价推导 |
| `research-report` | 研报与推介 | 首次覆盖（5 任务流水线）、投资备忘录、多空推介、行业综述、晨会纪要 |
| `risk-monitoring` | 风险与跟踪 | 仓位与对冲、论点记分卡、催化剂日历、事件情景与敏感性分析 |
| `idea-screening` | 选股与创意 | 价值/成长/质量/做空/特殊情形筛选、主题价值链扫描、一页纸想法卡 |

完整结构、字段定义与扩展维护见 [SPEC.md](SPEC.md)。

---

## 3. 安装

```bash
# 方式一：仓库内使用（Agent 自动发现 skills/ 目录）
git clone https://github.com/JIANGEPLUS/agent-skills.git
cd agent-skills && codex

# 方式二：安装到用户级目录，全局生效
mkdir -p ~/.agents/skills
cp -r agent-skills/skills/* ~/.agents/skills/
```

安装后重启 Agent 生效（Codex 会自动检测技能变更；未出现时重启一次）。

---

## 4. 使用与调用示例

### 4.1 显式调用

推荐，行为最可控：

```text
$equity-research       帮我研究宁德时代，给出评级、目标价和关键催化
$fundamentals-analysis 做一份贵州茅台 2026Q2 业绩点评
$valuation            给比亚迪建 DCF 模型，做 WACC × 永续增速敏感性
$research-report      写一份立讯精密首次覆盖报告（Task 1）
$risk-monitoring      仓位该给多大？如何对冲？止损怎么设
$idea-screening       筛一批 AI 基建主题的中盘股
```

### 4.2 隐式调用

自然语言，Agent 按 description 自动匹配：

```text
这家公司最近财报超预期了吗       → fundamentals-analysis
按 DCF 和可比估值给个合理区间     → valuation
帮我写一份投委会用的投资备忘录   → research-report
我的多头逻辑还成立吗？何时止损   → risk-monitoring
有什么低估的成长股可以看        → idea-screening
```

### 4.3 组合工作流

`equity-research` 是总纲：复杂任务先做任务分解与路由，再按
`idea-screening → fundamentals-analysis → valuation → research-report → risk-monitoring`
串联执行，最后按 PM 七问收尾，输出评级、目标价、催化与风险。

### 4.4 验证

在 Codex CLI 运行 `/skills`，应看到 6 个模块；或直接询问 Agent："列出当前可用的 skills"。

---

## 5. 使用纪律

- 所有结论标注数据来源与截至日期；缺失标 `[MISSING]`，超 90 天标 `[STALE]`
- 评级须附目标价与时间维度；证据不足时标注"低信心"
- 每个论点必须有可证伪条件，多空双向呈现
- 输出末尾附："本报告仅供研究参考，不构成个人投资建议"

---

## 6. 来源与许可

源自 WorkBuddy「严估深 / EquityResearchExpert」专家插件（v2.1.0：1 个 agent + 16 个内置 skill + 3 份规则），按职责重构为 6 个模块。MIT 许可。
