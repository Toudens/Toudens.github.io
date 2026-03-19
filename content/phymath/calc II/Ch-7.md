---
title: Ch-7 空间曲面方程
date: 2026-03-19
weight: "1"
type: docs
---
### 矢量的矢量积

$a\times b=\begin{vmatrix}a_2&a_3\\b_2&b_3\end{vmatrix}i-\begin{vmatrix}a_1&a_3\\b_1&b_3\end{vmatrix}j+\begin{vmatrix}a_1&a_2\\b_1&b_2\end{vmatrix}k=\begin{vmatrix}i&j&k\\a_1&a_2&a_3\\b_1&b_2&b_2\end{vmatrix}$
矢量积所得的矢量垂直于 $a,b$ 构成的平面
### 矢量的混合积

$a\cdot(b\times c)=\begin{vmatrix}a_1&a_2&a_3\\b_1&b_2&b_3\\c_1&c_2&c_3\end{vmatrix}$
### 三矢量的二重矢积

$a\times(b\times c)=(a\cdot c)b-(a\cdot b)c$
### 平面的方程表示

任何平面都可用关于 $x,y,z$ 的一次方程 $Ax+By+Cz+D=0$ （其中 $A,B,C$ 不全为零）来表示，而 $Ax+By+Cz+D=0$ 表示一张以 $f=Ai+Bj+Ck$ 为法矢量的平面
### 直线的方程表示


| 表示方式  | 方程                                                                                              |
| ----- | ----------------------------------------------------------------------------------------------- |
| 点向式方程 | $\begin{aligned}\frac{x-x_0}{l}=\frac{y-y_0}{m}=\frac{z-z_0}{n}\end{aligned}$                   |
| 参数式方程 | $\begin{cases}x=x_0+lt\\y=y_0+mt\\z=z_0+nt\end{cases}$                                          |
| 两点式方程 | $\begin{aligned}\frac{x-x_1}{x_2-x_1}=\frac{y-y_1}{y_2-y_1}=\frac{z-z_1}{z_2-z_1}\end{aligned}$ |
| 一般式方程 | $\begin{cases}A_1x+B_1y+C_1z+D_1=0\\A_2x+B_2y+C_2z+D_2=0\end{cases}$                            |

直线一般式方程的方向矢量为 $\begin{vmatrix}i&j&k\\A_1&B_1&C_1\\A_2&B_2&C_2\end{vmatrix}$

直线的方向矢量为 $v=li+mj+nk$

过点 $P$ 作与直线垂直的平面方程为 $l(x-x_1)+m(y-y_1)+n(z-z_1)=0$
### 平面束方程

记直线 $L$ 的一般式方程为 $L:\begin{cases}\pi_1:A_1x+B_1y+C_1z+D_1=0\\\pi_2:A_2x+B_2y+C_2z+D_2=0\end{cases}$
设 $\lambda,\mu$ 为不同时为零的任意实数，则 $$\lambda(A_1x+B_1y+C_1z+D_1)+\mu(A_2x+B_2y+C_2z+D_2)=0$$就表示以 $L$ 为轴的平面束方程
### 曲面方程

在空间直角坐标系中，如果某个曲面上任意点的坐标都满足方程 $F(x,y,z)=0$ ，而不在该曲面上的任何点的坐标都不满足该方程，则方程 $F(x,y,z)=0$ 称为该曲面方程

球面方程：$(x-x_0)^2+(y-y_0)^2+(z-z_0)^2=R^2$
### 柱面方程

一条动直线 $L$ 沿一定曲线 $\Gamma$ 平行移动所成的曲面称为柱面，并称动直线 $L$ 为该柱面的母线，称定曲线 $\Gamma$ 为该柱面的准线

以 $Oxy$ 平面的曲线 $\Gamma:F(x,y)$ 为准线，母线 $L$ 的方向矢量为 $v=ai+bj+ck,(c\neq 0)$ 的柱面方程为 $\begin{aligned}F(x-\frac{a}{c}z,y-\frac{b}{c}z)=0\end{aligned}$

由平行于 $Oz$ 轴的直线沿曲线 $\Gamma$ 平行移动所生成的曲面称为母线平行于 $Oz$ 轴的柱面
### 锥面方程

过空间一定点 $O$ 的动直线 $L$ ，沿空间曲线 $\Gamma$（不过定点 $O$ ）移动所生成的曲线称为锥面，其中动直线 $L$ 称为该锥面的母线，曲线 $\Gamma$ 称为该锥面的准线，$O$ 称为该锥面的顶点
锥面的准线取平面曲线，以 $z=h,(h\neq0)$ 平面上的曲线 $\Gamma:F(x,y)=0$ 为准线，以原点为顶点的锥面方程为 $\begin{aligned}F(\frac{h}{z}x,\frac{h}{z}y)=0\end{aligned}$ 
### 旋转曲面方程

一曲线 $\Gamma$ 绕一定直线 $L$ 旋转而生成的曲面叫做旋转曲面，其中定直线 $L$ 称为旋转曲面的轴
设 $\Gamma$ 为 $Oyz$ 平面上的曲线，其方程为 $F(y,z)=0$ ，将该曲线绕 $Oz$ 旋转，就得到一个以 $Oz$ 轴为轴的旋转曲面，其方程为 $F(\pm\sqrt{x^2+y^2},z)=0$
### 空间曲线方程

任意空间曲线总可以看成两曲面的交线，设 $F(x,y,z)=0,G(x,y,z)=0$ 表示两曲面的方程，它们相交，且交线是曲线 $\Gamma$ ，则 $\Gamma:\begin{cases}F(x,y,z)=0\\G(x,y,z)=0\end{cases}$
空间曲线也可用参数方程来表示，其一般形式是$\begin{cases}x=\varphi(t)\\y=\psi(t)\\z=\omega(t)\end{cases}$
将 $\Gamma:\begin{cases}F(x,y,z)=0\\G(x,y,z)=0\end{cases}$ 方程中消去一个变量，得到的就是对应轴的投影柱面
### 空间曲线在坐标平面上的投影

空间曲线 $\Gamma$ 可以用方程组 $\begin{cases}F_1(x,y,z)=0\\F_2(x,y,z)=0\end{cases}$ 表示，将方程组中消去一个变量，以 $z$ 为例，得到方程 $F(x,y)=0$ ，表示一个母线平行于 $Oz$ 轴的柱面，所以该柱面必定包含曲线 $\Gamma$ ,过曲线 $\Gamma$ 上的一切点所作的平行于 $Oz$ 轴的所有直线都在该柱面上，该柱面称为投影柱面，投影柱面与 $Oxy$ 平面的交线叫空间曲线 $\Gamma$ 在 $Oxy$ 平面上的投影曲线，简称投影
### 二次曲面
| 曲面方程                                                                                         | 曲面类型      |
| -------------------------------------------------------------------------------------------- | --------- |
| $\begin{aligned}\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1(a>0,b>0,c>0)\end{aligned}$ | 椭球面       |
| $\begin{aligned}z=\frac{x^2}{a^2}+\frac{y^2}{b^2}(a>0,b>0)\end{aligned}$                     | 椭圆抛物面     |
| $\begin{aligned}\frac{x^2}{a^2}+\frac{y^2}{b^2}-\frac{z^2}{c^2}=0\end{aligned}$              | 二次锥面      |
| $\begin{aligned}z=-\frac{x^2}{a^2}+\frac{y^2}{b^2}\end{aligned}$                             | 双曲抛物面、马鞍面 |
| $\begin{aligned}\frac{x^2}{a^2}+\frac{y^2}{b^2}-\frac{z^2}{c^2}=1\end{aligned}$              | 单叶双曲面     |
| $\begin{aligned}\frac{x^2}{a^2}+\frac{y^2}{b^2}-\frac{z^2}{c^2}=-1\end{aligned}$             | 双叶双曲面     |
