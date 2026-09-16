---
author: "Anish Goyal"
title: "Perpetuities"
description: "An annuity-immediate whose term is infinite"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-10-26T14:25:29
modified: 2025-10-26T21:53:27
readingtime: "1"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 18
weight: 180
slug: "perpetuities"
links: []
sources: []
generated: true
---

## Perpetuity {#perpetuity}
- An annuity-immediate whose term is infinite

$$a_{\left< \infty \right> } = \lim_{ n \to \infty } a_{\left< n \right> } = \lim_{ n \to \infty } \frac{1 - (1 + i)^{-n}}{i} = \frac{1}{i}$$

- There is no such thing as finding the "future value" of a perpetuity at infinity, since the expression for the FV is divergent
	- Therefore, you can only find the present value
	- You can, however, still find the future value of the perpetuity at a noninfinite time 
- Annuity-due:

$$\ddot a_{\left< \infty \right> } = \lim_{ n \to \infty } \ddot a_{\left< n \right> } = (1+i) \lim_{ n \to \infty } \frac{1 - (1 + i)^{-n}}{i} = \frac{1+i}{i}=\frac{1}{d}$$

<a class="zoom" href="/notes/img/perpetuity-example-probelm.png"><img src="/notes/img/perpetuity-example-probelm.png" alt="Perpetuity example probelm" loading="lazy"></a>

<a class="zoom" href="/notes/img/perpetuity-second-example-problem.png"><img src="/notes/img/perpetuity-second-example-problem.png" alt="Perpetuity second example problem" loading="lazy"></a>
