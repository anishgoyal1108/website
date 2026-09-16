---
author: "Anish Goyal"
title: "Discrete-time Transfer Functions"
description: "The ratio of the z-transform of the output to the z-transform of the input with initial conditions at zero, denoted b]y H(z)"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-04-17T21:33:53
modified: 2025-04-17T21:46:18
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 22
weight: 220
slug: "discrete-time-transfer-functions"
links: []
sources:
  - "Transfer functions"
generated: true
---

## Transfer Functions {#transfer-functions}
- The ratio of the $z$-transform of the output to the $z$-transform of the input with initial conditions at zero, denoted b]y $H(z)$
- Can also be determined by taking the $z$-transform of the impulse response or difference equation

## Zeros and Poles {#zeros-and-poles}
- Roots of the numerator of $H(z)$ are the zeros
- Roots of the denominator of $H(z)$ are the poles

<a class="zoom" href="/notes/img/z-transform-system-zeros-and-poles.png"><img src="/notes/img/z-transform-system-zeros-and-poles.png" alt="z-transform system zeros and poles" loading="lazy"></a>

## BIBO Stability {#bibo-stability}
- A system is BIBO stable if its impulse response is absolutely summable
- If all system poles have a magnitude less than one, the system is BIBO stable and has an absolutely summable impulse response

## References {#references}
- <span class="cite cite-ref">Transfer functions (course handout)</span>
