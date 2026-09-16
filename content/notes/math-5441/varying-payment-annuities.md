---
author: "Anish Goyal"
title: "Varying-Payment Annuities"
description: "Compute the present and future values of annuities with varying payment amounts"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-11-01T18:11:44
modified: 2025-11-01T18:36:29
readingtime: "1"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 26
weight: 260
slug: "varying-payment-annuities"
links: []
sources: []
generated: true
---

## Concept {#concept}
- Compute the present and future values of annuities with varying payment amounts

## Solution {#solution}

### Arithmetic Progression {#arithmetic-progression}
- Payment installments increase by a fixed amount $Q$

$$\text{PV} = Pa_{\left< n \right> } + Q\left( \frac{a_{\left< n \right>} - n(1+i)^{-n}}{i} \right)$$

$$\text{FV} = Ps_{\left< n \right> } + Q \left( \frac{s_{\left< n \right> } - n}{i} \right)$$

- In perpetuity:

$$\text{PV}_{\infty} = \frac{P}{i} + \frac{Q}{i^2}$$

### Geometric Progression {#geometric-progression}
- Payment installments increase by $k$%

$$\text{PV} = \begin{cases}
P\left( \frac{1- \left( \frac{1 + k}{1 + i} \right)^n }{i-k} \right), \ i \ne k \\
\frac{Pn}{1+i}, \ i = k
\end{cases}$$

$$
\text{FV} = \begin{cases}
P\,\dfrac{(1+i)^n - (1+k)^n}{\,i - k\,}, & i \ne k,\\[6pt]
Pn(1+i)^{n-1}, & i = k.
\end{cases}
$$

- In perpetuity (valid iff $i \gt k$):

$$\text{PV}_{\infty} = \frac{P}{i-k}$$

### Annuity-Due {#annuity-due}
- If it's annuity-due, just multiply by $(i+1)$
