---
author: "Anish Goyal"
title: "Transfer Functions"
description: "The ratio of the Laplace transform of the system output to the Laplace transform of the system input"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-04-01T05:12:50
modified: 2025-04-01T05:24:55
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 19
weight: 190
slug: "transfer-functions"
links:
  - "/notes/engr-2341/laplace-transform/"
sources:
  - "Transfer functions"
generated: true
---

## Transfer (System) Functions {#transfer-system-functions}
- The ratio of the <a class="internal-link" href="/notes/engr-2341/laplace-transform/">Laplace transform</a> of the system output to the Laplace transform of the system input

$$H(s) = \frac{Y(s)}{X(s)}$$

- Can also be determined by taking the Laplace transform of the impulse response or from differential equations describing the system

$$H(s) = \int_{-\infty}^{\infty}h(t)e^{-st} \ \mathrm{d}t$$

## Poles and Zeros {#poles-and-zeros}
- Roots of $Y(s)$ are the system zeros
- Roots of $X(s)$ are the system poles ($\mathcal{P}$)

$$\forall p \in \mathcal{P}, \Re(p) < 0 \implies \int_{-\infty}^{\infty} |h(t)| \, dt < \infty \implies \text{BIBO stability}$$

<a class="zoom" href="/notes/img/poles-and-bibo-stability-example.png"><img src="/notes/img/poles-and-bibo-stability-example.png" alt="poles and bibo stability example" loading="lazy"></a>
<a class="zoom" href="/notes/img/transfer-functions-example.png"><img src="/notes/img/transfer-functions-example.png" alt="transfer functions example" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Transfer functions (course handout)</span>
