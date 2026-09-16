---
author: "Anish Goyal"
title: "Frequency Response"
description: "Represented by:"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-02-18T15:27:00
modified: 2025-04-01T05:58:32
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 10
weight: 100
slug: "frequency-response"
links:
  - "/notes/engr-2341/fourier-transform/"
sources:
  - "Frequency response"
generated: true
---

## Continuous-time Systems {#continuous-time-systems}
- Represented by:
	- Differential equation
	- Impulse response (convolution integral)
	- Frequency response
	- Transfer function
- Impulse response, $h(t)$, is the system response to $\delta$
- LTI system is BIBO stable if its impulse response is absolutely integrable

$$
h(t) = y(t) \ \vert_{x(t) = \delta(t)}
$$

$$
y(t) = h(t) * x(t) = \int_{-\infty}^{\infty} = h(\tau)x(t-\tau) \ \mathrm{d}\tau
$$

## Frequency Response {#frequency-response-1}
- Describes what the system does to sinusoidal inputs
- Broken down into magnitude and phase components

$$H(j\omega) = \vert H(j\omega) \vert \angle H(j\omega)$$

- Determined using the <a class="internal-link" href="/notes/engr-2341/fourier-transform/">Fourier transform</a> of $h(t)$

$$H(j\omega) = \int_{-\infty}^{\infty}h(t)e^{-j\omega t} \ \mathrm{d}t$$

### Analysis of $H(j\omega)$ {#analysis-of-h-j}
Let $H(j\omega)$ be a general frequency response function of the form $H(jω)= \frac{N(j\omega)}{D(j\omega)}$. Then:
- $|H(j\omega)| = \frac{|N(j\omega)|}{|D(j\omega)|}$
- $H(j\omega) = \angle N(j\omega) - \angle D(j\omega)$

#### Magnitude Calculation {#magnitude-calculation}
- If $M(j\omega) = A e^{j\phi(\omega)}$, $|M(j\omega)| = A$
- If $M(j\omega) = a + j b(\omega)$, $|M(j\omega)| = \sqrt{a^2 + b(\omega)^2}$

#### Phase Calculation {#phase-calculation}
- If $M(j\omega) = A e^{j\phi(\omega)}$, $\angle M(j\omega) = \phi(\omega)$
- If $M(j\omega) = a + j b(\omega)$, $\angle M(j\omega) = \tan^{-1}\left(\frac{b(\omega)}{a}\right)$

## Sinusoidal Response {#sinusoidal-response}
- Response to sinusoids for an LTI system is a sinusoid of the same frequency with a shifted amplitude (gain) and phase, dependent on $H(j\omega)$
- Frequencies of the sinusoidal components cannot change and it must be two-sided
- Input format $x(t)$:

$$x(t) = A_{0} + \sum_{k=1}^{N}A_{k}\cos(\omega_{k}t + \phi_{k})$$

- Output format $y(t)$:

$$y(t) = \vert H(j0) \vert A_{0} + \sum_{k=1}^{N} \vert H(j\omega_{k}) \vert A_{k} \cos(\omega_{k}t + \phi_{k} + \angle H(j\omega_{k}))$$

<a class="zoom" href="/notes/img/sinusoidal-response-example.png"><img src="/notes/img/sinusoidal-response-example.png" alt="sinusoidal response example" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Frequency response (course handout)</span>
