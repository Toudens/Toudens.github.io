---
title: Appendix 易错点
type: docs
date: 2026-03-19
weight: "7"
---
### 易错点1

导函数在 $x_0$ 两侧的不同单调性确保了 $f(x_0)$ 取到极值是充分条件而非必要条件

例如 $f(x)=\begin{cases}x^2(1+\sin^2(\dfrac{1}{x})),&x\neq0\\0,&x=0\end{cases}$
### 易错点2

函数可导一定连续，函数连续不一定可导
### 易错点3

原函数不可能有第一类间断点

### 易错点4

利用导数的定义研究函数在一点的可导性时，要满足以下三个条件：

$\begin{aligned}\lim_{\Delta x\rightarrow0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}\end{aligned}$ 中 $\Delta x$ 的替换项必须与 $\Delta x$ 是同阶无穷小

$\Delta x\rightarrow 0$ 必须从左右两侧趋于 $0$

$\begin{aligned}\lim_{\Delta x\rightarrow0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}\end{aligned}$ 的分子上一定要有 $f(x_0)$ 这个元素  

### 易错点5

若 $f(x)$ 为周期函数，其原函数 $F(x)$ 不一定为周期函数

若 $f(x)$ 为可导的周期函数，则 $f'(x)$ 一定为周期函数

### 易错点6

$f(x)$ 在 $[a,b]$ 上有界是函数可积的必要条件，无界函数一定不可积