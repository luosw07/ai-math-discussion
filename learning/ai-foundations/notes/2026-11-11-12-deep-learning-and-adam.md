# Note 1: Deep Learning and Adam

**Study dates:** November 11–12, 2026  
**Reading:** *LeeDL Tutorial*, Chapters 1–3  
**Focus:** Understanding deep learning as function learning, diagnosing training problems, and understanding how Adam improves parameter updates.

## 1. The main picture I took away

After reading these chapters, I have a clearer picture of how a deep learning model learns. We choose a family of functions, define a loss that measures prediction errors, and use an optimization algorithm to find useful parameters. The network architecture determines which functions we can represent; training determines which member of that family we actually obtain.

The three chapters build this picture from different angles:

| Chapter | Main topic | My takeaway |
|---|---|---|
| 1: Machine Learning Basics | Models, losses, neural networks, and the learning framework | A neural network is a parameterized function built by composing layers. |
| 2: Practical Methodology | Model bias, optimization, overfitting, validation, and distribution mismatch | Poor performance needs a diagnosis before choosing a remedy. |
| 3: Deep Learning Basics | Critical points, batches, momentum, adaptive learning rates, classification, and normalization | The way parameters are updated has a major effect on whether training makes progress. |

The chapter names and section references here follow the tutorial's [v1.2.4 PDF](https://github.com/datawhalechina/leedl-tutorial/releases/tag/v1.2.4).

## 2. What makes a model a deep neural network?

A linear model has the form

$$
f_{w,b}(x)=w^\top x+b.
$$

A neural network repeatedly combines affine transformations with nonlinear activation functions:

$$
h^{(0)}=x,\qquad
h^{(\ell)}=\sigma\!\left(W^{(\ell)}h^{(\ell-1)}+b^{(\ell)}\right).
$$

Each layer transforms the representation produced by the previous layer. For example, ReLU, $\sigma(z)=\max(0,z)$, lets a network construct piecewise-linear functions. Composing these transformations gives the model flexibility to represent more complicated relationships. Multiple affine layers without nonlinear activations would still reduce to one affine transformation.

For a training set with $N$ examples, the objective can be written as

$$
L(\theta)=\frac{1}{N}\sum_{i=1}^{N}\ell\!\left(f_\theta(x_i),y_i\right),
$$

where $\theta$ collects the network's weights and biases. Backpropagation applies the chain rule efficiently to compute gradients. The optimizer then uses those gradients to update $\theta$.

This connects the network diagram to an actual learning procedure: **forward computation, loss evaluation, gradient computation, and parameter update**. Depth gives the model more ways to build representations, while the loss and optimization procedure guide what it learns. [Tutorial, §1.2]

## 3. Diagnosing poor performance

Chapter 2 helped me separate several problems that can look similar if I only look at one final score.

| Observation | Possible problem | A useful next check |
|---|---|---|
| Training loss stays high | The model may be too restrictive, or optimization may be ineffective | Compare model capacity and inspect training behavior. |
| Training loss is low but validation loss is high | Overfitting | Try regularization, more appropriate data, or early stopping. |
| Validation performance is good but deployment performance is poor | Distribution mismatch | Compare how the validation and deployment data were collected. |

The distinction between **model bias** and **optimization difficulty** is especially useful. A model may lack a suitable function, or it may contain a suitable function that the training procedure has not found. Changing the optimizer addresses the second issue. Choosing hyperparameters using a validation set, and reserving a test set for final evaluation, helps assess whether the resulting model generalizes. [Tutorial, §§2.1–2.5]

## 4. Why ordinary gradient descent can struggle

With a mini-batch $B_t$, a basic update is

$$
g_t=\nabla_\theta L_{B_t}(\theta_{t-1}),\qquad
\theta_t=\theta_{t-1}-\eta g_t.
$$

The learning rate $\eta$ controls the scale of the update. A large value can produce oscillation or divergence; a small value can make progress slow.

One example that makes the geometry concrete is

$$
L(a,b)=\frac12(100a^2+b^2),\qquad
\nabla L=(100a,b).
$$

Here, ordinary gradient descent gives

$$
a_t=(1-100\eta)a_{t-1},\qquad
b_t=(1-\eta)b_{t-1}.
$$

Convergence in both coordinates requires $0<\eta<0.02$. At $\eta=0.01$, the first coordinate reaches zero in one step, but the second shrinks by only a factor of $0.99$ per step. One shared learning rate has to accommodate two very different curvatures. This is a simple illustration of the narrow-valley problem discussed in §3.3.

Chapter 3 also discusses local minima and saddle points. A small gradient can occur at either; a loss plateau can also arise while gradients remain large and updates oscillate. Looking at the gradient and the update behavior gives more information than the loss curve alone. [Tutorial, §§3.1–3.3]

## 5. From momentum to Adam

I find it helpful to separate two questions: **which direction should the update follow, and how should each coordinate be scaled?**

- **Momentum** accumulates a weighted history of gradients. Persistent directions reinforce one another, while alternating directions can partially cancel.
- **AdaGrad** uses accumulated squared gradients to scale coordinate-wise updates. In its standard formulation, the cumulative denominator grows over time.
- **RMSProp** uses an exponential moving average of squared gradients, giving more weight to recent behavior.
- **Adam** combines a moving average of gradients with a moving average of squared gradients, and applies bias correction.

The tutorial introduces Adam as combining momentum with RMSProp-style scaling. I used Algorithm 1 of the [original Adam paper](https://arxiv.org/abs/1412.6980) to expand that idea into the equations below. [Tutorial, §§3.2–3.3]

### The update rule

Starting from $m_0=v_0=0$, for $t\geq1$:

$$
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t,
$$

$$
v_t=\beta_2v_{t-1}+(1-\beta_2)(g_t\odot g_t),
$$

$$
\widehat m_t=\frac{m_t}{1-\beta_1^t},\qquad
\widehat v_t=\frac{v_t}{1-\beta_2^t},
$$

$$
\theta_t=\theta_{t-1}
-\eta_t\frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}.
$$

Squares, square roots, and division are element-wise. The first moment tracks gradient direction; the second **raw** moment tracks squared-gradient scale. Starting both estimates at zero motivates the bias-correction factors. The small constant $\epsilon$ stabilizes division. Common settings from the original paper are $\beta_1=0.9$, $\beta_2=0.999$, and $\epsilon=10^{-8}$.

### A first-step calculation

Suppose one parameter has gradient $g_1=2$. With those decay rates,

$$
m_1=0.2,\qquad v_1=0.004.
$$

Bias correction gives

$$
\widehat m_1=2,\qquad \widehat v_1=4.
$$

With $\eta_1=0.001$, the update is approximately

$$
\Delta\theta=-0.001\frac{2}{\sqrt4+10^{-8}}
\approx-0.001.
$$

At the same numerical learning rate, ordinary gradient descent would update by $-0.002$. The calculation helps me see how Adam changes the relationship between raw gradient magnitude and step size. The meaningful comparison between optimizers should use learning rates suited to each method.

My interpretation is that Adam retains information about consistent directions while adapting the scale of individual parameter updates. Its $v_t$ estimates the second raw moment, $E[g^2]$; a variance estimate would additionally subtract the squared mean. Adam still has a base learning rate to choose, and its usefulness should be evaluated through both training behavior and validation performance.

## 6. Other training choices still matter

The optimizer works together with the rest of the training setup:

- **Batch size:** Mini-batches trade off computation, memory use, and gradient noise. Larger batches give more stable gradient estimates, while smaller batches introduce more variation into the updates. [Tutorial, §3.2]
- **Learning-rate scheduling:** Coordinate-wise adaptation can be combined with a time-dependent base learning rate $\eta_t$. Warmup gradually increases it at the beginning; decay reduces it later. [Tutorial, §§3.4–3.5]
- **Loss choice:** For classification, softmax converts logits into class probabilities. With a one-hot label, cross-entropy becomes $-\log p_\theta(y\mid x)$, connecting classification training to maximum likelihood. [Tutorial, §3.6]

This gives me a more precise meaning for “making optimization better”: choose updates that make useful progress on the training objective, and then check whether that progress improves performance on held-out data.

## 7. What I want to check next

- [ ] Implement the Adam update once to connect each equation to code.
- [ ] Compare SGD, momentum, and Adam on the same small task, tuning their learning rates separately.
- [ ] Record training and validation curves, batch size, initialization, and random seed.
- [ ] Revisit batch normalization in §3.7 and explain how training-time and evaluation-time behavior differ.

These are follow-up experiments. The numerical example above is a worked calculation.

## References

1. Qi Wang, Yiyuan Yang, and Ji Jiang. *LeeDL Tutorial*, v1.2.4. Chapters 1–3, especially §1.2, Chapter 2, and §§3.1–3.6. [Project](https://github.com/datawhalechina/leedl-tutorial) · [PDF release](https://github.com/datawhalechina/leedl-tutorial/releases/tag/v1.2.4).
2. Diederik P. Kingma and Jimmy Ba. *Adam: A Method for Stochastic Optimization*. ICLR 2015. Algorithm 1 and §§2–3. [Paper](https://arxiv.org/abs/1412.6980).

*Writing assistance: AI helped organize the reading notes, expand the equations, and check the worked calculation.*
