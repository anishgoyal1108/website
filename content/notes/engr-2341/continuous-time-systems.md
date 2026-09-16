---
author: "Anish Goyal"
title: "Continuous Time Systems"
description: "Manipulates (changes, records, transmits) signals"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-01-20T14:58:04
modified: 2025-01-20T16:10:35
readingtime: "2"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 3
weight: 30
slug: "continuous-time-systems"
links:
  - "/notes/engr-2341/additivity/"
  - "/notes/engr-2341/homogeneity/"
sources:
  - "Continuous-time systems"
generated: true
---

## System {#system}
- Manipulates (changes, records, transmits) signals
- Receives an input signal, operates on it, and produces an output signal
- Common representations:
	- Differential equations
	- Impulse response/convolution integral
	- Transfer/system function
	- Frequency response

## Impulse Response {#impulse-response}
- Impulse responses, $h(t)$, is the system's response to a unit impulse input

$$
\begin{align}
y(t) &= f(y(t), x(t)) \\
h(t) &= y(t) \ \vert_{x(t)=\delta(t)}
\end{align}
$$

- The impulse response of an integrator is the unit step

$$
\begin{align}
y(t) &= \int_{-\infty}^{t}x(\tau) \ \mathrm{d}\tau \\
h(t) &= \int_{-\infty}^{t}\delta(\tau) \ \mathrm{d}\tau \\
&= u(t)
\end{align}
$$

## System Properties {#system-properties}
### Causality {#causality}
- Causal (non-predictive): the output only depends on the current and past inputs
- Causal iff the output at $t_1$ solely depends on the input from $t \in (-\infty, t_1]$
- Memoryless iff the output at $t_1$ solely depends on the input at $t_1$
- Non-causal systems cannot be physically implemented because that implies future values are contributing to the current output (reverse time)
- $h(t) = 0, \ t < 0$ for a causal LTI system

### Linearity {#linearity}
- Linear: the output is a linear mapping where <a class="internal-link" href="/notes/engr-2341/additivity/">additivity</a> and <a class="internal-link" href="/notes/engr-2341/homogeneity/">homogeneity</a> hold
- The superposition of additivity and homogeneity is possible:

$$
f(\alpha x_{1} + \beta x_{2}) = \alpha f(x_{1}) + \beta f(x_{2})
$$

### Time Invariance {#time-invariance}
- Time-invariant: a system that does not change over time
	- An input applied at some time or another time is the same, just delayed (shifted in time)
- Linear time-invariant (LTI) systems are desirable:
	- Can be characterized by their impulse response
	- Cannot produce frequency components not in the input

### BIBO Stability {#bibo-stability}
- Bounded-Input-Bounded-Output (BIBO) stable: a system with an absolutely integrable impulse response
- Typically have finite duration impulse responses or one-sided and decay to zero

$$
\int_{-\infty}^{\infty} \vert h(t) \vert \ \mathrm{d}t \lt \infty
$$

## References {#references}
- <span class="cite cite-ref">Continuous-time systems (course handout)</span>
