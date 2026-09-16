---
author: "Anish Goyal"
title: "Annuities Intro"
description: "Fixed payments at specific time intervals"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-10-25T06:49:21
modified: 2025-10-26T07:47:19
readingtime: "1"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 14
weight: 140
slug: "annuities-intro"
links: []
sources: []
generated: true
---

## Annuity {#annuity}
- Fixed payments at specific time intervals
- Objective is to find the present value of the $n$’th payment

## Geometric Series {#geometric-series}
- The $n$’th partial sum is

$$S_{n} = a \frac{1-r^{n+1}}{1-r}$$

## Annuity Into Geometric Series {#annuity-into-geometric-series}
- $a = P(1-i)^{-1}$
- $r = (1-i)^{-1}$
- The formula becomes:

$$
\begin{align}
\text{PV}_{n} &= P(1+i)^{-1} \frac{1-((1+i)^{-1})^{(n-1)+1}}{1-(1+i)^{-1}} \\
&= P \frac{1-(1+i)^{-n}}{i} 
\end{align}
$$

- The shorthand notation for the present value of an annuity with 1 dollar invested for $n$ time periods at an interest $i$ is $a_{\langle n \rangle}$ 

## Accumulated Value of Annuity {#accumulated-value-of-annuity}
- Denoted $s_{\langle n \rangle}$
- Just accumulating the present value over $n$ payment periods (multiplying by $(1+i)^n$)

$$s_{\langle n \rangle} = \frac{(1+i)^n - 1}{i}$$

## Sum and Difference Identities {#sum-and-difference-identities}

$$
\begin{aligned}
a_{\langle m+n \rangle} &= a_{\langle m \rangle} + \nu^{m} a_{\langle n \rangle} \\
a_{\langle m-n \rangle} &= a_{\langle m \rangle} - \nu^{m-n} a_{\langle n \rangle} \\
s_{\langle m+n \rangle} &= s_{\langle m \rangle} + (1+i)^{m} s_{\langle n \rangle} \\
s_{\langle m-n \rangle} &= s_{\langle m \rangle} - (1+i)^{m-n} s_{\langle n \rangle}
\end{aligned}
$$
