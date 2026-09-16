---
author: "Anish Goyal"
title: "Propositional Logic"
description: "From p q, we can form other conditional statements:"
tags:
  - "notes"
  - "mathematics"
  - "math-2130"
date: 2025-01-15T13:12:27
modified: 2025-07-10T00:11:08
readingtime: "3"
course: "MATH 2130"
course_slug: "math-2130"
subject: "mathematics"
kind: "lecture"
ordinal: 1
weight: 10
slug: "propositional-logic"
links:
  - "/notes/math-2130/atomic-propositions/"
  - "/notes/math-2130/proposition/"
sources:
  - "Course slides §1.1: Propositions"
generated: true
---

<div class="transclusion" data-source="04. Notes/Undergraduate Courses/MATH 2130/Proposition.md">
<a class="transclusion-source" href="/notes/math-2130/proposition/" title="Open Proposition"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

## Proposition {#proposition-embed1}
- A declarative statement that is true or false
- Symbolized with propositional variables (typically $p, q, r, s$) 
## Compound Propositions {#compound-propositions-embed1}
- Can be constructed with the use of logical connectives
	- $\neg$ Negation ("not")
	- $\land$ Conjunction ("and")
	- $\lor$ Disjunction ("or")
	- $\implies$ Implication ("implies")
	- $\iff$ Biconditional ("iff")
- The propositions that build a compound proposition are known as <a class="internal-link" href="/notes/math-2130/atomic-propositions/">atomic propositions</a>

</div>

## Logical Connectives Truth Table {#logical-connectives-truth-table}

| p   | q   | $p \land q$ | $p \lor q$ | $p \implies q$ | $p \iff q$ | $p \oplus q$ |
| --- | --- | ----------- | ---------- | -------------- | ---------- | ------------ |
| T   | T   | T           | T          | T              | T          | F            |
| T   | F   | F           | T          | F              | F          | T            |
| F   | T   | F           | T          | T              | F          | T            |
| F   | F   | F           | F          | T              | T          | F            |

## Converse, Contrapositive, and Inverse {#converse-contrapositive-and-inverse}
- From $p \implies q$, we can form other conditional statements:
	- Converse: $q \implies p$
	- Inverse: $\neg p \implies \neg q$
	- Contrapositive: $\neg q \implies \neg p$
- "It raining is a sufficient condition for my not going to town."
	- Converse: "If I do not go to town, then it is raining."
	- Inverse: "If it is not raining, then I will go to town."
	- Contrapositive: "If I go to town, then it is not raining."

## Truth Tables for Compound Propositions {#truth-tables-for-compound-propositions}
- The number of rows are $2^n$ for $n$ propositional variables
- Need a column for every part of a compound proposition that is itself a proposition
- Need a column at the end for the entire compound proposition

### Example Truth Table {#example-truth-table}
- Construct a truth table for $p \lor q \implies \neg r$

| $p$ | $q$ | $r$ | $\neg r$ | $p \lor q$ | $p \lor q \implies \neg r$ |
| --- | --- | --- | -------- | ---------- | -------------------------- |
| F   | F   | F   | T        | F          | T                          |
| F   | F   | T   | F        | F          | T                          |
| F   | T   | F   | T        | T          | T                          |
| F   | T   | T   | F        | T          | F                          |
| T   | F   | F   | T        | T          | T                          |
| T   | F   | T   | F        | T          | F                          |
| T   | T   | F   | T        | T          | T                          |
| T   | T   | T   | F        | T          | F                          |

## References {#references}
- <span class="cite cite-ref">Course slides §1.1: Propositions</span>
