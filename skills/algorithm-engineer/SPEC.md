# 完整说明（SPEC）

本文档定义「小算 · 高级算法工程师」技能包的文件结构、字段规范、模块职责边界与维护方式。

---

## 1. 来源与拆解逻辑

源专家：`senior-algorithm-engineer`（小算 · 高级算法工程师）

组成：1 个 agent 主文档 + 1 个内置 skill（`algorithm-engineering-playbook`，含 7 篇 references + 3 份 templates + 1 个 scripts）

拆解原则：**按"一次调用要交付什么"划分职责边界**，而非按源 skill 数量一比一照搬。源 playbook 的 7 篇 references 按主题拆为 5 个专业模块，agent 主文档收敛为总纲。

| 模块 | 来源内容 | 保留的参考/模板 |
|------|---------|----------------|
| `algorithm-engineer` | agent 主文档（能力范围、接单与授权、解决问题主线、判断边界、输出方式） | `acceptance-cases.md`、`templates/solution-review.md` |
| `algorithm-modeling` | `references/model-and-selection.md` | `templates/problem-contract.md` |
| `algorithm-proof` | `references/proof-and-complexity.md` | — |
| `algorithm-domain-checks` | `references/domain-checks.md` | — |
| `algorithm-applied` | `references/applied-algorithms.md` | — |
| `algorithm-implementation` | `references/implementation-and-testing.md`、`references/worked-example.md` | `scripts/verify_shortest_paths.py`、`templates/benchmark-record.md` |

---

## 2. 目录结构

本包遵循 `agent-skills` 仓库的扁平约定，每个模块是一个独立目录（`skills/<name>/SKILL.md`）。

```text
skills/
├── algorithm-engineer/            # 总纲 / 路由 + 包级文档
│   ├── SKILL.md
│   ├── README.md                  # 包总览：核心职责、能力栈、模块路由
│   ├── SPEC.md                    # 本文件（完整说明）
│   ├── agents/openai.yaml
│   ├── references/acceptance-cases.md
│   └── templates/solution-review.md
├── algorithm-modeling/
│   ├── SKILL.md
│   ├── README.md
│   ├── agents/openai.yaml
│   ├── references/model-and-selection.md
│   └── templates/problem-contract.md
├── algorithm-proof/
│   ├── SKILL.md
│   ├── README.md
│   ├── agents/openai.yaml
│   └── references/proof-and-complexity.md
├── algorithm-domain-checks/
│   ├── SKILL.md
│   ├── README.md
│   ├── agents/openai.yaml
│   └── references/domain-checks.md
├── algorithm-applied/
│   ├── SKILL.md
│   ├── README.md
│   ├── agents/openai.yaml
│   └── references/applied-algorithms.md
└── algorithm-implementation/
    ├── SKILL.md
    ├── README.md
    ├── agents/openai.yaml
    ├── references/
    │   ├── implementation-and-testing.md
    │   └── worked-example.md
    ├── scripts/verify_shortest_paths.py
    └── templates/benchmark-record.md
```

模块总数：6 个 `SKILL.md` + 6 个 `README.md` + 6 个 `openai.yaml` + 1 个 `SPEC.md` + 7 篇 references + 3 份 templates + 1 个 script。

---

## 3. SKILL.md 字段定义

`SKILL.md` 顶部为 YAML frontmatter，Codex 仅强制要求 `name` 与 `description`，其余为标准可选字段。

| 字段 | 必需 | 说明 | 约束 |
|------|------|------|------|
| `name` | ✅ | 技能唯一标识，同时决定目录名与显式调用名（`$name`） | 小写字母 + 连字符，≤64 字符，与目录名一致 |
| `description` | ✅ | 触发判断依据：能力 + TRIGGER / DO NOT TRIGGER + 触发词 | 触发词前置；写清适用与不适用边界；会被截断时仍能命中 |
| `license` | 可选 | 分发许可 | 本项目统一 `MIT` |
| `metadata.version` | 可选 | 模块版本 | 语义化版本 |
| `metadata.category` | 可选 | 分类 | `algorithm-engineering` |
| `metadata.origin` | 可选 | 来源标识 | `workbuddy-expert/senior-algorithm-expert` |
| `metadata.language` | 可选 | 主语言 | `zh-CN` |
| `metadata.modules` | 可选 | 关联模块（仅总纲使用） | 模块名数组 |

### 3.1 agents/openai.yaml

Codex CLI 专有，其他 Agent 忽略：

```yaml
display_name: "Algorithm Engineer"   # 选择器中的显示名
icon: "cpu"                            # 图标标识
```

### 3.2 正文结构约定

功能定位 → 触发条件（TRIGGER / DO NOT TRIGGER）→ 工作流程 → 决策准则或核查清单 → 输出格式 → 约束与注意事项 → 参考文档索引。

---

## 4. 模块职责边界

| 场景 | 使用模块 |
|------|---------|
| 不知道该用什么能力 / 需要总控流程 | `algorithm-engineer`（路由） |
| 厘清目标与约束、选算法方向 | `algorithm-modeling` |
| 写正确性证明、算复杂度账本 | `algorithm-proof` |
| 核查图/字符串/数论/几何的隐含前提 | `algorithm-domain-checks` |
| 数值优化、机器学习、调度与分布式 | `algorithm-applied` |
| 写代码、做对拍、记性能 | `algorithm-implementation` |

**避免越界**：`algorithm-modeling` 不写证明；`algorithm-proof` 不做实测跑分；`algorithm-implementation` 不重新选型；`algorithm-applied` 不处理经典算法题的领域前提。

---

## 5. 扩展方式

### 5.1 新增模块

1. 在 `skills/` 下新建目录，目录名 = `name`（小写连字符）
2. 编写 `SKILL.md`：`description` 中前置触发词、写清 TRIGGER / DO NOT TRIGGER 边界
3. 如需 Codex 显示名，加 `agents/openai.yaml`
4. 深度内容（>200 行）拆到 `references/`，在正文中用相对路径索引
5. 编写模块 `README.md`（职责边界、触发条件、输入输出、工作流、使用要点）
6. 更新 `skills/algorithm-engineer/SKILL.md` 的路由表与 `README.md` 模块表

### 5.2 新增参考文档

放入模块 `references/` 目录，并在 `SKILL.md` 末尾建立索引表（文档 → 用途）。保持 SKILL.md 精简，让 Agent 按需加载 references。

### 5.3 新增模板与脚本

- 交付类模板放 `templates/`，在 `SKILL.md` 的「输出格式」中给出相对路径
- 可执行脚本放 `scripts/`，必须在文档中标明适用范围与限制（如"仅该契约，非通用证明器"）

---

## 6. 维护规范

- **版本**：模块内容实质变更时递增 `metadata.version`；结构调整同步更新本文件目录树
- **内容校验**：每次改动后确认 YAML frontmatter 可被解析、`name` 与目录名一致、相对链接有效
- **算法工程底线**（改动时不得删除）：
  1. 结论先给前提，再给思路、证明、复杂度、代码、测试与局限
  2. 区分"推导成立 / 已执行测试 / 性能实测 / 尚未核实"，不用笼统"全部通过"
  3. 未证明不声称全局最优；测试通过不能替代证明
  4. 性能结论只支持被测配置与输入，须记录版本、硬件、分布、种子与计时口径
  5. 环境缺失时标注"未运行"，不伪造通过
  6. `acceptance-cases.md` 是待运行案例，不得当作已验证能力声明
- **上游同步**：源专家升级（新增 references 或改动规则）时，评估是否需要新增模块或更新 references；保持 `metadata.origin` 记录来源

---

## 7. 推送与同步

仓库：`JIANGEPLUS/agent-skills`（默认分支 `main`）。

提交粒度建议：一个逻辑变更一个 commit，message 采用 `type(scope): subject`（如 `feat(skills): add algorithm-proof module`）。
