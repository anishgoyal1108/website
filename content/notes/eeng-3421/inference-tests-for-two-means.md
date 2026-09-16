---
author: "Anish Goyal"
title: "Inference Tests for Two Means"
description: "Population 1 parameters"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-04-21T16:18:00
modified: 2026-04-21T16:18:51
readingtime: "1"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 27
weight: 270
slug: "inference-tests-for-two-means"
links: []
sources:
  - "Course lecture slides 23–26"
generated: true
---

## Independent Vs Dependent Samples {#independent-vs-dependent-samples}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="27.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 27.1</span> <span class="theorem-callout-subtitle">(Independent Versus Dependent Samples)</span>.</div></div>
<div class="callout-content">

Two samples drawn from two populations are independent if the selection of one sample does not affect the selection of the second sample. Otherwise, the samples are dependent

</div>
</div>

## Setup and Notation {#setup-and-notation}

- Population 1 parameters
	- $\mu_1$ mean
	- $\sigma_1$ standard deviation
	- $n_1$ sample size
	- $\bar x_1$ sample mean
- Population 2 parameters
	- $\mu_2$ mean
	- $\sigma_2$ standard deviation
	- $n_2$ sample size
	- $\bar x_2$ sample mean

## Sampling Distribution of $\bar x_1 - \bar x_2$ {#sampling-distribution-of-x-1-x-2}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="27.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 27.2</span> <span class="theorem-callout-subtitle">(Sampling Distribution of $\bar x_1 - \bar x_2$)</span>.</div></div>
<div class="callout-content">

If
- samples are independent
- $\sigma_1,\sigma_2$ are known
- samples are large or populations are normal
then $\bar x_1 - \bar x_2$ is approximately normal with

$$
\mu_{\bar x_1-\bar x_2} = \mu_1 - \mu_2
$$

$$
\sigma_{\bar x_1-\bar x_2} = \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}
$$

</div>
</div>

## Confidence Interval for $\mu_1 - \mu_2$ {#confidence-interval-for-1-2}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="27.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 27.3</span> <span class="theorem-callout-subtitle">(Confidence Interval for $\mu_1 - \mu_2$)</span>.</div></div>
<div class="callout-content">

Using the normal model, the $(1-\alpha)100\%$ confidence interval for $\mu_1-\mu_2$ is

$$
(\bar x_1 - \bar x_2) \pm z\,\sigma_{\bar x_1-\bar x_2}
$$

where

$$
\sigma_{\bar x_1-\bar x_2} = \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}
$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 23–26</span>
