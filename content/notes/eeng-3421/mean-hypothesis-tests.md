---
author: "Anish Goyal"
title: "Mean Hypothesis Tests"
description: "A hypothesis test evaluates a claim about a population parameter using sample information"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-04-21T16:16:06
modified: 2026-04-21T16:16:51
readingtime: "2"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 26
weight: 260
slug: "mean-hypothesis-tests"
links: []
sources:
  - "Course lecture slides 23–26"
generated: true
---

## Core Setup {#core-setup}

- A hypothesis test evaluates a claim about a population parameter using sample information

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="26.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 26.1</span> <span class="theorem-callout-subtitle">(Null and Alternative Hypotheses)</span>.</div></div>
<div class="callout-content">

Null hypothesis $H_0$ is the default claim to be tested
Alternative hypothesis $H_1$ is the competing claim

</div>
</div>

- Test types
	- right tailed
	- left tailed
	- two tailed
- Significance level $\alpha$
	- probability threshold used for deciding rejection

## Two Common Approaches {#two-common-approaches}

- p value approach
- critical value approach

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="26.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 26.2</span> <span class="theorem-callout-subtitle">(p Value)</span>.</div></div>
<div class="callout-content">

The p value is the probability under $H_0$ of observing a sample statistic at least as extreme as the observed value

</div>
</div>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="26.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 26.3</span> <span class="theorem-callout-subtitle">(p Value for One Tailed Tests)</span>.</div></div>
<div class="callout-content">

For a one tailed test, the p value is the area in the relevant tail beyond the observed value of the sample statistic

</div>
</div>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="26.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 26.4</span> <span class="theorem-callout-subtitle">(p Value for Two Tailed Tests)</span>.</div></div>
<div class="callout-content">

For a two tailed test, the p value is twice the tail area beyond the observed value of the sample statistic

</div>
</div>

## Decision Rule Using P Value {#decision-rule-using-p-value}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="26.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 26.5</span> <span class="theorem-callout-subtitle">(Decision Rule)</span>.</div></div>
<div class="callout-content">

Reject $H_0$ if

$$
\text{p value} \le \alpha
$$

Do not reject $H_0$ if

$$
\text{p value} > \alpha
$$

</div>
</div>

## Procedure Skeleton {#procedure-skeleton}

- State $H_0$ and $H_1$
- Select the distribution to use for the test statistic under $H_0$
- Determine rejection and nonrejection regions or compute p value
- Compute test statistic from sample
- Decide reject or fail to reject

## References {#references}
- <span class="cite cite-ref">Course lecture slides 23–26</span>
