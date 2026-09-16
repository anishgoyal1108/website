---
author: "Anish Goyal"
title: "Deferred Annuities"
description: "Asked to evaluate:"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-10-26T07:10:07
modified: 2025-10-26T08:11:47
readingtime: "2"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 17
weight: 170
slug: "deferred-annuities"
links: []
sources: []
generated: true
---

## Concept {#concept}
- Asked to evaluate:
	1. Present value before annuity's starting period
	2. Accumulated value after annuity's ending period
	3. Current value during an annuity
- We will break each of these into specific subcases

### Present Value Before First Payment {#present-value-before-first-payment}
- Assume there are $(m+1)$ periods before the first payment
- Also assume there are $n$ periods during the annuity (therefore $(m + n)$ periods total)
- We are asked to find the present value at $t=0$
	- This is equal to $\nu^m a_{\left< n \right>}$
	- In other words, it's the present value at the beginning of the annuity $(t=m)$ discounted by $m$ time periods
- Also valid to think of it as a subtraction of annuities; by the addition identity for annuities, we have:

$$\text{PV} = a_{\left< m + n \right>} - a_{\left< m \right>} = \nu^m a_{\left< n \right>}$$

<a class="zoom" href="/notes/img/timeline-present-value-before-first-payment.png"><img src="/notes/img/timeline-present-value-before-first-payment.png" alt="timeline present value before first payment" loading="lazy"></a>

### Accumulated Value After Last Payment {#accumulated-value-after-last-payment}
- It's the same concept; just accumulate the annuity, take the result, and accumulate it for $m$ periods

$$\text{FV} = s_{\left< m + n \right>} - s_{\left< m \right>} = (1+i)^m s_{\left< n \right>}$$

### Current Value During Annuity {#current-value-during-annuity}
- Suppose the annuity has a term of $n$ periods and we are varying $m$ within the term
- Then, the present value of the annuity at the $m$'th payment date (also known as the *current value*) is:

$$(1+i)^m a_{\left< n \right>} = \nu^{n-m} s_{\left< n \right>}$$

- Basically: you have to accumulate the present value and discount the future value of the annuity to $t=m$
- A relation with less entropy that is equivalent to the LHS and RHS of the above equation:
	- This basically means you can find the current value by taking the sum of: 
		1. The future value of the annuity at $t=m$
		2. The present value of the annuity at $t=n-m$ (the value you must subtract $n$ by to get $m$)

$$s_{\left< m \right>} + a_{\left< n - m \right>}$$
