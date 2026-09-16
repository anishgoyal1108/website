---
author: "Anish Goyal"
title: "Discrete-time Frequency Response"
description: "Represented by"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-03-27T08:21:42
modified: 2025-04-01T10:12:58
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 16
weight: 160
slug: "discrete-time-frequency-response"
links:
  - "/notes/engr-2341/discrete-time-fourier-transform/"
sources:
  - "Dt frequency response"
generated: true
---

## Discrete-time Systems {#discrete-time-systems}
- Represented by
	- Difference equations
	- Impulse response (convolution sum)
	- Frequency response
	- Transfer (system) function
- $h[n]$, the impulse response, is the system response to a unit impulse input

$$h[n] = y[n] \vert_{x[n]=\delta[n]}$$

- BIBO stable if $h[n]$ is absolutely summable

$$y[n] = h[n] * x[n] = \sum_{k=-\infty}^{\infty}h[k]x[n-k]$$

## Frequency Response {#frequency-response}
- Describes what the system does to sinusoidal inputs
	- Commonly broken up into magnitude and phase
- Frequency response of a system can be found by taking the <a class="internal-link" href="/notes/engr-2341/discrete-time-fourier-transform/">DTFT</a> of $h[n]$

$$H(e^{j\hat{\omega}}) = \sum_{n=-\infty}^\infty h[n]e^{-j\hat{\omega}n} = |H(e^{j\hat{\omega}})|\angle H(e^{j\hat{\omega}})$$

## Sinusoidal Response {#sinusoidal-response}
- Response to sinusoidal inputs is a sinusoid of same frequency with an amplitude change and phase shift dependent on $H(e^{j\hat{\omega}})$
- The sinusoidal input must be two-sided and the frequencies of the sinusoidal components cannot change

$$x[n] = A_{0} + \sum_{k=1}^{N}A_{k}\cos(\hat{\omega_{k}}n+\phi_{k}), -\infty \lt n \lt \infty$$

$$
\begin{align*}
y[n] &= H(e^{j_{0}})A_{0} + \sum_{k=1}^{N}H(e^{j \hat{\omega_{k}}})A_{k}\cos(\hat{\omega_{k}}n + \phi_{k}) \\
&= \left|H(e^{j_{0}})\right|A_{0} + \sum_{k=1}^N \left|H(e^{j\hat{\omega_{k}}})\right|A_{k}\cos\left(\hat{\omega_{k}}n+\phi_{k}+\angle H(e^{j \hat{\omega_{k}}})\right)
\end{align*}
$$

<a class="zoom" href="/notes/img/discrete-sinusoidal-response-example.png"><img src="/notes/img/discrete-sinusoidal-response-example.png" alt="discrete sinusoidal response example" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Dt frequency response (course handout)</span>
