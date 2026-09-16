---
author: "Anish Goyal"
title: "Predicates and Quantifiers"
description: "Variables: x, y, z"
tags:
  - "notes"
  - "mathematics"
  - "math-2130"
date: 2025-02-06T13:21:50
modified: 2025-10-22T00:48:34
readingtime: "1"
course: "MATH 2130"
course_slug: "math-2130"
subject: "mathematics"
kind: "lecture"
ordinal: 3
weight: 30
slug: "predicates-and-quantifiers"
links:
  - "/notes/math-2130/proposition/"
sources:
  - "Course slides §4.1: Predicates, Quantifiers, and De Morgan Laws"
  - "Course slides §4.2: Distributing Quantifiers over Conjunctions and Disjunctions"
generated: true
---

## Predicate Logic {#predicate-logic}
- Variables: $x, y, z$
- Predicates: $P(x), M(x)$
- Quantifiers

## Propositional Functions {#propositional-functions}
- A generalized version of <a class="internal-link" href="/notes/math-2130/proposition/">propositions</a>
	- Contain variables and a predicate (e.g. $P(x)$)
	- Variables can be replaced with elements from their domain

## Quantifiers {#quantifiers}
- *Universal Quantifier*: $\forall x P(x)$: $P(x)$ is true for every $x$ in the domain
	- Equivalent to the conjunction of all inputs in the domain
- *Existential Quantifier*: $\exists x P(x)$: $P(x)$ is true for some $x$ in the domain
	- Equivalent to the disjunction of all inputs in the domain
- You can restrict the scope of a quantifier by the use of a predicate and a logical connective
	- $\forall$ goes with $\rightarrow$
	- $\exists$ goes with $\land$

<a class="zoom" href="/notes/img/restricting-quantifier-scope.png"><img src="/notes/img/restricting-quantifier-scope.png" alt="restricting quantifier scope" loading="lazy"></a>

## Predicate Equivalences {#predicate-equivalences}
- Statements involving predicates and quantifiers are equivalent if and only if they have the same truth value
	- for every predicate substituted into the statement
	- for every domain used for the variables

## References {#references}
- <span class="cite cite-ref">Course slides §4.1: Predicates, Quantifiers, and De Morgan Laws</span>
- <span class="cite cite-ref">Course slides §4.2: Distributing Quantifiers over Conjunctions and Disjunctions</span>
