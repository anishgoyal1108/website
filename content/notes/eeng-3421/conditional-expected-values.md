---
author: "Anish Goyal"
title: "Conditional Expected Values"
description: "lecture21-3421.pdf"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-04-21T16:11:31
modified: 2026-04-21T16:12:14
readingtime: "2"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 21
weight: 210
slug: "conditional-expected-values"
links: []
sources:
  - "Course lecture slides 21"
generated: true
---

## Conditional Probability of Sets Under a Conditional PMF/PDF {#conditional-probability-of-sets-under-a-conditional-pmf-pdf}
  
<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="21.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 21.1</span> <span class="theorem-callout-subtitle">(Properties of Conditional PMF and Conditional PDF)</span>.</div></div>
<div class="callout-content">

Discrete  
- $P_{X\mid B}(x) \ge 0$ for $x \in B$  
- $\sum_{x \in B} P_{X\mid B}(x) = 1$  
- for any set $C$  

$$  
P[C \mid B] = \sum_{x \in C} P_{X\mid B}(x)  
$$  

 
Continuous  
- $f_{X\mid B}(x) \ge 0$ for $x \in B$  
- $\int_{B} f_{X\mid B}(x)\,dx = 1$  
- for any set $C$  

$$  
P[C \mid B] = \int_{C} f_{X\mid B}(x)\,dx  
$$  

</div>
</div>

  
## Conditional Expected Value {#conditional-expected-value}
  
<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="21.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 21.2</span> <span class="theorem-callout-subtitle">(Conditional Expected Value)</span>.</div></div>
<div class="callout-content">

The conditional expected value of random variable $X$ given condition $B$ is  
 
Discrete  

$$  
E[X \mid B] = \sum_{x \in B} x\,P_{X\mid B}(x)  
$$  

 
Continuous  

$$  
E[X \mid B] = \int_{-\infty}^{\infty} x\,f_{X\mid B}(x)\,dx  
$$  

</div>
</div>

  
## Total Expectation with a Partition {#total-expectation-with-a-partition}
  
<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="21.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 21.3</span> <span class="theorem-callout-subtitle">(Total Expectation over a Partition)</span>.</div></div>
<div class="callout-content">

For a random variable $X$ resulting from an experiment with partition $B_1,\dots,B_m$  

$$  
E[X] = \sum_{i=1}^{m} E[X \mid B_i]\,P[B_i]  
$$  

</div>
</div>

  
## Conditional Expectation of a Function {#conditional-expectation-of-a-function}
  
<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="21.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 21.4</span> <span class="theorem-callout-subtitle">(Conditional Expected Value of a Function)</span>.</div></div>
<div class="callout-content">

The conditional expected value of $Y=g(X)$ given condition $B$ is  
 
Discrete  

$$  
E[Y \mid B] = E[g(X)\mid B] = \sum_{x \in B} g(x)\,P_{X\mid B}(x)  
$$  

 
Continuous  

$$  
E[Y \mid B] = E[g(X)\mid B] = \int_{-\infty}^{\infty} g(x)\,f_{X\mid B}(x)\,dx  
$$  

</div>
</div>

  
## Conditional Variance and Standard Deviation {#conditional-variance-and-standard-deviation}
  
<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="21.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 21.5</span> <span class="theorem-callout-subtitle">(Conditional Variance and Standard Deviation)</span>.</div></div>
<div class="callout-content">

The conditional variance of $X$ given event $B$ is  

$$  
\mathrm{Var}[X \mid B] = E[(X-\mu_{X\mid B})^2 \mid B] = E[X^2 \mid B] - \mu_{X\mid B}^2  
$$  

The conditional standard deviation is  

$$  
\sigma_{X\mid B} = \sqrt{\mathrm{Var}[X \mid B]}  
$$  

</div>
</div>

  
## References {#references}
- <span class="cite cite-ref">Course lecture slides 21</span>
