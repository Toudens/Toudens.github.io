---
title: Ch-1 数列极限
date: 2026-03-18
type: docs
weight: "1"
---
### 数列极限定义

设 $\{a_n\}$ 是 $\mathrm{R}$ 中的一个数列，如果存在 $a\in\mathrm{R}$ 使得 $\forall \varepsilon>0,\exists N\in\mathrm{N_+}$ ，当 $n\geq N$ 时，都有 $|a_n-a|<\varepsilon$ ，就称数列 $\{a_n\}$ 是收敛于 $a$ 的，记为 $\begin{aligned}\lim_{n\rightarrow\infty}a_n=a\end{aligned}$ ,称 $a$ 是数列 $\{a_n\}$ 的极限

### 数列极限性质

**唯一性**  如果数列 $\{a_n\}$ 收敛，那么其极限是唯一的

**有界性**  如果数列 $\{a_n\}$ 收敛，那么 $\{a_n\}$ 是有界的，即 $\exists M>0,\forall n\in\mathrm{N_+},|a_n|\leq M$

**保号性**  如果 $\begin{aligned}\lim_{n\rightarrow\infty}a_n=a>0\end{aligned}$ 那么 $\forall p\in(0,a),\exists N>0$ 当 $n\geq N$ 时 $a_n>p>0$

### 夹逼定理

设数列 $\{a_n\},\{b_n\},\{c_n\}$ 满足当 $n\geq N_0\in\mathrm{N}_+$ 时，有 $b_n\leq a_n\leq c_n$ 并且 $\begin{aligned}\lim_{n\rightarrow\infty}b_n=\lim_{n\rightarrow\infty}c_n=a\end{aligned}$ ，则数列 $\{a_n\}$ 也是收敛的，且 $\begin{aligned}\lim_{n\rightarrow\infty}a_n=a\end{aligned}$

### 波尔查诺-魏尔斯特拉斯定理

设 $\{a_n\}$ 是 $\mathrm{R}$ 中的一个有界数列，则数列 $\{a_n\}$ 中存在收敛的子列

### 柯西准则

设 $a_n$ 是 $\mathrm{R}$ 中的一个数列，若对于任意 $\varepsilon>0$ ，存在正整数 $N$ ，当 $m,n\geq N$ 时， $|a_m-a_n|<\varepsilon$ 则称 $\{a_n\}$ 是柯西数列，$\{a_n\}$ 收敛当且仅当 $\{a_n\}$ 是柯西数列

### 施托尔茨第一公式

给定数列 $\{x_n\},\{y_n\}$ ，若 $\{x_n\}$ 单调增加，且 $\begin{aligned}\lim_{x\rightarrow+\infty}x_n=+\infty\end{aligned}$ ,

若 $\begin{aligned}\lim_{n\rightarrow+\infty}\frac{y_n-y_{n-1}}{x_n-x_{n-1}}=a\end{aligned}$ ，那么有 $\begin{aligned}\lim_{n\rightarrow+\infty}\frac{y_n}{x_n}=a\end{aligned}$ ，其中 $a$ 可以是实数也可以是 $\pm\infty$

### 施托尔茨第二公式

给定数列 $\{x_n\},\{y_n\}$ ，若$\{x_n\}$ 单调减少，且 $\begin{aligned}\lim_{n\rightarrow+\infty}x_n=\lim_{n\rightarrow+\infty}y_n=0\end{aligned}$ ，

若$\begin{aligned}\lim_{n\rightarrow+\infty}\frac{y_n-y_{n-1}}{x_n-x_{n-1}}=a\end{aligned}$ ，那么有 $\begin{aligned}\lim_{n\rightarrow+\infty}\frac{y_n}{x_n}=a\end{aligned}$ ，其中 $a$ 可以是实数也可以是 $\pm\infty$