---
title: Ch-3 Intro to SQL
date: 2026-03-18
type: docs
weight: "3"
---
### Domain Types

| Type                          | Explanation               |
| ----------------------------- | ------------------------- |
| `char(n)`                     | 固定长度为 $n$ 的定长字符串          |
| `varchar(n)`                  | 最大长度为 $n$ 的变长字符串          |
| `int`                         | 整数，具体实现取决于使用机器            |
| `smallint`                    | 小整数，具体实现取决于使用机器           |
| `numeric(p,d)`/`decimal(p,d)` | 定点数，共 $p$ 位有效位，小数点后 $d$ 位 |
| `real`/`double precision`     | 单精度/双精度浮点数，具体实现取决于使用机器    |
| `float(n)`                    | 浮点数，用户可自定义精度为 $n$ 位       |
>[!Note] **Note**
>1. `char(n)` 结尾没有终止符 ‘\0’ ，长度不足定长会用 **空格补齐**；
>2. `varchar(n)` 在实际实现中会在开头保留1~2个byte来保存字符串长度；
>3.  有些操作系统还会引入 `tinyint` 来表示年龄等小整数
>4. `float(n)` 中 $n$ 标准表述是十进制的有效位，而在一些数据库中表示尾数的 **二进制位数**。实际上 $n$ 的取值范围为 $[1,53]$ ，当 $n\in[1,24]$ 时，使用单精度浮点数（显式尾数23位）存储，当 $n\in[25,53]$ 时，使用双精度浮点数（显式尾数52位）存储。

### Built-in Data Types

| Type        | Explanation      | Example                  |
| ----------- | ---------------- | ------------------------ |
| `date`      | 日期，包含年月日         | `2005-7-27`              |
| `time`      | 事件，包含时分秒等        | `09:00:30`/`09:00:30.75` |
| `timestamp` | 日期与事件连接而成        | `2005-7-27 09:00:30.75`  |
| `interval`  | 时间间隔，可以由以上三者相减得到 | interval '1' day         |

日期时间相关函数：`current_date()`、`current_time()`、`year(x)`、`month(x)`、`day(x)`、`hour(x)`、`minute(x)`、`second(x)`
### Table Construction

```SQL
create table r(A1 D1,A2 D2,...An Dn,
			  (integrity-constraint1),
			  ...
			  (integrity-constraintk)
)
-- Example
create table instructor(
	ID         char(5),
	name       varchar(20) not null,
	dept_name  varchar(20),
	salary     numeric(8,2)
)
insert into instructor  values ('10211', 'Smith', 'Biology', 66000);
insert into instructor  values ('10211', null, 'Biology', 66000);
```

插入值的顺序需要与定义的 **顺序相同**，并用 null 表示空缺值。

* 主键 `primary key (A1,...,An)` 可以是一个属性或多个属性的组合，非空唯一；
* 外键 `foreign key (A1,...,An) references r` 必须满足**参照完整性**。

>[!Note] **Note**
>被设置为主键的字段强制要求非空。即使是由两个及以上字段组成的复合主键，其中的任何一个字段都不能为空。

>[!Note] **静态语义与动态语义**
>* **静态语义** 指数据库在某一静止状态下必须满足的约束条件：对于主键，指任意时刻表中任意两行的主键不相同且不允许为空；对于外键，指外键列的每个非空值都必须存在于被引用表的主键列中，如果外键列允许为空则空值不受此限。
>* **动态语义** 指数据库状态发生变化时，为了维持约束必须遵循的规则或触发动作：对于主键指更新时保证唯一非空；对于外键，指级联（父表主键更新或删除时，子表中外键值同步更新或删除）、置空（父表主键被删除或更新时，子表中外键置为空）等规则。

```SQL
create table instructor(
	ID         char(5),
	name       varchar(20) not null,   -- 非空限制
	dept_name  varchar(20),
	salary     numeric(8,2) default 0, -- 设置缺省值
	primary key (ID),
	foreign key (dept_name) references department
)
```

### Table Modification

在 **删除某字段** 时，若该字段被外键引用，有以下策略：跟随删除、置空、事务执行前检查并限制修改、事务执行时不检查结束检查后 rollback、置为缺省值。

在 **修改某字段** 时，若该字段被外键引用，有以下策略：跟随修改、置空、事务执行前检查并限制修改、事务执行时不检查结束检查后 rollback、置为缺省值。

```SQL
drop table student     -- 删除整张表和内容
delete from student    -- 删除内容但表仍然存在
alter table r add A D  -- 新增字段
alter table student add resume varchar(256); -- Example 
alter table drop A     -- 删除一个字段
```

新增一个字段，表中所有元组的该字段都会被置 null。

> [!Note] **Note**
> 修改字段，重组表的代价太大，可以通过新建一个表，复制其余内容实现。
### SQL and Relational Algebra
#### Example 1
```SQL
select A1,A2,...,An
from r1,r2,...,rm
where P
```
$\prod_{A_1,\cdots,A_n}(\sigma_P(r_1\times r_2\times\cdots\times r_m))$
#### Example 2
```SQL
select A1,A2,sum(A3)
from r1,r2,...,rm
where P
group by A1,A2
```
${\small A_1,A_2}{\large\mathcal{G}}{\small \mathrm{sum}(A_3)}{\normalsize(\sigma_P(r_1\times r_2\times\cdots\times r_m))}$
#### Example 3
```SQL
select A1,sum(A3)
from r1,r2,...,rm
where P
group by A1,A2
```
$\prod_{A_1,\mathrm{sum}A_3}({\small A_1,A_2}{\large\mathcal{G}}{\small\mathrm{sum}(A_3)\text{ as }\mathrm{sum}A_3}(\sigma_P(r_1\times r_2\times\cdots\times r_m)))$

>[!Note] **Note**
>在 `select` 中出现的非聚类列必须是 `group by` 的子集。
### The select Clause

The select clause list the attributes desired in the result of a query, corresponds to the **projection** operation of the relational algebra.

SQL names are **case insensitive**, e.g. `name`=`NAME`=`Name`.

SQL allows duplicates in relations as well as in query results. To force the elimination of duplicates, insert the keyword **distinct**  after select.

The select clause can contain **arithmetic expression** involving the operation, and operating on constants or attributes of tuples.

```SQL
select distinct dept_name -- remove duplicates
from instructor

select all dept_name -- duplicates not be removed
from instructor

select * -- all attributes
from instructor

select ID,name,salary/12 -- contain arithmetic expression
from instructor
```
### The where Clause

The where clause specifies conditions that the result must satisfy, corresponds to the **selection predicate** of the relational algebra.

Comparison results can be combined using the logical connectives **and**, **or**, and **not**. Comparisons can be applied to results of arithmetic expressions.

SQL includes a **between** comparison operator.

```SQL
select name
from instructor
where dept_name='Comp.Sci' and salay>80000

select name
from instuctor
where salary between 90000 and 100000
```
