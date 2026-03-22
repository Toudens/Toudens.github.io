---
title: Ch-3 Intro to SQL
date: 2026-03-18
type: docs
weight: "3"
---
### Data Types

#### Domain Types

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
>3. 有些操作系统还会引入 `tinyint` 来表示年龄等小整数；
>4. `float(n)` 中 $n$ 标准表述是十进制的有效位，而在一些数据库中表示尾数的 **二进制位数**。实际上 $n$ 的取值范围为 $[1,53]$ ，当 $n\in[1,24]$ 时，使用单精度浮点数（显式尾数23位）存储，当 $n\in[25,53]$ 时，使用双精度浮点数（显式尾数52位）存储。

#### Built-in Data Types

| Type        | Explanation      | Example                  |
| ----------- | ---------------- | ------------------------ |
| `date`      | 日期，包含年月日         | `2005-7-27`              |
| `time`      | 时间，包含时分秒等        | `09:00:30`/`09:00:30.75` |
| `timestamp` | 日期与时间连接而成        | `2005-7-27 09:00:30.75`  |
| `interval`  | 时间间隔，可以由以上三者相减得到 | interval '1' day         |

日期时间相关内置函数：`current_date()`、`current_time()`、`year(x)`、`month(x)`、`day(x)`、`hour(x)`、`minute(x)`、`second(x)`。

### Table Construction & Modification

#### Table Construction

插入值的顺序需要与定义的 **顺序相同**，并用 `null` 表示空缺值。主键 `primary key` 可以是一个属性或多个属性的组合，非空且唯一；外键 `foreign key` 必须满足**参照完整性**。

```SQL
create table instructor(
	ID         char(5),
	name       varchar(20) not null,   -- 非空限制
	dept_name  varchar(20),
	salary     numeric(8,2) default 0, -- 设置缺省值
	primary key (ID),
	foreign key (dept_name) references department (dept_name)
        on delete cascade
        on update cascade
);

insert into instructor values ('10211', 'Smith', 'Biology', 66000);
insert into instructor values ('10212', null, 'Biology', 66000);
```

>[!Note] **Note**
>被设置为主键的字段强制要求非空。即使是由两个及以上字段组成的复合主键，其中的任何一个字段都不能为空。

>[!Note] **静态语义与动态语义**
>* **静态语义** 指数据库在某一静止状态下必须满足的约束条件：对于主键，指任意时刻表中任意两行的主键不相同且不允许为空；对于外键，指外键列的每个非空值都必须存在于被引用表的主键列中，如果外键列允许为空则空值不受此限。
>* **动态语义** 指数据库状态发生变化时，为了维持约束必须遵循的规则或触发动作：对于主键指更新时保证唯一非空；对于外键，指级联（`cascade`：父表主键更新或删除时，子表中外键值同步更新或删除）、置空（`set null`：父表主键被删除或更新时，子表中外键置为空）、限制（`restrict`）或缺省（`set default`）等规则。

>[!Note] **Note**
>复合主键的设计需要注意业务语义。例如在定义选课表 `takes` 时，如果从主键 `(ID, course_id, sec_id, semester, year)` 中删除 `sec_id`，则意味着强制约束：一个学生在同一个学期内不能注册同一门课程的两个不同 section。

#### Table Modification

新增一个字段时，表中所有元组的该字段都会被置为 `null`。

```SQL
drop table student;                          -- 删除整张表和内容
delete from student;                         -- 删除内容但表仍然存在
alter table student add resume varchar(256); -- 新增字段
alter table student drop resume;             -- 删除一个字段（部分数据库不支持）
```

>[!Note] **Note**
>直接修改表结构中字段（特别是删除或更改类型）会导致重组表的代价太大。实际应用中，通常可以通过新建一个表，复制其余内容来实现结构的修改。

### SQL and Relational Algebra

SQL 的核心查询结构可以等价转换为多重集关系代数（Multiset Relational Algebra）。

```SQL
select A1, A2, .. An
from r1, r2, ..., rm
where P
```
等价于：$\prod_{A_1,\cdots,A_n}(\sigma_P(r_1\times r_2\times\cdots\times r_m))$

```SQL
select A1, A2, sum(A3)
from r1, r2, ..., rm
where P
group by A1, A2
```
等价于：${\small A_1,A_2}{\large\mathcal{G}}{\small \mathrm{sum}(A_3)}{\normalsize(\sigma_P(r_1\times r_2\times\cdots\times r_m))}$

```SQL
select A1, sum(A3)
from r1, r2, ..., rm
where P
group by A1, A2
```
等价于：$\prod_{A_1,\mathrm{sum}A_3}({\small A_1,A_2}{\large\mathcal{G}}{\small\mathrm{sum}(A_3)\text{ as }\mathrm{sum}A_3}(\sigma_P(r_1\times r_2\times\cdots\times r_m)))$

>[!Note] **Note**
>在带有 `group by` 的查询中，在 `select` 子句中出现的非聚合属性，**必须**是 `group by` 列表中列出的属性（子集）。

### Basic Query Structure

SQL 数据操作语言 (DML) 提供了信息查询能力，典型查询由 `select ... from ... where ...` 构成，查询的返回结果本身也是一个关系（表）。
#### The select Clause
对应关系代数中的**投影（Projection）**操作。
* `distinct` 用于强制消除重复元组；`all` 显式指定保留重复元组。
* 星号 `*` 代表查询所有属性。
* 可以在选择子句中包含 `+`、`-`、`*`、`/` 等算术表达式。

```SQL
select distinct dept_name 
from instructor;

select ID, name, salary/12 
from instructor;
```

>[!Note] **Note**
>SQL 的名称（包括保留字和列名）是**大小写不敏感（case insensitive）**的。例如 `Name` $\equiv$ `NAME` $\equiv$ `name`。

#### The where Clause
对应关系代数中的**选择（Selection）**操作，用于指定结果必须满足的条件。
* 支持逻辑连接词：`and`、`or`、`not`。
* 支持 `between` 比较运算符。
* 支持元组级别的对比（Tuple comparison）。

```SQL
select name
from instructor
where salary between 90000 and 100000;

select name, course_id
from instructor, teaches
where (instructor.ID, dept_name) = (teaches.ID, 'Biology');
```

#### The from Clause & Joins
对应关系代数中的**笛卡尔积（Cartesian product）**操作。它列出了查询涉及的所有关系，生成所有可能的元组对。
**自然连接（Natural Join）**会匹配所有同名属性值相同的元组，并且对于同名的公共列，结果集**只保留一个副本**。

```SQL
select name, course_id
from instructor natural join teaches;

select name, title
from (instructor natural join teaches) join course using(course_id);
```

>[!Note] **Note**
>使用 `natural join` 时，要小心不同表中含义不同但**恰好同名**的属性被错误地强制等同（例如 `course.dept_name = instructor.dept_name`）。为了避免这种情况，建议在涉及多表关联时使用 `join ... using(属性名)` 来明确指定需要匹配的列。

#### The Rename Operation
SQL 提供 `as` 关键字用于重命名关系或属性：`old-name as new-name`。

```SQL
select ID, name, salary/12 as monthly_salary
from instructor;

select distinct T.name
from instructor as T, instructor as S
where T.salary > S.salary and S.dept_name = 'Comp. Sci.';
```

>[!Note] **Note**
>关键字 `as` 是可选的（如 `instructor as T` 等同于 `instructor T`）。但是在 **Oracle 数据库** 中，重命名表时**必须省略** `as` 关键字。

#### String Operations
SQL 的字符串匹配比较算符为 `like`，它使用两个特殊字符来描述模式（模式匹配是**区分大小写**的）：
* **百分号（`%`）**：匹配任意长度的子串。
* **下划线（`_`）**：匹配任意单个字符。

```SQL
select name
from instructor
where name like '%dar%';

select name
from instructor
where name like '100 \%' escape '\';
```

#### Ordering the Display of Tuples
支持对一个或多个属性进行排序。

```SQL
select distinct name
from instructor
order by dept_name, name desc;
```

>[!Note] **Note**
>排序时，`desc` 表示降序（Descending order），`asc` 表示升序（Ascending order）。默认情况下，缺省行为是升序。

#### The limit Clause
用于约束 `select` 语句返回的行数。参数为非负整数：`limit offset, row_count` 或者 `limit row_count`（等价于 `limit 0, row_count`）。

```SQL
select name
from instructor
order by salary desc
limit 3;
```

### Set Operations

集合运算包括：`union`（并集）、`intersect`（交集）、`except`（差集）。

```SQL
(select course_id from section where sem = 'Fall' and year = 2009)
except
(select course_id from section where sem = 'Spring' and year = 2010);
```

>[!Note] **Note**
>上述默认的集合运算会**自动消除重复元组**。要在多重集（Multiset）关系中保留所有的重复副本，必须使用其对应的多重集版本：`union all`、`intersect all` 以及 `except all`。
>假设元组在 $r$ 中出现 $m$ 次，在 $s$ 中出现 $n$ 次，则它出现：
>* $m + n$ 次在 `r union all s` 中
>* $\min(m,n)$ 次在 `r intersect all s` 中
>* $\max(0, m - n)$ 次在 `r except all s` 中

### Null Values

`null` 代表缺失或未知的状态。
* 任何包含 `null` 的算术表达式结果均为 `null`（例如 `5 + null` 为 `null`）。
* 使用谓词 `is null` 专门用于检测空值。
* 含有空值的比较运算会返回一种特殊的逻辑真值：**unknown**。

```SQL
select name
from instructor
where salary is null;
```

>[!Note] **Note**
>SQL 中的三值逻辑（true, false, unknown）：
>* **OR**: (`unknown` or `true`) = `true`, (`unknown` or `false`) = `unknown`, (`unknown` or `unknown`) = `unknown`
>* **AND**: (`true` and `unknown`) = `unknown`, (`false` and `unknown`) = `false`, (`unknown` and `unknown`) = `unknown`
>* **NOT**: (`not unknown`) = `unknown`
>
>如果谓词 $P$ 的计算结果为 `unknown`，则 `P is unknown` 的结果为 `true`。但对于查询，如果 `where` 谓词最终计算为 `unknown`，SQL 将会把它当作 `false` 处理（即不返回该元组）。

### Aggregate Functions

聚合函数操作给定关系某一列的多重集值，并返回一个标量：`avg`（平均值）、`min`（最小值）、`max`（最大值）、`sum`（求和）、`count`（计数）。

```SQL
select dept_name, count(*) as cnt
from instructor
where salary >= 100000
group by dept_name
having count(*) > 10
order by cnt;
```

>[!Note] **Note**
>聚合查询执行的生命周期：
>`where` 子句中的谓词在形成分组**之前**应用（用于初步过滤数据），而 `having` 子句中的谓词在形成分组**之后**应用（用于过滤计算后的聚合组）。
>需要注意的是，使用 `group by` 时，数据源中不存在或者没有匹配记录的分组（例如没有讲师的部门）将不会出现在最终结果中。

>[!Note] **Null Values and Aggregates**
>除 `count(*)` 以外，所有的聚合操作都会在运算时**忽略**对应属性上的 `null` 值。如果被聚合的字段集合中仅仅只包含空值，则 `count` 返回 0，而其余所有的聚合函数都会返回 `null`。

### Nested Subqueries

嵌套子查询是位于另一个查询内部的 `select-from-where` 表达式，常用于检测集合的成员资格、集合比较及集合基数。

#### Set Membership (`in` / `not in`)
用于判断某个值是否包含在子查询生成的集合中。

```SQL
select count(distinct ID)
from takes
where (course_id, sec_id, semester, year) in
      (select course_id, sec_id, semester, year
       from teaches
       where teaches.ID = '10101');
```

#### Set Comparison (`some` / `all`)
将某个值与子查询生成集合中的值进行大于/小于比较。

```SQL
select name
from instructor
where salary > all (select salary
                    from instructor
                    where dept_name = 'Biology');
```

>[!Note] **Note**
>**标量子查询（Scalar Subquery）**是指预期仅返回单个数值的子查询（例如被用在需要具体数值的算术运算或比较处）。如果该子查询在实际执行时返回了多于一个结果元组，将会导致系统产生运行时错误（Runtime error）。

#### Test for Empty Relations (`exists` / `not exists`)
`exists` 用于测试子查询的返回结果是否为非空集合：
* `exists` $r \iff r \neq \emptyset$
* `not exists` $r \iff r = \emptyset$

可以与关联变量（Correlation Variables）一起构成**相关子查询（Correlated subquery）**。

```SQL
-- 相关子查询，外部表的 S 被内部子查询引用
select course_id
from section as S
where semester = 'Fall' and year = 2009 and 
      exists (select *
              from section as T
              where semester = 'Spring' and year = 2010 
              and S.course_id = T.course_id);
```

>[!Note] **Note**
>集合论中有 $X - Y = \emptyset \iff X \subseteq Y$。因此，如果我们需要实现“找到选修了生物系开设的所有课程的学生” 这类存在普遍性量化关系的查询，可以使用双重否定 `not exists (Y except X)` 来实现。注意该查询在 SQL 中不能直接使用 `= all` 及其变体来编写。

#### Test for Absence of Duplicate Tuples (`unique`)
`unique` 结构用于测试子查询结果中是否存在任何重复的元组。

```SQL
select T.course_id
from course as T
where unique (select R.course_id
              from section as R
              where T.course_id = R.course_id and R.year = 2009);
```

>[!Note] **Note**
>`unique` 判断的是是否没有重复。当其测试的子查询计算结果为一个**空集（empty set）**时，`unique` 的求值结果依然为 `true`。

### The with Clause

`with` 子句提供了一种定义**临时视图**的方法，该视图的定义仅在包含此 `with` 子句的当前查询生命周期内有效。这对于编写极其复杂的查询非常有用。

```SQL
with dept_total (dept_name, value) as
     (select dept_name, sum(salary)
      from instructor
      group by dept_name),
     dept_total_avg (value) as
     (select avg(value)
      from dept_total)
select dept_name
from dept_total, dept_total_avg
where dept_total.value >= dept_total_avg.value;
```

### Modification of the Database

#### Deletion
从给定关系中删除元组。

```SQL
delete from instructor
where salary < (select avg(salary) from instructor);
```

>[!Note] **Note**
>当基于聚合运算的结果进行数据删除时，为避免数据不断变化导致基准改变，SQL 的执行方案是：首先计算出平均薪水并找到所有符合删除条件的元组，**然后**再统一次性执行删除操作。在实际的逐行删除过程中，不会重新计算平均值或重新测试元组。

#### Insertion
向给定关系插入新的元组。

```SQL
insert into course (course_id, title, dept_name, credits)
values ('CS-437', 'Database Systems', 'Comp. Sci.', 4);

insert into student
select ID, name, dept_name, 0
from instructor;
```

>[!Note] **Note**
>在执行插入操作时，`select from where` 语句在将其任何结果插入目标表之前会被**完全计算出来**。否则，如果目标表 `table1` 没有定义主键，类似于 `insert into table1 select * from table1` 的自引式查询会导致无限循环插入的问题。

#### Updates
更新特定元组的值。如果有多个更新逻辑分支，为防止多条单独的 `update` 语句的执行顺序导致数据被二次覆盖，推荐在单条更新中使用 `case` 语句。同时可以在更新中结合标量子查询使用。

```SQL
-- 使用 Case 语句执行多分支安全更新
update instructor
set salary = case
    when salary <= 100000 then salary * 1.05
    else salary * 1.03
    end;

-- 结合子查询的更新
update student S 
set tot_cred = (select case 
                       when sum(credits) is not null then sum(credits)
                       else 0
                       end
                from takes natural join course
                where S.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);
```