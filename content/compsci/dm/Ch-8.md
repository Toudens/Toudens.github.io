---
title: Ch-8 Counting II
date: 2026-03-19
type: docs
weight: "8"
---
### Word Table
| 术语                  | 翻译    | 术语             | 翻译  | 术语      | 翻译  |
| ------------------- | ----- | -------------- | --- | ------- | --- |
| recurrence relation | 递推关系  | parenthese     | 括号  | degreee | 阶   |
| divide-and-conquer  | 分治    | master theorem | 主定理 | linear  | 线性  |
| binomial theorem    | 二项式定理 | homogeneous    | 齐次  |         |     |
### Catalan Numbers

 Note That the initial conditions are $C_0=1$ and $C_1=1$
$$
\begin{align} 
C_n&=C_0C_{n-1}+C_1C_{n-2}+\cdots+C_{n-2}C_1+C_{n-1}C_0\\
&=\sum_{k=0}^{n-1}C_kC_{n-k-1}\\
&=\frac{C(2n,n)}{n+1} 
\end{align}
$$
### LRR

Linear homogeneous recurrence relation with constant coefficients refers to a recurrence relation of the form
$$ a_n=c_1a_{n-1}+c_2a_{n-2}+\cdots+c_ka_{n-k}$$
where $c_1,c_2,\cdots,c_k$ are real numbers, and $c_k\neq0$

Suppose that the characteristic equation $r^k-c_1r^{k-1}-\cdots-c_k=0$has $k$ distinct roots $r_1,r_2,\cdots,r_k$ Then a sequence $\{a_n\}$ is a solution of the recurrence relation
$$
a_n=c_1a_{n-1}+c_2a_{n-2}+\cdots+c_ka_{n-k}
$$
if and only if $a_n=\alpha_1r_1^n+\alpha_2r_2^n+\cdots+\alpha_kr_k^n$
if the characteristic equation has t distinct roots $r_1,r_2,\cdots,r_t$
$$
\begin{align}
a_n
=&(\alpha_{1,0}+\alpha_{1,1}n+\cdots+\alpha_{1,m_1-1}n^{m_1-1})r_1^n\\
+&(\alpha_{2,0}+\alpha_{2,1}n+\cdots+\alpha_{2,m_2-1}n^{m_2-1})r_2^n\\
+&\quad\cdots\\
+&(\alpha_{t,0}+\alpha_{t,1}n+\cdots+\alpha_{t,m_t-1}n^{m_t}-1)r_t^n
\end{align}
$$
### LNRR with Constant Coefficients

If  $\{a_n^{(p)}\}$ is a particular solution of the nonhomogeneous linear recurrence relation (LNRR) with constant coefficients
$$
a_n=c_1a_{n-1}+c_2a_{n-2}+\cdots+c_ka_{n-k}+F(n)
$$
then every solution is of the form $\{a_n^{(p)}+a_n^{(h)}\}$ where $\{a_n^{(h)}\}$ is a solution of the associated homogeneous recurrence relation 

Suppose that $F(n)=(b_tn^t+b_{t-1}n^{t-1}+\cdots+b_1n+b_0)s^n$ , the multiplicity of $s$ in the characteristic equation is $m$ ,there is a particular solution of the form
$$
n^m(p_tn^t+p_{t-1}n^{t-1}+\cdots+p_1n+p_0)s^n
$$
### Divide-and-Conquer

Let $f$ be an increasing function that satisfies the recurrence relation
$$
f(n)=af(n/b)+c
$$
whenever $n$ is divisible by $b$ , where $a\geq1$ , $b\in Z^+,b>1,c\in R^+$
$$
f(n)\text{is}
\begin{cases}
O(n^{\log_ba}),&a>1\\
O(\log n),&a=1
\end{cases}
$$
when $n=b^k$ and $a\neq1$ when $k$ is a positive integer,
$$
f(n)=C_1n^{\log_ba}+C_2,C_1=f(1)+c/(a-1),C_2=-c/(a-1)
$$
### Master Theorem

Let $f$ be an increasing function that satisfies the recurrence relation
$$
f(n)=af(n/b)+cn^d
$$
whenever $n=b^k$ ,where $k\in Z^+,a\geq1,b>1,b\in Z,c\in R^+,d\in R,d\geq0$
$$
f(n)\text{is}
\begin{cases}
O(n^d)&a<b^d\\
O(n^d\log n)&a=b^d\\
O(n^{\log_ba})&a>b^d
\end{cases}
$$
### Generating Functions

The generating function for the sequence $a_0,a_1,\cdots,a_k,\cdots$ of real numbers is the infinite series
$$
G(x)=a_0+a_1x+\cdots+a_kx^k+\cdots=\sum_{k=0}^\infty a_kx^k
$$
### Extended Binomial Theorem

Let $x$ be a real number with $|x|<1$ and let $u$ be a real number, then
$$
(1+x)^u=\sum_{k=0}^\infty\begin{pmatrix}u\\k\end{pmatrix}x^k
$$
### Useful GFunctions

|                 Sequence $a_k$                 |          Generating Function $G(x)$          |
| :--------------------------------------------: | :------------------------------------------: |
|                    $C(n,k)$                    |                  $(1+x)^n$                   |
|                  $C(n,k)a^k$                   |                  $(1+ax)^n$                  |
|                    $[k<n]$                     | $\begin{align}\frac{1-x^n}{1-x}\end{align}$  |
|                      $1$                       |   $\begin{align}\frac{1}{1-x}\end{align}$    |
|                     $a^k$                      |   $\begin{align}\frac{1}{1-ax}\end{align}$   |
|                     $k+1$                      | $\begin{align}\frac{1}{(1-x)^2}\end{align}$  |
|                  $C(n+k-1,k)$                  | $\begin{align}\frac{1}{(1-x)^n}\end{align}$  |
|               $(-1)^kC(n+k-1,k)$               | $\begin{align}\frac{1}{(1+x)^n}\end{align}$  |
|                $C(n+k-1,k)a^k$                 | $\begin{align}\frac{1}{(1-ax)^n}\end{align}$ |
|     $\begin{align}\frac{1}{k!}\end{align}$     |                    $e^x$                     |
| $\begin{align}\frac{(-1)^{k+1}}{k}\end{align}$ |                  $\ln(1+x)$                  |
### Inclusion-Exclusion

Let $A_1,A_2,\cdots A_n$ be finite sets, then
$$
\begin{align}
|A_1\cup A_2\cup\cdots\cup A_n|
&=\sum_{1\leq i\leq n}|A_i|
-\sum_{1\leq i< j\leq n}|A_i\cap A_j|\\
&+\sum_{1\leq i<j<k\leq n}|A_i\cap A_j\cap A_k|-\cdots+(-1)^{n+1}|A_1\cap A_2\cap\cdots\cap A_n|
\end{align}
$$
### Derangement

Counting the permutations of $n$ objects that leave no objects in their original positions, the number of derangements of a set with $n$ elements is :
$$
\begin{align}
D_n&=n!(1-\frac{1}{1!}+\frac{1}{2!}-\frac{1}{3!}+\cdots+(-1)^n\frac{1}{n!})\\
&=(n-1)(D_{n-1}+D_{n-2})
\end{align}
$$