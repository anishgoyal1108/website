---
author: "Anish Goyal"
title: "Functions of a Random Variable"
description: "Sometimes we define a new random variable in terms of an existing one"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-03-31T18:19:21
modified: 2026-03-31T18:20:06
readingtime: "2"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 11
weight: 110
slug: "functions-of-a-random-variable"
links: []
sources:
  - "Course lecture slides 16–17"
generated: true
---

## Derived Random Variables {#derived-random-variables}

- Sometimes we define a new random variable in terms of an existing one
- The new random variable is called a derived random variable
- The mapping is a deterministic function applied to the original random variable

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="11.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 11.1</span> <span class="theorem-callout-subtitle">(Derived Random Variable)</span>.</div></div>
<div class="callout-content">

Each sample value $y$ of a derived random variable $Y$ is a mathematical function $g(x)$ of a sample value $x$ of another random variable $X$
We write

$$
Y = g(X)
$$

</div>
</div>

- The range of $Y$ is
	- all possible values $g(x)$ where $x \in S_X$
	- multiple values of $x$ may map to the same $y$
- When multiple $x$ map to the same $y$, the probabilities add

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="11.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 11.2</span> <span class="theorem-callout-subtitle">(PMF of a Derived Random Variable)</span>.</div></div>
<div class="callout-content">

For a discrete random variable $X$, the PMF of $Y=g(X)$ is

$$
P_Y(y) = \sum_{x \,:\, g(x)=y} P_X(x)
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="11.3">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 11.3</span> <span class="theorem-callout-subtitle">(One to One Case)</span>.</div></div>
<div class="callout-content">

If $g$ is one to one on $S_X$, then for $y=g(x)$

$$
P_Y(y) = P_X(x)
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="11.4">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 11.4</span> <span class="theorem-callout-subtitle">(Many to One Case)</span>.</div></div>
<div class="callout-content">

If $g(x_1)=g(x_2)=y$ with $x_1\ne x_2$, then

$$
P_Y(y)=P_X(x_1)+P_X(x_2)
$$

and similarly for more than two preimages

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 16–17</span>
