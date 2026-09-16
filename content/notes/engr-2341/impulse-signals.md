---
author: "Anish Goyal"
title: "impulse signals"
description: "Non-zero signals concentrated around a specific moment in time"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-01-14T08:36:33
modified: 2025-01-16T21:53:02
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "concept"
weight: 9010
slug: "impulse-signals"
links:
  - "/notes/engr-2341/dirac-delta-function/"
sources: []
generated: true
---

## Impulse Signals {#impulse-signals}

- Non-zero signals concentrated around a specific moment in time
- Has an area of 1 
- Not a function, but can be approximated with the

  <div class="transclusion" data-source="04. Notes/Undergraduate Courses/ENGR 2341/Dirac delta function.md">
  <a class="transclusion-source" href="/notes/engr-2341/dirac-delta-function/" title="Open Dirac delta function"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  ## Dirac Delta Function {#dirac-delta-function-embed1}
  A limiting case of a rectangular pulse function, $\delta_{\Delta}(t)$, as the width $\Delta \rightarrow 0$.

  ### Rectangular Pulse Function {#rectangular-pulse-function-embed1}
  - For $-\Delta \le t \le \Delta$, the rectangular pulse has a value of $\frac{1}{2\Delta}$
  - Outside this range, the function is 0

  ### Normalization Property {#normalization-property-embed1}
  - Regardless of the choice of $\Delta$, the area of $\delta_{\Delta} = 1$

  $$\int_{-\Delta}^{\Delta}\frac{1}{2\Delta} \ \mathrm{d}t = 1$$

  - This ensures that the height of the pulse increases proportionally as the width becomes narrower

  ### Dirac Delta as a Limit {#dirac-delta-as-a-limit-embed1}
  - $\delta(t)$ is defined as the limit of this rectangular pulse as $\Delta \rightarrow 0$

  </div>

### Sampling Property {#sampling-property}
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

#### Example of Impulse Sampling {#example-of-impulse-sampling}
Simplify this as much as possible: $x_{2}(t) = e^{-(t-5)}u(t-5)\delta(t-10)$

$$
\begin{align}
x_{2}(t) &= e^{-(10-5)}u(10-5)\delta(t-10) \\
&= e^{-5} \cdot 1 \cdot \delta(t-10) \\
&= e^{-5}\delta(t-10)
\end{align}
$$
