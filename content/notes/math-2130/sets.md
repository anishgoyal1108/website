---
author: "Anish Goyal"
title: "Sets"
description: "Definition of a set"
tags:
  - "notes"
  - "mathematics"
  - "math-2130"
date: 2025-02-26T14:33:59
modified: 2025-02-26T14:49:12
readingtime: "2"
course: "MATH 2130"
course_slug: "math-2130"
subject: "mathematics"
kind: "lecture"
ordinal: 7
weight: 70
slug: "sets"
links:
  - "/notes/math-2130/cardinality/"
  - "/notes/math-2130/cartesian-product/"
  - "/notes/math-2130/elements/"
  - "/notes/math-2130/empty-set/"
  - "/notes/math-2130/finite/"
  - "/notes/math-2130/power-set/"
  - "/notes/math-2130/proper-subset/"
  - "/notes/math-2130/set/"
  - "/notes/math-2130/subset/"
  - "/notes/math-2130/tuple/"
  - "/notes/math-2130/universal-set/"
sources:
  - "Course slides §7.2: Sets"
  - "Course slides §8.1: Power Set, Cartesian Product"
generated: true
---

## Sets {#sets-1}
- Definition of a <a class="internal-link" href="/notes/math-2130/set/">set</a>
- The objects in a set are <a class="internal-link" href="/notes/math-2130/elements/">elements</a>
- A set is said to contain its elements
	- $a \in A$

## Describing a Set {#describing-a-set}
- $S = \{a, b, c, d\}$
- Ordering of elements is unimportant
- Repeating an element doesn't change the set
- Elipses (...) can describe a set without listing all elements if the pattern is clear

## Important Sets {#important-sets}
- $\mathbb{N}$: natural numbers = $\{0, 1, 2, 3, \dots\}$
- $\mathbb{Z}$: integers = $\{\dots,-3,-2,-1,0,1,2,3,\dots\}$
- $\mathbb{Z}^{+}$: positive integers = $\{1, 2, 3, \dots\}$
- $\mathbb{R}$: real numbers
- $\mathbb{R}^{+}$: positive real numbers
- $\mathbb{C}$: complex numbers
- $\mathbb{Q}$: rational numbers

## Set-Builder Notation {#set-builder-notation}
- Specify the property that all members of a set satisfy
	- $S = \{x \ | \ P(x)\}$
- Intervals:
	- $[a, b] = \{x | a \le x \le b\}$
	- $[a, b) = \{x | a \le x \lt b\}$
	- $(a, b] = \{x | a \lt x \le b\}$
	- $(a, b) = \{x | a \lt x \lt b\}$ 

## Set Equality {#set-equality}
- Two sets are equal iff they have the same elements
	- $\forall x(x \in A \iff x \in B)$
- Definition of <a class="internal-link" href="/notes/math-2130/universal-set/">universal set</a> and <a class="internal-link" href="/notes/math-2130/empty-set/">empty set</a>
	- Note that $\emptyset \ne \{\emptyset\}$

## Set Cardinality {#set-cardinality}
- Definition of <a class="internal-link" href="/notes/math-2130/finite/">finite</a> and <a class="internal-link" href="/notes/math-2130/cardinality/">cardinality</a>
- Cannot take the cardinality of an infinite set or interval

## Subsets {#subsets}
- Definition of <a class="internal-link" href="/notes/math-2130/subset/">subset</a>
- $A = B$ iff $A \subseteq B$ and $B \subseteq A$
- For *any* set S: $\emptyset \subseteq S$ and $S \subseteq S$
- Definition of <a class="internal-link" href="/notes/math-2130/proper-subset/">proper subset</a>

## Power Set {#power-set}
- Definition of <a class="internal-link" href="/notes/math-2130/power-set/">power set</a>
- $B \in \mathscr{P}(A) \iff B \subseteq A$
- $|\mathscr{P}(A)| = 2^{|A|}$
- If $|A| > 0$, $\mathscr{P}(A) \ge 2$

## Tuples and Cartesian Product {#tuples-and-cartesian-product}
- Definition of <a class="internal-link" href="/notes/math-2130/tuple/">tuple</a>
- Definition of <a class="internal-link" href="/notes/math-2130/cartesian-product/">cartesian product</a>
- $|A_1 \times A_2 \times \dots A_n| = |A_1| \cdot |A_2| \cdot \dots \cdot |A_n|$

## Truth Set {#truth-set}
- Outputs a set of elements that meet the constraints of the domain
- Denoted $TS(P, D)$ 

## Quantifiers with Sets {#quantifiers-with-sets}
- $\forall x \in A \ P(x) \equiv\forall x(x \in A \implies P(x))$
- $\exists x \in A \ P(x) \equiv \exists x(x \in A \land P(x))$

<a class="zoom" href="/notes/img/quantifiers-with-sets.png"><img src="/notes/img/quantifiers-with-sets.png" alt="quantifiers with sets" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Course slides §7.2: Sets</span>
- <span class="cite cite-ref">Course slides §8.1: Power Set, Cartesian Product</span>
