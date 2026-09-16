---
author: "Anish Goyal"
title: "Laplace Transform"
description: "Transforms differential equations into algebraic systems"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3345"
date: 2025-07-14T11:25:36
modified: 2025-07-21T19:46:13
readingtime: "5"
course: "EENG 3345"
course_slug: "eeng-3345"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 8
weight: 80
slug: "laplace-transform"
links:
  - "/notes/engr-2341/fourier-system-response/"
  - "/notes/engr-2341/laplace-system-response/"
sources:
  - "Continuous-Time Systems Analysis Laplace Transform 1"
  - "Laplace transform"
  - "Laplace transform table (course handout)"
  - "System response"
generated: true
---

## Laplace Transform {#laplace-transform-1}
- Transforms differential equations into algebraic systems  
  - Solve the system and convert back to time domain  
- LT of a signal $x(t)$:  
  $$
  X(s) = \int_{-\infty}^{\infty} x(t) e^{-st} \, dt
  $$
- iLT of $X(s)$:  
  $$
  x(t) = \frac{1}{j 2 \pi} \int_{c - j\infty}^{c + j\infty} X(s) e^{st} \, ds
  $$
- Use the <cite class="cite">table of pairs and properties <span class="cite-src">[Laplace transform table (course handout)]</span></cite> to evaluate LT and iLT

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.1</span> <span class="theorem-callout-subtitle">(Find iLT of $\frac{7s - 6}{s^2 - s - 6}$)</span>.</div></div>
<div class="callout-content">

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-laplace-transform-2025-07-16-10-25-16.svg"><img src="/notes/excalidraw/08-laplace-transform-2025-07-16-10-25-16.svg" alt="08 Laplace Transform 2025-07-16 10.25.16" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.2</span> <span class="theorem-callout-subtitle">(Find iLT of $\frac{2s^2 + 5}{s^2 + 3s + 2}$)</span>.</div></div>
<div class="callout-content">

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-laplace-transform-2025-07-16-10-30-41.svg"><img src="/notes/excalidraw/08-laplace-transform-2025-07-16-10-30-41.svg" alt="08 Laplace Transform 2025-07-16 10.30.41" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.3</span> <span class="theorem-callout-subtitle">(Find iLT of $\frac{s+1}{s^2 + 5s + 6}$)</span>.</div></div>
<div class="callout-content">

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-laplace-transform-2025-07-16-10-48-07.svg"><img src="/notes/excalidraw/08-laplace-transform-2025-07-16-10-48-07.svg" alt="08 Laplace Transform 2025-07-16 10.48.07" loading="lazy"></a></figure>

</div>
</div>

## Solving Circuits Using Laplace Transform {#solving-circuits-using-laplace-transform}
### Transfer Function and System Response {#transfer-function-and-system-response}
- Take the Laplace transform of the system's equations including any nonzero initial conditions and solve for $Y(s)$  
- The $s$-domain output is:  
  $$
  Y(s) = H(s) X(s) + Y_{\text{IC}}(s)
  $$
- where:
	- $H(s)$ is the transfer function
	- $X(s)$ is the Laplace transform of the input signal
	- $Y_{\text{IC}}(s)$ is the Laplace terms resulting from the initial conditions
		- This is obtained by setting $X(s) = 0$
- Take the inverse Laplace transform to get the time-domain output:  
  $$
  y(t) = \mathcal{L}^{-1} \left\{ H(s) X(s) + Y_{\text{IC}}(s) \right\}
  $$
- This gives the total response as the sum of:
  - Zero-state response: 
    $$
    y_{\text{ZS}}(t) = \mathcal{L}^{-1} \left\{ H(s) X(s) \right\}
    $$
  - Zero-input response:
    $$
    y_{\text{ZI}}(t) = \mathcal{L}^{-1} \left\{ Y_{\text{IC}}(s) \right\}
    $$
- So the complete output is:
  $$
  y(t) = y_{\text{ZS}}(t) + y_{\text{ZI}}(t)
  $$

### Domain Transformation {#domain-transformation}
  - Transform the circuit into the $s$-domain equivalent circuit:
	  - Resistors remain unchanged
	  - Inductors and capacitors may be modeled as $s$-impedances in series with an ideal independent voltage source
		  - Capacitor: 

$$V_{C} = \frac{1}{sC}i + \frac{V_{0}}{s}$$

		  - Inductor: 

$$V_{L} = sL i - L i_{0}$$ 

  - Solve for variables in the $s$-domain using methods of circuit analysis
  - Apply inverse Laplace transform for time domain solution 

<a class="zoom" href="/notes/img/s-domain-circuit-transformation.png"><img src="/notes/img/s-domain-circuit-transformation.png" alt="s-domain circuit transformation" loading="lazy"></a>

### (Special Case of Above) Sinusoidal Steady-State Analysis {#special-case-of-above-sinusoidal-steady-state-analysis}
- Assume all sources are sinusoidal and operating at the same frequency  
- Transform the circuit into the phasor (frequency) domain  
- Replace $s$ with $j\omega$ to convert from Laplace to steady-state analysis  
- Replace elements with their steady-state impedances  
  - Resistor: $R$  
  - Inductor: $j\omega L$  
  - Capacitor: $\frac{1}{j\omega C}$  
- Use phasor circuit analysis to solve for voltages and currents  
- Convert phasor results back to time domain using  
  $$
  x(t) = \Re \left\{ \tilde{X} e^{j\omega t} \right\}
  $$
  where $\tilde{X}$ is the phasor representation of the signal

## Initial and Final Value Theorem {#initial-and-final-value-theorem}
- Useful so that you don't have to solve for initial and final conditions of current/voltage using transient analysis
- Using IVT/FVT, we may rewrite the complete response of a first-order circuit as:

$$
x(t) = \lim_{s \to 0} s X(s) + \left( \lim_{s \to \infty} s X(s) - \lim_{s \to 0} s X(s) \right) e^{-\frac{t}{\tau}}
$$

### Initial Value Theorem (IVT) {#initial-value-theorem-ivt}

$$
\lim_{t \to 0^+} f(t) = \lim_{s \to \infty} s F(s)
$$

**Requirements:**
- $f(t) \in \mathcal{L}\{f(t)\}$
- $\lim_{t \to 0^+} f(t) \in \mathbb{R}$
- $f(t) \not\ni \delta(t)$

### Final Value Theorem (FVT) {#final-value-theorem-fvt}

$$
\lim_{t \to \infty} f(t) = \lim_{s \to 0} s F(s)
$$

**Requirements:**
- $f(t) \in \mathcal{L}\{f(t)\}$
- $\lim_{t \to \infty} f(t) \in \mathbb{R}$
- Let $\mathcal{P}$ be the set of poles of $s F(s)$. Then:

$$
\forall p \in \mathcal{P} \setminus \{0\},\ \Re(p) < 0
$$

- $s = 0 \in \mathcal{P} \Rightarrow \operatorname{ord}_{s=0}(sF(s)) \le 1$

## References {#references}
- <span class="cite cite-ref">Continuous-Time Systems Analysis Laplace Transform 1 (course handout)</span>  
- <span class="cite cite-ref">Laplace transform (course handout)</span>  

- <div class="transclusion" data-source="04. Notes/Undergraduate Courses/ENGR 2341/20 Laplace System Response.md">
  <a class="transclusion-source" href="/notes/engr-2341/laplace-system-response/" title="Open Laplace System Response"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  ## System Response Using Laplace Transform {#system-response-using-laplace-transform-embed1}
  - Similar to <a class="internal-link" href="/notes/engr-2341/fourier-system-response/">Fourier System Response</a>, multiplication in the $s$-domain is convolution in the time domain
  - Take the product of the transfer function and the input in the $s$-domain, then take the inverse laplace transform

  $$y(t) = \mathcal{L}^{-1} \left[ H(s) \cdot X(s) \right]$$

  <a class="zoom" href="/notes/img/system-response-with-laplace-transform-example.png"><img src="/notes/img/system-response-with-laplace-transform-example.png" alt="system response with laplace transform example" loading="lazy"></a>

  ### Using LTI Properties {#using-lti-properties-embed1}
  - May leverage linearity property of LTI systems if the step/impulse response is already known 
  <a class="zoom" href="/notes/img/lti-linearity-property-laplace-system-response-example.png"><img src="/notes/img/lti-linearity-property-laplace-system-response-example.png" alt="LTI linearity property laplace system response example" loading="lazy"></a>

  ## Using MATLAB {#using-matlab-embed1}
  - Analytic response with symbolic toolbox
  <a class="zoom" href="/notes/img/analytic-response-with-symbolic-toolbox-laplace-transform-matlab.png"><img src="/notes/img/analytic-response-with-symbolic-toolbox-laplace-transform-matlab.png" alt="analytic response with symbolic toolbox laplace transform matlab" loading="lazy"></a>

  - Numeric response (convolution sum)
  <a class="zoom" href="/notes/img/numeric-response-using-convolution-sum-laplace-transform-matlab.png"><img src="/notes/img/numeric-response-using-convolution-sum-laplace-transform-matlab.png" alt="numeric response using convolution sum laplace transform matlab" loading="lazy"></a>

  - Numeric response using built-in functions (`impulse`, `step`, `lsim`)
  	- Easiest method possible
  <a class="zoom" href="/notes/img/numeric-response-using-builtin-functions-laplace-transform-matlab.png"><img src="/notes/img/numeric-response-using-builtin-functions-laplace-transform-matlab.png" alt="numeric response using builtin functions laplace transform matlab" loading="lazy"></a>

  ## References {#references-embed1}
  - <span class="cite cite-ref">System response (course handout)</span>

  </div>
