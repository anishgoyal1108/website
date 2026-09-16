---
author: "Anish Goyal"
title: "Cumulative Distribution Function"
description: "The CDF encodes all probability information about a random variable"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-03-04T09:48:16
modified: 2026-03-31T18:09:13
readingtime: "3"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 9
weight: 90
slug: "cumulative-distribution-function"
links: []
sources:
  - "Course lecture slides 13–14"
generated: true
---

## Cumulative Distribution Function {#cumulative-distribution-function-1}

- The CDF encodes all probability information about a random variable
- It packages probabilities of the form $P[X \le x]$ into a single function of $x$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="09.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 09.1</span> <span class="theorem-callout-subtitle">(Cumulative Distribution Function)</span>.</div></div>
<div class="callout-content">

Let $X$ be a real valued random variable
The cumulative distribution function of $X$ is

$$
F_X(x) = P[X \le x]
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="09.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 09.2</span> <span class="theorem-callout-subtitle">(CDF Determines Interval Probabilities)</span>.</div></div>
<div class="callout-content">

For any real numbers $a < b$

$$
P[a < X \le b] = F_X(b) - F_X(a)
$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>
Write the event $\{X \le b\}$ as a disjoint union

$$
\{X \le b\} = \{X \le a\} \cup \{a < X \le b\}
$$

Take probabilities and subtract $P[X \le a]$
<span class="math-booster-end-proof"></span>

</blockquote>

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="09.3">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 09.3</span> <span class="theorem-callout-subtitle">(One Sided Probability From CDF)</span>.</div></div>
<div class="callout-content">

$$
P[X > a] = 1 - F_X(a)
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="09.4">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 09.4</span> <span class="theorem-callout-subtitle">(Closed Interval Probability)</span>.</div></div>
<div class="callout-content">

$$
P[a \le X \le b] = F_X(b) - \lim_{x \uparrow a} F_X(x)
$$

</div>
</div>

## Basic Properties {#basic-properties}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="09.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 09.5</span> <span class="theorem-callout-subtitle">(Basic Properties of a CDF)</span>.</div></div>
<div class="callout-content">

For any CDF $F_X$
- Boundedness

$$
0 \le F_X(x) \le 1
$$

- Monotonicity

$$
x_1 \le x_2 \implies F_X(x_1) \le F_X(x_2)
$$

- Right continuity

$$
\lim_{h \downarrow 0} F_X(x+h) = F_X(x)
$$

- Limits at infinity

$$
\lim_{x \to -\infty} F_X(x) = 0
$$

$$
\lim_{x \to \infty} F_X(x) = 1
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="09.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 09.6</span> <span class="theorem-callout-subtitle">(Jump Size Equals Point Mass)</span>.</div></div>
<div class="callout-content">

For any real number $x$

$$
P[X=x] = F_X(x) - \lim_{t \uparrow x} F_X(t)
$$

</div>
</div>

- A jump at $x$ means $P[X=x] > 0$
- No jump at $x$ means $P[X=x] = 0$

## Discrete Random Variables {#discrete-random-variables}

- If $X$ is discrete then $F_X$ is a step function
- The steps occur at the values in the range of $X$
- The size of the step at $x$ equals $P[X=x]$

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="09.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 09.7</span> <span class="theorem-callout-subtitle">(CDF in Terms of the PMF)</span>.</div></div>
<div class="callout-content">

If $X$ is discrete with PMF $P_X$

$$
F_X(x) = \sum_{t \in S_X \,:\, t \le x} P_X(t)
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="09.8">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 09.8</span> <span class="theorem-callout-subtitle">(PMF in Terms of the CDF)</span>.</div></div>
<div class="callout-content">

If $X$ is discrete then for any $x \in S_X$

$$
P_X(x) = P[X=x] = F_X(x) - \lim_{t \uparrow x} F_X(t)
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="09.9">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 09.9</span> <span class="theorem-callout-subtitle">(Probability of a Set From the CDF)</span>.</div></div>
<div class="callout-content">

For any set $B \subseteq S_X$

$$
P[X \in B] = \sum_{x \in B} \bigl(F_X(x) - \lim_{t \uparrow x} F_X(t)\bigr)
$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 13–14</span>
