---
author: "Anish Goyal"
title: "Digital Filtering"
description: "Sample the continuous signal"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-05-05T19:17:37
modified: 2025-05-05T19:23:53
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 23
weight: 230
slug: "digital-filtering"
links:
  - "/notes/engr-2341/nyquist-interval/"
  - "/notes/engr-2341/nyquist-rate/"
sources: []
generated: true
---

## Discrete-time Processing of Continuous-time Signals {#discrete-time-processing-of-continuous-time-signals}

### Overview {#overview}
1. Sample the continuous signal
2. Process the sampled signal to produce a discrete-time output
3. Reconstruct discrete-time output to create a continuous-time output

### More In-depth {#more-in-depth}
- Signal must be pre-filtered to make it bandlimited so that it can be sampled without aliasing
	- The pre-filter is an analog filter with a cutoff frequency less than the <a class="internal-link" href="/notes/engr-2341/nyquist-rate/">Nyquist rate</a>
	- The system response is only defined for the <a class="internal-link" href="/notes/engr-2341/nyquist-interval/">Nyquist interval</a>
- The analog to digital converter samples and quantizes the filtered signal
- The sampled signal is processed using a discrete-time system, typically a difference equation (FIR or IIR filter)
- The digital to analog converter reconstructs a continuous-time signal from the discrete-time output of the discrete-time system
- There may be analog post filtering done on the reconstructed signal

## Effective Frequency Response {#effective-frequency-response}
- The equivalent continuous-time frequency response corresponding to the effect of processing a continuous-time signal within a discrete-time signal
	- A mapping between discrete-time frequency response and continuous-time frequencies
	- Replace $\hat{\omega}$ with $\omega / f_s$
	
<a class="zoom" href="/notes/img/effective-frequency-response.png"><img src="/notes/img/effective-frequency-response.png" alt="effective frequency response" loading="lazy"></a>

### Example {#example}
<a class="zoom" href="/notes/img/effective-frequency-response-example.png"><img src="/notes/img/effective-frequency-response-example.png" alt="effective frequency response example" loading="lazy"></a>

## References {#references}
- 
