---
title: Ch-8 多元函数微分学
weight: "2"
date: 2026-03-19
type: docs
---
### 平面点集

设 $P(x_0,y_0)\in R^2$ ，把 $U^\circ(P_0,\delta)=\{P(x,y):0<(x-x_0)^2+(y-y_0)^2<\delta^2\}$
称为 $P_0$ 的 $\delta$ 空心邻域，任意一点 $P_0\in R^2$ 与任意一个点集 $E\in R^2$ 的关系有
* 内点，存在点 $P_0$ 的某一邻域 $U(P_0)\subset E$
* 外点，存在点 $P_0$ 的某一邻域 $U(P_0)\cup E=\emptyset$ 
* 边界点，在点 $P_0$ 的任一邻域既含有属于 $E$ 的点又含有不属于 $E$ 的点

根据点集中所属点的特征，可以将点集分为
* 开集，平面点集 $E$ 中的每一点都是 $E$ 的内点，即 $\mathrm{int} E=E$
* 闭集，平面点集 $E$ 的余集 $R^2-E$ 是开集

若 $E$ 中任意两点都可用一条完全含于 $E$ 的有限条折线连接，则称具有连通性
若 $E$ 既是开集又具有连通性，则称 $E$ 为开区域

开区域连同其边界构成的点集称为闭区域
开区域、闭区域连同其一部分边界点组成的点集统称为区域
若存在常数 $r$ 使 $E\subset U(O,r)$ 则称 $E$ 是有界集，否则称为无界集
### 二元函数的极限与连续

设二元函数 $z=f(P)=f(x,y)$ 在点 $P_0(x_0,y_0)$ 的某邻域 $U^\circ(P_0)$ 内有意义，若存在常数 $A$ ，任给 $\varepsilon>0$ ，若存在 $\delta>0$ 当 $0<\rho(P,P_0)<\delta$ 时都有 $|f(P)-A|=|f(x,y)-A|<\varepsilon$ 则称 $A$ 是函数 $f(P)=f(x,y)$ 当点 $P(x,y)$ 趋于点 $P_0(x_0,y_0)$ 时的极限，记作
$$
\begin{aligned}\lim_{(x,y)\rightarrow(x_0,y_0)}f(x,y)=A\quad或\quad\lim_{P\rightarrow P_0}f(P)=A\end{aligned}
$$
可用归结原理，当发现 $P$ 按两个特殊路径趋于 $P_0$ 时 $f(P)$ 极限不一致则判断极限不存在

若累次极限 $\begin{aligned}\lim_{x\rightarrow x_0}\lim_{y\rightarrow y_0}f(x,y),\lim_{y\rightarrow y_0}\lim_{x\rightarrow x_0}f(x,y)\end{aligned}$ 和二重极限 $\begin{aligned}\lim_{\begin{aligned}x\rightarrow x_0\\y\rightarrow y_0\end{aligned}}f(x,y)\end{aligned}$   都存在则三者相等
若 $\begin{aligned}\lim_{x\rightarrow x_0}\lim_{y\rightarrow y_0}f(x,y),\lim_{y\rightarrow y_0}\lim_{x\rightarrow x_0}f(x,y)\end{aligned}$ 存在但不相等，则 $\begin{aligned}\lim_{\begin{aligned}x\rightarrow x_0\\y\rightarrow y_0\end{aligned}}f(x,y)\end{aligned}$ 不存在
### 全增量与偏增量

若 $f(P)=f(x,y)$ 在点 $P(x_0,y_0)$ 的某邻域 $U(P_0)$ 内有意义，且 $\begin{aligned}\lim_{\begin{aligned}x\rightarrow x_0\\y\rightarrow y_0\end{aligned}}f(x,y)\end{aligned}=f(x_0,y_0)$ 则称函数 $f(P)$ 在点 $P_0(x_0,y_0)$ 处连续，记函数的全增量为
$$
\Delta z=f(x,y)-f(x_0,y_0)=f(x_0+\Delta x,y_0+\Delta y)-f(x_0,y_0)
$$
记函数对 $x$ 的偏增量为 $\Delta_xz=f(x,y_0)-f(x_0,y_0)=f(x_0+\Delta x,y_0)-f(x_0,y_0)$
记函数对 $y$ 的偏增量为 $\Delta_yz=f(x_0,y)-f(x_0,y_0)=f(x_0,y_0+\Delta y)-f(x_0,y_0)$
设 $f(P)=f(x,y)$ 在平面有界闭区间 $G$ 上连续，则 $f(P)$ 必在 $G$ 上取到最大值、最小值以及中间的一切值，闭区域上连续的二元函数的图形称为连续曲面
### 偏导数

设函数 $z=f(x,y)$ 在点 $P_0(x_0,y_0)$ 的某邻域内有定义，若极限 
$$
\begin{aligned}\lim_{\Delta x\rightarrow 0}\frac{\Delta_x z}{\Delta x}=\lim_{\Delta x\rightarrow 0}\frac{f(x_0+\Delta x,y_0)-f(x_0,y_0)}{\Delta x}=\lim_{x\rightarrow x_0}\frac{f(x,y_0)-f(x_0,y_0)}{x-x_0}\end{aligned}
$$
存在，则称该极限为函数 $z=f(x,y)$ 在 $P_0(x_0,y_0)$ 处关于 $x$ 的偏导数，记为
$$\begin{aligned}f'_x(x_0,y_0)=\frac{d}{dx}f(x_0,y_0)\quad或\quad\frac{\partial z}{\partial x}\Big{|}_{\begin{aligned}x=x_0\\y=y_0\end{aligned}}\quad或\quad z'_x\Big{|}_{\begin{aligned}x=x_0\\y=y_0\end{aligned}}\quad或\quad\frac{\partial}{\partial x}f(x,y)\Big{|}_{\begin{aligned}x=x_0\\y=y_0\end{aligned}}\end{aligned}$$ 
求解 $f'_x(x_0,y_0)$ 有三种方法：定义、求偏导再带入、带入已知量再求导

若函数 $z=f(x,y)$ 的二阶偏导数 $f''_{xy}(x,y),f''_{yx}(x,y)$ 都在点 $P_0(x_0,y_0)$ 处连续，则二者相等
对在一点存在直到 $m$ 阶连续偏导数的 $n$ 元函数，在该点的 $k(\leq m)$ 阶混合偏导数与求偏导数的顺序无关
### 全微分

若二元函数 $z=f(x,y)$ 在点 $(x,y)$ 处的全增量 $\Delta z=f(x+\Delta x,y+\Delta y)-f(x,y)$ 可以表示为 $\Delta z=A\Delta x+B\Delta y+o(\rho)(\rho=\sqrt{(\Delta x)^2+(\Delta y)^2}\rightarrow 0)$ 其中 $A,B$ 与变量 $x,y$ 的增量 $\Delta x,\Delta y$ 无关，而仅与 $x,y$ 有关，则称函数 $f(x,y)$ 在点 $(x,y)$ 处可微，其中 $A\Delta x+B\Delta y$ 称为函数 $f(x,y)$ 在点 $(x,y)$ 处的全微分，记作 $\mathrm{d}z=A\Delta x+B\Delta y$

若 $z=f(x,y)$ 在点 $(x,y)$ 处可微，则 $f(x,y)$ 在点 $(x,y)$ 处连续，由 $z=f(x,y)$ 在点 $(x,y)$ 处可微，有 $\Delta z=A\Delta x+B\Delta y+o(\rho)(\rho\rightarrow 0)$ 其中 $A,B$ 是与 $\Delta x,\Delta y$ 无关的常数， $\begin{aligned}\lim_{\begin{aligned}\Delta x\rightarrow 0\\\Delta y\rightarrow 0\end{aligned}}\Delta z=\lim_{\begin{aligned}\Delta x\rightarrow 0\\\Delta y\rightarrow 0\end{aligned}}(A\Delta x+B\Delta y+o(\rho))=0\end{aligned}$ 所以 $z=f(x,y)$ 在点 $(x,y)$ 处连续

若 $z=f(x,y)$ 在点 $(x,y)$ 处可微，则 $z=f(x,y)$ 在点 $(x,y)$ 处的两个偏导数 $f_x'(x,y),f_y'(x,y)$ 都存在，且 $A=f_x'(x,y),B=f_y'(x,y)$，多元函数连续不一定可微
### 多元函数的可微性

偏导数即使都存在，原函数也不一定可微，验证多元函数不可微的方法：
* 若 $f(x,y)$ 在 $(x,y)$ 处不连续，则 $f(x,y)$ 在点 $(x,y)$ 处不可微
* 若 $f(x,y)$ 在 $(x,y)$ 处至少有一个偏导数不存在，则 $f(x,y)$ 在点 $(x,y)$ 处不可微
* 若 $f(x,y)$ 在 $(x,y)$ 处的两个偏导数都存在，但极限 $\begin{aligned}\lim_{\begin{aligned}\Delta x\rightarrow 0\\\Delta y\rightarrow 0\end{aligned}}\frac{\Delta z-(A\Delta x+B\Delta y)}{\rho}\end{aligned}$ 不存在或极限存在但不为零，则 $f(x,y)$ 在 $(x,y)$ 处不可微

可微的充分条件：若函数 $z=f(x,y)$ 的偏导数 $f'_x(x,y),f'_y(x,y)$ 在点 $(x_0,y_0)$ 处连续，则函数 $z=f(x,y)$ 在点 $(x_0,y_0)$ 处可微

函数 $z=f(x,y)$ 在点 $(x_0,y_0)$ 处可微而两偏导数在该点不连续的情况
$$\begin{align}(x^2+y^2)\sin\frac{1}{x^2+y^2}\end{align}$$
全增量公式：$\Delta z=f_x'(x_0,y_0)\Delta x+f_y'(x_0,y_0)\Delta y+\varepsilon_1\Delta x+\varepsilon_2\Delta y$ 其中 $\begin{aligned}\lim_{\begin{aligned}\Delta x\rightarrow 0\\\Delta y\rightarrow 0\end{aligned}}\varepsilon_1=\lim_{\begin{aligned}\Delta x\rightarrow 0\\\Delta y\rightarrow 0\end{aligned}}\varepsilon_2=0\end{aligned}$ 
近似估算：$f(x+\Delta x,y+\Delta y)\approx f(x,y)+f_x'(x,y)\Delta x+f_y'(x,y)\Delta y$
### 复合函数的偏导数

若函数 $u=\varphi(x,y),v=\psi(x,y)$ 在点 $(x,y)$ 处的偏导数都存在，$z=f(u,v)$ 在点 $(u,v)=(\varphi(x,y),\psi(x,y))$ 处可微，则复合函数 $z=f[\varphi(x,y),\psi(x,y)]$ 在点 $(x,y)$ 处的偏导数存在，并有求偏导公式：
$$\begin{aligned}\frac{\partial z}{\partial x}=\frac{\partial z}{\partial u}\cdot\frac{\partial u}{\partial x}+\frac{\partial z}{\partial v}\cdot\frac{\partial v}{\partial x},\quad\frac{\partial z}{\partial y}=\frac{\partial z}{\partial u}\cdot\frac{\partial u}{\partial y}+\frac{\partial z}{\partial v}\cdot\frac{\partial v}{\partial y}\end{aligned}$$
特别地，若 $z=f(u,v),u=\varphi(x),v=\psi(x)$ ，即 $z$ 是一个自变量 $x$ 的复合函数，则有 $\begin{aligned}\frac{dz}{dx}=\frac{\partial z}{\partial u}\cdot\frac{du}{dx}+\frac{\partial z}{\partial v}\cdot\frac{dv}{dx}\end{aligned}$ ，这里 $\begin{aligned}\frac{dz}{dx}\end{aligned}$ 称为全导数 
### 复合函数的全微分

设 $z=f(x,y),x,y$ 是自变量，且 $z=f(x,y)$ 可微，则其全微分为 $\begin{aligned}dz=\frac{\partial z}{\partial x}dx+\frac{\partial z}{\partial y}dy\end{aligned}$

若设 $z=f(x,y),x=x(s,t),y=y(s,t)$ 都具有连续的偏导数，则复合函数 $z=f(x(s,t),y(s,t))$ 具有连续的偏导数 $\begin{aligned}dz=\frac{\partial z}{\partial s}ds+\frac{\partial z}{\partial t}dt\end{aligned}$ 

虽然 $x,y$ 不是自变量，但全微分的形式与 $x,y$ 是自变量时是一样的，称为全微分的一阶微分形式不变性，即若 $z=z(u,v)$ 可微，且 $dz=\varphi(u,v)du+\psi(u,v)dv$ ，则有
$$\begin{aligned}\frac{\partial z}{\partial u}=\varphi(u,v),\quad \frac{\partial z}{\partial v}=\psi(u,v)\end{aligned}$$

考虑多元函数 $z=f(x,y)$ 的二阶微分，当 $x$ 和 $y$ 是自变量时，二阶微分为
$$\begin{aligned}d^2z=\frac{\partial^2z}{\partial x^2}(dx)^2+2\frac{\partial^2z}{\partial x\partial y}dxdy+\frac{\partial^2 z}{\partial y^2}(dy)^2\end{aligned}$$

当 $x$ 和 $y$ 是中间变量时，如 $x=x(u,v),y=y(u,v)$ ，计算二阶微分为
$$\begin{aligned}d^2z=\frac{\partial^2z}{\partial x^2}(dx)^2+2\frac{\partial^2z}{\partial x\partial y}dxdy+\frac{\partial^2 z}{\partial y^2}(dy)^2+\frac{\partial z}{\partial x}d^2x+\frac{\partial z}{\partial y}d^2y\end{aligned}$$
其中的额外项是因为中间变量二阶微分不为 $0$ 导致的
高阶微分在变量替换时会产生与中间变量二阶微分相关的额外项，导致形式改变
### 隐函数的偏导数

设 $F(x,y,z)$ 在 $P_0(x_0,y_0,z_0)$ 的某一邻域内具有连续的偏导数，且 $F(x_0,y_0,z_0)=0,F'_x(x_0,y_0,z_0)\neq0$ ，则方程 $F(x,y,z)=0$ 在 $P_0(x_0,y_0,z_0)$ 的某一邻域内能唯一确定一个连续且具有连续偏导数的函数 $z=f(x,y)$ ,满足 $z_0=f(x_0,y_0)$ 并有 $$\begin{aligned}\frac{\partial z}{\partial x}=-\frac{F_x'}{F_z'},\quad \frac{\partial z}{\partial y}=-\frac{F_y'}{F_z'}\end{aligned}$$
### 隐函数组的偏导数

设方程组 $\begin{cases}F(x,y,u,v)=0\\G(x,y,u,v)=0\end{cases}$ 确定隐函数组 $u=u(x,y),v=v(x,y)$ ，即 $F(x,y,u(x,y),v(x,y))\equiv0\quad G(x,y,u(x,y),v(x,y))\equiv0$ ，有定理：

设 $F(x,y,u,v)=0,G(x,y,u,v)=0$ 在点 $P_0(x_0,y_0,u_0,v_0)$ 的某邻域内具有对各个变量的连续偏导数，又 $F(x_0,y_0,u_0,v_0)=G(x_0,y_0,u_0,v_0)=0$ ，且偏导数所组成的函数行列式
$$J=\begin{aligned}\frac{\partial(F,G)}{\partial(u,v)}\end{aligned}=\begin{vmatrix}\begin{aligned}\frac{\partial F}{\partial u}&\frac{\partial F}{\partial v}\\\frac{\partial G}{\partial u}&\frac{\partial G}{\partial v}\end{aligned}\end{vmatrix}$$
在点 $P_0(x_0,y_0,u_0,v_0)$ 不为零，则方程组 $\begin{cases}F(x,y,u,v)=0\\G(x,y,u,v)=0\end{cases}$ 在点 $P_0(x_0,y_0,u_0,v_0)$ 的某一邻域内恒能唯一确定一组连续且具有连续偏导数的函数组 $u=(x,y),v=v(x,y)$ ，它们满足条件 $u_0=u(x_0,y_0),v_0=v(x_0,y_0)$ ，并有
$$\begin{aligned}\frac{\partial u}{\partial x}=-\frac{1}{J}\frac{\partial(F,G)}{\partial(x,v)}=-\frac{\begin{vmatrix}F_x'&F_v'\\G_x'&G_v'\end{vmatrix}}{\begin{vmatrix}F_u'&F_v'\\G_u'&G_v'\end{vmatrix}}\quad\frac{\partial v}{\partial x}=-\frac{1}{J}\frac{\partial(F,G)}{\partial(u,x)}=-\frac{\begin{vmatrix}F_u'&F_x'\\G_u'&G_x'\end{vmatrix}}{\begin{vmatrix}F_u'&F_v'\\G_u'&G_v'\end{vmatrix}}\\
\frac{\partial u}{\partial y}=-\frac{1}{J}\frac{\partial(F,G)}{\partial(y,v)}=-\frac{\begin{vmatrix}F_y'&F_v'\\G_y'&G_v'\end{vmatrix}}{\begin{vmatrix}F_u'&F_v'\\G_u'&G_v'\end{vmatrix}}\quad\frac{\partial v}{\partial y}=-\frac{1}{J}\frac{\partial(F,G)}{\partial(u,y)}=-\frac{\begin{vmatrix}F_u'&F_y'\\G_u'&G_y'\end{vmatrix}}{\begin{vmatrix}F_u'&F_v'\\G_u'&G_v'\end{vmatrix}}\end{aligned}$$
### 场的方向导数与梯度

根据场中的物理量的数量和矢量之分将场分为数量场和矢量场两类
格局场中的物理量是否随时间而变化将场分为稳定场和不稳定场
数量场可以用点 $P(x,y,z)$ 的数量函数 $u=u(P)$ 或 $u=u(x,y,z),P(x,y,z)\in V$ 表示
矢量场可以用电 $P(x,y,z)$ 的矢量函数 $A=A(P)$ 或 $A=A_x(P)i+A_y(P)j+A_z(P)k$ 表示

若函数 $u$ 在点 $P_0(x_0,y_0,z_0)$ 处可微，则 $u$ 在点 $P_0$ 处沿任一方向 $l$ 的方向导数都存在，且
$$
\frac{\partial u}{\partial l}\Big{|}_{P_0}=
\frac{\partial u}{\partial x}\Big{|}_{P_0}\cos\alpha+
\frac{\partial u}{\partial y}\Big{|}_{P_0}\cos\beta+
\frac{\partial u}{\partial z}\Big{|}_{P_0}\cos\gamma
$$
函数 $u(P)$ 在 $P$ 处的梯度为矢量
$$
\mathrm{grad}\,u=
\frac{\partial u}{\partial x}i+
\frac{\partial u}{\partial y}j+
\frac{\partial u}{\partial z}k
$$
当 $u$ 在点 $P_0$ 处可微时，$u$ 在点 $P_0$ 的梯度方向是 $u$ 值增长最快的方向
### 梯度运算的性质

设 $u,v$ 可微，$\alpha,\beta$ 为常数，则梯度运算具有如下性质
（1） $\mathrm{grad}\,(\alpha u+\beta v)=\alpha\mathrm{grad}\, u+\beta\mathrm{grad}\, v$
（2） $\mathrm{grad}\,(u\cdot v)=u\mathrm{grad}\, v+v\mathrm{grad}\, u$
（3） $\mathrm{grad}\, f(u)=f'(u)\mathrm{grad}\,u$
### 多元函数泰勒公式

若函数 $f$ 在点 $P_0(x_0,y_0)$ 的某邻域 $U(P_0)$ 内有直到 $n+1$ 阶连续偏导数，则对于 $U(P_0)$ 内任一点 $(x_0+h,y_0+k)$，存在 $\theta\in(0,1)$ ，使得
$$
\begin{align}
f(x_0+h,y_0+k)&=f(x_0,y_0)+
(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y})f(x_0,y_0)\\
&+\frac{1}{2!}
(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y})^2f(x_0,y_0)\\
&+\cdots\\
&+\frac{1}{n!}
(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y})^nf(x_0,y_0)\\
&+\frac{1}{(n+1)!}
(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y})^{n+1}
f(x_0+\theta h,y_0+\theta k)
\end{align}
$$
### 极值的必要条件

若函数 $f$ 在点 $P_0(x_0,y_0)$ 存在偏导数且在 $P_0$ 处取极值，则有
$$
f_x'(x_0,y_0)=0,f_y'(x_0,y_0)=0
$$
点 $P_0$ 满足上式则称为 $f$ 的稳定点或驻点
### 极值的充分条件

设函数 $z=f(x,y)$ 在点 $P_0(x_0,y_0)$ 的某邻域 $U(P_0)$ 内连续，且有连续偏导数，如果 $f_x'(x_0,y_0)=0,f_y'(x_0,y_0)=0$ ，设 $A=f_{xx}''(x_0,y_0),B=f_{xy}''(x_0,y_0),C=f_{yy}''(x_0,y_0)$ ，则
（1）当 $B^2-AC<0$ 时，$f(x_0,y_0)$ 一定为极值，且 $A>0$ 时为极小值，$A<0$ 时为极大值
（2）当 $B^2-AC>0$ 时，$f(x_0,y_0)$ 不是极值
（3）当 $B^2-AC=0$ 时，不能确定 $f(x_0,y_0)$ 是否为极值
### 空间曲线的法平面

过点 $P_0$ 且与该直线垂直的平面称为在 $P_0$ 处的法平面，法平面方程为
$$
x'(t_0)(x-x_0)+y'(t_0)(y-y_0)+z'(t_0)(z-z_0)=0
$$
### 空间曲面的切平面

过点 $M_0$ 且与该平面相切的平面称为在 $M_0$ 处的切平面，切平面方程为
$$
F_x'(x_0,y_0,z_0)(x-x_0)+F_y'(x_0,y_0,z_0)(y-y_0)+F_z'(x_0,y_0,z_0)(z-z_0)=0
$$