---
title: Ch-5 SQL 高级
weight: "5"
type: docs
date: 2026-06-15
---

### 1. 程序访问

#### 1.1 访问方式

SQL 是声明式语言，适合描述“要什么数据”，但它不负责通用程序中的输入输出、界面交互、报表打印和复杂控制流程。因此应用程序通常需要通过通用编程语言访问数据库。

程序访问数据库主要有两种方式：

| 方式 | 思路 | 代表 |
| --- | --- | --- |
| API | 程序调用函数连接数据库、发送 SQL、逐行读取结果 | JDBC、ODBC |
| 嵌入式 SQL | 在宿主语言中直接写 SQL，由预处理器翻译为函数调用 | Embedded SQL、SQLJ |

API 方式更灵活，SQL 字符串可以在运行时构造；嵌入式 SQL 更接近静态检查，编译前会把 SQL 语句翻译成宿主语言中的数据库调用。

#### 1.2 JDBC

**JDBC (Java Database Connectivity)** 是 Java 访问关系数据库的标准 API。典型流程是打开连接、创建语句对象、执行 SQL、读取结果、处理异常并关闭资源。

```java
Connection conn = DriverManager.getConnection(
    "jdbc:oracle:thin:@db.example.edu:2000:univdb",
    userid,
    passwd
);

Statement stmt = conn.createStatement();
ResultSet rset = stmt.executeQuery(
    "select dept_name, avg(salary) from instructor group by dept_name"
);

while (rset.next()) {
    System.out.println(rset.getString("dept_name") + " " + rset.getFloat(2));
}

rset.close();
stmt.close();
conn.close();
```

`ResultSet` 是结果游标。`next()` 会移动到下一行，`getString("dept_name")` 和 `getString(1)` 都可以取列值；如果读取基本类型后需要判断是否为 SQL 空值，可以调用 `wasNull()`。

```java
int a = rset.getInt("a");
if (rset.wasNull()) {
    System.out.println("Got null value");
}
```

JDBC 默认把每条 SQL 语句当作一个独立事务并自动提交。涉及多条更新时，通常应关闭自动提交，并显式提交或回滚。

```java
conn.setAutoCommit(false);

try {
    // multiple updates
    conn.commit();
} catch (SQLException e) {
    conn.rollback();
}
```

#### 1.3 预编译语句

`PreparedStatement` 会先把 SQL 模板交给数据库编译，参数位置用 `?` 表示。之后可以反复绑定参数并执行。

```java
PreparedStatement pStmt = conn.prepareStatement(
    "insert into instructor values (?, ?, ?, ?)"
);

pStmt.setString(1, "88877");
pStmt.setString(2, "Perry");
pStmt.setString(3, "Finance");
pStmt.setInt(4, 125000);
pStmt.executeUpdate();

pStmt.setString(1, "88878");
pStmt.executeUpdate();
```

第二次执行只改了第一个参数，其余参数仍沿用前面绑定的值，所以插入的是同名同院系同工资的另一位教师。

预编译语句的核心作用是避免 SQL 注入。不要把用户输入直接拼接进 SQL 字符串，否则输入 `X' or 'Y' = 'Y` 会让条件恒真：

```SQL
select *
from instructor
where name = 'X' or 'Y' = 'Y';
```

更严重时，攻击者还可以尝试用分号拼接更新语句。使用参数绑定后，用户输入会被当作普通字符串值处理，而不是 SQL 语法的一部分。

#### 1.4 元数据

JDBC 可以读取结果集元数据和数据库元数据。`ResultSetMetaData` 描述查询结果的列名、列数和类型。

```java
ResultSetMetaData rsmd = rset.getMetaData();

for (int i = 1; i <= rsmd.getColumnCount(); i++) {
    System.out.println(rsmd.getColumnName(i));
    System.out.println(rsmd.getColumnTypeName(i));
}
```

`DatabaseMetaData` 描述数据库目录结构，例如有哪些表、某张表有哪些列、列的类型是什么。

```java
DatabaseMetaData dbmd = conn.getMetaData();
ResultSet rs = dbmd.getColumns(null, "univdb", "department", "%");
```

JDBC 还支持 `CallableStatement` 调用数据库函数和存储过程；对大对象可以通过 `getBlob()`、`getClob()` 读取，再用字节数组或流处理。

#### 1.5 ODBC

**ODBC (Open Database Connectivity)** 是 C、C++、C# 等语言常用的数据库访问 API。应用程序调用 ODBC 接口，具体数据库厂商提供驱动库，驱动负责和数据库服务器通信。

ODBC 的基本流程是分配环境句柄、分配连接句柄、建立连接、分配语句句柄、执行 SQL、绑定结果列、循环抓取结果。

```c
SQLAllocEnv(&env);
SQLAllocConnect(env, &conn);
SQLConnect(conn, "db.example.edu", SQL_NTS, "user", SQL_NTS, "pass", SQL_NTS);

SQLAllocStmt(conn, &stmt);
SQLExecDirect(stmt, sqlquery, SQL_NTS);
SQLBindCol(stmt, 1, SQL_C_CHAR, deptname, 80, &lenOut1);
SQLBindCol(stmt, 2, SQL_C_FLOAT, &salary, 0, &lenOut2);

while (SQLFetch(stmt) == SQL_SUCCESS) {
    printf("%s %g\n", deptname, salary);
}
```

`SQLBindCol()` 把查询结果列绑定到 C 语言变量。每次 `SQLFetch()` 抓取一行时，属性值会自动写入对应变量；变长字段还会把实际长度写入长度变量，负长度通常表示该列为 `null`。

ODBC 也支持预编译语句：`SQLPrepare()` 编译 SQL 模板，`SQLBindParameter()` 绑定参数，`SQLExecute()` 执行。它同样可以避免把用户输入拼接成 SQL 字符串。

ODBC 定义了不同符合性级别。Core 提供核心功能，Level 1 要求支持元数据查询，Level 2 进一步支持参数数组和更详细的目录信息。SQL CLI 标准与 ODBC 类似，但细节略有差异。

#### 1.6 嵌入 SQL

嵌入式 SQL 把 SQL 语句写入宿主语言。预处理器会识别 `EXEC SQL`，并在编译前把 SQL 语句转换为宿主语言函数调用。

```c
EXEC SQL BEGIN DECLARE SECTION;
    int credit_amount;
    char si[6];
    char sn[30];
EXEC SQL END DECLARE SECTION;
```

宿主变量在 SQL 中使用时要加冒号，表示它来自宿主语言而不是数据库属性。

```c
EXEC SQL declare c cursor for
    select ID, name
    from student
    where tot_cred > :credit_amount;

EXEC SQL open c;
EXEC SQL fetch c into :si, :sn;
EXEC SQL close c;
```

`open` 会执行查询并把结果保存在临时关系中，`fetch` 每次把一行结果写入宿主变量。SQL 通信区中的 `SQLSTATE` 用于报告状态，例如 `'02000'` 表示没有更多数据。

游标也可以用于更新当前行。声明游标时写 `for update`，随后用 `where current of c` 指向当前抓取的元组。

```SQL
update instructor
set salary = salary + 1000
where current of c;
```

Java 中的嵌入式 SQL 通常称为 SQLJ。它比普通 JDBC 更静态，部分 SQL 错误能在编译阶段发现；JDBC 更动态，错误往往到运行时才暴露。

### 2. 过程扩展

#### 2.1 函数过程

SQL 的过程化扩展允许把业务逻辑放入数据库中执行。这样可以减少应用程序与数据库之间的往返，也能让多个应用共享同一套规则。

函数通常返回一个值，可以出现在 SQL 表达式中。例如定义一个函数，返回某个院系的教师数量：

```SQL
create function dept_count(dept_name varchar(20))
returns integer
begin
    declare d_count integer;

    select count(*)
    into d_count
    from instructor
    where instructor.dept_name = dept_count.dept_name;

    return d_count;
end;
```

调用时可以像普通函数一样使用：

```SQL
select dept_name, budget
from department
where dept_count(dept_name) > 12;
```

存储过程不一定返回表达式值，通常通过 `in` 和 `out` 参数交换数据，并用 `call` 调用。

```SQL
create procedure dept_count_proc(
    in dept_name varchar(20),
    out d_count integer
)
begin
    select count(*)
    into d_count
    from instructor
    where instructor.dept_name = dept_count_proc.dept_name;
end;

call dept_count_proc('Physics', d_count);
```

函数和过程既可以在 SQL 过程内部调用，也可以通过嵌入式 SQL 或动态 SQL 调用。

#### 2.2 表函数

SQL:2003 引入了返回关系的表函数。表函数可以出现在 `from` 子句中，像普通关系一样参与查询。

```SQL
create function instructors_of(dept_name char(20))
returns table (
    ID varchar(5),
    name varchar(20),
    dept_name varchar(20),
    salary numeric(8,2)
)
return table (
    select ID, name, dept_name, salary
    from instructor
    where instructor.dept_name = instructors_of.dept_name
);
```

调用时用 `table(...)` 把函数结果当作关系：

```SQL
select *
from table(instructors_of('Music'));
```

表函数适合把一段可复用查询封装起来，尤其适合返回多行多列结果的逻辑。

#### 2.3 控制结构

SQL 标准提供类似通用语言的过程控制结构，但实际数据库常有自己的方言。复合语句用 `begin ... end` 包裹多条语句，局部变量可以在复合语句内部声明。

`while` 和 `repeat` 用于循环：

```SQL
declare n integer default 0;

while n < 10 do
    set n = n + 1;
end while;

repeat
    set n = n - 1;
until n = 0
end repeat;
```

`for` 循环可以遍历一个查询结果集：

```SQL
declare n integer default 0;

for r as
    select budget
    from department
    where dept_name = 'Music'
do
    set n = n - r.budget;
end for;
```

条件语句包括 `if-then-else` 和 `case`。过程化扩展让数据库内部可以表达分支和循环，但也会把一部分业务逻辑绑定到数据库系统中，迁移时要注意方言差异。

#### 2.4 外部例程

SQL:1999 允许用 C、C++、Java 等外部语言编写函数或过程，再在数据库中声明。

```SQL
create procedure dept_count_proc(
    in dept_name varchar(20),
    out count integer
)
language C
external name '/usr/app/bin/dept_count_proc';
```

外部语言更适合复杂计算，也可能更高效。但如果外部代码直接加载到数据库进程地址空间中，越界访问、内存破坏或恶意代码都可能影响数据库安全。

常见保护方式有两种：一种是在沙箱中运行，例如使用受限 Java 环境；另一种是让外部例程运行在独立进程中，通过进程间通信传递参数和结果。前者和后者都牺牲一定性能，直接在数据库地址空间执行则更快但风险更高。

### 3. 触发器

#### 3.1 基本结构

**触发器 (Trigger)** 是数据库修改事件发生时由系统自动执行的语句。它遵循 ECA 规则：事件 Event 指 `insert`、`delete` 或 `update`；条件 Condition 判断是否触发动作；动作 Action 是实际执行的 SQL 逻辑。

设计触发器时要明确三件事：在哪类事件后或前触发，触发条件是什么，触发后执行什么动作。

```SQL
create trigger account_trigger
after update of balance on account
referencing new row as nrow
referencing old row as orow
for each row
when nrow.balance - orow.balance >= 200000
  or orow.balance - nrow.balance >= 50000
begin atomic
    insert into account_log
    values (nrow.account_number, nrow.balance - orow.balance, current_time);
end;
```

`referencing old row` 和 `referencing new row` 用来访问更新前后的行。删除只有旧行，插入只有新行，更新同时有旧行和新行。

#### 3.2 约束维护

触发器可以补充表达 SQL 约束难以直接表达的规则。例如 `section.time_slot_id` 可能无法直接引用 `time_slot`，因为 `time_slot_id` 不是 `time_slot` 的主键。可以在插入 `section` 时检查对应时间段是否存在。

```SQL
create trigger timeslot_check1
after insert on section
referencing new row as nrow
for each row
when nrow.time_slot_id not in (
    select time_slot_id
    from time_slot
)
begin atomic
    rollback;
end;
```

删除 `time_slot` 时也要检查是否还被 `section` 引用。如果删除的是某个 `time_slot_id` 的最后一个元组，并且该值仍在 `section` 中出现，就回滚删除。

```SQL
create trigger timeslot_check2
after delete on time_slot
referencing old row as orow
for each row
when orow.time_slot_id not in (
        select time_slot_id
        from time_slot
    )
  and orow.time_slot_id in (
        select time_slot_id
        from section
    )
begin atomic
    rollback;
end;
```

触发器也可以在事件发生前执行，用来规范写入值。例如把空字符串成绩改成 `null`：

```SQL
create trigger setnull_trigger
before update of grade on takes
referencing new row as nrow
for each row
when nrow.grade = ' '
begin atomic
    set nrow.grade = null;
end;
```

#### 3.3 学分维护

触发器常见用途是维护冗余汇总字段。下面例子在学生某门课成绩从不及格或空值变成及格时，把课程学分加入 `student.tot_cred`。

```SQL
create trigger credits_earned
after update of grade on takes
referencing new row as nrow
referencing old row as orow
for each row
when nrow.grade <> 'F'
  and nrow.grade is not null
  and (orow.grade = 'F' or orow.grade is null)
begin atomic
    update student
    set tot_cred = tot_cred + (
        select credits
        from course
        where course.course_id = nrow.course_id
    )
    where student.ID = nrow.ID;
end;
```

这个条件避免了重复加学分：只有从“不计入学分”的状态转为“计入学分”的状态时才更新总学分。

#### 3.4 语句触发

行级触发器使用 `for each row`，会对受影响的每一行执行一次动作。语句级触发器使用 `for each statement`，一条 SQL 语句无论影响多少行都只触发一次。

语句级触发器可以通过过渡表访问本次语句影响的所有行。

```SQL
create trigger grade_trigger
after update of grade on takes
referencing new table as new_table
for each statement
when exists (
    select avg(grade)
    from new_table
    group by course_id, sec_id, semester, year
    having avg(grade) < 60
)
begin atomic
    rollback;
end;
```

当一条语句更新大量行时，语句级触发器通常比逐行触发更高效，也更适合检查整体性质。

#### 3.5 使用边界

触发器会自动执行，因此很容易产生隐式副作用。过度使用触发器会让程序行为难以追踪，尤其是一个触发器引发另一个触发器时，可能形成连锁执行。

过去常用触发器维护汇总数据或复制增量表，但现在更推荐使用物化视图和数据库复制机制。触发器仍适合表达局部、紧密依附于表修改的约束和派生维护。

导入备份数据或复制远端更新时，触发器可能被意外触发，所以这类批处理任务常需要临时禁用触发器。触发器中的错误也可能导致关键事务失败。

### 4. 递归查询

#### 4.1 递归 CTE

没有递归或迭代时，SQL 查询只能写出固定次数的连接。因此对于先修关系、组织上下级关系这类深度未知的问题，普通查询无法覆盖任意层数。

SQL:1999 引入递归公共表表达式。递归 CTE 通常由锚成员和递归成员组成：锚成员给出初始结果，递归成员引用自身生成更深层结果，两部分用 `union` 合并。

```SQL
with recursive rec_prereq(course_id, prereq_id) as (
    select course_id, prereq_id
    from prereq

    union

    select rec_prereq.course_id, prereq.prereq_id
    from rec_prereq, prereq
    where rec_prereq.prereq_id = prereq.course_id
)
select *
from rec_prereq;
```

`rec_prereq` 表示 `prereq` 关系的传递闭包，即某门课程的直接和间接先修课程。

#### 4.2 递归能力

递归查询的能力来自“不断把已知结果继续扩展”。对先修课程来说，第一轮得到直接先修课，第二轮得到先修课的先修课，之后继续扩展，直到没有新元组产生。

非递归 SQL 可以手写有限层连接，例如连接两次、三次或四次，但层数一旦超过预设连接次数，查询就会失效。递归 CTE 能把“层数未知”的遍历交给数据库执行。

另一个典型例子是员工和经理关系。若 `manager(employee_name, manager_name)` 保存直接汇报关系，可以递归求出所有直接或间接汇报关系。

```SQL
with recursive empl(employee_name, manager_name) as (
    select employee_name, manager_name
    from manager

    union

    select manager.employee_name, empl.manager_name
    from manager, empl
    where manager.manager_name = empl.employee_name
)
select *
from empl;
```

递归查询必须注意终止条件。使用 `union` 会自动去重，有助于在有限图上收敛；若使用 `union all`，则需要额外避免循环导致无限生成。

### 5. 高级聚合

#### 5.1 排名函数

排名函数和 `order by` 配合使用。`rank()` 会给排序后的元组分配名次；若存在并列，下一名会跳过空缺名次。

```SQL
select ID,
       rank() over (order by GPA desc) as s_rank
from student_grades
order by s_rank;
```

如果两名学生并列第一，下一名的 `rank()` 是 3。`dense_rank()` 不留下空缺，下一名是 2。

排名也可以在分区内计算。下面查询给每个院系内部的学生 GPA 排名：

```SQL
select ID,
       dept_name,
       rank() over (
           partition by dept_name
           order by GPA desc
       ) as dept_rank
from dept_grades
order by dept_name, dept_rank;
```

排名函数在 `group by` 和聚集之后执行。它比简单的 `limit n` 更一般，因为它可以求每个分区内部的前若干名。

其它常见排名函数如下：

| 函数 | 含义 |
| --- | --- |
| `percent_rank()` | 返回相对排名百分比 |
| `cume_dist()` | 返回小于等于当前值的元组比例 |
| `row_number()` | 给每行唯一序号，并列时顺序可能不确定 |
| `ntile(n)` | 按排序结果把每个分区分成 $n$ 个桶 |

```SQL
select ID,
       ntile(4) over (order by GPA desc) as quartile
from student_grades;
```

排序时可以指定空值位置，例如 `nulls first` 或 `nulls last`。

#### 5.2 窗口计算

窗口函数不会像 `group by` 那样把多行压缩为一行，而是在保留原始行的同时，对与当前行相关的一组行进行计算。

移动平均是窗口计算的典型例子。给定 `sales(date, value)`，可以对每一天计算前一天、当天和后一天的销售平均或总和。

```SQL
select date,
       sum(value) over (
           order by date
           rows between 1 preceding and 1 following
       ) as moving_sum
from sales;
```

窗口边界可以有多种形式。`rows unbounded preceding` 表示从分区第一行到当前行；`rows between unbounded preceding and current row` 表示同样的累计窗口；`range between 10 preceding and current row` 表示按排序值范围而不是物理行数取窗口。

窗口也可以与分区结合。下面查询对每个账户按交易时间计算累计余额：

```SQL
select account_number,
       date_time,
       sum(value) over (
           partition by account_number
           order by date_time
           rows unbounded preceding
       ) as balance
from transaction
order by account_number, date_time;
```

这里 `partition by account_number` 把不同账户分开，`order by date_time` 确定账户内部交易顺序，窗口从该账户第一笔交易累计到当前交易。

#### 5.3 OLAP 基础

**OLAP (Online Analytical Processing)** 用于交互式多维数据分析。能按多个维度查看和汇总的数据称为多维数据。

多维数据通常包含两类属性：

| 属性 | 含义 | 示例 |
| --- | --- | --- |
| 维度属性 | 观察和分组的角度 | 商品名、颜色、尺码、日期 |
| 度量属性 | 可以聚集的数值 | 销售数量、销售额 |

交叉表把一个维度放在行标题，一个维度放在列标题，其它维度可以固定在表头，每个单元格保存某个度量的聚集值。数据立方体是交叉表的多维推广，交叉表可以看作数据立方体的一个二维视图。

维度常带有层次结构。例如时间可以按小时、日期、星期、月份、季度、年份查看；商品可以按商品、类别、品牌查看。沿层次从细粒度到粗粒度汇总称为上卷，从粗粒度回到细粒度称为下钻。

#### 5.4 cube

`cube` 会对给定属性集合的每个子集分别执行 `group by`，再把结果合并。若有 $n$ 个分组属性，则共有 $2^n$ 种分组。

```SQL
select item_name, color, size, sum(number)
from sales
group by cube(item_name, color, size);
```

上面查询等价于对下列分组结果求并：

| 分组 |
| --- |
| `(item_name, color, size)` |
| `(item_name, color)` |
| `(item_name, size)` |
| `(color, size)` |
| `(item_name)` |
| `(color)` |
| `(size)` |
| `()` |

不出现在某个分组中的属性，在结果中会以 `null` 表示“所有值汇总”。这会和数据中真实存在的 `null` 混淆，因此 SQL 提供 `grouping()` 函数区分两者。

```SQL
select item_name,
       color,
       size,
       sum(number),
       grouping(item_name) as item_name_flag,
       grouping(color) as color_flag,
       grouping(size) as size_flag
from sales
group by cube(item_name, color, size);
```

`grouping(A)` 对汇总产生的空值返回 1，对普通值或真实空值返回 0。可以配合 `decode()` 或 `case` 把汇总空值显示为 `all`。

#### 5.5 rollup

`rollup` 只生成指定属性列表的所有前缀分组，适合层次型维度。

```SQL
select item_name, color, size, sum(number)
from sales
group by rollup(item_name, color, size);
```

它生成的分组为：

| 分组 |
| --- |
| `(item_name, color, size)` |
| `(item_name, color)` |
| `(item_name)` |
| `()` |

若有商品类别表 `itemcategory(item_name, category)`，可以按类别和商品做层次汇总：

```SQL
select category, item_name, sum(number)
from sales, itemcategory
where sales.item_name = itemcategory.item_name
group by rollup(category, item_name);
```

多个 `rollup` 和 `cube` 可以同时出现在一个 `group by` 子句中。每个结构生成一组分组列表，最终分组集合是这些列表的笛卡尔积。

```SQL
select item_name, color, size, sum(number)
from sales
group by rollup(item_name), rollup(color, size);
```

它生成 `{(item_name),()}` 与 `{(color,size),(color),()}` 的组合，因此会得到 `(item_name,color,size)`、`(item_name,color)`、`(item_name)`、`(color,size)`、`(color)` 和 `()`。

#### 5.6 OLAP 操作

常见 OLAP 操作如下：

| 操作 | 含义 |
| --- | --- |
| Pivoting | 改变交叉表使用的行列维度 |
| Slicing | 固定一个维度值，查看一个切片 |
| Dicing | 固定多个维度值，查看一个子立方体 |
| Rollup | 从细粒度上卷到粗粒度 |
| Drill down | 从粗粒度下钻到细粒度 |

OLAP 实现也有不同路线。MOLAP 用多维数组存储数据立方体，查询快但预计算和空间开销大；ROLAP 只依赖关系数据库和 SQL 聚合，空间更灵活；HOLAP 把常用汇总放在多维结构中，底层明细和其它汇总仍放在关系数据库中。

早期 OLAP 系统会预计算所有聚集，但 $n$ 个维度会产生 $2^n$ 种分组，时间和空间代价都可能很高。实际系统通常只预计算一部分汇总，其它汇总从已有汇总继续计算。例如 `(item_name,color)` 可以从 `(item_name,color,size)` 的汇总继续聚集得到。

大多数聚集可以这样分解计算，但 `median` 这类不可分解聚集较难从粗粒度或已有汇总中直接得到。

### 6. 合并语句

#### 6.1 merge

`merge` 用于批量处理“匹配则更新，不匹配则插入”的场景，也常被称为 upsert。它把原本需要应用程序先查询、再分支决定更新或插入的逻辑交给数据库执行。

```SQL
merge into account as A
using (
    select *
    from funds_received
) as F
on A.account_number = F.account_number
when matched then
    update set balance = balance + F.amount;
```

如果系统支持 `when not matched`，还可以在没有匹配账户时插入新账户。

```SQL
merge into account as A
using funds_received as F
on A.account_number = F.account_number
when matched then
    update set balance = balance + F.amount
when not matched then
    insert (account_number, balance)
    values (F.account_number, F.amount);
```

`merge` 的优势是把批量匹配、更新和插入放在单条语句中完成，语义更集中，也更容易由数据库系统保证并发执行时的一致性。
