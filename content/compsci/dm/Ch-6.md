---
title: Ch-6 Counting I
date: 2026-03-19
type: docs
weight: "6"
---
### Word Table

| 术语       | 翻译  | 术语          | 翻译  | 术语          | 翻译  |
| -------- | --- | ----------- | --- | ----------- | --- |
| disjoint | 不相交 | combination | 组合  | permutation | 排列  |
### Counting Principles

**The Sum Rule** : If $S$ and $T$ are disjoint finite sets, then $|S\cup T|=|S|+|T|$

**The Product Rule** : If $S$ and $T$ are finite sets, then $|S\times T|=|S|\times|T|$

**The Inclusion-Exclusion Principle** : If $S$ and $T$ are finite sets, then $|S\cup T|=|S|+|T|-|S\cap T|$
### The Pigeonhole Principle

If $k$ is a positive integer and $k+1$ or more objects are placed into $k$ boxes, then there is at least one box containing two or more of the objects.

If $n$ objects are placed into $k$ boxes, then there is at least one box containing at least $\lceil n/k\rceil$ objects.
### Applications of P&C

**r-permutation with repetition**: The number of r-permutations of a set of $n$ objects with repetition allowed 
$$
n^r
$$
**n-permutation with limited repetition**: the number of different permutation of $n$ objects, where there are $n_1,n_2,\cdots,n_k$ indistinguishable objects
$$
\frac{n!}{n_1!n_2!\cdots n_k!}
$$
**r-circle permutation**: The number of r-circle permutations of a set of $n$ objects is
$$
\frac{P(n,r)}{r}
$$
**r-combination with repetition**: The number of r-combination from a set with $n$ elements when repetition of elements is allowed is
$$
\begin{pmatrix}n+r-1\\r\end{pmatrix}
$$
**Indistinguishable objects and distinguishable boxes**: The number of ways to distribute $n$ indistinguishable objects into kk distinguishable boxes is
$$
\begin{pmatrix}n-1\\k-1\end{pmatrix}
$$
### Combinatorial Identities

**the binomial theorem**: Let $x$ and $y$ be variables, and let $n$ be a nonnegative integer
$$
\begin{align}
(x+y)^n=\sum_{j=0}^n\begin{pmatrix}n\\j\end{pmatrix}x^{n-j}y^j
\end{align}
$$
**Pascal's identity**: Let $n$ and $k$ be positive integers with $k\leq n$ ,then
$$
\begin{pmatrix}n+1\\k\end{pmatrix}=
\begin{pmatrix}n\\k-1\end{pmatrix}+
\begin{pmatrix}n\\k\end{pmatrix}
$$
**Vandermonde's identity**: Let $m,n$ and $r$ be nonnegative integer with $r\leq m,n$，then
$$
\begin{pmatrix}m+n\\r\end{pmatrix}=
\sum_{k=0}^r
\begin{pmatrix}m\\r-k\end{pmatrix}
\begin{pmatrix}n\\k\end{pmatrix}
$$
Let $n$ and $r$ be nonnegative integer with $r\leq n$ ,then
$$
\begin{pmatrix}n+1\\r+1\end{pmatrix}=
\sum_{j=r}^n
\begin{pmatrix}j\\r\end{pmatrix}
$$
### Combinatorial Proofs

**double counting proof**: uses counting arguments to prove that both sides of an identity count the same objects, but in different ways.

**bijective proof**: shows that there is a bijection between the sets of objects counted by the two sides of the identity.