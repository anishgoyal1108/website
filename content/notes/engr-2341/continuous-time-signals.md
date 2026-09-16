---
author: "Anish Goyal"
title: "Continuous Time Signals"
description: "Physical signals are analog"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-01-15T11:02:45
modified: 2025-01-20T15:00:48
readingtime: "4"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 1
weight: 10
slug: "continuous-time-signals"
links:
  - "/notes/engr-2341/analog/"
  - "/notes/engr-2341/dirac-delta-function/"
  - "/notes/engr-2341/fundamental-period/"
  - "/notes/engr-2341/impulse-signals/"
  - "/notes/engr-2341/periodic/"
  - "/notes/engr-2341/pulse-signals/"
  - "/notes/engr-2341/step-signals/"
sources:
  - "Continuous-time signals"
  - "Sinusoidal signals"
generated: true
---

- Physical signals are <a class="internal-link" href="/notes/engr-2341/analog/">analog</a>
- Examples include: impulses, steps, exponentials, ramps, sinusoids, and combinations of them

<div class="transclusion" data-source="04. Notes/Undergraduate Courses/ENGR 2341/impulse signals.md">
<a class="transclusion-source" href="/notes/engr-2341/impulse-signals/" title="Open impulse signals"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

## Impulse Signals {#impulse-signals-embed1}

- Non-zero signals concentrated around a specific moment in time
- Has an area of 1 
- Not a function, but can be approximated with the

  <div class="transclusion" data-source="04. Notes/Undergraduate Courses/ENGR 2341/Dirac delta function.md">
  <a class="transclusion-source" href="/notes/engr-2341/dirac-delta-function/" title="Open Dirac delta function"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  ## Dirac Delta Function {#dirac-delta-function-embed2}
  A limiting case of a rectangular pulse function, $\delta_{\Delta}(t)$, as the width $\Delta \rightarrow 0$.

  ### Rectangular Pulse Function {#rectangular-pulse-function-embed2}
  - For $-\Delta \le t \le \Delta$, the rectangular pulse has a value of $\frac{1}{2\Delta}$
  - Outside this range, the function is 0

  ### Normalization Property {#normalization-property-embed2}
  - Regardless of the choice of $\Delta$, the area of $\delta_{\Delta} = 1$

  $$\int_{-\Delta}^{\Delta}\frac{1}{2\Delta} \ \mathrm{d}t = 1$$

  - This ensures that the height of the pulse increases proportionally as the width becomes narrower

  ### Dirac Delta as a Limit {#dirac-delta-as-a-limit-embed2}
  - $\delta(t)$ is defined as the limit of this rectangular pulse as $\Delta \rightarrow 0$

  </div>

### Sampling Property {#sampling-property-embed2}
- A function multiplied by an impulse scales the function by its value at the time of the impulse
	- $f(t)\delta(t-t_{0}) = f(t_{0})\delta(t-t_{0})$
- Basically, you're getting the value of $f(t)$ specifically only at $t_0$, and 0 everywhere else

$$
\begin{align}
\cos(25\pi t)(\delta(t)+\delta(t-0.01)) &= \cos(25\pi t)\delta(t) + \cos(25\pi t)\delta(t-0.01) \\
&= \cos(0)\delta(t) + \cos(0.25\pi t)\delta(t-0.01) \\
&= \delta(t) + 0.707\delta(t-0.01)
\end{align}
$$

#### Example of Impulse Sampling {#example-of-impulse-sampling-embed2}
Simplify this as much as possible: $x_{2}(t) = e^{-(t-5)}u(t-5)\delta(t-10)$

$$
\begin{align}
x_{2}(t) &= e^{-(10-5)}u(10-5)\delta(t-10) \\
&= e^{-5} \cdot 1 \cdot \delta(t-10) \\
&= e^{-5}\delta(t-10)
\end{align}
$$

</div>

<div class="transclusion" data-source="04. Notes/Undergraduate Courses/ENGR 2341/step signals.md">
<a class="transclusion-source" href="/notes/engr-2341/step-signals/" title="Open step signals"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

## Step Signals {#step-signals-embed3}
- Signals that are nonzero for $t \ge 0$

$$
u(t) = \begin{cases}
0 & t \lt 0 \\
1 & t \ge 0
\end{cases}
$$

- Unit step signals have a height of 1
- Used to create one sided signals (usually right-sided)

$$ 
\begin{align}
x(t) &= 3.72e^{-12.8t} \\
x_{\mathrm{rs}}(t) &= 3.72e^{-12.8t} \cdot u(t)
\end{align}
$$

- Discontinuous at $t = 0$ due to the piecewise nature of the function

</div>

$$

$$

<div class="transclusion" data-source="04. Notes/Undergraduate Courses/ENGR 2341/pulse signals.md">
<a class="transclusion-source" href="/notes/engr-2341/pulse-signals/" title="Open pulse signals"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

## Pulse Signals {#pulse-signals-embed4}
- Pulses are only non-zero between $t_1$ and $t_2$
- Unit pulses have a height of 1
- Technically a difference of step signals

$$
p(t) = u(t-t_{1})-u(t-t_{2})=\begin{cases}
1 & t_{1} \le t \le t_{2} \\
0 & t \lt t_{1} \ \mathrm{or} \ \gt t_{2}
\end{cases}
$$

- Multiplying a function by a pulse gives us a finite duration signal

$$
x(t) = 5\cos(3\pi t) \cdot (u(t)-u(t-2))
$$

- This gives us a cosine wave with $f = 3 \pi$ rad/s and $A = 5$ for $t \in [0, 2]$ 

</div>

## Continuity {#continuity}
- Signals are time-continuous if the value of the signal at a time $t$ is the same as the limit of the right and left sides
- Signals that are continuous for all time are called continuous signals

## Time Shifts {#time-shifts}
- Signals can shift left/right in time with respect to $t = 0$.
- Leftward shifts: advance in time; rightward shifts: delay in time

$$
u(t) = \begin{cases}
0 & t \lt 0 \\
1 & t \ge 0
\end{cases} \\
$$

$$
u(t-2) = \begin{cases}
0 & t \lt 2 \\
1 & t \ge 2 \\
\end{cases}
$$

## Periodicity {#periodicity}
- A continuous-time signal $x(t)$ is <a class="internal-link" href="/notes/engr-2341/periodic/">periodic</a> if $\exists \ T \ | \ x(t+T) = x(t) \ \forall \ t$
- The <a class="internal-link" href="/notes/engr-2341/fundamental-period/">fundamental period</a> $T_0$ is the smallest $T$ that satisfies periodicity
	- $T_0 = \frac{1}{f}$, assuming $f$ is the frequency in rad/s
- The sinusoid has $A = 5, f = 2000$ rad/s, and phase shift of 0 rad

<a class="zoom" href="/notes/img/periodic-sin.png"><img src="/notes/img/periodic-sin.png" alt="periodic sin" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Continuous-time signals (course handout)</span>
- <span class="cite cite-ref">Sinusoidal signals (course handout)</span>
