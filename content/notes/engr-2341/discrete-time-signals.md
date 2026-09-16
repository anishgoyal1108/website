---
author: "Anish Goyal"
title: "Discrete Time Signals"
description: "Discrete-time signals have an independent variable (typically represented with n) that only takes integers"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-01-16T21:53:24
modified: 2025-01-20T15:01:30
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 2
weight: 20
slug: "discrete-time-signals"
links:
  - "/notes/engr-2341/digital-signals/"
  - "/notes/engr-2341/discrete-time-signals-concept/"
sources:
  - "Discrete-time signals"
generated: true
---

- <a class="internal-link" href="/notes/engr-2341/discrete-time-signals-concept/">Discrete-time signals</a> have an independent variable (typically represented with $n$) that only takes integers

<a class="zoom" href="/notes/img/discrete-time-signal.png"><img src="/notes/img/discrete-time-signal.png" alt="discrete time signal" loading="lazy"></a>

- <a class="internal-link" href="/notes/engr-2341/digital-signals/">Digital signals</a> are a type of discrete-time signal that accepts values from a finite set.
	- This occurs by sampling continuous-time signals
	- Digital and discrete-time can be used interchangeably
- Digital and discrete-time signals can be represented by:
	- Formula: $x[n] = 0.5e^{0.1n}(u[n]-u[n-3])$
	- Weighted sum of discrete-time impulses: $x[n] = 0.5\delta[n]+0.553\delta[n-1]+0.611\delta[n-2]$
		- Is 1 for $n=0$ or at $n=d$ for $\delta[n-d]$ (timeshifted)
	- Number sequence: $x[n]=(0.5, 0.553,0.611,0,\dots)$

### Example {#example}
- Weighted sum form: $x[n] = 2\delta[n]+4\delta[n-1]-\delta[n-2]+\delta[n-3]+3\delta[n-4]$
- Sequence form: $x[n] = (2, 4, -1, 1, 3, 0, \dots)$

<a class="zoom" href="/notes/img/example-discrete-signal.png"><img src="/notes/img/example-discrete-signal.png" alt="example discrete signal" loading="lazy"></a>

## Sampling {#sampling}
- A continuous-time signal can be converted into digital signals by periodically sampling its values at regular intervals, quantizing them
	- $x[n] = x(t) \vert_{t=nT_s} = x(nT_s) = x(n / f_s)$
- The sample rate should be at least twice the highest frequency component in the signal ([Shannon/Nyquist rate](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem))

## References {#references}
- <span class="cite cite-ref">Discrete-time signals (course handout)</span>
