---
title: Ch-3 SQL 基础
weight: "3"
type: docs
date: 2026-06-15
---

### 1. SQL 定义

#### 1.1 SQL 标准

**SQL (Structured Query Language)** 是关系数据库的标准语言。它最初来自 IBM 的 Sequel 语言和 System R 项目，后来逐渐形成 SQL-86、SQL-89、SQL-92、SQL:1999、SQL:2003、SQL:2006、SQL:2008、SQL:2011、SQL:2016、SQL:2019 等标准。

SQL 标准通常比具体数据库系统更稳定。不同数据库会支持标准的一部分，也会加入自己的扩展语法，所以学习时要区分“标准思想”和“某个系统的具体写法”。

SQL 大致包含两类核心能力：**数据定义语言 (DDL)** 用于定义关系模式、属性类型、完整性约束、索引和存储结构；**数据操作语言 (DML)** 用于查询、插入、删除和更新数据。

#### 1.2 基本类型

SQL 的属性类型用来限定一个列可以保存的值域。常见数值和字符串类型如下：

| 类型 | 含义 |
| --- | --- |
| `char(n)` | 定长字符串，长度固定为 $n$ |
| `varchar(n)` | 变长字符串，最大长度为 $n$ |
| `int` | 整数，具体范围与系统实现有关 |
| `smallint` | 小整数，范围通常小于 `int` |
| `numeric(p,d)` | 定点数，共 $p$ 位有效数字，小数点后 $d$ 位 |
| `decimal(p,d)` | 与 `numeric(p,d)` 含义基本相同 |
| `real` | 单精度浮点数 |
| `double precision` | 双精度浮点数 |
| `float(n)` | 至少有 $n$ 位精度的浮点数 |

`char(n)` 的不足部分通常用空格补齐，比较时不同系统对尾随空格的处理可能存在差异。`varchar(n)` 更适合长度差异明显的文本，但系统往往需要额外保存实际长度。

SQL 还提供日期和时间类型：

| 类型 | 含义 | 示例 |
| --- | --- | --- |
| `date` | 年、月、日 | `2005-07-27` |
| `time` | 时、分、秒 | `09:00:30.75` |
| `timestamp` | 日期和时间 | `2005-07-27 09:00:30.75` |
| `interval` | 时间间隔 | `interval '1' day` |

常用时间函数包括 `current_date`、`current_time`、`year(x)`、`month(x)`、`day(x)`、`hour(x)`、`minute(x)` 和 `second(x)`。不同系统可能要求函数名后是否带括号。

#### 1.3 创建表

`create table` 用于定义关系模式、属性类型和完整性约束。主键 `primary key` 要求非空且唯一；外键 `foreign key ... references ...` 要求引用值能在被引用关系中找到，从而维护参照完整性。

```SQL
create table instructor (
    ID        char(5),
    name      varchar(20) not null,
    dept_name varchar(20),
    salary    numeric(8,2),
    primary key (ID),
    foreign key (dept_name) references department (dept_name)
);
```

`not null` 是列级约束，表示该属性不能取空值。被声明为主键的属性自动具有非空要求；若主键由多个属性组成，则每个组成属性都不能为 `null`。

复合主键本身也表达业务语义。例如选课关系 `takes(ID, course_id, sec_id, semester, year, grade)` 可以把 `(ID, course_id, sec_id, semester, year)` 作为主键，表示同一学生在同一学期、同一课程、同一开课班次中最多出现一次。若去掉 `sec_id`，语义就会变成同一学生同一学期不能同时注册同一课程的不同班次。

#### 1.4 约束动作

外键不仅有静态约束，也有更新和删除时的动态动作。常见动作如下：

| 动作 | 含义 |
| --- | --- |
| `cascade` | 被引用元组删除或键值更新时，引用方同步删除或更新 |
| `set null` | 被引用元组删除或键值更新时，引用方外键置为 `null` |
| `set default` | 被引用元组删除或键值更新时，引用方外键置为默认值 |
| `restrict` | 如果仍有引用方元组，则拒绝本次删除或更新 |
| `no action` | 与 `restrict` 类似，但检查时机可能由系统推迟到语句或事务结束 |

```SQL
create table course (
    course_id char(8),
    title     varchar(50),
    dept_name varchar(20),
    credits   numeric(2,0),
    primary key (course_id),
    foreign key (dept_name) references department
        on delete set null
        on update cascade
);
```

使用级联动作时要特别注意影响范围。级联删除可以自动清理依赖数据，但也可能让一次删除传播到大量关系；`set null` 则要求外键列本身允许空值。

#### 1.5 修改表

`drop table` 删除关系模式和所有数据，`delete from` 只删除关系中的元组而保留表结构。`alter table` 用于修改表结构，例如新增或删除属性。

```SQL
drop table student;

delete from student;

alter table student add resume varchar(256);

alter table student drop resume;
```

新增属性时，已有元组在该属性上的值通常被置为 `null`。删除属性在部分数据库中不一定支持，即使支持也可能带来重写表数据的开销。

### 2. 基本查询

#### 2.1 查询结构

SQL 查询的基本形式是 `select ... from ... where ...`。`select` 指定输出属性，对应关系代数中的投影；`from` 指定输入关系，对应笛卡尔积或连接；`where` 指定筛选条件，对应选择。

```SQL
select A1, A2, ..., An
from r1, r2, ..., rm
where P;
```

它可以看作如下关系代数表达式：

$$
\Pi_{A_1,A_2,\ldots,A_n}(\sigma_P(r_1\times r_2\times\cdots\times r_m))
$$

SQL 的查询结果本身仍是一个关系，但 SQL 默认采用多重集语义，因此结果中允许出现重复元组。

#### 2.2 投影选择

`select` 子句可以列出属性，也可以使用表达式。`distinct` 用于消除重复元组，`all` 显式表示保留重复元组；如果省略，SQL 默认相当于 `all`。

```SQL
select distinct dept_name
from instructor;

select ID, name, salary / 12 as monthly_salary
from instructor;
```

SQL 名称通常大小写不敏感，例如 `name`、`Name` 和 `NAME` 会被视为同一个标识符。但字符串常量是否大小写敏感，要看具体字符集、排序规则和数据库配置。

`where` 子句支持比较运算、逻辑连接词 `and`、`or`、`not`，也支持 `between` 和元组比较。

```SQL
select name
from instructor
where salary between 90000 and 100000;

select name, course_id
from instructor, teaches
where (instructor.ID, dept_name) = (teaches.ID, 'Biology');
```

#### 2.3 连接查询

在 `from` 中列出多个关系时，如果没有连接条件，系统会先形成笛卡尔积。实际查询通常需要在 `where` 子句或显式连接语法中加入连接条件。

```SQL
select name, course_id
from instructor, teaches
where instructor.ID = teaches.ID;
```

`natural join` 会自动匹配所有同名属性，并且在结果中只保留一份同名属性。

```SQL
select name, course_id
from instructor natural join teaches;
```

自然连接要谨慎使用，因为它会把所有同名属性都当作连接条件。如果两个表中存在同名但语义不同的属性，查询结果就可能被错误过滤。更稳妥的方式是用 `join ... using(...)` 明确指定公共连接列。

```SQL
select name, title
from (instructor natural join teaches)
     join course using (course_id);
```

上面写法只用 `course_id` 连接课程信息，避免把 `instructor.dept_name` 和 `course.dept_name` 误认为必须相同。

#### 2.4 重命名

`as` 可以为属性或关系指定别名。属性别名常用于表达式结果，关系别名常用于自连接和相关子查询。

```SQL
select ID, name, salary / 12 as monthly_salary
from instructor;

select distinct T.name
from instructor as T, instructor as S
where T.salary > S.salary
  and S.dept_name = 'Comp. Sci.';
```

`as` 在多数位置可以省略，例如 `instructor as T` 可写成 `instructor T`。但不同数据库存在差异，例如 Oracle 在表别名中通常不写 `as`。

#### 2.5 字符串

字符串匹配使用 `like`。百分号 `%` 匹配任意长度字符串，下划线 `_` 匹配任意单个字符。

```SQL
select name
from instructor
where name like '%dar%';
```

如果需要把 `%` 或 `_` 当作普通字符匹配，可以用 `escape` 指定转义字符。

```SQL
select name
from instructor
where name like '100 \%' escape '\';
```

SQL 还常支持字符串连接、大小写转换、长度计算和子串截取等操作，例如 `upper(x)`、`lower(x)`、`length(x)`、`substring(x from m for n)`。字符串连接在标准 SQL 中常写作 `||`，但部分数据库会使用 `concat(...)` 或其它语法。

#### 2.6 排序限制

`order by` 用于控制结果显示顺序。`asc` 表示升序，`desc` 表示降序，默认一般为升序。

```SQL
select distinct name
from instructor
order by name desc;
```

排序可以使用多个关键字，前面的关键字优先级更高。

```SQL
select name, dept_name, salary
from instructor
order by dept_name asc, salary desc;
```

`limit` 用于限制返回元组数量。常见写法有 `limit row_count` 和 `limit offset, row_count`，其中 `offset` 表示跳过前多少行。

```SQL
select name
from instructor
order by salary desc
limit 3;
```

`limit` 不是所有数据库的标准写法。部分系统会使用 `fetch first n rows only`、`top n` 或其它语法。

### 3. 集合空值

#### 3.1 多重集

关系代数通常以集合为基础，而 SQL 查询默认保留重复元组，因此更接近**多重集 (Multiset)**。如果一个元组在关系 $r$ 中出现 $m$ 次，则选择运算保留满足条件的所有副本，投影也可能因为丢弃属性而产生新的重复。

在多重集语义下，如果元组 $t_1$ 在 $r_1$ 中出现 $m_1$ 次，元组 $t_2$ 在 $r_2$ 中出现 $m_2$ 次，则组合元组 $t_1t_2$ 在 $r_1\times r_2$ 中出现 $m_1m_2$ 次。

带分组的查询也可以写成扩展关系代数。下面查询先筛选，再按照 `A1,A2` 分组，并对 `A3` 求和：

```SQL
select A1, A2, sum(A3)
from r1, r2, ..., rm
where P
group by A1, A2;
```

对应表达式可以写作：

$$
_{A_1,A_2}\mathcal{G}_{\text{sum}(A_3)}(\sigma_P(r_1\times r_2\times\cdots\times r_m))
$$

如果 `select` 中没有输出全部分组属性，可以在分组后再做投影：

$$
\Pi_{A_1,\text{sum}A_3}(_{A_1,A_2}\mathcal{G}_{\text{sum}(A_3)\ \text{as}\ \text{sum}A_3}(\sigma_P(r_1\times r_2\times\cdots\times r_m)))
$$

#### 3.2 集合运算

SQL 提供 `union`、`intersect` 和 `except`，分别表示并、交、差。默认情况下，它们会消除重复元组。

```SQL
(select course_id from section where semester = 'Fall' and year = 2009)
except
(select course_id from section where semester = 'Spring' and year = 2010);
```

如果要保留重复元组，需要使用 `union all`、`intersect all` 和 `except all`。设某元组在 $r$ 中出现 $m$ 次，在 $s$ 中出现 $n$ 次，则它在 `r union all s` 中出现 $m+n$ 次。

它在 `r intersect all s` 中出现 $\min(m,n)$ 次。

它在 `r except all s` 中出现 $\max(0,m-n)$ 次。

#### 3.3 空值逻辑

`null` 表示未知、缺失或不适用的值。任何包含 `null` 的算术表达式结果通常仍为 `null`，例如 `5 + null` 的结果是 `null`。

检测空值要使用 `is null` 或 `is not null`，不能使用 `= null`。

```SQL
select name
from instructor
where salary is null;
```

涉及 `null` 的比较结果通常不是 `true` 或 `false`，而是 `unknown`。SQL 因此采用三值逻辑：`unknown or true` 为 `true`，`unknown or false` 为 `unknown`；`unknown and true` 为 `unknown`，`unknown and false` 为 `false`；`not unknown` 仍为 `unknown`。

在 `where` 子句中，只有条件结果为 `true` 的元组会被保留；结果为 `false` 或 `unknown` 的元组都会被过滤。

### 4. 聚集子查询

#### 4.1 聚集分组

聚集函数把一组值压缩为一个标量。常见聚集函数包括 `avg`、`min`、`max`、`sum` 和 `count`。

```SQL
select avg(salary)
from instructor
where dept_name = 'Comp. Sci.';

select count(distinct ID)
from teaches
where semester = 'Spring' and year = 2010;
```

`count(*)` 统计元组个数，`count(A)` 统计属性 `A` 上非空值的个数，`count(distinct A)` 统计属性 `A` 上不同非空值的个数。

`group by` 按属性值分组，每个组分别计算聚集值。使用 `group by` 时，`select` 中出现的非聚集属性必须出现在分组属性中。

```SQL
select dept_name, avg(salary) as avg_salary
from instructor
group by dept_name;
```

`where` 在分组前筛选元组，`having` 在分组后筛选分组。

```SQL
select dept_name, count(*) as cnt
from instructor
where salary >= 100000
group by dept_name
having count(*) > 10
order by cnt;
```

除 `count(*)` 以外，聚集函数通常忽略 `null`。如果输入集合中只有空值，`count` 返回 0，而 `avg`、`min`、`max` 和 `sum` 返回 `null`。

聚集条件也可以表达更细的约束。例如找出没有重名学生的院系，可比较不同姓名数和学生数：

```SQL
select dept_name
from student
group by dept_name
having count(distinct name) = count(ID);
```

如果允许极少数重名，可以写成近似比例条件：

```SQL
select dept_name
from student
group by dept_name
having 1 - count(distinct name) / count(ID) < 0.001;
```

#### 4.2 集合成员

嵌套子查询是出现在另一个 SQL 查询内部的 `select-from-where` 表达式。`in` 和 `not in` 用于测试某个值是否属于子查询结果。

```SQL
select distinct course_id
from section
where semester = 'Fall' and year = 2009
  and course_id in (
      select course_id
      from section
      where semester = 'Spring' and year = 2010
  );
```

`in` 也可以作用于元组，用来同时比较多个属性。

```SQL
select count(distinct ID)
from takes
where (course_id, sec_id, semester, year) in (
    select course_id, sec_id, semester, year
    from teaches
    where teaches.ID = '10101'
);
```

`not in` 与空值结合时需要小心。如果子查询结果中包含 `null`，比较结果可能变为 `unknown`，从而让外层元组被过滤。

#### 4.3 集合比较

`some` 表示与子查询结果中的至少一个值比较成功。若 $\theta$ 是比较运算符，则含义为：

$$
F\ \theta\ \text{some}\ r\iff \exists t\in r,\ F\ \theta\ t
$$

例如找出工资至少高于 Biology 系某位教师工资的教师：

```SQL
select name
from instructor
where salary > some (
    select salary
    from instructor
    where dept_name = 'Biology'
);
```

`= some` 等价于 `in`；但 `<> some` 只表示“不等于集合中的至少一个值”，并不等价于 `not in`。

`all` 表示与子查询结果中的所有值比较都成功，其含义为：

$$
F\ \theta\ \text{all}\ r\iff \forall t\in r,\ F\ \theta\ t
$$

例如找出工资高于 Biology 系所有教师工资的教师：

```SQL
select name
from instructor
where salary > all (
    select salary
    from instructor
    where dept_name = 'Biology'
);
```

`<> all` 等价于 `not in`。`= all` 并不等价于 `in`，它要求左侧值等于集合中的每一个值。

标量子查询用于需要单个值的位置。如果实际返回多行，系统会在运行时报错。

```SQL
select dept_name
from department
where budget = (
    select max(budget)
    from department
);
```

#### 4.4 存在测试

`exists` 测试子查询结果是否非空，`not exists` 测试子查询结果是否为空。

$$
\text{exists}\ r\iff r\ne\emptyset
$$

$$
\text{not exists}\ r\iff r=\emptyset
$$

相关子查询会引用外层查询的别名。下面查询找出同时在 2009 年 Fall 和 2010 年 Spring 开设过的课程：

```SQL
select course_id
from section as S
where semester = 'Fall' and year = 2009
  and exists (
      select *
      from section as T
      where semester = 'Spring' and year = 2010
        and S.course_id = T.course_id
  );
```

`not exists` 常用于表达“对所有”的需求。集合论中 $X-Y=\emptyset$ 等价于 $X\subseteq Y$，因此可以用双重否定写出“选修了 Biology 系所有课程的学生”：

```SQL
select distinct S.ID, S.name
from student as S
where not exists (
    (select course_id
     from course
     where dept_name = 'Biology')
    except
    (select T.course_id
     from takes as T
     where S.ID = T.ID)
);
```

`unique` 用于判断子查询结果中没有重复元组。空集没有重复元组，因此 `unique` 作用于空集时结果为 `true`。

```SQL
select T.course_id
from course as T
where unique (
    select R.course_id
    from section as R
    where T.course_id = R.course_id
      and R.year = 2009
);
```

如果要表达某门课程在 2009 年恰好开设一次，需要同时要求存在和唯一。

#### 4.5 派生关系

子查询可以出现在 `from` 子句中，此时它的结果被当作一个临时关系使用，并且通常需要给出关系别名和属性别名。

```SQL
select dept_name, avg_salary
from (
    select dept_name, avg(salary) as avg_salary
    from instructor
    group by dept_name
) as dept_avg
where avg_salary > 42000;
```

普通 `from` 子查询不能随意引用同一 `from` 子句中前面关系的别名。`lateral` 允许后面的派生关系访问前面已经定义的相关变量，但很多数据库不支持标准 `lateral`，或者使用自己的替代语法。

```SQL
select I.name, C.title
from instructor as I,
     lateral (
         select title
         from teaches natural join course
         where teaches.ID = I.ID
     ) as C;
```

### 5. 数据修改

#### 5.1 with 子句

`with` 子句可以定义只在当前查询中有效的临时视图。它适合把复杂查询拆成若干命名步骤，减少嵌套层级。

```SQL
with max_budget(value) as (
    select max(budget)
    from department
)
select dept_name
from department, max_budget
where department.budget = max_budget.value;
```

多个 `with` 关系可以互相引用前面已经定义的关系。下面查询先计算每个院系的工资总额，再找出工资总额不低于平均工资总额的院系。

```SQL
with dept_total(dept_name, value) as (
    select dept_name, sum(salary)
    from instructor
    group by dept_name
),
dept_total_avg(value) as (
    select avg(value)
    from dept_total
)
select dept_name
from dept_total, dept_total_avg
where dept_total.value >= dept_total_avg.value;
```

#### 5.2 删除

`delete from` 删除满足条件的元组。如果没有 `where` 子句，则删除关系中的所有元组，但表结构仍然保留。

```SQL
delete from instructor;

delete from instructor
where dept_name = 'Finance';
```

删除条件可以包含子查询。例如删除位于 Watson 楼的院系中的所有教师：

```SQL
delete from instructor
where dept_name in (
    select dept_name
    from department
    where building = 'Watson'
);
```

当删除条件依赖聚集结果时，SQL 会先计算子查询并确定要删除的元组集合，再执行删除；删除过程中不会因为表内容变化而反复重算条件。

```SQL
delete from instructor
where salary < (
    select avg(salary)
    from instructor
);
```

#### 5.3 插入

`insert into ... values ...` 用于插入显式给出的元组。若省略属性列表，值的顺序必须与表定义中的属性顺序一致。

```SQL
insert into course
values ('CS-437', 'Database Systems', 'Comp. Sci.', 4);

insert into course(course_id, title, dept_name, credits)
values ('CS-437', 'Database Systems', 'Comp. Sci.', 4);
```

插入时可以显式写入 `null`。

```SQL
insert into student
values ('3003', 'Green', 'Finance', null);
```

也可以把查询结果插入目标关系。此时查询会在插入任何结果前先完整求值，避免自插入查询随着插入过程不断扩大结果。

```SQL
insert into student
select ID, name, dept_name, 0
from instructor;
```

#### 5.4 更新

`update` 用于修改满足条件的元组。多条更新语句的执行顺序可能影响结果，因此条件分支通常更适合写在一个 `case` 表达式中。

```SQL
update instructor
set salary = case
    when salary <= 100000 then salary * 1.05
    else salary * 1.03
end;
```

更新语句也可以使用标量子查询。下面语句重新计算学生总学分，只统计成绩不是 `F` 且成绩非空的课程：

```SQL
update student as S
set tot_cred = (
    select case
        when sum(credits) is not null then sum(credits)
        else 0
    end
    from takes natural join course
    where S.ID = takes.ID
      and takes.grade <> 'F'
      and takes.grade is not null
);
```

如果直接使用 `sum(credits)`，没有选过课的学生会得到 `null`。用 `case` 可以把这种情况改写为 0。
