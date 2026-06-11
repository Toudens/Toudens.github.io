
| 变量名                        | 含义                                                         | 取值                               |
| :------------------------- | :--------------------------------------------------------- | :------------------------------- |
| `INVALID_PAGE_ID`          | **无效的物理/逻辑数据页 ID**。<br>用于标记空指针、链表终点或未初始化的页。                | `-1`                             |
| `INVALID_FRAME_ID`         | **无效的缓冲池内存帧 ID**。<br>用于标记缓冲池查找未命中或槽位未分配。                   | `-1`                             |
| `INVALID_TXN_ID`           | **无效的事务 ID**。<br>用于标记非事务性的系统操作。                            | `-1`                             |
| `INVALID_LSN`              | **无效的日志序列号（Log Sequence Number）**。<br>用于标记未被修改过或无需写日志的数据页。 | `-1`                             |
| `META_PAGE_ID`             | **磁盘物理文件元数据页 ID**。<br>数据库文件的第一页（第 0 页），存储磁盘文件管理信息。         | `0`                              |
| `CATALOG_META_PAGE_ID`     | **系统目录元数据逻辑页 ID**。<br>用于存储表结构、列信息等 Catalog 元数据，通常映射在第 0 页。 | `0`                              |
| `INDEX_ROOTS_PAGE_ID`      | **索引根节点逻辑页 ID**。<br>文件的第 1 页，存储所有索引及其对应的 B+ 树根节点页号。        | `1`                              |
| `PAGE_SIZE`                | **数据页的固定大小（字节数）**。<br>磁盘读写和内存缓存的最小粒度单位。                    | `4096`（即 4KB）                    |
| `DEFAULT_BUFFER_POOL_SIZE` | **缓冲池默认管理的页帧数量**。<br>规定内存中最大能同时缓存多少个数据页（非字节数）。             | `20480`                          |
| `FIELD_NULL_LEN`           | **NULL 值字段的长度标记**。<br>在序列化存储时，用来表示该字段的值为 `NULL`。           | `UINT32_MAX`<br>（即 `4294967295`） |
| `VARCHAR_MAX_LEN`          | **VARCHAR 类型的最大允许字节数**。<br>限制单条记录过大以防止溢出单个页面。              | `PAGE_SIZE / 2`<br>（即 `2048`）    |
### 2. 核心数据类型别名表

虽然不是变量，但这些别名规定了上述变量的类型，同样是代码的关键部分：

| 类型别名 | 底层实际类型 | 对应表达的业务含义 |
| :--- | :--- | :--- |
| `page_id_t` | `int32_t` | **页 ID**。磁盘文件的物理页号。 |
| `frame_id_t` | `int32_t` | **帧 ID**。缓冲池内存数组中的槽位索引。 |
| `txn_id_t` | `int32_t` | **事务 ID**。全局事务的唯一标识符。 |
| `lsn_t` | `int32_t` | **日志序列号**。WAL 预写日志的序号。 |
| `column_id_t` | `uint32_t` | **列 ID**。表中某一列的序号位置。 |
| `index_id_t` | `uint32_t` | **索引 ID**。系统索引的唯一标识符。 |
| `table_id_t` | `uint32_t` | **表 ID**。物理数据表的唯一标识符。 |
# MiniSQL 工作流 Checklist

## 0. 准备阶段

- [x] 解压项目，确认目录结构
- [x] 阅读 `README.md`
- [x] 阅读 `CMakeLists.txt`
- [ ] 阅读 `src/CMakeLists.txt`
- [ ] 阅读 `test/CMakeLists.txt`
- [ ] 成功配置构建目录：`cmake ..`
- [ ] 确认可运行单元测试入口：`./test/minisql_test`

## 1. 公共基础

- [ ] 阅读 `src/include/common/config.h`
- [ ] 理解 `PAGE_SIZE`
- [ ] 理解 `page_id_t`
- [ ] 理解 `frame_id_t`
- [ ] 理解 `table_id_t`
- [ ] 理解 `index_id_t`
- [ ] 阅读 `src/include/common/rowid.h`
- [ ] 理解 `RowId = page_id + slot_num`
- [ ] 阅读 `src/include/common/dberr.h`

## 2. Disk Manager

### 先看

- [ ] 阅读 `src/include/page/disk_file_meta_page.h`
- [ ] 阅读 `src/include/page/bitmap_page.h`
- [ ] 阅读 `src/include/storage/disk_manager.h`
- [ ] 阅读 `test/storage/disk_manager_test.cpp`

### 再写

- [x] 实现 `src/page/bitmap_page.cpp`
- [ ] 实现 `BitmapPage::AllocatePage`
- [ ] 实现 `BitmapPage::DeAllocatePage`
- [ ] 实现 `BitmapPage::IsPageFree`
- [ ] 实现 `src/storage/disk_manager.cpp`
- [ ] 实现 `DiskManager::AllocatePage`
- [ ] 实现 `DiskManager::DeAllocatePage`
- [ ] 实现 `DiskManager::IsPageFree`
- [ ] 实现 `DiskManager::MapPageId`

### 验证

- [ ] 运行 `disk_manager_test`
- [ ] 确认逻辑页号从 0 递增
- [ ] 确认释放页后可重新分配

## 3. Buffer Pool

### 先看

- [ ] 阅读 `src/include/page/page.h`
- [ ] 阅读 `src/include/buffer/replacer.h`
- [ ] 阅读 `src/include/buffer/lru_replacer.h`
- [ ] 阅读 `src/include/buffer/buffer_pool_manager.h`
- [ ] 阅读 `test/buffer/lru_replacer_test.cpp`
- [ ] 阅读 `test/buffer/buffer_pool_manager_test.cpp`

### 再写

- [ ] 实现 `src/buffer/lru_replacer.cpp`
- [ ] 实现 `LRUReplacer::Victim`
- [ ] 实现 `LRUReplacer::Pin`
- [ ] 实现 `LRUReplacer::Unpin`
- [ ] 实现 `LRUReplacer::Size`
- [ ] 实现 `src/buffer/buffer_pool_manager.cpp`
- [ ] 实现 `FetchPage`
- [ ] 实现 `NewPage`
- [ ] 实现 `UnpinPage`
- [ ] 实现 `FlushPage`
- [ ] 实现 `DeletePage`

### 验证

- [ ] 运行 `lru_replacer_test`
- [ ] 运行 `buffer_pool_manager_test`
- [ ] 确认 pin count 变化正确
- [ ] 确认 dirty page 会写回磁盘

## 4. Record 层

### 先看

- [ ] 阅读 `src/include/record/type_id.h`
- [ ] 阅读 `src/include/record/types.h`
- [ ] 阅读 `src/record/types.cpp`
- [ ] 阅读 `src/include/record/field.h`
- [ ] 阅读 `src/include/record/column.h`
- [ ] 阅读 `src/include/record/schema.h`
- [ ] 阅读 `src/include/record/row.h`
- [ ] 阅读 `test/record/tuple_test.cpp`

### 再写

- [ ] 实现 `src/record/column.cpp`
- [ ] 实现 `Column::SerializeTo`
- [ ] 实现 `Column::DeserializeFrom`
- [ ] 实现 `Column::GetSerializedSize`
- [ ] 实现 `src/record/schema.cpp`
- [ ] 实现 `Schema::SerializeTo`
- [ ] 实现 `Schema::DeserializeFrom`
- [ ] 实现 `Schema::GetSerializedSize`
- [ ] 实现 `src/record/row.cpp`
- [ ] 实现 `Row::SerializeTo`
- [ ] 实现 `Row::DeserializeFrom`
- [ ] 实现 `Row::GetSerializedSize`

### 验证

- [ ] 运行 `tuple_test`
- [ ] 确认 int/float/char 字段可序列化
- [ ] 确认 null 字段可处理
- [ ] 确认 Row 反序列化后字段值一致

## 5. Table 层

### 先看

- [ ] 阅读 `src/include/page/table_page.h`
- [ ] 阅读 `src/page/table_page.cpp`
- [ ] 阅读 `src/include/storage/table_heap.h`
- [ ] 阅读 `src/include/storage/table_iterator.h`
- [ ] 阅读 `test/storage/table_heap_test.cpp`

### 再写

- [ ] 实现 `TableHeap` 构造函数
- [ ] 实现 `TableHeap::InsertTuple`
- [ ] 实现 `TableHeap::GetTuple`
- [ ] 实现 `TableHeap::UpdateTuple`
- [ ] 实现 `TableHeap::ApplyDelete`
- [ ] 实现 `TableHeap::Begin`
- [ ] 实现 `TableHeap::End`
- [ ] 实现 `TableIterator`
- [ ] 实现 `TableIterator::operator*`
- [ ] 实现 `TableIterator::operator++`

### 验证

- [ ] 运行 `table_heap_test`
- [ ] 插入 10000 条记录
- [ ] 随机读取记录
- [ ] 顺序遍历记录

## 6. B+ 树页结构

### 先看

- [ ] 阅读 `src/include/index/generic_key.h`
- [ ] 阅读 `src/include/page/b_plus_tree_page.h`
- [ ] 阅读 `src/include/page/b_plus_tree_leaf_page.h`
- [ ] 阅读 `src/include/page/b_plus_tree_internal_page.h`

### 再写

- [ ] 实现 `src/page/b_plus_tree_page.cpp`
- [ ] 实现 `IsLeafPage`
- [ ] 实现 `IsRootPage`
- [ ] 实现 size/max/min/page id 相关接口
- [ ] 实现 `src/page/b_plus_tree_leaf_page.cpp`
- [ ] 实现叶子页二分查找
- [ ] 实现叶子页插入
- [ ] 实现叶子页删除
- [ ] 实现叶子页 split/merge/redistribute 辅助函数
- [ ] 实现 `src/page/b_plus_tree_internal_page.cpp`
- [ ] 实现内部页查找
- [ ] 实现内部页插入
- [ ] 实现内部页 split/merge/redistribute 辅助函数

### 验证

- [ ] 单独检查页内 key 顺序
- [ ] 检查叶子页 next page id
- [ ] 检查内部页 child parent id 更新

## 7. B+ 树整体

### 先看

- [ ] 阅读 `src/include/index/b_plus_tree.h`
- [ ] 阅读 `src/include/index/index_iterator.h`
- [ ] 阅读 `src/include/index/b_plus_tree_index.h`
- [ ] 阅读 `test/index/b_plus_tree_test.cpp`
- [ ] 阅读 `test/index/index_iterator_test.cpp`
- [ ] 阅读 `test/index/b_plus_tree_index_test.cpp`

### 再写

- [ ] 实现 `BPlusTree::IsEmpty`
- [ ] 实现 `BPlusTree::FindLeafPage`
- [ ] 实现 `BPlusTree::GetValue`
- [ ] 实现 `BPlusTree::Insert`
- [ ] 实现 `BPlusTree::StartNewTree`
- [ ] 实现 `BPlusTree::InsertIntoLeaf`
- [ ] 实现 `BPlusTree::Split`
- [ ] 实现 `BPlusTree::InsertIntoParent`
- [ ] 实现 `BPlusTree::Remove`
- [ ] 实现 `IndexIterator`
- [ ] 实现 `Begin`
- [ ] 实现 `End`

### 验证

- [ ] 运行 `b_plus_tree_test`
- [ ] 运行 `index_iterator_test`
- [ ] 运行 `b_plus_tree_index_test`
- [ ] 插入大量 key 后仍能查询
- [ ] 删除 key 后查询失败
- [ ] 迭代器顺序正确

## 8. Catalog 层

### 先看

- [ ] 阅读 `src/include/catalog/table.h`
- [ ] 阅读 `src/catalog/table.cpp`
- [ ] 阅读 `src/include/catalog/indexes.h`
- [ ] 阅读 `src/catalog/indexes.cpp`
- [ ] 阅读 `src/include/catalog/catalog.h`
- [ ] 阅读 `test/catalog/catalog_test.cpp`

### 再写

- [ ] 实现 `CatalogMeta::GetSerializedSize`
- [ ] 实现 `IndexMetadata::GetSerializedSize`
- [ ] 实现 `IndexInfo::Init`
- [ ] 实现 `CatalogManager` 构造函数
- [ ] 实现 `CreateTable`
- [ ] 实现 `GetTable`
- [ ] 实现 `GetTables`
- [ ] 实现 `CreateIndex`
- [ ] 实现 `GetIndex`
- [ ] 实现 `GetTableIndexes`
- [ ] 实现 `DropTable`
- [ ] 实现 `DropIndex`
- [ ] 实现 `FlushCatalogMetaPage`
- [ ] 实现 `LoadTable`
- [ ] 实现 `LoadIndex`

### 验证

- [ ] 运行 `catalog_test`
- [ ] 创建表后能查到
- [ ] 重启数据库后表仍能加载
- [ ] 创建索引后能查到
- [ ] 重启数据库后索引仍能加载

## 9. Executor 层

### 先看

- [ ] 阅读 `src/include/executor/execute_context.h`
- [ ] 阅读 `src/include/executor/plans/*.h`
- [ ] 阅读 `src/include/executor/executors/*.h`
- [ ] 阅读 `src/executor/*_executor.cpp`
- [ ] 阅读 `test/execution/executor_test.cpp`

### 再写

- [ ] 实现 `ValuesExecutor`
- [ ] 实现 `SeqScanExecutor`
- [ ] 实现 `InsertExecutor`
- [ ] 实现 `DeleteExecutor`
- [ ] 实现 `UpdateExecutor`
- [ ] 实现 `IndexScanExecutor`
- [ ] 实现 `ExecuteEngine::ExecuteCreateTable`
- [ ] 实现 `ExecuteEngine::ExecuteDropTable`
- [ ] 实现 `ExecuteEngine::ExecuteCreateIndex`
- [ ] 实现 `ExecuteEngine::ExecuteDropIndex`
- [ ] 实现 `ExecuteEngine::ExecuteShowIndexes`
- [ ] 实现 `ExecuteEngine::ExecuteExecfile`
- [ ] 实现 `ExecuteEngine::ExecuteQuit`

### 验证

- [ ] 运行 `executor_test`
- [ ] 测试 select
- [ ] 测试 insert
- [ ] 测试 delete
- [ ] 测试 update
- [ ] 测试 index scan

## 10. Parser 和 Planner

### 先看

- [ ] 阅读 `src/include/parser/syntax_tree.h`
- [ ] 阅读 `src/include/parser/minisql.y`
- [ ] 阅读 `src/planner/planner.cpp`
- [ ] 阅读 `src/include/planner/statement/*.h`

### 理解

- [ ] SQL 如何变成 AST
- [ ] AST 如何变成 Statement
- [ ] Statement 如何变成 Plan
- [ ] Plan 如何交给 Executor

一般不建议先改 parser，除非你要新增 SQL 语法。

## 11. Concurrency

### 先看

- [ ] 阅读 `src/include/concurrency/txn.h`
- [ ] 阅读 `src/include/concurrency/txn_manager.h`
- [ ] 阅读 `src/include/concurrency/lock_manager.h`
- [ ] 阅读 `test/concurrency/lock_manager_test.cpp`

### 再写

- [ ] 实现共享锁
- [ ] 实现排他锁
- [ ] 实现锁升级
- [ ] 实现解锁
- [ ] 实现等待图
- [ ] 实现环检测
- [ ] 实现死锁检测线程

### 验证

- [ ] 运行 `lock_manager_test`
- [ ] 检查 Growing/Shrinking 状态
- [ ] 检查升级冲突
- [ ] 检查死锁中止事务

## 12. Recovery

### 先看

- [ ] 阅读 `src/include/recovery/log_rec.h`
- [ ] 阅读 `src/include/recovery/recovery_manager.h`
- [ ] 阅读 `test/recovery/recovery_manager_test.cpp`

### 再写

- [ ] 实现 BeginLog
- [ ] 实现 InsertLog
- [ ] 实现 DeleteLog
- [ ] 实现 UpdateLog
- [ ] 实现 CommitLog
- [ ] 实现 AbortLog
- [ ] 实现 RedoPhase
- [ ] 实现 UndoPhase

### 验证

- [ ] 运行 `recovery_manager_test`
- [ ] 检查 redo 后数据正确
- [ ] 检查 undo 后未提交事务被回滚

## 13. 最终验证

- [ ] 删除旧构建目录
- [ ] 重新 `cmake ..`
- [ ] 重新 `make -j`
- [ ] 运行全部测试：`./test/minisql_test`
- [ ] 运行 main 程序手动输入 SQL
- [ ] 测试 create database
- [ ] 测试 use database
- [ ] 测试 create table
- [ ] 测试 insert
- [ ] 测试 select
- [ ] 测试 create index
- [ ] 测试 delete
- [ ] 测试 update
- [ ] 测试 drop table
- [ ] 测试 quit


BMP文件结构、图像分类（压缩不压缩等）、大光圈小光圈对景深的影响、透镜的影响