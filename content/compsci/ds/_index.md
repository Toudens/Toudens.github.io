---
title: 数据结构基础
date: 2026-06-28
type: docs
weight: "1"
---
【注】本文为笔者复习时记录的易错点，非完整复习笔记。

- predecessor 前驱 successor 后继
- `ooo` 132,123,213,312,321
- 树的节点的度：连接的子树数量
- 树的度是节点度的最大值
- 叶子节点的度为零
- 路径的长度就是路径上的边的数量
- 深度为根到节点的长度
- 高度为节点到叶子结点的最长路径长度
- 树的高度为根的高度
- preorder 先序 postorder 后序 inorder 中序 levelorder 层序
- 左儿子为空指向中序前驱，右儿子为空指向中序后继
- head->left 指向根节点，中序遍历的第一个前驱与最后一个后继指向 head
- perfect binary tree：高度为 $h$ 的满二叉树有 $2^{h+1}-1$ 个节点
- complete binary tree：除最后一层全满，最后一层节点从左到右连续排列无空缺
- full binary tree：一个节点要么没有孩子，要么有两个孩子
- 斜二叉树：退化成链表的二叉树
- 二叉搜索树删除有两种策略：用左儿子最大或右儿子最小替换
- 小根堆 min heap 同时满足两个条件：完全二叉树，每个节点不大于儿子节点
- 满二叉树的左右节点高度之和为 $2^{h+1}-1-(h+1)$ 
- 满足自反性、传递性、对称性的是等价关系，等价类是被等价关系分到同一组的元素集合
- 连通分量定义在无向图上，强联通分量定义在有向图上，将有向边变为无向边则连通的有向图被称为弱连通的
- AOE网中，如果存在 $i$ 到 $j$ 的一条路径，则 $i$ 是 $j$ 的 predecessor，如果存在一条直接边从 $i$ 到 $j$ ，则 $i$ 是 $j$ 的 immediate predecessor
- Dijkstra 的时间复杂度为 $\Theta(|E|\log|V|)$，SPFA 的时间复杂度为 $\Theta(|E||V|)$
- AOE 网中一条边 $<v,w>$ 的 slack time 为 $LC_w-EC_v-C_{v,w}$
- 有 $n$ 个不同数的序列，平均逆序对个数为 $n(n-1)/4$
- 插入排序的时间复杂度为 $\Theta(I+N)$ 其中 $I$ 为序列的逆序对个数
- 双联通分量指的是删去任何一个节点 ，仍然为联通分量，若删去后变为至少两个连通分类，则这个删去的节点是 anticulation point
- 寻找欧拉回路的算法时间复杂度为 $\Theta(|V|+|E|)$ 
- 不加优化的希尔排序的最坏时间复杂度为 $\Theta(N^2)$ ，加了 Hibbard's Increments 的最坏时间复杂度为 $\Theta(N^{3/2})$ 
- $T$ 是所有标识符可能布线的不同值，$n$ 是在哈希表中的标识符，则 identifier density 为 $n/T$ ，loading density 为 $n/(s\cdot b)$
- 哈希冲突指的是不同的标识符被映射到哈希表的相同 bucket 中，哈希溢出则指哈希表的某 bucket 已经满了，但是又有了新的插入请求
- If quadratic probing is used, and the table size is prime, then a new element can always be inserted if the table is at least half empty.
- If the table size is a prime of the form $4k+3$ , then the quadratic probing $f(x)=\pm i^2$ can probe the entire table.
- double hashing $f(i)=i\times\text{hash}_2(x)$
- usually there should have been $N/2$ insertions before rehash, so $O(N)$ rehash only adds a constant cost to each insertion.
- 线性探测成功查找 $T=\frac{1}{2}\left(1+\frac{1}{1-\lambda}\right)$ ，成功插入（等价于失败查找）$T=\frac{1}{2}\left(1+\frac{1}{(1-\lambda)^2}\right)$
- 开放地址 $h_i(x)=(\text{hash}(x)+f(i))\mod\text{tableSize}$ 注意表的大小不一定和哈希函数一致
- 定义探测距离为 $d(x)=(g(x)-h(x))\%\text{TableSize}$ ，探测距离短的在 Robin Hood Hashing 中定义为 rich 的，长的定义为 poor 的
- Robin Hood Hashing 检查元素是否存在时，如果当前 distance 比位置上的 distance 还要大，就可以中止探测认为元素不存在
- rehashing 时常选比原来的 table size 两倍大的最小素数
- 最大流时间复杂度 $O(f\cdot|E|)$ 其中 $f$ 是最大流的数值，若使用 Dijkstra 算法进行优化，时间复杂度为 $O(|E|^2\log|V|\log\text{cap}_\text{max})$ 
- 最小生成树问题需要考虑图是否连通等问题

| 希尔排序 | 堆排序 | 归并排序 | 快速排序 | 插入排序 | 基数排序 |
| ---- | --- | ---- | ---- | ---- | ---- |
| 不稳定  | 不稳定 | 稳定   | 不稳定  | 稳定   | 稳定   |
