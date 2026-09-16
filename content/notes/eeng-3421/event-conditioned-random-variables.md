---
author: "Anish Goyal"
title: "Event-Conditioned Random Variables"
description: "Condition on an event B with P[B] > 0"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-04-21T16:10:21
modified: 2026-04-21T16:11:22
readingtime: "1"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 20
weight: 200
slug: "event-conditioned-random-variables"
links: []
sources:
  - "Course lecture slides 21"
generated: true
---

## Conditional Distribution Given an Event {#conditional-distribution-given-an-event}
- Condition on an event $B$ with $P[B] > 0$  
- Conditioning restricts the underlying sample space to outcomes in $B$  
  
<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="20.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 20.1</span> <span class="theorem-callout-subtitle">(Conditional CDF)</span>.</div></div>
<div class="callout-content">

Given event $B$ with $P[B] > 0$, the conditional cumulative distribution function of $X$ is  

$$  
F_{X\mid B}(x) = P[X \le x \mid B]  
$$  

</div>
</div>

  
<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="20.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 20.2</span> <span class="theorem-callout-subtitle">(Conditional PMF)</span>.</div></div>
<div class="callout-content">

Given event $B$ with $P[B] > 0$, the conditional probability mass function of $X$ is  

$$  
P_{X\mid B}(x) = P[X = x \mid B]  
$$  

</div>
</div>

  
<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="20.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 20.3</span> <span class="theorem-callout-subtitle">(Conditional PDF)</span>.</div></div>
<div class="callout-content">

For a random variable $X$ and an event $B$ with $P[B] > 0$, the conditional PDF of $X$ given $B$ is  

$$  
f_{X\mid B}(x) = \frac{dF_{X\mid B}(x)}{dx}  
$$  

</div>
</div>

  
<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="20.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 20.4</span> <span class="theorem-callout-subtitle">(Conditional PMF and Conditional PDF from Unconditional)</span>.</div></div>
<div class="callout-content">

For a random variable $X$ and an event $B \subset S_X$ with $P[B] > 0$  
 
Discrete  

$$  
P_{X\mid B}(x) =  
\begin{cases}  
\dfrac{P_X(x)}{P[B]} & x \in B \\  
0 & \text{otherwise}  
\end{cases}  
$$  

 
Continuous  

$$  
f_{X\mid B}(x) =  
\begin{cases}  
\dfrac{f_X(x)}{P[B]} & x \in B \\  
0 & \text{otherwise}  
\end{cases}  
$$  

</div>
</div>

  
## References {#references}
- <span class="cite cite-ref">Course lecture slides 21</span>
