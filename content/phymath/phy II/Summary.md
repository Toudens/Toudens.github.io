---
title: Appendix 总结整理
date: 2026-03-19
type: docs
weight: "3"
---
## 电学公式

**库伦定律** $\begin{align}F=\frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r^2}\end{align}$

试探电荷所在点的 **电场强度** $\begin{align}E=\frac{F}{q_0}=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}(\text{点电荷})\end{align}$

**电偶极矩** 的定义 $p=ql$ ， $l$ 为电荷间的距离

均匀带电细棒外一点的 **电场强度** $\begin{align}E_x=\frac{\lambda}{4\pi\varepsilon_0a}(\sin\theta_2-\sin\theta_1),E_y=\frac{\lambda}{4\pi\varepsilon_0a}(\cos\theta_2-\cos\theta_1)\end{align}$

若带电细棒是 **无限长** 的则 $\begin{align}E_x=0,E_y=\frac{\lambda}{2\pi\varepsilon_0a}\end{align}$

均匀带电圆环轴上的 **电场强度** $\begin{align}E=\frac{1}{4\pi\varepsilon_0}\frac{qx}{(x^2+R^2)^{3/2}}\end{align}$

电偶极子在均匀电场中受到的 **力矩** $\begin{align}M=p\times E\end{align}$

静电场中的 **高斯定律** $\begin{align}\Phi_e=\oint_SE\cdot\mathrm{d}S=\frac{1}{\varepsilon_0}\sum_iq_i(\text{内})\end{align}$

静电场中的 **环路定律** $\begin{align}\oint_LE\cdot\mathrm{d}l=0\end{align}$ 

**电势梯度** $\begin{align}E=-\nabla=-(\frac{\partial V}{\partial x}i+\frac{\partial V}{\partial y}j+\frac{\partial V}{\partial z}k)\end{align}$ 一些电场强度可以用此式求解

| 电容器类型    | 电容大小                                                                                 |
| -------- | ------------------------------------------------------------------------------------ |
| 孤立导体球    | $\begin{align}C=\frac{q}{V}=4\pi\varepsilon_0R\end{align}$                           |
| 平行板电容器   | $\begin{align}C=\frac{q}{\Delta V}=\frac{q}{Ed}=\frac{\varepsilon_0S}{d}\end{align}$ |
| 同心球形电容器  | $\begin{align}C=4\pi\varepsilon_0\frac{R_AR_B}{R_B-R_A}\end{align}$                  |
| 同轴圆柱形电容器 | $\begin{align}C=\frac{2\pi\varepsilon_0l}{\ln\frac{R_B}{R_A}}\end{align}$            |

电介质的 **极化强度** $\begin{align}\frac{\sum p_{\text{分子}}}{\Delta V}\end{align}$ 注意方向是由负电荷指向正电荷

束缚电荷**面密度** $\sigma'=P\cos\theta=P_n$

电介质的**极化率** $P=\chi_e\varepsilon_0E$ 

电介质中的 **高斯定律** $\begin{align}\oint_S D\cdot\mathrm{d}S=\sum_{\text{S内}}q_0\end{align}$ 其中 $D=\varepsilon_0\varepsilon_rE$ 

可以理解为 **电位移 $D$** 是没有电介质的情况下应有的电场强度，$E$ 是 **实际电场强度** 

带电导体的能量 $\begin{align}U_e=\frac{1}{2}\frac{q^2}{C}=\frac{1}{2}CV^2=\frac{1}{2}qV\end{align}$

**电场能量密度** $\begin{align}u_e=\frac{1}{2}\varepsilon_0\varepsilon_rE^2=\frac{1}{2}DE\end{align}$

静电场是 **保守力场** 而非静电性电场强度 $E_K$ 不是保守力场

平行载流导线单位长度上受 **磁相互作用力** $\begin{align}F_m=\frac{\mu_0I_1I_2}{2\pi b}\end{align}$

运动电荷产生磁场的 **磁感应强度** $\begin{align}B=\frac{\mu_0}{4\pi}\frac{qv}{r^2}\end{align}$

毕奥-萨伐尔定律 $\begin{align}\mathrm{d}B=\frac{\mu_0}{4\pi}\frac{I\mathrm{d}l}{r^2}\end{align}$

载流直导线外一点的 **磁感应强度** $\begin{align}B=\frac{\mu_0I}{4\pi r_0}(\cos\theta_1-\cos\theta_2)\end{align}$

对于无限长载流直导线 $\begin{align}B=\frac{\mu_0I}{2\pi r_0}\end{align}$

载流圆线圈轴线上的 **磁感应强度** $\begin{align}B=\frac{\mu_0}{2}\frac{IR^2}{(R^2+r_0^2)^{3/2}}\end{align}$ 

线圈的磁矩定义为 $p_m=IS$ 方向服从右手螺旋定则

磁场中的 **高斯定律** $\begin{align}\Phi_m=\oint_SB\cdot\mathrm{d}S=0\end{align}$

**安培环路定律** $\begin{align}\oint_LB\cdot\mathrm{d}l=\mu_0\sum_{\text{L内}}I\end{align}$

磁场中运动的电荷受 **洛伦兹力** $F_m=qv\times B$ 

安培定律 $\begin{align}F=I\mathrm{d}l\times B\end{align}$

载流线圈在磁场中受到的磁力矩 $M=p_m\times B$

束缚电流密度与磁化强度的关系 $M=j_m$

有磁介质存在时的 **安培环路定律** $\begin{align}\oint_LH\cdot\mathrm{d}l=\sum_{(\text{L内})}I\end{align}$ 其中 $B=\mu_0\mu_rH$

可以理解为 **磁场强度 $H$** 是没有磁介质的情况下应有的磁场强度 ，$B$ 是 **实际磁场强度**

**矫顽力** 只有 $H=-H_c$ 时磁感应强度才能变为零

感应电动势的大小 $\begin{align}E=-N\frac{\mathrm{d}\Phi_m}{\mathrm{d}t}=-\frac{\mathrm{d}\Psi}{\mathrm{d}t}\end{align}$ 

**自感系数** $\begin{align}L=\frac{\Psi}{I}=\mu_0n^2V(\text{螺线管})\end{align}$

**磁场中的能量** $\begin{align}U_m=\frac{1}{2}LI^2\end{align}$ 

**磁场中的能量密度** $\begin{align}u_m=\frac{1}{2}\mu_0\mu_rH^2=\frac{1}{2}HB\end{align}$

**位移电流** $\begin{align}I_d=\frac{\mathrm{d}\Phi_d}{\mathrm{d}t},\Phi_d=\oint_SD\cdot\mathrm{d}S\end{align}$

| 麦克斯韦方程    | 公式                                                                                        |
| --------- | ----------------------------------------------------------------------------------------- |
| 电学的高斯定律   | $\begin{align}\oint_SD\cdot\mathrm{d}S=\sum_iq_i\end{align}$                              |
| 磁学的高斯定律   | $\begin{align}\oint_SB\cdot\mathrm{d}S=0\end{align}$                                      |
| 法拉第电磁感应定律 | $\begin{align}\oint_LE\cdot\mathrm{d}l=-\frac{\mathrm{d}\Phi_m}{\mathrm{d}t}\end{align}$  |
| 普遍的安培环路定律 | $\begin{align}\oint_LH\cdot\mathrm{d}l=I+\frac{\mathrm{d}\Phi_d}{\mathrm{d}t}\end{align}$ |

**电磁场的总能量密度** $\begin{align}u=u_e+u_m=\frac{1}{2}\varepsilon_0\varepsilon_rE^2+\frac{1}{2}\mu_0\mu_rH^2\end{align}$

$E$ 和 $H$ 有比例关系 $\sqrt{\varepsilon_0\varepsilon_r}E=\sqrt{\mu_0\mu_r}H$ ，振幅也具有此比例关系

电磁波的平均能流密度 $\begin{align}\bar{S}=\frac{1}{2}E_0H_0\end{align}$

**霍尔效应** $\begin{align}U_H=R_H\frac{BI}{d},R_H=\frac{1}{nq}\end{align}$
## 光学公式

**光程**：光在介质中传播的路程与介质折射率的乘积 $nr$ 

**半波损失**：光从折射率较小的介质入射到较大的介质的界面并反射时，光程减少 $\lambda/2$

**杨氏双缝干涉**：$\delta=d\frac{x}{D}$ 暗纹 $x_k=\pm(2k+1)\frac{D}{2d}\lambda$  明纹 $x_k=\pm k\frac{D}{d}\lambda$  

**等倾干涉**：$\delta=2en_2\cos\gamma+\frac{\lambda}{2}$ 

**等厚干涉**：$\delta=2n_2e+\frac{\lambda}{2}$

**牛顿环**：暗纹 $r_k=\sqrt{kR\lambda}$  明纹 $r_k=\sqrt{(k-\frac{1}{2})R\lambda}$

**衍射角**：$\delta=a\sin\theta\approx \frac{ax}{f}$  明纹 $\pm(2k+1)\frac{\lambda}{2}$ 

**主极大**：$d\sin\theta=(a+b)\sin\theta=\pm k\lambda$ 若该角度恰为衍射角暗纹则缺级，若不是垂直入射而是存在入射角 $i$ 则将 $\sin\theta$ 替换为 $\sin\theta+\sin i$

**马吕斯定律**：自然光 $I=\frac{1}{2}I_0$ 线偏振光 $I=I_0\cos^2\theta$

**布儒斯特定律**：布儒斯特角 $\tan i_0=\frac{n_2}{n_1}$
1. 振动方向与光轴垂直，传播速度为正常值，折射率为 $n_o$ 
2. 振动方向与光轴平行，传播速度为最值，折射率为 $n_e$

对于正晶体 $n_e>n_o$ ，对于负晶体 $n_o>n_e$ ，在波片中折射率的不同导致光程差 $\delta=|n_o-n_e|d$ 

## 量子力学公式

**维恩位移定律**：$\lambda_{\text{max}}=\frac{b}{T},b=2.897\times10^{-3}\text{m}\cdot\text{K}$ 

黑体辐出度与温度的四次方成正比：$M(T)=\sigma T^4,\sigma=5.67\times 10^{-8}\text{W}/(\text{m}^2\text{K}^4)$ 

**光电效应**： $h\nu=E_{km}+A$ 

**康普顿效应**：$\delta\lambda=\lambda-\lambda_0=\frac{h}{m_ec}(1-\cos\varphi)$

**德布罗意波**：物质波 $E=mc^2=h\nu,p=mv=\frac{h}{\lambda}$

动量与位置的不确定关系：$\Delta x\Delta p_x\geq\frac{h}{4\pi}$

能量和时间的不确定关系：$\Delta E\Delta t\geq\frac{h}{4\pi}$

玻尔氢原子理论：$r_n=n^2a_0=n^2\frac{\varepsilon_0h^2}{\pi me^2}$  $E_n=-\frac{1}{n^2}(\frac{me^4}{8\varepsilon_0^2h^2})$ 

氢原子光谱：$\frac{1}{\lambda}=R(\frac{1}{n_1^2}-\frac{1}{n_2^2})$
## 易错点

1. 电势梯度的计算漏负号
2. 注意区分题目问的是极化电荷产生的电场还是极板上的电荷产生的电场
3. 注意并联电路要分流，不要误认为无阻导线
4. 注意公式 $D=\varepsilon_0\varepsilon_rE,B=\mu_0\mu_rH$ 中系数的位置是反的
5. 注意运动的物体的初速度
6. 注意题目是圆盘还是线圈
7. 计算过程中漏了线圈匝数
8. 注意题目中给的是半径还是直径，单位是否规范
9. 计算数量级错误
10. 单位量级的换算验证
11. 注意介质，考虑半波损失
12. 注意粒子速度达到接近光速时要考虑相对论效应