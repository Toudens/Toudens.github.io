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

| **层次**          | **硬件技术**    | **管理者** | **典型容量** | **访问延迟**   |
| --------------- | ----------- | ------- | -------- | ---------- |
| **L0 寄存器**      | Custom CMOS | 编译器     | 字节级      | < 1 ns     |
| **L1/L2 Cache** | SRAM        | 硬件      | KB\~MB 级 | 1\~10 ns   |
| **L3 主存**       | DRAM        | 操作系统    | GB 级     | 50\~100 ns |
| **L4 辅存**       | 磁盘 / SSD    | 操作系统/用户 | TB 级     | 毫秒 / 微秒级   |
> [!Note] **Performance of Main Memory**
> * **access time** 读取请求发出到请求的 word 抵达所用的时间；
> * **cycle time** 相邻两次读取请求的最小时间间隔。

#### 1.3 DRAM

**DRAM** 实现中分为 **bank, row, column 三级结构**。预充电命令用于打开或关闭存储库， row 地址通过激活命令发送，随后该 row 的数据被传输至 **缓冲区**，对于缓冲区中的 row，可以通过连续的通过连续的 column 地址进行传输。

为了提升传输速率等性能， DRAM 引入了：
* **DDR (double data rate) 技术**，在时钟的上升和下降沿均传输数据；
* 将单个 SDRAM 拆分成多个 banks，可以 **独立进行数据传输**；
* 分为动态和静态耗能，当 DRAM 被设置为 power down mode 时 **停止非必要刷新**。

为适应 GPU 等并行处理器对数据传输的要求，有 bandwidth 更高的 GDRAM (Graphic)。
#### 1.4 Flash Memory

**Flash Memory** 是一种 EEPROM（电可擦可编程只读存储器）类型。只读，但可擦除，具有 **非易失性**（无需电源即可保持数据），用作便携式设备的主存。

Flash Memory 与 DRAM 的不同之处：
* 写入前必须先 **以块为单位** 擦除；
* 具有非易失性，功耗更低；
* 每个块都有有限的写入次数；
* 比 SDRAM 便宜但慢，比硬盘贵但块；
* 采用写入均衡技术，确保写入操作在整个存储中 **均匀分布**。
#### 1.5 错误与检测纠正

**软错误/瞬态故障（soft error/transient fault）** 指由外部干扰引起的存储单元内容翻转，但硬件电路本身没有物理损坏，是瞬时、可恢复的。

**硬错误/永久性故障（hard error/permanent fault）** 指由硬件电路物理缺陷导致某个存储单元或电路功能永久失效的错误，是不可恢复的，必须通过冗余或替换来规避。

**检测纠正技术**：奇偶校验 parity，纠错码 ECC（典型配置为每64位数据额外增加8位检验位，可纠正1位错误，检测2位错误），Chipkill（将 ECC 类似于 RAID 分散到芯片上）。

### 2. Cache 结构与机制

#### 2.1 映射机制

主存块（Block）如何放置到 Cache 中，决定了硬件查找的复杂度和冲突的概率。

1. **直接映射 (Direct Mapped)**
	- **规则**：一个主存块只能放在 Cache 中的唯一固定位置。
	- **公式**：$\text{Cache Index} = \text{Block Address} \bmod \text{Number of Blocks in Cache}$
	- **特点**：查找极快，硬件简单，但容易发生冲突。
2. **全相联映射 (Fully Associative)**
	- **规则**：一个主存块可以放在 Cache 中的任何位置。
	- **特点**：空间利用率最高，无冲突缺失，但需要并行比较所有 Tag，硬件成本极高。
3. **组相联映射 (Set Associative)**
	- **规则**：将 Cache 分为若干组（Set），主存块映射到固定的组，但可以放在该组内的任何位置（通常是 $n$-way，即 $n$-way 中任何位置）。
	- **公式**：$\text{Cache Set Index} = \text{Block Address} \bmod \text{Number of Sets in Cache}$
#### 2.2 地址划分

当 CPU 发出物理地址（Physical Address）时，硬件将其截断为三部分以并行查询：

```plantxt
+---------------------------+---------------+------------------+
|           Tag             |     Index     |    Byte Offset   |
+---------------------------+---------------+------------------+
 \_________________________/ \_____________/ \________________/
        匹配块标识              定位 Cache 行       定位块内字节
```

- **块内偏移 (Byte Offset)**：$\text{Byte Offset Bits} = \log_2(\text{Bytes per Block})$
- **索引 (Index)**：$\text{Index Bits} = \log_2(\text{Number of Sets})$
- **标记 (Tag)**：$\text{Tag Bits} = \text{Total Address Bits} - \text{Index Bits} - \text{Offset Bits}$

> [!Note] **有效位 (Valid Bit)**
> 除了 Tag，每个 Cache 行还自带一个 Valid Bit。冷启动时全为 0，只有 Valid = 1 且 Tag 匹配时，才算真正的 **Cache Hit**。
#### 2.3 缺失与替换

| **缺失类型**              | **释义**                      | **优化方向**                          |
| --------------------- | --------------------------- | --------------------------------- |
| **强制性缺失 Compulsory**  | 第一次访问该数据，必然缺失。              | 增加块大小 (Block Size)、预取 (Prefetch)。 |
| **容量性缺失 Capacity**    | Cache 总容量装不下工作集，被挤出后再次访问。   | 增加 Cache 总容量。                     |
| **冲突性缺失<br>Conflict** | 多个主存块映射到同一个 Cache 行/组，互相驱逐。 | 提高相联度 (Associativity)。            |

* **LRU (Least Recently Used)**：最近最少使用。硬件记录访问顺序，优先替换最久未被访问的块（性能好，硬件开销随相联度呈指数增加）。
- **Random**：随机替换。相联度较高时，性能与 LRU 极其接近，且硬件实现极简。
#### 2.4 写入策略

* **写命中（Write Hit）**
	1. **写直达 (Write-Through)**：数据同时写入 Cache 和下层存储。保证一致性，但极慢，通常需加装 Write Buffer；
	2. **写回 (Write-Back)**：只写 Cache，并把该行标记为 **脏块 (Dirty Bit = 1)**。直到该块被替换时才写回下层。
* **写缺失（Write Miss）**
	1. **按写分配 (Write Allocate)**：把主存块读入 Cache，然后在 Cache 内修改；
	2. **不按写分配 (No-Write Allocate)**：绕过 Cache，直接修改下层存储。。

按写分配通常搭配写回策略，不按写分配通常搭配写直达策略。
### 3. Cache 六种基本优化
#### 3.1 增大块大小

*  **优点** ：利用空间局部性降低缺失率，标签位数量减少降低静态功耗；
*  **缺点** ：会增加缺失代价（Miss Penalty），增加容量缺失与冲突缺失的情况。

衡量整个存储层级平均每次访问所需的时间 **AMAT** (Average Memory Access Time)。
$$
\begin{align}
\text{AMAT} 
&= (1-\text{Miss Rate})\times\text{Hit Time} + \text{Miss Rate} \times \text{Miss Time}\\
&=(1-\text{Miss Rate})\times\text{Hit Time}+\text{Miss Rate}\times(\text{Hit Time}+\text{Miss Penalty})\\
&=\text{Hit Time}+\text{Miss Rate}\times\text{Miss Penalty}
\end{align}
$$
#### 3.2 增大容量

* **优点** ：减少容量缺失的情况，降低缺失率；
* **缺点** ：会增加命中时间、成本和功耗。
#### 3.3 增大关联度

* **优点** ：减少冲突缺失的情况，降低缺失率；
* **缺点** ：会增加命中时间和功耗。

>[!Note] **cache rule of thumb**
> A direct-mapped cache of size $N$ has about the same miss rate as a two-way set associative cache of size $N/2$.
#### 3.4 多级缓存

* **优点** ：兼具大 Cache 减少冲突缺失和小 Cache 速度快的优点，降低缺失代价和功耗；
* **缺点** ：增加硬件设计复杂度，带来额外的功耗。

两级 Cache 架构的 **平均访存时间 AMAT** 计算：
$$\begin{align}\text{AMAT} = \text{Hit Time}_{\text{L1}} +& \text{Miss Rate}_{\text{L1}} \\&\times (\text{Hit Time}_{\text{L2}} + \text{Miss Rate}_{\text{L2}} \times \text{Miss Penalty}_{\text{L2}} )\end{align}$$ 两级缓存系统中，处理器因等待数据而 **平均每条指令停顿的时钟周期数**：
$$
\begin{align}
\text{Average mem}&\text{ stalls per instruction}\\
=&\text{Misss per instr}_\text{L1}\times\text{Hit time}_\text{L2}
+\text{Miss per instr}_\text{L2}\times\text{Miss Penalty}_\text{L2}
\end{align}
$$
Cache 性能指标公式：
$$
\text{CPU Exe Time}=(\text{CPU clock cycles}+\text{Memory stall cycles})\times\text{Clock Cycle Time}
$$
$$
\begin{align}
\text{Memory Stall Cycles}
&=\text{Number of Misses}\times\text{Miss Penalty}\\
&=\text{IC}\times\frac{\text{Misses}}{\text{Instruction}}\times\text{Miss Penalty}\\
&= \text{IC} \times \frac{\text{Memory Accesses}}{\text{Instruction}} \times \text{Miss Rate} \times \text{Miss Penalty}
\end{align}
$$
$$
\begin{align}
\text{Memory Stall}& \text{ Clock Cycles}\\ =& \text{IC}\times \text{Reads per inst} \times \text{Read Miss Rate} \times \text{Read Miss Penalty}\\ +& \text{IC}\times \text{Writes per inst} \times \text{Write Miss Rate} \times \text{Write Miss Penalty}
\end{align}
$$

* **Local miss rate** : 缓存中的缺失次数除以该缓存收到的访问总次数 The number of misses in a cache divided by the total number of mem accesses to this cache；
* **Global miss rate** : 缓存中的缺失次数除以处理器产生的总访问次数 The number of misses in the cache divided by the number of mem accesses gen by the processor。

L1 缓存中的数据和 L2 缓存中的数据有包含或互斥两种处理策略：
* **Multilevel inclusion** : L1 缓存中的数据始终存在于 L2 缓存中，仅需针对 L2 缓存进行一致性检查，从而简化一致性维护；
* **Multilevel exclusion** : L2 缓存容量略大于 L1 时，L1 缓存中的数据不会出现在 L2 中，当 L1 缺失时，会在 L1 和 L2 之间进行块互换。
#### 3.5 读缺失优先于写操作

* 降低缺失代价，引入写缓冲滞后执行写操作。

**具体实现逻辑**：当发生读缺失时，不再简单地让读请求一直阻塞，直到写缓冲区完全清空；先检查写缓冲区的内容，如果读请求要访问的地址与写缓冲区中待写的地址没有冲突，并且内存系统当前可用，就允许读请求先执行，而写操作可以继续在后台排队；只有当读请求与写缓冲区存在地址冲突时，才需要等待相关写操作完成，以保证数据一致性。
#### 3.6 虚拟索引物理标签

* **优点**：降低命中时间，使用页内偏移量作为缓存索引，采用虚拟索引、物理标签。
* **缺点**：进程切换时，相同虚拟地址可能对应不同物理地址，需要处理缓存别名问题。

![](graph/Ch-2-Cache.png)

> [!Note] **Note**
> * 传统方式使用 **串行** 方法，即先将虚拟地址通过 TLB 转换为物理地址，再将物理地址高位作为 tag，中间部分作为 index，低位作为 byte offset 读取。
> * 用页内偏移量作为缓存索引时，利用虚拟地址和物理地址的 page offset 相同的特性，**并行** 处理 TLB 转换物理地址和索引 cache 两个操作，从而做到更快读取。需要注意的是，在物理地址转换完成后仍然需要比对 tag 来判断是否 Hit。
> * page offset = index + byte offset ，两种方法的 **地址划分相同但时序不同**。
### 4. 虚拟内存

#### 4.1 虚拟内存四问

1. **虚拟内存的块放置在哪里**：全相连策略，虚拟内存的块允许放置在主存的任何位置，因为发生页面/地址错误时，访问硬盘等存储设备会导致很高的缺失代价。
2. **如何找到块放置在哪里**：使用页表来记录虚拟地址与物理地址之间的映射关系，页表中的每个条目记录了某个虚拟页映射到哪个物理页，然后利用虚拟地址中包含的偏移量，即可在物理页中定位到确切的数据。
3. **块缺失的替换策略**：替换最近最少使用的块 LRU (Least Recently Used)，使用一个“使用位”，在访问某个块时对该位进行标记，未标记使用位的块就可被选为替换目标。
4. **虚拟内存的写回策略**：访问硬盘等存储设备耗时大，使用脏位 （Dirty Bit），仅当块从磁盘读入后被修改过，才将其写回磁盘。
#### 4.2 页表与 TLB

**页表** 存储在主存中，一次数据访问需要 **两次内存访问**：从页表中获取物理地址和从物理地址获取数据。为了加速数据访存的速度，引入 TLB 缓存用于缓存先前完成的地址转换。

**TLB** 是一种特殊的缓存 Cache，每个条目记录一个从虚拟页号到物理页号的先前映射关系，每个表目分成两部分：**标签** 部分记录虚拟页号，**数据** 部分记录物理页号。**使用位** 用于跟踪已访问的页面；**脏位** 用于跟踪已修改的页面；**有效位** 标记有效才能匹配成功。

![](graph/Ch-2-TLB.png)

>[!Note] **TLB 访存流程** 
>1. 虚拟内存地址 page number 与 TLB 中的所有 tag 进行比对；
>2. TLB 中匹配的物理地址会被发送给多选器；
>3. 将物理地址与 page offset 拼接得到最终的物理地址；

![](graph/Ch-2-TLB-2.png)
#### 4.3 页面尺寸

* **大页面尺寸的优势**：
	1. **页表更小**：占用更少内存，减少页表存储开销；
	2. **缓存命中更快**：可以利用更大的缓存块或更高的 TLB 覆盖范围，提升缓存命中率；
	3. **I/O 效率更高**：与二级存储之间传输大页面更高效，减少传输次数和开销；
	4. **减少 TLB 缺失**：单个TLB条目可映射更大的内存区域，从而降低TLB缺失率。
* **小页面尺寸的优势**：
	1. **节省存储空间**：小页面可减少内部碎片，避免浪费内存；
	2. **更细粒度的内存管理**：适合对内存使用要求紧凑的场景，减少因对齐造成的空间浪费。

大页面可显著减少TLB缺失（某些程序中对 CPI 的影响甚至与缓存缺失相当），小页面能减少内部碎片，近年来的微处理器普遍支持 **多种页面大小**（如4KB、2MB、1GB）。操作系统可根据应用的内存访问模式动态选择合适的页面大小，在TLB覆盖率和内存利用率之间取得平衡。
$$
\text{Virtual Memory}=\text{main Memory}+\text{Secondary Storage}
$$
### 5. Cache 十种进阶优化

#### 5.1 小而简单的一级缓存

**原理**：较小容量可以支持更快的时钟频率（电信号传输、多选器延迟等因素），降低功耗。

* 采用较低的关联度（如直接映射），使标签检查和数据传输 **并行**，缩短命中时间。
#### 5.2 缓存路预测

**原理**：在保持高关联度的同时，减少冲突缺失并缩短命中时间。

* 为每个缓存块添加 **块预测位 (block predictor bits)**，预测下一次访问的“路”。预测命中则仅执行一次标签比较；失败则在下一周期检查其他块。
#### 5.3 流水线与缓存划分

**原理**：提高缓存带宽，减少访问缓存过程中器件的空闲时长。

* 类比于 CPU 流水线，将缓存访问过程划分为多个 **流水级**，虽然增加了单次访问的延迟 (latency)，但极大地提升了指令吞吐量；
* 将缓存分为多个 **独立的存储体 (bank)** ，支持同时被访问，通过顺序交错 (Sequential Interleaving) 的地址映射方式，将连续的块地址轮流分到各个存储体中。

![[graph/Ch-2-MultiBank.png]]
#### 5.4 非阻塞缓存

**原理**：在发生缓存缺失时，允许处理器继续为后续的命中请求提供服务，而不必停顿。

对非阻塞缓存的支持程度包含以下几类：
1. Hit under miss: 一个未命中发生时，后续的 **命中** 请求可以正常完成；
2. Miss under miss: 多个未命中可以 **并发处理**（第二个未命中可在第一个完成前发出）；
3. Hit under multiple misses: 多个未命中并发进行时，仍能处理新的命中请求。

* 内存访问延迟可能达到数百个周期，如果只处理一个未命中，当程序存在多个缓存缺失时，后续的未命中必须等待前一个完成才能发出请求，无法利用内存的并行性，支持miss under miss 可以让处理器同时发出多个内存请求，**并行处理隐藏延迟**；
* 支持并发未命中的数量 **并不是越多越好**，每个未命中的状态都需要独立的存储、缺失状态保持寄存器等硬件，条目越多，硬件成本与复杂度越高，资源冲突可能性也越大。
#### 5.5 关键字优先与早重启

**原理**：针对大缓存块，不需要等待这个块加载完毕，优先满足处理器的字需求。

* **关键字优先 (Critical Word First)**：优先请求缺失的字，一旦到达立即送往处理器，处理器在执行的同时填充大缓存块的剩余部分；
* **尽早重启动 (Early Restart)**：按照正常顺序传输大缓冲块，但目标字一旦到达就送往处理器执行，同时按顺序继续传输剩余部分。
#### 5.6 合并写缓冲区

**原理：** 将同一缓存行内的连续写操作合并，减少对下级存储器的写操作次数。

* 检查写缓冲区 (write buffer) 中已有的地址，如果新写入的数据地址与已有条目 **连续**，则将其合并为单个物理条目（中间不能有空洞），以减少写操作次数。

>[!Note] **Example**
>
>假设写缓冲每个条目可以存放一个 64 字节的缓存行，且支持部分写入，CPU 依次执行以下写操作（地址按照字节寻址）：
>1. 写入地址 0x1000，4 字节数据 A；
>2. 写入地址 0x1004，4 字节数据 B；
>3. 写入地址 0x1008，4 字节数据 C；
>
>* 如果写缓冲区 **不支持合并**，那么三个写操作会占用三个独立的条目，最终需要向下级存储发出三次写入请求（即使它们可能属于同一个缓存行）。
>* 如果 **支持合并**，则有效范围最终扩展为 0x1000~0x100B。只有一个条目被发送到下级存储，合并为一次写操作。

实际硬件设计会根据以下规则判断是否可以合并：
* **地址对齐**：通常以缓存行为边界。合并只允许在同一个缓存行内进行。
* **连续性**：新写入的地址与已有条目的地址范围必须恰好连续（即首尾相接），不能有空洞。有些设计也允许重叠，这时需要更新已有数据；
* **掩码支持**：每个条目通常带有一个 **字节掩码（byte mask）**，用于标记哪些字节是有效数据。合并时只需更新掩码和数据部分，无需移动其他数据。
#### 5.7 编译器优化

* **循环交换 (Loop Interchange)：** 改变嵌套循环顺序，使访问模式符合数据在内存中的存储顺序，提升空间局部性；

```C++
// Program 1 
// 相邻的 a[i][j] 和 a[i+1][j] 相距 1024 个整数，空间局部性极差
for(int j=0;j<1024;j++)
for(int i=0;i<1024;i++)
	sum+=a[i][j];

// Program 2 
// 每次缺失载入的后 15 个整数均 hit，缺失率降到原来的约 1/16
for(int i=0;i<1024;i++)
for(int j=0;j<1024;j++)
	sum+=a[i][j];
```

* **分块 (Blocking)：** 将大型矩阵运算划分为较小的子块 (sub-blocks)，确保子块能完全装入缓存，提升时间局部性。
```C++
// Program 1 
// 由于矩阵规模远超缓存容量，导致数据在重用前被频繁替换，时间局部性极差
// 当计算 c[i][j+1] 时，之前为 c[i][j] 加载的 b 列数据可能已经被替换
for(int i=0;i<N;i++)
for(int j=0;j<N;j++)
for(int k=0;k<N;k++)
	c[i][j]+=a[i][k]*b[k][j];

// Program 2 
// 限制访问范围确保子块驻留在缓存中，提升时间局部性，数据重用率提升约 B 倍
// 处理方块时 B*B 块大小小于缓存容量，a 和 b 的数据会驻留在缓存中
// 若 B 太小则无法充分利用缓存空间，理想的 B 应使 a,b,c 块综合略小于缓存有效容量
for(int j_st=0;j_st<N;j_st+=B)
for(int k_st=0;k_st<N;k_st+=B)
{
	int j_ed=std::min(j_st+B,N);
	int k_ed=std::min(k_st+B,N);
	for(int i=0;i<N;i++)
	{
		for(int j=j_st;j<j_ed;j++)
		{
			int tmp=0;
			for(int k=k_st;k<k_ed;k++)
				tmp+=a[i][k]*b[k][j];
			c[i][j]+=tmp;
		}
	}
}

```

>[!Note] **Note**
>**软件优化的优势：** 编译器优化不需要任何硬件改动，通过纯软件手段就能显著降低缺失率 (miss rate)，是现代高性能计算的核心。
#### 5.8 硬件预取

**原理**：硬件根据访问模式预测未来需要的数据，提前将其加载到缓存或**指令流缓冲区 (instruction stream buffer)** 。

* 发生未命中时取回两个块，将请求的块放入缓存，下一个连续的块放入指令流缓冲区。
* 如果请求的块已经在流缓冲区中，则取消原本的缓存请求，然后从流缓冲区读取该块并发出下一个预取请求。
#### 5.9 编译器预取

**原理**：编译器在代码中显式插入 **预取指令 (prefetch instructions)**。

* 分为 **寄存器预取** 和 **缓存预取**。将预取操作的时间与流水线执行重叠，有效隐藏缺失惩罚。

```C++
// 16-byte blocks, 8-byte elements for a and b, write back

// Program 1 251 misses
// a 每相邻两次发生一次 miss,一共发生了 3*(100/2) = 150 misses
// b 从 0 至 100 各发生一次 miss,一共发生了 101 misses
for(int i=0;i<3;i++)
	for(int j=0;j<100;j++)
		a[i][j]=b[j][0]+b[j+1][0];

// Program 2 19 misses
// a 是 4 misses 因为在预取的时，相邻的两次有一次 hit
// b 是 7 misses 因为在预取的时，列相距远全部 miss
// 预取指令 prefetch(+7) 意味着处理器尝试提前加载 7 轮之后才用得到的数据
for(int j=0;j<100;j++)
{
	prefetch(b[j+7][0]); // b[0][0]~b[6][0] 7 misses
	prefetch(a[0][j+7]); // a[0][0]~a[0][6] 4 misses
	a[0][j]=b[j][0]*b[j+1][0];
}
for(int i=1;i<3;i++)
	for(int j=0;j<100;j++)
	{
		prefetch(a[i][j+7]); // a[1][0]~a[1][6] 4 misses
		a[i][j]=b[j][0]*b[j+1][0]; // a[2][0]~a[2][6] 4 misses
	}
```
#### 5.10 HBM 优化

**原理**：利用高带宽内存 (High Bandwidth Memory, HBM) 作为巨大的 L4 缓存 。

传统 HBM 的访存过程一个简单表述为：
1. **行激活 (ACT)**：根据地址打开 HBM 内部的一个数据行，搬运几 KB 数据到行缓冲区；
2. **列寻址 (CAS)**：在缓冲区中定位到 Tag 所在的列并读出；
3. **比对与传输**：CPU 比对 Tag，若 Hit，则发起第二次列寻址读出 Data，若 Data 不在已经激活的数据行中，则需要再激活其所在的数据行；
4. **突发传输 (Burst)**：数据通过 1024-bit 位宽的总线高速传回 CPU；
5. **预充电 (PRE)**：关闭当前行，准备下次访问。

由于 L4 容量巨大，会导致标签 (tags) 数据量极其庞大，通常需要两次 DRAM 访问（一次查标签进行地址翻译，一次 Hit 后查数据） ，针对此问题有以下优化策略：
1. 将标签和数据放在 DRAM 的同一行 (same row) 中，不需要再激活 row buffer；
2. 采用 **合金缓存 (Alloy cache)** ：将标签和数据结构性地融合在一起（直接映射结构），Hit 直接读数据以加快访问速度，使得只需单次 HBM 周期就能进行突发传输 (burst transfer) 同时获取标签和数据；
3. 使用映射表 (map) 或访存预测器 (memory access predictor) 加快未命中检测速度。