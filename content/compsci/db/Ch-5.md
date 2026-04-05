---
title: Ch-5 Advanced SQL
type: docs
date: 2026-03-31
weight: "5"
---
### 1. 数据库访问

SQL 是一种**声明式语言 (Declarative Language)**，缺乏**计算完备性**（没有顺序、分支、循环结构）。同时，SQL 无法执行与数据库内容无关的**非声明式操作**，如用户交互、打印报表或图形用户界面集成。因此，我们必须借助通用编程语言来访问数据库。主要有两种方法：
* **API (Application Program Interface)**：使用一组函数来连接并与数据库服务器通信；
* **嵌入式 SQL (Embedded SQL)**：提供了一种程序与数据库服务器交互的方式。
	* SQL 语句在编译时被翻译成函数调用；
	* 运行时这些函数调用使用一个提供动态 SQL 功能的 API 来连接数据库。
#### 1.1 JDBC API

**JDBC (Java Database Connectivity)** 是 Java 语言与数据库通信的标准 API。它提供了一套接口用于建立连接、发送 SQL 以及处理返回结果。与数据库通信的流程为：
1. 打开一个与数据库的连接；
2. 创建一个“语句”（Statement）对象；
3. 使用 Statement 对象执行查询，以发送查询并获取结果
4. 通过异常机制处理错误。

JDBC 支持多种功能，用于查询和更新数据，以及检索查询结果，还支持元数据检索，例如查询数据库中存在的关系（表）以及这些关系属性的名称和类型。

```java
public static void JDBCexample(String userid, String passwd)
{
    try 
    {
        // 1. 与数据库建立连接
        Connection conn=DriverManager.getConnection
	        ("jdbc:oracle:thin:@db.zju.edu:2000:univdb", userid, passwd);
        conn.setAutoCommit(false); // 关闭自动提交，用于手动事务控制
        
        // 2. 预编译语句
        PreparedStatement pStmt=conn.prepareStatement
	        ("insert into instructor values(?,?,?,?)");
        pStmt.setString(1, "88877");
        pStmt.setString(2, "Perry");
        pStmt.setString(3, "Finance");
        pStmt.setInt(4, 125000);
        pStmt.executeUpdate(); // 执行更新操作
        pStmt.setString(1,"88878");
        pStmt.executeUpdate();

        // 3. Statement与结果集
        Statement stmt=conn.createStatement();
        ResultSet rset=stmt.executeQuery
	        ("select dept_name, avg(salary) from instructor group by dept_name");
        while(rset.next()) 
        {
            System.out.println(rset.getString("dept_name") + " " + rset.getFloat(2));
            if (rset.wasNull()) // 通过 wasNull() 检查上一次读取的列是否为 NULL
	            System.out.println("Got null value");
        }
        conn.commit(); // 提交事务 (或使用 conn.rollback() 回滚)
        rset.close(); stmt.close(); pStmt.close(); conn.close();
    } 
    catch (SQLException sqle) 
        System.out.println("SQLException : " + sqle);
}
```

>[!Note] **Note**
>* 使用字符串作为 SQL 语句，编译时 **无法检查 SQL 语句**（可能会违反 primary key, foreign key 等约束条件），使用 embedded SQL 可以在一定程度上解决该问题；
>* 数据库中为集合，在高级程序设计语言中没有这个概念，需要通过 **循环** 从指针中读取 tuple 中的数据，以进行数据类型的转换；
>* 如果在参数设定时后面的参数没有提供则 **默认使用前面已经设置的参数**，对于上面的例子，第二次 `executeUpdate` 插入的元组为 `("88878,"Perry","Finance",125000)`
>* 使用预编译语句可以先进行语法检查，可以生成内部执行计划，更加高效，近似于函数，便于批量化处理语句。


*   **防止 SQL 注入 (SQL Injection)**：是 `PreparedStatement` 最核心的优势。不要使用字符串拼接去构造查询（例如输入 `"X' or 'Y' = 'Y"` 会使 `WHERE` 永远为真导致数据全表泄露，甚至通过分号注入 `update` 语句），占位符 `?` 会在底层将参数正确转义；
*   **元数据 (Metadata)**：可通过 `ResultSetMetaData rsmd=rset.getMetaData();` 动态获取查询结果的列名和数据类型；通过 `DatabaseMetaData` 获取数据库系统的目录；
*   **其他特性**：JDBC 支持通过 `CallableStatement` 调用数据库函数和存储过程；支持通过 `getBlob()`/`getClob()` 处理二进制大对象 (BLOB) 和字符大对象 (CLOB)。
#### 1.2 ODBC API

**ODBC (Open Database Connectivity)** 是 C/C++ 等语言的标准底层 API。程序通过 ODBC 驱动与数据库通信，与具体使用的数据库无关，是公认的标准函数库。

*   **工作流程与句柄 (Handles)**：
    1. 分配环境句柄 (`SQLAllocEnv`) 和连接句柄 (`SQLAllocConnect`)。
    2. 建立连接 (`SQLConnect`)，字符串参数常使用 `SQL_NTS` (Null-Terminated String)。
    3. 分配语句句柄 (`SQLAllocStmt`) 并执行查询 (`SQLExecDirect` 或使用 `SQLPrepare` 进行预编译)。
    4. **绑定列 (Bind Columns)**：使用 `SQLBindCol()` 将查询结果的列与 C 语言的内存变量直接绑定。
    5. **抓取数据 (Fetch)**：通过 `SQLFetch()` 循环读取结果。
*   **符合性级别 (Conformance Levels)**：ODBC 定义了不同的功能级别：Core（核心基本功能）、Level 1（要求支持元数据查询）和 Level 2（要求支持参数数组等高级目录信息）。

#### 1.3 嵌入式 SQL (Embedded SQL)
嵌入式 SQL 允许将 SQL 语句以特定格式直接写在**宿主语言 (Host Language)** 中，编译前由**预处理器 (Preprocessor)** 转换为宿主语言的函数调用。

*   **宿主变量 (Host Variables)**：在嵌入式 SQL 中调用外部宿主语言的变量时，需加上冒号前缀 `:`。状态码存放在 **SQLCA (SQL 通信区)** 中，如 `SQLSTATE` 为 `'02000'` 代表无更多数据。
*   **游标的使用 (Cursor)**：
    ```c
    EXEC SQL BEGIN DECLARE SECTION;
        int credit_amount; char student_name[30];
    EXEC SQL END DECLARE SECTION;

    // 1. 声明游标
    EXEC SQL declare c cursor for select name from student where tot_cred > :credit_amount;
    EXEC SQL open c; // 2. 打开游标

    // 3. 循环 fetch 取数据
    while (SQLSTATE != '02000') {
        EXEC SQL fetch c into :student_name;
    }
    EXEC SQL close c; // 4. 关闭游标
    ```
*   **游标更新 (Updates Through Cursor)**：可在声明时添加 `for update`，随后在遍历过程中使用 `update ... where current of c` 直接更新当前游标指向的行。
*   **Java 中的嵌入 (SQLJ)**：通过 `#sql { ... }` 语法使用，能在编译期进行 SQL 语法检查（JDBC 只能在运行期报错）。

---

### 2. 函数与存储过程 (Functions & Procedures)

将复杂的业务逻辑封装在数据库系统中，可以大幅减少客户端与数据库之间的网络数据传输，并提升性能。

#### 2.1 SQL 函数 (SQL Functions)
函数通常返回一个值，可直接嵌入在 SQL 表达式中。
*   **标量函数 (Scalar Function)**：返回单个值（如统计人数）。
*   **表函数 (Table Function)**：返回一个关系表，在 SQL:2003 中引入。可以在 `FROM` 子句中通过 `TABLE()` 关键字调用。
    ```sql
    CREATE FUNCTION instructors_of (dept_name CHAR(20))
        RETURNS TABLE (ID VARCHAR(5), name VARCHAR(20), salary NUMERIC(8,2))
        RETURN TABLE (
            SELECT ID, name, salary FROM instructor 
            WHERE instructor.dept_name = instructors_of.dept_name
        );
    -- 调用方式：
    SELECT * FROM TABLE(instructors_of('Music'));
    ```

#### 2.2 存储过程与过程化扩展 (Stored Procedures & Procedural Constructs)
存储过程不强制返回结果集，而是通过 `IN` (输入)、`OUT` (输出) 等参数交互，需使用 `CALL` 语句执行。SQL 标准支持类似于通用编程语言的控制流结构：
*   **复合语句**：`BEGIN ... END`。
*   **循环语句**：`WHILE ... DO`、`REPEAT ... UNTIL`。
*   **FOR 循环遍历**：可以直接遍历查询结果集。
    ```sql
    DECLARE n INTEGER DEFAULT 0;
    FOR r AS SELECT budget FROM department WHERE dept_name = 'Music' DO
        SET n = n - r.budget;
    END FOR;
    ```
*   **条件语句**：`IF-THEN-ELSE` 与类似于 C 语言的 `CASE` 语句。

#### 2.3 外部语言例程 (External Language Routines)
为了应对高复杂度计算，SQL 允许导入使用 C、C++ 或 Java 编写的外部函数 (`LANGUAGE C EXTERNAL NAME ...`)。
*   **安全隐患**：外部代码运行在数据库内存中，若有越界等 Bug 可能损坏数据库结构。
*   **解决方案**：采用**沙箱技术 (Sandbox)**（如 Java 的权限限制），或让外部代码在独立的进程中运行，通过**进程间通信 (IPC)** 与数据库交互。若对效率要求极高且确信安全，也可直接在数据库系统地址空间内执行。

---

### 3. 触发器 (Triggers)

触发器是特定的数据库修改事件（`INSERT`, `DELETE`, `UPDATE`）作为副作用而自动唤醒的特殊语句，遵循 **ECA 规则 (Event-Condition-Action Rule)**。

#### 3.1 触发器的应用与分类
*   **BEFORE 触发器**：可在事件发生**前**激活，用于在数据写入前进行修改。例如，将所有空字符串 `''` 成绩在存入前强制转换为 `NULL`。
*   **行级触发器 (Row-level)**：使用 `FOR EACH ROW`，针对受影响的每一行执行。
*   **语句级触发器 (Statement-level)**：使用 `FOR EACH STATEMENT`。在批量更新大量行时效率极高，它通过引用 **过渡表 (Transition Tables)** 来处理所有受影响的行，而不是逐行循环。

```sql
-- 触发器示例：维护学分总和
CREATE TRIGGER credits_earned
AFTER UPDATE OF takes ON grade        -- Event (事件): 更新 grade 列
REFERENCING NEW ROW AS nrow           -- 引用新旧值
REFERENCING OLD ROW AS orow
FOR EACH ROW                          -- 行级触发器
WHEN nrow.grade <> 'F' AND nrow.grade IS NOT NULL  -- Condition (条件)
     AND (orow.grade = 'F' OR orow.grade IS NULL)
BEGIN ATOMIC
    UPDATE student                    -- Action (动作)
    SET tot_cred = tot_cred + (SELECT credits FROM course WHERE course.course_id = nrow.course_id)
    WHERE student.ID = nrow.ID;
END;
```

#### 3.2 何时不应使用触发器 (When Not To Use)
尽管触发器强大，但由于可能导致**连锁执行 (Cascading execution)**（A 触发 B，B 触发 C），极难调试并可能引发死锁和关键事务失败。现代开发建议寻找替代方案：
1.  **维护汇总数据**：不要用触发器每次更新去维护总数表，现代数据库提供原生的 **物化视图 (Materialized Views)**，自动且高效。
2.  **数据库复制同步**：不要用触发器去记录增量表（Delta relations），应使用数据库底层的**系统复制机制 (Replication)**。
3.  **防止意外执行**：在做数据备份恢复或远程数据加载时，必须提前禁用触发器。

---

### 4. 递归查询 (Recursive Queries)

没有迭代或递归的常规非递归 SQL，只能执行固定次数的 `JOIN`，因此它无法应对树状或图状等深度未知的结构（如寻找**传递闭包 Transitive Closure**）。

#### 4.1 递归 CTE (WITH RECURSIVE)
SQL:1999 引入了递归视图定义。它包含两部分：**锚成员 (Anchor Member)** 负责定义起始条件；**递归成员 (Recursive Member)** 负责引用自身并向下一层级遍历。两者通过 `UNION` 合并。

```sql
-- 寻找所有课程的直接与间接先修课 (传递闭包)
WITH RECURSIVE rec_prereq(course_id, prereq_id) AS (
    -- 1. 锚成员：非递归，查找最基础的直接先修课关系
    SELECT course_id, prereq_id FROM prereq
    
    UNION
    
    -- 2. 递归成员：将当前的递归表自身(rp)与底表(p)做 JOIN，不断查找深层间接关系
    SELECT rp.course_id, p.prereq_id
    FROM rec_prereq AS rp, prereq AS p
    WHERE rp.prereq_id = p.course_id
)
SELECT * FROM rec_prereq;
```

---

### 5. 高级聚合与 OLAP (Advanced Aggregation & OLAP)

#### 5.1 排名与窗口函数 (Ranking & Windowing)
传统 `GROUP BY` 会把多行压缩为单行，而窗口函数允许针对某行相关联的“窗口”进行计算聚合，同时保留原生数据行。

*   **排名函数 (Ranking)**：
    *   `RANK()`：遇到并列时，名次会跳跃（有空缺，如 1, 1, 3）。
    *   `DENSE_RANK()`：遇到并列时，名次不跳跃（无空缺，如 1, 1, 2）。
    *   其他包括：`PERCENT_RANK()` (百分比)、`CUME_DIST()` (累积分布)、`ROW_NUMBER()` (强制唯一序号)、`NTILE(n)` (将数据分成 n 个桶/四分位数)。
    *   支持 `NULLS FIRST` 或 `NULLS LAST` 定义 NULL 值的排序位置。
*   **窗口框架 (Window Frame)**：可定义相对当前行的计算范围。
    ```sql
    -- 计算移动平均 (前一行、当前行、后一行的平均)
    SELECT date, AVG(value) OVER (
        ORDER BY date
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING 
    ) AS moving_avg_sales FROM sales;
    
    -- 计算账户累计余额 (从开头加到当前行)
    SELECT account_number, date_time, SUM(value) OVER (
        PARTITION BY account_number
        ORDER BY date_time
        ROWS UNBOUNDED PRECEDING
    ) AS balance FROM transaction;
    ```

#### 5.2 联机分析处理 (OLAP)
OLAP 支持多维数据的交互式聚合与分析。数据模型由 **维度属性 (Dimension)**（如时间、颜色）和 **度量属性 (Measure)**（如销售额）构成，统称 **数据立方体 (Data Cube)**。

*   **扩展聚合关键字**：
    *   `CUBE(A, B, C)`：生成 $2^n$ 种全组合的分组汇总并集（包括空集总计）。
    *   `ROLLUP(A, B, C)`：生成所有前缀的分组汇总并集（如 `(A,B,C)`, `(A,B)`, `(A)`, `()`），特别适用于年-月-日或分类层级数据的聚合。
*   **处理汇总的 NULL 值**：聚合产生的总计字段会被置为 `NULL`。使用 `GROUPING(列名)` 可区分它是汇总产生的 `NULL`（返回 1）还是原本的真实 `NULL`（返回 0）。配合 `DECODE()` 可以将其美化输出为 `'ALL'`。

#### 5.3 OLAP 操作与实现架构
*   **常用分析操作**：
    *   **Pivoting (旋转/透视)**：变换维度在交叉表中的行列位置。
    *   **Slicing (切片)** / **Dicing (切块)**：固定一个或多个维度的值来截取局部数据。
    *   **Rollup (上卷)** / **Drill down (下钻)**：改变颗粒度（例如从国家级下钻至城市级）。
*   **实现架构**：分为基于多维数组内存的 **MOLAP**、基于关系数据库和复杂 SQL 的 **ROLAP**，以及结合两者的混合型 **HOLAP**。

---

### 6. 其他高级特性 (Other Advanced Features)

#### 6.1 合并语句 (Merge Statement)
`MERGE` 语句（也称为 UPSERT）可以在单一的原子事务中，根据两个表的匹配条件同时执行批量的 `INSERT`、`UPDATE` 或 `DELETE` 操作。

```sql
-- 将流水账 (funds_received) 批量合并到账户主表 (account) 中
MERGE INTO account AS A 
USING (SELECT * FROM funds_received) AS F 
ON (A.account_number = F.account_number) 
WHEN MATCHED THEN
    -- 如果存在对应账户，则直接累加余额
    UPDATE SET balance = balance + F.amount
WHEN NOT MATCHED THEN
    -- 如果不存在，则插入新开户记录
    INSERT (account_number, balance) VALUES (F.account_number, F.amount);
```
*   **优势**：在宿主语言中，传统做法是先 `SELECT` 查询再用 `IF` 决定发 `INSERT` 还是 `UPDATE`。`MERGE` 将该过程全部交由数据库内核处理，不仅极大精简了代码，更避免了高并发场景下的数据冲突。