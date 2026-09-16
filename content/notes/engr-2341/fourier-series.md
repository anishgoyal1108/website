---
author: "Anish Goyal"
title: "Fourier Series"
description: "Harmonic frequencies are integer multiples of a fundamental frequency"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-02-10T14:50:05
modified: 2025-02-10T14:51:56
readingtime: "3"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 8
weight: 80
slug: "fourier-series"
links:
  - "/notes/engr-2341/dirichlet-conditions/"
  - "/notes/engr-2341/fundamental-frequency/"
  - "/notes/engr-2341/fundamental-period/"
  - "/notes/engr-2341/sum-of-complex-exponentials/"
  - "/notes/engr-2341/sum-of-cosines-and-sines/"
  - "/notes/engr-2341/sum-of-cosines/"
  - "/notes/engr-2341/sum-of-sines/"
sources:
  - "Fourier series"
generated: true
---

## Harmonic Sum of Sinusoids {#harmonic-sum-of-sinusoids}
- Harmonic frequencies are integer multiples of a <a class="internal-link" href="/notes/engr-2341/fundamental-frequency/">fundamental frequency</a>
- Signals that are a sum of sinusoids are periodic as multiples of the <a class="internal-link" href="/notes/engr-2341/fundamental-period/">fundamental period</a>
	- $T_0 = \frac{2\pi}{\omega_0}= \frac{1}{f_0}$
- General form:

$$x(t) = A_{0} + \sum_{k=0}^N A_{k} \cos(k\omega_{0}t + \phi_{k})$$

- The fundamental frequency is the greatest common denominator of the frequency components of the signal
	- $f_0 = \gcd(f_1, f_2, \dots, f_N)$ (measured in Hz, without the $2\pi$)
	- $\omega_0 = \gcd(\omega_1, \omega_2, \dots, \omega_N)$ (measured in rad/s, with the $2\pi$)

## Fourier Series {#fourier-series-1}
- Allows representation of non-sinusoids as harmonic sums of sinusoids
	- *Fourier analysis*: finding spectrum from signal
	- *Fourier synthesis*: finding signal from spectrum
- What signals have a Fourier series representation?
	- Must be periodic
	- Must meet <a class="internal-link" href="/notes/engr-2341/dirichlet-conditions/">Dirichlet conditions</a>
- Fourier series representations:

	- <div class="transclusion" data-source="04. Notes/Undergraduate Courses/ENGR 2341/Sum of cosines.md">
      <a class="transclusion-source" href="/notes/engr-2341/sum-of-cosines/" title="Open Sum of cosines"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

      $$x(t) = \sum_{k=0}^\infty A_{k} \cos(\omega_{0}kt)$$

      </div>

	- <div class="transclusion" data-source="04. Notes/Undergraduate Courses/ENGR 2341/Sum of sines.md">
      <a class="transclusion-source" href="/notes/engr-2341/sum-of-sines/" title="Open Sum of sines"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

      $$x(t) = \sum_{k=0}^\infty B_{k} \sin(\omega_{0}kt)$$

      </div>

	- <div class="transclusion" data-source="04. Notes/Undergraduate Courses/ENGR 2341/Sum of complex exponentials.md">
      <a class="transclusion-source" href="/notes/engr-2341/sum-of-complex-exponentials/" title="Open Sum of complex exponentials"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

      $$x(t) = \sum_{k=-\infty}^\infty a_{k}e^{j\omega_{0}kt}$$

      </div>

	- <div class="transclusion" data-source="04. Notes/Undergraduate Courses/ENGR 2341/Sum of cosines and sines.md">
      <a class="transclusion-source" href="/notes/engr-2341/sum-of-cosines-and-sines/" title="Open Sum of cosines and sines"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

      $$x(t) = \sum_{k=0}^\infty A_{k} \cos(\omega_{0}kt) +  \sum_{k=0}^\infty B_{k} \sin(\omega_{0}kt)$$

      </div>

## Fourier Analysis {#fourier-analysis}
- To get the Fourier series representation of a signal:
	1. Determine $T_0$ and $\omega_0 = \frac{2\pi}{T_0}$
	2. Determine the coefficient of the DC (constant) term
	3. Determine the coefficients of the remaining harmonics
- For the <a class="internal-link" href="/notes/engr-2341/sum-of-complex-exponentials/">Sum of complex exponentials</a> Fourier series:
	- $k$ is the harmonic number
	- $k\omega_0$ is the frequency of the harmonic
	- $a_k$ is the complex amplitude of the harmonic
	- $(k\omega_0, a_k)$ pairs correspond to the two-sided spectrum
- Complex amplitude formula
	- The DC amplitude lacks an exponential term inside the integrand

$$
a_{k} = \frac{1}{T_{0}} \int_{0}^{T_{0}}x(t)e^{-j\omega_{0}kt} \ \mathrm{d}t
$$

## Fourier Synthesis {#fourier-synthesis}
- To synthesize a signal from its spectrum, perform a running loop of each term in the Fourier series
- Should already have complex amplitude and frequency arrays
	- $a_k$ should be halved if summing over complex exponentials
- Make sure to initialize the following:
	- $t$ array over the proper time interval
	- $x(t)$ array with all zeros
	- `sum` variable for running sum of the Fourier series

### Complex exponentials {#complex-exponentials}
1. Loop over $k \in [-N, N]$
2. Compute each harmonic $x_k(t) = a_k e^{j\omega_0 kt}$
3. Add each computed harmonic to the running sum $x(t)$

### Sum of cosines {#sum-of-cosines}
1. Loop over $k \in [0, N]$
2. Compute each harmonic $x_k(t) = A_{k} \cos(\omega_{0}kt)$
3. Add each computed harmonic to the running sum $x(t)$ 

## References {#references}
- <span class="cite cite-ref">Fourier series (course handout)</span>
