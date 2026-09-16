---
author: "Anish Goyal"
title: "Discrete Fourier Transform and Fast Fourier Transform"
description: "Takes x[n] and returns the corresponding X[k], where X[k] is the discrete spectrum with complex amplitudes corresponding to the discrete frequencies"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-03-27T08:22:51
modified: 2025-03-30T20:15:16
readingtime: "2"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 17
weight: 170
slug: "discrete-fourier-transform-and-fast-fourier-transform"
links: []
sources:
  - "Dft and fft"
generated: true
---

## DFT {#dft}
- Takes $x[n]$ and returns the corresponding $X[k]$, where $X[k]$ is the discrete spectrum with complex amplitudes corresponding to the discrete frequencies
- Numerical method for computing DTFT over a finite number of samples

$$X[k] = X\left(e^{j\hat{\omega_{k}}}\right) = \sum_{n=0}^{N-1}x[n]e^{-\hat{\omega_{k}}n}, \hat{\omega_{k}} = 2\pi k / N$$

$$X[k] = \sum_{n=0}^{N-1}x[n]e^{-j(2\pi k / N)n}, k=0, \dots, N-1$$

- Frequency resolution ($\Delta \hat{\omega} = \frac{2\pi}{N}$) is proportional to $N$ 
- First half are the complex amplitudes for $\hat{\omega_{k}} \gt 0$ and the second half are the complex amplitudes for $\hat{\omega_{k}} \lt 0$

### Inverse DFT {#inverse-dft}
Inverse DFT:

$$x[n] = \frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j(2 \pi k / N)n}, n \in [0, N-1]$$

Computing using DFT:

$$x[n] = \frac{1}{N}\left(\sum_{k=0}^{N-1}X^*[k]e^{-j(2 \pi k / N)n}\right)^*, n \in [0, N-1]$$

<a class="zoom" href="/notes/img/dft-example.png"><img src="/notes/img/dft-example.png" alt="dft example" loading="lazy"></a>
<a class="zoom" href="/notes/img/dft-example-2.png"><img src="/notes/img/dft-example-2.png" alt="dft example 2" loading="lazy"></a>

## FFT {#fft}
- Faster way to compute DFT
- Cooley-Turkey algorithm breaks an N-point DFT into smaller DFTs
- DFT requires $N^2$ complex multiplications and $N^2 - N$ complex additions to compute $X[k]$ for $x[n]$
- FFT requires $N\log_2(N) - N$ complex multiplications and $N\log_2(N)$ complex additions additions to compute $X[k]$ assuming $N$ is an integer power of 2

### MATLAB FFT {#matlab-fft}
- Use `fft` function will pad the signal with zeros or truncate the signal to match the number of points $N$
- The result is interpreted as follows:
	- The frequency resolution is $2\pi / N$
	- $X[k]$ is complex amplitude for $\hat{\omega}$
	- The amplitudes are scaled by $1 / N$ to match the two-sided spectrum

### Frequency Resolution for FFT {#frequency-resolution-for-fft}
- The waveform resolution of continuous-time frequencies is $\Delta R = 1 / T$ where T is the duration of the captured signal without padding
- The FFT resolution in terms of continuous-time frequency is $\Delta R = f_s / N$
- When choosing FFT size:
	- The waveform resolution needs to be smaller than the minimum distance between two frequencies
	- FFT resolution should be at least the waveform resolution
	- The frequencies of interest should not be split among several FFT points
- Zero padding can be used to make the signal length a power of 2 for better computation

<a class="zoom" href="/notes/img/frequency-resolution-for-fft-example.png"><img src="/notes/img/frequency-resolution-for-fft-example.png" alt="frequency resolution for fft example" loading="lazy"></a>

### Uses of FFT {#uses-of-fft}
- Spectrum of discrete-time signals

$$X[k] = FFT(x[n])$$

- Frequency response of discrete-time signals

$$H[k] = FFT(h[n])$$

- System response

$$y[n] = FFT^{-1}(Y[k]) = FFT^{-1}(FFT(h[n]) \cdot FFT(x[n]))$$

#### Sinusoidal System Response {#sinusoidal-system-response}
<a class="zoom" href="/notes/img/discrete-sinusoidal-system-response-example.png"><img src="/notes/img/discrete-sinusoidal-system-response-example.png" alt="discrete sinusoidal system response example" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Dft and fft (course handout)</span>
- [When to use DTFT vs DFT?](https://dsp.stackexchange.com/questions/10541/when-to-use-the-dtft-vs-the-dft-and-their-inverses-in-analysis)
- [Discrete Fourier transform](https://en.wikipedia.org/wiki/Discrete_Fourier_transform)
