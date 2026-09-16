---
author: "Anish Goyal"
title: "Fourier Transform"
description: "FT decomposes a signal into its frequency components"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3345"
date: 2025-07-21T10:45:00
modified: 2025-07-22T10:07:10
readingtime: "2"
course: "EENG 3345"
course_slug: "eeng-3345"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 9
weight: 90
slug: "fourier-transform"
links:
  - "/notes/eeng-3345/laplace-transform/"
  - "/notes/engr-2341/fourier-system-response/"
  - "/notes/engr-2341/fourier-transform/"
  - "/notes/engr-2341/frequency-response/"
sources:
  - "Fourier Transforms"
  - "Fourier transform"
  - "Fourier transform table (course handout)"
  - "System response"
generated: true
---

## Introduction {#introduction}
- FT decomposes a signal into its frequency components
- Unlike the <a class="internal-link" href="/notes/eeng-3345/laplace-transform/">Laplace Transform</a> (which uses $s = \sigma + j\omega$), FT is restricted to $s = j\omega$

## Continuous-Time Fourier Transform {#continuous-time-fourier-transform}
- FT:

$$
X(j\omega) = \int_{-\infty}^{\infty} x(t) e^{-j \omega t} \, \mathrm{d}t
$$

- iFT:

$$
x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega) e^{j \omega t} \, \mathrm{d}\omega
$$

- Use the <cite class="cite">table of pairs and properties <span class="cite-src">[Fourier transform table (course handout)]</span></cite> to evaluate FT/iFT

## Solving Circuits Using Fourier Transform {#solving-circuits-using-fourier-transform}
- Although possible in some cases, it's not really practical to use FT when dealing with initial conditions or systems involving transient behavior
- General rule of thumb: LT for response, FT for spectral analysis (which isn't really covered in this course)

### Transfer Function and System Response {#transfer-function-and-system-response}
- Use when the impulse response $h(t)$ and input $x(t)$ are both known  
- Transform both signals:
  - $H(j\omega) = \mathcal{F}\{ h(t) \}$  
  - $X(j\omega) = \mathcal{F}\{ x(t) \}$  
- Multiply in frequency domain:
  $$
  Y(j\omega) = H(j\omega) X(j\omega)
  $$
- Inverse transform to get output:
  $$
  y(t) = \mathcal{F}^{-1} \left\{ Y(j\omega) \right\}
  $$

### Domain Transformation {#domain-transformation}
- Replace each circuit element with its Fourier-domain impedance
  - Resistor: $R$  
  - Inductor: $j\omega L$  
  - Capacitor: $\frac{1}{j\omega C}$
- Take the FT of the input signal
- Solve the circuit using methods of circuit analysis
- Compute output in the Fourier domain  
  $$
  Y(j\omega) = H(j\omega) X(j\omega)
  $$
- Take the iFT to find $y(t)$  
  $$
  y(t) = \mathcal{F}^{-1} \left\{ Y(j\omega) \right\}
  $$

## References {#references}
- <span class="cite cite-ref">Fourier Transforms (course handout)</span>  
- <span class="cite cite-ref">Fourier transform (course handout)</span>

- <div class="transclusion" data-source="04. Notes/Undergraduate Courses/ENGR 2341/12 Fourier System Response.md">
  <a class="transclusion-source" href="/notes/engr-2341/fourier-system-response/" title="Open Fourier System Response"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  ## Using Fourier Transform {#using-fourier-transform-embed1}
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

  ## Using Sum of Sinusoids {#using-sum-of-sinusoids-embed1}
  - See <a class="internal-link" href="/notes/engr-2341/frequency-response/">Frequency Response</a>
  <a class="zoom" href="/notes/img/sum-of-sinusoids-system-response-example.png"><img src="/notes/img/sum-of-sinusoids-system-response-example.png" alt="sum of sinusoids system response example" loading="lazy"></a>

  ## References {#references-embed1}
  - <span class="cite cite-ref">System response (course handout)</span>

  </div>
