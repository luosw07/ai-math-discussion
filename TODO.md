# TODO：AI Foundations 两周学习与每日上传

状态：**进行中｜LeeDL 第 1—3 章已阅读，第一篇学习笔记已完成**  
建立日期：2026-11-10  
建议周期：2026-11-10—2026-11-23。日期是个人排期，课程未公布精确截止日。

课程要求：[课程 README](https://github.com/powergiant/ai-math-discussion#current-task-ai-foundations-two-weeks)。

## 现在先做

- [x] 阅读课程要求，明确 ML/DL、LLM、RL 三块重点。
- [x] 将课程仓库下载到本地。
- [x] 整理参考资料、学习顺序、每日记录模板和自测题。
- [x] 准备首日概念导读与可运行的梯度下降实验。
- [x] [Fork 课程仓库](https://github.com/luosw07/ai-math-discussion) 到 `luosw07`。
- [x] 把本次准备的 `learning/`、`TODO.md` 和 `.gitignore` 上传到个人 Fork。
- [ ] 阅读首日导读，亲自运行实验，填写今天的个人理解与疑问。

入口：[学习主页](learning/ai-foundations/README.md) · [资料导航](learning/ai-foundations/resources.md) · [自测清单](learning/ai-foundations/self-check.md) · [今日记录](learning/ai-foundations/daily/2026-11-10.md)

## 已记录的学习进展

- [x] 2026-11-11—11-12：阅读 LeeDL 第 1—3 章，理解深度学习训练流程与 Adam 的基本思想。
- [x] 完成英文笔记 [Note 1: Deep Learning and Adam](learning/ai-foundations/notes/2026-11-11-12-deep-learning-and-adam.md)。
- [ ] 在同一个小任务上比较 SGD、Momentum 与 Adam，分别调整学习率并记录训练和验证结果。

## 两周计划

先按每天约 90 分钟安排：阅读 40 分钟、推导或实验 30 分钟、记录与上传 20 分钟。每完成一行再勾选；进度变化时保留实际日期。

| 完成 | 日期 | 重点与阅读入口 | 当天最小产出 |
|---|---|---|---|
| [ ] | 11-10 | ML/DL：LeeDL 引言；本仓库首日导读 | 解释模型、损失、优化；运行线性回归；上传第一条记录 |
| [ ] | 11-11 | LeeDL 深度学习：训练技巧、学习率 | 推导 MSE 梯度；比较 3 个学习率；记录数值结果 |
| [ ] | 11-12 | 神经网络、链式法则、分类损失 | 手算一个小网络的梯度；解释 softmax 与交叉熵 |
| [ ] | 11-13 | 泛化、验证集、过拟合、正则化 | 做一个训练集/验证集对比实验；总结错误来源 |
| [ ] | 11-14 | Happy-LLM 第 1 章；CS336 HW1 分词部分 | 说明 token 与 embedding；写分词示例及测试 |
| [ ] | 11-15 | Happy-LLM 第 2 章：注意力、Transformer | 手算一次 attention；标注 Q/K/V 的形状和 mask |
| [ ] | 11-16 | Happy-LLM 第 3—4 章；第一周复盘 | 画出 decoder-only 数据流；回答前 20 道自测中的已学部分 |
| [ ] | 11-17 | Happy-LLM 第 5 章；CS336 HW1 模型部分 | 实现一个最小模块并验证输入输出；记录 HW1 实际进度 |
| [ ] | 11-18 | Happy-LLM 第 6 章；交大“微调与部署” | 解释预训练、SFT、LoRA；记录环境需求与可运行步骤 |
| [ ] | 11-19 | Easy RL 第 1—2 章 | 用一个例子写清 MDP 五元组，手算折扣回报 |
| [ ] | 11-20 | Easy RL 第 2—3 章 | 推导 Bellman 关系；在小型环境实现 Q-learning |
| [ ] | 11-21 | Easy RL 第 6 章；回看第 3 章 | 说明 DQN 的回放与目标网络；比较 SARSA/Q-learning |
| [ ] | 11-22 | Easy RL 第 4—5 章；CS336 HW5 概览 | 解释策略梯度、PPO；梳理 RL 与语言模型后训练的联系 |
| [ ] | 11-23 | 三块基础复盘；CS336 HW2—4 范围梳理 | 整理三份主题总结、实验记录、未解决问题及后续 HW 计划 |

## CS336 HW1—5：完整作业进度单独跟踪

保留五份作业的完整学习目标。上面的两周安排先推进三块基础和 HW1 的入门部分；完整作业继续逐项完成，具体耗时按先修基础和算力调整。

| 作业 | 内容 | 阅读题面 | 实现与实验 | 整理结果 |
|---|---|---|---|---|
| [HW1 Basics](https://github.com/stanford-cs336/assignment1-basics) | 分词器、Transformer、优化器、训练 | [ ] | [ ] | [ ] |
| [HW2 Systems](https://github.com/stanford-cs336/assignment2-systems) | 性能分析、attention 优化、分布式训练 | [ ] | [ ] | [ ] |
| [HW3 Scaling](https://github.com/stanford-cs336/assignment3-scaling) | 缩放规律与拟合 | [ ] | [ ] | [ ] |
| [HW4 Data](https://github.com/stanford-cs336/assignment4-data) | 数据清洗、过滤、去重 | [ ] | [ ] | [ ] |
| [HW5 Alignment](https://github.com/stanford-cs336/assignment5-alignment) | SFT、推理强化学习；可选安全对齐 | [ ] | [ ] | [ ] |

## 每天上传的最低标准

- 写出今天阅读的章节/链接。
- 用自己的话解释至少一个概念，并给出一个例子、推导或实验结果。
- 留下至少一个疑问和下一步动作。
- 更新本清单，上传已有进展。没有读懂的地方直接写成问题。

## 两周复盘时检查

- [ ] ML/DL：能解释训练流程、反向传播、损失与泛化；有一个可复现实验。
- [ ] LLM：能解释分词、attention、Transformer、自回归训练与微调；有一个手算或代码验证。
- [ ] RL：能解释 MDP、回报、价值函数、Bellman 关系、Q-learning 与策略梯度；有一个小环境实验。
- [ ] 三块主题都有自己的文字、例子或推导；自测中不会的题都有标记。
- [ ] 日常记录已上传到个人 Fork，CS336 HW1—5 保留真实进度。
