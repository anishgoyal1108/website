---
author: "Anish Goyal"
title: "Laplace System Response"
description: "Similar to 12 Fourier System Response, multiplication in the s-domain is convolution in the time domain"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-04-01T05:25:05
modified: 2025-04-01T05:26:29
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 20
weight: 200
slug: "laplace-system-response"
links:
  - "/notes/engr-2341/fourier-system-response/"
sources:
  - "System response"
generated: true
---

## System Response Using Laplace Transform {#system-response-using-laplace-transform}
- Similar to <a class="internal-link" href="/notes/engr-2341/fourier-system-response/">Fourier System Response</a>, multiplication in the $s$-domain is convolution in the time domain
- Take the product of the transfer function and the input in the $s$-domain, then take the inverse laplace transform

$$y(t) = \mathcal{L}^{-1} \left[ H(s) \cdot X(s) \right]$$

<a class="zoom" href="/notes/img/system-response-with-laplace-transform-example.png"><img src="/notes/img/system-response-with-laplace-transform-example.png" alt="system response with laplace transform example" loading="lazy"></a>

### Using LTI Properties {#using-lti-properties}
- May leverage linearity property of LTI systems if the step/impulse response is already known 
<a class="zoom" href="/notes/img/lti-linearity-property-laplace-system-response-example.png"><img src="/notes/img/lti-linearity-property-laplace-system-response-example.png" alt="LTI linearity property laplace system response example" loading="lazy"></a>

## Using MATLAB {#using-matlab}
- Analytic response with symbolic toolbox
<a class="zoom" href="/notes/img/analytic-response-with-symbolic-toolbox-laplace-transform-matlab.png"><img src="/notes/img/analytic-response-with-symbolic-toolbox-laplace-transform-matlab.png" alt="analytic response with symbolic toolbox laplace transform matlab" loading="lazy"></a>

- Numeric response (convolution sum)
<a class="zoom" href="/notes/img/numeric-response-using-convolution-sum-laplace-transform-matlab.png"><img src="/notes/img/numeric-response-using-convolution-sum-laplace-transform-matlab.png" alt="numeric response using convolution sum laplace transform matlab" loading="lazy"></a>

- Numeric response using built-in functions (`impulse`, `step`, `lsim`)
	- Easiest method possible
<a class="zoom" href="/notes/img/numeric-response-using-builtin-functions-laplace-transform-matlab.png"><img src="/notes/img/numeric-response-using-builtin-functions-laplace-transform-matlab.png" alt="numeric response using builtin functions laplace transform matlab" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">System response (course handout)</span>
