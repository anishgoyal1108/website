---
author: "Anish Goyal"
title: "Continuous Time System Response"
description: "An operator that takes a kernel h(t) and a signal x(t) and accumulates the interactions between both"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-01-20T16:11:32
modified: 2025-01-21T17:01:52
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 5
weight: 50
slug: "continuous-time-system-response"
links: []
sources:
  - "Continuous-time system response"
generated: true
---

## Convolution {#convolution}
- An operator that takes a kernel $h(t)$ and a signal $x(t)$ and accumulates the interactions between both
	- For each $\tau$, the reflected kernel $h(-τ)$ is shifted by $t$ to become $h(t−τ)$. This shifted kernel is then multiplied with the signal $x(τ)$
	- Fancy multiplication; the kernel acts as a weight/filter that determines how much influence different parts of the signal have on the output
- Linear, distributive, associative, and commutative

$$
h(t) * x(t) = \int_{-\infty}^{\infty}h(\tau)x(t-\tau) \ \mathrm{d}\tau
$$

<a class="zoom" href="/notes/img/convolution-example.png"><img src="/notes/img/convolution-example.png" alt="convolution example" loading="lazy"></a>

## LTI System Responses {#lti-system-responses}
- If fed a weighted sum of impulses and the impulse response is known, the output is the corresponding weighted sum of response output

<a class="zoom" href="/notes/img/weighted-lti-response-example.png"><img src="/notes/img/weighted-lti-response-example.png" alt="weighted lti response example" loading="lazy"></a>

- If fed a weighted sum of functions and the response for each of those functions is known, the output is the corresponding weighted sum

<a class="zoom" href="/notes/img/weighted-lti-system-response-example-2.png"><img src="/notes/img/weighted-lti-system-response-example-2.png" alt="weighted lti system response example 2" loading="lazy"></a>

## Numerical Convolution {#numerical-convolution}
- Responses can be approximated when integral convolution is not practical
- MATLAB uses `conv` to approximate convolution integrals with midpoint method

$$
y(t) \approx \Delta \tau \sum_{k=0}^{n-1} h(\tau_{k})x(t-\tau_{k})
$$

### MATLAB Code {#matlab-code}
<a class="zoom" href="/notes/img/numerical-convolution-matlab-code.png"><img src="/notes/img/numerical-convolution-matlab-code.png" alt="numerical convolution matlab code" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Continuous-time system response (course handout)</span>
- https://betterexplained.com/articles/intuitive-convolution/
