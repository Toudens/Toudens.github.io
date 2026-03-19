---
title: Ch-5 Induction
date: 2026-03-19
type: docs
weight: "5"
---
### Word Table
| 术语       | 翻译  | 术语                     | 翻译    | 术语        | 翻译   |
| -------- | --- | ---------------------- | ----- | --------- | ---- |
| deduce   | 演绎  | mathematical induction | 数学归纳法 | validity  | 有效性  |
| polygon  | 多边形 | interior               | 内部    | exterior  | 外部   |
| diagonal | 对角线 | interior diagonal      | 内对角线  | convex    | 凸多边形 |
| vertex   | 顶点  | triangulation          | 三角剖分  | recursion | 递归   |
### Mathematical Induction

**mathematical induction** is used to prove propositions of form $\forall nP(n)$ where the domain of discourse is the set of positive integers:
$$
P(n_0)\land\forall k\geq n_0(P(k)\rightarrow P(k+1))\rightarrow\forall n\geq n_0(P(n))
$$
1. **Basis step**: Establish $P(1)$
2. **Inductive step**: Prove that $P(k)\rightarrow P(k+1)$ for $k\geq 1$
3. **Conclusion**: The basis step and the inductive step together imply $\forall nP(n)$

> [!Note] **Proof of Mathematical induction**
> The validity of mathematical induction follows from the well-ordering property for the set of $\mathrm{Z}^+$.
> 1. Assume that there is at least of positive integer for which $P(n)$ is false
> 2. $S$ is the set of positive integer for which $P(n)$ is false, then $S$ is nonempty
> 3. By the well-ordering property, $S$ has a least element,  denoted by $m$
> 4. Then $m\neq1,m-1$ is a positive integer, $m-1$ is not in $S$ ,so $P(m-1)$ is true
> 5.  Since the implication $P(m-1)\rightarrow P(m)$ is also true ,$P(m)$ must be true
> 
> by contradiction ,$\forall nP(n)$

### Strong Induction

strong induction or second principle of mathematical induction.
$$
P(n_0)\land\forall k\geq n_0(P(n_0)\land P(n_0+1)\land\cdots\land P(k)\rightarrow P(k+1))\rightarrow \forall n\geq n_0(P(n))
$$
1. **Basis step**: Establish $P(n_0)$
2. **Inductive Step**: Prove $P(n_0)\land P(n_0+1)\land\cdots\land P(k)\rightarrow P(k+1)$
3. **Conclusion**: the basis step and the inductive step together imply $\forall n\geq n_0 P(n)$

>[!Note] Note
>The validities of both mathematical induction and strong induction follow from the well-ordering property. In fact, mathematical induction, strong induction, and well-ordering are all equivalent principles.

### Structural Induction

recursion is a principle closely related to mathematical induction. In a recursive definition, an object is defined in terms of itself.

1. **basis step**: Show that the result holds for all elements specified in the basis step of thee recursive definition to be in the set
2. **Recursive step**: Show that if the statement is true for each of the elements used to construct new elements in the recursive step of the definition, the result holds for these new elements.