---
author: "Anish Goyal"
title: "More on Cumulative Distribution Function"
description: "lecture18-20-3421.pdf"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-03-31T18:42:56
modified: 2026-03-31T18:43:48
readingtime: "1"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 15
weight: 150
slug: "more-on-cumulative-distribution-function"
links: []
sources:
  - "Course lecture slides 18–20"
generated: true
---

## CDF {#cdf}
  
<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="15.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 15.1</span> <span class="theorem-callout-subtitle">(Cumulative Distribution Function)</span>.</div></div>
<div class="callout-content">

The cumulative distribution function of random variable $X$ is  

$$  
F_X(x)=P[X\le x]  
$$  

</div>
</div>

  
<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="15.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 15.2</span> <span class="theorem-callout-subtitle">(CDF Boundary Values and Interval Probability)</span>.</div></div>
<div class="callout-content">

For any random variable $X$  

$$  
F_X(-\infty)=0  
$$  

$$  
F_X(\infty)=1  
$$  

For $x_1<x_2$  

$$  
P[x_1<X\le x_2]=F_X(x_2)-F_X(x_1)  
$$  

</div>
</div>

  
<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="15.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 15.3</span> <span class="theorem-callout-subtitle">(Continuous Random Variable)</span>.</div></div>
<div class="callout-content">

$X$ is a continuous random variable if the CDF $F_X(x)$ is a continuous function  

</div>
</div>

  
<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="15.4">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 15.4</span> <span class="theorem-callout-subtitle">(Upper Tail From CDF)</span>.</div></div>
<div class="callout-content">

For any real number $a$  

$$  
P[X>a]=1-F_X(a)  
$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 18–20</span>
