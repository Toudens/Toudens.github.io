---
title: Ch-1 Logic and Proofs
date: 2026-03-19
type: docs
weight: "1"
---
### Word Table

| 术语            | 翻译  | 术语             | 翻译   | 术语            | 翻译   |
| ------------- | --- | -------------- | ---- | ------------- | ---- |
| rational      | 有理数 | counterexample | 反例   | premise       | 前提   |
| proposition   | 命题  | paradox        | 悖论   | consistent    | 一致的  |
| conjunction   | 和取  | disjunction    | 析取   | exclusive or  | 异或   |
| hypothesis    | 假设  | antecedent     | 假设   | premise       | 假设   |
| conclusion    | 结论  | consequence    | 假设   | converse      | 逆命题  |
| inverse       | 否命题 | contrapositive | 逆否命题 | tautology     | 永真式  |
| contradiction | 永假式 | contingency    | 可能式  | predicate     | 谓词   |
| axiom         | 公理  | corollary      | 推论   | conjecture    | 猜想   |
| lemma         | 引理  | vacuous proof  | 空证明  | trivial proof | 平凡证明 |
### Proposition

**proposition**:  a declarative sentence that is either true or false, but not both.

**propositional variables**: use variables to represent propositions.

**atomic propositions**: Propositions that cannot be expressed in terms of simpler propositions.

**compound propositions**: propositions formed from existing propositions using logical operators.
### Logical Operators

| Connectives   | Expression           | Abbreviation   | Translation |
| ------------- | -------------------- | -------------- | ----------- |
| negation      | $\neg p$             | NOT            | 非           |
| conjunction   | $p\land q$           | AND            | 和取          |
| disjunction   | $p\lor q$            | OR             | 析取          |
| exclusive or  | $p\oplus q$          | XOR            | 异或          |
| conditional   | $p\rightarrow q$     | IF-THEN        | 条件          |
| biconditional | $p\leftrightarrow q$ | IF AND ONLY IF | 双条件         |

The word "or" in English can represent both inclusive and exclusive.
### Conditional Statements

| Statement      | Expression                |
| -------------- | ------------------------- |
| implication    | $p\rightarrow q$          |
| converse       | $q\rightarrow p$          |
| inverse        | $\neg p\rightarrow\neg q$ |
| contrapositive | $\neg q\rightarrow\neg p$ |

The contrapositive has **the same truth values** as the original implication.
### Propositional Equivalences

**tautology**: A proposition which is always true.

**contradiction**: A proposition which is always false.

**contingency**: A proposition which is neither a tautology nor a contradiction .

A compound proposition is satisfiable if there is an assignment of truth values to make it true.

A compound proposition is unsatisfiable when it is false for all assignments of truth values to its variables.
### Logical Laws

![](01.png)
### Normal Forms

**Disjunctive Normal Form**: A formula is said to be in disjunctive normal form if it is written as a disjunction, in which all the terms are conjunctions of literals.

**Conjunctive Normal Form**: A formula is said to be in conjunctive normal form if it is written as a conjunction, in which all the terms are disjunctions of literals.

**minterm**: a conjunctive of literals in which each variable is represented exactly once.

**maxterm**: a disjunctive of literals in which each variable is represented exactly once.

**Full Disjunctive Normal Form**: Each term includes all variables.

**Full Conjunctive Normal Form**: Each term includes all variables.
### Predicate Logic
$$
\begin{align}
&\begin{cases}
\neg\forall xP(x)\equiv\exists x\neg P(x)\\
\neg\exists xP(x)\equiv\forall x\neg P(x)
\end{cases}\\
&\begin{cases}
\forall x(A(x)\land B(x))\equiv\forall xA(x)\land\forall xB(x)\\
\exists x(A(x)\lor B(x))\equiv\exists xA(x)\lor\exists xB(x)
\end{cases}\\
&\begin{cases}
\forall xA(x)\lor\forall xB(x)\Rightarrow\forall x(A(x)\lor B(x))\\
\exists x(A(x)\land B(x))\Rightarrow\exists xA(x)\land\exists xB(x)
\end{cases}
\end{align}
$$
### Nested Quantifiers

Nest quantifiers are quantifiers that occur within the scope of other quantifiers
The order of nested quantifiers matters if quantifiers are of different types.
### Prenex Normal Form

Any expression can be transformed into a prefix normal form.
1.  Eliminate all occurrences of $\rightarrow$ and $\leftrightarrow$ from the formula in question
2.  Move all negations inward such that negation only appear as part if literals
3.  Standardize the variables a part (when necessary)
4.  moving all quantifiers to the front of the formula
### Rules of Inference

An **argument** is a sequence of statements that end with a conclusion.

By **valid** ,we mean the conclusion must follow from the truth of the preceding statements.

We use **rules of inference** to construct valid arguments.
### Direct Proof

A direct proof of a conditional statement $p\rightarrow q$ is constructed when the first step is the assumption that $p$ is true, subsequent steps are constructed using rules of inference, with the final step show that $q$ must also be true.
### Vacuous Proof

The conditional statement $p\rightarrow q$ is true when we know that $p$ is false, consequently, if we can show that $p$ is false, then we have a proof called a vacuous proof.
### Trivial Proof

We can prove a conditional statement $p\rightarrow q$ if we know that the conclusion $q$ is true.
### Proof by Contraposition

To proof the conditional statement $p\rightarrow q$ ,we can proof that $\neg q\rightarrow\neg p$ .
### Proof by Contradiction

Proof $p$ by contradiction:
1. assume $p$ is false
2. deduces that $\neg p\rightarrow(q\land\neg q)$ ,which $q\land\neg q$ is a contradiction
3. $p$ follows from the above

Proof $p\rightarrow q$ by contradiction:
1. assume that both $\neg q$ and $p$ are true
2. show that $(p\land\neg q)\rightarrow\mathrm{F}$ 
### Proof by cases

Convince the reader that the cases are inclusive and establish all implications
Without Loss of Generality: WLOG.
### Exhaustive Proof

An **exhaustive proof** is a special type of proof by cases where each case involves checking a single example.
### Uniqueness Proof

To show that a theorem assert the existence of a unique element with a particular property:
$$
\exists x(P(x)\land\forall y(y\neq x\rightarrow\neg P(y)))
$$
**existence**: show that an element $x$ with the desired property exists.

**uniqueness**: show that if $y\neq x$ ,then $y$ does not have the desired property. 

Equivalently, we can also show that if $x$ and $y$ both have the desired property, then $x=y$ .