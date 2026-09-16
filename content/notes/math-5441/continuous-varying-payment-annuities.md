---
author: "Anish Goyal"
title: "Continuous Varying-Payment Annuities"
description: "The payment is continuously-changing according to some function f(t)"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-11-01T18:37:53
modified: 2025-11-01T18:46:06
readingtime: "1"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 29
weight: 290
slug: "continuous-varying-payment-annuities"
links: []
sources: []
generated: true
---

## Concept {#concept}
- The payment is continuously-changing according to some function $f(t)$
- This also implies there is a continuous force of interest acting on the fund

## Solution {#solution}

### Present Value {#present-value}

$$\int_{0}^{n} f(t) e^{-\int_{0}^{t} \delta_{\tau} \, \mathrm{d}\tau} \, \mathrm{d}t$$

### Future Value {#future-value}

$$\int_{0}^{n} f(t) e^{\int_{t}^{n}\delta_{\tau}\,\mathrm{d}\tau}\,\mathrm{d}t$$
