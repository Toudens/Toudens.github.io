---
title: Ch-4 Intermediate SQL
type: docs
weight: "4"
date: 2026-03-24
---
### 1. Joined Relations

Join operations take two relations and return another relation as a result. They are typically used as subquery expressions in the `from` clause.

*   **Join condition**: Defines which tuples in the two relations match, and what attributes are present in the result of the join.
*   **Join type**: Defines how tuples in each relation that do not match any tuple in the other relation are treated. It uses `null` values to avoid loss of information.

```sql
-- inner join (Only matching tuples)
select * from course inner join prereq on course.course_id = prereq.course_id;

-- left outer join (Keeps all tuples from the left relation)
select * from course natural left outer join prereq;

-- right outer join (Keeps all tuples from the right relation)
select count(*) from course natural right outer join prereq where prereq_id is null;

-- full outer join (Keeps all tuples from both relations)
select * from course full outer join prereq using (course_id);
```

> [!NOTE] **Note**
> **Join Conditions 对应的中文概念**：
> *   `natural`：自然连接（自动匹配同名列）。
> *   `on <predicate>`：条件连接（自定义匹配条件）。
> *   `using (A1, A2, ...)`：等值连接（指定同名列进行匹配）。

### 2. Data Types

#### 2.1 Built-in Types
SQL supports basic data types and operations for dates and times. Subtracting a date/time value from another gives an interval value.

```sql
date '2005-7-27'
time '09:00:30.75'
timestamp '2005-7-27 09:00:30.75'
interval '1' day
```

#### 2.2 User Types
SQL allows creating user-defined types and domain types. Domains are similar to types but can have constraints (such as `not null` or `check`) specified on them.

```sql
-- User-defined types
create type Dollars as numeric (12,2) final;

-- Domains with constraints
create domain person_name char(20) not null;

create domain degree_level varchar(10)
    constraint degree_level_test
    check (value in ('Bachelors', 'Masters', 'Doctorate'));
```

> [!NOTE] **Note**
> `create type` 类似于 C 语言的 `typedef`。关键字 `final` 表示这是最基本的数据类型，不能再派生。需要特别注意的是，即使底层的定义完全相同，不同的 `typedef` 名称也会被系统视为完全不同的类型，不能直接混用。

#### 2.3 Large Objects
Large objects (photos, videos, CAD files, etc.) are stored as a large collection of uninterpreted binary or character data.
*   **blob** (binary large object): Uninterpreted binary data.
*   **clob** (character large object): Large collection of character data.

>[!NOTE] **Note**
> 出于性能考虑，当查询返回一个大对象时，数据库实际返回的是一个指向该对象的指针（pointer），而不是将整个大对象本身全部读取出来。

### 3. Constraints

Integrity constraints guard against accidental damage to the database, ensuring that authorized changes do not result in a loss of data consistency.

#### 3.1 Single Relation
Constraints applied to a single relation include `not null`, `primary key`, `unique`, and `check (P)`.

```sql
create table section (
    course_id varchar (8),
    sec_id varchar (8),
    semester varchar (6),
    year numeric (4,0),
    primary key (course_id, sec_id, semester, year),
    check (semester in ('Fall', 'Winter', 'Spring', 'Summer'))
);
```

> [!NOTE] **Note**
> *   `Primary key` 声明的属性必须非空，但 `unique` 声明的候选键（candidate key）是可以为空的。
> *   `check` 通常是对单行（一行内的各个属性）进行逻辑检验。

#### 3.2 Foreign Keys
Ensures referential integrity. A value appearing in a specific attribute of one relation must also appear in the primary key attribute of another relation.

```sql
create table course (
    course_id char(5) primary key,
    dept_name varchar(20),
    foreign key (dept_name) references department
        on delete cascade
        on update cascade
);
```

> [!NOTE] **Note**
> `cascade` 表示级联操作（主表删除/更新时，从表跟着变）。其他替代操作还包括：`set null`（设为空）、`set default`（设为默认值）、`restricted`（拒绝违反约束的操作）。

#### 3.3 Complex Checks
Complex constraints that involve subqueries or multiple relations. To prevent constraint violation during multiple insertions, constraint checking can be deferred to transaction end.

```sql
-- Creating an assertion
create assertion credits_earned_constraint check
(not exists 
    (select ID from student
     where tot_cred <> (
         select sum(credits) from takes natural join course
         where student.ID=takes.ID and grade is not null and grade<>'F')
    )
);
```

>[!NOTE] **Note**
> *   **关于嵌套查询**：理论上 `check` 子句中可以使用子查询，但这在目前大多数的数据库系统中都不被支持。
> *   **关于 Assertion（断言）**：SQL 中表达全称量词（所有满足...）时，通常使用“不存在不”（`not exists`）的逻辑形式。很多数据库并没有原生实现 `assertion`，但在工程上可以通过编写触发器（`triggers`）等方式来实现复杂的完整性校验。

### 4. Views

A view provides a mechanism to hide certain data from the view of certain users. Any relation that is not of the conceptual model but is made visible to a user as a "virtual relation" is called a view.

```sql
create view faculty as
    select ID, name, dept_name
    from instructor;

-- Querying the view
select name from faculty where dept_name = 'Biology';
```

#### 4.1 View Expansion
View definition is not creating a new relation. It causes the saving of an expression, which is substituted into queries using the view.

>[!NOTE] **Note**
> **视图展开（View Expansion）**：实际上就是将前一个 view 的定义直接嵌入（替换）到当前查询的语句中执行，`from` 后面也可以像使用普通表一样插入基于视图的查询。

#### 4.2 View Updates
Insertions, updates, or deletions on a view must be represented by corresponding operations on the underlying database relations.

```sql
insert into faculty values ('30765', 'Green', 'Music');
-- Must be translated by the system to:
insert into instructor values ('30765', 'Green', 'Music', null);
```

>[!NOTE] **Note**
> 对视图的插入实际上是插入原来的底表。如果原表中有未包含在视图里的列，且该列定义为 `not null`，则插入必定失败。大多数 SQL 实现仅允许对“简单视图”（**Updatable views**：行列视图、有 primary key、无 group by/聚集函数、from 只涉及单个表）进行更新。

#### 4.3 Materialized
Materializing a view means creating a physical table containing all the tuples in the result of the query.

```sql
create materialized view departments_total_salary(dept_name, total_salary) as
    select dept_name, sum (salary)
    from instructor
    group by dept_name;
```

> [!NOTE] **Note**
> 物化视图查询快捷便利，但会实际占用物理存储空间，并且需要与底表保持一致性（通常采用增量式更新）。
> **Logical Data Independence**：很多分析型的数据库倾向于按列存储成表。虽然将全部列放到一起导致 IO 代价大，但是按列压缩方便，查询单属性效率极高。视图机制能在底层表结构修改（拆分/合并）时，为上层应用保持逻辑上的数据独立性。

### 5. Indexes

Indices are data structures used to speed up access to records with specified values for index attributes, without looking at all records.

```sql
create table student (
    ID varchar (5) primary key,
    name varchar (20) not null
);

create index studentID_index on student(ID);

-- Query executed by using the index
select * from student where ID = '12345';
```

> [!NOTE] **Note**
> *   有序结构方便查找。但在庞大的数据库系统中，普通的二分查找效率相对并不算高，底层通常使用**百叉树（B树、B+树）**来实现索引。
> *   对于查询中常用的属性可以专门建立 index。需要注意的是，复合 Index 中包含的属性顺序不同，建立出来的 index 也完全不同。
> *   Index 属于物理层的概念，虽然能大幅加速查询，但会占用存储空间，并且在插入、修改、删除记录时会带来额外的维护成本。

### 6. Transactions

A transaction is a unit of program execution that accesses and possibly updates various data items. It must be either fully executed or rolled back as if it never occurred (NONE or ALL).

```sql
SET AUTOCOMMIT=0;

UPDATE account SET balance=balance -100 WHERE ano='1001';
UPDATE account SET balance=balance+100 WHERE ano='1002';
COMMIT;

UPDATE account SET balance=balance -200 WHERE ano='1003';
UPDATE account SET balance=balance+200 WHERE ano='1004'; 
COMMIT;
```

> [!NOTE] **Note**
> *   **银行转账/买车票**是典型的事务边界（Transaction Boundaries）场景。
> *   数据库中没有一条 SQL 语句能游离在事务之外。第一条语句执行就视为事务自动开始，`Commit` 代表上一个事务的结束和下一个事务的开始。
> *   包含复杂计算或耗时长的“长事务”，在执行期间可能会锁定资源并阻塞其它的事务。

#### 6.1 ACID Properties
To preserve the integrity of data, the system must ensure:
*   **Atomicity**: Either all operations are properly reflected or none are. (原子性：全有全无)
*   **Consistency**: Execution in isolation preserves the consistency of the database. (一致性)
*   **Isolation**: Multiple transactions executing concurrently must be unaware of each other. (隔离性)
*   **Durability**: Changes persist successfully even if there are system failures. (持久性)

### 7. Authorization

Forms of authorization on parts of the database include modifying data (`Select`, `Insert`, `Update`, `Delete`) and modifying the schema (`Create`, `Alter`, `Drop`, `Index`, `Create view`).

#### 7.1 Grant & Revoke
The `grant` statement is used to confer authorization, and `revoke` is used to remove it.

```sql
-- Granting privileges
grant select on instructor to U1, U2, U3;
grant select on department to public;
grant update (budget) on department to U1, U2;

-- Revoking privileges
revoke select on branch from U1, U2, U3;

-- Transfer of privileges
grant select on department to Amit with grant option;
revoke select on department from Amit cascade;
```

> [!NOTE] **Note**
> *   **`public`**：代表允许所有有效用户拥有该权限。
> *   **`references`**：引用也是一种权限，比如 `grant reference (dept_name)...` 用于授权用户创建指向该表的外键。
> *   **`with grant option`**：允许获得权限的用户将该权限继续向下级授予。取消权限时，如果使用了 `cascade`，则由此引发的下级权限也会被级联回收。

#### 7.2 Roles
Roles are named sets of privileges that can be granted to users or to other roles, creating a chain of roles.

```sql
create role instructor;
grant select on takes to instructor;
grant instructor to Amit;

-- Chain of roles
create role teaching_assistant;
grant teaching_assistant to instructor; -- instructor inherits assistant's privileges
```

>[!NOTE] **Note**
> 角色（Role）本质上就是一堆权限的集合。引入角色机制可以极大地简化权限管理。有些数据库系统还专门对 user 进行了分组（group）操作来实现类似的管理目的。