---
author: "Anish Goyal"
title: "Fourier System Response"
description: "It is possible to obtain the response of a continuous LTI system via Fourier transform"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-02-18T15:28:19
modified: 2025-04-01T05:26:40
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 12
weight: 120
slug: "fourier-system-response"
links:
  - "/notes/engr-2341/fourier-transform/"
  - "/notes/engr-2341/frequency-response/"
sources:
  - "System response"
generated: true
---

## Using Fourier Transform {#using-fourier-transform}
- It is possible to obtain the response of a continuous LTI system via <a class="internal-link" href="/notes/engr-2341/fourier-transform/">Fourier transform</a>
- Should only be used when:
	- Convolution integral is not manageable
	- Step responses are unknown (cannot leverage homogeneity/additivity)
	- System is not a sum of sinusoids
- For a system described by impulse response $h(t)$ and input $x(t)$:
	1. $x(t) \xrightarrow{\mathscr{F}}X(j\omega)$
	2. $h(t) \xrightarrow{\mathscr{F}}H(j\omega)$
	3. $X(j\omega) \cdot H(j\omega) = Y(j\omega)$
	4. $Y(j\omega) \xrightarrow{\mathscr{F}^{-1}}y(t)$
- This is possible due to convolution property of <a class="internal-link" href="/notes/engr-2341/fourier-transform/">Fourier transform</a>

<a class="zoom" href="/notes/img/fourier-transform-system-response-example.png"><img src="/notes/img/fourier-transform-system-response-example.png" alt="fourier transform system response example" loading="lazy"></a>

## Using Sum of Sinusoids {#using-sum-of-sinusoids}
- See <a class="internal-link" href="/notes/engr-2341/frequency-response/">Frequency Response</a>
<a class="zoom" href="/notes/img/sum-of-sinusoids-system-response-example.png"><img src="/notes/img/sum-of-sinusoids-system-response-example.png" alt="sum of sinusoids system response example" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">System response (course handout)</span>
