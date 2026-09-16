---
author: "Anish Goyal"
title: "Families of Continuous Random Variables"
description: "lecture18-20-3421.pdf"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-03-31T18:45:41
modified: 2026-03-31T18:46:09
readingtime: "2"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 18
weight: 180
slug: "families-of-continuous-random-variables"
links: []
sources:
  - "Course lecture slides 18–20"
generated: true
---

## Uniform $(a,b)$ {#uniform-a-b}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="18.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 18.1</span> <span class="theorem-callout-subtitle">(Uniform $(a,b)$ Random Variable)</span>.</div></div>
<div class="callout-content">

$X$ is a uniform $(a,b)$ random variable if the PDF of $X$ has the form

$$
f_X(x)=\begin{cases}
\dfrac{1}{b-a} & a\le x<b \\
0 & \text{otherwise}
\end{cases}
$$

where $b>a$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="18.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 18.2</span> <span class="theorem-callout-subtitle">(Uniform CDF Mean Variance)</span>.</div></div>
<div class="callout-content">

If $X$ is uniform $(a,b)$

$$
F_X(x)=\begin{cases}
0 & x\le a \\
\dfrac{x-a}{b-a} & a<x\le b \\
1 & x>b
\end{cases}
$$

$$
E[X]=\frac{a+b}{2}
$$

$$
\mathrm{Var}[X]=\frac{(b-a)^2}{12}
$$

</div>
</div>

## Exponential $(\lambda)$ {#exponential}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="18.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 18.3</span> <span class="theorem-callout-subtitle">(Exponential $(\lambda)$ Random Variable)</span>.</div></div>
<div class="callout-content">

$X$ is an exponential $(\lambda)$ random variable if the PDF of $X$ is

$$
f_X(x)=\begin{cases}
\lambda e^{-\lambda x} & x\ge 0 \\
0 & \text{otherwise}
\end{cases}
$$

where $\lambda>0$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="18.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 18.4</span> <span class="theorem-callout-subtitle">(Exponential CDF Mean Variance)</span>.</div></div>
<div class="callout-content">

If $X$ is exponential $(\lambda)$

$$
F_X(x)=\begin{cases}
1-e^{-\lambda x} & x\ge 0 \\
0 & \text{otherwise}
\end{cases}
$$

$$
E[X]=\frac{1}{\lambda}
$$

$$
\mathrm{Var}[X]=\frac{1}{\lambda^2}
$$

</div>
</div>

## Erlang $(n,\lambda)$ {#erlang-n}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="18.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 18.5</span> <span class="theorem-callout-subtitle">(Erlang $(n,\lambda)$ Random Variable)</span>.</div></div>
<div class="callout-content">

$X$ is an Erlang $(n,\lambda)$ random variable if the PDF of $X$ is

$$
f_X(x)=\begin{cases}
\dfrac{\lambda^n x^{n-1} e^{-\lambda x}}{(n-1)!} & x\ge 0 \\
0 & \text{otherwise}
\end{cases}
$$

where $\lambda>0$ and $n\ge 1$ is an integer

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="18.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 18.6</span> <span class="theorem-callout-subtitle">(Erlang Mean Variance)</span>.</div></div>
<div class="callout-content">

If $X$ is Erlang $(n,\lambda)$

$$
E[X]=\frac{n}{\lambda}
$$

$$
\mathrm{Var}[X]=\frac{n}{\lambda^2}
$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 18–20</span>
