---
author: "Anish Goyal"
title: "Sampling"
description: "Converts a continuous-time signal to discrete-time signal"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-03-12T18:42:20
modified: 2025-04-01T05:58:40
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 13
weight: 130
slug: "sampling"
links:
  - "/notes/engr-2341/bandlimited/"
  - "/notes/engr-2341/fourier-series/"
  - "/notes/engr-2341/nyquist-interval/"
  - "/notes/engr-2341/nyquist-rate/"
  - "/notes/engr-2341/sqnr/"
sources:
  - "Sampling"
generated: true
---

## Sampling {#sampling-1}
- Converts a continuous-time signal to discrete-time signal
- The signal is periodically measured over discrete intervals of time
	- Each interval is called a **time step**
- Can be *quantized* over a finite number of bits to obtain a **digital signal**
	- Bit depth is the number of bits used to represent a sample. This means that the range of the amplitude will be split into $2^n$ levels 
	- <a class="internal-link" href="/notes/engr-2341/sqnr/">SQNR</a> measures the quantization precision
- Conditions for a signal to be unambiguously represented by its samples
	- Must be <a class="internal-link" href="/notes/engr-2341/bandlimited/">bandlimited</a>
	- Sampled at <a class="internal-link" href="/notes/engr-2341/nyquist-rate/">Nyquist rate</a> or higher

## Bandlimited Signals {#bandlimited-signals}
- Have a finite spectrum
	- There is an $f_\text{max} = \omega_{b}$ for which $X(j\omega) = 0$ for $|\omega| \gt \omega_{b}$
- Square waves are not bandlimited because they are represented by an infinite <a class="internal-link" href="/notes/engr-2341/fourier-series/">Fourier Series</a>

<a class="zoom" href="/notes/img/bandlimited-signals.png"><img src="/notes/img/bandlimited-signals.png" alt="bandlimited signals" loading="lazy"></a>

## Sampling and Spectrum {#sampling-and-spectrum}
- Sampling a continuous-time signal creates a mapping between the spectra and the discrete-time domain with $\hat{\omega} = \frac{\omega}{f_s}$
	- This constrains the discrete-time frequencies to the interval $[-\pi, \pi]$ (known as the <a class="internal-link" href="/notes/engr-2341/nyquist-interval/">Nyquist interval</a>), with the amplitudes remaining unchanged
- $\frac{\omega_b}{\pi} = f_s$, assuming $\omega_b$ in rad/s and $f_s$ in Hz
	- Basically, just remove $\pi$ to obtain the <a class="internal-link" href="/notes/engr-2341/nyquist-rate/">Nyquist rate</a> from $\omega_b$
-  discrete-time 

<a class="zoom" href="/notes/img/sampling-and-spectrum.png"><img src="/notes/img/sampling-and-spectrum.png" alt="sampling and spectrum" loading="lazy"></a>

<a class="zoom" href="/notes/img/sampled-signal-with-spectrum-example.png"><img src="/notes/img/sampled-signal-with-spectrum-example.png" alt="sampled signal with spectrum example" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Sampling (course handout)</span>
- <a class="video-link" href="https://www.youtube.com/watch?v=1KBLguIXL30&amp;t=279s">▶ Watch on YouTube</a>
