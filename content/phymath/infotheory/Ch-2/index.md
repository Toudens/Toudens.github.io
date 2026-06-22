---
date: 2026-04-06
weight: "2"
type: docs
title: Lec-2 信息的度量 2
---
### 1. 连续变量的互信息
#### 1.1 概率密度函数

|          概率密度函数          | 意义                     | 计算公式                                                                                |
| :----------------------: | ---------------------- | ----------------------------------------------------------------------------------- |
|      $p_{XY}(x,y)$       | 连续随机变量 $XY$ 的联合概率密度函数  |                                                                                     |
|         $p_X(x)$         | $X$ 的边际概率密度函数          | $\begin{align}p_X(x) = \int_{-\infty}^{+\infty} p_{XY}(x,y) \mathrm{d}y\end{align}$ |
|         $p_Y(y)$         | $Y$ 的边际概率密度函数          | $\begin{align}p_Y(y) = \int_{-\infty}^{+\infty} p_{XY}(x,y) \mathrm{d}x\end{align}$ |
| $p_{Y\vert X}(y\vert x)$ | 已知 $X$ 取值时 $Y$ 的概率密度函数 | $\begin{align}p_{Y\vert X}(y\vert x) = \frac{p_{XY}(x,y)}{p_X(x)}\end{align}$       |

#### 1.2 互信息及其性质

联合连续随机变量 $((X,Y),R^2,p_{XY}(x,y))$ 之间的 **互信息**：
$$
\begin{aligned}
I(X; Y) &= \sum_{i=-\infty}^{+\infty} \sum_{j=-\infty}^{+\infty} [p_{XY}(x_i, y_j) \Delta x_i \Delta y_j] \log \frac{[p_{XY}(x_i, y_j) \Delta x_i \Delta y_j]}{[p_X(x_i) \Delta x_i][p_Y(y_j) \Delta y_j]} \\
&= \sum_{i=-\infty}^{+\infty} \sum_{j=-\infty}^{+\infty} \left( p_{XY}(x_i, y_j) \log \frac{p_{XY}(x_i, y_j)}{p_X(x_i)p_Y(y_j)} \right) \Delta x_i \Delta y_j \\
&\xrightarrow{\Delta x_i \to 0,\ \Delta y_j \to 0} \iint p_{XY}(x, y) \log \frac{p_{XY}(x, y)}{p_X(x)p_Y(y)} \, \mathrm{d}x \, \mathrm{d}y
\end{aligned}
$$
在已知连续随机变量 $Z$ 的条件下，联合连续随机变量 $X,Y$ 之间的互信息：
$$
\begin{align}
I(X;Y|Z) 
&= \iiint p_{XYZ}(x,y,z) \log \frac{p_{XY|Z}(x,y|z)}{p_{X|Z}(x|z)p_{Y|Z}(y|z)} \mathrm{d}x \mathrm{d}y \mathrm{d}z\\
\end{align}
$$
联合连续随机变量 $Y,Z$ 和连续随机变量 $X$ 之间的互信息：
$$
\begin{align}
I(X;Y,Z)
=\iiint p_{XYZ}(x,y,z) \log \frac{p_{XYZ}(x,y,z)}{p_X(x)p_{YZ}(y,z)} \mathrm{d}x \mathrm{d}y \mathrm{d}z
\end{align}
$$
- **性质 1** $I(X;Y) \geq 0$ 对于任何联合连续随机变量 $X,Y$ 恒成立
- **性质 2** $I(X;Y) = I(Y;X),\quad I(X;Y|Z) = I(Y;X|Z)$
- **性质 3** $I(X;Y,Z) = I(X;Y) + I(X;Z|Y) = I(X;Z) + I(X;Y|Z)$
- **性质 4** 如果 $X \to Y \to Z$, 那么 $I(X;Y) \geq I(X;Z), I(X;Y) \geq I(X;Y|Z)$

【注】上面的公式同样可以用微分熵去表示，并用韦恩图去证明。
### 2. 连续变量的微分熵

#### 2.1 微分熵及其性质

连续随机变量 $(X,R,p_X(x))$ 的 **离散化熵值**：
$$
\begin{aligned} H_{\Delta}(X) &= -\sum_{i=-\infty}^{+\infty} p_X(x_i) \Delta x_i \log \left(p_X(x_i) \Delta x_i\right) \\ &= -\sum_{i=-\infty}^{+\infty} \left[p_X(x_i) \log p_X(x_i)\right] \Delta x_i - \sum_{i=-\infty}^{+\infty} p_X(x_i) \Delta x_i \log \Delta x_i \\ \xrightarrow{\Delta x_i\rightarrow 0} & -\int p_X(x) \log p_X(x) \, \mathrm{d}x + \infty \end{aligned}
$$
定义连续随机变量 $X$ 的 **微分熵**：
$$
H_C(X) = h(X) \triangleq -\int p_X(x) \log p_X(x) \, \mathrm{d}x
$$
>[!Note] **微分熵的本质**
>微分熵 $H_C(X)$ **不反映**连续随机变量 $X$ 的不确定性。连续随机变量的不确定性一般都是无穷大。但微分熵的确在一定程度上反映了该连续随机变量的 **相对不确定性**；

由于概率密度函数 $f(x)$ 的取值可以大于 $1$ ，微分熵是 **可正可负** 的。以均匀分布为例，假设 $X$ 服从区间 $[0,a]$ 上的均匀分布，其概率密度函数为 $f(x)=1/a$ ，则微分熵为：
$$
H_C(X)=-\int_0^a\frac{1}{a}\log\frac{1}{a}\mathrm{d}x=\log a
$$
- 当 $a>1$ 时，该连续随机变量的微分熵为正；
- 当 $a=1$ 时，该连续随机变量的微分熵为零；
- 当 $a<1$ 时，该连续随机变量的微分熵为负。

从该例也可以看出，对于均匀分布，直观上区间越宽变量 $X$ 的不确定性越大，同时微分熵的计算结果也越大，可见微分熵能在一定程度上反应该随机变量的相对不确定性。
#### 2.2 条件/联合微分熵

$$H_{C}(X, Y) = - \iint p_{XY}(x,y) \log p_{XY}(x,y) \mathrm{d}x \mathrm{d}y$$
$$H_{C}(X|Y) = - \iint p_{XY}(x,y) \log p_{X|Y}(x|y) \mathrm{d}x \mathrm{d}y$$
$$H_{C}(X,Y) = H_{C}(X) + H_{C}(Y|X) = H_{C}(Y) + H_{C}(X|Y)$$
$$\begin{align}H_{C}(U^{N}) &= H_{C}(U_1, U_2, \cdots U_N) = \sum_{n=1}^{N} H_{C}(U_n | U_1 U_2 \cdots U_{n-1})\\&= \sum_{n=1}^{N} H_{C}(U_n | U^{n-1})\end{align}$$
$$\begin{align}I(X;Y) &= H_{C}(X) - H_{C}(X|Y)\\&= H_{C}(Y) - H_{C}(Y|X)\\&= H_{C}(X) + H_{C}(Y) - H_{C}(X,Y)\end{align}$$
【注】就像在 Lec-1 中表述的那样，用熵来衡量不确定性，用互信息来衡量变量间提供了多少确定性，在课件中用了 $I(X,Y)$ 而不是 $I(X;Y)$ ，其实并不够严谨。
#### 2.3 线性不变性

对于离散随机变量 $X$，令 $Y = f(X)$ 是 $X \to Y$ 上的一对一函数，则 $H(X) = H(Y)$，但是对于连续随机变量，有：
$$
H_C(Y) = - \int p(y) \log p(y) \,\mathrm{d}y = - \int p(x) \log \left[\frac{p(x)}{ f'(x)}\right] \,\mathrm{d}x \neq H_C(X)
$$
即使对于线性变换，微分熵也不具有不变性。

#### 2.4 微分熵极大化

**定理 1** 设 $X$ 满足 $\begin{align}\int_{-M}^Mp(x)\mathrm{d}x=1\end{align}$ 则微分熵 $H_C(X)\leq\ln(2M)$ ，**均匀分布** 时取等号。
$$
\begin{align}
J(p(x))
&\triangleq H_C(X)-\lambda\int_{-M}^{M} p(x)\mathrm{d}x\\
&=-\int_{-M}^M p(x)\ln p(x)\mathrm{d}x-\lambda\int_{-M}^M p(x)\mathrm{d}x\\
&=-\int_{-M}^M p(x)\ln(\mathrm{e}^\lambda p(x))\mathrm{d}x\\
&\leq-\int_{-M}^M p(x)\left(\frac{1}{\mathrm{e}^\lambda p(x)}-1\right)\mathrm{d}x\\
&=\frac{2M}{\mathrm{e}^\lambda}-1=\text{const}
\end{align}
$$
等号成立的条件是 $\begin{align}\frac{1}{\mathrm{e}^\lambda p(x)}=1\end{align}$ ，即 $p(x)=\mathrm{e}^{-\lambda}$ 为均匀分布时成立。由概率密度函数的归一性，$\begin{align}\int_{-M}^{M}p(x)\mathrm{d}x=1\end{align}$ 得 $\begin{align}p(x)=\frac{1}{2M}\end{align}$ ，故 $H_C(X)\leq\ln(2M)$ 成立。

**定理 2** 在方差 $\sigma^2$ 一定的条件下，当 $X$ 服从正态分布时，微分熵取得最大值 $\ln(\sqrt{2\pi\mathrm{e}}\sigma)$ 。
$$
\begin{align}
J(p(x))
&\triangleq H_C(X)-\lambda_1\int_{-\infty}^{+\infty}p(x)\mathrm{d}x-\lambda_2\int_{-\infty}^{+\infty}p(x)(x-m)^2\mathrm{d}x\\
&=\int_{-\infty}^{+\infty}p(x)\ln\left(\frac{\mathrm{e}^{\lambda_1}\mathrm{e}^{-\lambda_2(x-m)^2}}{p(x)}\right)\mathrm{d}x\\
&\leq\int_{-\infty}^{+\infty}p(x)\left(\frac{\mathrm{e}^{\lambda_1}\mathrm{e}^{-\lambda_2(x-m)^2}}{p(x)}-1\right)\mathrm{d}x\\
&=\text{const}
\end{align}
$$
等号成立的条件是 $\begin{align}p(x)=\mathrm{e}^{\lambda_1}\mathrm{e}^{-\lambda_2(x-m)^2}\end{align}$ ，根据概率密度函数的归一性 $\begin{align}\int_{-\infty}^{+\infty} p(x)\mathrm{d}x=1\end{align}$ 及约束条件 $\begin{align}\int_{-\infty}^{+\infty}p(x)(x-m)^2\mathrm{d}x=\sigma^2\end{align}$ 可得 $\begin{align}p(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(x-m)^2}{2\sigma^2}\right)\end{align}$ ，此时 $H_C=\ln(\sqrt{2\pi\mathrm{e}}\sigma)$。
#### 2.5 熵功率不等式

连续随机变量 $X$ 的熵功率定义为：
$$
\overline{\sigma_x}^2=\frac{1}{2\pi\mathrm{e}}\mathrm{e}^{2H_C(X)}
$$
高斯随机变量 $\begin{align}X\sim p(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{1}{2\sigma^2}x^2\right)\end{align}$ 的微分熵为：
$$
H_C(X)=\frac{1}{2}\ln(2\pi\mathrm{e}\sigma^2)
$$
其熵功率刚好为高斯随机变量的方差：
$$
\overline{\sigma_x}^2=\frac{1}{2\pi\mathrm{e}}\mathrm{e}^{2H_C(X)}=\sigma^2
$$
根据微分熵极大化中的定理 2 推导可得 **熵功率不等式**：
$$
H_C(X)\leq \ln(\sqrt{2\pi\mathrm{e}}\sigma)
\Leftrightarrow
\overline{\sigma_x}^2=\frac{1}{2\pi\mathrm{e}}\mathrm{e}^{2H_C(X)}\leq\sigma^2
$$
