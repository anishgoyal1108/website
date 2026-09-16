---
author: "Anish Goyal"
title: "Functions"
description: "Definition of function"
tags:
  - "notes"
  - "mathematics"
  - "math-2130"
date: 2025-03-31T14:19:32
modified: 2025-03-31T14:19:43
readingtime: "1"
course: "MATH 2130"
course_slug: "math-2130"
subject: "mathematics"
kind: "lecture"
ordinal: 9
weight: 90
slug: "functions"
links:
  - "/notes/math-2130/bijection/"
  - "/notes/math-2130/composition/"
  - "/notes/math-2130/function/"
  - "/notes/math-2130/graph/"
  - "/notes/math-2130/image/"
  - "/notes/math-2130/injection/"
  - "/notes/math-2130/inverse/"
  - "/notes/math-2130/preimage/"
  - "/notes/math-2130/range/"
  - "/notes/math-2130/surjection/"
sources:
  - "Course slides §11.1: Functions"
  - "Course slides §12.1: Function Composition, Floor and Ceiling Functions"
generated: true
---

## Functions {#functions-1}
- Definition of <a class="internal-link" href="/notes/math-2130/function/">function</a>
- For $a \in A$, we write $f(a)$, the image of $a$ to denote the unique element of $B$ assigned to $a$
- Definition of <a class="internal-link" href="/notes/math-2130/image/">image</a>, <a class="internal-link" href="/notes/math-2130/preimage/">preimage</a>, and <a class="internal-link" href="/notes/math-2130/range/">range</a>

<a class="zoom" href="/notes/img/functions-overview.png"><img src="/notes/img/functions-overview.png" alt="functions overview" loading="lazy"></a>
<a class="zoom" href="/notes/img/functions-overview-2.png"><img src="/notes/img/functions-overview-2.png" alt="functions overview 2" loading="lazy"></a>

## Injection and Surjection {#injection-and-surjection}
- Definition of <a class="internal-link" href="/notes/math-2130/injection/">injection</a>
- Definition of <a class="internal-link" href="/notes/math-2130/surjection/">surjection</a>
- Definition of <a class="internal-link" href="/notes/math-2130/bijection/">bijective</a>
	- Bijective functions also have <a class="internal-link" href="/notes/math-2130/inverse/">inverses</a>

## Composition {#composition}
- Definition of <a class="internal-link" href="/notes/math-2130/composition/">composition</a>

## Graphs {#graphs}
- Definition of <a class="internal-link" href="/notes/math-2130/graph/">graph</a>
	- The graph is always a subset of the cartesian product 

## Floor and Ceiling {#floor-and-ceiling}
- $\lfloor x \rfloor = \max\{n \in \mathbb{Z} \ | \ n \le x\}$
- $\lceil x \rceil = \min\{n \in \mathbb{Z} \ | \ n \gt x\}$
- $\forall \ n \in \mathbb{Z}$, $\lceil n \rceil = \lfloor n \rfloor = n$

### Properties {#properties}
- $\lfloor x \rfloor = n \iff x \in [n, n+1) \lor n \in (x-1, x]$
- $\lceil x \rceil = n \iff x \in (n-1, n] \lor n \in [x, x+1)$
- $x - 1 \lt \lfloor x \rfloor \le x \le \lceil x \rceil \lt x + 1$
- $\lfloor -x \rfloor = -(x+1) = -\lceil x \rceil$
- $\lceil -x \rceil = -(x-1) = -\lfloor x \rfloor$
- $\lfloor x + n \rfloor = \lfloor x \rfloor + n$
- $\lceil x + n \rceil = \lceil x \rceil + n$

## References {#references}
- <span class="cite cite-ref">Course slides §11.1: Functions</span>
- <span class="cite cite-ref">Course slides §12.1: Function Composition, Floor and Ceiling Functions</span>
