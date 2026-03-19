---
title: Ch-9 多元函数积分学
type: docs
weight: "3"
date: 2026-03-19
---
### 二重积分的定义

设二元函数 $f(P)=f(x,y)$ 在平面有界闭区域 $\sigma$ 上有界，将 $\sigma$ 分成 $n$ 个小闭区域
$$
\Delta\sigma_1,\Delta\sigma_2,\cdots,\Delta\sigma_n
$$
在每个 $\Delta\sigma_i$ 上任意取一点 $(\xi_i,\eta_i)$ ，如果当各个小闭区域的直径中的最大值趋于零时下式右侧极限存在，则称此极限为函数 $f(x,y,z)$ 在 $\sigma$ 上的二重积分
$$
\iint_\sigma f(x,y)d\sigma=\lim_{\lambda\rightarrow0}\sum_{i=1}^nf(\xi_i,\eta_i)\Delta\sigma_i
$$
若 $f(x,y)$ 在有界闭区域 $\sigma$ 上连续，则 $f(x,y)$ 在 $\sigma$ 上可积
### 二重积分的性质

**性质 1**
$$
\iint_\sigma[f(x,y)\pm g(x,y)]d\sigma=
\iint_\sigma f(x,y)d\sigma\pm
\iint_\sigma g(x,y)d\sigma
$$
**性质 2**
$$
\iint_\sigma kf(x,y)d\sigma=k\iint_\sigma f(x,y)d\sigma
$$
**性质 3**
$$
\iint_\sigma1d\sigma=\iint_\sigma d\sigma=\sigma
$$
**性质 4**  若 $\sigma$ 可分解为两个不共内点的区域 $\sigma_1,\sigma_2$ ，记作 $\sigma=\sigma_1+\sigma_2$ ，则有
$$
\iint_\sigma f(x,y)d\sigma=\iint_{\sigma_1}f(x,y)d\sigma+\iint_{\sigma_2}f(x,y)d\sigma
$$
**性质 5** 若 $\begin{align}\iint_\sigma f(x,y)d\sigma\end{align}$ 存在，$f(x,y)\geq0$ ，则 $\begin{align}\iint_\sigma f(x,y)d\sigma\geq 0\end{align}$ 

**性质 6** 若 $\begin{align}f(x,y)\geq 0,f(x,y)\not\equiv0,(x,y)\in\sigma\end{align}$ 且 $f(x,y)$ 连续，则$\begin{align}\iint_\sigma f(x,y)d\sigma>0\end{align}$

**性质 7**
$$
\Big{|}\iint_\sigma f(x,y)d\sigma\Big{|}\leq\iint_\sigma|f(x,y)|d\sigma
$$
**性质 8** 若 $f(x,y)$ 在有界闭区域 $\sigma$ 上连续，则在 $\sigma$ 上至少存在一点 $P(x^*,y^*)$ 使得
$$
\iint_\sigma f(x,y)d\sigma=f(x^*,y^*)\sigma
$$
### 直角坐标系二重积分

设积分区域为 $x$ 型区域 $\sigma=\{(x,y):\varphi_1(x)\leq y\leq\varphi_2(x),a\leq x\leq b\}$
$$
\begin{align}
\iint_\sigma f(x,y)d\sigma&=\int_a^bA(x)dx
=\int_a^b[\int_{\varphi_1(x)}^{\varphi_2(x)}f(x,y)dy]dx\\
&=\int_a^bdx\int_{\varphi_1(x)}^{\varphi_2(x)}f(x,y)dy
\end{align}
$$
### 极坐标系二重积分

通过坐标变换 $x=r\cos\theta,y=r\sin\theta$ 可以简化一些二重积分的计算
$$
\begin{align}
\iint_\sigma f(x,y)d\sigma&
=\iint f(r\cos\theta,r\sin\theta)rdrd\theta\\
&=\int_{\alpha}^\beta d\theta\int_{r_1(\theta)}^{r_2(\theta)}
f(r\cos\theta,r\sin\theta)rdr
\end{align}
$$
### 一般曲线坐标二重积分

设有坐标变换函数组 $\begin{cases}x=x(u,v)\\y=y(u,v)\end{cases}$ 具有连续的偏导数，且有
$$
\frac{\partial(x,y)}{\partial(u,v)}=
\begin{vmatrix}
\frac{\partial x}{\partial u}&
\frac{\partial x}{\partial v}\\
\frac{\partial y}{\partial u}&
\frac{\partial y}{\partial v}
\end{vmatrix}
=r
$$
则有二重积分的一般换元公式
$$
\iint_\sigma f(x,y)d\sigma
=\iint_\sigma f(x(u,v),y(u,v))
\Big{|}
\frac{\partial(x,y)}{\partial(u,v)}
\Big{|}
dudv
$$

### 三重积分的定义

设 $f(x,y,z)$ 是空间有限闭区间 $V$ 上的有界函数，将 $V$ 任意分成 $n$ 个小闭区域
$$
\Delta V_1,\Delta V_2,\cdots,\Delta V_n
$$
在每个 $\Delta V_i$ 上任意取一点 $(\xi_i,\eta_i,\zeta_i)$ ，如果当各个小闭区域直径中的最大值 $\lambda$ 趋于零时下式右侧极限存在，则称此极限为函数 $f(x,y,z)$ 在 $V$ 上的三重积分
$$
\iiint_Vf(x,y,z)dV=\lim_{\lambda\rightarrow0}
\sum_{i=1}^nf(\xi_i,\eta_i,\zeta_i)\Delta V_i
$$
如果用平行于坐标面的平面划分 $V$ ，可把 $dV$ 记作 $dxdydz$ ，有
$$
\iiint_Vf(x,y,z)dxdydz
$$
其中 $dxdydz$ 称为直角坐标系中的体积元素
### 直角坐标系三重积分

**（1）投影法**
积分区域 $V$ 表示为 $V=\{(x,y,z):z_1(x,y)\leq z\leq z_2(x,y),(x,y)\in\sigma_{xy}\}$
$$
\begin{align}
M&=\iiint_Vf(x,y,z)dV=\iint_{\sigma xy}\mu(x,y)d\sigma\\
&=\iint_{\sigma xy}[\int_{z_1(x,y)}^{z_2(x,y)}f(x,y,z)dz]d\sigma\\
&=\iint_{\sigma xy}\int_{z_1(x,y)}^{z_2(x,y)}f(x,y,z)dz
\end{align}
$$
若 $\sigma_{xy}$ 为 $x$ 型区域，$\varphi_1(x)\leq y\leq\varphi_2(x),a\leq x\leq b$ ，则有
$$
\iiint_Vf(x,y,z)dV=\int_a^bdx
\int_{\varphi_1(x)}^{\varphi_2(x)}dy
\int_{z_1(x,y)}^{z_2(x,y)}
f(x,y,z)dz
$$

**（2）截面法**
设立体介于两平面 $z=c,z=d$ 之间，过 $(0,0,z),z\in[c,d]$ 作垂直于 $Oz$ 的平面与立体相截，截面区域为 $D_z$ ，只要能求 $[c,d]$ 上任意一 $z$ 处的线密度 $\mu(z)$ 即可求解 
$$
\begin{align}
\iiint_Vf(x,y,z)dV&=\int_c^d\mu(z)dz
=\int_c^d[\iint_{D_x}f(x,y,z)d\sigma]dz\\
&=\int_c^ddz\iint_{D_x}f(x,y,z)d\sigma
\end{align}
$$
若 $D_x$ 为 $x$ 型区域，$y_1(x,z)\leq y\leq y_2(x,z),x_1(z)\leq x\leq x_2(z)$ ，则有
$$
\iiint_Vf(x,y,z)dV=\int_c^ddz\int_{x_1(z)}^{x_2(z)}dx\int_{y_1(x,z)}^{y_2(x,z)}f(x,y,z)dy
$$
当 $f(x,y,z)$ 仅是 $z$ 的表达式，而 $D_z$ 的面积又容易计算时，记 $f(x,y,z)=g(z)$
$$
\begin{align}
\iiint_Vf(x,y,z)dV&=\iiint_Vg(z)dV=\int_c^ddz\iint_{D_z}g(z)dxdy\\
&=\int_c^dg(z)dz\int_{D_x}dxdy=\int_c^dg(z)S_{D_x}dz
\end{align}
$$
### 柱面坐标系三重积分

在计算三重积分 $\begin{align}\iiint_Vf(x,y,z)dV\end{align}$ 时，若 $f(x,y,z)$ 中含有 $x^2+y^2$ ， $V$ 在 $Oxy$ 平面上投影区域是圆域或圆域的一部分时可以进行柱面坐标变换
$$
x=r\cos\theta,\quad y=r\sin\theta,\quad z=z
$$
$$
\begin{align}
\iiint_Vf(x,y,z)dV
&=\iiint_Vf(r\cos\theta,r\sin\theta,z)rdrd\theta dz\\
&=\iint_{\sigma xy}rdrd\theta\int_{z_1(r,\theta)}^{z_2(r,\theta)}
f(r\cos\theta,r\sin\theta,z)dz\\
&=\int_\alpha^\beta d\theta
\int_{r_1(\theta)}^{r_2(\theta)}rdr
\int_{z_1(r\cos\theta,r\sin\theta)}^{z_2(r\cos\theta,r\sin\theta)}
f(r\cos\theta,r\sin\theta,z)dz
\end{align}
$$
### 球面坐标系三重积分

若三重积分被积函数中含有 $x^2+y^2+z^2$ ，可对这一类积分进行球面坐标变换
$$
\begin{cases}
x=r\cos\theta\\
y=r\sin\theta\\
z=z
\end{cases}
\quad
\begin{cases}
z=\rho\cos\varphi\\
r=\rho\sin\varphi\\
\theta=\theta
\end{cases}
\quad
\Rightarrow
\quad
\begin{cases}
x=\rho\sin\varphi\cos\theta\\
y=\rho\sin\varphi\sin\theta\\
z=\rho\cos\varphi
\end{cases}
$$
$$
\iiint_Vf(x,y,z)dV=\iiint_Vf(\rho\sin\varphi\cos\theta,\rho\sin\varphi\sin\theta,\rho\cos\varphi)\rho^2\sin\varphi d\rho d\varphi d\theta
$$
广义球坐标有 $dV=abc\rho^2\sin\varphi d\rho d\varphi d\theta$ 
### 三重积分的一般曲面坐标变换

求 $\begin{align}\iiint_Vf(x,y,z)dV\end{align}$ ，其中 $f(x,y,z)$ 连续，设变换：
$$
\begin{cases}
x=x(u,v,w)\\
y=y(u,v,w)\\
z=z(u,v,w)
\end{cases}
$$ 
均具有连续的偏导数，且有：
$$
|J|=
\begin{vmatrix}
\begin{align}
\frac{\partial(x,y,z)}{\partial(u,v,w)}
\end{align}
\end{vmatrix}
\neq 0
$$
则对应该一般的曲面坐标变换，有：
$$
\iiint_Vf(x,y,z)dV=
\iiint_Vf(x(u,v,w),y(u,v,w),z(u,v,w))
\begin{vmatrix}\begin{align}
\frac{\partial(x,y,z)}{\partial(u,v,w)}
\end{align}\end{vmatrix}
dudvdw
$$
### 第一类曲线积分

设函数 $f(P)$ 是定义 $A,B$ 为端点的光滑曲线 $\Gamma$ 上的有界函数，在 $\Gamma$ 上任取点
$$
A=M_0,M_1,M_2,\cdots,M_n=B
$$
将曲线分成 $n$ 个部分，记弧 $\overparen{M_{i-1}M_i}$ 的长度为 $\Delta s_i$ ，并取点 $P_i(\xi_i,\eta_i,\zeta_i)$ 
$$
\sum_{i=1}^nf(P_i)\Delta s_i
$$
记 $\lambda=\max\{\Delta s_i:1\leq i\leq n\}$ 当 $\lambda\rightarrow0$ 时，此极限的值与曲线分法和取点无关，则称此极限值为函数 $f(P)$ 沿曲线 $\Gamma$ 的第一类积分曲线
$$
\int_\Gamma f(P)ds=\lim_{\lambda\rightarrow 0}\sum_{i=1}^nf(P_i)\Delta s_i
$$
$$
\int_{\Gamma}f(x,y,z)ds=\int_\alpha^\beta f(x(t),y(t),z(t))
\sqrt{x'^2(t)+y'^2(t)+z'^2(t)}dt
$$
$$
\begin{align}
\int_\Gamma f(x,y)ds
&=\int_\alpha^\beta f(x(t),y(t))\sqrt{x'^2(t)+y'^2(t)}dt\\
&=\int_a^bf(x,\varphi(x))\sqrt{1+\varphi'^2(x)}dx\\
&=\int_c^df(\phi(y),y)\sqrt{1+\phi'^2(y)}dy\\
&=\int_\alpha^\beta f(r\cos\theta,r\sin\theta)\sqrt{r^2(\theta)+r'^2(\theta)}d\theta
\end{align}
$$
### 第一类曲面积分

设 $f(P)=f(x,y,z)$ 是定义在有界光滑曲面 $S$ 上的有界函数，用曲线网将 $S$ 任意分成 $n$ 部分 $\Delta S_1,\Delta S_2,\cdots,\Delta S_n$ ，仍用其表示面积，在 $\Delta S_i$ 上取点 $P_i(\xi_i,\eta_i,\zeta_i)$ 
$$
\sum_{i=1}^nf(P_i)\Delta S_i
$$
以 $\lambda$ 表示 $\Delta S_i$ 直径中的最大者，当 $\lambda\rightarrow 0$ 时，若和式极限存在，且此极限值与曲面的分法以及 $P_i$ 的取法无关，则称其为函数 $f(P)$ 沿曲面 $S$ 的第一类曲面积分
$$
\iint_Sf(P)dS=\lim_{\lambda\rightarrow0}\sum_{i=1}^nf(P_i)\Delta S_i
$$
$$
\begin{align}
\iint_Sf(x,y,z)dS=\iint_{\sigma_{yz}}f(x(y,z),y,z)
\sqrt{1+(\frac{\partial x}{\partial y})^2+
(\frac{\partial x}{\partial z})^2}d\sigma\\
\iint_Sf(x,y,z)dS=\iint_{\sigma_{zx}}f(x,y(x,z),z)
\sqrt{1+(\frac{\partial y}{\partial x})^2+
(\frac{\partial y}{\partial z})^2}d\sigma\\
\iint_Sf(x,y,z)dS=\iint_{\sigma_{xy}}f(x,y,z(x,y))
\sqrt{1+(\frac{\partial z}{\partial x})^2+
(\frac{\partial z}{\partial y})^2}d\sigma
\end{align}
$$
若曲面 $S$ 由方程 $F(x,y,z)=0$ 给出，且确定隐函数 $z=z(x,y),(x,y)\in\sigma_{xy}$ ，并且有 $\begin{align}\frac{\partial z}{\partial x}=-\frac{F_x'}{F_z'},\frac{\partial z}{\partial y}=-\frac{F_y'}{F_z'}\end{align}$ 连续，则有
$$
\iint_sf(x,y,z)dS=\iint_{\sigma_{xy}}f(x,y,z(x,y))\frac{\sqrt{F_x'^2+F_y'^2+F_z'^2}}{|F_z'|}d\sigma
$$