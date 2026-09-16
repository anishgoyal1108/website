---
author: "Anish Goyal"
title: "Expected Value of a Derived Random Variable"
description: "If Yg(X), we can compute E[Y] without explicitly finding the PMF of Y"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-03-31T18:27:48
modified: 2026-03-31T18:34:01
readingtime: "2"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 12
weight: 120
slug: "expected-value-of-a-derived-random-variable"
links: []
sources:
  - "Course lecture slides 16–17"
generated: true
---

- If $Y=g(X)$, we can compute $E[Y]$ without explicitly finding the PMF of $Y$
- This is useful when $g$ collapses many $x$ values into the same $y$ value

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="12.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 12.1</span> <span class="theorem-callout-subtitle">(Expected Value of a Derived Random Variable)</span>.</div></div>
<div class="callout-content">

Given a random variable $X$ with PMF $P_X(x)$ and the derived random variable $Y=g(X)$

$$
E[Y] = \mu_Y = \sum_{x \in S_X} g(x) P_X(x)
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="12.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 12.2</span> <span class="theorem-callout-subtitle">(Centered Random Variable Has Zero Mean)</span>.</div></div>
<div class="callout-content">

For any random variable $X$

$$
E[X-\mu_X]=0
$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>
Let $g(X)=X-\mu_X$ and apply the derived expectation theorem

$$
E[g(X)] = \sum_{x\in S_X} (x-\mu_X)P_X(x)
$$

Split the sum

$$
\sum_{x\in S_X} xP_X(x) - \mu_X \sum_{x\in S_X} P_X(x)
$$

The first sum is $\mu_X$ by definition
The second sum is $1$
So the result is $0$
<span class="math-booster-end-proof"></span>

</blockquote>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="12.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 12.3</span> <span class="theorem-callout-subtitle">(Linearity for Affine Functions)</span>.</div></div>
<div class="callout-content">

For any random variable $X$ and constants $a,b$

$$
E[aX+b]=aE[X]+b
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="12.4">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 12.4</span> <span class="theorem-callout-subtitle">(Shift Does Not Change Relative Centering)</span>.</div></div>
<div class="callout-content">

$$
E[X+b]=E[X]+b
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="12.5">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 12.5</span> <span class="theorem-callout-subtitle">(Scaling Scales the Mean)</span>.</div></div>
<div class="callout-content">

$$
E[aX]=aE[X]
$$

</div>
</div>

- In general
	- $E[g(X)]$ depends on the full distribution of $X$
	- it is not true that $E[g(X)]=g(E[X])$ unless $g$ is affine

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="12.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 12.6</span> <span class="theorem-callout-subtitle">(Nonlinearity Warning)</span>.</div></div>
<div class="callout-content">

In general

$$
E[g(X)] \ne g(E[X])
$$

when $g$ is nonlinear

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 16–17</span>
