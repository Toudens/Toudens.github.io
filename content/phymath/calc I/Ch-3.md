---
title: Ch-3 导数与微分
date: 2026-03-19
type: docs
weight: "3"
---
### 导数定义

设函数 $y=f(x)$ 在 $x_0$ 的某个邻域内有定义，如果极限 $\begin{aligned}\lim_{x\rightarrow x_0}\frac{f(x)-f(x_0)}{x-x_0}\end{aligned}$ 存在，就称 $f$ 在 $x_0$ 处可导，$x_0$ 是 $f$ 的可导点，极限值为 $f$ 在 $x_0$ 处的导数，记为 $f'(x_0)$

### 单侧导数

若函数 $f$ 在 $x_0$ 的某个邻域有定义，则 $f$ 在 $x_0$ 处可导当且仅当 $f$ 在 $x_0$ 处分别左右导数相等

### 反函数求导

函数 $y=f(x)$ 在 $U(x_0)$ 严格单调，在 $x_0$ 可导且 $f'(x_0)\neq0,y_0=f(x_0)$, $g:U(y_0)\rightarrow U(x_0)$ 为 $y=f(x)$ 的反函数，则函数 $g$ 在 $y_0$ 处可导，且 $g'(y_0)=\dfrac{1}{f'(x_0)}$

由 $y_0=f(x_0)$ 有 $g'(f(x_0))=\dfrac{1}{f'(x_0)}$ ，即 $g'(x)=\dfrac{1}{f'(g(x))}$

### 参数方程的导数

对于参数方程 $\begin{cases}x=\varphi(t)\\y=\psi(t)\end{cases}$ 有 $\dfrac{\mathrm{d}x}{\mathrm{d}t}=\varphi'(t)，\dfrac{\mathrm{d}y}{\mathrm{d}t}=\psi'(t)$  则 $\dfrac{\mathrm{d}y}{\mathrm{d}x}=\dfrac{\psi'(t)}{\varphi'(t)}$ 

参数方程的导数可以表示为 $\begin{cases}x=\varphi(t)\\y=\dfrac{\psi'(t)}{\varphi'(t)}\end{cases}$  或 $\dfrac{\mathrm{d}y}{\mathrm{d}x}=\dfrac{\psi'(t)}{\varphi'(t)}\bigg|_{t=\varphi^{-1}(x)}$

### 莱布尼茨公式

若函数 $u,v$ 均 $n$ 阶可导，则乘积函数 $uv$ 也 $n$ 阶可导

$\begin{aligned}(uv)^{(n)}=\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}u^{(n-k)}v^{(k)}\end{aligned}$

### 微分定义

设 $y=f(x)$ 在 $x_0$ 某个邻域内有定义， $\Delta x$ 是自变量的一个改变量，如果存在不依赖于 $\Delta x$ 的常数 $A$ ，使得当 $|\Delta x|$ 充分小时，函数的增量 

$\Delta y=f(x_0+\Delta x)-f(x_0)=A\Delta x+o(\Delta x),\Delta x\rightarrow 0$

那么称 $f$ 在 $x_0$ 处可微，称 $A\Delta x$ 为 $f$ 在 $x_0$ 处的微分，记为 $\mathrm{d}y|_{x=x_0}=A\Delta{x}$

### 近似估计与误差分析

$f(x_0+\Delta{x})\approx f(x_0)+f'(x_0)\Delta x$

在测量某个值 $x^*$ 时得到的 $x$ 是近似值，程 $|x-x^*|$ 为绝对误差， $\dfrac{|x-x^*|}{|x|}$ 为相对误差 

如果存在 $\delta_x>0$ 使 $|x-x^*|\leq\delta_x$ ，则称 $\delta_x$ 为绝对误差限，$\dfrac{\delta_x}{|x|}$ 称为相对误差限