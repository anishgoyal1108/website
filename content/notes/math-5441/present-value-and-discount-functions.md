---
author: "Anish Goyal"
title: "Present Value and Discount Functions"
description: "Present value: what principal should I invest to obtain $X t years from now?"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-10-01T14:31:35
modified: 2025-10-06T23:04:49
readingtime: "1"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 7
weight: 70
slug: "present-value-and-discount-functions"
links: []
sources: []
generated: true
---

## The Idea of Present Value {#the-idea-of-present-value}
- Present value: *what principal should I invest to obtain $X t years from now?*
	- Effectively a way to travel back in time when starting with a future value

$$A_{0} = \frac{A(t)}{a(t)} = A(t)[a(t)]^{-1}$$

- The above equation is the generalized case, though we will almost always encounter compound interest, in which $a(t)$ has the form $(1 + i)^t$
	- Therefore, for compound interest: $A_0 = A(t)(1 + i)^{-t}$
	- $\nu=(1+i)^{-1}$ is known as the discount factor and it is the inverse of the accumulation factor
- A **discount function** relates the value needed to invest today to obtain a particular amount in the future; it is equal to $[a(t)]^{-1}=\frac{1}{(1+i)^t}=\nu^t$ (only for compound interest, though the concept is similar for simple interest)
- Discounting and accumulation are opposite processes
	- Discounting goes backwards in time from the final value to get the present value
	- Accumulation goes forward in time from the present value to get the final value
