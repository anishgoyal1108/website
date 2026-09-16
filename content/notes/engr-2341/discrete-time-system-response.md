---
author: "Anish Goyal"
title: "Discrete Time System Response"
description: "Exact same properties as integral convolution for continuous-time systems"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-01-21T17:38:24
modified: 2025-01-21T18:12:23
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 6
weight: 60
slug: "discrete-time-system-response"
links: []
sources:
  - "Discrete-time system response"
generated: true
---

## Discrete-time Convolution {#discrete-time-convolution}
- Exact same properties as integral convolution for continuous-time systems

$$y[n] = h[n] * x[n] = \sum_{k=-\infty}^\infty h[k] \cdot x[n-k]$$

## System Response {#system-response}
- Just like in continuous-time systems, you can use the properties of LTI systems to determine the output if the responses for the inputs are known

## FIR and IIR System Response {#fir-and-iir-system-response}
- The difference equation is more straightforward to evaluate than convolution sum for IIRs
	- Sum the products of the filter coefficients and the corresponding input/output samples
- Causal FIR (this is practically the same as convolution sum)

$$y[n] = \sum_{k=0}^M b_{k}x[n-k]$$

<a class="zoom" href="/notes/img/fir-system-response-example.png"><img src="/notes/img/fir-system-response-example.png" alt="fir system response example" loading="lazy"></a>
<a class="zoom" href="/notes/img/fir-system-response-numeric-example.png"><img src="/notes/img/fir-system-response-numeric-example.png" alt="fir system response numeric example" loading="lazy"></a>

- Causal IIR

$$y[n] = \sum_{\ell=1}^M a_{\ell}y[n-\ell]+\sum_{k=0}^M b_{k}x[n-k]$$

<a class="zoom" href="/notes/img/iir-system-response-example.png"><img src="/notes/img/iir-system-response-example.png" alt="iir system response example" loading="lazy"></a>
<a class="zoom" href="/notes/img/iir-system-response-numeric-example.png"><img src="/notes/img/iir-system-response-numeric-example.png" alt="iir system response numeric example" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Discrete-time system response (course handout)</span>
