---
author: "Anish Goyal"
title: "Propositional Equivalences"
description: "A tautology is always true"
tags:
  - "notes"
  - "mathematics"
  - "math-2130"
date: 2025-01-27T14:32:47
modified: 2025-02-01T13:46:22
readingtime: "2"
course: "MATH 2130"
course_slug: "math-2130"
subject: "mathematics"
kind: "lecture"
ordinal: 2
weight: 20
slug: "propositional-equivalences"
links:
  - "/notes/math-2130/contingency/"
  - "/notes/math-2130/contradiction/"
  - "/notes/math-2130/logically-equivalent/"
  - "/notes/math-2130/satisfiable/"
  - "/notes/math-2130/tautology/"
sources:
  - "Course slides §2.1: Logic Applications"
  - "Course slides §3.2: Proving New Equivalences, Satisfibility"
generated: true
---

## Tautologies, Contradictions, and Contingencies {#tautologies-contradictions-and-contingencies}
-  A <a class="internal-link" href="/notes/math-2130/tautology/">tautology</a> is always true
	- $p \lor \neg p$
	- $q \implies (p \lor q)$
- A <a class="internal-link" href="/notes/math-2130/contradiction/">contradiction</a> is always false
- A <a class="internal-link" href="/notes/math-2130/contingency/">contingency</a> is neither a tautology or a contradiction (such as $p$) 
## Logical Equivalence {#logical-equivalence}
- Two propositions, $p$ and $q$, are <a class="internal-link" href="/notes/math-2130/logically-equivalent/">logically equivalent</a> if they have the same truth table
	- Alternatively, if $p \iff q$ is a tautology
	- Labeled $p \equiv q$

## De Morgan's Law {#de-morgan-s-law}
- Distribute the negation and switch the and/or operator

## Key Equivalences {#key-equivalences}
### Identity Laws {#identity-laws}
- $p \land T \equiv p$
- $p \lor F \equiv p$

### Domination Laws {#domination-laws}
- $p \lor T \equiv T$
- $p \land F \equiv F$

### Idempotent Laws {#idempotent-laws}
- $p \lor p \equiv p$
- $p \land p \equiv p$

### Absorption Laws {#absorption-laws}
- $p \land (p \lor q) \equiv p$
- $p \lor (p \land q) \equiv p$

### Commutative Laws {#commutative-laws}
- $p \land q \equiv q \land p$
- $p \lor q \equiv q \lor p$

### Associative Laws {#associative-laws}
- $(p \land q) \land r \equiv p \land (q \land r)$
- $(p \lor q) \lor r \equiv p \lor (q \lor r)$

### Distributive Laws {#distributive-laws}
- $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$
- $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$

## Satisfiability {#satisfiability}
- A compound proposition is <a class="internal-link" href="/notes/math-2130/satisfiable/">satisfiable</a> if there is an arrangement of propositional variables that make its output true, and insatisfiable otherwise
	- can prove insatisfiable if its negation is a tautology

## References {#references}
- <span class="cite cite-ref">Course slides §2.1: Logic Applications</span>
- <span class="cite cite-ref">Course slides §3.2: Proving New Equivalences, Satisfibility</span>
