---
author: "Anish Goyal"
title: "Variance and Standard Deviation"
description: "Variance measures spread around the mean"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-03-31T18:35:41
modified: 2026-05-06T06:39:38
readingtime: "2"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 13
weight: 130
slug: "variance-and-standard-deviation"
links: []
sources:
  - "Course lecture slides 16–17"
generated: true
---

## Variance {#variance}
- Variance measures spread around the mean
- Variance is the expected squared deviation from the mean

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="13.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 13.1</span> <span class="theorem-callout-subtitle">(Variance)</span>.</div></div>
<div class="callout-content">

The variance of random variable $X$ is

$$
\mathrm{Var}[X] = E\left[(X-\mu_X)^2\right]
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="13.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 13.2</span> <span class="theorem-callout-subtitle">(Standard Deviation)</span>.</div></div>
<div class="callout-content">

The standard deviation of random variable $X$ is

$$
\sigma_X = \sqrt{\mathrm{Var}[X]}
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="13.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 13.3</span> <span class="theorem-callout-subtitle">(Moments)</span>.</div></div>
<div class="callout-content">

For random variable $X$
- The $n$th moment is

$$
E[X^n]
$$

- The $n$th central moment is

$$
E[(X-\mu_X)^n]
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="13.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 13.4</span> <span class="theorem-callout-subtitle">(Variance Expansion)</span>.</div></div>
<div class="callout-content">

$$
\mathrm{Var}[X] = E[X^2]-\mu_X^2 = E[X^2]-(E[X])^2
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="13.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 13.5</span> <span class="theorem-callout-subtitle">(Variance Under Affine Transformations)</span>.</div></div>
<div class="callout-content">

For constants $a,b$

$$
\mathrm{Var}[aX+b] = a^2\mathrm{Var}[X]
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="13.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 13.6</span> <span class="theorem-callout-subtitle">(Variances of Common Families)</span>.</div></div>
<div class="callout-content">

- If $X$ is Bernoulli $(p)$

$$
\mathrm{Var}[X] = p(1-p)
$$

- If $X$ is Geometric $(p)$

$$
\mathrm{Var}[X] = \frac{1-p}{p^2}
$$

- If $X$ is Binomial $(n,p)$

$$
\mathrm{Var}[X] = np(1-p)
$$

- If $X$ is Pascal $(k,p)$

$$
\mathrm{Var}[X] = \frac{k(1-p)}{p^2}
$$

- If $X$ is Poisson $(\alpha)$

$$
\mathrm{Var}[X] = \alpha
$$

- If $X$ is Discrete Uniform $(k,\ell)$

$$
\mathrm{Var}[X] = \frac{(\ell-k)(\ell-k+2)}{12}
$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 16–17</span>
