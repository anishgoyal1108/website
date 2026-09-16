---
author: "Anish Goyal"
title: "Digital Filter Design"
description: "Designed to have certain characteristics in the frequency domain"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-05-05T16:41:07
modified: 2025-05-05T19:16:13
readingtime: "2"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 24
weight: 240
slug: "digital-filter-design"
links:
  - "/notes/engr-2341/discrete-time-systems/"
sources: []
generated: true
---

## Digital Filters {#digital-filters}
- Designed to have certain characteristics in the frequency domain
- Advantages over analog filters:
	- Linear phase response
	- Robust to environmental changes (temperature)
	- Can be modified if implemented with a microprocessor or digitized
- Disadvantages over analog filters:
	- Speed limitation at high RF frequencies 
	- Noise generated from sampling and quantization

## FIR Vs IIR Filters {#fir-vs-iir-filters}

- Can find more at <a class="internal-link" href="/notes/engr-2341/discrete-time-systems/#fir-and-iir-filters">FIR and IIR Filters</a>

### FIR {#fir}
- Linear phase
- Always BIBO stable
- More robust to quantization of filter coefficients
- Difficult to design without CAD tools

### IIR {#iir}
- Nonlinear phase, especially at the edges of bands
- Not guaranteed to be BIBO stable
- Can be designed from analog filters (less difficult to design)
- Can process signals more quickly to meet higher frequency specifications

### Recommended Use Cases {#recommended-use-cases}
- FIR is recommended when you have a small number of filter coefficients and the phase distortion needs to be minimized
- IIR is recommended when sharp band edges are needed and the frequency is very high

## Filter Design Steps {#filter-design-steps}
1. Specify filter requirements
	- Frequency domain specs
	- Processing time
	- Implementation method
	- Cost of filter
2. Calculate filter coefficients
	- FIR coefficients determined using windowing, frequency sampling, or Parks-McClellan optimization method
	- IIR coefficients determined by transforming analog filters or using zero-pole placement
3. Verify the design meets specifications
4. Realize the design using a computer
5. Analyze the effect of finite word length on the performance
	- Check that the specifications met with filter coefficient quantization
6. Implement the filter in hardware/software
	- Need memory to store filter coefficients and present/past inputs/outputs, multipliers, and adders

## FIR Low Pass Filter Design Example {#fir-low-pass-filter-design-example}
<a class="zoom" href="/notes/img/fir-low-pass-filter-design-example-1.png"><img src="/notes/img/fir-low-pass-filter-design-example-1.png" alt="fir low pass filter design example 1" loading="lazy"></a>
<a class="zoom" href="/notes/img/fir-low-pass-filter-design-example-2.png"><img src="/notes/img/fir-low-pass-filter-design-example-2.png" alt="fir low pass filter design example 2" loading="lazy"></a>

## IIR Low Pass Filter Design Example {#iir-low-pass-filter-design-example}
<a class="zoom" href="/notes/img/iir-low-pass-filter-design-example-1.png"><img src="/notes/img/iir-low-pass-filter-design-example-1.png" alt="iir low pass filter design example 1" loading="lazy"></a>
<a class="zoom" href="/notes/img/iir-low-pass-filter-design-example-2.png"><img src="/notes/img/iir-low-pass-filter-design-example-2.png" alt="iir low pass filter design example 2" loading="lazy"></a>

## References {#references}
