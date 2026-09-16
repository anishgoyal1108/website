---
author: "Anish Goyal"
title: "Sampling Distributions and Estimation"
description: "Sample statistics are numerical summary measures computed from sample data"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-04-21T16:14:25
modified: 2026-04-21T16:15:15
readingtime: "4"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 24
weight: 240
slug: "sampling-distributions-and-estimation"
links: []
sources:
  - "Course lecture slides 23–26"
generated: true
---

## Sample Statistic and Population Parameter {#sample-statistic-and-population-parameter}

- Sample statistics are numerical summary measures computed from sample data
- Population parameters are the corresponding measures computed from the full population
- Population parameters are constants at a given time
- Sample statistics vary from sample to sample
- Sample statistics are random variables
- Sampling distribution is the probability distribution of a sample statistic

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="24.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 24.1</span> <span class="theorem-callout-subtitle">(Sample Statistic)</span>.</div></div>
<div class="callout-content">

A sample statistic is a numerical summary measure calculated for sample data

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="24.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 24.2</span> <span class="theorem-callout-subtitle">(Population Parameter)</span>.</div></div>
<div class="callout-content">

A population parameter is the corresponding numerical summary measure calculated for population data

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="24.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 24.3</span> <span class="theorem-callout-subtitle">(Sampling Distribution)</span>.</div></div>
<div class="callout-content">

The probability distribution of a sample statistic is called its sampling distribution

</div>
</div>

## Population Distribution {#population-distribution}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="24.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 24.4</span> <span class="theorem-callout-subtitle">(Population Distribution)</span>.</div></div>
<div class="callout-content">

The population distribution is the probability distribution of the population data

</div>
</div>

## Sampling Error and Nonsampling Error {#sampling-error-and-nonsampling-error}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="24.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 24.5</span> <span class="theorem-callout-subtitle">(Sampling Error)</span>.</div></div>
<div class="callout-content">

Sampling error is the difference between the value of a sample statistic and the value of the corresponding population parameter
For the mean

$$
\text{sampling error} = \bar x - \mu
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="24.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 24.6</span> <span class="theorem-callout-subtitle">(Nonsampling Errors)</span>.</div></div>
<div class="callout-content">

Errors that occur in the collection recording and tabulation of data are called nonsampling errors

</div>
</div>

## Mean and Standard Deviation of the Sampling Distribution of $\bar x$ {#mean-and-standard-deviation-of-the-sampling-distribution-of-x}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="24.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 24.7</span> <span class="theorem-callout-subtitle">(Mean and Standard Deviation of $\bar x$)</span>.</div></div>
<div class="callout-content">

The mean and standard deviation of the sampling distribution of $\bar x$ are denoted by $\mu_{\bar x}$ and $\sigma_{\bar x}$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="24.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 24.8</span> <span class="theorem-callout-subtitle">(Mean of the Sampling Distribution of $\bar x$)</span>.</div></div>
<div class="callout-content">

$$
\mu_{\bar x} = \mu
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="24.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 24.9</span> <span class="theorem-callout-subtitle">(Unbiased Estimator)</span>.</div></div>
<div class="callout-content">

A sample statistic is an unbiased estimator of a population parameter if its expected value equals the parameter
$\bar x$ is an unbiased estimator of $\mu$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="24.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 24.10</span> <span class="theorem-callout-subtitle">(Standard Deviation of the Sampling Distribution of $\bar x$)</span>.</div></div>
<div class="callout-content">

$$
\sigma_{\bar x} = \frac{\sigma}{\sqrt n}
$$

used when $n/N \le 0.05$

</div>
</div>

## Shape of the Sampling Distribution of $\bar x$ {#shape-of-the-sampling-distribution-of-x}

- Case population is normal
	- sampling distribution of $\bar x$ is normal for any $n$
- Case population not normal
	- use central limit theorem for large $n$

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="24.11">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 24.11</span> <span class="theorem-callout-subtitle">(Sampling Distribution When Population is Normal)</span>.</div></div>
<div class="callout-content">

If the population is normal with mean $\mu$ and standard deviation $\sigma$
then $\bar x$ is normal with

$$
\mu_{\bar x} = \mu
$$

$$
\sigma_{\bar x} = \frac{\sigma}{\sqrt n}
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="24.12">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 24.12</span> <span class="theorem-callout-subtitle">(Central Limit Theorem)</span>.</div></div>
<div class="callout-content">

For a large sample size, the sampling distribution of $\bar x$ is approximately normal irrespective of the population shape

$$
\mu_{\bar x} = \mu
$$

$$
\sigma_{\bar x} = \frac{\sigma}{\sqrt n}
$$

sample size usually considered large when $n \ge 30$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 23–26</span>
