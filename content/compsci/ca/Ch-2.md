---
title: Ch-2 存储结构层次设计
type: docs
date: 2026-03-25
weight: "2"
---
### 1. 存储层次与局部性

#### 1.1 局部性原理

存储系统设计的根本依据是程序的访存局部性（Principle of Locality）：
- **时间局部性 (Temporal Locality)**：被访问过的数据在不久的将来极可能再次被访问。如循环结构中的控制变量、频繁调用的函数等。
- **空间局部性 (Spatial Locality)**：被访问过的数据其地址相邻的数据在近期极可能被访问。如数组的顺序遍历、顺序执行的指令流等。
#### 1.2 存储器金字塔

采用极简层级分类，从上至下满足“速度递减、容量递增、单位成本递减”的物理规律。

|**层次**|**硬件技术**|**管理者**|**典型容量**|**访问延迟**|
|---|---|---|---|---|
|**L0 寄存器**|Custom CMOS|编译器|字节级|< 1 ns|
|**L1/L2 Cache**|SRAM|硬件|KB - MB 级|1 - 10 ns|
|**L3 主存**|DRAM|操作系统|GB 级|50 - 100 ns|
|**L4 辅存**|磁盘 / SSD|操作系统/用户|TB 级|毫秒 / 微秒级|

### 2. Cache 映射与结构

#### 2.1 经典映射机制

主存块（Block）如何放置到 Cache 中，决定了硬件查找的复杂度和冲突的概率。

1. **直接映射 (Direct Mapped)**
	- **规则**：一个主存块只能放在 Cache 中的唯一固定位置。
	- **公式**：$\text{Cache Index} = \text{Block Address} \bmod \text{Number of Blocks in Cache}$
	- **特点**：查找极快，硬件简单，但容易发生冲突。
2. **全相联映射 (Fully Associative)**
	- **规则**：一个主存块可以放在 Cache 中的任何位置。
	- **特点**：空间利用率最高，无冲突缺失，但需要并行比较所有 Tag，硬件成本极高。
3. **组相联映射 (Set Associative)**
	- **规则**：将 Cache 分为若干组（Set），主存块映射到固定的组，但可以放在该组内的任何位置（通常是 $n$-way）。
	- **公式**：$\text{Cache Set Index} = \text{Block Address} \bmod \text{Number of Sets in Cache}$

#### 2.2 地址划分图解

当 CPU 发出物理地址（Physical Address）时，硬件将其截断为三部分以并行查询：

```plantxt
+---------------------------+---------------+-------------+
|           Tag             |     Index     |   Offset    |
+---------------------------+---------------+-------------+
 \_________________________/ \_____________/ \___________/
        匹配块标识              定位 Cache 行    定位块内字节
```

- **块内偏移 (Offset)**：$\text{Offset Bits} = \log_2(\text{Bytes per Block})$
- **索引 (Index)**：$\text{Index Bits} = \log_2(\text{Number of Sets})$
- **标记 (Tag)**：$\text{Tag Bits} = \text{Total Address Bits} - \text{Index Bits} - \text{Offset Bits}$

> [!Note]
> 
> **有效位 (Valid Bit)** > 除了 Tag，每个 Cache 行还自带一个 Valid Bit。冷启动时全为 0，只有 Valid = 1 且 Tag 匹配时，才算真正的 **Cache Hit**。
### 3. Cache 缺失与替换

#### 3.1 3C 缺失模型

分析 Cache Miss 的根本原因，以便对症下药进行优化。

|**缺失类型**|**英文简称**|**极简释义**|**优化方向**|
|---|---|---|---|
|**强制性缺失**|Compulsory|第一次访问该数据，必然缺失。|增加块大小 (Block Size)、预取 (Prefetch)。|
|**容量性缺失**|Capacity|Cache 总容量装不下工作集，被挤出后再次访问。|增加 Cache 总容量。|
|**冲突性缺失**|Conflict|多个主存块映射到同一个 Cache 行/组，互相驱逐。|提高相联度 (Associativity)。|

#### 3.2 替换策略

在组相联或全相联中，当一组满了需要调入新块时，淘汰谁？

- **LRU (Least Recently Used)**：最近最少使用。硬件记录访问顺序，优先替换最久未被访问的块（性能好，硬件开销随相联度呈指数增加）。
- **Random**：随机替换。相联度较高（如 > 4-way）时，性能与 LRU 极其接近，且硬件实现极简。
### 4. 写入策略

#### 4.1 写命中 (Write Hit)

1. **写直达 (Write-Through)**：数据同时写入 Cache 和下层存储。保证一致性，但极慢，通常需加装 $\text{Write Buffer}$。
2. **写回 (Write-Back)**：只写 Cache，并把该行标记为 **脏块 (Dirty Bit = 1)**。直到该块被替换时才写回下层。
#### 4.2 写缺失 (Write Miss)

1. **按写分配 (Write Allocate)**：把主存块读入 Cache，然后在 Cache 内修改。通常搭配 **Write-Back**。
2. **不按写分配 (No-Write Allocate)**：绕过 Cache，直接修改下层存储。通常搭配 **Write-Through**。

### 5. 性能评估核心公式

#### 5.1 平均访存时间

衡量整个存储层级平均每次访问所需的时间。

$$\text{AMAT} = \text{Hit Time} + \text{Miss Rate} \times \text{Miss Penalty}$$

#### 5.2 CPU 访存停顿周期

计算由于等待内存而浪费的 CPU 周期总数。

$$
\begin{align}
\text{Memory Stall Cycles} &= \text{Reads} \times \text{Read Miss Rate} \times \text{Read Miss Penalty}\\ &+ \text{Writes} \times \text{Write Miss Rate} \times \text{Write Miss Penalty}
\end{align}
$$

如果是极其统一的模型，可简化为：

$$\text{Memory Stall Cycles} = \text{IC} \times \frac{\text{Memory Accesses}}{\text{Instruction}} \times \text{Miss Rate} \times \text{Miss Penalty}$$

#### 5.3 实际 CPU 执行时间

结合流水线本身的 CPI 和存储带来的停顿 CPI。

$$
\begin{align}
\text{CPU Execution Time} =& (\text{CPU Clock Cycles} + \text{Memory Stall Cycles})\\ &\times \text{Clock Cycle Time}
\end{align}
$$

或表达为实际 CPI：

$$\text{CPI}_{\text{actual}} = \text{CPI}_{\text{ideal}} + \frac{\text{Memory Accesses}}{\text{Instruction}} \times \text{Miss Rate} \times \text{Miss Penalty}_{\text{in cycles}}$$

> [!Note] **多级 Cache 的 AMAT 计算**
> 针对现代 L1 + L2 架构，公式可递归展开：
> $$\begin{align}\text{AMAT} = \text{Hit Time}_{\text{L1}} + \text{Miss Rate}_{\text{L1}} \times ( &\text{Hit Time}_{\text{L2}}\\ +& \text{Miss Rate}_{\text{L2}} \times \text{Miss Penalty}_{\text{L2}} )\end{align}$$
