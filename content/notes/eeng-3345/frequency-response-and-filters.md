---
author: "Anish Goyal"
title: "Frequency Response and Filters"
description: "A function generator conducts a \"sweep\" of frequencies as input to circuit"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3345"
date: 2025-07-08T10:02:20
modified: 2025-07-14T11:35:47
readingtime: "7"
course: "EENG 3345"
course_slug: "eeng-3345"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 7
weight: 70
slug: "frequency-response-and-filters"
links:
  - "/notes/engr-2341/fourier-transform/"
  - "/notes/engr-2341/frequency-response/"
  - "/notes/engr-2341/laplace-transform/"
  - "/notes/engr-2341/transfer-functions/"
sources:
  - "Frequency Response and Filters 1"
  - "Frequency response"
  - "Transfer functions"
generated: true
---

## Determining Frequency Response Experimentally {#determining-frequency-response-experimentally}
- A function generator conducts a "sweep" of frequencies as input to circuit
- Spectrum analysis is shown in oscilloscope output
	- Typically, a bode plot of gain and phase

## Gain, Phase Shift, and Transfer Function {#gain-phase-shift-and-transfer-function}
- We may express the input/output of any circuit variable (voltage, current, power) as phasors, measuring the amplitude and phase
- The **frequency response** is characterized by:
	- *Gain* $(A_x)$: ratio of output and input amplitudes
	- *Phase shift* $(\phi_x)$: difference between output and input phases 
- Thus, we may define the **Transfer function**, $H(j \omega)$, as the ratio of the output and input phasors
	- Combines the above by characterizing the input-output relationship as a phasor (magnitude is gain and phase is phase shift)
	- May be used to determine the frequency response for sinusoidal inputs

$$H_(j\omega) = |H(j \omega)| \angle H(j \omega) = \frac{X_{\text{out}}(j \omega)}{X_{\text{in}}(j \omega)}$$

## Bode Plot {#bode-plot}
- Two subplots:
	1. Measures $|H|$ vs $\omega$
	2. Measures $\angle H$ vs $\omega$
- Uses a $\log_{10}$ $x$-axis scale
- The slope of $|H|$ at $\omega >> 0$ determines how quickly the magnitude of the signal changes for every tenfold increase in frequency, in dB/decade
	- "Decade" here means tenfold increase, not an actual decade of time
	- This gives an asymptotic line that can help you better graph the plot

<a class="zoom" href="/notes/img/bode-plot-example.png"><img src="/notes/img/bode-plot-example.png" alt="bode plot example" loading="lazy"></a>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.1</span>.</div></div>
<div class="callout-content">

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-frequency-response-and-filters-2025-07-08-10-47-47.svg"><img src="/notes/excalidraw/07-frequency-response-and-filters-2025-07-08-10-47-47.svg" alt="07 Frequency Response and Filters 2025-07-08 10.47.47" loading="lazy"></a></figure>

</div>
</div>

### MATLAB {#matlab}
- Sample HPF code:
```matlab
R = 1e4;
L = 10e-3;
C = 100e-6;
w = logspace(0, 5, 40);
temp = (w * L - 1 ./ (w*C));
gain = w*L ./ sqrt(R**2 + temp .^ 2);
phi = -atand(temp / R);
figure(1), semilogx(w, gain), grid;
figure(2), semilog(w, phi), grid;
```

## RLC Filters {#rlc-filters}
- RLC circuits effectively act as **bandpass filters** since they have two energy storage components (L and C).
- At the **resonant frequency** $\omega_0 = \frac{1}{\sqrt{LC}}$, the gain is **maximized** (typically normalized to unity in passive systems).

### Drop-off Frequencies {#drop-off-frequencies}
- Defined as the frequencies where the gain drops to **-3 dB** from the peak (i.e., $\frac{1}{\sqrt{2}}$ of max).
- For a standard series RLC:
  - **High drop-off frequency**: $\omega_{\text{high}} = \omega_0 + \frac{R}{2L}$
  - **Low drop-off frequency**: $\omega_{\text{low}} = \omega_0 - \frac{R}{2L}$
  - Approximate bandwidth: $\Delta \omega = \omega_{\text{high}} - \omega_{\text{low}} = \frac{R}{L}$
- In terms of simpler low/high-frequency approximations:
  - High drop-off: $\frac{R}{L}$
  - Low drop-off: $\frac{1}{RC}$

### Cutoff Frequencies {#cutoff-frequencies}
- Defined here as the frequencies where gain drops to **-20 dB** (i.e., 10 times further from the peak than -3 dB).
- Rule-of-thumb estimations:
  - **High cutoff**: $\omega_{\text{cutoff, high}} = 10 \cdot \frac{R}{L}$
  - **Low cutoff**: $\omega_{\text{cutoff, low}} = \frac{1}{10RC}$

## Generalized Second-Order Circuits with Complex Roots {#generalized-second-order-circuits-with-complex-roots}
- Only applicable to *underdamped* systems where the characteristic equation has complex roots
- The general form of the transfer function is:

$$
H(j \omega) = \frac{k}{1 - \left( \frac{\omega}{\omega_0} \right)^2 + j 2\zeta \left( \frac{\omega}{\omega_0} \right)}
$$

where $\zeta = \frac{\alpha}{\omega_{0}}$

- Behavior depends on how $\omega$ compares to the natural frequency $\omega_0$:

### Three Subcases: {#three-subcases}
1. **Low-frequency regime**: $\omega \ll \omega_0$
   - Magnitude: $|H| \approx k$
   - Phase: $\angle H \approx 0^\circ$
2. **At resonance**: $\omega = \omega_0$
   - Magnitude: $|H| = \frac{k}{2\zeta}$
   - Phase: $\angle H = -90^\circ$
3. **High-frequency regime**: $\omega \gg \omega_0$
   - Dominant term is $-\left( \frac{\omega}{\omega_0} \right)^2$ in the denominator
   - Magnitude: $|H| \approx \frac{k \omega_0^2}{\omega^2}$ (i.e., rolls off as $1/\omega^2$)
   - Phase: $\angle H \approx -180^\circ$

## General Second-Order Transfer Function Decomposition {#general-second-order-transfer-function-decomposition}
- All second-order circuits can be written as a transfer function in "standard form":
	- If it is not already in this form, you must perform partial fraction decomposition

$$
H(j\omega) = \frac{k}{(1 + j \omega / p_1)(1 + j \omega / p_2)}
$$

- This overall transfer function may be broken down as the product of three simpler transfer functions:

$$H(j \omega) = H_{1}(j \omega)H_{2}(j \omega)H_{3}(j \omega)$$

where
  - $H_1 = k$
  - $H_2 = \frac{1}{1 + j \omega / p_1}$
  - $H_3 = \frac{1}{1 + j \omega / p_2}$

- Each of these simpler transfer functions corresponds to a first-order low-pass filter or a gain term
- $p_1$ and $p_2$ are the pole frequencies of the system (complex conjugates in the underdamped case, real in overdamped)
- The expression $1 + j \omega / p_i$ is not the pole itself, but a standard form for expressing frequency-domain behavior near that pole

### Log-Magnitude Decomposition {#log-magnitude-decomposition}
- The overall magnitude in decibels is the sum of the magnitudes:

$$
\begin{align*}
|H(j\omega)|_{dB} &= 20 \log_{10}(|H_1|) + 20 \log_{10}(|H_2|) + 20 \log_{10}(|H_3|) \\
&= 20 \log_{10}(k) - 20 \log_{10}\left(\sqrt{1 + \left(\frac{\omega}{p_1}\right)^2}\right) - 20 \log_{10}\left(\sqrt{1 + \left(\frac{\omega}{p_2}\right)^2}\right)
\end{align*}
$$

## References {#references}

- <div class="transclusion" data-source="04. Notes/Undergraduate Courses/ENGR 2341/19 Transfer Functions.md">
  <a class="transclusion-source" href="/notes/engr-2341/transfer-functions/" title="Open Transfer Functions"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  ## Transfer (System) Functions {#transfer-system-functions-embed1}
  - The ratio of the <a class="internal-link" href="/notes/engr-2341/laplace-transform/">Laplace transform</a> of the system output to the Laplace transform of the system input

  $$H(s) = \frac{Y(s)}{X(s)}$$

  - Can also be determined by taking the Laplace transform of the impulse response or from differential equations describing the system

  $$H(s) = \int_{-\infty}^{\infty}h(t)e^{-st} \ \mathrm{d}t$$

  ## Poles and Zeros {#poles-and-zeros-embed1}
  - Roots of $Y(s)$ are the system zeros
  - Roots of $X(s)$ are the system poles ($\mathcal{P}$)

  $$\forall p \in \mathcal{P}, \Re(p) < 0 \implies \int_{-\infty}^{\infty} |h(t)| \, dt < \infty \implies \text{BIBO stability}$$

  <a class="zoom" href="/notes/img/poles-and-bibo-stability-example.png"><img src="/notes/img/poles-and-bibo-stability-example.png" alt="poles and bibo stability example" loading="lazy"></a>
  <a class="zoom" href="/notes/img/transfer-functions-example.png"><img src="/notes/img/transfer-functions-example.png" alt="transfer functions example" loading="lazy"></a>

  ## References {#references-embed1}
  - <span class="cite cite-ref">Transfer functions (course handout)</span>

  </div>

- <div class="transclusion" data-source="04. Notes/Undergraduate Courses/ENGR 2341/10 Frequency Response.md">
  <a class="transclusion-source" href="/notes/engr-2341/frequency-response/" title="Open Frequency Response"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  ## Continuous-time Systems {#continuous-time-systems-embed2}
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

  ## Frequency Response {#frequency-response-1-embed2}
  - Describes what the system does to sinusoidal inputs
  - Broken down into magnitude and phase components

  $$H(j\omega) = \vert H(j\omega) \vert \angle H(j\omega)$$

  - Determined using the <a class="internal-link" href="/notes/engr-2341/fourier-transform/">Fourier transform</a> of $h(t)$

  $$H(j\omega) = \int_{-\infty}^{\infty}h(t)e^{-j\omega t} \ \mathrm{d}t$$

  ### Analysis of $H(j\omega)$ {#analysis-of-h-j-embed2}
  Let $H(j\omega)$ be a general frequency response function of the form $H(jω)= \frac{N(j\omega)}{D(j\omega)}$. Then:
  - $|H(j\omega)| = \frac{|N(j\omega)|}{|D(j\omega)|}$
  - $H(j\omega) = \angle N(j\omega) - \angle D(j\omega)$

  #### Magnitude Calculation {#magnitude-calculation-embed2}
  - If $M(j\omega) = A e^{j\phi(\omega)}$, $|M(j\omega)| = A$
  - If $M(j\omega) = a + j b(\omega)$, $|M(j\omega)| = \sqrt{a^2 + b(\omega)^2}$

  #### Phase Calculation {#phase-calculation-embed2}
  - If $M(j\omega) = A e^{j\phi(\omega)}$, $\angle M(j\omega) = \phi(\omega)$
  - If $M(j\omega) = a + j b(\omega)$, $\angle M(j\omega) = \tan^{-1}\left(\frac{b(\omega)}{a}\right)$

  ## Sinusoidal Response {#sinusoidal-response-embed2}
  - Response to sinusoids for an LTI system is a sinusoid of the same frequency with a shifted amplitude (gain) and phase, dependent on $H(j\omega)$
  - Frequencies of the sinusoidal components cannot change and it must be two-sided
  - Input format $x(t)$:

  $$x(t) = A_{0} + \sum_{k=1}^{N}A_{k}\cos(\omega_{k}t + \phi_{k})$$

  - Output format $y(t)$:

  $$y(t) = \vert H(j0) \vert A_{0} + \sum_{k=1}^{N} \vert H(j\omega_{k}) \vert A_{k} \cos(\omega_{k}t + \phi_{k} + \angle H(j\omega_{k}))$$

  <a class="zoom" href="/notes/img/sinusoidal-response-example.png"><img src="/notes/img/sinusoidal-response-example.png" alt="sinusoidal response example" loading="lazy"></a>

  ## References {#references-embed2}
  - <span class="cite cite-ref">Frequency response (course handout)</span>

  </div>

- <span class="cite cite-ref">Frequency Response and Filters 1 (course handout)</span>
- [Construction of Bode Diagrams](https://lpsa.swarthmore.edu/Bode/BodeRules.html)
- [Drawing Bode Diagrams](https://lpsa.swarthmore.edu/Bode/BodeReviewRules.html)
