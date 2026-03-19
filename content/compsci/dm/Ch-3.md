---
title: Ch-3 Algorithm
date: 2026-03-19
type: docs
weight: "3"
---
### Word Table

| 术语           | 翻译  | 术语          | 翻译  | 术语         | 翻译  |
| ------------ | --- | ----------- | --- | ---------- | --- |
| definiteness | 确定性 | correctness | 正确性 | finiteness | 有限性 |
| generality   | 通用性 | notation    | 记号  | complexity | 复杂度 |
### The Growth of Functions

**asymptotic running time** is the number of operation used by the algorithm as the input size approaches infinity
### Big-O notation
Let $f$ and $g$ be functions from $\mathrm{Z}$ (or $\mathrm{R}$) to $\mathrm{R}$ , we say that $f(x)$ is $O(g(x))$ if there are constants $C$ and $k$ such that $|f(x)|\leq C|g(x)|$ whenever $x>k$
### Big-Omega notation
Let $f$ and $g$ be functions from $\mathrm{Z}$ (or $\mathrm{R}$) to $\mathrm{R}$ ,  we say that $f(x)$ is $\Omega(g(x))$ if there are constants $C$ and $k$ such that $|f(x)|\geq C|g(x)|$ whenever $x>k$
### Big-Theta notation
Let $f$ and $g$ be functions from $\mathrm{Z}$ (or $\mathrm{R}$) to $\mathrm{R}$ , we say that $f(x)$ is $\Theta(g(x))$ if $f(x)$ is $O(g(x))$ and $f(x)$ is $\Omega(g(x))$ ,there are constants $C_1,C_2$ and $k$ such that $0\leq C_1g(x)\leq f(x)\leq C_2g(x)$  whenever $x>k$
### Complexity Table

| Complexity        | Terminology            |
| ----------------- | ---------------------- |
| $\Theta(1)$       | constant complexity    |
| $\Theta(\log n)$  | logarithmic complexity |
| $\Theta(n)$       | linear complexity      |
| $\Theta(n\log n)$ | /                      |
| $\Theta(n^b)$     | polynomial complexity  |
| $\Theta(b^n),b>1$ | exponential complexity |
| $\Theta(n!)$      | factorial complexity   |