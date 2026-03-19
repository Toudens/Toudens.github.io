---
title: Ch-1 信息的度量
date: 2026-03-18
type: docs
---
## 随机事件的自信息与互信息
### 随机变量与概率空间

对于随机变量的 **概率空间** $\{X,\mathcal{X},q(x)\}$ ，有如下定义与约束： 
*  $\mathcal{X}$ 为 $X$ 的 **取值空间**，$\mathcal{X}=\{x_k|k=1,2,\cdots,K\}$
* $q(x)$ 为事件 $\{X=x\}$ 发生的 **概率**，$q(x)\geq0,\sum_{x\in\mathcal{X}}q(x)=1$

对于 **联合变量对** $(X,Y)$ 的二维随机变量 $\{(X,Y),\mathcal{X}\times\mathcal{Y},p(x,y)\}$ ,有如下定义与约束：
* $p(x,y)=P\{X=x,Y=y\}$
* $\mathcal{X}=\{x_k|k=1,2,\cdots,K\},\mathcal{Y}=\{y_j|j=1,2,\cdots,J\}$
### 事件的自信息

对于概率空间 $\{X,\mathcal{X},q(x)\}$ ，事件 $\{X=x_k\}$ 的 **自信息** 定义为：$$
I(x_k)=-\log_aq(x_k)
$$ 当 $a=2$ 时单位为 **比特** bit ，当$a=e$ 时单位为 **奈特** nat。

> [!Note]**定义为概率的负对数的优点：**
> 1、符合概率越小，信息量越大的要求；\
> 2、对数函数是比较简单的函数，容易进行数学处理；\
> 3、对数函数的可加性符合生活中信息可叠加的经验。

> [!Note]**事件自信息的本质：**
> 1、事件发生后对外界所提供的信息量；\
> 2、事件发生前外界为确证该事件发生所需的信息量；\
> 3、事件的自信息 **不代表** 事件的不确定性。

**性质1**：$q(x_k)$ 越大，$I(x_k)$ 越小，概率越小的事件其自信息越大。

**性质2**：$q(x_k)=1$ , $I(x_k)=0$ ，确定事件的自信息为零。

**性质3**：$q(x_k)\rightarrow0$ , $I(x_k)=\infty$。

### 事件的条件自信息

二维随机变量 $\{(X,Y),\mathcal{X}\times\mathcal{Y},p(x,y)\}$ ，事件 $\{Y=y_j\}$ 发生的条件下事件 $\{X=x_k\}$ 的**条件自信息定义**为：
$$
I(x_k|y_j)=-\log p(x_k|y_j)
$$

> [!Note]**事件条件自信息的本质：**
> 1、事件 $\{Y=y_j\}$ 发生后，$\{X=x_k\}$ 如果再发生需要的新的信息量；\
> 2、事件 $\{Y=y_j\}$ 发生后，如果 $\{X=x_k\}$ 再发生提供给外界的信息量。

**性质1**：若 $\{Y=y_j\}$ 与 $\{X=x_k\}$ 为 **无关事件**，则有 $I(x_k)=I(x_k|y_j)$。

### 事件的互信息

二维随机变量 $\{(X,Y),\mathcal{X}\times\mathcal{Y},p(x,y)\}$ ，事件 $\{Y=y_j\}$ 与事件 $\{X=x_k\}$ 之间的 **互信息** 定义为：
$$
\begin{align}
I(x_k;y_j)
&=I(x_k)-I(x_k|y_j)
=-\log q(x_k)-\{-\log p(x_k|y_j)\}\\
&=\log\frac{p(x_k|y_j)}{q(x_k)}
=\log\frac{p(x_k,y_j)}{q(x_k)\cdot\omega(y_j)}
=\log\frac{p(y_j|x_k)}{\omega(y_j)}
=I(y_j;x_k)
\end{align}
$$

> [!Important]**事件互信息的本质：**
> 事件 $\{Y=y_j\}$ 发生后对事件 $\{X=x_k\}$ 不确定性的 **降低量（可正可负）**。
>
> **注：** 此处的解释不甚完美，在事件的自信息的解释中不将 $I(x_k)$ 视为不确定性的表现，此处却引入了不确定性。由于 $x_k$ 和 $y_j$ 的位置互换不影响互信息的值，不妨观察上述定义式，对于等式第二行的中间结果可以得到：
>$$I(x_k;y_j)=I(x_k)+I(y_j)-I(x_k,y_j)$$ 即事件 $\{X=x_k\}$ 与 $\{Y=y_j\}$ 的自信息之和与二者的联合自信息（见下文）之差，因此互信息应解释为：两个信息同时发生时，是产生了新信息（负）还是产生了冗余信息（正），或解释为两个信息同时发生时产生冗余信息的程度。

**性质1**：$I(x_k;y_j)=I(y_j;x_k)$ 用条件概率的定义展开即可证明。

**性质2**：若 $\{Y=y_j\}$ 与 $\{X=x_k\}$ 为 **无关事件**，则有 $I(x_k;y_j)=0$。

### 事件的联合自信息

二维随机变量 $\{(X,Y),\mathcal{X}\times\mathcal{Y},p(x,y)\}$ ，事件 $\{Y=y_j\}$ 与事件 $\{X=x_k\}$ 之间的 **联合自信息**定义为：
$$
I(x_k,y_j)=-\log p(x_k,y_j)
$$
> [!Note]**事件的联合自信息的本质：**
> 事件 $\{X=x_k\}$ 和 $\{Y=y_i\}$ 同时发生需要的或同时发生后对外界提供的信息量。

在给定 $Z=z$ 的条件下，事件 $X=x$ 与 $Y=y$ 之间的 **条件互信息** 为：
$$
I(x;y|z)=\log\frac{p(x|y,z)}{p(x|z)}=\log\frac{p(x,y|z)}{p(x|z)\cdot p(y|z)}
$$

联合事件 $\{Y=y,Z=z\}$ 与事件 $\{X=x\}$ 之间的 **互信息** 为：
$$
I(x;y,z)=\log\frac{p(x|y,z)}{p(x)}=\log\frac{p(x,y,z)}{p(x)\cdot p(y,z)}
$$

$$
\begin{align}
I(x;y,z)
&=\log\frac{p(x|y,z)}{p(x)}
=\log\frac{p(x|y)\cdot p(x|y,z)}{p(x)\cdot p(x|y)}
=\log\frac{p(x|y)}{p(x)}+\log\frac{p(x|y,z)}{p(x|y)}\\
&=I(x;y)+I(x;z|y)
\end{align}
$$

## 随机变量的熵及性质
### 随机变量的熵

随机变量的 **熵** 定义为随机变量各个事件的平均自信息：
$$
H(X)
=E[I(X)]
=\sum_{x\in\mathcal{X}}q(x)I(x)
=-\sum_{x\in\mathcal{X}}q(x)\log q(x)
$$

> [!Note]**熵与自信息的区别：**
> 熵针对的是随机变量，自信息针对具体的事件。熵是随机 **变量不确定性** 的度量。

### 随机变量的联合熵

随机变量的 **联合熵** 定义为随机变量各个事件的平均联合自信息：
$$
H(X,Y)=E[I(X,Y)]=-\sum_{x\in\mathcal{X},y\in\mathcal{Y}}p(x,y)\log p(x,y)
$$
### 随机变量的条件熵

**定义1**：给定 $Y=y$ 的条件下，$X$ 的 **条件熵** 为：
$$
H(X|y)
=\sum_{x\in\mathcal{X}}p(x|y)I(x|y)
=-\sum_{x\in\mathcal{X}}p(x|y)\log p(x|y)
$$

**定义2**：随机变量 $X$ 相对于随机变量 $Y$ 的 **条件熵** 为：
$$
H(X|Y)
=E[H(X|y)]
=-\sum_{x\in\mathcal{X}}\sum_{y\in\mathcal{Y}}p(x,y)\log p(x|y)
$$

**性质1**：$X$ 和 $Y$ **统计独立** 时，有 $H(X|Y)=H(X)$。

**性质2**：$X$ 和 $Y$ 的联合熵满足 **链式法则**。
$$
H(X,Y)=H(X)+H(Y|X)=H(Y)+H(X|Y)
$$
$$
\begin{align}
H(X,Y)&=E[I(X,Y)]
=-\sum_{x\in\mathcal{X}}\sum_{y\in\mathcal{Y}}p(x,y)\log p(x,y)\\
&=-\sum_{x\in\mathcal{X}}\sum_{y\in\mathcal{Y}}p(x,y)\log p(x)-
\sum_{x\in\mathcal{X}}\sum_{y\in\mathcal{Y}}p(x,y)\log p(y|x)\\
&=H(X)+H(Y|X)
\end{align}
$$
$$
H(X,Y,Z)=H(X)+H(Y,Z|X)=H(X)+H(Y|Z)+H(Z|X,Y)
$$

**性质3**：$X$ 和 $Y$ **统计独立** 时，有 $H(X,Y)=H(X)+H(Y)$。

### 熵的性质
$$
X\sim
\begin{pmatrix}
x_1&x_2&\cdots&x_K\\
p_1&p_2&\cdots&p_K
\end{pmatrix}
$$
$$
H(X)
\triangleq H_K(p_1,p_2,\cdots,p_K)
\triangleq H_K(P)
=-\sum_{k=1}^{K}p_k\log p_k
$$
1. $H_K(P)$ 对概率矢量 $P$ 的分量是 **对称** 的；
2. **非负性** ，即 $H_K(P)\geq 0$；
3. **确定性** ，若 $P=(p_1,p_2,\cdots,p_K)$ 中有一个分量为 $1$ ，其余均为零，则 $H_K(P)=0$；
4. **可扩展性** ，即 $\lim_{\epsilon\rightarrow0}H_{K+1}(p_1,p_2,\cdots,p_K-\epsilon,\epsilon)=H_K(p_1,p_2,\cdots,p_K)$；
5. **可加性** ，$H(X_2)|_{X_2\in\mathcal{X}_2}=H(X_1)|_{X_1\in\mathcal{X}_1}+H(X_2|X_1)|_{X_2\in\mathcal{X}_2}^{X_1\in\mathcal{X}_1}$；

> [!Note] **链式法则**
> 对变量 $X$ 可以进行多步分层的观察，每一步都可从上一步的观察结果中得到更为细致的结果，变量 $X$ 在最后的观察结果集合中的不确定性等于第一次观察结果的不确定性，加上其后每次观察结果在前一次观察结果已知的前提下的条件不确定性。

6. **极值性** ，$H_K(p_1,p_2,\cdots,p_K)\leq H_K(\frac{1}{K},\frac{1}{K},\cdots,\frac{1}{K})=\log K$；

$$
\begin{align}
&H_K(p_1,p_2,\cdots,p_K)+\sum_{k=1}^Kp_k\log q_k=\sum_{k=1}^K p_k\log\frac{q_k}{p_k}\leq\log\mathrm{e}\cdot\sum_{k=1}^Kp_k(\frac{q_k}{p_k}-1)=0\\
&\Rightarrow H_K(p_1,p_2,\cdots,p_K)\leq-\sum_{k=1}^Kp_k\log q_k
\end{align}
$$
7. **条件熵小于熵**，增加条件使熵减少 $H(X|Y)\leq H(X)$；
$$
\begin{align}
H(X|Y)
&=E[H(X|y)]=-\sum_{x\in\mathcal{X}}\sum_{y\in\mathcal{Y}}p(x,y)\log p(x|y)\\
&=-\sum_{y\in\mathcal{Y}}\omega(y)(\sum_{x\in\mathcal{X}}p(x|y)\log p(x|y))\\
&\leq -\sum_{y\in\mathcal{Y}}\omega(y)(\sum_{x\in\mathcal{X}}p(x|y)\log q(x))\\
&=-\sum_{x\in\mathcal{X}}q(x)\log q(x)=H(X)
\end{align}
$$
8. **凸性**， $H_K(P)$ 是 $P=(p_1,p_2,\cdots,p_K)$ 的 **严格上凸函数**，即对任何 $\theta,0<\theta<1$ ，和任何两个 $K$ 维概率矢量 $P_1,P_2,P_1\neq P_2$ ，有：
$$
H_K(\theta P_1+(1-\theta)P_2)>\theta H_K(P_1)+(1-\theta)H_K(P_2)
$$
### 凸集与凸函数

令 $\alpha=(\alpha_1,\alpha_2,\cdots,\alpha_k),\beta=(\beta_1,\beta_2,\cdots,\beta_k)$ 是 $k$ 维矢量空间集合 $R$ 中的任何两个矢量，如果对于任何实数 $\theta (0\leq\theta\leq1)$ 有：$\theta\alpha+(1-\theta)\beta\in R$ ，则称 $R$ 为 **凸集合**。

定义在凸集合 $R$ 上的实值矢量函数 $f$ 被称为 **上凸函数**，当且仅当对任何两个矢量 $\alpha,\beta$ 以及实数 $\theta (0\leq\theta\leq1)$ 有 $\theta f(\alpha)+(1-\theta)f(\beta)\leq f[\theta\alpha+(1-\theta)\beta]$。若不等号翻转为下凸函数。

**性质1**：若 $f_1(\alpha),f_2(\alpha),\cdots,f_L(\alpha)$ 是上凸函数，$C_1,C_2,\cdots,C_L$ 为正，有上凸函数：
$$
\sum_{l=1}^L C_lf_l(\alpha)
$$

**性质2**：一元函数 $f(\alpha)$ 上凸的充要条件是在所定义的区间中满足：
$$
\frac{\mathrm{d}^2f(\alpha)}{\mathrm{d}\alpha^2}\leq 0
$$

**性质3**：Jensen 不等式，令 $(\alpha_1,\alpha_2,\cdots,\alpha_L)$ 是凸集中的一组矢量， $f(\alpha)$ 是该凸集中的一个上凸函数，$(\theta_1,\theta_2,\cdots,\theta_L)$ 是一组概率分布，则有：
$$
\sum_{l=1}^L\theta_lf(\alpha_l)\leq f
\begin{bmatrix}
\sum_{l=1}^L\theta_l\alpha_l
\end{bmatrix}
$$
