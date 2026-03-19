---
title: Ch-5 机械振动
date: 2026-03-19
type: docs
---
### 简谐振动方程

简谐振动的微分方程及其解的一般形式为（可以通过常微分方程知识求解）：
$$
\frac{d^2x}{dt^2}+\omega^2x=0\quad\Rightarrow\quad x=A\cos(\omega t+\varphi)
$$
已知简谐振动的初始状态 $x_0=A\cos\varphi,\quad v_0=-\omega A\sin\varphi$ 可以求得：
$$
A=\sqrt{x_0^2+(\frac{v_0}{\omega})^2},
\quad
\varphi=\arctan\frac{-v_0}{\omega x_0}
$$
### 谐振动的能量

设物体的位移为 $x$ ，速度为 $v$ 时，系统的弹性势能与动能分别为：
$$
\begin{align}
&E_p=\frac{1}{2}kx^2=\frac{1}{2}kA^2\cos^2(\omega t+\varphi)
\quad \omega^2=\frac{k}{m}
\\
&E_k=\frac{1}{2}mv^2=\frac{1}{2}m\omega^2A^2\sin^2(\omega t+\varphi)=\frac{1}{2}kA^2\sin^2(\omega t+\varphi)\\
&E=\frac{1}{2}kx^2+\frac{1}{2}mv^2=\frac{1}{2}kA^2
\end{align}
$$
则系统的势能和动能总量守恒，总能量与振幅平方成正比。

### 稳定平衡位置附近的运动

#### 单摆的简谐振动
$$
m\frac{d^2x}{dt^2}=m\frac{d^2(l\theta)}{dt^2}=-\frac{mg}{l}(l\theta)=-\frac{mg}{l}x=F_t\quad\Rightarrow\quad\frac{d^2\theta}{dt^2}=-\frac{g}{l}\theta
$$
则当 $\theta$ 角很小时，单摆的运动可以看作谐振动。

#### 复摆的简谐振动
$$
-mgl\sin\theta=J\frac{d^2\theta}{dt^2}
\quad(\sin\theta\approx\theta)
\quad\Rightarrow\quad
\frac{d^2\theta}{dt^2}=-\frac{mgl}{J}\theta
$$
则复摆的振动角频率为 $\begin{align}\omega=\sqrt{\frac{mgl}{J}}\end{align}$ ，单摆可以视为复摆的特例。

### 阻尼振动

振动系统收到弹性力和阻力两个力的作用，应用牛顿方程，得到：

$$
\begin{align}m\frac{d^2x}{dt^2}=-kx-b\frac{dx}{dt}\Rightarrow\frac{d^2x}{dt^2}+\frac{b}{m}\frac{dx}{dt}+\frac{k}{m}x=0\end{align}
$$
应用常微分方程中的特征方程，得到：
$$
\begin{align}r^2+\frac{b}{m}r+\frac{k}{m}=0\end{align} 
$$
由于是弱阻尼运动，该方程的解应当反应振幅减弱的情况，则 $\Delta<0$
该方程的复数解为：
$$
\begin{align}
r=\frac{-\frac{b}{m}\pm\sqrt{\frac{b^2}{m^2}-4\frac{k}{m}}}{2}
=-\frac{b}{2m}\pm\sqrt{(\frac{b}{2m})^2-\frac{k}{m}}
=-\frac{b}{2m}\pm\sqrt{\frac{k}{m}-(\frac{b}{2m})^2}\cdot\mathrm{i}
\end{align}
$$
根据常微分方程的知识可以得到方程的一个解为：
$$
\begin{align}
Ae^{-\frac{b}{2m}t}\cos(\sqrt{\frac{k}{m}-(\frac{b}{2m})^2}\cdot t+\varphi)
\end{align}
$$
由无阻尼振动中的 $\begin{align}\omega_0=\sqrt{\frac{k}{m}}\end{align}$ ，令 $\gamma=\frac{b}{2m}$ ，则新的振动方程为：
$$
\begin{align}Ae^{-\gamma t}\cos(\sqrt{\omega_0^2-\gamma^2}\cdot t+\varphi)\end{align} 
$$

**振动能量** $\begin{align}E=E_\theta e^{-2\gamma t}\end{align}$ 振动的能量也随时间作指数衰减。

**时间常数** $\begin{align}\tau=\frac{1}{2\gamma}=\frac{m}{b}\end{align}$ 表示能量衰减为原来的 $\begin{align}\frac{1}{e}\end{align}$ 的时间。

**品质因数** $\begin{align}Q=2\pi\frac{1}{2\gamma T}=\frac{\omega}{2\gamma}=\omega\tau\end{align}$ 表示阻尼振动在一个时间常数振动对应的相位变化。

### 受迫振动与共振

假设驱动力按照余弦规律变化，即 $F=F_0\cos(\omega t)$ ，则物体受弹性力、阻力和驱动力得到牛顿运动方程：
$$
m\frac{d^2x}{dt^2}=-kx-b\frac{dx}{dt}+F_0\cos\omega t
$$
在稳态等幅受迫振动中，上述方程的解为 $x=A\cos(\omega t+\varphi)$ ，其中：
$$
\begin{align}
&A=\frac{\begin{align}\frac{F_0}{m}\end{align}}{\sqrt{(\omega_0^2-\omega^2)^2+4\gamma^2\omega^2}},\quad\varphi=\arctan\frac{-2\gamma\omega}{\omega_0^2-\omega^2}\\
&\omega_0^2=\frac{k}{m},\quad\gamma=\frac{b}{2m}
\end{align}
$$
当阻尼为 $0$ 时 $\omega_{共振}=\omega_0$ ，当阻尼不为 $0$ 时 $\omega_{共振}=\sqrt{\omega_0^2-2\gamma^2}$。
### 振动的合成

#### 同方向同频率谐振动的合成

设物体沿 $x$ 轴同时参与两个独立振动，分别以 $x_1,x_2$ 表示其位移：
$$
x_1=A_1\cos(\omega t+\varphi_1),\quad x_2=A_2\cos(\omega t+\varphi_2)
$$
合振动仍然是谐振动，即 $x=A\cos(\omega t+\varphi)$ ：
$$
\begin{align}
&A=\sqrt{A_1^2+A_2^2+2A_1A_2\cos(\varphi_2-\varphi_1)}\\
&\varphi=\arctan\frac{A_1\sin\varphi_1+A_2\sin\varphi_2}{A_1\cos\varphi_1+A_2\cos\varphi_2}
\end{align}
$$
#### 同方向不同频率谐振动的合成

设物体沿 $x$ 轴同时参与两个独立振动，简便起见设分振动的初相均为零。

合振幅的大小为 $\begin{aligned}A=\sqrt{A_1^2+A_2^2+2A_1A_2\cos(\omega_2-\omega_1)t}\end{aligned}$ 。

当 $A_1=A_2$ 时，$\begin{align}x=2A_1\cos(\frac{\omega_2-\omega_1}{2})t\cos(\frac{\omega_1+\omega_2}{2})t\end{align}$ 。

在 $\omega_2-\omega_1\ll\omega_1+\omega_2$ 的条件下，振幅随时间周期变化。

合振动强弱交替变化的现象称为拍，单位时间内振动忽强（或忽弱）的次数称为拍频：
$$
\begin{align}\nu_{拍}=\frac{\omega_2}{2\pi}-\frac{\omega_1}{2\pi}=\nu_2-\nu_1\end{align}
$$
拍频是 $\begin{align}\cos(\frac{\omega_2-\omega_1}{2})t\end{align}$ 的振动频率的两倍。