---
title: 线性代数
date: 2026-03-19
type: docs
---
### 线性代数的几何解释

#### 矩阵与线性变换的几何意义

对于方阵 $A,B$ ，表达式 $B(AX)$ 表示在新基 $B$ 下坐标为在新基 $A$ 下坐标为 $X$ 的坐标的坐标。
$(BA)X$ 表示 $A$ 中的每一个列向量在新基 $B$ 下对应的向量构成的一组基下坐标为 $X$ 的坐标。
这表明矩阵的乘法是线性变换依次进行的等价线性变换。

对于非方阵的矩阵乘法，一个 $m\times n$ 的矩阵：
* 若 $m>n$ ，则表示了从低维倾斜到高维空间的线性变换；
* 若 $m<n$ ，则表示了从高维压缩到低维空间的线性变换。

对于矩阵的相似 $A=PBP^{-1}$ ，可以解读为：将基更换为 $P$ 后再进行线性变换 $B$ ，再更换为原来的基。

#### 行列式的几何意义

一个 $2\times2$ 的方阵 $A$ 的行列式反应了面积被放大了几倍，即原来在正交基下面积为 $S$ 的图形在经过该方阵线性变换后，面积变为了 $\det(A)\cdot S$。

一个 $3\times3$ 的方阵 $A$ 的行列式反应了体积被放大了几倍，即原来在正交基下体积为 $V$ 的图形在经过该方阵线性变换后，体积变为了 $\det(A)\cdot V$。

考虑 $n$ 维空间中的一组标准正交基 $\{i_1,i_2,\cdots,i_n\}$ ，空间中的任意一个向量都可以表示为 $\vec{v}=k_1i_1+k_2i_2+\cdots+k_ni_n$ ，则对于 $n$ 个向量 $\{\vec{v_1},\vec{v_2},\cdots,\vec{v_n}\}$ ，记它们围成的体积为 $V(\vec{v_1},\vec{v_2},\cdots,\vec{v_n})$ ，则体积函数满足以下性质：
* $V(i_1,i_2,\cdots,i_n)=1$ 
* $V(\vec{v_1},\vec{v_1},\cdots,\vec{v_n})=0 $ 
* $\begin{aligned}V(c\vec{v_1},\vec{v_2},\cdots,\vec{v_n})=cV(\vec{v_1},\vec{v_2},\cdots,\vec{v_n})\end{aligned}$
* $V(\vec{v_1}+\vec{u},\vec{v_2},\cdots,\vec{v_n})=V(\vec{v_1},\vec{v_2},\cdots,\vec{v_n})+V(\vec{u},\vec{v_2},\cdots,\vec{v_n})$
* $V(\vec{v_1},\vec{v_2},\cdots,\vec{v_n})=-V(\vec{v_2},\vec{v_1},\cdots,\vec{v_n})$

根据以上几条性质展开 $V(\vec{v_1},\vec{v_2},\cdots,\vec{v_n})$ ，得到的结果与行列式的定义推导是一致的，由此还可以推导克拉默法则。

#### 向量点乘的理解
可以将 $\alpha\cdot\beta$ 中的向量 $\alpha$ 看作线性变换，设 $\alpha=\begin{bmatrix}x_1\\y_1\end{bmatrix},\beta=\begin{bmatrix}x_2\\y_2\end{bmatrix}$ ，则有：
$\begin{aligned}\alpha\cdot\beta&=\begin{bmatrix}x_1\\y_1\end{bmatrix}\cdot\begin{bmatrix}x_2\\y_2\end{bmatrix}=\begin{bmatrix}x_1&y_1\end{bmatrix}\begin{bmatrix}x_2\\y_2\end{bmatrix}=\sqrt{x_1^2+y_1^2}\begin{bmatrix}u_x&u_y\end{bmatrix}\begin{bmatrix}x_2\\y_2\end{bmatrix}\\&=\sqrt{x_1^2+y_1^2}\times\sqrt{x_2^2+y_2^2}\times\cos{\theta}=x_1\cdot x_2+y_1\cdot y_2\end{aligned}$
其中 $u_x,u_y$ 分别代表了 $x,y$ 轴上的单位向量在经过线性变换后在向量 $x$ 所在直线上的坐标。

#### 特征值与特征向量的几何意义
特征向量是在经过方阵对应的线性变换之后，方向保持不变的向量；特征值则是该向量在该方向上缩放的倍数。
### 行列式及其计算

#### 行列式的定义与特殊形式

**行列式的定义**：

$\begin{aligned}\begin{vmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&&\vdots\\a_{n1}&a_{n2}&\cdots&a_{nn}\end{vmatrix}=\sum(-1)^{\tau(i_1i_2\cdots i_n)+\tau(j_1j_2\cdots j_n)}a_{i_1j_1}a_{i_2j_2}\cdots a_{i_nj_n}\end{aligned}$

**范德蒙德行列式**：

$\begin{aligned}\begin{vmatrix}1&1&\cdots&1\\a_1&a_2&\cdots&a_n\\a_1^2&a_2^2&\cdots&a_n^2\\\vdots&\vdots&&\vdots\\a_1^{n-1}&a_2^{n-1}&\cdots&a_n^{n-1}\end{vmatrix}=\prod_{1\leq i\leq j\leq n}(a_j-a_i)\end{aligned}$

#### 行列式的基本性质

**性质1** 转置不改变行列式。

**性质2** 如果行列式中两行（或列）互换，行列式只改变符号。

**性质3** 行列式如果有两行（或列）对应元素相等，则行列式为 $0$。

**性质4** 以数 $k$ 乘行列式中某一行（或列）中所有元素，等于用 $k$ 去乘此行列式。

**性质5** 若行列式中某一行（或列）的元素全为 $0$ ，则行列式为 $0$。

**性质6** 若行列式中有两行（或列）元素对应成比例，则行列式为 $0$。

**性质7** 行（或列）可拆分为多组后相加（分行/分列相加性）。

**性质8** 行列式的某一行（或列）元素加上另一行（或列）元素的 $k$ 倍，行列式不变。

**性质9** $n$ 阶行列式 $D=|a_{ij}|_n$ 等于它的任意一行（或列）的各元素与其对应的代数余子式乘积之和。

**性质10** $n$ 阶行列式 $D=|a_{ij}|_n$ 中某一行（或列）的各元素与另一行（或列）的对应元素的代数余子式乘积之和等于 $0$。

**性质11（Laplace定理）** 设 $D$ 为 $n$ 阶行列式，任取定其中 $k$ 行（列），由这 $k$ 行（列）构成的一切 $k$ 阶子式 $N_1,N_2,\cdots,N_t$ 与它们对应的代数余子式 $A_1,A_2,\cdots,A_t$ 乘积之和等于 $D$ ，即 $D=N_1A_1+N_2A_2+\cdots+N_tA_t$。重要推论如下：
$$\begin{vmatrix}A_{r\times r}&C_{r\times s}\\O&B_{s\times s}\end{vmatrix}=|A_{r\times r}||B_{s\times s}|$$
$$\begin{vmatrix}O&A_{r\times r}\\B_{s\times s}&C_{s\times r}\end{vmatrix}=\begin{vmatrix}C_{r\times s}&A_{r\times r}\\B_{s\times s}&O\end{vmatrix}=(-1)^{rs}|A_{r\times r}||B_{s\times s}|$$

**性质12** 两个 $n$ 阶方阵乘积的行列式等于行列式的乘积，即 $|AB|=|A||B|$。证明方法：$$|A||B|=\begin{vmatrix}A&O\\-E&B\end{vmatrix}=\begin{vmatrix}A&AB\\-E&O\end{vmatrix}=|AB|$$
**性质13** 设 $A_1,A_2,\cdots,A_m$ 都是 $n$ 阶方阵，则 $|A_1A_2\cdots A_m|=|A_1||A_2|\cdots|A_m|$。
### 矩阵及其基本运算

#### 矩阵的基本性质

**矩阵转置**：
$\begin{aligned}&(A^\mathrm{T})^\mathrm{T}=A\qquad(A+B)^\mathrm{T}=A^\mathrm{T}+B^\mathrm{T}\qquad(kA)^\mathrm{T}=kA^\mathrm{T}\\&|A|=|A^\mathrm{T}|\qquad(AB)^\mathrm{T}=B^\mathrm{T}A^\mathrm{T}\end{aligned}$  

**对称与反对称矩阵**：
对称矩阵的和、数量乘积、方幂仍为对称矩阵；反对称矩阵的和、数量乘积仍为反对称矩阵。
反对称矩阵的奇数次幂为反对称矩阵，偶数次幂为对称矩阵。
对于任意方阵 $A$ ，$A+A^\mathrm{T}$ 为对称矩阵，$A-A^\mathrm{T}$ 为反对称矩阵。奇数阶反对称矩阵的行列式为 $0$。

**矩阵的迹（Trace）**：
$n$ 阶方阵 $A=[a_{ij}]_{n\times n}$ 主对角线上元素之和称为矩阵 $A$ 的迹，记为 $\begin{aligned}\mathrm{tr}(A)=\sum_{i=1}^na_{ii}\end{aligned}$。设 $A,B$ 分别为 $m\times n$ 及 $n\times m$ 矩阵，则有 $\mathrm{tr}(AB)=\mathrm{tr}(BA)$。不存在 $n$ 阶方阵 $A,B$ 满足 $AB-BA=E$。

**逆矩阵**：
$n$ 阶方阵 $A$ 可逆 $\Leftrightarrow$ $|A|\not=0$ ，且当 $A$ 可逆时有 $A^{-1}=\dfrac{1}{|A|}A^*$。
相关运算法则：$(A^{-1})^{-1}=A\qquad(kA)^{-1}=\dfrac{1}{k}A^{-1}\qquad(A^\mathrm{T})^{-1}=(A^{-1})^{\mathrm{T}}\qquad|A^{-1}|=|A|^{-1}$

**准对角矩阵**：
$A=\mathrm{diag}[A_1,A_2,\cdots,A_t]$，有运算法则：
$AB=\mathrm{diag}[A_1B_1,A_2B_2,\cdots,A_tB_t]\qquad|A|=|A_1||A_2|\cdots|A_t|$
$A^{-1}=\mathrm{diag}[A_1^{-1},A_2^{-1},\cdots,A_t^{-1}]$

#### 初等变换与初等矩阵

**初等矩阵定义与逆**：
* 互换：$E(i,j)\qquad E^{-1}(i,j)=E(i,j)$
* 倍乘：$E(i(k))\qquad E^{-1}(i(k))=E(i(\dfrac{1}{k}))$
* 倍加：$E(i+j(k),j)\qquad E^{-1}(i+j(k),j)=E(i+j(-k),j)$

对矩阵 $A_{m\times n}$ 施行一次初等行变换相当于在左侧乘相应初等矩阵；施行一次列变换相当于在右侧乘相应初等矩阵。

**初等变换的性质**：
**性质1** 设 $A_{m\times n}$ 是秩为 $r$ 的矩阵，则存在一系列初等矩阵使得 $P_s\cdots P_1AQ_1\cdots Q_t=\begin{bmatrix}E_r&O\\O&O\end{bmatrix}$。

**性质2** 设 $A_{m\times n}$ 秩为 $r$ ，存在可逆矩阵 $P,Q$ 使 $PAQ=\begin{bmatrix}E_r&O\\O&O\end{bmatrix}$。

**性质3** $A$ 是可逆矩阵 $\Leftrightarrow$ $A$ 可以表示为初等矩阵的乘积 $\Leftrightarrow$ $A$ 仅通过初等行（或列）变换即可化为单位矩阵。

**性质4** 若 $A,B$ 均为可逆矩阵，则有 $r(AC)=r(C),r(CB)=r(C),r(ACB)=r(C)$。若 $C$ 可逆而 $A,B$ 不一定，则 $r(ACB)$ 和 $r(AB)$ 不一定相等。

#### 矩阵的秩
**性质1** $r(A+B)\leq r(A)+r(B)$。

**性质2** $r(A)+r(B)-n\leq r(AB)\leq\min\{r(A),r(B)\}$。

**性质3** $r(\begin{bmatrix}A&O\\O&B\end{bmatrix})=r(\begin{bmatrix}O&A\\B&O\end{bmatrix})=r(A)+r(B)$。

**性质4** 若 $A$ 列满秩，则 $r(AB)=r(B)$；若 $B$ 行满秩，则 $r(AB)=r(A)$。

**性质5** $r(AB)+r(BC)\leq r(B)+r(ABC)$。
### 线性空间与欧氏空间

#### 向量组与子空间
**向量组的线性相关性**：
**性质1** 一个向量组中有部分向量组线性相关，则整体必线性相关。

**性质2** 一个向量组线性无关，则其任何一个部分向量组必线性无关。

**性质3** 任何一个包含零向量的向量组必线性相关。

**性质4** 单个向量 $\alpha$ 线性相关 $\Leftrightarrow$ $\alpha=\theta$；$\alpha$ 线性无关 $\Leftrightarrow$ $\alpha\not=\theta$。

**性质5** 若两个向量组可以相互表示，则称等价；任意两个等价的线性无关向量组所含向量个数相等。

**平凡与非平凡子空间**：
设 $V$ 是线性空间，由零向量 $\{\theta\}$ 及 $V$ 自身组成的子空间称为平凡子空间，其它称为非平凡子空间（真子空间）。

**生成子空间**：
由 $\alpha_1,\alpha_2,\cdots,\alpha_t$ 生成的子空间记为 $L(\alpha_1,\cdots,\alpha_t)=\{k_1\alpha_1+\cdots+k_t\alpha_t|k_i\in P\}$。

#### 基变换与过渡矩阵
设 $(\mathrm{I}):\varepsilon_1,\cdots,\varepsilon_n$ 与 $(\mathrm{II}):\varepsilon'_1,\cdots,\varepsilon'_n$ 是 $n$ 维空间的两组基，矩阵 $M$ 满足 $[\varepsilon'_1,\cdots\varepsilon'_n]=[\varepsilon_1,\cdots\varepsilon_n]M$，则 $M$ 称为从基 $(\mathrm{I})$ 到基 $(\mathrm{II})$ 的过渡矩阵（理解为用 $(\mathrm{I})$ 的语言解读 $(\mathrm{II})$）。
若向量 $\alpha$ 在两组基下坐标为 $X_\mathrm{I}$ 和 $X_\mathrm{II}$，则坐标变换公式为 $X_\mathrm{I}=MX_\mathrm{II}$ 或 $X_\mathrm{II}=M^{-1}X_\mathrm{I}$。

#### 欧氏空间与内积
**欧氏空间定义**：
实线性空间 $V$ 若定义了满足对称性、双线性性和正定性（$(\alpha,\alpha)\geq0$ 且等于 $0\Leftrightarrow\alpha=\theta$）的实数映射 $(\alpha,\beta)$，则称为欧氏空间。欧氏空间中恒有柯西不等式：$|(\alpha,\beta)|\leq||\alpha||\cdot||\beta||$。

**常用不等式形式**：
代数形式：$(a_1b_1+\cdots+a_nb_n)^2\leq(a_1^2+\cdots+a_n^2)(b_1^2+\cdots+b_n^2)$
积分形式：$\begin{aligned}\left|\int_a^bf(x)g(x)\mathrm{d}x\right|\leq\sqrt{\int_a^bf^2(x)\mathrm{d}x\int_a^bg^2(x)\mathrm{d}x}\end{aligned}$

**度量矩阵与格拉姆行列式**：
取基 $\varepsilon_1,\cdots,\varepsilon_n$ ，记 $(\varepsilon_i,\varepsilon_j)=a_{ij}$，则实对称矩阵 $A$ 称为该基的度量矩阵。
内积可表示为：$\sum\sum x_iy_j(\varepsilon_i,\varepsilon_j)=X^{\mathrm{T}}AY$。
度量矩阵对应的行列式称为格拉姆（Gram）行列式，几何意义为基围成的平行体体积的平方。
### 特征值、特征向量与相似

#### 特征值与特征向量的性质

**性质1** $\lambda_0$ 是 $A$ 特征值的充要条件是 $|\lambda_0E-A|=0$。属于 $\lambda_0$ 的特征向量全体是 $(\lambda_0E-A)X=O$ 的非零解。特征向量个数为 $n-r(\lambda_0 E-A)$。

**性质2** 方阵 $A$ 属于不同特征值的特征向量必线性无关。

**性质3** $A$ 与对角矩阵相似的充要条件是 $A$ 的特征值重根数之和为 $n$（或有 $n$ 个线性无关的特征向量）。

**性质4** 特征多项式 $f(\lambda)=|\lambda E-A|=\lambda^n-(a_{11}+\cdots+a_{nn})\lambda^{n-1}+\cdots+(-1)^n|A|$。由此得出：$\mathrm{tr}(A)=\sum \lambda_i$ 以及 $|A|=\prod \lambda_i$。

**性质5** 若 $\xi_0$ 是 $A$ 关于 $\lambda_0$ 的特征向量，则对于多项式 $f(x)$，$f(\lambda_0)$ 是 $f(A)$ 的特征值，$\xi_0$ 仍为特征向量。

**性质6** 设 $A$ 可逆，若 $\lambda_0$ 是 $A$ 特征值（必不为 $0$），$\xi$ 是其特征向量，则 $\lambda_0^{-1}$ 是 $A^{-1}$ 的特征值，$\xi$ 仍是 $A^{-1}$ 的特征向量。

#### 矩阵的相似与对角化
**性质1** 相似矩阵有相同的特征多项式：$|\lambda E-A|=|\lambda E-B|$。

**性质2** 相似矩阵有相同的迹和行列式。

**性质3** 若 $A$ 与 $B$ 相似，则 $A^k$ 与 $B^k$ 相似；多项式矩阵 $f(A)$ 与 $f(B)$ 相似。

**性质4** 若 $A$ 可对角化即 $P^{-1}AP=\mathrm{diag}[\lambda_1,\cdots,\lambda_n]$，则 $f(A)=P\mathrm{diag}[f(\lambda_1),\cdots,f(\lambda_n)]P^{-1}$。

#### 实对称矩阵的对角化

**性质1** 实对称矩阵的特征值都是实数，特征向量都是实向量。

**性质2** 实对称矩阵的不同特征值的特征向量一定互相正交。
### 二次型与矩阵的合同

#### 二次型及其矩阵表示
**性质1** 数域 $P$ 上任意一个二次型均可经非退化线性替换化为标准型 $d_1y_1^2+\cdots+d_ny_n^2$。

**性质2** 二次型 $f=\sum\sum a_{ij}x_ix_j=X^\mathrm{T}AX$ 中，$A$ 必为对称矩阵，称为该二次型的矩阵。

**性质3** 任意对称阵 $A$ ，存在可逆矩阵 $C$ 使 $C^\mathrm{T}AC$ 为对角阵。

#### 矩阵的合同

**性质1** 若存在可逆阵 $C$ 使 $C^{\mathrm{T}}AC=B$，称 $A,B$ 合同。

**性质2** 合同关系具有自反性、对称性、传递性。

**性质3** 若 $A,B$ 合同，则 $r(A)=r(B)$，且对称性保持一致。

**性质4** 任意对称矩阵 $A$ 均与某对角阵合同，称为合同标准型。

**性质5** 任意实二次型 $X^{\mathrm{T}}AX$ 均可经正交变换 $X=UY$ 化为 $\lambda_1y_1^2+\cdots+\lambda_ny_n^2$，其中 $\lambda_i$ 为 $A$ 特征值，$U$ 为正交矩阵。

| 关系 | 定义 | 标准形 | 判别法 | 性质 |
| :---: | :---: | :---: | :---: | :---: |
| **等价** | $PAQ=B$ | $\begin{bmatrix}E_r&O\\O&O\end{bmatrix}$ | $r(A)=r(B)$ | $r(A)=r(B)$ |
| **同阶实对称矩阵合同** | $C^{\mathrm{T}}AC=B$ | $\begin{bmatrix}E_p&O&O\\O&-E_q&O\\O&O&O\end{bmatrix}$ | 秩相等且正负惯性指数相同 | 秩与惯性指数不变 |

#### 二次型的规范性
二次型标准形中，系数不为 $0$ 的平方项个数等于其矩阵的秩。
* **复数域**：任何复二次型可化为规范形 $z_1^2+\cdots+z_r^2$，规范形唯一，完全由秩决定。
* **实数域**：规范形为 $z_1^2+\cdots+z_p^2-z_{p+1}^2-\cdots-z_r^2$。正数项数 $p$ 为正惯性系数，负数项数 $r-p$ 为负惯性系数。实二次型的秩、正负惯性指数在非退化实替换下保持不变。

#### 正定二次型与正定矩阵
对于任意实向量 $X\not=O$，若 $X^{\mathrm{T}}AX>0$ 则正定；$<0$ 则负定；$\geq0$ 半正定；$\leq0$ 半负定。

**性质1** $f$ 负定（半负定） $\Leftrightarrow$ $-f$ 正定（半正定）。

**性质2** $f$ 正定 $\Leftrightarrow$ 正惯性指数为 $n$ $\Leftrightarrow$ 规范形为 $\sum y_i^2$ $\Leftrightarrow$ $A$ 特征值均 $>0$ $\Leftrightarrow$ 存在可逆阵 $B$ 使 $A=B^{\mathrm{T}}B$ $\Leftrightarrow$ $A$ 与单位矩阵 $E$ 合同。

**性质3** 实二次型 $f$ 正定 $\Leftrightarrow$ $A$ 的所有顺序主子式均大于零。负定 $\Leftrightarrow$ 奇数阶顺序主子式 $<0$，偶数阶 $>0$ (即 $(-1)^k\Delta_k>0$)。

**性质4** 若 $A$ 正定，则 $kA(k>0)$、$A^{-1}$、$A^*$、$A^k(k\in \mathbb{N}^+)$、$C^\mathrm{T}AC$ (C可逆) 均为正定矩阵。

**性质5** 若 $A,B$ 同阶正定，则 $A+B$ 及分块对角阵 $\mathrm{diag}[A,B]$ 均为正定矩阵。

**性质6（半正定）** 秩为 $r$ 的二次型半正定 $\Leftrightarrow$ 正惯性指数为 $r$ $\Leftrightarrow$ 特征值均 $\geq 0$ $\Leftrightarrow$ 存在实矩阵 $C$ 使 $A=C^\mathrm{T}C$ $\Leftrightarrow$ 所有主子式非负。
### 解题技巧与易错点总结

#### 特殊矩阵计算技巧

**爪型行列式求法**：当 $a_i\not=0$ 时：
$\begin{aligned}\begin{vmatrix}a_0&b_1&b_2&\cdots&b_n\\c_1&a_1\\c_2&&a_2\\\vdots&&&\ddots\\c_n&&&&a_n\end{vmatrix}=(a_0-\sum_{i=1}^n\frac{b_ic_i}{a_i})\prod_{i=1}^na_i\end{aligned}$

**加边法**：使 $n$ 阶行列式变为 $n+1$ 阶，通过增加的一行（列）消去其它行（列）的共同元素。

**特殊矩阵的特征值与特征向量**：

若 $A$ 特征值为 $\lambda$，特征向量为 $\xi$：

| 矩阵形式 | $aA+bE$ | $A^k$ | $f(A)$ | $A^{-1}$ | $A^*$ | $P^{-1}AP$ | $A^\mathrm{T}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **特征值** | $a\lambda+b$ | $\lambda^k$ | $f(\lambda)$ | $\lambda^{-1}$ | $|A|/\lambda$ | $\lambda$ | $\lambda$ |
| **特征向量**| $\xi$ | $\xi$ | $\xi$ | $\xi$ | $\xi$ | $P^{-1}\xi$| 视情况而定 |

若 $A$ 为分块对角阵（或分块上/下三角阵），则 $A$ 的特征值是主对角线上所有子方阵特征值的并集。

#### 常见解题思路与易错点

**易错点1（秩与零特征值）**：

“若 $A$ 的特征值中存在 $k$ 个 $0$ ,则 $r(A)=n-k$” 这个推论是**错误**的。
解释：特征值为 $0$ 的解空间即为 $A$ 的零空间。特征值 $0$ 是 $k$ 重代数根，并不代表其几何重数（即基础解系中包含的向量个数）也是 $k$。必须满足矩阵可对角化时才成立。

**易错点2（合同的判定）**：

只有**对称矩阵**才能通过“判断正负惯性系数是否相等”来判定是否合同。对于一般矩阵，只能严格使用定义判断。

**特殊特征向量的规律**：

若全 $1$ 向量 $\begin{bmatrix}1&1&\cdots&1\end{bmatrix}^{\mathrm{T}}$ 是矩阵 $A$ 的特征向量，说明 $A$ 的每一行元素之和都相等（即等于该特征值）。

**正定性的证明思维**：

正定性的根源在于特征值全部为正。若要抽象验证 $A$ 为正定矩阵，通常直接利用定义验证 $X^{\mathrm{T}}AX>0$。\
例如：已知 $A,B$ 均正定且可交换（$AB=BA$），证明 $AB$ 正定。\
思路：设 $AB\xi=\lambda\xi$ $\Rightarrow$ 左乘 $\xi^{\mathrm{T}}A^{-1}$ $\Rightarrow$ 结合 $AB=BA$ 得 $\xi^{\mathrm{T}}B\xi=\lambda\xi^\mathrm{T}A^{-1}\xi$。因 $A^{-1}$ 和 $B$ 正定，故左右二次型均为正，推得 $\lambda>0$。

**特征值性质验证思维**：
若题目要求证明两个不同矩阵具有某种一致的特征根性质，通常的破局点是**证明这两个矩阵相似**。

**维度公式**：
对于矩阵 $A\in\mathrm{R}^{m\times n}$ 有 $r(A)+\dim(\ker(A))=n$ ，其中 $\ker(A)$ 表示零空间（即方程 $AX=0$ 的解空间维度）。