---
author: "Anish Goyal"
title: "Spectrum Signals"
description: "The spectrum of a signal is the frequency content of the signal"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-02-10T14:48:21
modified: 2025-04-01T05:58:17
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 7
weight: 70
slug: "spectrum-signals"
links:
  - "/notes/engr-2341/spectrum-concept/"
  - "/notes/engr-2341/sum-of-complex-exponentials/"
sources:
  - "Sinusoidal signal"
  - "Spectrum modulated signals"
  - "Spectrum sinusoidal signals"
generated: true
---

## Spectrum {#spectrum}
- The <a class="internal-link" href="/notes/engr-2341/spectrum-concept/">spectrum</a> of a signal is the frequency content of the signal
- Represented as a list of frequency-amplitude pairs or a complex amplitude vs frequency plot
	- Negative complex amplitudes are impossible! To normalize negative amplitudes, add/subtract $\pi$ to the phase $\phi$

<a class="zoom" href="/notes/img/one-sided-vs-two-sided-spectrum.png"><img src="/notes/img/one-sided-vs-two-sided-spectrum.png" alt="one-sided vs two-sided spectrum" loading="lazy"></a>

### Plots {#plots}
- One-sided spectrum plots use the sum of cosines

$$
\sum_{k=1}^{n}A_{k}\cos(\omega t + \phi_{k}) = A\cos(\omega t+\phi)
$$

- Two-sided spectrum plots use the <a class="internal-link" href="/notes/engr-2341/sum-of-complex-exponentials/">Sum of complex exponentials</a> obtained using Inverse Euler

$$
\cos \theta = \frac{e^{j\theta} + e^{-j\theta}}{2}
$$

- Spectrograms have time on $x$-axis and $\omega$ on $y-axis$, with the magnitude of the spectrum being colored (like a heat map)

<a class="zoom" href="/notes/img/spectrum-plots.png"><img src="/notes/img/spectrum-plots.png" alt="spectrum plots" loading="lazy"></a>

## Sinusoidal Signals {#sinusoidal-signals}
- Signals can be expressed as a sum of sinusoidal signals
- Two forms: cosine and complex exponential

### Cosine Form {#cosine-form}
- Amplitude is $A$
- $\omega$ is radian frequency (rad/s)
- $\phi$ is phase (rad)

$$x(t) = A\cos(\omega t+\phi) = A\cos(\omega (t-t_{d}))$$

### Complex Exponential form {#complex-exponential-form}
- Each cosine comes with two pieces
	- Each piece has half the amplitude
	- One piece has $\omega \gt 0$ and the same phase
	- The other piece has $\omega \lt 0$ and negated phase

$$
A\cos(\omega t + \phi) = A\frac{e^{j(\omega t + \phi)} + e^{-j(\omega t + \phi)}}{2} = \frac{A}{2} \left(e^{j(\omega t + \phi)} + e^{-j(\omega t + \phi)}\right)
$$

## References {#references}
- <span class="cite cite-ref">Spectrum modulated signals (course handout)</span>
- <span class="cite cite-ref">Spectrum sinusoidal signals (course handout)</span>
- <span class="cite cite-ref">Sinusoidal signal (course handout)</span>
