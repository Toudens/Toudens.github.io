---
title: "Ch-1 级数及其应用"
date: 2026-03-18
type: "docs"
---

### 数项级数的定义
设 $u_1,u_2,\cdots,u_n,\cdots$ 是给定的数列，称 $\begin{aligned}\sum_{n=1}^\infty u_n=u_1+u_2+\cdots+u_n+\cdots\end{aligned}$ 为数项级数，称 $\begin{aligned}S_n=\sum_{i=1}^nu_i\end{aligned}$ 为 $\text{部分和}$，则有 $\begin{aligned}\sum_{n=1}^\infty u_n=\lim_{n\rightarrow\infty}S_n\end{aligned}$

### 几何级数的敛散性
几何级数 $\begin{aligned}a+aq+aq^2+\cdots+aq^{n-1}+\cdots=\sum_{n=1}^{\infty}aq^{n-1}\quad(a\neq0)\end{aligned}$ 的敛散性满足：
* 当 $|q|<1$ 时，几何级数收敛，且 $\begin{aligned}\sum_{n=1}^{\infty}aq^{n-1}=\frac{a}{1-q}\end{aligned}$
* 当 $|q|\geq1$ 时，几何级数发散，即 $\begin{aligned}\sum_{n=1}^{\infty}aq^{n-1}\text{DNE}\end{aligned}$

### p 级数的敛散性
$p$ 级数 $\begin{aligned}1+\frac{1}{2^p}+\frac{1}{3^p}+\cdots+\frac{1}{n^p}+\cdots=\sum_{n=1}^{\infty}\frac{1}{n^p}\end{aligned}$ 的敛散性满足：
* 当 $p>1$ 时，级数 $\begin{aligned}\sum_{n=1}^{\infty}\frac{1}{n^p}\end{aligned}$ $\text{收敛}$
* 当 $p\leq1$ 时，级数 $\begin{aligned}\sum_{n=1}^{\infty}\frac{1}{n^p}\end{aligned}$ $\text{发散}$

### 数项级数的基本性质
**性质1** 若级数 $\begin{aligned}\sum_{n=1}^{\infty}u_n,\sum_{n=1}^{\infty}v_n\end{aligned}$ 均收敛，且 $\begin{aligned}\sum_{n=1}^{\infty}u_n=A,\sum_{n=1}^{\infty}v_n=B\end{aligned}$ ，则对任何常数 $\alpha,\beta$ ，$\begin{aligned}\sum_{n=1}^\infty(\alpha u_n+\beta v_n)\end{aligned}$ 收敛，且有 $\begin{aligned}\sum_{n=1}^\infty(\alpha u_n+\beta v_n)=\alpha\sum_{n=1}^\infty u_n+\beta\sum_{n=1}^\infty v_n=\alpha A+\beta B\end{aligned}$

**性质2** 改变级数的有限项，或去掉前面有限项，或在级数前面加有限项，都不影响级数的敛散性

**性质3** 若级数 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 收敛，则在级数中任意添加括号得到的新级数也收敛，且其和不变

**性质4** 若级数 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 收敛，则 $\begin{aligned}\lim_{n\rightarrow\infty}u_n=0\end{aligned}$，逆命题不一定成立

**性质5** 若 $\begin{aligned}\lim_{n\rightarrow\infty}u_n\text{DNE}\end{aligned}$ 或 $\begin{aligned}\lim_{n\rightarrow\infty}u_n=A\neq0\end{aligned}$ 则级数 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 发散

**性质6** 柯西收敛准则：级数 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 收敛的充要条件是 $\forall \varepsilon>0, \exists$ $\text{正整数 } N$ ，当 $n>N$ 时，对一切 $\text{正整数 } p$ ，都有 $|u_{n+1}+u_{n+2}+\cdots+u_{n+p}|<\varepsilon$ 

### 正项级数的收敛性
正项级数 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 收敛的充要条件是：正项级数的 $\text{部分和数列 } \{S_n\} \text{ 有上界}$

### 正项级数的比较判别法
设 $\begin{aligned}\sum_{n=1}^\infty u_n,\sum_{n=1}^\infty v_n\end{aligned}$ 均为正项级数，且 $u_n\leq v_n(n=1,2,3,\cdots)$
* 若 $\begin{aligned}\sum_{n=1}^\infty v_n\end{aligned}$ 收敛，则 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 收敛
* 若 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 发散，则 $\begin{aligned}\sum_{n=1}^\infty v_n\end{aligned}$ 发散
定理条件可弱化为 $u_n\leq Cv_n(C>0,n=k,k+1,\cdots)$

### 比较判别法的极限形式
设 $\begin{aligned}\sum_{n=1}^\infty u_n,\sum_{n=1}^\infty v_n\end{aligned}$ 均为正项级数，且 $\begin{aligned}\lim_{n\rightarrow\infty}\frac{u_n}{v_n}=l\end{aligned}$
* 当 $0<l<+\infty$ 时，两个级数同敛散性
* 当 $l=0$ 时，若 $\begin{aligned}\sum_{n=1}^\infty v_n\end{aligned}$ 收敛，则 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 收敛
* 当 $l=+\infty$ 时，若 $\begin{aligned}\sum_{n=1}^\infty v_n\end{aligned}$ 发散，则 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 发散

### 比值判别法
设 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 是正项级数，并且 $\begin{aligned}\lim_{n\rightarrow\infty}\frac{u_{n+1}}{u_n}=\gamma\quad(\text{或 } +\infty)\end{aligned}$
* 当 $\gamma<1$ 时，级数收敛
* 当 $\gamma>1(\text{或 } \gamma=+\infty)$ 时，级数发散
* 当 $\gamma=1$ 时，本判别法失效
本判别法适合 $u_{n+1}$ 与 $u_n$ 有公因式且 $\begin{aligned}\lim_{n\rightarrow\infty}\frac{u_{n+1}}{u_n}\end{aligned}$ 存在或等于 $\infty$ 的情形

### 根值判别法
设 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 是正项级数，且 $\begin{aligned}\lim_{n\rightarrow\infty}\sqrt[n]{u_n}=\gamma\quad(\text{或 } +\infty)\end{aligned}$ 
* 当 $\gamma<1$ 时，级数收敛
* 当 $\gamma>1(\text{或 } \gamma=+\infty)$ 时，级数发散
* 当 $\gamma=1$ 时，本判别法失效
本判别法适合 $u_n$ 中含有表达式的 $n$ 次方，且 $\begin{aligned}\lim_{n\rightarrow\infty}\sqrt[n]{u_n}\end{aligned}$ 存在或等于 $\infty$ 的情形

### 积分判别法
设 $f(x)$ 在 $[1,+\infty)$ 上是非负且递减的连续函数，记 $u_n=f(n),n=1,2,3,\cdots$ ,则级数 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 与反常积分 $\begin{aligned}\int_1^{+\infty}f(x)\mathrm{d}x\end{aligned}$ 的敛散性相同

### 莱布尼茨定理
若交错级数 $\begin{aligned}\sum_{n=1}^\infty(-1)^{n-1}u_n\end{aligned}$ 满足条件 $u_1\geq u_2\geq u_3\geq\cdots$ 且 $\begin{aligned}\lim_{n\rightarrow\infty}u_n=0\end{aligned}$ 
则 $\begin{aligned}\sum_{n=1}^\infty(-1)^{n-1}u_n\end{aligned}$ 收敛，并且它的和 $S\leq u_1$
若交错级数满足莱布尼茨定理的条件，则以 $S_n$ 作为级数和近似值时，误差 $R_n$ 不超过 $u_{n+1}$ 

### 绝对收敛级数与条件收敛级数
如果 $\begin{aligned}\sum_{n=1}^\infty|u_n|\end{aligned}$ 收敛，则 $\begin{aligned}\sum_{n=1}^\infty u_n \end{aligned}$ 也收敛
设 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 为一般级数，则
* 如果 $\begin{aligned}\sum_{n=1}^\infty|u_n|\end{aligned}$ 收敛，则称 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ $\text{绝对收敛}$
* 如果 $\begin{aligned}\sum_{n=1}^\infty|u_n|\end{aligned}$ 发散，但 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 收敛，则称 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ $\text{条件收敛}$
如果是用比值判别法或根值判别法判定 $\begin{aligned}\sum_{n=1}^\infty|u_n|\end{aligned}$ 发散，则 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 发散

### 绝对值的比值判别法
设 $\begin{aligned}\sum_{n=1}^\infty u_n\end{aligned}$ 为一般级数，若 $\begin{aligned}\lim_{n\rightarrow}|\frac{u_{n+1}}{u_n}|=\gamma\quad(\text{或 } +\infty)\end{aligned}$ 
* 当 $\gamma<1$ 时，级数绝对收敛
* 当 $\gamma>1(\text{或 } \gamma=+\infty)$ 时，级数发散
* 当 $\gamma=1$ 时，本判别方法失效

### 绝对值的根值判别法
设 $\begin{aligned}\sum_{n=1}^\infty u_n \end{aligned}$ 为一般级数，若 $\begin{aligned}\lim_{n\rightarrow\infty}\sqrt[n]{|u_n|}=\gamma\quad(\text{或 } \infty)\end{aligned}$ 
* 当 $\gamma<1$ 时，级数绝对收敛
* 当 $\gamma>1(\text{或 } \gamma=+\infty)$ 时，级数发散
* 当 $\gamma=1$ 时，本判别方法失效

### 函数项级数
设 $\{u_n(x)\}$ 是定义在数集 $E$ 的一个函数列，表达式 $u_1(x)+u_2(x)+\cdots+u_n(x)+\cdots,x\in E$
称为定义在 $E$ 上的函数项级数，记为 $\begin{aligned}\sum_{n=1}^\infty u_n(x)\end{aligned}$
$\begin{aligned}S_n(x)=u_1(x)+u_2(x)+\cdots+u_n(x)=\sum_{k=1}^n u_k(x),x\in E,n=1,2,\cdots\end{aligned}$ 称为部分和函数列
* 若即 $\begin{aligned}\lim_{n\rightarrow\infty}S_n(x_0)\end{aligned}$ 存在，则称函数项级数在点 $x_0$ 收敛，$x_0$ 称为函数项级数的收敛点
* 若 $\begin{aligned}\lim_{n\rightarrow\infty}S_n(x_0)\end{aligned}$ 不存在，则称函数项级数在点 $x_0$ 发散
函数项级数全体收敛点的集合称为函数项级数的收敛域，记为 $D$
函数项级数在 $D$ 上的每一点 $x$，$\begin{aligned}\lim_{n\rightarrow\infty}S_n(x)\end{aligned}$ 存在，记为 $S(x)$ ，称为函数项级数的和函数
称 $R_n(x)=S(x)-S_n(x)=u_{n+1}(x)+u_{n+2}(x)+\cdots$ 为函数项级数的余项 $\begin{aligned}\lim_{n\rightarrow\infty}R_n(x)=0\end{aligned}$

### 幂级数
$\begin{aligned}\sum_{n=0}^\infty a_n(x-x_0)^n\end{aligned}$ 为关于 $x-x_0$ 的幂级数，$\begin{aligned}\sum_{n=0}^\infty a_nx^n\end{aligned}$ 为关于 $x$ 的幂级数

### 阿贝尔定理
* 如果 $\begin{aligned}\sum_{n=0}^\infty a_nx^n\end{aligned}$ 当 $x=x_0(x_0\neq0)$ 时收敛，则 $|x|<|x_0|$ 的一切 $x$ 使该幂级数绝对收敛
* 如果 $\begin{aligned}\sum_{n=0}^\infty a_nx^n\end{aligned}$ 当 $x=x_0$ 时发散，则 $|x|>|x_0|$ 的一切 $x$ 使该幂级数发散
幂级数的收敛域是以原点为中心的区间，若以 $2R$ 表示区间长度，$R$ 为收敛半径

### 柯西-阿达马公式
若幂级数 $\begin{aligned}\sum_{n=0}^\infty a_nx^n\end{aligned}$ ,若 $\begin{aligned}\lim_{n\rightarrow\infty}\frac{|a_n|}{|a_{n+1}|}=R\end{aligned}$ （$\begin{aligned}\lim_{n\rightarrow\infty}\frac{1}{\sqrt[n]{|a_n|}}=R\end{aligned}$）
* 当 $0<R<+\infty$ 时，级数 $\begin{aligned}\sum_{n=0}^\infty a_nx^n\end{aligned}$ 在 $(-R,+R)$ 绝对收敛，$|x|>R$ 发散
* 当 $R=0$ 时，级数 $\begin{aligned}\sum_{n=0}^\infty a_nx^n\end{aligned}$ 仅在 $x=0$ 处收敛，$x\neq0$ 时发散
* 当 $R=+\infty$ 时，级数 $\begin{aligned}\sum_{n=0}^\infty a_nx^n\end{aligned}$ 在 $(-\infty,+\infty)$ 内绝对收敛
在 $x=\pm R$ 时，幂级数可能发散也可能收敛，需要具体验证

### 幂级数的性质
若幂级数 $\begin{aligned}\sum_{n=0}^\infty a_nx^n\end{aligned}$ 的收敛半径为 $R(>0)$ ，则有：
* 级数在收敛域上的和函数 $S(x)$ 是连续函数，$S(x)$ 在 $(-R,R)$ 内也连续
* 幂级数在 $(-R,R)$ 内逐项可微，微分后所得到的幂级数与原级数有相同的收敛半径
* 幂级数在 $(-R,R)$ 内逐项可积，积分后所得到的幂级数与原级数有相同的收敛半径

即设 $S(x)=a_0+a_1x+a_2x^2+\cdots+a_nx^n+\cdots,|x|<R$ ，则
* $S(x)$ 在 $|x|<R$ 上连续
* $\begin{aligned}S'(x)&=\frac{\mathrm{d}}{\mathrm{d}x}(a_0+a_1x+a_2x^2+\cdots+a_nx^n+\cdots)\\&=a_1+2a_2x+\cdots+na_nx^{n-1}+\cdots,\quad|x|<R\end{aligned}$
* $\begin{aligned}\int_0^xS(t)\mathrm{d}t&=\int_0^x(a_0+a_1t+\cdots+a_nt^n+\cdots)\mathrm{d}t\\&=a_0x+\frac{a_1}{2}x^2+\cdots+\frac{a_n}{n+1}x^{n+1}+\cdots,\quad|x|<R\end{aligned}$

设 $S(x)$ 为幂级数在收敛区间 $(-R,R)$ 内的和函数，则在 $(-R,R)$ 内 $S(x)$ 具有 $\text{任何阶导数且可逐项求导，收敛半径仍为 } R$

**唯一性定理**：设 $S(x)$ 为幂级数在某邻域内的和函数，则幂级数的系数在 $x=0$ 处的各阶导数具有关系：$\begin{aligned}a_0=S(0),\quad a_n=\frac{S^{(n)}(0)}{n!},\quad n=1,2,\cdots\end{aligned}$
 
* 若幂级数 $\begin{aligned}\sum_{n=0}^\infty a_nx^n\end{aligned}$ 在收敛区间的端点 $x=R$ 处收敛，则 $S(x)=\begin{aligned}\sum_{n=0}^\infty a_nx^n\end{aligned}$ 在 $x=R$ 处左连续，即 $\begin{aligned}\lim_{x\rightarrow R^-}\sum_{n=0}^\infty a_nx^n\end{aligned}=\begin{aligned}\sum_{n=0}^\infty a_nR^n\end{aligned}$ 或 $\begin{aligned}\lim_{x\rightarrow R^-}S(x)=S(R)\end{aligned}$
* 若幂级数 $\begin{aligned}\sum_{n=0}^\infty a_nx^n\end{aligned}$ 在收敛区间的端点 $x=-R$ 处收敛，则 $S(x)=\begin{aligned}\sum_{n=0}^\infty a_nx^n\end{aligned}$ 在 $x=-R$ 处右连续，即 $\begin{aligned}\lim_{x\rightarrow -R^+}\sum_{n=0}^\infty a_nx^n\end{aligned}=\begin{aligned}\sum_{n=0}^\infty a_n(-R)^n\end{aligned}$ 或 $\begin{aligned}\lim_{x\rightarrow -R^+}S(x)=S(-R)\end{aligned}$

### 幂级数的运算
若级数 $\begin{aligned}\sum_{n=0}^\infty a_nx^n\end{aligned}$ 与 $\begin{aligned}\sum_{n=0}^\infty b_nx^n\end{aligned}$ 在 $x=0$ 的某邻域相等，则它们的同次幂项的系数相等
设 $\begin{aligned}\sum_{n=0}^\infty a_nx^n\end{aligned}$ 和 $\begin{aligned}\sum_{n=0}^\infty b_nx^n\end{aligned}$ 的收敛半径分别为 $R_a$ 和 $R_b$ ，则有
* $\begin{aligned}\lambda\sum_{n=0}^\infty a_nx^n=\sum_{n=0}^\infty \lambda a_nx^n,\quad|x|<R_a\end{aligned}$
* $\begin{aligned}\sum_{n=0}^\infty a_nx^n\pm\sum_{n=0}^\infty b_nx^n=\sum_{n=0}^\infty (a_n\pm b_n)x^n,\quad|x|<R\end{aligned}$
* $\begin{aligned}(\sum_{n=0}^\infty a_nx^n)(\sum_{n=0}^\infty b_nx^n)=\sum_{n=0}^\infty c_nx^n,\quad|x|<R\end{aligned}$
* $\begin{aligned}\frac{\sum_{n=0}^\infty a_nx^n}{\sum_{n=0}^\infty b_nx^n}=\sum_{n=0}^\infty c_nx^n\Rightarrow(\sum_{n=0}^\infty b_nx^n)(\sum_{n=0}^\infty c_nx^n)=\sum_{n=0}^\infty a_nx^n\end{aligned}$
其中 $\lambda$ 为常数，$\begin{aligned}R=\min\{R_a,R_b\},\quad c_n=\sum_{k=0}^na_kb_{n-k}\end{aligned}$

### 求幂级数的和函数常用方法
* 利用幂级数的线性运算法则
* 利用变量代换
* 通过逐项求导，再利用 $\begin{aligned}S(x)=S(0)+\int_0^xS'(t)\mathrm{d}t\end{aligned}$
* 通过逐项积分，再利用 $S(x)=\begin{pmatrix}\begin{aligned}\int_0^xS(t)\mathrm{d}t\end{aligned}\end{pmatrix}'$ 

### 函数展成幂级数
当 $f(x)$ 在区间 $|x-x_0|<R$ 内存在任意阶的导数，幂级数 $\begin{aligned}\sum_{n=0}^\infty\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n\end{aligned}$ 的收敛条件为 $|x-x_0|<R$ ，则在 $|x-x_0|<R$ 内 $f(x)=\begin{aligned}\sum_{n=0}^\infty\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n\end{aligned}$ 成立的充要条件是：在该区间内 $\begin{aligned}\lim_{n\rightarrow\infty}R_n(x)=\lim_{n\rightarrow\infty}\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}=0\end{aligned}$
$\begin{aligned}f(0)+\frac{f'(0)}{1!}x+\frac{f''(0)}{2!}x^2+\cdots+\frac{f^{(n)}(0)}{n!}x^n+\cdots=\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^n\end{aligned}$ 称为 $f(x)$ 的麦克劳林级数
* $\begin{aligned}\frac{1}{1-x}=\sum_{n=0}^\infty x^n,\quad|x|<1\end{aligned}$
* $\begin{aligned}\frac{1}{1+x}=\sum_{n=0}^\infty(-1)^nx^n,\quad|x|<1\end{aligned}$
* $f^{(n)}(x_0)=n!a_n,\quad n=0,1,2,\cdots$ 

### 欧拉公式
当 $x$ 为实数时，有 $\begin{aligned}e^x=\sum_{n=0}^\infty\frac{x^n}{n!}\end{aligned}$ ,推广到虚数，有
$\begin{aligned}e^{\text{i}x}&=\sum_{n=0}^\infty\frac{(\text{i}x)^n}{n!}=1+\text{i}x+\frac{(\text{i}x)^2}{2!}+\frac{(\text{i}x)^3}{3!}+\frac{(\text{i}x)^4}{4!}+\cdots\\&=(1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots)+\text{i}(x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots)\end{aligned}$
* $e^{\text{i}x}=\cos x+\text{i}\sin x$
* $e^{-\text{i}x}=\cos x-\text{i}\sin x$
* $\begin{aligned}\sin x=\frac{1}{2\text{i}}(e^{\text{i}x}-e^{-\text{i}x})\end{aligned}$
* $\begin{aligned}\cos x=\frac{1}{2}(e^{\text{i}x}+e^{-\text{i}x})\end{aligned}$

### 函数的傅里叶展开
周期 $T=2l$ 的函数 $f(x)$ 可以表示成 $\begin{aligned}\frac{a_0}{2}+\sum_{n=1}^\infty(a_n\cos\frac{n\pi x}{l}+b_n\sin\frac{n\pi x}{l})\end{aligned}$
在标准区间 $[-l,l]$ 上的三角解函数系：
    $\begin{aligned}1,\quad\cos\frac{\pi x}{l},\quad\sin\frac{\pi x}{l},\quad\cos\frac{2\pi x}{l},\quad\sin\frac{2\pi x}{l},\quad\cdots,\quad\cos\frac{n\pi x}{l},\quad\sin\frac{n\pi x}{l},\quad\dots\end{aligned}$
$\begin{cases}\begin{aligned}a_n=\frac{1}{l}\int_{-l}^lf(x)\cos\frac{n\pi x}{l}\mathrm{d}x\end{aligned},\quad n=0,1,2,\cdots\\\begin{aligned}b_n=\frac{1}{l}\int_{-l}^lf(x)\sin\frac{n\pi x}{l}\mathrm{d}x\end{aligned},\quad n=1,2,3,\cdots\end{cases}$
当 $f(x)$ 为奇函数，则 $a_n=0$ , 称为 $\text{傅里叶正弦级数}$
当 $f(x)$ 为偶函数，则 $b_n=0$ ，称为 $\text{傅里叶余弦级数}$

### 狄利克雷定理
如果 $f(x)$ 是以 $T=2l$ 为周期的周期函数，且 $f(x)$ 在 $[-l,l]$ 上逐段光滑，那么 $f(x)$ 的傅里叶级数在任意点 $x$ 处都收敛，并且收敛于 $f(x)$ 在该点左右极限的平均值，即
$\begin{aligned}\frac{a_0}{2}+\sum_{n=1}^\infty(a_n\cos\frac{n\pi x}{l}+b_n\sin\frac{n\pi x}{l})&=S(x)\\&=\frac{f(x-0)+f(x+0)}{2},x\in(-\infty,+\infty)\end{aligned}$ 

$\begin{aligned}S(x)=\begin{cases}f(x)&\text{当 } x \text{ 是 } f(x) \text{ 的连续点时};\\\begin{aligned}\frac{f(x-0)+f(x+0)}{2}\end{aligned}&\text{当 } x \text{ 是 } f(x) \text{ 的第一类间断点时};\\\begin{aligned}\frac{f(-l+0)+f(l-0)}{2}\end{aligned}&\text{当 } x=\pm l\end{cases}\end{aligned}$

### 对函数延拓
* 奇延拓 $F(x)=\begin{cases}f(x),&x\in(0,l]\\0,&x=0\\-f(-x),&x\in[-l,0)\end{cases}$
* 偶延拓 $F(x)=\begin{cases}f(x),&x\in[0,l]\\f(-x),&x\in[-l,0)\end{cases}$
