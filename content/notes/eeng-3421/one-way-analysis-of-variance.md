---
author: "Anish Goyal"
title: "One-Way Analysis of Variance"
description: "Compare means of more than two populations"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-04-21T16:19:08
modified: 2026-04-21T16:19:50
readingtime: "2"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 28
weight: 280
slug: "one-way-analysis-of-variance"
links: []
sources:
  - "Course lecture slides 23–26"
generated: true
---

## F Distribution {#f-distribution}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="28.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 28.1</span> <span class="theorem-callout-subtitle">(F Distribution)</span>.</div></div>
<div class="callout-content">

The F distribution is continuous and skewed right
It has two degrees of freedom
- numerator degrees of freedom
- denominator degrees of freedom
It has support on nonnegative values

</div>
</div>

## ANOVA Hypotheses {#anova-hypotheses}

- Compare means of more than two populations

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="28.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 28.2</span> <span class="theorem-callout-subtitle">(One Way ANOVA Hypotheses)</span>.</div></div>
<div class="callout-content">

$$
H_0:\ \mu_1 = \mu_2 = \cdots = \mu_k
$$

$$
H_1:\ \text{not all } \mu_i \text{ are equal}
$$

</div>
</div>

## Variance Decomposition and Test Statistic {#variance-decomposition-and-test-statistic}

- ANOVA compares two variance estimates
	- variance between samples
	- variance within samples
- Mean square between samples
	- $MSB$
- Mean square within samples
	- $MSW$
- One way ANOVA test is right tailed

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="28.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 28.3</span> <span class="theorem-callout-subtitle">(One Way ANOVA Test Statistic)</span>.</div></div>
<div class="callout-content">

$$
F = \frac{MSB}{MSW}
$$

</div>
</div>

## Sums of Squares {#sums-of-squares}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="28.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 28.4</span> <span class="theorem-callout-subtitle">(Total Sum of Squares Decomposition)</span>.</div></div>
<div class="callout-content">

$$
SST = SSB + SSW
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="28.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 28.5</span> <span class="theorem-callout-subtitle">(Between and Within Sums of Squares)</span>.</div></div>
<div class="callout-content">

Between samples

$$
SSB = \left(\frac{T_1^2}{n_1} + \frac{T_2^2}{n_2} + \cdots + \frac{T_k^2}{n_k}\right) - \frac{T^2}{n}
$$

Within samples

$$
SSW = \left(\sum x_{1j}^2 - \frac{T_1^2}{n_1}\right) + \left(\sum x_{2j}^2 - \frac{T_2^2}{n_2}\right) + \cdots + \left(\sum x_{kj}^2 - \frac{T_k^2}{n_k}\right)
$$

</div>
</div>

## Mean Squares and Degrees of Freedom {#mean-squares-and-degrees-of-freedom}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="28.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 28.6</span> <span class="theorem-callout-subtitle">(Mean Squares)</span>.</div></div>
<div class="callout-content">

$$
MSB = \frac{SSB}{k-1}
$$

$$
MSW = \frac{SSW}{n-k}
$$

where
- $k-1$ is numerator degrees of freedom
- $n-k$ is denominator degrees of freedom

</div>
</div>

## ANOVA Table {#anova-table}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="28.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 28.7</span> <span class="theorem-callout-subtitle">(ANOVA Table)</span>.</div></div>
<div class="callout-content">

- Between
	- df $k-1$
	- sum of squares $SSB$
	- mean square $MSB$
- Within
	- df $n-k$
	- sum of squares $SSW$
	- mean square $MSW$
- Total
	- df $n-1$
	- sum of squares $SST$

</div>
</div>

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="28.8">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 28.8</span> <span class="theorem-callout-subtitle">(Reported Test Statistic)</span>.</div></div>
<div class="callout-content">

$$
F = \frac{MSB}{MSW}
$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 23–26</span>
