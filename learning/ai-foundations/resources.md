# 资料导航

整理日期：2026-11-10。资料来自[课程指定列表](https://github.com/powergiant/ai-math-discussion#current-task-ai-foundations-two-weeks)；以下顺序是本次个人学习安排。

## 1. 机器学习与深度学习

**主线：[LeeDL Tutorial](https://github.com/datawhalechina/leedl-tutorial)**。

- [内容介绍](https://github.com/datawhalechina/leedl-tutorial/blob/master/docs/README.md)：用于按主题定位。
- [PDF 下载](https://github.com/datawhalechina/leedl-tutorial/releases)：按当前版本目录查找章节，记录实际页码。
- [配套练习](https://github.com/datawhalechina/leedl-tutorial/tree/master/Homework)。

阅读重点：引言 → 深度学习中的训练技巧、自适应学习率、分类损失、归一化 → 自注意力与 Transformer。同步补充线性回归、链式法则、训练/验证/测试集与过拟合的理解。

产出：MSE 梯度推导、一个训练实验、训练失败或泛化不佳的原因分析。

## 2. 大语言模型

**主线：[Happy-LLM](https://github.com/datawhalechina/happy-llm)**，从第 1—4 章建立概念，第 5—6 章进入实现。

| 阅读 | 重点 |
|---|---|
| 第 1 章 NLP 基础概念 | 文本表示与语言建模 |
| 第 2 章 Transformer 架构 | attention、位置、mask、模块连接 |
| 第 3 章 预训练语言模型 | encoder-only、encoder-decoder、decoder-only |
| 第 4 章 大语言模型 | 训练策略与整体流程 |
| 第 5 章 动手搭建大模型 | 分词器、模型实现、预训练 |
| 第 6 章 大模型训练实践 | 预训练、SFT、LoRA/QLoRA |

运行章节代码前阅读[学习与环境准备](https://github.com/datawhalechina/happy-llm/blob/main/docs/学习与环境准备.md)，按章节建环境。第一天的小实验只需要 Python 标准库。

**工程实践：[上海交大《动手学大模型》](https://github.com/Lordog/dive-into-llms)**。

- 优先阅读[微调与部署](https://github.com/Lordog/dive-into-llms/blob/main/documents/chapter1/README.md)，梳理输入数据、模型、训练参数与评估。
- 学完 RL 后再看[RLHF 安全对齐](https://github.com/Lordog/dive-into-llms/blob/main/documents/chapter11/README.md)，连接 PPO 与语言模型后训练。

**完整作业：[CS336 Spring 2025](https://cs336.stanford.edu/spring2025/)**。按课程仓库指定的 2025 版学习，HW1—5 的链接和状态在 [TODO](../../TODO.md)。主题依次为模型基础、系统、缩放、数据与对齐。先完成基础模块验证，再按作业要求安排训练或 GPU 实验。

产出：attention 手算、decoder 数据流、next-token 损失解释、一个模块的代码验证，以及各作业的实际进展。

## 3. 强化学习

**主线：[Easy RL](https://github.com/datawhalechina/easy-rl)**，按当前[目录](https://github.com/datawhalechina/easy-rl/blob/master/docs/_sidebar.md)选读。

1. [第 1 章](https://github.com/datawhalechina/easy-rl/blob/master/docs/chapter1/chapter1.md)：强化学习基础。
2. [第 2 章](https://github.com/datawhalechina/easy-rl/blob/master/docs/chapter2/chapter2.md)：MDP、回报、价值函数、策略与价值迭代。
3. [第 3 章](https://github.com/datawhalechina/easy-rl/blob/master/docs/chapter3/chapter3.md)：表格型方法；配合 Q-learning 小环境。
4. [第 6 章](https://github.com/datawhalechina/easy-rl/blob/master/docs/chapter6/chapter6.md)：DQN 基本概念。
5. [第 4 章](https://github.com/datawhalechina/easy-rl/blob/master/docs/chapter4/chapter4.md)与[第 5 章](https://github.com/datawhalechina/easy-rl/blob/master/docs/chapter5/chapter5.md)：策略梯度与 PPO。

产出：一个 MDP 例子、回报与 Bellman 关系手算、Q-learning 结果，以及策略方法和价值方法的比较。
