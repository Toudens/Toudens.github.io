---
title: Ch-4 Number Theory
date: 2026-03-19
type: docs
weight: "4"
---
### Word Table

| 术语         | 翻译  | 术语        | 翻译  | 术语          | 翻译  |
| ---------- | --- | --------- | --- | ----------- | --- |
| arithmetic | 算数  | congruent | 一致的 | pseudoprime | 伪素数 |
### Division

The notation $a\mid b$ denotes that $a$ divides $b$ ,and $a\not\mid b$ denotes that $a$ does not divide $b$
Let $a,b$ and $c$ be integers, where $a\neq0$ ,then:
*  if $a\mid b$ and $a\mid c$ ,then $a\mid(b+c)$
*  if $a\mid b$ then $a\mid bc$ for all integers $c$
*  if $a\mid b$ and $b\mid c$ ,then $a\mid c$
*  if $a\mid b$ and $a\mid c$ ,then $a\mid mb+nc$ whenever $m$ and $n$ are integers
### Modular Arithmetic

We use the notation $a\equiv b(\mathrm{mod}\,m)$ to indicate that $a$ is congruent to $b$ modulo $m$ 

* Let $a$ and $b$ be integers, and $m$ be a positive integer, then $a\equiv b(\mathrm{mod}\,m)$ if and only if $a\,\mathrm{mod}\,m=b\,\mathrm{mod}\,m$
* Let $m$ be a positive integer, if $a\equiv b(\mathrm{mod}\,m)$ and $c\equiv d(\mathrm{mod}\,m)$, then $a+c\equiv b+d(\mathrm{mod}\,m)$ and $ac\equiv bd(\mathrm{mod}\,m)$
* Let $m$ be a positive integer and let $a$ and $b$ be integers, then $(a+b)\,\mathrm{mod}\,m=((a\,\mathrm{mod}\,m)+(b\,\mathrm{mod}\,m))\,\mathrm{mod}\,m$ and $ab\,\mathrm{mod}\,m=((a\,\mathrm{mod}\,m)(b\,\mathrm{mod}\,m))\,\mathrm{mod}\,m$
### Arithmetic Modulo m

**Closure**: If $a$ and $b$ belong to $\mathrm{Z}_m$ ,then $a+_mb$ and $a\cdot_mb$ belong to $\mathrm{Z}_m$

**Associativity**:  $(a+_mb)+_mc=a+_m(b+_mc)$ and $(a\cdot_mb)\cdot_mc=a\cdot_m(b\cdot_mc)$

**Commutativity**:  $a+_mb=b+_ma$ and $a\cdot_mb=b\cdot_ma$

**Identity elements**: $a+_m0=0+_ma=a$ and $a\cdot_m1=1\cdot_ma=a$

**Additive inverses**: $a+_m(m-a)=0$ and $0+_m0=0$

**Distributivity**: $a\cdot_m(b+_mc)=(a\cdot_mb)+(a\cdot_mc)$ and $(a+_mb)\cdot_mc=(a\cdot_mc)+_m(b\cdot_mc)$
### Primes

An integer $p$ greater than $1$ is called prime if the only positive factors of $p$ are $1$ and $p$
A positive integer that is greater than $1$ and is not prime is called composite

> [!Note] **the fundamental theorem of arithmetic**
> Every integer greater than $1$ can be written uniquely as a prime or as the product of two or more primes, where the prime factors are written in order of nondecreasing size.

### GCD and LCM

Let $a$ and $b$ be integers, not both zero. The largest integer $d$ such that $d\mid a$ and $d\mid b$ is called the greatest common divisor of $a$ and $b$, denoted by $\gcd(a, b)$

The integers $a$ and $b$ are relatively prime if their greatest common divisor is $1$

The integers $a_1, a_2,\cdots, a_n$ are pairwise relatively prime if $\gcd(a_i , a_j ) = 1$ whenever $1\leq i < j \leq n$

The least common multiple of the positive integers a and b is the smallest positive integer that is divisible by both $a$ and $b$, denoted by $\mathrm{lcm}(a, b)$

*  If $\gcd(a,b)=1$ and $a\mid bc$ ,then $a\mid c$
*  If $p$ is prime and $p\mid a_1a_2\cdots a_n$ where each $a_i$ is an integer, then $p|a_i$ for some $i$
*  If $ac\equiv bc(\mathrm{mod}\,m)$ and $\gcd(c,m)=1$ ,then $a\equiv b(\mathrm{mod}\,m)$
### Bezout's Theorem

If $a$ and $b$ are positive integers, then there exist integers $s$ and $t$ such that $\gcd(a, b) = sa + tb$
### Fermat's Little Theorem

If $p$ is prime and $a$ is an integer not divisible by $p$ ,then:
$$
a^{p-1}\equiv 1(\mathrm{mod}\,p)
$$
### Pseudoprimes

Let $b$ be a positive integer. If $n$ is a composite positive integer, and $b^{n−1} \equiv 1 (\mathrm{mod}\, n)$, then $n$ is called a pseudoprime to the base $b$