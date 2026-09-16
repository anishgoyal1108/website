---
author: "Anish Goyal"
title: "Set Operations and Identities"
description: "A B \\{x \\ | \\ x A x B\\}"
tags:
  - "notes"
  - "mathematics"
  - "math-2130"
date: 2025-03-12T14:05:33
modified: 2025-03-12T14:34:53
readingtime: "2"
course: "MATH 2130"
course_slug: "math-2130"
subject: "mathematics"
kind: "lecture"
ordinal: 8
weight: 80
slug: "set-operations-and-identities"
links: []
sources:
  - "Course slides §8.2: Set Operations"
  - "Course slides §9.1: Set Identities"
  - "Course slides §9.2: Generalized Union and Intersection"
generated: true
---

## Set Operations {#set-operations}

### Union {#union}
- $A \cup B \equiv \{x \ | \ x\in A \lor x \in B\}$
- The set where $x$ is in $A$ or $B$ for any arbitrary $x$
- $|A \cup B| = |A| + |B| - |A \cap B|$

### Intersection {#intersection}
- $A \cap B \equiv \{x \ | \ x \in A \land x \in B\}$
- The set where $x$ is in both $A$ and $B$ for any arbitrary $x$

### Complement {#complement}
- $\bar{A} \equiv \{x \in U \ | \ x \notin A\}$
- The set where $x$ is not in $A$ for any arbitrary $x$

### Difference {#difference}
- $A - B \equiv \{x \ | \ x \in A \land x \notin B\} \equiv A \cap \bar{B}$
- The set where $x$ is strictly only in $A$, and not $B$, for any arbitrary $x$

### Symmetric Difference {#symmetric-difference}
- $A \oplus B \equiv (A - B) \cup (B - A) \equiv (A \cup B) - (A \cap B)$
- The set where $x$ is either in $A$ or $B$, but not both (xor)
	- $\{x \ | \ x \in A \oplus x \in B\}$

## Set Identities {#set-identities}

### Identity Laws {#identity-laws}
- $A \cup \emptyset = A$
- $A \cap U = A$

### Domination Laws {#domination-laws}
- $A \cup U = U$
- $A \cap \emptyset = \emptyset$

### Idempotent Laws {#idempotent-laws}
- $A \cup A = A$
- $A \cap A = A$

### Complementation Law {#complementation-law}
- $\bar{(\bar{A})} = A$

### Commutative Laws {#commutative-laws}
- $A \cup B = B \cup A$
- $A \cap B = B \cap A$

### Associative Laws {#associative-laws}
- $A \cup (B \cup C) = (A \cup B) \cup C$
- $A \cap (B \cap C) = (A \cap B) \cap C$

### Distributive Laws {#distributive-laws}
- $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
- $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$

### DeMorgan's Laws {#demorgan-s-laws}
- Still applies!

## Generalized Unions and Intersections {#generalized-unions-and-intersections}

### Generalized Union {#generalized-union}
- Denoted as:

$$\bigcup\limits_{i=1}^n A_{i} = A_{1} \cup A_{2} \cup \dots \cup A_{n}$$

- $x \in \bigcup\limits_{i=1}^n A_{i}$ if $\exists i | x \in A_i$

### Generalized Intersection {#generalized-intersection}
- Denoted as:

$$\bigcap\limits_{i=1}^n A_{i} = A_{1} \cap A_{2} \cap \dots \cap A_{n}$$

- $x \in \bigcap\limits_{i=1}^n A_{i}$ if $\forall i | x \in A_i$

## References {#references}
- <span class="cite cite-ref">Course slides §8.2: Set Operations</span>
- <span class="cite cite-ref">Course slides §9.1: Set Identities</span>
- <span class="cite cite-ref">Course slides §9.2: Generalized Union and Intersection</span>
