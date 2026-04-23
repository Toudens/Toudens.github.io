---
title: Ch-7 Rel-DB Design
date: 2026-04-14
type: docs
weight: "7"
---
### 1. 关系设计基础

#### 1.1 常见异常

不合理的数据库模式会导致 **数据冗余 (Data Redundancy)**，并可能引发以下异常现象：

- **插入异常 (Insertion Anomaly)**：若某个实体的信息不完整，就无法将其插入到数据库中。表“学生-课程-系主任”中，若一个新系还没有学生选课，就无法录入该系的系主任信息；
- **删除异常 (Deletion Anomaly)**：删除某条记录时，意外丢失了其他本该保留的信息。表“学生-课程-系主任”中，若删除该系所有学生的选课记录，该系的系主任信息也会丢失；
- **更新异常 (Update Anomaly)**：当修改某个重复出现的数据时，如果只修改了部分记录，会导致数据不一致。表“学生-课程-系主任”中，同一个系的多名学生记录里系主任姓名重复存储，若该系主任更换，只更新了部分学生的系主任字段，就会造成数据不一致。

> [!Note] **Note**
> 
> 糟糕的数据库设计往往是因为把过多的实体信息塞进了一个泛型关系中。规范化设计的核心思想就是“一事一表”，即一个关系只描述一个实体或一种联系。

#### 1.2 设计目标

关系数据库设计的核心目标是寻找一个合适的 **模式分解 (Decomposition)**，使得分解后的子模式能够消除数据冗余和操作异常，同时保留原有的数据信息和约束条件。具体地主要需要达到两个要求：消除冗余，节约存储空间和保证数据一致性。

### 2. 函数依赖
#### 2.1 函数依赖定义

**函数依赖 (Functional Dependency, FD)** 是一种完整性约束。 $r(R)$ 中的任意两个元组 $t_1$ 和 $t_2$，若它们在属性集 $\alpha$ 上的取值相等，则它们在属性集 $\beta$ 上的取值也必定相等，即：
$$
t_1[\alpha]=t_2[\alpha]\space\Rightarrow\space t_1[\beta]=t_2[\beta]
$$
则称 $\alpha$ 函数决定 $\beta$，或 $\beta$ 函数依赖于 $\alpha$，记作 $\alpha \rightarrow \beta$。

**平凡依赖 (Trivial FD)**：若 $\beta\subseteq\alpha$，那么 $\alpha\rightarrow\beta$ 永远成立，称为平凡的函数依赖。
#### 2.2 阿姆斯特朗公理

在给定的一组函数依赖集 $F$ 中，往往隐含着其他依赖。所有能由 $F$ 推导出的函数依赖集合称为 $F$ 的 **闭包 (Closure)**，记作 $F^+$。

闭包可以通过反复使用 **阿姆斯特朗公理 (Armstrong's Axioms)** 得到：
$$
\begin{cases}
\beta\subseteq\alpha
&\Rightarrow\quad
\alpha\rightarrow\beta,&\text{(reflexivity, 自反律)}\\
\alpha\rightarrow\beta
&\Rightarrow\quad
\gamma\alpha\rightarrow\gamma\beta&\text{(augmentation, 增补律)}\\
\alpha\rightarrow\beta,\beta\rightarrow\gamma
&\Rightarrow\quad
\alpha\rightarrow\gamma&\text{(transitivity, 传递律)}
\end{cases}
$$
阿姆斯特朗公理是 **正确有效 (sound)** 且 **完备 (complete)** 的，有以下补充推论：
$$
\begin{cases}
\alpha\rightarrow\beta,
\alpha\rightarrow\gamma
&\Rightarrow\quad
\alpha\rightarrow\gamma\beta
&\text{(union, 合并)}\\
\alpha\rightarrow\gamma\beta,
\alpha\rightarrow\beta
&\Rightarrow\quad
\alpha\rightarrow\gamma
&\text{(decomposition, 分解)}\\
\alpha\rightarrow\beta,
\gamma\beta\rightarrow\delta
&\Rightarrow\quad
\gamma\alpha\rightarrow\delta
&\text{(pseudotransitivity, 伪传递)}
\end{cases}
$$
#### 2.3 属性集闭包

判断一个依赖 $X \rightarrow Y$ 是否在 $F^+$ 中，直接计算 $F^+$ 开销太大。通常的做法是计算**属性集的闭包 (Closure of Attribute Set)**，记作 $X^+$。

- 算法逻辑：从 $X$ 出发，不断利用 $F$ 中的依赖向闭包中添加右部属性，直到闭包不再扩大为止。
    
- 如果最终 $Y \subseteq X^+$，则说明 $X \rightarrow Y$ 成立。
    

#### 2.4 最小覆盖

**最小覆盖 (Canonical Cover)**，也称为最小依赖集，记作 $F_c$。它是一个等价的依赖集，但没有任何冗余。

满足条件：

1. 所有函数依赖的右侧只有单一属性。
    
2. 不存在冗余的函数依赖（去掉某条规则后闭包不变）。
    
3. 不存在多余的左侧属性（即左侧不能再简化）。
    

### 3. 规范化范式

**规范化 (Normalization)** 是通过模式分解，将低级范式的关系转化为多个高级范式的关系的过程，旨在解决冗余和异常。

#### 3.1 第一范式

**第一范式 (First Normal Form, 1NF)** 要求关系中的所有属性都是**原子的 (Atomic)**，即每个属性不可再分。

- 例如，不能有“复合属性”（如将“省、市、区”写在一个字段）或“多值属性”（如一个单元格内填入多个电话号码）。
    

> [!Note]
> 
> 1NF 是关系数据库的基本要求。任何建立在传统关系型数据库（RDBMS）中的表，默认都必须满足第一范式。

#### 3.2 BCNF 范式

**BC范式 (Boyce-Codd Normal Form, BCNF)** 是一种非常严格的范式。

- 定义：对于 $F^+$ 中的所有非平凡的函数依赖 $\alpha \rightarrow \beta$，左侧 $\alpha$ 必须是关系的**超码 (Superkey)**。
    
- 意义：它消除了任何非超码属性对其他属性的决定作用，从而最大限度地消除了由函数依赖引起的数据冗余。

<img src="./ch-7-BCNFAlg.png" width="600" class="mx-auto" alt="CLC Diagram" />

#### 3.3 第三范式

**第三范式 (Third Normal Form, 3NF)** 略微放宽了 BCNF 的要求。

- 定义：对于所有非平凡的 $\alpha \rightarrow \beta$，要么 $\alpha$ 是超码，要么 $\beta$ 中的每个属性都是**主属性 (Prime Attribute)**（即包含在某个候选码中的属性）。
    
- 意义：3NF 允许非主属性依赖于主键，同时允许一定程度的主属性内部的相互依赖。它消除了非主属性对码的**传递依赖 (Transitive Dependency)**。

<img src="./ch-7-3NFAlg.png" width="600" class="mx-auto" alt="CLC Diagram" />

> [!Note]
> 
> BCNF 比 3NF 更严格。满足 BCNF 的必定满足 3NF，但满足 3NF 的不一定满足 BCNF。在实际工程设计中，3NF 往往是一个非常理想的折中点。

### 4. 模式的分解

当我们发现当前设计不满足范式时，需要将其分解为更小的关系。但分解必须遵循两项核心原则。

#### 4.1 无损连接

**无损连接分解 (Lossless-join Decomposition)** 是模式分解的**底线要求**。

- 含义：分解后的多个表，通过自然连接（Natural Join）能够完全且准确地恢复出原始表，不多出“幽灵记录”（Spurious Tuples），也不丢失原有记录。
    
- 判断条件：分解得到的子关系 $R_1$ 和 $R_2$，如果 $R_1 \cap R_2 \rightarrow R_1$ 或 $R_1 \cap R_2 \rightarrow R_2$ 成立（即公共属性是其中一个子关系的超码），则该分解是无损的。
    

#### 4.2 保持依赖

**保持依赖 (Dependency Preservation)** 是模式分解的进阶要求。

- 含义：分解后，原有的所有函数依赖约束，依然可以在局部的单个子关系中被校验，而不需要执行昂贵的跨表连接操作。
    

> [!Note]
> 
> 在分解时，无损连接是必须做到的。而保持依赖是期望做到的。在向 BCNF 分解时，有时无法兼顾“保持依赖”；但向 3NF 分解时，我们总是可以找到既无损连接又保持依赖的分解方案。

#### 4.3 分解算法

- **BCNF 分解**：不断寻找破坏 BCNF 的依赖 $\alpha \rightarrow \beta$，将原关系拆分为 $(\alpha \cup \beta)$ 和 $(R - (\beta - \alpha))$，直到所有关系都满足 BCNF。
    
- **3NF 综合算法**：通过求取最小覆盖 $F_c$，为每个依赖创建一个单独的关系模式，然后再确保包含原关系的候选码，这能完美保证无损连接和依赖保持。
    

### 5. 多值与四范

函数依赖处理的是“单值”约束，当引入多种独立的多值属性时，我们需要更高级的范式。

#### 5.1 多值依赖

**多值依赖 (Multivalued Dependency, MVD)** 描述了一种“一对多”的独立关系。记作 $X \rightarrow \rightarrow Y$。

- 现象：当一个实体有多个独立的属性集合时（例如一个老师教多门“课程”，同时有多个独立不相关的“兴趣爱好”），如果在同一个表中罗列，会产生大量的交叉组合的冗余（笛卡尔积）。
    

#### 5.2 第四范式

**第四范式 (Fourth Normal Form, 4NF)** 用于消除由多值依赖引发的冗余。

- 定义：对于每一个非平凡的多值依赖 $\alpha \rightarrow \rightarrow \beta$，左侧 $\alpha$ 必须是超码。
    
- 解决方式：将独立的多个多值属性分拆到不同的表中。满足 4NF 的关系模式也必然满足 BCNF。
    

> [!Note]
> 
> 在真实的业务开发中，大部分系统规范化到 3NF 或 BCNF 已经足够，4NF 往往在处理数组型或标签型独立列表特征时才会重点考虑使用。