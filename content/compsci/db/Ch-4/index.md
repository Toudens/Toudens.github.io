---
title: Ch-4 SQL 进阶
type: docs
weight: "4"
date: 2026-03-24
---

### 1. 连接关系

#### 1.1 连接基础

**连接关系 (Joined Relation)** 是 SQL 在 `from` 子句中组合多个关系的方式。连接操作接收两个关系，返回一个新的关系；它不仅决定哪些元组能够匹配，也决定结果中保留哪些属性。

连接语法可以从两个角度理解：

| 角度 | 含义 | 常见写法 |
| --- | --- | --- |
| 连接条件 | 判断两个关系中的元组是否匹配 | `natural`、`on <predicate>`、`using (...)` |
| 连接类型 | 处理没有匹配元组的一侧 | `inner join`、`left/right/full outer join` |

**自然连接 (Natural Join)** 会自动按照两个关系中的同名属性做等值匹配，并且同名属性只在结果中保留一份。**条件连接 (Join on)** 使用 `on` 后的谓词判断是否匹配，适合属性名不同或连接条件更复杂的情况。**using 连接** 则显式指定用于匹配的一组同名属性。

```SQL
select *
from course inner join prereq
    on course.course_id = prereq.course_id;

select *
from course natural join prereq;

select *
from course full outer join prereq using (course_id);
```

>[!Note] **Note**
>`natural join` 虽然写起来短，但它依赖同名属性自动匹配。如果两个关系后来新增了同名但语义无关的属性，查询含义可能被悄悄改变。实际写业务 SQL 时，`join ... on ...` 通常更可控。

#### 1.2 外连接

**内连接 (Inner Join)** 只保留两侧都能匹配的元组。若某门课程没有先修课，或某条先修课记录找不到对应课程，内连接都会丢弃这些不匹配元组。

**外连接 (Outer Join)** 用 `null` 保留不匹配的一侧，从而避免信息丢失：

| 类型 | 保留内容 | 不匹配位置 |
| --- | --- | --- |
| `left outer join` | 保留左侧全部元组 | 右侧属性填 `null` |
| `right outer join` | 保留右侧全部元组 | 左侧属性填 `null` |
| `full outer join` | 保留两侧全部元组 | 缺失一侧填 `null` |

```SQL
select *
from course natural left outer join prereq;

select count(*)
from course natural right outer join prereq
where prereq_id is null;

select *
from course natural full outer join prereq;
```

外连接的核心不是“多连接一些表”，而是在普通连接结果之外，把没有匹配成功的元组补回结果。由于补回的元组缺少另一侧属性，只能用 `null` 表示未知或不存在。

### 2. 类型系统

#### 2.1 内置类型

SQL 支持日期、时间、时间戳和时间间隔等内置类型。日期和时间值相减会得到 **间隔 (Interval)**，间隔也可以再加回日期、时间或时间戳。

```SQL
date '2005-7-27'
time '09:00:30'
time '09:00:30.75'
timestamp '2005-7-27 09:00:30.75'
interval '1' day
```

常见时间函数包括：

| 函数 | 含义 |
| --- | --- |
| `current_date()` | 当前日期 |
| `current_time()` | 当前时间 |
| `year(x)`、`month(x)`、`day(x)` | 提取日期部分 |
| `hour(x)`、`minute(x)`、`second(x)` | 提取时间部分 |

这些类型的意义不只是格式检查。数据库知道一个值是日期或时间后，才能正确执行比较、排序、间隔计算和函数提取。

#### 2.2 自定义类型

**用户定义类型 (User-Defined Type)** 可以给已有类型起一个具有业务语义的新名字。例如预算金额可以定义为 `Dollars`：

```SQL
create type Dollars as numeric(12, 2) final;

create table department (
    dept_name varchar(20),
    building varchar(15),
    budget Dollars
);
```

`create type` 类似 C 语言中的 `typedef`。`final` 表示该类型不能继续派生。需要注意的是，即使两个用户定义类型底层都是 `numeric(12, 2)`，只要类型名不同，系统也会把它们视为不同类型。

**域 (Domain)** 也是基于已有类型建立的新类型，但它可以附带约束，因此更适合表达“某类值必须满足什么条件”。

```SQL
create domain person_name char(20) not null;

create domain degree_level varchar(10)
    constraint degree_level_test
    check (value in ('Bachelors', 'Masters', 'Doctorate'));
```

类型偏重命名和区分，域偏重约束和检查。实际设计中，如果某个值不仅有名字，还有稳定的取值规则，使用 domain 会更清晰。

#### 2.3 大对象

**大对象 (Large Object)** 用于保存图片、视频、CAD 文件等体积很大的数据。SQL 中常见两类大对象：

| 类型 | 含义 |
| --- | --- |
| `blob` | binary large object，未解释的二进制数据 |
| `clob` | character large object，大型字符数据 |

MySQL 中常见的 BLOB 大小如下：

| 类型 | 大小 |
| --- | --- |
| `TinyBlob` | 0 到 255 bytes |
| `Blob` | 0 到 64 KB |
| `MediumBlob` | 0 到 16 MB |
| `LargeBlob` | 0 到 4 GB |

>[!Note] **Note**
>出于性能考虑，查询返回大对象时，数据库通常先返回指向该对象的定位信息，而不是立刻把整个大对象读入结果。应用真正需要内容时，再通过该定位信息取回完整对象。

### 3. 完整约束

#### 3.1 单表约束

**完整性约束 (Integrity Constraint)** 用于防止合法用户的更新破坏数据一致性。例如余额不能低于某个值、员工工资不能低于最低工资、客户电话不能为空，这些都属于完整性规则。

单个关系上常见约束包括：

| 约束 | 含义 |
| --- | --- |
| `not null` | 属性值不能为空 |
| `primary key` | 主键，唯一且非空 |
| `unique` | 候选键约束，要求组合值唯一 |
| `check (P)` | 每行必须满足谓词 $P$ |

```SQL
create table section (
    course_id varchar(8),
    sec_id varchar(8),
    semester varchar(6),
    year numeric(4, 0),
    building varchar(15),
    room_number varchar(7),
    time_slot_id varchar(4),
    primary key (course_id, sec_id, semester, year),
    check (semester in ('Fall', 'Winter', 'Spring', 'Summer'))
);
```

`primary key` 一定隐含非空；`unique` 声明的是候选键或超键，但 SQL 允许其中出现 `null`。组合唯一约束判断的是属性组整体是否重复，不是每个属性单独不能重复。

```SQL
create table enrollment (
    enrollment_id int primary key,
    student_id int not null,
    course_id int not null,
    enroll_date date,
    unique (student_id, course_id)
);
```

#### 3.2 参照完整

**参照完整性 (Referential Integrity)** 要求一个关系中出现的某组属性值，也必须出现在另一个关系的主键属性中。若 `instructor.dept_name = 'Biology'`，则 `department` 中必须存在主键为 `'Biology'` 的部门。

设 $A$ 是关系 $R$ 和 $S$ 都包含的一组属性，且 $A$ 是 $S$ 的主键。如果 $R$ 中任意出现的 $A$ 值都必须同时出现在 $S$ 中，则 $A$ 是 $R$ 引用 $S$ 的 **外键 (Foreign Key)**。

```SQL
create table course (
    course_id char(5) primary key,
    title varchar(20),
    dept_name varchar(20),
    foreign key (dept_name) references department
        on delete cascade
        on update cascade
);
```

当被引用元组被删除或主键被更新时，系统可以采取不同动作：

| 动作 | 含义 |
| --- | --- |
| `cascade` | 级联删除或级联更新引用方 |
| `set null` | 将引用方外键设为 `null` |
| `set default` | 将引用方外键设为默认值 |
| `restrict` | 拒绝破坏参照完整性的操作 |

#### 3.3 复杂约束

有些约束会跨越多行或多个关系。例如每个开课记录都必须至少有一位教师，或者 `student.tot_cred` 必须等于该学生所有已通过课程学分之和。理论上，`check` 中可以写子查询：

```SQL
check (time_slot_id in (
    select time_slot_id
    from time_slot
))
```

但很多数据库并不支持在 `check` 中使用子查询。工程上通常通过 **触发器 (Trigger)** 或应用层逻辑实现这类复杂检查。

SQL 还定义了 **断言 (Assertion)**，用于表达整个数据库必须始终满足的全局约束：

```SQL
create assertion credits_earned_constraint check
    (not exists (
        select ID
        from student
        where tot_cred <> (
            select sum(credits)
            from takes natural join course
            where student.ID = takes.ID
              and grade is not null
              and grade <> 'F'
        )
    ));
```

这里用 `not exists` 表达“所有学生都满足条件”。这种写法本质上是“不存在违反条件的学生”。很多数据库没有原生实现 `assertion`，因此复杂完整性规则仍然常由触发器实现。

#### 3.4 事务延迟

约束检查有时不能逐条语句立刻完成。例如 `person` 表中 `father` 和 `mother` 都引用同一个 `person` 表：

```SQL
create table person (
    ID char(10),
    name char(40),
    mother char(10),
    father char(10),
    primary key (ID),
    foreign key (father) references person,
    foreign key (mother) references person
);
```

如果先插入孩子，父母记录还不存在，会违反外键；如果先插入父母，又可能缺少其它相互引用关系。常见处理方式有三种：

| 方法 | 适用情况 |
| --- | --- |
| 先插入被引用元组 | 引用方向明确、无环 |
| 先把外键设为 `null`，之后更新 | 外键允许为空 |
| 延迟到事务结束检查 | 多条语句合起来才满足约束 |

延迟检查体现了事务的意义：单条语句执行后数据库可以暂时处在中间状态，但事务提交时必须恢复一致。

### 4. 视图机制

#### 4.1 视图定义

**视图 (View)** 是由查询表达式定义的虚拟关系。它不属于概念模型中的基本关系，却可以像普通关系一样暴露给用户。视图常用于隐藏敏感属性、简化复杂查询，或在底层结构变化时保持上层接口稳定。

```SQL
create view faculty as
    select ID, name, dept_name
    from instructor;

select name
from faculty
where dept_name = 'Biology';
```

上面的视图让用户看到教师编号、姓名和院系，但看不到工资。视图定义保存的是查询表达式，而不是立即创建一张新表。

视图还可以基于已有视图继续定义：

```SQL
create view physics_fall_2009 as
    select course.course_id, sec_id, building, room_number
    from course, section
    where course.course_id = section.course_id
      and course.dept_name = 'Physics'
      and section.semester = 'Fall'
      and section.year = 2009;

create view physics_fall_2009_watson as
    select course_id, room_number
    from physics_fall_2009
    where building = 'Watson';
```

#### 4.2 视图展开

**视图展开 (View Expansion)** 是把查询中出现的视图名替换为该视图的定义。对于：

```SQL
select course_id, room_number
from physics_fall_2009
where building = 'Watson';
```

系统可以将它展开为：

```SQL
select course_id, room_number
from (
    select course.course_id, building, room_number
    from course, section
    where course.course_id = section.course_id
      and course.dept_name = 'Physics'
      and section.semester = 'Fall'
      and section.year = 2009
)
where building = 'Watson';
```

进一步合并条件后，查询就回到底层关系 `course` 和 `section` 上执行。`from` 子句中出现子查询，本质上也是把一个查询结果当作临时关系使用。

#### 4.3 视图更新

视图更新的问题在于：对虚拟关系的插入、删除或修改，必须能唯一翻译成底层关系上的操作。简单视图通常可以更新：

```SQL
create view faculty as
    select ID, name, dept_name
    from instructor;

insert into faculty values ('30765', 'Green', 'Music');
```

这个插入可以翻译为：

```SQL
insert into instructor
values ('30765', 'Green', 'Music', null);
```

如果底层 `instructor` 中未出现在视图里的属性定义为 `not null`，上面的插入就会失败。更复杂的视图可能根本无法唯一更新：

```SQL
create view instructor_info as
    select ID, name, building
    from instructor, department
    where instructor.dept_name = department.dept_name;
```

若插入 `('69987', 'White', 'Taylor')`，系统无法判断该教师属于 `Taylor` 楼里的哪一个院系。因此多数 SQL 实现只允许更新简单视图。

可更新视图通常需要满足：

| 条件 | 原因 |
| --- | --- |
| `from` 中只有一个基本关系 | 避免无法判断更新哪张表 |
| `select` 中只包含属性名 | 表达式、聚集值无法直接写回 |
| 未列出的属性可以设为 `null` | 插入时需要补齐底层元组 |
| 不含 `group by` 和 `having` | 分组结果不对应单个底层元组 |
| 不含 `distinct` | 去重后无法确定原始元组 |

#### 4.4 物化视图

**物化视图 (Materialized View)** 会把视图查询结果真实存成一张物理表。它牺牲存储空间和维护成本，换取查询速度。

```SQL
create materialized view departments_total_salary(dept_name, total_salary) as
    select dept_name, sum(salary)
    from instructor
    group by dept_name;

select dept_name
from departments_total_salary
where total_salary > (
    select avg(total_salary)
    from departments_total_salary
);
```

底层关系更新后，物化视图会变旧，因此系统必须维护它。维护方式可以是完全重新计算，也可以是增量更新。分析型查询中，物化视图常用于预先保存昂贵的聚集结果。

#### 4.5 数据独立

视图还能实现 **逻辑数据独立性 (Logical Data Independence)**。例如原来有关系 `S(a, b, c)`，后来为了物理设计或列式存储，将其拆成 `S1(a, b)` 和 `S2(a, c)`。为了不修改上层查询，可以创建一个同名视图：

```SQL
create view S(a, b, c) as
    select a, b, c
    from S1 natural join S2;
```

这样，用户仍然可以执行：

```SQL
select *
from S
where a = 1;
```

底层实际访问的则是 `S1 natural join S2`。视图在这里充当稳定接口，使应用不必感知底层关系被拆分或重组。

### 5. 索引事务

#### 5.1 索引基础

**索引 (Index)** 是用于加速记录访问的物理结构。没有索引时，系统可能需要扫描整个 `student` 表；有索引时，可以先通过索引定位满足条件的记录。

```SQL
create table student (
    ID varchar(5),
    name varchar(20) not null,
    dept_name varchar(20),
    tot_cred numeric(3, 0) default 0,
    primary key (ID)
);

create index studentID_index on student(ID);

select *
from student
where ID = '12345';
```

索引适合建在查询频繁使用的属性上。复合索引中属性顺序不同，得到的索引也不同。例如 `(dept_name, ID)` 和 `(ID, dept_name)` 支持的高效访问路径并不相同。

>[!Note] **Note**
>索引属于物理层优化，不改变查询结果。它会占用额外存储空间，并在插入、删除、更新时带来维护成本。因此索引不是越多越好，而是要服务于高频查询和关键约束。

#### 5.2 事务边界

**事务 (Transaction)** 是数据库执行的工作单元。一个事务中的操作要么全部生效，要么全部回滚，不能只完成一半。

```SQL
set autocommit = 0;

update account
set balance = balance - 100
where ano = '1001';

update account
set balance = balance + 100
where ano = '1002';

commit;
```

多数数据库默认每条 SQL 自动提交，因此每条语句本身就是一个事务。关闭自动提交后，事务从第一条语句隐式开始，由 `commit` 或 `rollback` 结束。

| 命令 | 含义 |
| --- | --- |
| `commit` | 提交当前事务，使修改永久生效 |
| `rollback` | 回滚当前事务，撤销尚未提交的修改 |
| `set autocommit = 0` | 关闭自动提交，手动控制事务边界 |

事务边界需要按业务语义划分。买一张票和买多张票是否属于一个事务，订票和支付是否必须放在同一个事务中，都取决于业务希望“全有全无”的范围。事务越长，越容易持有锁并阻塞其它事务。

#### 5.3 ACID

数据库通过 **ACID** 性质保证事务可靠执行：

| 性质 | 含义 |
| --- | --- |
| 原子性 (Atomicity) | 事务中的操作全做或全不做 |
| 一致性 (Consistency) | 事务在隔离执行时保持数据库约束 |
| 隔离性 (Isolation) | 并发事务之间看不到彼此的中间结果 |
| 持久性 (Durability) | 事务提交后，即使系统故障，修改也不会丢失 |

隔离性可以用事务 $T_i$ 和 $T_j$ 来理解：对 $T_i$ 而言，$T_j$ 要么像是在 $T_i$ 开始前已经完成，要么像是在 $T_i$ 完成后才开始。这个“看起来串行”的效果，是并发控制要实现的核心目标。

### 6. 权限控制

#### 6.1 权限类型

**授权 (Authorization)** 控制用户能访问哪些数据、能执行哪些操作。数据权限通常包括：

| 权限 | 含义 |
| --- | --- |
| `select` | 读取数据 |
| `insert` | 插入新数据 |
| `update` | 修改已有数据 |
| `delete` | 删除数据 |

模式权限则控制数据库结构：

| 权限 | 含义 |
| --- | --- |
| `create` | 创建新关系 |
| `alter` | 增删关系中的属性 |
| `drop` | 删除关系 |
| `index` | 创建或删除索引 |
| `create view` | 创建视图 |

权限可以授予基本关系，也可以授予视图。对视图授予权限不会自动授予底层关系权限，这一点可以用来实现安全隔离。

```SQL
create view geo_instructor as
    select *
    from instructor
    where dept_name = 'Geology';

grant select on geo_instructor to geo_staff;
```

上例只允许 `geo_staff` 查询地质系教师视图，不意味着他们可以直接查询完整的 `instructor` 表。

#### 6.2 授予回收

`grant` 用于授予权限，`revoke` 用于回收权限：

```SQL
grant <privilege list>
on <relation name or view name>
to <user list>;

revoke <privilege list>
on <relation name or view name>
from <user list>;
```

`<user list>` 可以是具体用户、角色，也可以是 `public`。`public` 表示所有有效用户，但回收 `public` 权限时，不会回收单独授予某个用户的权限。

```SQL
grant select on instructor to U1, U2, U3;
grant select on department to public;
grant update (budget) on department to U1, U2;
grant all privileges on department to U1;

revoke select on branch from U1, U2, U3;
```

如果同一权限由多个授权者授予给同一用户，回收其中一条授权后，用户可能仍通过另一条授权保留权限。若某用户基于被回收的权限继续向下授权，则这些依赖权限也可能被级联回收。

```SQL
grant select on department to Amit with grant option;

revoke select on department from Amit cascade;
revoke select on department from Amit restrict;
revoke grant option for select on department from Amit;
```

`with grant option` 允许获得权限的用户继续授予他人。`cascade` 会级联回收依赖权限；`restrict` 则要求没有依赖授权时才允许回收。`revoke grant option` 只取消继续授权的能力，不一定取消用户自身已有的查询权限。

#### 6.3 角色权限

**角色 (Role)** 是一组命名权限。与其逐个用户授予大量权限，不如把权限授予角色，再把角色授予用户。

```SQL
create role instructor;
grant select on takes to instructor;
grant instructor to Amit;

create role teaching_assistant;
grant teaching_assistant to instructor;
```

角色还可以授予另一个角色，形成权限继承链。上例中，`instructor` 继承 `teaching_assistant` 的权限；如果再把 `instructor` 授予某个用户，该用户就间接获得助教角色中的权限。

外键引用也需要权限。若用户想创建引用 `department.dept_name` 的外键，需要拥有对应的 `references` 权限：

```SQL
grant references (dept_name)
on department
to Mariano;
```

这是因为外键约束会让一个关系依赖另一个关系的键值，可能限制被引用关系的删除和更新行为。把引用也纳入权限系统，可以避免用户在没有授权的情况下影响其它表的维护。
