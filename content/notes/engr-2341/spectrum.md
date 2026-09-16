---
author: "Anish Goyal"
title: "Spectrum"
description: "Can be determined by inspection"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-02-18T15:27:28
modified: 2025-02-18T15:27:55
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 11
weight: 110
slug: "spectrum"
links:
  - "/notes/engr-2341/fourier-series/"
  - "/notes/engr-2341/fourier-transform/"
  - "/notes/engr-2341/sum-of-complex-exponentials/"
  - "/notes/engr-2341/sum-of-cosines/"
sources:
  - "Spectrum"
generated: true
---

## Sum of Sinusoids {#sum-of-sinusoids}
- Can be determined by inspection
- A list of frequency-complex amplitude pairs
	- For one-sided spectrum, use <a class="internal-link" href="/notes/engr-2341/sum-of-cosines/">Sum of cosines</a>
	- For two-sided spectrum, use <a class="internal-link" href="/notes/engr-2341/sum-of-complex-exponentials/">Sum of complex exponentials</a>

<a class="zoom" href="/notes/img/spectrum-with-inspection-example.png"><img src="/notes/img/spectrum-with-inspection-example.png" alt="spectrum with inspection example" loading="lazy"></a>

## Using Fourier Series {#using-fourier-series}
- Possible to use <a class="internal-link" href="/notes/engr-2341/fourier-series/">Fourier series</a> representation if the signal is not a sum of sinusoids
- There will be an infinite number of terms in the spectrum corresponding to the Fourier series

$$X(j\omega) = \left\{(\omega_{k}, a_{k})\right\}, k \in (-\infty, \infty)$$ 

## Using Fourier Transform {#using-fourier-transform}
- The spectrum of any continuous-time signal is its <a class="internal-link" href="/notes/engr-2341/fourier-transform/">Fourier transform</a>
- It is expressed as a continuous function of frequency, $\omega$

$$X(j\omega) = \int_{-\infty}^{\infty} x(t) e^{-j\omega t} \ \mathrm{d}t$$

<a class="zoom" href="/notes/img/spectrum-fourier-transform-example.png"><img src="/notes/img/spectrum-fourier-transform-example.png" alt="spectrum fourier transform example" loading="lazy"></a>
<a class="zoom" href="/notes/img/spectrum-fourier-transform-example-2.png"><img src="/notes/img/spectrum-fourier-transform-example-2.png" alt="spectrum fourier transform example 2" loading="lazy"></a>

## Using Fourier Analysis {#using-fourier-analysis}
- Only useful for a piecewise periodic function
- Determine $a_0, \omega_0, a_k$ to find the infinite spectrum

<a class="zoom" href="/notes/img/spectrum-fourier-analysis-example.png"><img src="/notes/img/spectrum-fourier-analysis-example.png" alt="spectrum fourier analysis example" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Spectrum (course handout)</span>
