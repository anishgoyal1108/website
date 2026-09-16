---
author: "Anish Goyal"
title: "Discrete Time Systems"
description: "A discrete-time system (filter) operates on an input sequence x[n] and produces an output sequence y[n]"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-01-21T17:01:55
modified: 2025-01-28T00:26:13
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 4
weight: 40
slug: "discrete-time-systems"
links: []
sources:
  - "Discrete-time systems"
generated: true
---

- A discrete-time system (filter) operates on an input sequence $x[n]$ and produces an output sequence $y[n]$
- Common representations:
	- Difference equations
	- Impulse response/convolution sum
	- Transfer/system function
	- Frequency response

## System Representations {#system-representations}
| **Continuous-time**                                                             | **Discrete-time**                                                  |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| $y(t) = f(y(t), x(t))$                                                          | $y[n] = \sum_{\ell=2}^N a_{\ell}y[n-\ell]+\sum_{k=0}^Mb_{k}x[n-k]$ |
| $y(t) = x(t) * h(t) = \int_{-\infty}^{\infty}x(t-\tau)h(\tau) \ \mathrm{d}\tau$ | $y[n] = h[n] * x[n] = \sum_{k=-\infty}^\infty h[k]x[n-k]$          |
| $H(s), \ H(j\omega)$                                                            | $H(z), \ H(e^{j\hat{\omega}})$                                     |

## Impulse Response {#impulse-response}
- Impulse responses in discrete-time are labeled $h[n]$

$$
\begin{align}
y[n] &= \sum_{\ell=1}^N a_{\ell}y[n-\ell]+\sum_{k=0}^Mb_{k}x[n-k] \\
h[n] &= y[n] \ \vert_{x[n] = \delta[n]}
\end{align}
$$

## System Properties {#system-properties}
- Practically the same as continuous systems (see causality, linearity, time invariance, and BIBO stability)
	- For BIBO stability, the system must be absolutely summable

## FIR and IIR Filters {#fir-and-iir-filters}
- Finite impulse response (FIR) and infinite impulse response (IIR) filters are two specific discrete-time systems

### FIR {#fir}
- Properties:
	- LTI
	- Always stable
	- Ambiguous causality
- Output depends only on the input $x[n]$
- $b_k$ is the $(M+1)$ filter coefficients
- Filter order is $M$
- Response determined with difference equation or convolution sum

$$y[n] = \sum_{k=0}^M b_{k}x[n-k]$$

### IIR {#iir}
- Properties:
	- LTI iff I/O is 0 before first applied input at $n_0$
		- $x[n], y[n] = 0, n \lt n_{0}$
	- Ambiguous stability
	- Ambiguous causality
- Output depends on $x[n]$ *and* previous outputs $y[n]$ (recursive filter)
- $b_k$ and $a_\ell$ are the feedforward and feedback coefficients, respectively
- $(N+M+1)$ total coefficients
- Filter order is $\max(N, M)$
- Response determined with the difference equation

$$y[n] = \sum_{\ell=1}^M a_{\ell}y[n-\ell]+\sum_{k=0}^M b_{k}x[n-k]$$

## References {#references}
- <span class="cite cite-ref">Discrete-time systems (course handout)</span>
