---
author: "Anish Goyal"
title: "Laplace Transform"
description: "Determined using the Laplace transform integral or laplace transform table"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-04-01T04:33:11
modified: 2025-04-01T06:11:01
readingtime: "2"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 18
weight: 180
slug: "laplace-transform"
links: []
sources:
  - "Laplace transform"
  - "Laplace transform table (course handout)"
generated: true
---

## Laplace Transform {#laplace-transform-1}
- Determined using the Laplace transform integral or <cite class="cite">laplace transform table <span class="cite-src">[Laplace transform table (course handout)]</span></cite>
- Most continuous functions have a Laplace transform

$$X(s)=\int_{-\infty}^{\infty}x(t)e^{-st} \ \mathrm{d}t$$

<a class="zoom" href="/notes/img/laplace-transform-evaluation-example.png"><img src="/notes/img/laplace-transform-evaluation-example.png" alt="laplace transform evaluation example" loading="lazy"></a>

## Inverse Laplace Transform {#inverse-laplace-transform}
- Usually not practical using the mathematical definition of ILT
- Must change the $s$-domain function so that it can be evaluated with a <cite class="cite">table <span class="cite-src">[Laplace transform table (course handout)]</span></cite>
	- Accomplished with partial fraction decomposition or clever manipulation

$$x(t) = \frac{2\pi}{j}\int_{\alpha-j\infty}^{\alpha+j\infty}X(s)e^{st} \ \mathrm{d}s$$

## Partial Fraction Decomposition {#partial-fraction-decomposition}
- Every proper rational function can be expressed as a sum of first-order rational functions

$$X(s)=\frac{B(s)}{A(s)}=\frac{b_{M}s^M+b_{M-1}s^{M-1}+\dots+b_{1}s^{1}+b_{0}}{a_{M}s^M+a_{M-1}s^{M-1}+\dots+a_{1}s^{1}+a_{0}}$$

- Each term in the sum is a residue, $r_k$, divided by $s$ minus a pole factor, $p_k$

$$X(s) = \sum_{k}^{N}\frac{r_{k}}{s-p_{k}}$$

### Partial Fraction Decomposition with MATLAB {#partial-fraction-decomposition-with-matlab}
- Useful functions for partial fraction decomposition: `residue`, `roots`, `poly`
<a class="zoom" href="/notes/img/partial-fraction-decomposition-with-matlab-example.png"><img src="/notes/img/partial-fraction-decomposition-with-matlab-example.png" alt="partial fraction decomposition with matlab example" loading="lazy"></a>

### Complex Pole Pair {#complex-pole-pair}
<a class="zoom" href="/notes/img/partial-fraction-decomposition-complex-pole-pair-example.png"><img src="/notes/img/partial-fraction-decomposition-complex-pole-pair-example.png" alt="partial fraction decomposition complex pole pair example" loading="lazy"></a>

## Shortcuts {#shortcuts}
- Commonly-encountered functions that are not directly shown in the table

### Laplace Transform {#laplace-transform-2}

#### Delayed Step {#delayed-step}
<a class="zoom" href="/notes/img/laplace-transform-delayed-step-shortcut.png"><img src="/notes/img/laplace-transform-delayed-step-shortcut.png" alt="laplace transform delayed step shortcut" loading="lazy"></a>

#### Right-sided Sum of Sines {#right-sided-sum-of-sines}
- Distribute $u(t)$ and evaluate each sine independently as a general sine
- The example shown below is pretty poor since it has a constant for the first term instead of a sinusoid
<a class="zoom" href="/notes/img/laplace-transform-right-sided-sum-of-sines-shortcut.png"><img src="/notes/img/laplace-transform-right-sided-sum-of-sines-shortcut.png" alt="laplace transform right-sided sum of sines shortcut" loading="lazy"></a>

#### Finite Duration Exponential {#finite-duration-exponential}
- Two methods: algebraic manipulation and use the table, or convolution in the $s$-domain (harder)
<a class="zoom" href="/notes/img/laplace-transform-finite-duration-exponential-shortcut.png"><img src="/notes/img/laplace-transform-finite-duration-exponential-shortcut.png" alt="laplace transform finite duration exponential shortcut" loading="lazy"></a>

### Inverse Laplace Transform {#inverse-laplace-transform-1}

#### Exponential with Linear Term in Denominator $\left(\frac{1}{s+a}\right)$ {#exponential-with-linear-term-in-denominator-1-s-a}
<a class="zoom" href="/notes/img/inverse-laplace-transform-exponential-with-linear-term-in-denominator-shortcut.png"><img src="/notes/img/inverse-laplace-transform-exponential-with-linear-term-in-denominator-shortcut.png" alt="inverse laplace transform exponential with linear term in denominator shortcut" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Laplace transform (course handout)</span>
