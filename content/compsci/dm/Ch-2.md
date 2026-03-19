---
title: Ch-2 Basic Structures
date: 2026-03-19
type: docs
weight: "2"
---
### Word Table

| 术语          | 翻译   | 术语                    | 翻译   | 术语        | 翻译  |
| ----------- | ---- | --------------------- | ---- | --------- | --- |
| cardinality | 集合的势 | domain                | 定义域  | codomain  | 值域  |
| injection   | 单射   | surjection            | 满射   | bijection | 双射  |
| invertible  | 可逆的  | geometric progression | 等比数列 | countable | 可数  |
| progression | 数列   | common ratio          | 公比   | arbitrary | 任意  |
### Definition of Sets

A set is an unordered collection of objects
* The objects in a set are call the elements, or members, of the set
* $a\in A$ means $A$ is a member of the set $A$
* $a\not\in A$ means $A$ is not a member of the set $A$ 
* empty set: $\emptyset$ 
### Description of Sets

* Roster method: listing all its members between braces $S=\{1,4,5\}$
* Brace notation with ellipses: $S=\{1,2,\cdots,998244353\}$
* Specification using set builder: $S=\{x|P(x)\}$ 
* Venn diagrams
### Relations between Sets

**Subset**: $A\subseteq B\Leftrightarrow\forall x(x\in A\rightarrow x\in B)$

**Equal**: $A=B\Leftrightarrow A\subseteq B\land B\subseteq A$

**Proper Subset**: $A\subset B\Leftrightarrow A\subseteq B\land A\neq B\Leftrightarrow \forall x(x\in A\rightarrow x\in B)\land\exists x(x\in B\land x\not\in A)$

**The Size of Sets**: 
If there are exactly $n$ distinct elements in $S$ where $n$ is a nonnegative integer, we say that $S$ is a finite set and $n$ is the cardinality of $S$

**Power Sets**:
Given a set $S$ ,the power set of $S$ is the set of all subsets of the set $S$ , $\mathcal{P}(x)$ denotes the power set of $S$ 
$$
\mathcal{P}(A)\subset\mathcal{P}(B)\Rightarrow A\subset B
$$
**Cartesian Products**:
The ordered n-tuple $(a_1,a_2,\cdots,a_n)$ is the ordered collection that has $a_1$ as its first element, $a_2$ as its second element, . . . ,and $a_n$ as its nth element
$$
A_1\times A_2\times\cdots\times A_n=\{(a_1,a_2,\cdots,a_n|a_i\in A_i\quad\text{for}\quad i=1,2,\cdots,n\}
$$
**Truth Sets of Quantifiers**:
Given a predicate $P$ and a domain $D$ , the truth set of $P$ is the set of elements $x$ in $D$ for which $P(x)$ is true, which is $\{x\in D|P(x)\}$
### Set Operations


| Operation            | Explanation                                      |
| -------------------- | ------------------------------------------------ |
| Union                | $A\cup B=\{x\vert x\in A\lor x\in B\}$           |
| Intersection         | $A\cap B=\{x\vert x\in A\land x\in B\}$          |
| Difference           | $A-B=\{x\vert x \in A\land x\not\in B\}$         |
| Complement           | $\overline{A}=\{x\vert x\not\in A\land x\in U\}$ |
| Symmetric Difference | $A\oplus B=(A\cup B)-(A\cap B)$                  |
### Functions

Let $A$ and $B$ be nonempty sets, A function $f$ from $A$ to $B$
$$
f:A\rightarrow B,\quad\forall a(a\in A\rightarrow\exists b(b\in B\land f(a)=b))
$$
$A$ is called the domain of $f$ and $B$ is called the codomain of $f$

A function $f$ is **injection (one-to-one function)** if
$$
\forall a\forall b(f(a)=f(b)\rightarrow a=b)
$$
A function $f$ from $A$ to $B$ is called **surjection (onto function)** if 
$$
\forall b\in B\exists a\in A(f(a)=b)
$$
The function is a **bijection (one-to-one correspondence)** if it's both one-to-one and onto
### Inverse Functions

Let $f$ be a bijection from $A$ to $B$ ,then the inverse function of $f$ ,denoted as $f^{-1}$ is the function from $B$ to $A$ defined as
$$
f^{-1}(y)=x\quad\mathrm{iff}\quad f(x)=y
$$
Function $f$ is invertible if and only if $f$ is bijective
### Composition of Functions

Let $g$ be a function from the set $A$ to the set $B$ and let $f$ be a function from the set $B$ to the set $C$ ,the composition of the function $f$ and $g$ denoted by $f\circ g$ is defined by
$$
f\circ g(a)=f(g(a))
$$
$f\circ g$ can not be defined unless the range of $g$ is a subset of the domain of $f$
### Sequence

A sequence is a function from a subset of the set  of integers to a set $S$ , we use the notation $a_n$ to denote the image of the integer $n$ ,we call a term of the sequence

**geometric progression**: the initial term $a$ and common ratio $r$ are real numbers
$$
a,ar,ar^2,\cdots,ar^n
$$
**arithmetic progression**: the initial term $a$ and common difference $d$ are real numbers
$$
a,a+d,a+2d\cdots,a+nd
$$
### Cardinality of Sets

The cardinality of a set $A$ is equal to the cardinality of a set $B$ ,denoted $|A|=|B|$, if and only if there exists a bijection from $A$ to $B$

If there is an injection from $A$ to $B$ , the cardinality of $A$ is less than or the same as the cardinality of $B$ and we write $|A|\leq|B|$ ,when $|A|\leq |B|$ and $A$ and $B$ have different cardinality, then $|A|<|B|$
### Countable

A set that is either finite or has the same cardinality as the set of positive integers called countable

A set that is not countable is called uncountable

When an infinite set $S$ is countable, we denote the cardinality of $S$ by $\aleph_0$ 

If $|A|=|\mathrm{Z}_+|$ , the set $A$ is countable infinite
### Cantor's Theorem

The cardinality of the powerset of an arbitrary set has a greater cardinality than the original arbitrary set.