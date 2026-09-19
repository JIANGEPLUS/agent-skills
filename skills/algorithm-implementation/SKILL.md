---
name: algorithm-implementation
description: 算法实现、分层测试与性能记录：代码契约、边界与对拍、性质测试、压力测试、profiler 优化与可复现跑分。TRIGGER —— 写算法代码、单元测试与随机对拍、暴力基线验证、浮点容差、profiler 找热点、性能回归、benchmark 记录、跑通示范脚本。DO NOT TRIGGER —— 算法选型（→ algorithm-modeling）、正确性证明（→ algorithm-proof）、模型训练与调参（→ algorithm-applied）。
license: MIT
metadata:
  version: 1.0.0
  category: algorithm-engineering
  origin: workbuddy-expert/senior-algorithm-expert
  language: zh-CN
---

# 实现、测试与性能

## 功能定位

把已定方案落地为可运行、可复现、可度量的实现：明确代码契约 → 分层验证 → 用测量而非大 O 下性能结论。可独立调用，也可由 `algorithm-engineer` 总纲路由而来。

## 触发条件

**TRIGGER**：写算法实现 / 单元测试 / 随机对拍 / 暴力基线 oracle / 边界用例 / 浮点容差 / profiler 热点 / 性能回归 / benchmark 记录 / 运行示范脚本。

**DO NOT TRIGGER**：
- 还没定算法方向 → `algorithm-modeling`
- 要正确性证明或复杂度推导 → `algorithm-proof`
- 训练模型与调参 → `algorithm-applied`

## 代码契约

- 遵从仓库与语言版本；明确返回值、异常与非法输入策略、是否修改输入、确定性与多解选择。
- 不同时给出互相不一致的伪代码与实现。
- 注意 C++ 溢出/迭代器、Java 数值与比较器、Python 递归深度/切片复制/大整数等实际语义；不能把各语言运算都当常数成本。

## 分层验证

1. **样例与手工可算案例**：核对输出定义。
2. **边界**：空/单元素、重复、全相等、极值、无解、多解、不可达、零/负值、退化结构。
3. **小规模独立基线对拍**：生成有界输入、固定种子、保留完整失败输入；不要复制候选的关键逻辑当 oracle。
4. **性质/变形测试**：只用已证明适用的性质（如排序后有序且多重集不变）；多解检查合法性与目标值，不强制相同排列。
5. **压力测试**：隔离于生产，限制输入、时间与内存；避免指数基线跑大输入。

测试不能证明全输入正确；浮点对拍须有有根据的容差与误差尺度。发现失败先缩小反例，再判断是契约、证明还是实现层出错。

## 性能记录

- 同版本、同输入、同计时口径；计入/排除初始化、I/O、数据生成须注明。
- 适当预热与重复，记录分布而非只报最好一次；内存与尾延迟按需求测。
- 复杂度只是预算，不能虚构跑分；用 profiler 找热点后优化，并复查回归。
- 不为微小速度牺牲清晰性或正确性。

## 交付清单

实际代码、必要运行命令、依赖、测试输入与结果、复杂度、未验证项；并说明这是单元测试、随机对拍、实测性能还是仅静态推导——不得统称"所有测试通过"。

## 约束与注意事项

- 环境缺失无法运行时标注"未运行"并给出验证方法，不伪称 AC 或跑分通过。
- 不自动运行全量压测或生产变更。
- 示范脚本只覆盖其自身契约，迁移到其他算法必须重新设计契约、独立 oracle 与边界，不能只替换函数名。

## 输出格式

- 代码与运行方式（命令、依赖、版本）
- 验证层级与结果（样例 / 边界 / 对拍 / 性质 / 压力）
- 性能记录（口径、分布、内存、结论适用范围）
- 残留风险与未验证项

## 参考文档

| 文档 | 用途 |
|------|------|
| [references/implementation-and-testing.md](references/implementation-and-testing.md) | 代码契约、分层验证、性能记录与交付细则 |
| [references/worked-example.md](references/worked-example.md) | 非负整数权最短路对拍示范说明 |
| [scripts/verify_shortest_paths.py](scripts/verify_shortest_paths.py) | 最短路对拍示范脚本（仅该契约，非通用证明器） |
| [templates/benchmark-record.md](templates/benchmark-record.md) | 性能记录模板 |
