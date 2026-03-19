---
title: Ch-7 气体动理论
date: 2026-03-19
type: docs
---

### 热力学系统

**孤立系统** 系统与外界既无物质交换，也无能量交换。
**封闭系统** 系统与外界无物质交换，但有能量交换。
**开放系统** 系统与外界既有物质交换，又有能量交换。
### 平衡态 

若封闭系统与外界没有能量交换，系统内部也不发生化学反应或核反应等过程，则经过足够长时间后系统可观测的宏观性质达到稳定，不再随时间而变化，系统这种状态称为 **平衡态**。

当系统与外界交换能量时，系统原来的平衡态就被破坏，能量交换后经过足够时间，系统又达到一个新的平衡态，系统的状态随时间的变化，叫作 **热力学过程**。

### 气体动理论的基本假设

#### 分子及其运动假设
* 气体由大量分子组成；
* 每个分子都在不停地作无规则运动，并相互频繁碰撞。
#### 统计假设
* 气体处于平衡态时，分子的空间分布均匀；
* 气体处于平衡态时，分子沿各个方向运动的概率相等。
#### 理想气体的微观假设
* 理想气体分子本身的体积忽略不计，可视为弹性质点；
* 分子与分子之间，分子与器壁之间的碰撞是完全弹性碰撞；
* 除碰撞外，分子之间的相互作用力可以忽略。
只有压强较低，温度较高的气体才遵守该微观假设。

### 理想气体的压强公式

设理想气体由质量为 $\mu$ 的分子组成，处于平衡态，单位体积中的总分子数为 $n$ ，则：
$$
p=\frac{1}{3}n\mu\bar{v^2}=\frac{2}{3}n\bar{\epsilon_t}
$$
 $\begin{aligned}\bar{v^2}=\frac{\begin{aligned}\sum_in_iv_i^2\end{aligned}}{n}\end{aligned}$ 为气体分子速率二次方的统计平均值。
 $\begin{aligned}\bar{\epsilon_t}=\frac{\begin{aligned}\sum_in_i(\frac{1}{2}\mu v_i^2)\end{aligned}}{n}=\frac{\mu\bar{v^2}}{2}\end{aligned}$ 为平均每一个气体分子所具有的平动动能（平均平动动能）。
**注:** 此处的 $n$ 量纲为 $m^{-3}$ ，因此该压强公式的量纲是正确的。

### 温度与分子平均平动动能

系统的温度 $T$ 与分子平均平动动能 $\bar{\epsilon_t}$ 之间存在单值函数关系，两者关系为：
$$
\bar{\epsilon_t}=\frac{3}{2}kT,\quad k=1.38\times10^{-23}\mathrm{J/K}
$$
说明系统的温度越高，分子的平均平动动能越大，**温度是分子平均平动动能的度量**
**注:** 系统整体运动的动能对温度是 **无影响** 的。

### 气体分子的方均根速率

气体分子速率二次方统计平均值 $\bar{v^2}$ 的二次方根 $\sqrt{\bar{v^2}}$ 称为气体分子的方均根速率：
$$
\begin{cases}
\begin{aligned}
&\bar{\epsilon_t}=\frac{1}{2}\mu\bar{v^2}\\
&\bar{\epsilon_t}=\frac{3}{2}kT
\end{aligned}
\end{cases}
\Rightarrow
\sqrt{\bar{v^2}}=\sqrt{\frac{3kT}{\mu}}
$$
若以 $N_A$ 表示阿伏伽德罗常数，则有：
$$
\begin{align}
R&=N_Ak=(6.02\times10^{23}\times1.38\times10^{-23})\mathrm{J/(mol\cdot K)}\\
&=8.31\mathrm{J/(mol\cdot K)}
\end{align}
$$
$R$ 称为摩尔气体常量，若以 $M$ 表示气体的摩尔质量，则公式可表示为：
$$
\sqrt{\bar{v^2}}=\sqrt{\frac{3kT}{\mu}}=\sqrt{\frac{3RT}{M}}
$$
### 理想气体状态方程

将温度与分子平均平动动能的关系 $\begin{aligned}\bar{\epsilon_t}=\frac{3}{2}kT\end{aligned}$ 代入理想气体压强公式得到：
$$
p=nkT
$$
由于 $\begin{aligned}n=\frac{N}{V},R=N_Ak\end{aligned}$ ，则上式还可以表示为：
$$
pV=\nu RT
$$
其中 $\nu$ 表示理想气体的物质的量。

### 自由度

确定物体的空间位置所必需的独立坐标数目称为该物体的自由度，包含平动自由度、转动自由度、振动自由度等。

### 能量均分原理
$$
\bar{\epsilon_t}
=\frac{1}{2}\mu\bar{v^2}
=\frac{1}{2}\mu\bar{v_x^2}
+\frac{1}{2}\mu\bar{v_y^2}
+\frac{1}{2}\mu\bar{v_z^2}
=\frac{3}{2}kT
$$
$$
\bar{v_x^2}=\bar{v_y^2}=\bar{v_z^2}
$$
$$
\frac{1}{2}\mu\bar{v_x^2}
=\frac{1}{2}\mu\bar{v_y^2}
=\frac{1}{2}\mu\bar{v_z^2}
=\frac{1}{2}kT
$$
在平衡态下分子每个自由度的平均能量都相等，称为能量均分原理。液体和固体的温度较高时能量均分原理也适用。

平均每一个分子所具有的平动、转动和振动能量的总和称为气体分子的平均能量，用符号 $\bar{\epsilon}$ 表示，根据能量均分原理，若分子的自由度为 $i$ ，则分子的平均能量为：
$$
\bar{\epsilon}=\frac{i}{2}kT
$$
当温度不太高时，按刚性分子计算与许多气体的实验结果大致相符。

| 分子类型    | 自由度  | 平动自由度 | 转动自由度 | 振动自由度 | 平均能量                                                   |
| :------ | :--- | ----- | ----- | ----- | :----------------------------------------------------- |
| 单原子分子   | $3$  | $3$   | $0$   | $0$   | $\begin{align}\varepsilon_t=\frac{3}{2}kT\end{align}$  |
| 刚性双原子分子 | $5$  | $3$   | $2$   | $0$   | $\begin{align}\varepsilon_t=\frac{5}{2}kT\end{align}$  |
| 刚性多原子分子 | $6$  | $3$   | $3$   | $0$   | $\begin{align}\varepsilon_t=\frac{6}{2}kT\end{align}$  |
| 弹性双原子分子 | $7$  | $3$   | $2$   | $2$   | $\begin{align}\varepsilon_t=\frac{7}{2}kT\end{align}$  |
| 弹性多原子分子 | $12$ | $3$   | $3$   | $6$   | $\begin{align}\varepsilon_t=\frac{12}{2}kT\end{align}$ |

**注:** 热力学自由度中一个振动包含振动动能和振动势能两个自由度。
### 理想气体的内能

与气体内部分子无序运动相联系的能量称为系统的内能（热力学能）。

物质的量为 $\nu$ 的理想气体的内能为：
$$
E=\nu N_A(\frac{i}{2}kT)=\nu\frac{i}{2}RT
$$
当理想气体的量一定时，其内能仅决定于气体的温度。
### 速率分布函数

气体分子的速率分布函数为：
$$
f(v)=\frac{dN}{Ndv},\quad \int_0^\infty f(v)dv=1
$$
速率分布函数 $f(v)$ 表示速率在 $v$ 附近单位速率区间内的分子数占总分子数的比率。

#### 最概然速率

速率分布函数 $f(v)$ 的极大值对应的速率：
$$
\begin{align}\frac{df(v)}{dv}\Big{|}_{v_p}=0\end{align}
$$
#### 平均速率

大量分子速率的算术平均值，称为气体分子的平均速率：
$$
\overline{v}=\frac{\begin{align}\int vdN\end{align}}{N}=\int_0^\infty vf(v)dv
$$
#### 方均根速率

分子速率二次方统计平均值的二次方根：
$$
\overline{v^2}=\sqrt{\int_0^\infty v^2f(v)dv}
$$
### 麦克斯韦速率分布律

理想气体处于平衡态时，速率在 $v$ 和 $v+dv$ 区间的分子数占总分子数的比率为：
$$
\begin{align}
&f(v)=\frac{dN}{Ndv}=4\pi(\frac{\mu}{2\pi kT})^{\frac{3}{2}}e^{-\frac{\mu v^2}{2kT}}v^2\\
&f(v)=\frac{4}{\sqrt{\pi}}e^{-\frac{v^2}{v_p^2}}(\frac{v^2}{v_p^3})
\end{align}
$$
$$
\begin{align}
最概然速率:v_p=\sqrt{\frac{2kT}{\mu}}=\sqrt{\frac{2RT}{M}}\\
平均速率:\overline{v}=\sqrt{\frac{8kT}{\pi\mu}}=\sqrt{\frac{8RT}{\pi M}}\\
方均根速率:\sqrt{\overline{v^2}}=\sqrt{\frac{3kT}{\mu}}=\sqrt{\frac{3RT}{M}}\\
v_p:\overline{v}:\sqrt{\overline{v^2}}=\sqrt{2}:\frac{8}{\pi}:\sqrt{3}
\end{align}
 $$
 【注】在做题时要先判定是否是理想气体再带入公式计算。
### 等温气压公式

对于理想气体，有：
$$
\begin{cases}
dp=-\rho gdh\\
\begin{align}
\rho=\frac{pM}{RT}
\end{align}
\end{cases}
\Rightarrow
\frac{dp}{p}=-\frac{Mg}{RT}dh
\Rightarrow
p=p_0e^{-\frac{Mgh}{RT}}
$$
气体分子数密度按高度的分布：
$$
n=\frac{p_0}{kT}e^{-\frac{Mgh}{RT}}
=n_0e^{-\frac{\mu gh}{kT}}
=n_0e^{-\frac{\epsilon_p}{kT}}
$$
在重力场中，气体的分子数密度 $n$ 随高度 $h$ 的增大而指数级地减少；
分子质量 $\mu$ 越大，重力作用越强，$n$ 减小地越快；
温度 $T$ 越高，分子无序运动越剧烈，$n$ 减小地越慢。
### 玻尔兹曼分布律
$$
dN_{v,r}=n_0(\frac{\mu}{2\pi kT})^{3/2}e^{-\frac{\epsilon}{kT}}
\cdot dv_x
\cdot dv_y
\cdot dv_z
\cdot dx
\cdot dy
\cdot dz
$$
式中 $\epsilon=\epsilon_p+\epsilon_k$ ，即分子的平动动能和外力场的势能之和，$n_0$ 表示势能 $\epsilon_p=0$ 处的分子数密度。
### 平均碰撞频率

单位时间内一个分子与其他分子碰撞次数的统计平均值称为分子的平均碰撞频率 ：
$$
\overline{Z}=\sqrt{2}\pi d^2n\overline{v}
$$
其中 $d$ 为气体分子的有效直径，$n$ 为气体分子的数密度。
### 平均自由程
$$
\overline{\lambda}=\frac{\overline{v}}{\overline{Z}}=\frac{1}{\sqrt{2}\pi d^2n}
=\frac{kT}{\sqrt{2}\pi d^2p}
$$
### 热传导现象

假设气体温度仅与坐标 $z$ 有关， $dQ$ 表示 $dt$ 内沿 $z$ 轴正方向通过 $dS$ 传递的热量， $\begin{align}\frac{dT}{dz}\end{align}$ 表示 $dS$ 处温度的梯度，则有热传导定律：
$$
\begin{align}
dQ&=-\kappa\frac{dT}{dz}dSdt\\
\kappa&=\frac{1}{6}ikn\overline{v}\overline{\lambda}\\
\kappa&=\frac{ik}{3\pi d^2}\sqrt{\frac{kT}{\pi\mu}}
\end{align}
$$
 $\kappa$ 与气体分子的自由度 $i$ 、分子数密度 $n$ 、分子的平均速率 $\overline{v}$ 和平均自由程 $\overline{\lambda}$ 成正比，热传导是分子热运动能量的迁移过程。
### 黏滞现象

气体各部分流速不同时，各部分气体相互作用使流速趋于一致，这一现象称为粘滞现象：
$$
f=-\eta\frac{du}{dz}dS
$$
式中 $\eta$ 表示气体的黏度，上述定理称为黏滞定律：
$$
dP=-\eta\frac{du}{dz}dSdt
$$
黏滞现象是气体内部分子定向动量迁移的结果：
$$
\eta=\frac{1}{3}n\mu\overline{v}\overline{\lambda}
=\frac{1}{3}\rho\overline{v}\overline{\lambda}
$$
### 扩散现象

考虑纯扩散过程，两种气体的分子量、温度、压强均相等：
$$
dm=-D\frac{d\rho}{dz}dSdt
$$
式中 $D$ 表示气体的扩散率，上述定理称为扩散定律：
$$
D=\frac{1}{3}\overline{v}\overline{\lambda}
$$
$$
D=\frac{2}{3\sqrt{\mu}pd^2}(\frac{kT}{\pi})^{3/2}
$$
扩散是分子质量的迁移过程。
### 范德瓦尔斯方程
$$
\frac{pV}{\nu RT}=\zeta\neq1
$$
其中 $\zeta$ 称为压缩因子，与气体的性质、压强和温度有关。

范德瓦尔斯理想气体与理想气体的差别主要为以下两点：
* 实际气体分子本身的体积不能忽略；
* 实际气体分子之间的相互作用力不能忽略。
#### 体积的修正

一个分子的不可压缩体积相当于分子自身体积的 $4$ 倍，$1\mathrm{mol}$ 分子的不可压缩体积为：
$$
\begin{align}
&b=N_A\{4[\frac{4}{3}\pi(\frac{d}{2})^3\}=\frac{2}{3}N_A\pi d^3\\
&修正后的体积=V-\nu b
\end{align}
$$
#### 压强的修正
$$
\begin{align}
&p_i\varpropto器壁附近受力的分子数密度\varpropto\frac{\nu}{V}\\
&p_i\varpropto对器壁附近分子施力的其他分子数密度\frac{\nu}{V}\\
&p_i=a(\frac{\nu}{V})^2\\
&修正后的压强=(p+p_i)=[p+a(\frac{\nu}{V})^2]
\end{align}
$$
#### 范德瓦尔斯方程

将修正后的压强、体积代入理想气体状态方程，得到范德瓦尔斯方程：
$$
\begin{bmatrix}
\begin{align}
p+a(\frac{\nu}{V})^2
\end{align}
\end{bmatrix}
(V-\nu b)=\nu RT
$$
当气体压强很低时 $\begin{align}V\gg \nu b,p\gg a(\frac{\nu}{V})^2\end{align}$ ，范德瓦尔斯方程退化为理想气体方程。

**临界温度 $T_K$** 无论怎样恒温加压也不能使气体液化。

**临界等温线** 临界温度对应的等温线。

**临界点** 临界等温线上的拐点 $K$。

**临界压强 $p_K$** 临界点对应的压强。

**临界摩尔体积 $V_K$** 临界点对应的摩尔体积。
### 实际气体的内能

实际气体的内能应等于所有分子热运动能量之和与相互作用力势能之和：
$$
\begin{align}
&\Delta E_k=\nu C_{V,m}(T_2-T_1)\\
&\Delta E_p=\int_{V_1}^{V_2}p_idV=\int_{V_1}^{V_2}a(\frac{\nu}{V})^2dV=\nu^2a(\frac{1}{V_1}-\frac{1}{V_2})\\
&\Delta E=\Delta E_k+\Delta E_p=Q+A
\end{align}
$$