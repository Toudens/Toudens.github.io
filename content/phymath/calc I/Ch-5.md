---
title: Ch-5 不定积分
date: 2026-03-19
type: docs
weight: "5"
---
### 第一换元积分法

设 $f(u)$ 存在原函数 $F(u),u=\varphi(x)$ 可导，则函数 $f(\varphi(x))\varphi'(x)$ 也存在原函数

$$\begin{aligned}\int f(\varphi(x))\varphi'(x)\mathrm{d}x=\int f(\varphi(x))\mathrm{d}\varphi(x)=\int f(u)\mathrm{d}u=F(u)+C=F(\varphi(x))+C\end{aligned}$$

### 第二换元积分法

设 $f(x)$ 连续，$x=\varphi(t)$ 有连续导数，且 $\varphi'(t)\neq0$ 如果 $\begin{aligned}\int f(\varphi(t))\varphi'(t)\mathrm{d}t=F(t)+C\end{aligned}$

则 $\begin{aligned}\int f(x)\mathrm{d}x=\int f(\varphi(t))\varphi'(t)\mathrm{d}t=F(t)+C=F(t)+C=F(\varphi^{-1}(t))+C\end{aligned}$

### 分部积分法

$$\begin{aligned}\int u(x)v'(x)\mathrm{d}x=u(x)v(x)-\int v(x)u'(x)\mathrm{d}x\end{aligned}$$

### 有理函数的不定积分

一切有理函数的原函数可以用有理函数、对数函数和反正切函数表示出来

### 三角有理函数的不定积分

设 $t=\tan\dfrac{x}{2},|x|<\pi$ ，则 $x=2\arctan{t}$ 有以下替换：

$$\begin{cases}\mathrm{d}x=\dfrac{2}{1+t^2}\mathrm{d}t\\\sin x=\dfrac{2\tan\dfrac{x}{2}}{1+\tan^2\dfrac{x}{2}}=\dfrac{2t}{1+t^2}\\\cos x=\dfrac{1-\tan^2\dfrac{x}{2}}{1+\tan^2\dfrac{x}{2}}=\dfrac{1-t^2}{1+t^2}\end{cases}$$

则 $\begin{aligned}\int R(\sin x,\cos x)\mathrm{d}x=\int R(\frac{2t}{1+t^2},\frac{1-t^2}{1+t^2})\cdot\frac{2}{1+t^2}\mathrm{d}t\end{aligned}$

### 其它可有理化函数的不定积分

设 $R$ 为有理函数，则以 $\mathrm{e}^x$ 为变量的有理函数 $R(\mathrm{e}^x)$ 的积分 $\begin{aligned}\int R(\mathrm{e}^x)\mathrm{d}x\end{aligned}$ 

可通过变量替换 $x=\ln t$ 化成有理函数的积分 $\begin{aligned}\int R(t)\frac{1}{t}\mathrm{d}t\end{aligned}$
