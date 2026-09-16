---
author: "Anish Goyal"
title: "Continuous Random Variables"
description: "A random variable can have a continuous range"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-03-31T18:41:40
modified: 2026-03-31T18:42:16
readingtime: "1"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 14
weight: 140
slug: "continuous-random-variables"
links: []
sources:
  - "Course lecture slides 18–20"
generated: true
---

## Continuous Range {#continuous-range}

- A random variable can have a continuous range
- Typical ranges are intervals of $\mathbb R$
- Common examples
	- arrival time with range $[0,\infty)$
	- voltage with range $(-\infty,\infty)$
	- phase with range $[0,2\pi)$

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="14.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 14.1</span> <span class="theorem-callout-subtitle">(Point Probabilities for Continuous RV)</span>.</div></div>
<div class="callout-content">

If $X$ is continuous then for any real number $x$

$$
P[X=x]=0
$$

</div>
</div>

- For continuous RVs, probability is assigned to intervals not points
- Small intervals can have small probability
- Interval endpoints do not matter for probabilities since single points have probability zero

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="14.2">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 14.2</span> <span class="theorem-callout-subtitle">(Endpoint Irrelevance)</span>.</div></div>
<div class="callout-content">

If $X$ is continuous and $a<b$ then

$$
P[a<X<b]=P[a\le X<b]=P[a<X\le b]=P[a\le X\le b]
$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 18–20</span>
