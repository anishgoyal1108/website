---
author: "Anish Goyal"
title: "Continuous Annuities"
description: "Annuities that accrue interest compounded continuously for recurring payments (using the force of interest, )"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-11-01T17:33:02
modified: 2025-11-01T18:44:20
readingtime: "1"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 25
weight: 250
slug: "continuous-annuities"
links: []
sources: []
generated: true
---

## Concept {#concept}
- Annuities that accrue interest compounded continuously for recurring payments (using the force of interest, $\delta$)
- Notation: $\bar{a}_{\left< n \right>}$ or $\bar{s}_{\left< n \right>}$

## Solution {#solution}

### Constant Force of Interest {#constant-force-of-interest}
- Since $\delta$ is constant, then $i = e^{\delta} - 1$

$$\bar{a}_{\left< n \right>} = \frac{1 - e^{-\delta n}}{\delta}$$

$$\bar{s}_{\left< n \right>} = \frac{e^{\delta n} - 1}{\delta}$$

### Varying Force of Interest {#varying-force-of-interest}

$$\bar a_{\langle n\rangle}=\int_{0}^{n}e^{-\int_{0}^{t}\delta_{\tau}\,\mathrm{d}\tau} \, \mathrm{d}t$$

$$\bar s_{\langle n\rangle}=\int_{0}^{n} e^{\int_{t}^{n}\delta_{\tau}\,\mathrm{d}\tau}\,\mathrm{d}t$$
