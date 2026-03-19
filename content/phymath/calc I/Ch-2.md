---
title: Ch-2 函数的极限与连续性
date: 2026-03-19
type: docs
weight: "2"
---
### 函数极限

设 $f:D\rightarrow\mathrm{R}$ ，$D$ 是 $\mathrm{R}$ 的子集并且包含 $x_0$ 的某去心邻域，如果存在 $A\in\mathrm{R}$ ，使得对于任意的 $\varepsilon>0,\exists \delta>0$ ，当 $x\in \mathring{U}(x_0,\delta)\cap D$ 时，有 $|f(x)-A|<\varepsilon$ ，就称 $x$ 趋于 $x_0$ 时，$f(x)$ 趋于 $A$ ，记为 $\begin{aligned}\lim_{x\rightarrow x_0}f(x)=A\end{aligned}$

### 归结原理

设 $f:D\subset\mathrm{R}\rightarrow\mathrm{R},\exists\mathring{U}(x_0)\subset D$ ，则 $\begin{aligned}\lim_{x\rightarrow x_0}f(x)=A\end{aligned}$ 的充要条件为：对于任意满足 $\begin{aligned}\lim_{n\rightarrow\infty}x_n=x_0,x_n\neq x_0,n=1,2,3,\cdots\end{aligned}$ 的数列 $\{x_n\}$ ，其对应的函数值数列 $\{f(x_n)\}$ 均有 $\begin{aligned}\lim_{n\rightarrow\infty}f(x_n)=A\end{aligned}$

### 函数极限性质

**唯一性** 若函数在某点有极限，则极限是唯一的

**局部有界性** 设 $\begin{aligned}f:D\subset\mathrm{R}\rightarrow\mathrm{R},\lim_{x\rightarrow x_0}f(x)\end{aligned}$ 存在，则 $f(x)$ 在 $x_0$ 的某去心邻域内有界，即 $\exists M>0,\delta>0$ 当 $0<|x-x_0|<\delta$ 时， $|f(x)|<M$

**局部保号性** 如果 $\begin{aligned}\lim_{x\rightarrow x_0}f(x)=A>0\end{aligned}$ ，那么 $\forall p\in(0,A),\exists\delta>0,\forall x\in\mathring{U}(x_0,\delta),f(x)>p>0$

### 夹逼定理

设 $f,g,h:D\subset\mathrm{R}\rightarrow\mathrm{R}$ ，$D$ 包含 $x_0$ 的某去心邻域 $\mathring{U}(x_0,\delta)$ ，如果 $\forall x\in\mathring{U}(x,\delta)$ ，有 $g(x)\leq f(x)\leq h(x)$ ，且满足 $\begin{aligned}\lim_{x\rightarrow x_0}g(x)=\lim_{x\rightarrow x_0}h(x)=A\end{aligned}$  那么有 $\begin{aligned}\lim_{x\rightarrow x_0}f(x)=A\end{aligned}$

### 单侧极限

$\begin{aligned}\lim_{x\rightarrow x_0}f(x)=A\Leftrightarrow\lim_{x\rightarrow x_0^-}f(x)=\lim_{x\rightarrow x_0^+}f(x)=A\end{aligned}$

$\begin{aligned}\lim_{x\rightarrow \infty}f(x)=A\Leftrightarrow\lim_{x\rightarrow -\infty}f(x)=\lim_{x\rightarrow +\infty}f(x)=A\end{aligned}$

### 函数连续与间断点

设 $f:D\subset\mathrm{R}\rightarrow\mathrm{R}$ ，$D$ 包含 $x_0$ 的某个邻域，若 $\begin{aligned}\lim_{x\rightarrow x_0}f(x)=f(x_0)\end{aligned}$ 则称 $f$ 在 $x_0$ 处连续

**第一类间断点** 左极限 $\begin{aligned}\lim_{x\rightarrow x_0^-}f(x)\end{aligned}$ 和右极限 $\begin{aligned}\lim_{x\rightarrow x_0^+}f(x)\end{aligned}$ 都存在但 $f$ 在 $x_0$ 处不连续

**跳跃间断点** $\begin{aligned}\lim_{x\rightarrow x_0^-}f(x)\neq\lim_{x\rightarrow x_0^+}f(x)\end{aligned}$

**可去间断点** $\begin{aligned}\lim_{x\rightarrow x_0}f(x)\neq f(x_0)\end{aligned}$ 或 $f(x)$ 在 $x_0$ 处没有定义

**第二类间断点** 如果 $f$ 在 $x_0$ 处的左右极限至少有一个不存在

### 函数一致连续

设函数 $f:I\rightarrow\mathrm{R}$ ，如果 $\forall\varepsilon>0,\exists\delta>0$ ，使得 $\forall x_1,x_2\in I$ ，当 $|x_1,x_2|<\delta$ 时，都有 $|f(x_1)-f(x_2)|<\varepsilon$ ，就称函数 $f$ 在区间 $I$ 上一致连续

### 康托尔定理

设函数 $f(x)$ 在有限闭区间 $[a,b]$ 上连续，则 $f(x)$ 在 $[a,b]$ 上一致连续

### 无穷小

设 $f(x),g(x)$ 是当 $x\rightarrow x_0$ 时的无穷小，且 $g(x)\neq0$

* 若 $\begin{aligned}\lim_{x\rightarrow x_0}\frac{f(x)}{g(x)}=0\end{aligned}$ ，则称 $f(x)$ 是比 $g(x)$ 高阶的无穷小，记为 $f(x)=o(g(x))$
* 若 $\begin{aligned}\lim_{x\rightarrow x_0}\frac{f(x)}{g(x)}=0\end{aligned}$ ，则称 $g(x)$ 是比 $f(x)$ 低阶的无穷小，记为 $f(x)=o(g(x))$
* 若 $\begin{aligned}\lim_{x\rightarrow x_0}\frac{f(x)}{g(x)}=A\neq0\end{aligned}$ ，则称 $f(x)$ 与 $g(x)$ 是同阶无穷小，记为 $f(x)=O(g(x))$
* 若 $\begin{aligned}\lim_{x\rightarrow x_0}\frac{f(x)}{g(x)}=1\end{aligned}$ ，则称 $f(x)$ 与 $g(x)$ 是等价无穷小，记为 $f(x)\sim g(x)$

### 无穷大

设 $f(x),g(x)$ 是当 $x\rightarrow x_0$ 时的无穷大

* 若 $\begin{aligned}\lim_{x\rightarrow x_0}\frac{f(x)}{g(x)}=0\end{aligned}$ ，则称 $f(x)$ 是比 $g(x)$ 低阶的无穷大（增长更慢 ）
* 若 $\begin{aligned}\lim_{x\rightarrow x_0}\frac{f(x)}{g(x)}=0\end{aligned}$ ，则称 $g(x)$ 是比 $f(x)$ 高阶的无穷大（增长更快）
* 若 $\begin{aligned}\lim_{x\rightarrow x_0}\frac{f(x)}{g(x)}=A\neq0\end{aligned}$ ，则称 $f(x)$ 与 $g(x)$ 是同阶无穷大
* 若 $\begin{aligned}\lim_{x\rightarrow x_0}\frac{f(x)}{g(x)}=1\end{aligned}$ ，则称 $f(x)$ 与 $g(x)$ 是等价无穷大

### 等价无穷小替换

设 $f,g,\alpha,\beta$ 当 $x\rightarrow x_0$ 时是无穷小，且 $f\sim\alpha,g\sim\beta$ ，如果 $\begin{aligned}\lim_{x\rightarrow x_0}\frac{\alpha(x)}{\beta(x)}\end{aligned}$ 存在，

那么有 $\begin{aligned}\lim_{x\rightarrow x_0}\frac{f(x)}{g(x)}=\lim_{x\rightarrow x_0}\frac{\alpha(x)}{\beta(x)}\end{aligned}$

### 有限闭区间上连续函数的性质

有界性、最大值最小值定理、零点存在定理、介值定理、不动点