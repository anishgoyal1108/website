---
author: "Anish Goyal"
title: "Estimation and Confidence Intervals"
description: "Estimation assigns numerical value or values to a population parameter based on sample information"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-04-21T16:15:22
modified: 2026-04-21T16:15:51
readingtime: "2"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 25
weight: 250
slug: "estimation-and-confidence-intervals"
links: []
sources:
  - "Course lecture slides 23–26"
generated: true
---

## Estimation {#estimation}

- Estimation assigns numerical value or values to a population parameter based on sample information

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="25.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 25.1</span> <span class="theorem-callout-subtitle">(Estimation)</span>.</div></div>
<div class="callout-content">

The assignment of value or values to a population parameter based on a value of the corresponding sample statistic is called estimation

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="25.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 25.2</span> <span class="theorem-callout-subtitle">(Estimate and Estimator)</span>.</div></div>
<div class="callout-content">

The value assigned to a population parameter based on a sample statistic is called an estimate
The sample statistic used to estimate a population parameter is called an estimator

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="25.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 25.3</span> <span class="theorem-callout-subtitle">(Point Estimate)</span>.</div></div>
<div class="callout-content">

The value of a sample statistic used to estimate a population parameter is called a point estimate

</div>
</div>

## Interval Estimation and Confidence Level {#interval-estimation-and-confidence-level}

- Interval estimation builds an interval around a point estimate
- Margin of error is the amount added and subtracted from the point estimate

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="25.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 25.4</span> <span class="theorem-callout-subtitle">(Confidence Level and Confidence Interval)</span>.</div></div>
<div class="callout-content">

Each interval is constructed with regard to a given confidence level and is called a confidence interval
The confidence interval is

$$
\text{point estimate} \pm \text{margin of error}
$$

Confidence level is denoted by $(1-\alpha)100\%$
The significance level is $\alpha$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="25.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 25.5</span> <span class="theorem-callout-subtitle">(Margin of Error)</span>.</div></div>
<div class="callout-content">

The margin of error for the estimate of $\mu$ is denoted by $E$

$$
E = z\,\sigma_{\bar x}
$$

</div>
</div>

## Confidence Interval for $\mu$ with $\sigma$ Known {#confidence-interval-for-with-known}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="25.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 25.6</span> <span class="theorem-callout-subtitle">(Confidence Interval for $\mu$)</span>.</div></div>
<div class="callout-content">

The $(1-\alpha)100\%$ confidence interval for $\mu$ under the normal model is

$$
\bar x \pm z\,\sigma_{\bar x}
$$

where

$$
\sigma_{\bar x} = \frac{\sigma}{\sqrt n}
$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 23–26</span>
