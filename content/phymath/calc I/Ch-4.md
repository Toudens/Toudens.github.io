---
title: Ch-4 微分中值定理
date: 2026-03-19
weight: "4"
type: docs
---
### 函数极值

设函数 $f$ 在 $x_0$ 的某个邻域内有定义，如果存在 $\delta>0$ 使得对于任何 $x\in(x_0-\delta,x_0+\delta)$ 恒有 $f(x)\leq f(x_0)$ ,就称 $f(x_0)$ 是函数 $f$ 的一个极大值， $x=x_0$ 为极大值点

### 费马定理

设 $x_0$ 为函数 $f$ 的极值点，如果 $f$ 在 $x_0$ 处可导，则 $f'(x_0)=0$

### 罗尔定理

如果函数 $f$ 满足在闭区间 $[a,b]$ 上连续，在开区间 $(a,b)$ 内可导，$f(a)=f(b)$ 

那么至少存在一点 $\xi\in(a,b)$ 使得 $f'(\xi)=0$

### 拉格朗日中值定理

如果函数 $f$ 满足在闭区间 $[a,b]$ 上连续，在开区间 $(a,b)$ 内可导

那么至少存在一点 $\xi\in(a,b)$ 使得 $f'(\xi)=\dfrac{f(b)-f(a)}{b-a}$

### 柯西中值定理

设函数 $f,g$ 在 $[a,b]$ 上连续，在 $(a,b)$ 内可导，且 $g'$ 在 $(a,b)$ 内没有零点

则至少存在一点 $\xi\in(a,b)$ ，使得 $\dfrac{f'(\xi)}{g'(\xi)}=\dfrac{f(b)-f(a)}{g(b)-g(a)}$

### 洛必达法则

**形式1**

函数 $f$ 和 $g$ 在 $x_0$ 的某去心邻域 $\mathring{U}(x_0)$ 内可导，且 $g'\neq0$ 

如果 $\begin{aligned}\lim_{x\rightarrow x_0}f(x)=\lim_{x\rightarrow x_0}g(x)=0\end{aligned}$ ，且极限 $\begin{aligned}\lim_{x\rightarrow x_0}\frac{f'(x)}{g'(x)}\end{aligned}=A$ （或 $\infty$ ）

那么有$\begin{aligned}\lim_{x\rightarrow x_0}\frac{f(x)}{g(x)}=\lim_{x\rightarrow x_0}\frac{f'(x)}{g'(x)}\end{aligned}$

**形式2**

函数 $f$ 和 $g$ 在 $x_0$ 的某去心邻域 $\mathring{U}(x_0)$ 内可导，且 $g'\neq0$ 

如果 $\begin{aligned}\lim_{x\rightarrow x_0}g(x)=\infty\end{aligned}$ ，且极限 $\begin{aligned}\lim_{x\rightarrow x_0}\frac{f'(x)}{g'(x)}\end{aligned}=A$ （或 $\infty$ ）

那么有$\begin{aligned}\lim_{x\rightarrow x_0}\frac{f(x)}{g(x)}=\lim_{x\rightarrow x_0}\frac{f'(x)}{g'(x)}\end{aligned}$

### 带佩亚诺余项的泰勒公式

$f(x)=f(x_0)+f'(x_0)(x-x_0)+\cdots+\dfrac{f^{(n)}(x_0)}{n!}(x-x_0)^n+o((x-x_0)^n)$

### 带拉格朗日余项的泰勒公式

$f(x)=f(x_0)+f'(x_0)(x-x_0)+\cdots+\dfrac{f^{(n)}(x_0)}{n!}(x-x_0)^n+\dfrac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}$

### 极值第一判别法

如果 $f$ 在 $x_0$ 的某邻域内连续， $f'$ 在 $x_0$ 两侧异号，那么 $x_0$ 必定是 $f$ 的极值点

### 极值第二判别法

假设 $f$ 在 $x_0$ 的某邻域内连续，且在 $x_0$ 处二阶可导，如果 $f'(x_0)=0,f''(x_0)\neq0$ 

则 $x_0$ 必定是 $f$ 的极值点

### 凹凸性判别法

设 $f$ 在区间 $[a,b]$ 上连续，在 $(a,b)$ 内可导

曲线 $f$ 在 $[a,b]$ 上是凹的，当且仅当在 $(a,b)$ 内恒有 $f''\geq0$

曲线 $f$ 在 $[a,b]$ 上是凸的，当且仅当在 $(a,b)$ 内恒有 $f''\leq 0$

### 渐近线

当 $x\rightarrow x_0$ 时， $f(x)\rightarrow\infty$ ，则直线 $x=x_0$ 是 $y=f(x)$ 的一条垂直渐近线

$\begin{aligned}a=\lim_{x\rightarrow+\infty}\frac{f(x)}{x},b=\lim_{x\rightarrow+\infty}[f(x)-ax]\end{aligned}$ 

若 $a\neq0$ 则 $y=ax+b$ 为曲线的斜渐近线，否则 $y=b$ 为曲线的水平渐近线

### 曲率与曲率半径

$\begin{aligned}K=\lim_{l\rightarrow0}\frac{\theta}{l}\end{aligned}$ 定义曲线在 $P$ 点处的弯曲程度，称为曲率， $R=\dfrac{1}{K}$ 为曲率半径

$K(x)=\dfrac{|f''(x)|}{[1+(f'(x))^2]^{3/2}}$

曲率圆和曲线 $y=f(x)$ 在 $P$ 点相切，在切点有相同的凹凸性和曲率

曲率圆圆心坐标为 $(\xi,\eta),\begin{cases}\xi=x-\dfrac{f'(x)[1+(f'(x))^2]}{f''(x)}\\\eta=f(x)+\dfrac{1+[f'(x)]^2}{f''(x)}\end{cases}$ 

### 达布定理

设 $f$ 在 $(a,b)$ 内可导， $x_1,x_2\in(a,b)$ ，且 $x_1<x_2$ ，则对于任何介于  $f'(x_1)$ 和 $f'(x_2)$ 的实数 $\eta$ ，必存在 $\xi\in(a,b)$ ，使得 $\eta=f'(\xi)$
