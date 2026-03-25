---
title: Ch-1 量化设计与分析基础
weight: "1"
type: docs
date: 2026-03-25
---
### 1. 体系结构定义

#### 1.1 任务与组成

计算机体系结构（Computer Architecture）主要包含三个核心子类别 ：
- **指令集架构 (ISA)**：程序员编程时所使用的硬件抽象 ；
- **微架构 (Microarchitecture)**：又称计算机组织，涉及系统各部分如何互连以实现ISA ；
- **硬件系统设计 (System Design)**：包括逻辑设计、电路实现和物理实现 ；
>[!Note] **计算机设计的三个层面**
>计算机设计包含三个层面：**指令集架构**、**组织** 和 **硬件**。
#### 1.2 计算市场分类

根据目标与需求，计算机市场可划分为五大主要类别 ：

| **市场类别**              | **关键系统设计挑战**    | **核心特点与要求**                         |
| --------------------- | --------------- | ----------------------------------- |
| **PMD (个人移动设备)**      | 成本、能效、媒体性能、响应速度 | 具有多媒体用户界面的无线设备，依赖电池供电，强调实时性         |
| **Desktop (桌面计算)**    | 性价比、图形性能、能效     | 追求优化的性价比，通常最先应用最高性能的微处理器            |
| **Server (服务器)**      | 吞吐量、可用性、扩展性、能效  | 提供大规模且可靠的计算与文件服务，停机成本极高             |
| **Clusters/WSC (集群)** | 性价比、吞吐量、能效比例    | 成千上万台服务器作为一个整体运行（如SaaS），可用性和扩展性至关重要 |
| **Embedded (嵌入式)**    | 价格、能效、特定应用性能    | 严格的资源限制（内存、功耗等），要求硬/软实时性能           |
### 2. 技术与成本趋势

#### 2.1 摩尔定律与技术壁垒

- **摩尔定律 (Moore's Law)**：半导体行业指导原则，预测芯片晶体管数每1.5到2年翻一番 ；
- **带宽与延迟 (Bandwidth vs. Latency)**：在技术演进中，带宽（吞吐量）的增长速度远快于延迟（响应时间）的改善速度 ；
- **三堵墙 (Three Walls)**：现代架构设计的三大挑战为 **ILP Wall**（指令级并行收益递减）、**Memory Wall**（CPU与内存速度差距拉大）和 **Power Wall**（高频率带来高功耗）。
>[!Note] **架构演变趋势**
>* 从指令级并行 ILP 到线程级并行 TLP 、数据级并行 DLP 和请求级并行 RLP；
>* 从二维存储演变为三维立体存储（散热问题）；
>* 从单核性能提升演变为单位功耗性能设计提升。
#### 2.2 成本与价格分析

**影响成本的三要素**：时间（学习曲线与良率）、产量（规模经济）和商品化（供应商竞争） 。

**集成电路成本公式**：芯片的成本主要取决于晶圆成本、测试和封装成本 。
$$\text{Cost of die}=\frac{\text{Cost of wafer}}{\text{Dies per wafer}\times \text{Die yield}}$$

> [!Note] **设计经验法则 (Rules of Thumb)**
> 芯片良率翻倍将使成本减半；而产品销量每翻一番，成本约下降10% 。
### 3. 功耗与能效

#### 3.1 功耗类型

**动态功耗 (Dynamic Power)**：晶体管开关时消耗的能量。计算公式为： $$
\begin{align}
&\text{Power}_\text{dynamic}=\frac{1}{2}\times\text{Capacitive load}\times\text{Voltage}^2\times\text{Frequency switched}\\
&\text{Energy}_\text{dynamic}=\text{Capacitive load}\times \text{Voltage}^2
\end{align}
$$**静态功耗 (Static Power)**：晶体管关闭时由漏电流引起的功耗：$$
	\text{Power}_\text{static}=\text{current static}\times\text{Voltage}
$$
#### 3.2 优化策略
**主要节能技术**：
- **DVFS (动态电压频率调整)**：根据工作负载降低电压和频率 。
- **Overclocking (超频)**：关闭部分核心，让剩余单核以更高频率运行 。
- **Race-to-halt**：全速运行以最快完成任务，随后让系统进入深度睡眠模式 。

> [!Note] **电压与多核的能效关系**
> 电压降低10%，虽然频率和性能会有微小下降，但功耗可大幅降低30%。多核架构（在较低频率和电压下并行）通常比单核架构能提供更高的每瓦性能 (Performance per watt) 。

### 4. 可靠性与可用性

可靠性是计算机系统设计的基石，核心指标包含 ：

| 指标                                   | 定义          |                                公式                                 |
| ------------------------------------ | ----------- | :---------------------------------------------------------------: |
| **MTTF (Mean Time To Failure)**      | 平均无故障时间     |                                 /                                 |
| **MTTR (Mean Time To Repair)**       | 平均修复时间      |                                 /                                 |
| **MTBF (Mean Time Between Failure)** | 平均故障间隔时间    |               $\text{MTBF}=\text{MTTF}+\text{MTTR}$               |
| **Availability (可用性)**               | 系统正常运行时间的比例 | $\text{Availability}=\frac{\text{MTTF}}{\text{MTTF}+\text{MTTR}}$ |
| **FIT (Failure In Time)**            | 故障率         |                $\text{FIT}=\frac{1}{\text{MTTF}}$                 |

> [!Note] **Note**
> MTTF 用于衡量可靠性。FIT 通常表示为每十亿小时的故障数。在实际计算中假设：系统中任何一个部件发生故障会导致整个系统失效，各部件寿命相互独立，服从指数分布（即认为在任何时间内部件的故障率是不变的，系统失效率是各部件故障率的叠加）。

>[!TIPS] **Example**
>**Assumption**:
>- $10$ disks, $1,000,000$ hour MTTF
>- $1$ SCSI controller, $500,000$ hour MTTF
>- $1$ power supply, $1$ fan, both $200,000$ hour MTTF
>- $1$ SCSI cable, $1,000,000$ hour MTTF
>
>**Question: MTTF of the whole system**$$\begin{align}
\text{FIT}_\text{system}&=10\times\frac{1}{1,000,000}+\frac{1}{500,000}+\frac{1}{200,000}\times2+\frac{1}{1,000,000}\\&=\frac{23,000}{1000,000,000}\\
\text{MTTF}_\text{system}&=\frac{1}{\text{FIT}_\text{system}}=43,500\text{hour}\approx 5\text{years}
\end{align}
$$
### 5. 性能评估

#### 5.1 吞吐率与延迟

- **响应时间/延迟 (Response Time/Latency)**：完成单个任务所需的时间，通常是普通用户（User）最关心的指标 。
- **吞吐率/带宽 (Throughput/Bandwidth)**：单位时间内完成的总工作量，通常是系统管理员（Administrator）评估服务器时最关心的指标 。
#### 5.2 基准测试与均值

**基准测试 (Benchmarks)**：用真实应用评估最准确，业界开发了各类标准化测试集，如 **SPEC**（针对CPU和服务器）、**TPC**（针对数据库与事务处理）和 **EEMBC**（针对嵌入式微处理器）。

**如何汇总性能数据**：
- **算术平均 (Arithmetic Mean)**：适用于汇总执行时间 (Execution Time) ：
$$
\begin{align}
&\text{execution time}=\frac{1}{n}\sum_{i=1}^n\text{time}_i\\
&\text{performance}=\frac{n}{\sum_{i=1}^n\frac{1}{\text{rate}_i}}
\end{align}
$$
- **加权平均 (Weighted Arithmetic Mean)**：适用于各部分占比不同的情况：
$$
\begin{align}
&\text{execution time}=\sum_{i=1}^n\text{weight}_i\times\text{time}_i\\
&\text{performance}=\frac{1}{\sum_{i=1}^n\frac{\text{weight}_i}{\text{rate}_i}}
\end{align}
$$
- **几何平均 (Geometric Mean)**：适用于汇总归一化后的相对性能（如 SPEC Ratio），其优势在于结果不受所选参考计算机的影响 ：
$$
\text{Gmean}=\sqrt[n]{\sum_{i=1}^n\text{relative_rate}_i}=\sqrt[n]{\sum_{i=1}^n\frac{\text{time}_\text{machine}}{\text{time}_\text{reference}}}
$$

> [!Note] **关于 MIPS 指标**
> MIPS（每秒百万条指令）并不是一个完美的比较指标。有时具有复杂指令集的计算机 MIPS 较低，但因为执行所需的总指令数少，整体运行速度反而更快 。

### 6. 并行计算模型

根据指令流和数据流的数量，Flynn将计算机架构划分为以下四类 ：

1. **SISD (单指令单数据)**：传统的单处理器计算机；
2. **SIMD (单指令多数据)**：非常适合高度规律性的问题（如图像处理、向量计算、GPU）；
3. **MISD (多指令单数据)**：多个处理单元对同一数据执行不同操作；
4. **MIMD (多指令多数据)**：目前最常见的并行计算机类型，每个处理器都可以执行不同的指令流和数据流（如现代多核PC、集群）。