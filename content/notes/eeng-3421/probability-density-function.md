---
author: "Anish Goyal"
title: "Probability Density Function"
description: "Density is not probability at a point"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-03-31T18:43:58
modified: 2026-03-31T18:44:45
readingtime: "1"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 16
weight: 160
slug: "probability-density-function"
links: []
sources:
  - "Course lecture slides 18–20"
generated: true
---

## PDF {#pdf}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="16.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 16.1</span> <span class="theorem-callout-subtitle">(Probability Density Function)</span>.</div></div>
<div class="callout-content">

The probability density function of a continuous random variable $X$ is

$$
f_X(x)=\frac{dF_X(x)}{dx}
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="16.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 16.2</span> <span class="theorem-callout-subtitle">(Basic Properties of a PDF)</span>.</div></div>
<div class="callout-content">

For a continuous random variable $X$ with PDF $f_X(x)$
- nonnegativity

$$
f_X(x)\ge 0 \quad \text{for all } x
$$

- CDF as an integral of the PDF

$$
F_X(x)=\int_{-\infty}^{x} f_X(u)\,du
$$

- total area

$$
\int_{-\infty}^{\infty} f_X(x)\,dx=1
$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>
Since $F_X(x)$ is nondecreasing its derivative is nonnegative
The integral formula follows from the definition of derivative and the fundamental theorem of calculus
The total area follows by taking $x\to\infty$ in the integral formula and using $F_X(\infty)=1$
<span class="math-booster-end-proof"></span>

</blockquote>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="16.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 16.3</span> <span class="theorem-callout-subtitle">(Probability of an Interval Using the PDF)</span>.</div></div>
<div class="callout-content">

For $x_1<x_2$

$$
P[x_1<X\le x_2]=\int_{x_1}^{x_2} f_X(x)\,dx
$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>
Use

$$
P[x_1<X\le x_2]=F_X(x_2)-F_X(x_1)
$$

and substitute

$$
F_X(x)=\int_{-\infty}^{x} f_X(u)\,du
$$

<span class="math-booster-end-proof"></span>

</blockquote>

## Interpretation of PDF {#interpretation-of-pdf}

- Density is not probability at a point
- Density converts small interval length into probability

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="16.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 16.4</span> <span class="theorem-callout-subtitle">(Small Interval Approximation)</span>.</div></div>
<div class="callout-content">

Let $x_2=x_1+\Delta$ with $\Delta>0$ small

$$
P[x_1<X\le x_1+\Delta]=F_X(x_1+\Delta)-F_X(x_1)
$$

In the limit $\Delta\to 0$

$$
P[x<X\le x+dx]=f_X(x)\,dx
$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 18–20</span>
