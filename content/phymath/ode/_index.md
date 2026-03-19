---
title: 常微分方程
date: 2026-03-19
type: docs
---
### Word Table
| 术语                   | 翻译   | 术语             | 翻译   | 术语          | 翻译  |
| -------------------- | ---- | -------------- | ---- | ----------- | --- |
| homogeneous          | 齐次   | constant       | 常数   | derivative  | 导数  |
| superposition        | 叠加   | multiplication | 乘法   | subtitute   | 代替  |
| partial derivative   | 偏导数  | arbitrary      | 任意   | reducible   | 可简化 |
| autonomous           | 自治   | algebra        | 代数   | interval    | 区间  |
| infinite family      | 无穷集  | proportional   | 比例   | explicit    | 特解  |
| assertion            | 断言   | intersect      | 相交   | parameter   | 参数  |
| antiderivative       | 不定积分 | branch         | 分支   | domain      | 范围  |
| independent variable | 自变量  | verify         | 验证   | coefficient | 系数  |
| identity equation    | 恒等式  | curve          | 曲线   | equation    | 方程  |
| dependent variable   | 因变量  | integration    | 积分   | slope       | 斜率  |
| necessary condition  | 必要条件 | exponential    | 指数的  | static      | 静态  |
| asymptote            | 渐近线  | denote         | 表示   | indeed      | 的确  |
| hypothesis           | 假设   | error function | 误差方程 | emcompass   | 包含  |
| equilibrium          | 平衡   | vibration      | 振动   | duplication | 重复  |
### nth-order Differential Equation
The most general form of an nth-order differential equation with independent $x$ and unknown function or dependent variable $y=y(x)$ is $F(x,y,y',y'',\cdots,y^{(n)})$
An nth-order differential equation ordinarily has an n-parameter family of solutions-one involving n different arbitrary constants or parameters.

### Integrals as General and Particular Solutions
The first-order equation $\begin{aligned}\frac{\mathrm{d}y}{\mathrm{d}x}=f(x,y)\end{aligned}$ takes an especially simple form if the function $f$ is independent of the dependent variable $y$ , $\begin{aligned}\frac{\mathrm{d}y}{\mathrm{d}x}=f(x)\end{aligned}$ , in this special case only need to integrate both sides $\begin{aligned}y(x)=\int f(x)\mathrm{d}x+C\end{aligned}$

### Existence  and Uniqueness of Solutions
Suppose that both the function $f(x,y)$ and its partial derivative $D_yf(x,y)$ are continuous on some rectangle $R$ in the xy-plane that contains the point $(a,b)$  in its interior.

Then, for some open interval $I$ containing the point $a$ , the initial value problem $\begin{aligned}\frac{\mathrm{d}y}{\mathrm{d}x}=f(x,y),\quad y(a)=b\end{aligned}$ has one and only one solution that is defined on the interval $I$ .

if the function $f(x,y)$ and/or its partial derivative $\begin{aligned}\frac{\partial f}{\partial y}\end{aligned}$ fail to satisfy the continuity hypothesis , then the initial value problem may have either no solution or many (even infinitely many) solutions.

### Separable Equations
The first-order differential equation $\begin{aligned}\frac{\mathrm{d}y}{\mathrm{d}x}=H(x,y)\end{aligned}$  is called separable provided that $H(x,y)$ can be written as the product of a function of $x$ and a function of $y$ : $\begin{aligned}\frac{\mathrm{d}y}{\mathrm{d}x}=g(x)h(y)=\frac{g(x)}{f(y)}\end{aligned}$
$$\begin{aligned}\int f(y)\mathrm{d}y=\int g(x)\mathrm{d}x+C,\quad F(y)=\int f(y)\mathrm{d}y,\quad G(x)=\int g(x)\mathrm{d}x\end{aligned}$$

### Singular Solutions
It is common for a nonlinear first-order differential equation to have both a general solution involving a n arbitrary constant $C$ and  one or several particular solutions that cannot be obtained by selecting a value for $C$ . These exceptional solutions are frequently called singular solutions.

### Linear first-order Equation
Standard form:
$$\begin{aligned}\frac{\mathrm{d}y}{\mathrm{d}x}+P(x)y=Q(x)\end{aligned},\quad \rho(x)=\mathrm{e}^{\int P(x)\mathrm{d}x}$$
Solution:
$$\begin{aligned}&\mathrm{e}^{\int P(x)\mathrm{d}x}\frac{\mathrm{d}y}{\mathrm{d}x}+P(x)\mathrm{e}^{\int P(x)\mathrm{d}x}y=Q(x)\mathrm{e}^{\int P(x)\mathrm{d}x}\\&y(x)=\mathrm{e}^{-\int P(x)\mathrm{d}x}\begin{bmatrix}\begin{aligned}\int(Q(x)\mathrm{e}^{\int P(x)\mathrm{d}x})\end{aligned}\mathrm{d}x+C\end{bmatrix}\end{aligned}$$
1. Begin by calculating the integrating factor $\rho(x)=e^{\int P(x)\mathrm{d}x}$
2. Then multiply both sides of the differential equation by $\rho(x)$	
3. Next , recognize the left-hand side of the resulting equation as the derivative of a product : 
$$D_x[\rho(x)y(x)]=\rho(x)Q(x)$$
4. Finally , integrate this equation
$$\begin{aligned}\rho(x)y(x)=\int\rho((x)Q(x)\mathrm{d}x+C\end{aligned}$$

Properties:
* guarantee only a solution on a possibly smaller interval.
* linear first-order differential equation has no singular solutions.

### Exact Differential Equation 
A general solution $y(x)$ of a first-order differential equation is often defined implicitly by an equation of the form $F(x,y(x))=C$ ,differentiate each side with respect to $x$ 
$$\begin{aligned}&\frac{\partial F}{\partial x}+\frac{\partial F}{\partial y}\frac{\mathrm{d}y}{\mathrm{d}x}=0\\&\Rightarrow M(x,y)+N(x,y)\frac{\mathrm{d}y}{\mathrm{d}x}=0\\&\Rightarrow M(x,y)\mathrm{d}x+N(x,y)\mathrm{d}y=0\end{aligned}$$
If there exists a function $F(x,y)$ such that $\begin{aligned}\frac{\partial F}{\partial x}=M, \quad \frac{\partial F}{\partial y}=N\end{aligned}$ ,then the equation $F(x,y)=C$ implicitly defines a general solution of $M(x,y)\mathrm{d}x+N(x,y)\mathrm{d}y=0$ ,then $M(x,y)\mathrm{d}x+N(x,y)\mathrm{d}y=0$ is called an exact differential equation.

If $M(x,y)\mathrm{d}x+N(x,y)\mathrm{d}y=0$ is exact and $M$ and $N$ have continuous partial derivatives, it then follows that $\begin{aligned}\frac{\partial M}{\partial y}=F_{xy}=F_{yx}=\frac{\partial N}{\partial x}\end{aligned}$ .

Thus the equation $\begin{aligned}\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}\end{aligned}$ is a necessary condition that the differential equation $M\mathrm{d}x+N\mathrm{d}y=0$ to be exact.

whether a given differential equation is exact or not is related to the precise form $M\mathrm{d}x+N\mathrm{d}y=0$ in which it is written.

$$\begin{aligned}F(x,y)=\int M(x,y)\mathrm{d}x+g(y)\end{aligned}$$
$$\begin{aligned}N=\frac{\partial F}{\partial y}=\begin{pmatrix}\begin{aligned}\frac{\partial}{\partial y}\int M(x,y)\mathrm{d}x\end{aligned}\end{pmatrix}+g'(y)\end{aligned}$$
$$\begin{aligned}g'(x)=N-\frac{\partial}{\partial y}\int M(x,y)\mathrm{d}x\end{aligned}$$
$$\begin{aligned}F(x,y)=\int M(x,y)\mathrm{d}x+\int\begin{pmatrix}\begin{aligned}N(x,y)-\frac{\partial}{\partial y}\int M(x,y)\mathrm{d}x\end{aligned}\end{pmatrix}\mathrm{d}y\end{aligned}$$

### Integrating Factor
If the original equation $M(x,y)\mathrm{d}x+N(x,y)\mathrm{d}y=0$ is not exact, we can multiply it by an integrating factor $\mu(x,y)M(x,y)\mathrm{d}x+\mu(x,y)N(x,y)\mathrm{d}y=0$
* Assume the integrating factor $\mu$ depends only on $x$ , $\mu=\mu(x)$ , Then:
$$
\begin{aligned}
&\frac{\partial(\mu M)}{\partial y} 
= \frac{\partial(\mu N)}{\partial x} \\
&\Rightarrow \mu\frac{\partial M}{\partial y} = \frac{\partial\mu}{\partial x}N + \mu\frac{\partial N}{\partial x} \\
&\Rightarrow \mu\left(\frac{\partial M}{\partial y} - \frac{\partial N}{\partial x}\right) = \frac{\partial\mu}{\partial x}N \\
&\Rightarrow \frac{\mathrm{d}\mu}{\mu} = \frac{1}{N}\left(\frac{\partial M}{\partial y} - \frac{\partial N}{\partial x}\right)\mathrm{d}x \\
&\Rightarrow \ln|\mu| = \int \frac{1}{N}\left(\frac{\partial M}{\partial y} - \frac{\partial N}{\partial x}\right)\mathrm{d}x + C \\
&\Rightarrow \mu = \exp\left[\int \frac{1}{N}\left(\frac{\partial M}{\partial y} - \frac{\partial N}{\partial x}\right)\mathrm{d}x + C\right]
\end{aligned}
$$
* Assume the integrating factor $\mu$ depends only on $y$ , $\mu=\mu(y)$ , Then:
$$
\begin{aligned}
&\frac{\partial(\mu M)}{\partial y} = \frac{\partial(\mu N)}{\partial x} \\
&\Rightarrow \frac{\partial\mu}{\partial y}M + \mu\frac{\partial M}{\partial y} = \mu\frac{\partial N}{\partial x} \\
&\Rightarrow \mu\left(\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y}\right) = \frac{\partial\mu}{\partial y}M \\
&\Rightarrow \frac{\mathrm{d}\mu}{\mu} = \frac{1}{M}\left(\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y}\right)\mathrm{d}y \\
&\Rightarrow \ln|\mu| = \int \frac{1}{M}\left(\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y}\right)\mathrm{d}y + C \\
&\Rightarrow \mu = \exp\left[\int \frac{1}{M}\left(\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y}\right)\mathrm{d}y + C\right]
\end{aligned}
$$
### Substitution Methods
#### Exp 1: General First-Order Equation

Consider the equation  
$$
\frac{\mathrm{d}y}{\mathrm{d}x} = f(x,y).
$$

**Solution:**  
Introduce a new dependent variable $v = \alpha(x,y)$, so that $y = \beta(x,v)$. Then  
$$
\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\partial \beta}{\partial x}\frac{\mathrm{d}x}{\mathrm{d}x} + \frac{\partial \beta}{\partial v}\frac{\mathrm{d}v}{\mathrm{d}x} = \beta_x + \beta_v \frac{\mathrm{d}v}{\mathrm{d}x}.
$$
Substituting into the original equation yields a new first‑order equation for $v$:
$$
\frac{\mathrm{d}v}{\mathrm{d}x} = g(x,v).
$$
This new equation may be separable or linear, and can be solved by standard methods.
#### Exp 2: Bernoulli Equation

The Bernoulli equation has the form  
$$
\frac{\mathrm{d}y}{\mathrm{d}x} + P(x)\,y = Q(x)\,y^{\,n}, \qquad n \neq 0,1.
$$

**Solution:**  
Set $v = y^{1-n}$. Then  
$$
\frac{\mathrm{d}v}{\mathrm{d}x} = (1-n)y^{-n}\frac{\mathrm{d}y}{\mathrm{d}x}.
$$
Multiply the original equation by $(1-n)y^{-n}$:
$$
(1-n)y^{-n}\frac{\mathrm{d}y}{\mathrm{d}x} + (1-n)P(x)y^{1-n} = (1-n)Q(x).
$$
Using the expression for $\frac{\mathrm{d}v}{\mathrm{d}x}$, we obtain a linear first‑order equation for $v$:
$$
\frac{\mathrm{d}v}{\mathrm{d}x} + (1-n)P(x)\,v = (1-n)Q(x).
$$
Solve this linear equation for $v(x)$, then recover $y = v^{1/(1-n)}$.
#### Exp 3: Homogeneous Equation

A homogeneous first‑order equation can be written as  
$$
\frac{\mathrm{d}y}{\mathrm{d}x} = F\!\left(\frac{y}{x}\right).
$$

**Solution:**  
Introduce the substitution $v = \dfrac{y}{x}$, so that $y = vx$. Then  
$$
\frac{\mathrm{d}y}{\mathrm{d}x} = v + x\frac{\mathrm{d}v}{\mathrm{d}x}.
$$
Substituting into the equation gives  
$$
v + x\frac{\mathrm{d}v}{\mathrm{d}x} = F(v) \quad\Longrightarrow\quad x\frac{\mathrm{d}v}{\mathrm{d}x} = F(v) - v.
$$
This is a separable equation in $x$ and $v$. Solve it to find $v(x)$, and then $y = x\,v(x)$.

#### Exp 4: Reducible Second‑Order Equation

Consider a second‑order equation of the form  
$$
\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}} = f\!\left(x,y,\frac{\mathrm{d}y}{\mathrm{d}x}\right) \quad\text{or}\quad F(x,y,y',y'')=0.
$$
Two common cases allow reduction to a first‑order problem:

1. **Dependent variable $y$ missing:**  
   The equation is $F(x,y',y'')=0$. Set $p = y' = \dfrac{\mathrm{d}y}{\mathrm{d}x}$, so $y'' = \dfrac{\mathrm{d}p}{\mathrm{d}x}$.  
   The equation becomes $F(x,p,p')=0$. If this first‑order equation can be solved for $p(x,C_1)$, then  
   $$
   y(x) = \int y'(x)\,\mathrm{d}x = \int p(x,C_1)\,\mathrm{d}x + C_2.
   $$

2. **Independent variable $x$ missing:**  
   The equation is $F(y,y',y'')=0$. Set $p = y' = \dfrac{\mathrm{d}y}{\mathrm{d}x}$ and use the chain rule:  
   $$
   y'' = \frac{\mathrm{d}p}{\mathrm{d}x} = \frac{\mathrm{d}p}{\mathrm{d}y}\frac{\mathrm{d}y}{\mathrm{d}x} = p\frac{\mathrm{d}p}{\mathrm{d}y}.
   $$  
   The equation reduces to $F\!\left(y,p,p\frac{\mathrm{d}p}{\mathrm{d}y}\right)=0$, a first‑order equation in $y$ and $p$.  
   If we can find a solution $p(y,C_1)$, then  
   $$
   x(y) = \int \frac{\mathrm{d}x}{\mathrm{d}y}\,\mathrm{d}y = \int \frac{1}{\mathrm{d}y/\mathrm{d}x}\,\mathrm{d}y = \int \frac{1}{p(y,C_1)}\,\mathrm{d}y + C_2,
   $$
   which gives $x$ as a function of $y$.
### Singular solutions

There are special solutions thar cannot be obtained from the general solution $y=\varphi(x;C)$ for some value of $C$ ,but are always tangent to one of the $y=\varphi(x,C)$ solution at some point.

If there is a singular solution, at each point on the curve has more than 1 solution.
if $y=\varphi(x)$ is a singular solution $\Rightarrow$ It's a p-discriminant  

1. Re-write the ODE as an integral equation.
2. Construct the Picard iterates.
3. Show that the Picard iterates converges uniformly on $|x-x_0|\leq h$
4. Show that the above limit function is a solution.
5. Show that the solution is unique. 

### Principle of the p-Discriminant Method

Consider a first-order OED in implicit form
$$\begin{aligned}F(x,y,p)=0,\quad p=\frac{\mathrm{d}y}{\mathrm{d}x}\end{aligned}$$
A singular solution must satisfy two conditions simultaneously
*  The original equation $F(x,y,p)=0$
*  The partial derivative of $F$ with respect to $\begin{aligned}p:\frac{\partial F}{\partial p}=0\end{aligned}$
By eliminating $p$ from these equations, we obtain the p-discriminant curve, which may represent the singular solution.

### Proving the Correctness of the p-Discriminant Method

**Singular Solution:** A solution of a differential equation that is not tangent to any solution in the family of general solutions and cannot be obtained by choosing specific values for the constants in the general solution.

**Envelop:** A curve that is tangent at each point to some solution in the family of general solutions. A singular solution is typically the envelope of general solution family.
**p-Discriminant Method:** By solving the system $F(x,y,p)=0$ and $\begin{aligned}\frac{\partial F}{\partial p}=0\end{aligned}$ , the curve obtained after eliminating $p$ may represent a singular solution.

Assume the family of general solutions is $\varphi(x,y,C)=0$ where $C$ is a constant. 
The envelope must satisfy: $\varphi(x,y,C)=0\quad\begin{aligned}\frac{\partial\varphi}{\partial C}=0\end{aligned}$
Eliminating $C$ gives the envelope's equation.

For the differential equation $F(x,y,p)=0$ , the envelope (singular solution) of its general solution family must satisfy:
* Every point $(x,y)$ on the envelope satisfies $F(x,y,p)=0$ (Since it is a solution)
* The slope $p$ of the envelope at that point matches the slope of the corresponding solution in the general family
* The envelope represents a limiting case where distinct solutions "coalesce", implying the dependence on $C$ vanishes, leading to $\begin{aligned}\frac{\partial F}{\partial p}=0\end{aligned}$

### Homogeneous Second-Order Linear Equations

Let $y_1$ and $y_2$ be two solutions of the homogeneous linear equation in $y''+p(x)y'+q(x)y=0$ on the interval $I$.If $c_1$ and $c_2$ are constants, then the linear combination $y=c_1y_1+c_2y_2$ is also a solution on $I$.

The second-order equation $y''+p(x)y'+q(x)y=f(x)$ has infinitely many solution curves passing through the point $(a,b_0)$ , namely one for each (real number) value of the initial slope $y'(a)=b_1$ . That is, instead of there being only one line through $(a,b_0)$ tangent to a solution curve, every nonvertical straight line through $(a,b_0)$ is tangent to some solution curve of $y''+p(x)y'+q(x)y=f(x)$.

### Linear Independence of Two Functions

Two functions defined on an open interval $I$ are said to be linearly independent on $I$ provided that neither is a constant multiple of the other.
Given two functions $f$ and $g$ , the Wronskian of $f$ and $g$ is the determinant
$$W=\begin{vmatrix}f&g\\f'&g'\end{vmatrix}=fg'-f'g$$ 
Suppose that $y_1$ and $y_2$ are solutions of the homogeneous second-order linear equation $y''+p(x)y'+q(x)y=0$ on an open interval $I$ on which $p$ and $q$ are continuous
* If $y_1$ and $y_2$ are linearly dependent, then $W(y_1,y_2)=0$ on $I$
* If $y_1$ and $y_2$ are linearly independent, then $W(y_1,y_2)\neq0$ at each point of $I$

### Linear Second-Order Equations with Constant Coefficients

$ar^2+br+c=0$ this quadratic equation is called the characteristic equation of the homogeneous linear differential equation $ay''+by'+cy=0$ 
* If the roots $r_1$ and $r_2$ of the characteristic equation are real and distinct, then $y(x)=c_1e^{r_1x}+c_2e^{r_2x}$ is a general solution.
* If the characteristic equation has equal roots $r_1=r_2$ , then $y(x)=(c_1+c_2x)e^{r_1x}$ is a general solution.

### General Solutions of Linear Equations

Let $y_1,y_2,\cdots,y_n$ be $n$ solutions of the homogeneous linear equation in $y^{(n)}+p_1(x)y^{(n-1)}+\cdots+p_{n-1}(x)y'+p_n(x)y=0$ on the interval $I$ . If  $c_1,c_2,\cdots,c_n$ are constants, then the linear combination $y=c_1y_2+c_2y_c+\cdots+c_ny_n$ is also a solution.

The $n$ functions $f_1,f_2,\cdots,f_n$ are said to be linearly dependent on the interval $I$ provided that there exist constants $c_1,c_2,\cdots,c_n$ not all zero such that $c_1f_1+c_2f_2+\cdots+c_nf_n=0$ 
Their Wronskian is the $n\times n$ determinant 
$$W=\begin{vmatrix}f_1&f_2&\cdots&f_n\\f_1'&f_2'&\cdots&f_n'\\\vdots&\vdots&&\vdots\\f^{(n-1)}_1&f^{(n-1)}_2&\cdots&f^{(n-1)}_n\end{vmatrix}$$ 
Suppose that $y_1,y_2,\cdots,y_n$ are $n$ solutions of the homogeneous nth-order linear equation $y^{(n)}+p_1(x)y^{(n-1)}+\cdots+p_{n-1}(x)y'+p_n(x)y=0$ on an open interval $I$ where each $p_i$ is continuous. Let $W=W(y_1,y_2,\cdots,y_n)$ 
* If $y_1,y_2,\cdots,y_n$ are linearly dependent, then $W=0$ on $I$
* If $y_1,y_2,\cdots,y_n$ are linearly independent, then $W\neq0$ at each point of $I$

### Nonhomogeneous Equations

Let $y_p$ be a particular solution of the nonhomogeneous equation $y^{(n)}+p_1(x)y^{(n-1)}+\cdots+p_{n-1}(x)y'+p_n(x)y=f(x)$ on an open interval $I$ where the functions $p_i$ and $f$ are continuous. Let $y_1,y_2,\cdots,y_n$ be linearly independent solutions of the associated homogeneous equation $y^{(n)}+p_1(x)y^{(n-1)}+\cdots+p_{n-1}(x)y'+p_n(x)y=0$ . If $Y$ is any solution whatsoever of $y^{(n)}+p_1(x)y^{(n-1)}+\cdots+p_{n-1}(x)y'+p_n(x)y=f(x)$ on $I$ ,then there exist number $c_1,c_2,\cdots,c_n$ such that for all $x$ in $I$ :
$$Y(x)=c_1y_1(x)+c_2y_2(x)+\cdots+c_ny_n(x)+y_p(x)$$
### Polynomial Operators

$$\begin{aligned}L&=a_n\frac{d^n}{dx^n}+a_{n-1}\frac{d^{n-1}}{dx^{n-1}}+\cdots+a_2\frac{d^2}{dx^2}+a_1\frac{d}{dx}+a_0\\&=a_nD^n+a_{n-1}D^{n-1}+\cdots+a_nD^2+a_1D+a_0\end{aligned}$$

### Homogeneous Equations with Constant Coefficients

$a_nr^n+a_{n-1}r^{n-1}+\cdots+a_2r^2+a_1r+a_0=0$ is called the characteristic equation or auxiliary equation of the differential equation of $a_ny^{(n)}+a_{n-1}y^{(n-1)}+\cdots+a_1y'+a_0y=0$
* If the roots $r_1,r_2,\cdots,r_n$ of the characteristic equation are real and distinct, then $y(x)=c_1e^{r_1x}+c_2e^{r_2x}+\cdots+c_ne^{r_nx}$ is a general solution.
* If the characteristic equation has repeated roots $r_1$ , the desired solution  of $(D-r_1)^ky=0$ is $y(x)=ue^{r_1x}=(c_1+c_2x+c_3x^2+\cdots+c_kx^{k-1})e^{r_1x}$

### Complex-Valued Functions and Euler's Formula

$$\begin{cases}e^{ix}=\cos{x}+i\sin{x}\\e^{(a+bi)x}=e^{ax}(\cos{bx}+i\sin{bx})\\e^{(a-bi)x}=e^{ax}(\cos{bx}-i\sin{bx})\end{cases}$$

$$\begin{aligned}y(x)&=c_1e^{r_1x}+c_2e^{r_2x}=c_1e^{(a+bi)x}+c_2e^{(a-bi)x}\\&=c_1e^{ax}(\cos{bx}+i\sin{bx})+c_2e^{ax}(\cos{bx}-i\sin{bx})\\&=(c_1+c_2)e^{ax}\cos{bx}+i(c_1-c_2)e^{ax}\sin{bx}\\&=e^{ax}(d_1\cos{bx}+d_2\sin{bx})\end{aligned}$$

### Reduction of Order

Suppose that one solution $y_1(x)$ of the homogeneous second-order linear differential equation $y''+p(x)y'+q(x)y=0$ is known. The method of reduction of order consists of substituting $y_2(x)=v(x)y_1(x)$ and attempting to determine the function $v(x)$ so that $y_2(x)$ is a second linearly independent solution.

### Method of Undetermined Coefficients

$f(x)$ can be written as a sum of terms each of the form $P_m(x)e^{rx}\cos{kx}$ or $P_m(x)e^{rx}\sin{kx}$ take the trail solution $y_p(x)=x^s[(A_0+A_1x+\cdots+A_mx^m)e^{rx}\cos{kx}+(B_0+B_1x+\cdots+B_mx^m)e^{rx}\sin{kx}]$
where $s$ is the smallest nonnegative integer such that no term in $y_p$ duplicates a term in the complementary function $y_c$  

|            $f(x)$             |                                                  $y_p$                                                   |
| :---------------------------: | :------------------------------------------------------------------------------------------------------: |
| $P_m=b_0+b_1x+\cdots+b_mx^m$  |                                      $x^s(A_0+A_1x+\cdots+A_mx^m)$                                       |
|     $a\cos{kx}+b\sin{kx}$     |                                        $x^s(A\cos{kx}+B\sin{kx})$                                        |
| $e^{rs}(a\cos{kx}+b\sin{kx})$ |                                     $x^se^{rx}(A\cos{kx}+B\sin{kx})$                                     |
|        $P_m(x)e^{rx}$         |                                   $x^s(A_0+A_1x+\cdots+A_mx^m)e^{rx}$                                    |
| $P_m(x)(a\cos{kx}+b\sin{kx})$ | $\begin{aligned}x^s[&(A_0+A_1x+\cdots+A_mx^m)\cos{kx}+\\&(B_0+B_1x+\cdots+B_mx^m)\sin{kx}]\end{aligned}$ |

### Variation of Parameters

If the nonhomogeneous equation $y''+P(x)y'+Q(x)y=f(x)$ has complementary function $y_c(x)=c_1y_1(x)+c_2y_2(x)$ , then a particular solution is given by
$$\begin{cases}u_1'y_1+u_2'y_2=0\\u_1'y_1'+u_2'y_2'=f(x)\end{cases}$$
$$\begin{aligned}y_p(x)=-y_1(x)\int\frac{y_2(x)f(x)}{W(x)}dx+y_2\int\frac{y_1(x)f(x)}{W(x)}dx\end{aligned}$$
where $W=W(y_1,y_2)$ is the Wronskian of the two independent solutions $y_1$ and $y_2$ of the associated homogeneous equation. 

### Endpoint Problems and Eigenvalues

$$y''+p(x)y'+q(x)y=0,y(a)=0,y(b)=0$$
to find a solution of the differential equation on the interval $(a,b)$ that satisfies the condition $y(a)=0$ and $y(b)=0$ at the endpoints of the interval. Such a problem is called an endpoint or boundary value problem.
$$y''+p(x)y'+\lambda q(x)y=0,y(a)=0,y(b)=0$$
An  endpoint problem containing a parameter $\lambda$  is called an eigenvalue problem. If there are values of the parameter $\lambda$ exist a nontrivial solution of the endpoint problem, such a value of $\lambda$ is called an eigenvalue of characteristic value of the problem. 
Suppose that $\lambda_{\ast}$ is an eigenvalue of the problem and that $y_{\ast}$ is a nontrivial solution of the problem with this value of $\lambda$ inserted
$$
y_*''+p(x)y_*'+\lambda_*q(x)y_*=0,y_*(a)=0,y_*(b)=0
$$
Then we call $y_\ast$ an eigenfunction associated with the eigenvalue $\lambda_{\ast}$ .

### Power Series

$\begin{aligned}\sum_{n=0}^{\infty}c_n(x-a)^n=c_0+c_1(x-a)+\cdots+c_n(x-a)^n\end{aligned}+\cdots$
$\begin{aligned}f(x)=\sum_{n=0}^\infty c_nx^n=c_0+c_1x+c_2x^2+\cdots\end{aligned}$
$\begin{aligned}f'(x)=\sum_{n=1}^\infty nc_nx^{n-1}=c_1+2c_2x+3c_3x^2+\cdots\end{aligned}$
### Radius of Convergence

Given the power series $\sum c_nx^n$ ,suppose that the limit $\begin{aligned}\rho=\lim_{n\rightarrow\infty}|\frac{c_n}{c_{n+1}}|\end{aligned}$
exists ($\rho$ is finite) or infinite, Then
* if $\rho=0$ ,then the series diverges for all $x\neq 0$
* if $0<\rho<\infty$ ,then $\sum c_nx^n$ converges if $|x|<\rho$ and diverges if $|x|>\rho$
* if $\rho=\infty$ ,then the series converges for all $x$
$A(x)y''+B(x)y'+C(x)y=0$ the point $x=a$ is called an ordinary point of $y''+P(x)y'+Q(x)y=0$ provided that the function $P(x)$ and $Q(x)$ are both analytic at $x=a$ ,Otherwise $x=a$ is a singular point

### Solutions Near an Ordinary Point

Suppose thar $a$ is an ordinary point of the equation $A(x)y''+B(x)y'+C(x)y=0$ that is the functions $P=B/A$ and $Q=C/A$ are analytic at $x=a$ ,then the equation has two linearly independent solutions , each of the form $\begin{aligned}y(x)=\sum_{n=0}^\infty c_n(x-a)^n\end{aligned}$
The radius of convergence of any such series solution is at least as large as the distance from $a$ to the nearest (real or complex) singular point of the equation, the coefficients in the series can be determined by its substitution.

### Regular Singular Points

A differential equation having a singular point at 0 ordinarily will not have power series solutions of the form $y(x)=\sum c_nx^n$ . To investigate the form that a solution of such an equation might take, assume that analytic coefficient functions and rewrite it in the standard form $$\begin{aligned}&y''+P(x)y'+Q(x)y=0\\&y''+\frac{p(x)}{x}y'+\frac{q(x)}{x^2}y=0,p(x)=xP(x),q(x)=x^2Q(x)\end{aligned}$$
The singular point $x=0$ is a regular singular point if the functions $p(x)=xP(x)$ and $q(x)=x^2Q(x)$ are both analytic at $x=0$. Otherwise it is an irregular singular point.
$$\begin{aligned}p_0=p(0)=\lim_{x\rightarrow0}p(x)=\lim_{x\rightarrow0}xP(x)\end{aligned}$$
$$\begin{aligned}q_0=q(0)=\lim_{x\rightarrow0}q(x)=\lim_{x\rightarrow0}x^2Q(x)\end{aligned}$$
* if $p_0=q_0=0$ then $x=0$ may be an ordinary point
* if the limits exist and are finite, then $x=0$ is a regular singular point
* if either limit fails to exist or is infinite, then $x=0$ is an irregular singular point

### The Method of Frobenius
In general case, $p(x)$ and $q(x)$ are power series rather than constants, it is a reasonable conjecture that out differential equation might have a solution of the form
$$\begin{aligned}y(x)=x^r\sum_{n=0}^\infty c_nx^n=\sum_{n=0}^\infty c_nx^{n+r}=c_0x^r+c_1x^{r+1}+\cdots\end{aligned}$$
such series is called a Frobenius series.
To investigate the possible existence of Frobenius series solutions, begin with the equation
$$x^2y''+xp(x)y'+q(x)y=0$$
If $x=0$ is a regular singular point, then $p(x)$ and $q(x)$ are analytic at $x=0$ ,so
$$
\begin{align}
p(x)=p_0+p_1x+p_2x^2+p_3x^3+\cdots \\
q(x)=q_0+q_1x+q_2x^2+q_3x^3+\cdots
\end{align}
$$
Suppose the equation has the Frobenius series solution
$$\begin{aligned}y=\sum_{n=0}^\infty c_nx^{n+r}\quad y'=\sum_{n=0}^{\infty}c_n(n+r)x^{n+r-1}\quad y''=\sum_{n=0}^\infty c_n(n+r)(n+r-1)x^{n+r-2}\end{aligned}$$
the coefficient $r(r-1)c_0+p_0rc_0+q_0c_0$ of $x^r$ must vanish, because $c_0\neq0$ ,it follows that $r$ must satisfy the quadratic equation $r(r-1)+p_0r+q_0=0$  , which is called the indicial equation, and its two roots are the exponents of the differential equation at $x=0$
1. If $r_1\neq r_2$ ,it follows that there are two possible Frobenius series solutions
2. If $r_1=r_2$ ,there is only one possible Frobenius series solution

### Frobenius Series Solutions
Suppose that $x=0$ is a regular singular point of the equation $x^2y''+xp(x)y'+q(x)y=0$
Let $\rho>0$ denote the minimum of the radii of convergence of the power series
$$
\begin{aligned}p(x)=\sum_{n=0}^\infty p_nx^n\quad\mathrm{and}\quad q(x)=\sum_{n=0}^\infty q_nx^n\end{aligned}
$$
Let $r_1$ and $r_2$ be the roots, with $r_1\geq r_2$
* For $x>0$ , there exists a solution of the form $\begin{aligned}y_1(x)=x^{r_1}\sum_{n=0}^\infty a_nx^n\quad(a_0\neq 0)\end{aligned}$
* If $r_1-r_2$ is neither zero nor a positive integer, there exists a second linearly independent solution for $x>0$ of the form $\begin{aligned}y_2(x)=x^{r_2}\sum_{n=0}^\infty b_nx^n\quad(b_0\neq 0)\end{aligned}$
* If $r_1-r_2$ is a positive integer there may or may not exist a second Frobenius series solution of the equation

### The Nonlogarithmic Case with r1=r2+N

Derived the indicial equation by substituting the power series $p(x)=\sum p_nx^n$ and $\sum q_nx^n$ and the Frobenius series $\begin{aligned}y(x)=x\sum_{n=0}^\infty c_nx^{n+r},c_0\neq0\end{aligned}$ in the differential equation in the form $x^2y''+xp(x)y'+q(x)y=0$

The result of this substitution, after collection of the coefficients of like powers of $x$ , is an equation of the form $\begin{aligned}\sum_{n=0}^\infty F_n(r)x^{n+r}=0\end{aligned}$
$$F_0(r)=[r(r-1)+p_0r+q_0]c_0=\phi(r)c_0$$
$$F_n(r)=\phi(r+n)c_n+L_n(r:c_0,c_1,\cdots,c_{n-1})$$
$$\begin{aligned}L_n=\sum_{k=0}^{n-1}[(r+k)p_{n-k}+q_{n-k}]c_k\end{aligned}$$
$$\begin{aligned}y_2=y_1\int\frac{\exp(-\int P(x)dx)}{y_1^2}dx\end{aligned}$$
* $N=0$ , $\begin{aligned}y_2(x)=y_1(x)\ln{x}+x^{1+r_1}\sum_{n=0}^{\infty}b_nx^n\end{aligned}$
* $N\neq0$ , $\begin{aligned}y_2(x)=C_Ny_1(x)\ln{x}+x^{r_2}\sum_{n=0}^\infty b_nx^n\end{aligned}$

### First-Order Systems and Applications
Consider the system consisting of the single nth-order equation
$$x^{(n)}=f(t,x,x',\cdots,x^{(n-1)})$$
Introduce the dependent variables $x_1,x_2,\cdots,x_n$ defined as follows:
$$x_1=x,\quad x_2=x',\quad x_3=x'',\quad\cdots,\quad x_n=x^{(n-1)}$$
The substitution yields the system
$$x_n'=f(t,x_1,x_2,\cdots,x_n)$$

### Linear systems
Consider a linear first-order system of the form
$$
\begin{align}
x_1'&=p_{11}(t)x_1+p_{12}(t)x_2+\cdots+p_{1n}(t)x_n+f_1(t)\\
x_2'&=p_{21}(t)x_1+p_{22}(t)x_2+\cdots+p_{2n}(t)x_n+f_2(t)\\
&\quad\quad\quad\quad\quad\quad\quad\quad\quad\vdots\\
x_n'&=p_{n1}(t)x_1+p_{n2}(t)x_2+\cdots+p_{nn}(t)x_n+f_n(t)
\end{align}
$$
We say that this system is homogeneous if the functions $f_1,f_2,\cdots,f_n$ are all identically zero, Otherwise, it is nonhomogeneous

Any system of two linear differential equations with constant coefficients can be written in the form $L_1x+L_2y=f_1(t),L_3x+L_4y=f_2(t)$
$$\begin{align}&\begin{cases}L_1x+L_2y=f_1(t)\Rightarrow L_3L_1x+L_3L_2y=L_3f_1(t)\\L_3x+L_4y=f_2(t)\Rightarrow L_1L_3x+L_1L_4y=L_1f_2(t)\end{cases}\\&\Rightarrow(L_1L_4-L_2L_3)y=L_1f_2(t)-L_3f_1(t)\end{align}$$
define the operational determinant
$$\begin{vmatrix}L_1&L_2\\L_3&L_4\end{vmatrix}=L_1L_4-L_2L_3$$
Then the equation related to $x$ and $y$ can be rewritten as
$$\begin{vmatrix}L_1&L_2\\L_3&L_4\end{vmatrix}x=\begin{vmatrix}f_1(t)&L_2\\f_2(t)&L_4\end{vmatrix},\quad\begin{vmatrix}L_1&L_2\\L_3&L_4\end{vmatrix}y=\begin{vmatrix}L_1&f_1(t)\\L_3&f_2(t)\end{vmatrix}$$
Similarly, for the system of three linear equations, $x$ satisfies the single linear equation
$$\begin{vmatrix}L_{11}&L_{12}&L_{13}\\L_{21}&L_{22}&L_{23}\\L_{31}&L_{32}&L_{33}\end{vmatrix}x=\begin{vmatrix}f_1(t)&L_{12}&L_{13}\\f_2(t)&L_{22}&L_{23}\\f_3(t)&L_{32}&L_{33}\end{vmatrix}$$

Suppose that $x_1,x_2,\cdots x_n$ are $n$ solutions of the homogeneous linear equation $x'=P(t)x$ on an open interval $I$ ,suppose that $P(t)$ is continuous on $I$ ,let $W=W(x_1,x_2,\cdots,x_n)$
* If $x_1,x_2,\cdots,x_n$ are linearly dependent on $I$ ,then $W=0$ at every point of $I$
* If $x_1,x_2,\cdots,x_n$ are linearly independent  on $I$ ,then $W\neq0$ at every point of $I$

### The Eigenvalue Method for Homogeneous Systems

Write the system in the matrix form $x'=Ax$ where $A=[a_{ij}]$ , When substitute the trial solution $x=ve^{\lambda t}$ with derivative $x'=\lambda ve^{\lambda t}$ , the result is $\lambda ve^{\lambda t}=Ave^{\lambda t}\Rightarrow Av=\lambda v$
The number $\lambda$ is called an eigenvalue of the $n\times n$ matrix $A$ provided that $|A-\lambda I|=0$
The vector $v$ is called an eigenvector of $\lambda$

### Chains of Generalized Eigenvalues

Begin with a nonzero solution of $(A-\lambda I)^{d+1}u=0$ and successively multiply by the matrix $A-\lambda I$ until the zero vector is obtained, If
$$\begin{aligned}&(A-\lambda I)u_1=u_2\neq 0\\&\quad\quad\quad\quad\vdots\\&(A-\lambda I)u_{k-1}=u_k\neq0\end{aligned}$$
but  $(A-\lambda I)u_k=0$ ,then the vectors $\{v_1,v_2,\cdots,v_k\}=\{u_k,u_{k_1}\cdots,u_2,u_1\}$ form a length $k$ chain of generalized eigenvectors based on the eigenvector $v_1$

### Fundamental Matrix Solutions

Let $\Phi(t)$ be a fundamental matrix for the homogeneous linear system $x'=Ax$
Then the unique solution of the initial value problem $x'=Ax,x(0)=x_0$
is given by $x(t)=\Phi(t)\Phi(0)^{-1}x_0=e^{At}x_0$
$$\begin{aligned}x(t)=e^{At}x_0+e^{At}\int_0^te^{-As}f(s)ds\end{aligned}$$
$$\begin{aligned}x(t)=\Phi(t)\Phi(a)^{-1}x_a+\Phi(t)\int_a^t\Phi(s)^{-1}f(s)ds\end{aligned}$$



