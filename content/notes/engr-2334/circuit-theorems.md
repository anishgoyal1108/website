---
author: "Anish Goyal"
title: "Circuit Theorems"
description: "Actual circuits are not ideal, and the voltage decreases as you add more load"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2334"
date: 2025-04-03T03:03:14
modified: 2025-04-03T07:03:08
readingtime: "1"
course: "ENGR 2334"
course_slug: "engr-2334"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 5
weight: 50
slug: "circuit-theorems"
links: []
sources:
  - "Course slides, chapter 5: Circuit Theorems"
generated: true
---

## Source Transformations {#source-transformations}
- Actual circuits are not ideal, and the voltage decreases as you add more load

### Examples {#examples}
<a class="zoom" href="/notes/img/source-transformations-example-1.png"><img src="/notes/img/source-transformations-example-1.png" alt="source transformations example 1" loading="lazy"></a>

<a class="zoom" href="/notes/img/polarity-changing-answer-example.png"><img src="/notes/img/polarity-changing-answer-example.png" alt="polarity changing answer example" loading="lazy"></a>

## Superposition {#superposition}
- The total response of a circuit is the sum of the responses of each independent source
- This can be done by shorting each voltage source or creating an open circuit for each current source

### Examples {#examples-1}
<a class="zoom" href="/notes/img/superposition-example.png"><img src="/notes/img/superposition-example.png" alt="superposition example" loading="lazy"></a>

## Thevenin's Theorem {#thevenin-s-theorem}
- Any part of a circuit can be represented as a Thevenin Equivalent
- If there is a dependent source, must find the equivalent voltage $V_{\text{oc}}$ using superposition/analysis

<a class="zoom" href="/notes/img/thevenin-theorem-equivalent-circuit.png"><img src="/notes/img/thevenin-theorem-equivalent-circuit.png" alt="thevenin theorem equivalent circuit" loading="lazy"></a>

### Examples {#examples-2}

<a class="zoom" href="/notes/img/thevenin-equivalent-circuit-dependent-source-example.png"><img src="/notes/img/thevenin-equivalent-circuit-dependent-source-example.png" alt="thevenin equivalent circuit dependent source example" loading="lazy"></a>

## Norton's Theorem {#norton-s-theorem}
- Any part of a circuit can be represented as a Norton Equivalent
- If there is a dependent source, must find the equivalent current $i_{\text{sc}}$ using superposition/analysis

<a class="zoom" href="/notes/img/norton-theorem-equivalent-circuit.png"><img src="/notes/img/norton-theorem-equivalent-circuit.png" alt="norton theorem equivalent circuit" loading="lazy"></a>

### Examples {#examples-3}

## Maximum Power Transfer Theorem {#maximum-power-transfer-theorem}
- Answers one of two questions:
	- Choose an $R_L$ to maximize $P$
	- Choose a circuit to provide max $P$ given $R_L$
- Expression for power

$$P = \left(\frac{V_{\text{oc}}}{R_{T}+R_{L}}\right)^2 R_{L}$$

- Taking the derivative of $P$ wrt $R_L$, we obtain that the max power is achieved when $R_T = R_L$

$$P_{\text{max}} = \frac{1}{4}\left(\frac{V_{\text{oc}}^2}{R_{T}}\right) = \frac{R_{T}i_{\text{sc}}^2}{4}$$

### Examples {#examples-4}
<a class="zoom" href="/notes/img/max-power-example-1.png"><img src="/notes/img/max-power-example-1.png" alt="max power example 1" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Course slides, chapter 5: Circuit Theorems</span>
