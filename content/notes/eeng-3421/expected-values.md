---
author: "Anish Goyal"
title: "Expected Values"
description: "lecture18-20-3421.pdf"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-03-31T18:44:59
modified: 2026-03-31T18:45:30
readingtime: "1"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 17
weight: 170
slug: "expected-values"
links: []
sources:
  - "Course lecture slides 18–20"
generated: true
---

## Expected Value for Continuous RV {#expected-value-for-continuous-rv}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="17.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 17.1</span> <span class="theorem-callout-subtitle">(Expected Value)</span>.</div></div>
<div class="callout-content">

The expected value of a continuous random variable $X$ is

$$
E[X]=\int_{-\infty}^{\infty} x f_X(x)\,dx
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="17.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 17.2</span> <span class="theorem-callout-subtitle">(Expected Value of a Function of a Continuous RV)</span>.</div></div>
<div class="callout-content">

The expected value of a function $g(X)$ of random variable $X$ is

$$
E[g(X)]=\int_{-\infty}^{\infty} g(x) f_X(x)\,dx
$$

</div>
</div>

## Properties {#properties}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="17.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 17.3</span> <span class="theorem-callout-subtitle">(Core Identities)</span>.</div></div>
<div class="callout-content">

For any random variable $X$
- centering

$$
E[X-\mu_X]=0
$$

- linearity for affine functions

$$
E[aX+b]=aE[X]+b
$$

- variance expansion

$$
\mathrm{Var}[X]=E[X^2]-\mu_X^2
$$

- variance scaling

$$
\mathrm{Var}[aX+b]=a^2\mathrm{Var}[X]
$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 18–20</span>
