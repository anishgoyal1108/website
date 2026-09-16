---
author: "Anish Goyal"
title: "Aliasing and Reconstruction"
description: "Discrete-time frequencies differing by 2 k have equal amplitudes and are considered aliases"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-03-12T18:42:53
modified: 2025-04-01T05:58:43
readingtime: "5"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 14
weight: 140
slug: "aliasing-and-reconstruction"
links:
  - "/notes/engr-2341/impulse-train/"
  - "/notes/engr-2341/nyquist-interval/"
  - "/notes/engr-2341/nyquist-rate/"
  - "/notes/engr-2341/principal-alias/"
sources:
  - "Aliasing and reconstruction"
generated: true
---

## Aliases {#aliases}
- Discrete-time frequencies differing by $2\pi k$ have equal amplitudes and are considered aliases
- Frequencies inside the <a class="internal-link" href="/notes/engr-2341/nyquist-interval/">Nyquist interval</a> are called <a class="internal-link" href="/notes/engr-2341/principal-alias/">principal aliases</a>
- There are an infinite number of aliases outside the <a class="internal-link" href="/notes/engr-2341/nyquist-interval/">Nyquist interval</a>
- Sinusoids with different frequencies can produce the identical discrete sequences
	- This occurs when $|f_1 - f_2| = k \cdot f_s$, which implies their <a class="internal-link" href="/notes/engr-2341/principal-alias/">principle aliases</a> coincide
	- This ambiguity can be avoided by sampling at the <a class="internal-link" href="/notes/engr-2341/nyquist-rate/">Nyquist rate</a> of the sinusoid with the greatest $f_\text{max}$

<a class="zoom" href="/notes/img/alias-sinusoidal-sampling-ambiguity.png"><img src="/notes/img/alias-sinusoidal-sampling-ambiguity.png" alt="alias sinusoidal sampling ambiguity" loading="lazy"></a>

<a class="zoom" href="/notes/img/sampling-aliases.png"><img src="/notes/img/sampling-aliases.png" alt="sampling aliases" loading="lazy"></a>

## Sampling in the Time Domain {#sampling-in-the-time-domain}
- <a class="internal-link" href="/notes/engr-2341/impulse-train/">Impulse trains</a> are used to retrieve continuous values at intervals of $T_s$
	- This is possible due to the sampling property of impulse

$$
\begin{align*}
x[n] &= x(t) \cdot \sum_{n=-\infty}^{\infty} \delta(t - nT_s) \\
&= \sum_{n=-\infty}^{\infty} x(nT_{s})\delta(t - nT_s)
\end{align*}
$$

- Therefore, $x[n] = x(nT_s)$, since the <a class="internal-link" href="/notes/engr-2341/impulse-train/">impulse train</a> samples $x(t)$ every $T_s$

## Sampling in the Frequency Domain {#sampling-in-the-frequency-domain}
- Multiplying $x(t)$ by an <a class="internal-link" href="/notes/engr-2341/impulse-train/">impulse train</a> in the time domain corresponds to convolution in the frequency domain
	- The spectrum of a sampled signal, $X_s(j\omega)$, is obtained by convolving $X(j\omega)$ with an <a class="internal-link" href="/notes/engr-2341/impulse-train/">impulse train</a>
	- The convolution causes periodic replications of $X(j\omega)$, spaced apart by $\omega_s$
	- The amplitude of each spectra is also scaled down by $\frac{1}{T_s}$

$$X_{s}(j\omega) = \frac{1}{T_{s}} \sum_{k=-\infty}^{\infty} X(j(\omega - k \omega_{s}))$$

- If the sampling frequency is less than the <a class="internal-link" href="/notes/engr-2341/nyquist-rate/">Nyquist rate</a>, the copies of the spectra will overlap

<a class="zoom" href="/notes/img/sampling-in-frequency-domain.png"><img src="/notes/img/sampling-in-frequency-domain.png" alt="sampling in frequency domain" loading="lazy"></a>

## Reconstruction {#reconstruction}
- The process of creating analog signals from samples using a reconstruction filter that extracts only the <a class="internal-link" href="/notes/engr-2341/principal-alias/">principal aliases</a> (only one copy of the repeated spectrum)

### Time Domain {#time-domain}
- In the time domain, this corresponds to replacing each sample with a weighted sinc pulse. When those pulses are summed together, it interpolates between the samples to reconstruct the analog signal
	- This is because the sinc function has a peak at $t = 0$ and decays as $t$ moves away from zero. When these sinc pulses centered at each sample point are summed together, a smooth, continuous function is obtained
	- In more practical applications, you use rectangular pulses instead of sinc

$$
h_r(t) = \frac{\sin\left(\frac{\omega_s}{2} t\right)}{\frac{\omega_s}{2} t}
$$

<a class="zoom" href="/notes/img/reconstruction-interpolation-time-domain.png"><img src="/notes/img/reconstruction-interpolation-time-domain.png" alt="reconstruction interpolation time domain" loading="lazy"></a>

### Frequency Domain {#frequency-domain}
- In the frequency domain, this corresponds to using a low-pass filter to extract the spectra inside the <a class="internal-link" href="/notes/engr-2341/nyquist-interval/">Nyquist interval</a>
	- Passes frequencies in the range $|\omega| \leq \frac{\omega_s}{2}$
	- Removes frequencies outside this range to eliminate aliasing

$$
H_r(j\omega) = T_s \left[ u\left(\omega + \frac{\omega_s}{2}\right) - u\left(\omega - \frac{\omega_s}{2}\right) \right]
$$

- In piecewise form:

$$
H_r(j\omega) =
\begin{cases}
T_s, & |\omega| \leq \frac{\omega_s}{2} \\
0, & |\omega| > \frac{\omega_s}{2}
\end{cases}
$$

<a class="zoom" href="/notes/img/reconstruction-interpolation-frequency-domain.png"><img src="/notes/img/reconstruction-interpolation-frequency-domain.png" alt="reconstruction interpolation frequency domain" loading="lazy"></a>

### Reconstruction Formulas {#reconstruction-formulas}
- The general form of reconstruction formula in the time domain is

$$y_r(t) = \sum_{n=-\infty}^{\infty} y[n] p(t - n T_s)$$

where $y[n]$ are the sampled values of the signal and $p(t)$ is a pulse function

#### Sinc Pulse {#sinc-pulse}
- The reconstruction formula using the sinc pulse is:

$$
y_r(t) = \sum_{n=-\infty}^{\infty} y[n] \cdot \text{sinc}\left( \frac{t - n T_s}{T_s} \right)
$$

- This sums over all the samples $y[n]$ and shifts each sinc pulse to the corresponding sample location $n T_s$
	- The resulting signal is a continuous-time signal that approximates the original analog signal

#### Rectangular Pulse {#rectangular-pulse}
- In practical applications, using an ideal sinc pulse is not feasible due to the infinite duration of the sinc function. Instead, a more commonly used approximation is a rectangular pulse, which is computationally simpler
- A rectangular pulse is defined as:

$$
p_{\text{rect}}(t) = \begin{cases} 
1, & |t| \leq \frac{T_s}{2} \\
0, & |t| > \frac{T_s}{2}
\end{cases}
$$

- This pulse has a finite duration of $T_s$ and is centered at each sample point. When we use this rectangular pulse to reconstruct the signal, we sum the shifted rectangular pulses weighted by the samples $y[n]$:

$$
y_{r}(t) = \sum_{n=-\infty}^{\infty} y[n] \cdot p_{\text{rect}}\left( \frac{t - n T_s}{T_s} \right)
$$

- This results in a piecewise constant approximation of the continuous signal, which is often used in digital-to-analog converters

#### Summary of both Methods {#summary-of-both-methods}
- **Sinc Pulse**: Ideal interpolation with infinite duration. This gives the best reconstruction, as it perfectly interpolates between samples and avoids any distortion
- **Rectangular Pulse**: Practical approximation with finite duration. This results in a piecewise constant reconstruction, which is easier to implement but introduces some distortion due to the abrupt transitions between samples, referred to at the Gibbs phenomenon

## Sampling and Reconstruction Process Overview {#sampling-and-reconstruction-process-overview}
- Sampling maps analog frequencies to discrete frequencies and replicates the discrete spectrum
- Signal bandwidth must be less than half of the <a class="internal-link" href="/notes/engr-2341/nyquist-rate/">Nyquist rate</a> to avoid aliasing while sampling
- Finite duration signals are not bandlimited, so practical signals must be filtered to remove frequency components greater than $\frac{f_s}{2}$ via bandlimiting
- Reconstruction filter extracts the principal aliases to reconstruct the smoothest signal corresponding to the samples, denoted $y(t)$

<a class="zoom" href="/notes/img/sampling-and-reconstruction-process-overview.png"><img src="/notes/img/sampling-and-reconstruction-process-overview.png" alt="sampling and reconstruction process overview" loading="lazy"></a>

<a class="zoom" href="/notes/img/sampling-and-reconstruction-example.png"><img src="/notes/img/sampling-and-reconstruction-example.png" alt="sampling and reconstruction example" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Aliasing and reconstruction (course handout)</span>
- Whittaker–Shannon interpolation formula - Wikipedia]
