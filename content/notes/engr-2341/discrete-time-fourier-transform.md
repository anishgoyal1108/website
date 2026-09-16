---
author: "Anish Goyal"
title: "Discrete-time Fourier Transform"
description: "Transforms x[n] (sequence of values) to a continuous function of frequency, X(e^{j{}}), with period 2"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-03-13T19:26:31
modified: 2025-03-27T10:31:02
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 15
weight: 150
slug: "discrete-time-fourier-transform"
links: []
sources:
  - "Dtft"
  - "Dtft table (course handout)"
generated: true
---

## Types of Frequency Transforms {#types-of-frequency-transforms}

<a class="zoom" href="/notes/img/frequency-transform-types-1.png"><img src="/notes/img/frequency-transform-types-1.png" alt="frequency transform types 1" loading="lazy"></a>

<a class="zoom" href="/notes/img/frequency-transform-types-2.png"><img src="/notes/img/frequency-transform-types-2.png" alt="frequency transform types 2" loading="lazy"></a>

## DTFT {#dtft}
- Transforms $x[n]$ (sequence of values) to a continuous function of frequency, $X(e^{j\hat{\omega}})$, with period $2\pi$
- Can be used to determine $X(e^{j\hat{\omega}})$, the continuous frequency spectrum of $x[n]$
- Can be used to find $H(e^{j\hat{\omega}})$, the frequency response of $x[n]$, by taking DTFT of $h[n]$, the impulse response
- Only exists for analytical purposes because it is impossible to process an infinite number of samples
	- This makes it less important for computational processing, but DTFT may be used for short sequences
	- Can use the <cite class="cite">Dtft table (course handout)</cite> for this purpose
- The sequence must be absolutely summable
	- Finite-length sequences are always absolutely convergent
	- Infinite length sequences are convergent if they are one-sided and decaying

### Representation {#representation}

$$X(e^{j\hat{\omega}}) = \sum_{n=-\infty}^{\infty} x[n]e^{-j \hat{\omega}n}$$

### Inverse DTFT {#inverse-dtft}

$$x[n] = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(e^{j\omega})e^{j \hat{\omega}n} \ \mathrm{d}\omega$$

## Spectrum of Discrete-time Signals {#spectrum-of-discrete-time-signals}
- Practical, finite duration signals will always have a DTFT with a continuous frequency spectrum
- Cannot take the DTFT of any square wave functions, including $u(t)$, since they are not absolutely summable
- Some two-sided signals (sines/cosines and compkex exponentials) have DTFTs

## References {#references}
- <span class="cite cite-ref">Dtft (course handout)</span>
- [Discrete-time Fourier transform](https://en.wikipedia.org/wiki/Discrete-time_Fourier_transform)
- Can anyone intuitively explain why the Dirac delta function contains all frequencies
