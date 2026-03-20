---
title: 常微分方程
date: 2026-03-19
type: docs
---
### 一、基础概念

#### 1.1 常用术语
| 术语                   | 翻译   | 术语             | 翻译   | 术语          | 翻译  |
| -------------------- | ---- | -------------- | ---- | ----------- | --- |
| homogeneous          | 齐次   | constant       | 常数   | derivative  | 导数  |
| superposition        | 叠加   | multiplication | 乘法   | substitute  | 代换  |
| partial derivative   | 偏导数  | arbitrary      | 任意   | reducible   | 可化简 |
| autonomous           | 自治   | algebra        | 代数   | interval    | 区间  |
| infinite family      | 无穷集  | proportional   | 比例   | explicit    | 特解  |
| assertion            | 断言   | intersect      | 相交   | parameter   | 参数  |
| antiderivative       | 不定积分 | branch         | 分支   | domain      | 范围  |
| independent variable | 自变量  | verify         | 验证   | coefficient | 系数  |
| identity equation    | 恒等式  | curve          | 曲线   | equation    | 方程  |
| dependent variable   | 因变量  | integration    | 积分   | slope       | 斜率  |
| necessary condition  | 必要条件 | exponential    | 指数的  | static      | 静态  |
| asymptote            | 渐近线  | denote         | 表示   | indeed      | 的确  |
| hypothesis           | 假设   | error function | 误差方程 | encompass   | 包含  |
| equilibrium          | 平衡   | vibration      | 振动   | duplication | 重复  |

#### 1.2 n 阶方程形式
The most general form of an nth-order differential equation with independent $x$ and unknown function or dependent variable $y=y(x)$ is $F(x,y,y',y'',\cdots,y^{(n)})=0$.
An nth-order differential equation ordinarily has an n-parameter family of solutions—one involving n different arbitrary constants or parameters.

#### 1.3 积分求解
The first-order equation $\begin{aligned}\frac{\mathrm{d}y}{\mathrm{d}x}=f(x,y)\end{aligned}$ takes an especially simple form if the function $f$ is independent of the dependent variable $y$, i.e., $\begin{aligned}\frac{\mathrm{d}y}{\mathrm{d}x}=f(x)\end{aligned}$. In this special case, we only need to integrate both sides: 
$$\begin{aligned}y(x)=\int f(x)\mathrm{d}x+C\end{aligned}$$

#### 1.4 解的存在唯一性
Suppose that both the function $f(x,y)$ and its partial derivative $D_yf(x,y)$ are continuous on some rectangle $R$ in the xy-plane that contains the point $(a,b)$ in its interior.
Then, for some open interval $I$ containing the point $a$, the initial value problem $\begin{aligned}\frac{\mathrm{d}y}{\mathrm{d}x}=f(x,y),\quad y(a)=b\end{aligned}$ has **one and only one** solution that is defined on the interval $I$.

If the function $f(x,y)$ and/or its partial derivative $\begin{aligned}\frac{\partial f}{\partial y}\end{aligned}$ fail to satisfy the continuity hypothesis, then the initial value problem may have either no solution or many (even infinitely many) solutions.

#### 1.5 皮卡迭代法
To prove the existence and uniqueness theorem rigorously, the typical Picard iteration method follows these steps:
1. Re-write the ODE as an integral equation.
2. Construct the Picard iterates.
3. Show that the Picard iterates converge uniformly on $|x-x_0|\leq h$.
4. Show that the above limit function is a solution.
5. Show that the solution is unique. 

---
### 二、一阶方程解法

#### 2.1 分离变量法
The first-order differential equation $\begin{aligned}\frac{\mathrm{d}y}{\mathrm{d}x}=H(x,y)\end{aligned}$ is called separable provided that $H(x,y)$ can be written as the product of a function of $x$ and a function of $y$: $\begin{aligned}\frac{\mathrm{d}y}{\mathrm{d}x}=g(x)h(y)=\frac{g(x)}{f(y)}\end{aligned}$.
Solution method:
$$\begin{aligned}\int f(y)\mathrm{d}y=\int g(x)\mathrm{d}x+C,\quad F(y)=\int f(y)\mathrm{d}y,\quad G(x)=\int g(x)\mathrm{d}x\end{aligned}$$

#### 2.2 一阶线性方程
**Standard form:**
$$\begin{aligned}\frac{\mathrm{d}y}{\mathrm{d}x}+P(x)y=Q(x)\end{aligned},\quad \rho(x)=\mathrm{e}^{\int P(x)\mathrm{d}x}$$
**Solution steps:**
1. Begin by calculating the integrating factor $\rho(x)=e^{\int P(x)\mathrm{d}x}$.
2. Multiply both sides of the differential equation by $\rho(x)$.
3. Recognize the left-hand side of the resulting equation as the derivative of a product: $D_x[\rho(x)y(x)]=\rho(x)Q(x)$.
4. Integrate this equation to get the solution:
$$\begin{aligned}\rho(x)y(x)=\int\rho(x)Q(x)\mathrm{d}x+C \implies y(x)=\mathrm{e}^{-\int P(x)\mathrm{d}x}\left[\int(Q(x)\mathrm{e}^{\int P(x)\mathrm{d}x})\mathrm{d}x+C\right]\end{aligned}$$

**Properties:**
* Guarantee only a solution on a possibly smaller interval.
* Linear first-order differential equation has **no singular solutions**.

#### 2.3 恰当方程
A general solution $y(x)$ of a first-order differential equation is often defined implicitly by an equation of the form $F(x,y)=C$. Differentiate each side with respect to $x$:
$$\begin{aligned}&\frac{\partial F}{\partial x}+\frac{\partial F}{\partial y}\frac{\mathrm{d}y}{\mathrm{d}x}=0 \Rightarrow M(x,y)+N(x,y)\frac{\mathrm{d}y}{\mathrm{d}x}=0 \Rightarrow M(x,y)\mathrm{d}x+N(x,y)\mathrm{d}y=0\end{aligned}$$
If there exists a function $F(x,y)$ such that $\begin{aligned}\frac{\partial F}{\partial x}=M, \quad \frac{\partial F}{\partial y}=N\end{aligned}$, then $M(x,y)\mathrm{d}x+N(x,y)\mathrm{d}y=0$ is called an exact differential equation.

Thus the equation $\begin{aligned}\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}\end{aligned}$ is a **necessary condition** for the differential equation to be exact.

**Solution:**
$$\begin{aligned}F(x,y)=\int M(x,y)\mathrm{d}x+g(y)\end{aligned}$$
$$\begin{aligned}N=\frac{\partial F}{\partial y}=\begin{pmatrix}\begin{aligned}\frac{\partial}{\partial y}\int M(x,y)\mathrm{d}x\end{aligned}\end{pmatrix}+g'(y) \implies g'(y)=N-\frac{\partial}{\partial y}\int M(x,y)\mathrm{d}x\end{aligned}$$
$$\begin{aligned}F(x,y)=\int M(x,y)\mathrm{d}x+\int\begin{pmatrix}\begin{aligned}N(x,y)-\frac{\partial}{\partial y}\int M(x,y)\mathrm{d}x\end{aligned}\end{pmatrix}\mathrm{d}y = C\end{aligned}$$

#### 2.4 积分因子

If $M(x,y)\mathrm{d}x+N(x,y)\mathrm{d}y=0$ is not exact, we can multiply it by an integrating factor $\mu$ to make it exact.
* **If $\mu$ depends only on $x$:**
$$
\begin{aligned}
\frac{\mathrm{d}\mu}{\mu} = \frac{1}{N}\left(\frac{\partial M}{\partial y} - \frac{\partial N}{\partial x}\right)\mathrm{d}x \Rightarrow \mu(x) = \exp\left[\int \frac{1}{N}\left(\frac{\partial M}{\partial y} - \frac{\partial N}{\partial x}\right)\mathrm{d}x\right]
\end{aligned}
$$
* **If $\mu$ depends only on $y$:**
$$
\begin{aligned}
\frac{\mathrm{d}\mu}{\mu} = \frac{1}{M}\left(\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y}\right)\mathrm{d}y \Rightarrow \mu(y) = \exp\left[\int \frac{1}{M}\left(\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y}\right)\mathrm{d}y\right]
\end{aligned}
$$

#### 2.5 变量代换法

**一阶普遍代换:**

Consider $\frac{\mathrm{d}y}{\mathrm{d}x} = f(x,y)$. Introduce a new dependent variable $v = \alpha(x,y)$, so that $y = \beta(x,v)$. 

Substituting $\frac{\mathrm{d}y}{\mathrm{d}x} = \beta_x + \beta_v \frac{\mathrm{d}v}{\mathrm{d}x}$ into the original equation yields a new first‑order 

equation for $v$: $\frac{\mathrm{d}v}{\mathrm{d}x} = g(x,v)$.

**伯努利方程:**

Form: $\frac{\mathrm{d}y}{\mathrm{d}x} + P(x)\,y = Q(x)\,y^{\,n}, \quad n \neq 0,1$.

Solution: Set $v = y^{1-n}$. Multiply the original equation by $(1-n)y^{-n}$ to obtain a linear first‑order equation for $v$:
$$\frac{\mathrm{d}v}{\mathrm{d}x} + (1-n)P(x)\,v = (1-n)Q(x)$$
Solve for $v(x)$, then recover $y = v^{1/(1-n)}$.

**一阶齐次方程:**

Form: $\frac{\mathrm{d}y}{\mathrm{d}x} = F\!\left(\frac{y}{x}\right)$.

Solution: Introduce the substitution $v = \dfrac{y}{x}$, so $y = vx$ and $\frac{\mathrm{d}y}{\mathrm{d}x} = v + x\frac{\mathrm{d}v}{\mathrm{d}x}$.

Substituting gives $x\frac{\mathrm{d}v}{\mathrm{d}x} = F(v) - v$, which is a separable equation in $x$ and $v$.

---
### 三、奇解与p-判别式法

#### 3.1 奇解与包络

It is common for a nonlinear first-order differential equation to have both a general solution involving an arbitrary constant $C$ and one or several particular solutions that cannot be obtained by selecting a value for $C$. These exceptional solutions are frequently called **singular solutions**.

* **Singular Solution:** A solution of a differential equation that is not tangent to any solution in the family of general solutions (wait, actually it *is* tangent to them) and cannot be obtained by choosing specific values for the constants in the general solution.
* **Envelope:** A curve that is tangent at each point to some solution in the family of general solutions. A singular solution is typically the envelope of the general solution family.

If there is a singular solution, at each point on the curve the ODE has more than 1 solution (uniqueness fails).

#### 3.2 p-判别式原理
Consider a first-order ODE in implicit form:
$$\begin{aligned}F(x,y,p)=0,\quad p=\frac{\mathrm{d}y}{\mathrm{d}x}\end{aligned}$$
A singular solution must satisfy two conditions simultaneously:
* The original equation: $F(x,y,p)=0$
* The partial derivative of $F$ with respect to $p$: $\begin{aligned}\frac{\partial F}{\partial p}=0\end{aligned}$
By eliminating $p$ from these equations, we obtain the p-discriminant curve, which may represent the singular solution.

#### 3.3 判别式法证明
Assume the family of general solutions is $\varphi(x,y,C)=0$ where $C$ is a constant. The envelope must satisfy: $\varphi(x,y,C)=0$ and $\begin{aligned}\frac{\partial\varphi}{\partial C}=0\end{aligned}$. Eliminating $C$ gives the envelope's equation.
For the differential equation $F(x,y,p)=0$, the envelope (singular solution) of its general solution family must satisfy:

1. Every point $(x,y)$ on the envelope satisfies $F(x,y,p)=0$ (since it is a solution).
2. The slope $p$ of the envelope at that point matches the slope of the corresponding solution in the general family.
3. The envelope represents a limiting case where distinct solutions "coalesce", implying the dependence on $p$ in relation to $C$ vanishes, leading to $\begin{aligned}\frac{\partial F}{\partial p}=0\end{aligned}$.

---

### 四、高阶线性方程

#### 4.1 二阶方程降阶
Consider $F(x,y,y',y'')=0$. Two common cases allow reduction to a first‑order problem:
1. **Dependent variable $y$ missing ($F(x,y',y'')=0$):**  
   Set $p = y'$, so $y'' = \frac{\mathrm{d}p}{\mathrm{d}x}$. The equation becomes $F(x,p,p')=0$. Solve for $p(x,C_1)$, then $y(x) = \int p(x,C_1)\,\mathrm{d}x + C_2$.
2. **Independent variable $x$ missing ($F(y,y',y'')=0$):**  
   Set $p = y'$. Use the chain rule: $y'' = \frac{\mathrm{d}p}{\mathrm{d}x} = \frac{\mathrm{d}p}{\mathrm{d}y}\frac{\mathrm{d}y}{\mathrm{d}x} = p\frac{\mathrm{d}p}{\mathrm{d}y}$. The equation reduces to $F\!\left(y,p,p\frac{\mathrm{d}p}{\mathrm{d}y}\right)=0$. Solve for $p(y,C_1)$, then $x(y) = \int \frac{1}{p(y,C_1)}\,\mathrm{d}y + C_2$.

#### 4.2 线性无关与朗斯基
Two functions defined on an open interval $I$ are linearly independent provided neither is a constant multiple of the other. The Wronskian of $n$ functions $f_1, \cdots, f_n$ is:
$$W=\begin{vmatrix}f_1&f_2&\cdots&f_n\\f_1'&f_2'&\cdots&f_n'\\\vdots&\vdots&&\vdots\\f^{(n-1)}_1&f^{(n-1)}_2&\cdots&f^{(n-1)}_n\end{vmatrix}$$ 
For solutions $y_1, y_2, \cdots, y_n$ of a homogeneous nth-order linear ODE:
* If they are linearly dependent, then $W=0$ on $I$.
* If they are linearly independent, then $W\neq0$ at each point of $I$.

#### 4.3 通解结构
Let $y_1, \cdots, y_n$ be $n$ linearly independent solutions of the homogeneous equation $y^{(n)}+p_1(x)y^{(n-1)}+\cdots+p_n(x)y=0$ on $I$. Then the linear combination $y=c_1y_1+\cdots+c_ny_n$ is also a solution, giving the general solution.

#### 4.4 常系数齐次方程
For the differential equation $a_ny^{(n)}+a_{n-1}y^{(n-1)}+\cdots+a_1y'+a_0y=0$, its characteristic equation is $a_nr^n+a_{n-1}r^{n-1}+\cdots+a_1r+a_0=0$.
* **Real and distinct roots:** $y(x)=c_1e^{r_1x}+c_2e^{r_2x}+\cdots+c_ne^{r_nx}$.
* **Repeated roots:** If $r_1$ has multiplicity $k$, the solution includes $(c_1+c_2x+\cdots+c_kx^{k-1})e^{r_1x}$.
* **Complex roots (Euler's Formula):** $e^{(a\pm bi)x}=e^{ax}(\cos{bx}\pm i\sin{bx})$. Complex conjugate roots yield solutions in the form $e^{ax}(d_1\cos{bx}+d_2\sin{bx})$.

**Polynomial Operators:**
$$\begin{aligned}L=a_nD^n+a_{n-1}D^{n-1}+\cdots+a_2D^2+a_1D+a_0\end{aligned}$$

#### 4.5 降阶法
Suppose one solution $y_1(x)$ of $y''+p(x)y'+q(x)y=0$ is known. Substitute $y_2(x)=v(x)y_1(x)$ to find a second linearly independent solution $v(x)$. 
(Also yields the integral formula: $\begin{aligned}y_2=y_1\int\frac{\exp(-\int P(x)dx)}{y_1^2}dx\end{aligned}$)

#### 4.6 非齐次方程通解
If $y_p$ is a particular solution of the nonhomogeneous equation and $y_1,\cdots,y_n$ are linearly independent solutions of the associated homogeneous equation, then the general solution is:
$$Y(x)=c_1y_1(x)+c_2y_2(x)+\cdots+c_ny_n(x)+y_p(x)$$

#### 4.7 待定系数法
Take the trial solution $y_p(x)=x^s[(A_0+\cdots+A_mx^m)e^{rx}\cos{kx}+(B_0+\cdots+B_mx^m)e^{rx}\sin{kx}]$ where $s$ is the smallest nonnegative integer such that no term in $y_p$ duplicates a term in $y_c$.

|            $f(x)$             |                                              $y_p$ 设定形式                                              |
| :---------------------------: | :--------------------------------------------------------------------------------------------------: |
| $P_m=b_0+b_1x+\cdots+b_mx^m$  |                                    $x^s(A_0+A_1x+\cdots+A_mx^m)$                                     |
|     $a\cos{kx}+b\sin{kx}$     |                                      $x^s(A\cos{kx}+B\sin{kx})$                                      |
| $e^{rx}(a\cos{kx}+b\sin{kx})$ |                                   $x^se^{rx}(A\cos{kx}+B\sin{kx})$                                   |
|        $P_m(x)e^{rx}$         |                                 $x^s(A_0+A_1x+\cdots+A_mx^m)e^{rx}$                                  |
| $P_m(x)(a\cos{kx}+b\sin{kx})$ | $\begin{align}&x^s[(A_0+A_1x+\cdots+A_mx^m)\cos{kx}\\&+(B_0+B_1x+\cdots+B_mx^m)\sin{kx}]\end{align}$ |

#### 4.8 参数变易法
For nonhomogeneous equation $y''+P(x)y'+Q(x)y=f(x)$, if $y_c(x)=c_1y_1(x)+c_2y_2(x)$, set $y_p=u_1y_1+u_2y_2$. We solve the system:
$$\begin{cases}u_1'y_1+u_2'y_2=0\\u_1'y_1'+u_2'y_2'=f(x)\end{cases}$$
Which yields:
$$\begin{aligned}y_p(x)=-y_1(x)\int\frac{y_2(x)f(x)}{W(x)}dx+y_2(x)\int\frac{y_1(x)f(x)}{W(x)}dx\end{aligned}$$

---

### 五、级数解法

#### 5.1 幂级数与收敛半径
Given $\sum c_nx^n$, suppose the limit $\begin{aligned}\rho=\lim_{n\rightarrow\infty}\left|\frac{c_n}{c_{n+1}}\right|\end{aligned}$ exists.
* If $\rho=0$, the series diverges for all $x\neq 0$.
* If $0<\rho<\infty$, the series converges if $|x|<\rho$ and diverges if $|x|>\rho$.
* If $\rho=\infty$, the series converges for all $x$.

#### 5.2 常点级数解
For $y''+P(x)y'+Q(x)y=0$, $x=a$ is an **ordinary point** if $P(x)$ and $Q(x)$ are both analytic at $x=a$. It will have two linearly independent power series solutions of the form $\begin{aligned}y(x)=\sum_{n=0}^\infty c_n(x-a)^n\end{aligned}$.

#### 5.3 正则奇点
Rewrite as $y''+\frac{p(x)}{x}y'+\frac{q(x)}{x^2}y=0$. The singular point $x=0$ is a **regular singular point** if $p(x)=xP(x)$ and $q(x)=x^2Q(x)$ are both analytic at $x=0$.
Calculate limits: $p_0=\lim_{x\rightarrow0}xP(x)$ and $q_0=\lim_{x\rightarrow0}x^2Q(x)$.
* If limits are finite, $x=0$ is a regular singular point.
* If either limit fails to exist or is infinite, $x=0$ is an irregular singular point.

#### 5.4 弗罗贝尼乌斯法
If $x=0$ is a regular singular point, assume a Frobenius series solution:
$$\begin{aligned}y(x)=x^r\sum_{n=0}^\infty c_nx^n=\sum_{n=0}^\infty c_nx^{n+r}\quad (c_0\neq0)\end{aligned}$$
Substituting into the ODE yields the **indicial equation**: $r(r-1)+p_0r+q_0=0$. Its two roots $r_1, r_2$ are the exponents.
1. If $r_1-r_2$ is not an integer, there are two Frobenius series solutions.
2. If $r_1=r_2$, there is only one Frobenius series solution.
3. If $r_1-r_2$ is a positive integer, there may or may not exist a second Frobenius series solution.

#### 5.5 对数与非对数情形
Let $r_1 \geq r_2$ and $r_1-r_2=N$. The first solution is always $y_1(x)=x^{r_1}\sum a_nx^n$. The second solution $y_2$ takes the form:
* If $N=0$ ($r_1=r_2$): $\begin{aligned}y_2(x)=y_1(x)\ln{x}+x^{1+r_1}\sum_{n=0}^{\infty}b_nx^n\end{aligned}$
* If $N>0$ (positive integer): $\begin{aligned}y_2(x)=C_Ny_1(x)\ln{x}+x^{r_2}\sum_{n=0}^\infty b_nx^n\end{aligned}$

---

### 六、微分方程组

#### 6.1 高阶转一阶
For $x^{(n)}=f(t,x,x',\cdots,x^{(n-1)})$, introduce variables $x_1=x, x_2=x', \cdots, x_n=x^{(n-1)}$.
The substitution yields the system: $x_1' = x_2, \cdots, x_{n-1}' = x_n, x_n'=f(t,x_1,x_2,\cdots,x_n)$.

#### 6.2 方程组与消元法
Any system of two linear differential equations with constant coefficients $L_1x+L_2y=f_1(t), L_3x+L_4y=f_2(t)$ can be uncoupled by defining the operational determinant $\Delta = L_1L_4-L_2L_3$:
$$\begin{vmatrix}L_1&L_2\\L_3&L_4\end{vmatrix}x=\begin{vmatrix}f_1(t)&L_2\\f_2(t)&L_4\end{vmatrix},\quad\begin{vmatrix}L_1&L_2\\L_3&L_4\end{vmatrix}y=\begin{vmatrix}L_1&f_1(t)\\L_3&f_2(t)\end{vmatrix}$$
If $x_1,x_2,\cdots x_n$ are $n$ solutions of $x'=P(t)x$, their Wronskian $W \neq 0$ globally if they are linearly independent, or $W = 0$ globally if dependent.

#### 6.3 特征值法
Write the system as $x'=Ax$. Substitute the trial solution $x=ve^{\lambda t} \Rightarrow Av=\lambda v$.
$\lambda$ is an eigenvalue of $A$ if $|A-\lambda I|=0$, and $v$ is the corresponding eigenvector.

#### 6.4 特征向量链
If there's a defective eigenvalue, find a vector $u_{k}$ such that $(A-\lambda I)^{k}u_{k}=0$ but $(A-\lambda I)^{k-1}u_{k} \neq 0$. Multiply successively by $(A-\lambda I)$ to build a chain of generalized eigenvectors $\{v_1,v_2,\cdots,v_k\} = \{u_k, \cdots, u_1\}$.

#### 6.5 基础解矩阵
Let $\Phi(t)$ be a fundamental matrix for $x'=Ax$. 
* The unique solution of $x'=Ax, x(0)=x_0$ is $x(t)=\Phi(t)\Phi(0)^{-1}x_0=e^{At}x_0$.
* For nonhomogeneous system $x'=Ax+f(t)$:
$$\begin{aligned}x(t)=\Phi(t)\Phi(a)^{-1}x_a+\Phi(t)\int_a^t\Phi(s)^{-1}f(s)ds\end{aligned}$$

---
### 七、边值问题

#### 7.1 边值与特征函数
For the boundary value problem $y''+p(x)y'+q(x)y=0$ subject to $y(a)=0, y(b)=0$, the goal is to find solutions defined on $(a,b)$ satisfying conditions at endpoints.
When introducing a parameter $\lambda$: $y''+p(x)y'+\lambda q(x)y=0$, it is called an **eigenvalue problem**.
Values of $\lambda_*$ that yield non-trivial solutions are called **eigenvalues**, and the corresponding non-trivial solutions $y_*$ are **eigenfunctions**.