---
title: Ch-9 Relations
date: 2026-03-19
type: docs
weight: "9"
---
### Word Table
| 术语              | 翻译   | 术语         | 翻译  | 术语                  | 翻译   |
| --------------- | ---- | ---------- | --- | ------------------- | ---- |
| binary relation | 二元关系 | reflexive  | 自反的 | symmetric           | 对称的  |
| antisymmetric   | 反对称的 | vertex     | 顶点  | diagonal            | 对角线的 |
| irreflexive     | 非自反的 | congruence | 一致  | lexicographic order | 字典序  |
| hasse diagram   | 哈塞图  | maximal    | 最大元 | minimal             | 最小元  |
| dual            | 对偶   |            |     |                     |      |
### Relations and Properties

A binary relation from $A$ to $B$ is a subset of $A\times B$

A relation on a set $A$ is a relation from $A$ to $A$ 

| Property      | Requirement                                                                |
| ------------- | -------------------------------------------------------------------------- |
| reflexive     | $\forall a\in A,(a,a)\in R$                                                |
| symmetric     | $\forall a,b\in A,(a,b)\in R\rightarrow (b,a)\in R$                        |
| antisymmetric | $\forall a,b\in A,((a,b)\in R\land (b,a)\in R)\rightarrow a=b$             |
| transitive    | $\forall a,b,c\in A,((a,b)\in R\land(b,c)\in R)\rightarrow (a,c)\in R$     |
| composite     | $(\exists b\in B((a,b)\in R\land(b,c)\in S))\rightarrow (a,c)\in S\circ R$ |

The relation $R$ on a set $A$ is transitive if and only if $R^n\subseteq R$ for $n=1,2,3\cdots$
### n-ary Relations 

An n-ary relation is a subset of $A_1\times A_2\times\cdots\times A_n$

The sets $A_1,A_2,\cdots,A_n$ are called the domains of the relation, $n$ is called its degree

A domain is a primary key when no two n-tuples in the relation have the same value
### Matrices-Relations 

$R$ is symmetric if and only if $M_R=(M_R)^t$
$\begin{cases}M_{R_1\cup R_2}=M_{R_1}\lor M_{R_2}\\M_{R_1\cap R_2}=M_{R_1}\land M_{R_2}\\M_{S\circ R}=M_R\odot M_S\end{cases}$ 
### Closures of Relations

the closure of $R$ with respect to $P$ is the relation $S$ on $A$ with property $P$ that contains $R$  and is a subset of every subset containing $R$ with property $P$

There is a path of length $n$ from $a$ to $b$ if and only if $(a,b)\in R^n$

The connectivity relation $R^\ast$ consists of the pairs $(a,b)$ such that there is a path of length at least one from $a$ to $b$ in $R$ , $\begin{align}R^\ast=\bigcup_{n=1}^\infty R^n\end{align}$

$M_{R^\ast}=M_R\lor M_R^{[2]}\lor M_R^{[3]}\lor\cdots\lor M_R^{[n]}$
### Warshall's Algorithm

$W_k=[w_{ij}^{[k]}],\quad w_{ij}^{[k]}=w_{ij}^{[k-1]}\lor(w_{ik}^{[k-1]}\land w_{kj}^{[k-1]})$
### Equivalence Relations

Equivalence relation is **reflexive, symmetric and transitive**.

Two elements $a$ and $b$ that are related by an equivalence relation are called equivalent. $a\sim b$ denote that $a$ and $b$ are equivalent elements with respect to a particular equivalence relation
### Equivalence Classes

Let $R$ be a equivalence relation on a set $A$ . The set of all elements that are related to an element $a$ of $A$ is called the equivalence class of $a$
$$
[a]_R=\{s|(a,s)\in R\}
$$
If $b\in[a]_R$ , then $b$ is called a representative of this equivalence class

Let $R$ be an equivalence relation on a set $A$. these statements for elements $a$ and $b$ of $A$ are equivalent: $aRb,\quad [a]=[b],\quad [a]\cap[b]\neq\emptyset$ 

Let $R$ be an equivalence relation on a set $S$ , Then the equivalence classes of $R$ form a partition of $S$ . Conversely , given a partition $\{A)i|i\in I\}$ of the set $S$ , there is an equivalence relation $R$ that has the sets $A_i,i\in I$ as its equivalence classes.
### Partial Orderings

A relation $R$ on $S$ is called a **partial ordering** if it is **reflexive, antisymmetric and transitive**. A set $S$ together with a partial ordering $R$ is called a partially ordered set, and is denoted by $(S,R)$ . Members of $S$ are called elements of the poset. 

The elements $a$ and $b$ of a poset $(S,\preceq)$ are called **comparable** if either $a\preceq b$ or $b\preceq a$ . When $a$ and $b$ are elements of $S$ such that neither $a\preceq b$ nor $b\preceq a$ , $a$ and $b$ are called incomparable.

If $(S,\preceq)$ is a poset and every two elements of $S$ are comparable , $S$ is called a totally ordered or linearly ordered set, and $\preceq$ is called a total order or a linear order. A totally ordered set is also called a chain.

$(S,\preceq)$ is a well-ordered set if it is a poset such that $\preceq$ is a total ordering and every nonempty subset of $S$ has a least element.

Suppose that $S$ is a well-ordered set. Then $P(x)$ is true for all $x\in S$ 
For every $y\in S$, if $P(x)$ is true for all $x\in S$ with $x\prec y$ , then $P(y)$ is true

An element of is called **maximal** if it is not **less** than any element of the poset
An element of is called **minimal** if it is not **greater** than any element of the poset

**greatest element** is an element in a poset that is **greater** than every other element
**least element** is an element in a poset that is **less** than every other element

upper bound /lower bound /least upper bound /greatest lower bound

A partially ordered set in which every pair of elements has both a least upper bound and a greatest lower bound is called a lattice

Every finite nonempty poset $(S,\preceq)$ has at least one minimal element