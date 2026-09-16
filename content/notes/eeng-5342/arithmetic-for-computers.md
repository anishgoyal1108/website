---
author: "Anish Goyal"
title: "Arithmetic for Computers"
description: "Initial values:"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-5342"
date: 2025-10-08T20:04:33
modified: 2025-11-28T14:39:12
readingtime: "1"
course: "EENG 5342"
course_slug: "eeng-5342"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 3
weight: 30
slug: "arithmetic-for-computers"
links: []
sources:
  - "Course slides, chapter 3"
generated: true
---

## Binary Multiplication {#binary-multiplication}
- Initial values:
	- Multiplicand ($n$): given with LHS 0’s
	- Multiplier ($n$): given with RHS 0’s
	- Product ($2n$): 0
- Multiplier LSB dictates whether the multiplicand is added to product
- End after $n$ steps

<a class="zoom" href="/notes/img/binary-multiplication-example.png"><img src="/notes/img/binary-multiplication-example.png" alt="binary multiplication example" loading="lazy"></a>
<a class="zoom" href="/notes/img/binary-multiplication-algorithm.png"><img src="/notes/img/binary-multiplication-algorithm.png" alt="binary multiplication algorithm" loading="lazy"></a>

## Binary Division {#binary-division}
- Initial values:
	- Quotient ($n$): 0
	- Divisor ($n$): given with RHS 0’s
	- Remainder ($2n$): dividend
- $R-D$ determines the LSB of $Q$ with each step
- End after $n+1$ steps

<a class="zoom" href="/notes/img/binary-division-example.png"><img src="/notes/img/binary-division-example.png" alt="binary division example" loading="lazy"></a>
<a class="zoom" href="/notes/img/binary-division-algorithm.png"><img src="/notes/img/binary-division-algorithm.png" alt="binary division algorithm" loading="lazy"></a>

## IEEE 754 Standard {#ieee-754-standard}
- Sign bit
- Significand:
	- (1 + Mantissa)
	- Mantissa is unsigned 24/53-bit *fractional* value
- Exponent: 
	- (Power - Bias)
	- Power is unsigned 8/11-bit
	- Bias is fixed at 127/1023
		- Introduced so that floats could be sorted without any ambiguity with respect to the 2’s complement representation of the Power

$$(-1)^S \cdot (1 + M) \cdot 2^{P - B}$$

- Steps for problem solving:
	- Convert the base-10 representation to binary fractional representation
	- Convert to normalized form
	- Figure out mantissa and power

### Special Cases {#special-cases}
- Special cases for which the exponents zero and all ones are reserved
- If $M$ and $P$ zero, the number is zero
- If $M=0$ and $P=11111\dots$, the number is $\pm \infty$
- If $M \ne 0$ and $P=1111\dots$, the number is $\text{NaN}$

## References {#references}
- <span class="cite cite-ref">Course slides, chapter 3</span>
