---
title: "Ch-2 Relational Model"
date: 2026-03-18
type: "docs"
---
## Basic Structure

Formally, given sets $D_1,D_2,\cdots,D_n$ a **relation** $r$ is a subset of $D_1\times D_2\times \cdots\times D_n$ .
Thus, a relation is a **set** of n-tuple $(a_1,a_2,\cdots,a_n)$ where each $a_i\in D_i$ .

$A_1,A_2,\cdots,A_n$ are attributes, $R=(A_1,A_2,\cdots,A_n)$ is a relation schema.
A relation instance $r$ defined over schema $R$ is denoted by $r(R)$ .
The current values a relation are specified by a **table**.
An element $t$ of relation $r$ is called a **tuple** and is represented by a **row** in a table.

The set of allowed values for each attribute is called the **domain** of the attribute.
Attribute values are normally required to be **atomic**, that is indivisible.

> [!NOTE] Note
> 现代的数据库对此限制有所放开，例如一些大表中还可以嵌入一些小表，并非不可分割，但是在本课程中学习的经典数据库，一般认为是不可分割的。

The special value **null** is a member of every domain.

>[!NOTE] Note
> 在C语言中，对于含有实际意义的变量，通常需要根据实际情况单独设立特殊值表示空。

Order of tuples is **irrelevant** (tuples may be stored in an arbitrary order).
**Database schema** is the logical structure of the database.
**Database instance** is a snapshot of the data in the database at a given instant in time.

## Keys and Constraint

$K$ is a **superkey** of $R$ if values for $K$ are sufficient to identify a unique tuple of each possible relation $r(R)$ .
Superkey $K$ is a **candidate key** if $K$ is minimal.
One of the candidate keys is selected to be the **primary key**.

**Foreign key** constraint from attribute $A$ of relation $r_1$ to the primary key $B$ of relation $r_2$ states that on an database instance, the value of $A$ for each tuple in $r_1$ must also be the value of $B$ for some tuple in $r_2$ .

> [!NOTE] Note
> 外键是一个表中的一个字段或一组字段，它的值必须匹配另一个表的主键或唯一值。

**Referential integrity** constraint requires that the values appearing in specified attribute $A$ of any tuples in the referencing relation $r_1$ also appear in specified attribute $B$ of at least one tuple in the referenced relation $r_2$ .

> [!NOTE] Note
> 参照完整性是一组规则，这些规则确保数据库中的数据，特别是通过外键关联的数据，是一致、准确且有效的。禁止引用不存在的内容，禁止随意删除被引用的数据。外键是实现参照完整性的具体工具。（对于课本上的时刻表与课程的红线，是为了说明此处的 `time_slot_id` 并不是 `time_slot` 的完整主键，不能用标准 SQL 外键直接实现）

## Relational Algebra

| Operator                   | Explanation & Notation                    | Example                                                  |
| -------------------------- | ----------------------------------------- | -------------------------------------------------------- |
| select $\sigma$            | 横向选择符合某性质的行 $\sigma_p(r)$                 | $\sigma_{A=B\land D>5}(r)$                               |
| project $\prod$            | 纵向选择某几列并去重 $\prod_{A_1,A_2\cdots,A_k}(r)$ | $\prod_{A,C}(r)$                                         |
| union $\cup$               | 求并集，列应相同且可兼容 $r\cup s$                    | $r\cup s$                                                |
| set difference $-$         | 差集，列应相同且可兼容 $r-s$                         | $r-s$                                                    |
| Cartesian product $\times$ | 笛卡尔积，列名称要求不同 $r\times s$                  | $r\times s$                                              |
| rename $\rho$              | 更改表的名字 $\rho _X(E)$                       | $\rho_E(\text{Employee})$                                |
| rename $\rho$              | 更改表的名字并重命名列 $\rho_{x(A_1,A_2,...)}(E)$    | $\rho_{\text{Staff}(\text{ID,Salary})}(\text{Employee})$ |
> [!Note] Note
> 找到表 $t_1$ 中属性 $A$ 的最大值：$\prod_A t_1-\prod_{t_1.A}(\sigma_{t_1.A<t_2.A}(t_1\times\rho_{t_2}(t_1)))$ 。

Multiset relational algebra 操作与上述 Relational Algebra 类似，不过没有去重步骤。

## Additional Operation

| Operator                | Explanation & Notation                                                                                                                                                                                    |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| set-intersection $\cap$ | 求交集，列应相同且可兼容<br>$r\cap s=r-(r-s)$                                                                                                                                                                         |
| natural join $\text{⋈}$        | 合并两表，保留相同列值相同的行<br>$r\text{⋈}s=\prod_{r.A,r.B,r.C,s.D}(\sigma_{r.B=s.B}(r\times s))$                                                                                                                             |
| theta join $\text{⋈}_\theta$   | 合并两表，保留符合表达式的行<br>$r\text{⋈}_\theta s=\sigma_\theta(r\times s)$                                                                                                                                                  |
| semijoin $\text{⋉}_\theta$     | 在 $\text{⋈}_\theta$ 的基础上，只保留在 $r$ 中的列，即不合并<br>$r\text{⋉}_\theta s=\prod_R(r\text{⋈}_\theta s)$                                                                                                                                 |
| assignment $\leftarrow$ | 将复杂的计算过程拆解为简单步骤，用于赋值临时变量<br>$\text{Temp}\leftarrow \text{Expression}$                                                                                                                                     |
| left outer join $\text{⟕}$      | 在 $\text{⋈}$ 的基础上加入左侧的缺省行<br>$r\text{⟕}s=(r\text{⋈}s)\cup(r-\prod_R(r\text{⋈}s))\times\{(\text{null},...)\})$                                                                                                                         |
| right outer join $\text{⟖}$     | 在 $\text{⋈}$ 的基础上加入右侧的缺省行<br>$r\text{⟖}s=(r\text{⋈}s)\cup\{(\text{null},...)\}\times(s-\prod_S(r\text{⋈}s))$                                                                                                                          |
| full outer join $\text{⟗}$      | 在 $\text{⋈}$ 的基础上加入两侧的缺省行<br>$r\text{⟗}s=(r\text{⟕}s)\cup(r\text{⟖}s)$                                                                                                                                                                |
| division $\div$         | 满足 $t\times s\subseteq r$ 的最大集合 $t$<br>$\text{temp}_1\leftarrow\prod_{R-S}(r)$<br>$\text{temp}_2\leftarrow\prod_{R-S}((\text{temp}_1\times s)-\prod_{R-S,S}(r))$<br>$r\div s=\text{temp}_1-\text{temp}_2$ |

> [!Note] Note
> natural join 满足结合律，即 $(A\text{⋈}B)\text{⋈}C=A\text{⋈}(B\text{⋈}C)$ ，同时，若不考虑列的顺序问题，natural join 同时还满足交换律，即 $A\text{⋈}B=B\text{⋈}A$ 。

Comparisons with null values return the special truth value: **unknown**.
In SQL "P is unknown" evaluates to **true** if predicate P evaluates to unknown.
unknown or true = true/ false and known = false/ not known = known .

## Generalized Projection

Extends the projection operation by allowing **arithmetic functions** to be used in the projection list $\prod_{F_1,F_2,\cdots,F_n}(E)$ , where $E$ is any relational-algebra expression.

Given relation instructor (ID, name, dept\_name, salary) where salary is annual salary, get the same information but with monthly salary : $\prod_{\text{ID,name,dept\_name,salary/12}}(\text{instructor})$

> [!Note] Note
> 在使用 generalized projection 时，经常使用"算术式 as 新列名"的方式来规定列名。

## Aggregate Functions

**Aggregate Function** takes a collection of values and returns a single value as a result, including **avg**, **min**, **max**, **sum**, **count**, ...
$$
{\small G_1,G_2,\cdots,G_n}\ {\LARGE\mathcal{G}}\ {\small F_1(A_1),F_2(A_2),\cdots,F_n(A_n)}\normalsize(E)
$$
* $G_1,G_2,\cdots,G_n$ is a list of attributes on which to group (can be empty)
* Each $F_i$ is an aggregate function
* Each $A_i$ is an attribute name

Result of aggregation does not have a name. Can use rename operation to give it a name. For convenience, we permit renaming as part of aggregate operation. 
$$
{\small \text{dept_name}}\ {\LARGE\mathcal{G}}\ {\small\text{avg(salary) as avg_sal}} (\text{instructor}) 
$$