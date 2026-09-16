---
author: "Anish Goyal"
title: "Sinusoidal Signals and Phasor Representation"
description: "Time Domain Signal:"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3345"
date: 2025-06-24T10:29:09
modified: 2025-07-01T10:06:22
readingtime: "2"
course: "EENG 3345"
course_slug: "eeng-3345"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 2
weight: 20
slug: "sinusoidal-signals-and-phasor-representation"
links: []
sources:
  - "Course handout 2: phasor and time domains"
generated: true
---

## Time Domain vs. Phasor Domain {#time-domain-vs-phasor-domain}
* **Time Domain Signal**:
  $$
  v(t) = V_m \cos(\omega t + \phi)
  $$

  * Represents instantaneous voltage as a function of time.
  * Harder to manipulate analytically for AC circuit analysis.

* **Phasor Domain**:
  $$
  V = V_m e^{j\phi}
  \quad \text{or} \quad V = V_m (\cos(\phi) + j \sin(\phi))
  $$

  * Represents a **complex number** encoding amplitude and phase.
  * Omits time dependency (only valid for steady-state sinusoidal signals).
  * Based on **Euler’s formula**:
    $$
    e^{j\phi} = \cos(\phi) + j \sin(\phi)
    $$
  * Shorthand notation is $V_m \angle \phi$

## Conversion Between Phasor and Time Domain {#conversion-between-phasor-and-time-domain}
* **From Phasor to Time Domain**: Multiply phasor $V$ by $e^{j\omega t}$, then take the real part
  $$
  v(t) = \Re\{ V e^{j\omega t} \} = V_m \cos(\omega t + \phi)
  $$

* **From Time Domain to Phasor Domain**: Drop the time-dependent $e^{j\omega t}$ and keep only the amplitude and phase
  $$
  v(t) = V_m \cos(\omega t + \phi) \quad \Rightarrow \quad V = V_m e^{j\phi}
  $$

## Phasor Arithmetic {#phasor-arithmetic}
Let $V_1 = A e^{j\theta_1}$, $V_2 = B e^{j\theta_2}$:

* **Addition/Subtraction**:
  * Convert to rectangular form and add real/imaginary parts separately
    $$
    V = V_{m1}(\cos\phi_1 + j\sin\phi_1) \pm V_{m2}(\cos\phi_2 + j\sin\phi_2)
    $$

* **Multiplication**: Multiply magnitudes, add angles
  $$
  V_1 \cdot V_2 = AB e^{j(\theta_1 + \theta_2)}
  $$

* **Division**: Divide magnitudes, subtract angles
  $$
  \frac{V_1}{V_2} = \frac{A}{B} e^{j(\theta_1 - \theta_2)}
  $$

## Sinusoidal Steady State Analysis {#sinusoidal-steady-state-analysis}
### RC Circuit Example {#rc-circuit-example}
<a class="zoom" href="/notes/img/sinusoidal-steady-state-analysis-solved-example-1.png"><img src="/notes/img/sinusoidal-steady-state-analysis-solved-example-1.png" alt="sinusoidal steady state analysis solved example 1" loading="lazy"></a>

### RL Circuit Example {#rl-circuit-example}
- Should have $\cos$ at the end
<a class="zoom" href="/notes/img/sinusoidal-steady-state-analysis-solved-example-2.png"><img src="/notes/img/sinusoidal-steady-state-analysis-solved-example-2.png" alt="sinusoidal steady state analysis solved example 2" loading="lazy"></a>

## Phasor Arithmetic with Multiple Frequencies {#phasor-arithmetic-with-multiple-frequencies}
- Cannot be done, have to use Superposition instead

## References {#references}
- <span class="cite cite-ref">Course handout 2: phasor and time domains</span>
