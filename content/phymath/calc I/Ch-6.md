---
title: Ch-6 定积分
date: 2026-03-19
type: docs
weight: "6"
---
### 定积分中值定理

若 $f(x)$ 在 $[a,b]$ 上可积，则 $\exists\xi\in(a,b)$ ，使得 $\begin{aligned}\int_a^bf(x)\mathrm{d}x=f(\xi)(b-a)\end{aligned}$

### 推广的定积分中值定理

若 $f(x),g(x)$ 在 $[a,b]$ 上连续，且 $g(x)$ 在 $[a,b]$ 上不变号，则 $\exists\xi\in(a,b)$，使得

$\begin{aligned}\int_a^bf(x)g(x)\mathrm{d}x=f(\xi)\int_a^bg(x)\mathrm{d}x\end{aligned}$

### 柯西不等式

$\begin{pmatrix}\begin{aligned}\int_a^bf(x)g(x)\mathrm{d}x\end{aligned}\end{pmatrix}^2\leq\begin{aligned}\int_a^bf^2(x)\mathrm{d}x\cdot\int_a^bg^2(x)\mathrm{d}x\end{aligned}$

### 重要结果及技巧

$\begin{aligned}\int\csc{x}\mathrm{d}x=\int\frac{\csc{x}(\csc{x}-\cot{x})}{\csc{x}-\cot{x}}\mathrm{d}x=\int\frac{\mathrm{d}(\csc{x}-\cot{x})}{\csc{x}-\cot{x}}=\ln|\csc{x}-\cot{x}|\end{aligned}$

$\begin{aligned}\int\sec{x}\mathrm{d}x=\int\frac{\sec{x}(\sec{x}+\tan{x})}{\sec{x}+\tan{x}}\mathrm{d}x=\int\frac{\mathrm{d}(\sec x+\tan x)}{\sec x+\tan x}=\ln|\sec x+\tan x|\end{aligned}$

$\begin{aligned}\int\cos^nx\mathrm{d}x=\frac{1}{n}\sin x\cos^{n-1}x+\frac{n-1}{n}\int\cos^{n-2}x\mathrm{d}x\end{aligned}$

$\begin{aligned}\int\sin^nx\mathrm{d}x=-\frac{1}{n}\cos x\sin^{n-1}x+\frac{n-1}{n}\int\sin^{n-2}x\mathrm{d}x\end{aligned}$

$\begin{aligned}I_n=\int\frac{\mathrm{d}x}{(a^2+x^2)^n},I_n=\frac{x}{2(n-1)a^2(a^2+x^2)^{n-1}}+\frac{2n-3}{2(n-1)a^2}I_{n-1}\end{aligned}$

$\mathrm{d}(\sin x+\cos x)=\cos x-\sin x,\mathrm{d}(\sin x-\cos x)=\sin x+\cos x$

$\begin{aligned}\int_0^{\frac{\pi}{2}}\sin^nx\mathrm{d}x=\int_0^{\frac{\pi}{2}}\cos^nx\mathrm{d}x\end{aligned}=\begin{cases}\dfrac{n-1}{n}\cdot\dfrac{n-3}{n-2}\cdot\cdots\cdot\dfrac{2}{3}\cdot1,&n为奇数\\\dfrac{n-1}{n}\cdot\dfrac{n-3}{n-2}\cdot\cdots\cdot\dfrac{3}{4}\cdot\dfrac{1}{2}\cdot\dfrac{\pi}{2},&n为偶数\end{cases}$

$\begin{aligned}\Gamma(s+1)&=\int_0^{+\infty}x^{s}e^{-x}\mathrm{d}x=-x^se^{-x}\big|_0^{+\infty}+s\int_0^{+\infty}x^{s-1}e^{-x}\mathrm{d}x\\&=s\Gamma(s)=\cdots=n!\Gamma(1)=n!\end{aligned}$

对于一切 $a>0$ ，极限 $\begin{aligned}\lim_{x\rightarrow0^+}x^a\ln x=0\end{aligned}$ 成立

$\begin{aligned}\lim_{x\rightarrow0^+}x^a\ln x=\lim_{x\rightarrow0^+}\dfrac{\ln x}{x^{-a}}=-\frac{1}{a}\lim_{x\rightarrow0^+}\frac{x^{-1}}{x^{-a-1}}=-\frac{1}{a}\lim_{x\rightarrow0^+}x^a=0\end{aligned}$

在区间对称的积分中分离出奇函数的部分

### 中值定理构造原函数

将结果中的未知参数换为 $x$

如果结果中既有 $f(x)$ 又含有 $f'(x)$ ，则将等式变换为 $\dfrac{f'(x)}{f(x)}+h(x)=0$ 的形式

假使 $p'(x)=h(x)$ ，则构造 $g(x)=f(x)e^{p(x)}$

### 积分上限函数

$\begin{bmatrix}\begin{aligned}\int_a^{g(x)}f(t)\mathrm{d}t\end{aligned}\end{bmatrix}'=f[g(x)]g'(x)$

$\begin{bmatrix}\begin{aligned}\int_{h(x)}^{g(x)}f(t)\mathrm{d}t\end{aligned}\end{bmatrix}'=f[g(x)]g'(x)-f[h(x)]h'(x)$
