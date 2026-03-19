---
title: Ch-6 机械波
date: 2026-03-19
type: docs
---
### 纵波与横波

当机械波在某媒质中进行传播时，媒质中各质点只在平衡位置附近作振动。
质点振动方向与波的传播方向垂直的波称为 **横波**。
质点振动方向与波的传播方向平行的波称为 **纵波**。
### 一维波的一般表达式

假设函数 $f$ 描述波的形状，波的传播速度为 $u$ ，在坐标 $x$ 处的波形可以表示为：
$$
y(x,0)=f(x),\quad y(x,t)=f(x-ut)
$$
### 平面简谐波的波函数
$$
\begin{align}
&y(x,t)=A\cos\omega(t-\frac{x}{u})\\
&v=-A\omega\sin\omega(t-\frac{x}{u})\\
\end{align}
$$
### 一维波的波动微分方程

讨论平面简谐波满足的微分方程，令 $\begin{align}y(x,t)=A\cos\omega(t-\frac{x}{u})\end{align}$ ，则有：
$$
\begin{cases}
\begin{align}
&\frac{\partial^2y}{\partial x^2}=
-(\frac{\omega}{u})^2A\cos\omega(t-\frac{x}{u})\\
&\frac{\partial^2y}{\partial t^2}=
-\omega^2A\cos\omega(t-\frac{x}{u})
\end{align}
\end{cases}
\Rightarrow
\frac{\partial^2y}{\partial x^2}=
\frac{1}{u^2}\frac{\partial^2y}{\partial t^2}
$$
假设绳上张力为 $F$ ，绳的线密度为 $\mu$ ，在一小段绳上分析，有：
$$
\begin{align}
\sum F_y
&=F(\sin\theta_2-\sin\theta_1)\\
&=F(\tan\theta_2-\tan\theta_1)\\
&=F[(\frac{\partial y}{\partial x})_2-(\frac{\partial y}{\partial x})_1]\\
&\approx F\frac{\partial^2 y}{\partial x^2}\Delta x\\
\end{align}
$$
$$
\begin{align}
&\sum F_y=ma_y
\Rightarrow
F\frac{\partial^2 y}{\partial x^2}\Delta x
=\mu\Delta x\frac{\partial^2y}{\partial t^2}\\
&\Rightarrow\frac{\partial^2y}{\partial x^2}=\frac{\mu}{F}\frac{\partial^2 y}{\partial t^2}
\end{align}
$$
由此可以得到绳上横波的传播速度为 $\begin{align}u=\sqrt{\frac{F}{\mu}}\end{align}$。
在棒中纵波的传播速度为 $\begin{align}u=\sqrt{\frac{Y}{\rho}}\end{align}$ 其中 $Y$ 为杨氏模量，反应棒的弹性。
杨氏模量的定义为 $\begin{align}Y=\frac{(\frac{F}{s})}{\frac{\Delta l}{l_0}}\end{align}$ ，其中 $\begin{align}\frac{F}{s}\end{align}$ 表示应力， $\begin{align}\frac{\Delta l}{l_0}\end{align}$ 表示应变。
### 波的能量

线元在 $y$ 方向的振动速度为 $\begin{align}v=\frac{\partial y}{\partial t}\end{align}$ ，其动能为：
$$
\Delta E_k=\frac{1}{2}\Delta mv^2=\frac{1}{2}\mu\Delta x(\frac{\partial y}{\partial t})^2
$$
线元的伸长量为 $\delta l=\sqrt{\Delta x^2+\Delta y^2}-\Delta x$ ，在小位移下近似：
$$
\Delta E_p=F\delta l=F[\sqrt{\Delta x^2+\Delta y^2}-\Delta x]
\approx F\cdot\frac{1}{2}(\frac{\partial y}{\partial x})^2\Delta x
$$
将 $y$ 分别对 $t$ 和 $x$ 求一阶偏导，并代入 $F=\mu u^2$：
$$
E=\mu A^2\omega^2\sin^2\omega(t-\frac{x}{u})\Delta x
$$
线能量密度的平均值为：
$$
\overline{(\frac{\Delta E}{\Delta x})}=\mu A^2\omega^2\overline{[\sin\omega(t-\frac{x}{u})]^2}=\frac{1}{2}\mu A^2\omega^2
$$
如果为三维空间，引入体密度 $\rho$ ，则 $\begin{align}\overline{\omega}=\frac{1}{2}\rho A^2\omega^2\end{align}$。
### 能流密度

简谐波所传递的功率为：
$$
\begin{align}
&P=u\mu A^2\omega^2\sin^2\omega(t-\frac{x}{u})\\
&\overline{P}=\frac{1}{2}u\mu A^2\omega^2
\end{align}
$$
平均能流密度等于平均能量密度与波速的乘积：
$$
I=\overline{\omega}u=\frac{1}{2}\rho A^2\omega^2u
$$
取离波源单位距离处的振幅为 $A_0$ ,则距离波源任一 $r$ 处的振幅为 $\begin{align}A=\frac{A_0}{r}\end{align}$。
### 叠加原理

任一处质点的振动是各个波单独在该点产生的振动的合成。

### 驻波

当两列振幅相等，沿相反方向传播的相干波叠加时将形成驻波，其表达式为：
$$
\begin{align}
&y_1=A\cos(\omega t-\frac{2\pi}{\lambda}x)\\
&y_2=A\cos(\omega t+\frac{2\pi}{\lambda}x)\\
&y=y_1+y_2=2A\cos\frac{2\pi}{\lambda}x\cos\omega t
\end{align}
$$
其中 $x=k\frac{\lambda}{2}$ 处合振幅最大，这些点称为波腹，$x=(2k+1)\frac{\lambda}{4}$ 处最小，称为波节
在相邻波节之间动能和势能的总和保持不变，为 $\frac{1}{2}\mu A^2\omega^2\lambda$。

反射波与入射波叠加的合振动为零，入射波在反射时有 $\pi$ 的突变，称为半波损失。

对于两端固定的绳子，只有特定频率的驻波可以存在，即 $\begin{align}\lambda_n=\frac{4L}{n},n=2,4,6,\cdots\end{align}$。
对于一端可自由移动的绳子，同理，有 $\begin{align}\lambda_n=\frac{4L}{n},n=1,3,5,\cdots\end{align}$。
### 多普勒效应

**（1）波源相对媒质静止，观察者以 $v_R$ 向波源运动**

若波长为 $\lambda$ ，波速为 $u$ ，相当于波以速度 $u+v_R$ 向观察者移动则观察者接收到的波的频率为：
$$
\nu_R=\frac{u+v_R}{\lambda}=(\frac{u+v_R}{u})\nu_s
$$
**（2）观察者相对媒质静止，波源以 $v_s$ 向观察者运动**

波源的运动导致波的波长发生变化，可推导出以下关系：
$$
\begin{align}
\lambda'&=\lambda-v_sT_s=(u-v_s)T_s\\
\nu_R&=\frac{u}{\lambda'}=\frac{u}{(u-v_s)T_s}=\frac{u}{u-v_s}\nu_s
\end{align}
$$
**（3）波源和观察者在同一直线上同时运动**

综合上述两种情况，可以得到：
$$
\nu_R=\frac{u+v_R}{u-v_s}\nu_s
$$
**（4）光波的多普勒效应**

光源与接收器的相对运动速度为 $u$ ，在同一条直线上接收器收到的频率为：
$$
\nu_R=\sqrt{\frac{c+u}{c-u}}\nu_s
$$