# 首个实验：学习率怎样影响线性回归

日期：2026-11-10。示例由 AI 协助实现并在本地运行，供学习者复现、修改和解释。

## 要回答的问题

固定模型、数据、初始参数和迭代次数，只改变学习率，训练会发生什么变化？

## 模型和梯度

数据由 `y=3x+2+ε` 生成，其中 `x` 在 `[-2,2]` 均匀采样，噪声 `ε` 为均值 0、标准差 0.2 的高斯噪声。随机种子为 42，总计 160 个样本，打乱后取 120 个训练、40 个验证。

模型与损失是：

$$
\hat y_i=wx_i+b,\qquad L(w,b)=\frac1n\sum_i(\hat y_i-y_i)^2.
$$

令 `e_i=wx_i+b-y_i`。由链式法则：

$$
\frac{\partial L}{\partial w}=\frac2n\sum_i e_i x_i,\qquad
\frac{\partial L}{\partial b}=\frac2n\sum_i e_i.
$$

每次迭代使用同一组旧参数计算两个梯度，然后同时更新：

$$
w\leftarrow w-\eta\frac{\partial L}{\partial w},\qquad
b\leftarrow b-\eta\frac{\partial L}{\partial b}.
$$

验证集只计算误差，不参与梯度更新。初始 `w=b=0`。这是全批量梯度下降，每一步使用全部训练样本。

## 运行方法

在仓库根目录执行，Python 3 即可，无需安装额外依赖：

```bash
python3 learning/ai-foundations/experiments/linear_regression.py --lr 0.01 --output learning/ai-foundations/experiments/results/lr-0.01.json
python3 learning/ai-foundations/experiments/linear_regression.py --lr 0.1 --output learning/ai-foundations/experiments/results/lr-0.1.json
python3 learning/ai-foundations/experiments/linear_regression.py --lr 1.0 --output learning/ai-foundations/experiments/results/lr-1.json
```

默认运行 200 次参数更新。训练或验证误差超过 `1e12` 时提前停止，并在结果中保留停止原因。记录中的 step 0 是更新前状态，step 200 是第 200 次更新后的状态。

## 实际运行结果

运行环境：Python 3.13.6。初始训练 MSE 为 `17.399733`，初始验证 MSE 为 `15.953693`。

| 学习率 | 最后一步 | 训练 MSE | 验证 MSE | w | b | 观察 |
|---|---:|---:|---:|---:|---:|---|
| 0.01 | 200 | 0.050348 | 0.040621 | 3.012372 | 1.948285 | 在 200 步时已接近生成参数 |
| 0.1 | 200 | 0.049056 | 0.036310 | 3.020023 | 1.982991 | 在本次数据上较快稳定 |
| 1.0 | 19 | 1.114764×10¹² | 9.876528×10¹¹ | 871146.882681 | 3287.516951 | 误差增大，触发提前停止 |

完整逐步记录：[0.01](../experiments/results/lr-0.01.json) · [0.1](../experiments/results/lr-0.1.json) · [1.0](../experiments/results/lr-1.json)。

## 怎样理解结果

1. 合适的学习率让参数逐步靠近较小损失的位置。这里 0.1 得到了接近数据生成值 `w=3,b=2` 的参数。
2. 较小的学习率每一步移动得少。在固定 200 步预算下，0.01 的误差比 0.1 稍高，可以增加迭代次数观察其是否进一步降低。
3. 学习率 1.0 在这个数据尺度下太大，参数在更新中偏离低损失区域，误差不断放大。需要把“模型表达能力不够”和“优化过程不稳定”分开排查。
4. 数据含噪声，最佳拟合参数通常与生成参数略有差异，拟合后的 MSE 也会保留噪声贡献。

这里使用人工线性数据，目标是观察优化过程。后续泛化实验应加入更复杂的数据与模型，并保留最终测试集。

## 亲自补充的三个小任务

- [ ] 把 0.01 的步数改为 1000，记录最后参数和误差。
- [ ] 用一个样本手算一次 `dw,db`，检查更新方向。
- [ ] 不看代码，用自己的话解释为什么验证样本没有出现在梯度公式的求和里。

结果和解释填写在[今日记录](../daily/2026-11-10.md)。
