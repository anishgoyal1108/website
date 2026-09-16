---
author: "Anish Goyal"
title: "Averages and Expected Value"
description: "Different notions of average capture different ideas of a typical value"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-03-31T18:10:20
modified: 2026-03-31T18:12:29
readingtime: "3"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 10
weight: 100
slug: "averages-and-expected-value"
links: []
sources:
  - "Course lecture slides 15"
generated: true
---

## Averages {#averages}

- Different notions of average capture different ideas of a typical value
- Mean uses all data values and their magnitudes
- Median is based on ordering only
- Mode is based on frequency only

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="10.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 10.1</span> <span class="theorem-callout-subtitle">(Mode)</span>.</div></div>
<div class="callout-content">

A mode of random variable $X$ is a number $x_{\text{mod}}$ satisfying

$$
P_X(x_{\text{mod}}) \ge P_X(x) \quad \text{for all } x
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="10.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 10.2</span> <span class="theorem-callout-subtitle">(Median)</span>.</div></div>
<div class="callout-content">

A median, $x_{\text{med}}$, of random variable $X$ is a number that satisfies

$$
P[X \le x_{\text{med}}] \ge \frac12
$$

$$
P[X \ge x_{\text{med}}] \ge \frac12
$$

</div>
</div>

## Expected Value {#expected-value}

- Expected value is the probability weighted average of the possible values of a random variable
- For discrete $X$, the weights are given by the PMF
- Expected value is also called the mean of $X$
- Notation
	- $E[X]$
	- $\mu_X$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="10.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 10.3</span> <span class="theorem-callout-subtitle">(Expected Value)</span>.</div></div>
<div class="callout-content">

The expected value of $X$ is

$$
E[X] = \mu_X = \sum_{x \in S_X} x P_X(x)
$$

</div>
</div>

- Connection to the empirical average
	- If a value $x$ appears $N(x)$ times in $n$ observations, then the sample mean is
	$$
	\frac{1}{n}\sum_{\text{obs}} x
	$$
	- Grouping by values gives
	$$
	\frac{1}{n}\sum_x x N(x) = \sum_x x \frac{N(x)}{n}
	$$
	- $\frac{N(x)}{n}$ is the relative frequency of $x$
	- In the limit, relative frequency approaches $P_X(x)$
	- This motivates the expected value formula as a limiting average

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="10.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 10.4</span> <span class="theorem-callout-subtitle">(Expected Value as a Weighted Average)</span>.</div></div>
<div class="callout-content">

If $S_X = \{x_1,x_2,\dots\}$ then

$$
E[X] = \sum_i x_i P[X=x_i]
$$

where the weights $P[X=x_i]$ are nonnegative and sum to $1$

</div>
</div>

## Expected Value for Common Families {#expected-value-for-common-families}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="10.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 10.5</span> <span class="theorem-callout-subtitle">(Expected Value of Bernoulli $(p)$)</span>.</div></div>
<div class="callout-content">

If $X$ is Bernoulli $(p)$ then

$$
E[X] = p
$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>
For Bernoulli $(p)$

$$
P_X(0)=1-p,\quad P_X(1)=p
$$

So

$$
E[X] = 0\cdot(1-p) + 1\cdot p = p
$$

<span class="math-booster-end-proof"></span>

</blockquote>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="10.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 10.6</span> <span class="theorem-callout-subtitle">(Expected Value of Geometric $(p)$)</span>.</div></div>
<div class="callout-content">

If $X$ is Geometric $(p)$ then

$$
E[X] = \frac{1}{p}
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="10.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 10.7</span> <span class="theorem-callout-subtitle">(Expected Value of Poisson $(\alpha)$)</span>.</div></div>
<div class="callout-content">

If $X$ is Poisson $(\alpha)$ then

$$
E[X] = \alpha
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="10.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 10.8</span> <span class="theorem-callout-subtitle">(Expected Values of Other Discrete Families)</span>.</div></div>
<div class="callout-content">

- If $X$ is Binomial $(n,p)$

$$
E[X] = np
$$

- If $X$ is Pascal $(k,p)$

$$
E[X] = \frac{k}{p}
$$

- If $X$ is Discrete Uniform $(k,\ell)$

$$
E[X] = \frac{k+\ell}{2}
$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 15</span>
