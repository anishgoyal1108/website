---
author: "Anish Goyal"
title: "Nominal Rates"
description: "When rates are paid more than once per period"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-10-06T23:39:51
modified: 2025-10-18T12:54:06
readingtime: "1"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 9
weight: 90
slug: "nominal-rates"
links: []
sources: []
generated: true
---

## Nominal Rates Intro {#nominal-rates-intro}
- When rates are paid more than once per period
- Compound is assumed
- **Interest conversion period:** Fractional portion of a larger period during which interest is paid
- Nominal rate of interest $i^{(m)}$ is payable/convertible/compounded $m$ times per period
	- $\frac{i^{(m)}}{m}$ is the effective interest rate during $m$
- When you say something is nominal annually, that doesn't really make sense; it's just the effective annual rate
- Nominal rates of interest don't make sense for simple interest/discount because $i = i^{(m)}$ and $d = d^{(m)}$
- Accumulation function after $m$ subdivisions:

$$a(t) = \left( 1 + \frac{i^{(m)}}{m}\right)^{mt}$$

- Effective interest rate for any year:

$$i = \left( 1 + \frac{i^{(m)}}{m}\right)^{m} - 1$$
