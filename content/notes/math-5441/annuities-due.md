---
author: "Anish Goyal"
title: "Annuities Due"
description: "Payments are made at the beginning of each payment period"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-10-25T20:15:30
modified: 2025-10-25T21:16:49
readingtime: "1"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 16
weight: 160
slug: "annuities-due"
links: []
sources: []
generated: true
---

## Annuity-Due {#annuity-due}
- Payments are made at the beginning of each payment period
- Notation: two dots above
	- $\ddot a_{\langle n \rangle}$
	- $\ddot s_{\langle n \rangle}$
- The overall principle remains the same, but everything is shifted by one to the left, since the initial payment is received immediately at $t=0$ (not to be confused with annuity-immediate!)
	- If you accumulate the annuity-immediate by one, you get the annuity-due!

$$\begin{align}
\ddot a_{\langle n \rangle} = (1+i)a_{\left< n \right> } &= \frac{a_{\left< n \right> }}{\nu}  \\
&= \frac{1-\nu^n}{d} \\
&= \frac{1-(1-d)^n}{d}
\end{align}$$

- The same goes for the accumulated value for annuities:

$$\ddot s_{\langle n \rangle} = (1+i)^n \ddot a_{\langle n \rangle} = (1+i) s_{\langle n \rangle}$$
