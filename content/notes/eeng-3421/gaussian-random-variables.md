---
author: "Anish Goyal"
title: "Gaussian Random Variables"
description: "For a Gaussian random variable"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-03-31T18:46:26
modified: 2026-03-31T18:47:04
readingtime: "2"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 19
weight: 190
slug: "gaussian-random-variables"
links: []
sources:
  - "Course lecture slides 18–20"
generated: true
---

## Gaussian $(\mu,\sigma)$ {#gaussian}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="19.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 19.1</span> <span class="theorem-callout-subtitle">(Gaussian Random Variable)</span>.</div></div>
<div class="callout-content">

$X$ is a Gaussian $(\mu,\sigma)$ random variable if the PDF of $X$ is

$$
f_X(x)=\frac{1}{\sqrt{2\pi}\sigma}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

where $\mu\in\mathbb R$ and $\sigma>0$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="19.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 19.2</span> <span class="theorem-callout-subtitle">(Gaussian Mean Variance)</span>.</div></div>
<div class="callout-content">

If $X$ is Gaussian $(\mu,\sigma)$

$$
E[X]=\mu
$$

$$
\mathrm{Var}[X]=\sigma^2
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="19.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 19.3</span> <span class="theorem-callout-subtitle">(Affine Transform of Gaussian)</span>.</div></div>
<div class="callout-content">

If $X$ is Gaussian $(\mu,\sigma)$ and $Y=aX+b$
then $Y$ is Gaussian $(a\mu+b,|a|\sigma)$

</div>
</div>

## Standard Normal {#standard-normal}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="19.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 19.4</span> <span class="theorem-callout-subtitle">(Standard Normal Random Variable)</span>.</div></div>
<div class="callout-content">

The standard normal random variable $Z$ is the Gaussian $(0,1)$ random variable

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="19.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 19.5</span> <span class="theorem-callout-subtitle">(Standard Normal CDF)</span>.</div></div>
<div class="callout-content">

The CDF of $Z$ is

$$
\Phi(z)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{z} e^{-u^2/2}\,du
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="19.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 19.6</span> <span class="theorem-callout-subtitle">(Standardization)</span>.</div></div>
<div class="callout-content">

If $X$ is Gaussian $(\mu,\sigma)$ then

$$
Z=\frac{X-\mu}{\sigma}
$$

is standard normal

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="19.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 19.7</span> <span class="theorem-callout-subtitle">(Gaussian CDF via Standard Normal)</span>.</div></div>
<div class="callout-content">

If $X$ is Gaussian $(\mu,\sigma)$ then

$$
F_X(x)=\Phi\left(\frac{x-\mu}{\sigma}\right)
$$

and for $a<b$

$$
P[a<X\le b]=\Phi\left(\frac{b-\mu}{\sigma}\right)-\Phi\left(\frac{a-\mu}{\sigma}\right)
$$

</div>
</div>

## Symmetry {#symmetry}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="19.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 19.8</span> <span class="theorem-callout-subtitle">(Standard Normal Symmetry)</span>.</div></div>
<div class="callout-content">

$$
\Phi(-z)=1-\Phi(z)
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="19.9">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 19.9</span> <span class="theorem-callout-subtitle">(Symmetric Interval Probability)</span>.</div></div>
<div class="callout-content">

For $z>0$

$$
P[-z<Z\le z]=2\Phi(z)-1
$$

</div>
</div>

## 68 95 99.7 Rule {#68-95-99-7-rule}

- For a Gaussian random variable
	- about $68\%$ of outcomes are within $1\sigma$ of $\mu$
	- about $95\%$ of outcomes are within $2\sigma$ of $\mu$
	- about $99.7\%$ of outcomes are within $3\sigma$ of $\mu$

## Complementary CDF {#complementary-cdf}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="19.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 19.10</span> <span class="theorem-callout-subtitle">(Complementary CDF)</span>.</div></div>
<div class="callout-content">

The standard normal complementary CDF is

$$
Q(z)=P[Z>z]=\frac{1}{\sqrt{2\pi}}\int_{z}^{\infty} e^{-u^2/2}\,du=1-\Phi(z)
$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 18–20</span>
