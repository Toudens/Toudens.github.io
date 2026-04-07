---
date: 2026-04-06
weight: "2"
type: docs
title: Ch-2 微分熵
---
### 1. 连续随机变量
#### 1.1 概率密度

* $p_{XY}(x,y)$ 是连续随机变量$XY$的联合概率密度函数
* $p_X(x)$ 是$X$的边际概率密度函数
* $p_Y(y)$ 是$Y$的边际概率密度函数
$$
\begin{align}
p_X(x) = \int_{-\infty}^{+\infty} p_{XY}(x,y) \mathrm{d}y\quad
p_Y(y) = \int_{-\infty}^{+\infty} p_{XY}(x,y) \mathrm{d}x\quad
p_{Y|X}(y|x) = \frac{p_{XY}(x,y)}{p_X(x)}
\end{align}
$$
#### 1.2 互信息

联合连续随机变量 $((X,Y),R^2,p_{XY}(x,y))$ 之间的 **互信息**：
$$
\begin{aligned}
I(X; Y) &= \sum_{i=-\infty}^{+\infty} \sum_{j=-\infty}^{+\infty} [p_{XY}(x_i, y_j) \Delta x_i \Delta y_j] \log \frac{[p_{XY}(x_i, y_j) \Delta x_i \Delta y_j]}{[p_X(x_i) \Delta x_i][p_Y(y_j) \Delta y_j]} \\
&= \sum_{i=-\infty}^{+\infty} \sum_{j=-\infty}^{+\infty} \left( p_{XY}(x_i, y_j) \log \frac{p_{XY}(x_i, y_j)}{p_X(x_i)p_Y(y_j)} \right) \Delta x_i \Delta y_j \\
&\xrightarrow{\Delta x_i \to 0,\ \Delta y_j \to 0} \iint p_{XY}(x, y) \log \frac{p_{XY}(x, y)}{p_X(x)p_Y(y)} \, \mathrm{d}x \, \mathrm{d}y
\end{aligned}
$$
$$
I(X;Y|Z) = \iiint p_{XYZ}(x,y,z) \log \frac{p_{XY|Z}(x,y|z)}{p_{X|Z}(x|z)p_{Y|Z}(y|z)} \mathrm{d}x \mathrm{d}y \mathrm{d}z
$$
$$
I(X;YZ) = \iiint p_{XYZ}(x,y,z) \log \frac{p_{XYZ}(x,y,z)}{p_X(x)p_{YZ}(yz)} \mathrm{d}x \mathrm{d}y \mathrm{d}z
$$
**性质 1** $I(X;Y) \geq 0$\
**性质 2** $I(X;Y) = I(Y;X),\quad I(X;Y|Z) = I(Y;X|Z)$\
**性质 3** $I(X;YZ) = I(X;Y) + I(X;Z|Y) = I(X;Z) + I(X;Y|Z)$\
**性质 4** 如果 $X \to Y \to Z$, 那么 $I(X;Y) \geq I(X;Z), I(X;Y) \geq I(X;Y|Z)$
#### 1.3 微分熵

连续随机变量 $(X,R,p_X(x))$ 的 **离散化熵值**：
$$
\begin{aligned} H_{\Delta}(X) &= -\sum_{i=-\infty}^{+\infty} p_X(x_i) \Delta x_i \log \left(p_X(x_i) \Delta x_i\right) \\ &= -\sum_{i=-\infty}^{+\infty} \left[p_X(x_i) \log p_X(x_i)\right] \Delta x_i - \sum_{i=-\infty}^{+\infty} p_X(x_i) \Delta x_i \log \Delta x_i \\ \xrightarrow{\Delta x_i\rightarrow 0} & -\int p_X(x) \log p_X(x) \, \mathrm{d}x + \infty \end{aligned}
$$
定义连续随机变量 $X$ 的 **微分熵**：
$$
H_C(X) = h(X) \triangleq -\int p_X(x) \log p_X(x) \, \mathrm{d}x
$$
>[!Note] **微分熵的本质和性质**
>1. 微分熵 $H_C(X)$ 不反映连续随机变量 $X$ 的不确定性。连续随机变量的不确定性一般都是无穷大。但微分熵的确在一定程度上反映了该连续随机变量的相对不确定性；
>2. $H_C(X)$ 可正，可负，可为 0。

#### 1.4 条件/联合微分熵
$$H_{C}(X, Y) = - \iint p_{XY}(x,y) \log p_{XY}(x,y) \mathrm{d}x \mathrm{d}y$$
$$H_{C}(X|Y) = - \iint p_{XY}(x,y) \log p_{X|Y}(x|y) \mathrm{d}x \mathrm{d}y$$
$$H_{C}(X,Y) = H_{C}(X) + H_{C}(Y|X) = H_{C}(Y) + H_{C}(X|Y)$$
$$\begin{align}H_{C}(U^{N}) &= H_{C}(U_1, U_2, \cdots U_N) = \sum_{n=1}^{N} H_{C}(U_n | U_1 U_2 \cdots U_{n-1})\\&= \sum_{n=1}^{N} H_{C}(U_n | U^{n-1})\end{align}$$
$$\begin{align}I(X,Y) &= H_{C}(X) - H_{C}(X|Y)\\&= H_{C}(Y) - H_{C}(Y|X)\\&= H_{C}(X) + H_{C}(Y) - H_{C}(X,Y)\end{align}$$
#### 1.5 线性不变性

对于离散随机变量 $X$，令 $Y = f(X)$ 是 $X \to Y$ 上的一对一函数，则 $H(X) = H(Y)$，但是对于连续随机变量，有：
$$
H_C(Y) = - \int p(y) \log p(y) \,\mathrm{d}y = - \int p(x) \log p(x) f'(x) \,\mathrm{d}x \neq H_C(X)
$$
即使对于线性变换，微分熵也不具有不变性。

### 平稳离散信源的熵

#### 平稳随机过程

对于任意的 $n$，任意的 $t_1, t_2, \cdots, t_n \in T$ 和 $h$，\
若 $(X(t_1), X(t_1), \cdots , X(t_n))$ 与 $(X(t_1 + h), X(t_2 + h), \cdots , X(t_n + h))$ 具有同样的分布，则称随机过程 ${X(t)}$ 是平稳随机过程。

**性质 1** $E(X(t_n)) = E(X(t_n + h)) = E(X(0)) = \text{Const.}$\
**性质 2** $X(t)$ 的均值和方差对于所有 $t$ 都一样。
#### 平稳随机过程
$$
\cdots X_{-1}, X_{0}, X_{1}, X_{2}, \cdots, X_{n}, \cdots
$$
平稳信源：任意长度片段的联合概率分布与时间起点无关
$$
Pr(X_1 X_2 \cdots X_L) = Pr(X_{1+n} X_{2+n} \cdots X_{L+n})
$$
简单无记忆信源：不同时间的随机变量不相关
$$
Pr(X_1 X_2 \cdots X_L) = \prod_{i=1}^L Pr(X_i)
$$
$m$ 阶马尔可夫信源：（$m=1$：马尔可夫信源）
$$
Pr(X_l \mid X_{l-1} X_{l-2} \cdots X_0) = Pr(X_l \mid X_{l-1} X_{l-2} \cdots X_{l-m})
$$
#### 平稳信源的熵

如果一个平稳信源发出长度为 $N$ 的序列 $X_1, X_2, \cdots, X_n$，令 $N$ 维随机矢量 $\mathbf{X} = (X_1, X_2, \cdots, X_n)$，则：
$$
H(\mathbf{X}) = H(X_1, X_2, \cdots, X_n) = - \sum p(x_1, x_2, \cdots, x_n) \log p(x_1, x_2, \cdots, x_n)
$$
$H(\mathbf{X})$ 随 $N$ 增长而增长，趋向无穷大。

**平均每符号熵**：$H_N(\mathbf{X}) \triangleq \frac{1}{N} H(\mathbf{X}) = \frac{1}{N} (X_1 X_2 \cdots X_N)$

**熵速率**：$\begin{align}H_\infty(\mathbf{X}) = \lim_{N \to \infty} H_N(\mathbf{X})\end{align}$

**平均条件熵**： $H(X_N \mid X_{N-1} X_{N-2} \cdots X_1)$
#### 平稳信源熵的性质

**性质 1** $H(X_N \mid X_{N-1} X_{N-2} \cdots X_1)$ 随$N$增大而单调不增

**性质 2** $H_N(X)$ 随$N$增大也单调不增

**性质 3** $H_N(X) \geq H(X_N \mid X_{N-1} X_{N-2} \cdots X_1)$

**性质 4** $\begin{align}H_\infty(X) = \lim_{N \to \infty} H_N(X) = \lim_{N \to \infty} H(X_N \mid X_{N-1} X_{N-2} \cdots X_1)\end{align}$

