---
title: Ch-2 随机变量及概率分布
date: 2026-03-19
weight: "2"
type: docs
---
### 随机变量

设随机事件的 **样本空间** 为 $S$ ，若 $X=X(e)$ 为定义在样本空间 $S$ 上的 **实值单值函数**，且 $e\in S$ 则称 $X=X(e)$ 为随机变量，常用大写英文字母表示

若随机变量的所有取值为 **有限个** 或 **可列个** ，则称此变量为 **离散型随机变量**
### 概率分布律

设 $X$ 为 **离散型随机变量**，若其可能取值为 $x_1,x_2,\cdots,x_k,\cdots$ ，则称
$$
P\{X=x_k\}=p_k,\quad k=1,2,\cdots
$$
为 $X$ 的 **概率分布律** 或 **概率分布列**，称为 $X$ 的分布律或分布列

概率分布律满足以下两条性质：
$$
(1)\space p_k\geq0,k=1,2,\cdots;\quad(2)\sum_{k=1}^{+\infty}p_k=1
$$

| 分布类型           | 概率分布律                                                                                      | 记号                 | 备注                   |
| -------------- | ------------------------------------------------------------------------------------------ | ------------------ | -------------------- |
| 0-1分布          | $P\{X=k\}=p^k(1-p)^{1-k}$                                                                  | $X\sim 0-1(p)$     | 0-1                  |
| 二项分布           | $P\{X=k\}=\mathrm{C}_n^kp^k(1-p)^{n-k}$                                                    | $X\sim B(n,p)$     | Binomial             |
| 泊松分布           | $\begin{align}P\{X=k\}=\frac{e^{-\lambda}\lambda^k}{k!}\end{align}$                        | $X\sim P(\lambda)$ | Poisson              |
| 超几何分布          | $\begin{align}P\{X=k\}=\frac{\mathrm{C}_a^k\mathrm{C}_b^{n-k}}{\mathrm{C}_N^n}\end{align}$ | $X\sim H(n,a,N)$   | Hypergeometric       |
| 帕斯卡分布<br>负二项分布 | $\begin{align}P\{X=k\}=\mathrm{C}_{k-1}^{r-1}p^r(1-p)^{k-r}\end{align}$                    | $X\sim NB(r,p)$    | Negative<br>Binomial |
### 0-1 分布

若随机变量 $X$ 的概率分布律为
$$
P\{X=k\}=p^k(1-p)^{1-k},\quad k=0,1
$$
其中 $0<p<1$ ，则称 $X$ 服从参数为 $p$ 的 **0-1 分布**，也称为 **两点分布** 
并用记号 $X\sim 0-1(p)$ 表示
### 二项分布

若随机变量 $X$ 的概率分布律为
$$
P\{X=k\}=\mathrm{C}_n^kp^k(1-p)^{n-k},\quad k=0,1,2,\cdots,n,
$$
其中 $0<p<1,n\geq 1$ 则称 $X$ 服从参数为 $(n,p)$ 的 **二项分布**
并用记号 $X\sim B(n,p)$ 表示

设在 $n$ 次独立重复试验中，每次试验都只有两个结果：$A,\overline{A}$ ，且每次试验中 $A$ 发生的概率不变，记 $P(A)=p,0<p<1$ ，则称这一系列试验为 $n$ **重伯努利试验**
### 泊松分布

若随机变量 $X$ 的概率分布律为
$$
P\{X=k\}=\frac{e^{-\lambda}\lambda^k}{k!},\quad k=0,1,2\cdots,
$$
其中 $\lambda>0$ ，则称 $X$ 服从参数为 $\lambda$ 的 **泊松分布** 
并用记号 $X\sim P(\lambda)$ 表示

当 $n$ 足够大， $p$ 充分小（一般要求 $p<0.1$ ），且 $np$ 保持适当大小时，参数为 $(n,p)$ 的二项分布可以用参数为 $\lambda=np$ 的泊松分布 **近似描述**
$$
\begin{align}
P\{X=k\}&=\mathrm{C}_n^kp^k(1-p)^{n-k}
=\frac{n!}{k!(n-k)!}p^k(1-p)^{n-k}\\
&=\frac{n!}{k!(n-k)!}(\frac{\lambda}{n})^k(1-\frac{\lambda}{n})^{n-k}\\
&=\frac{n(n-1)\cdots(n-k+1)}{n^k}\cdot\frac{\lambda^k}{k!}\cdot
\frac{(1-\lambda/n)^n}{(1-\lambda/n)^k}\\
&\approx\frac{e^{-\lambda}\lambda^k}{k!}
\end{align}
$$
### 超几何分布

若随机变量 $X$ 的概率分布律为
$$
P\{X=k\}=\frac{\mathrm{C}_a^k\mathrm{C}_b^{n-k}}{\mathrm{C}_N^n},\quad k=l_1,l_1+1,\cdots,l_2,\quad a+b=N
$$
其中 $l_1=\max\{0,n-b\},l_2=\min\{a,n\}$ ，则称 $X$ 服从 **超几何分布**
并用记号 $X\sim H(n,a,N)$ 表示
### 帕斯卡分布

若随机变量 $X$ 的概率分布律为
$$
\begin{align}
P\{X=k\}&=P\{\text{前}\space k-1\space\text{次中恰有}\space r-1\space \text{次}\space A\space 发生，且第\space k\space 次\space A\space 发生\}\\
&=\mathrm{C}_{k-1}^{r-1}p^r(1-p)^{k-r},\space k=r,r+1,r+2,\cdots
\end{align}
$$
则称 $X$ 服从参数为 $(r,p)$ 的 **帕斯卡分布** ，也称为 **负二项分布**
并用记号 $X\sim NB(r,p)$ 表示
### 概率分布函数

设 $X$ 为一随机变量，$x$ 为任意实数，函数
$$
F(x)=P\{X\leq x\}
$$
称为随机变量 $X$ 的 **概率分布函数**，简称分布函数
### 连续型随机变量

对于随机变量 $X$ ，其 **分布函数** 为 $F(X)$ ，若存在一个 **非负的实值函数** $f(x),-\infty<x<+\infty$ ，则对于任意实数 $x$ ，有：
$$
F(x)=\int_{-\infty}^{x} f(t)\mathrm{d}t
$$
则称 $X$ 为 **连续型随机变量** ，称 $f(x)$ 为 **概率密度函数**，离散型随机变量 **没有** 密度函数

| 分布类型 | 密度函数                                                                                                     | 记号                      | 备注          |
| ---- | -------------------------------------------------------------------------------------------------------- | ----------------------- | ----------- |
| 均匀分布 | $f(x)=\begin{cases}\begin{align}&\frac{1}{b-a},&x\in(a,b)\\&0,&x\not\in(a,b)\end{align}\end{cases}$      | $X\sim U(a,b)$          | Uniform     |
| 正态分布 | $f(x)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}},\quad -\infty<x<+\infty$               | $X\sim N(\mu,\sigma^2)$ | Normal      |
| 指数分布 | $f(x)=\begin{cases}\begin{align}&\lambda \mathrm{e}^{-\lambda x},&x>0\\&0,&x\leq0\end{align}\end{cases}$ | $X\sim E(\lambda)$      | Exponential |
### 均匀分布

设随机变量 $X$ 具有 **密度函数**
$$
f(x)=\begin{cases}\begin{align}
&\frac{1}{b-a},&x\in(a,b)\\
&0,&x\not\in(a,b)
\end{align}\end{cases}
$$
则称 $X$ 在区间 $(a,b)$ 上 **均匀分布**，记为 $X\sim U(a,b)$ 
### 正态分布

设随机变量 $X$ 具有 **密度函数**
$$
f(x)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}},
\quad -\infty<x<+\infty
$$
其中 $-\infty<\mu<+\infty,\sigma>0$ 则称 $X$ 服从参数为 $(\mu,\sigma)$ 的 **正态分布**
简称 $X$ 为 **正态变量**，记为 $X\sim N(\mu,\sigma^2)$

正态变量 $X$ 的密度函数 $f(x)$ 具有以下性质：
$$
\begin{align}
&(1)\space f(x)关于\space x=\mu\space 对称\\
&(2)\max_{-\infty<x<+\infty} f(x)=f(\mu)=\frac{1}{\sqrt{2\pi}\sigma}\\
&(3)\lim_{|x-\mu|\rightarrow+\infty}f(x)=0
\end{align}
$$

特别地，当 $\mu=0,\sigma=1$ 时，此时的正态变量服从 **标准正态分布**
$$
\varphi(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2},\quad -\infty<x<+\infty
$$
### 指数分布

设随机变量 $X$ 具有 **密度函数**
$$
f(x)=\begin{cases}\begin{align}
&\lambda \mathrm{e}^{-\lambda x},&x>0\\
&0,&x\leq0
\end{align}\end{cases}
$$
其中 $\lambda>0$ ，则称 $X$ 服从参数为 $\lambda$ 的指数分布，记为 $X\sim E(\lambda)$
