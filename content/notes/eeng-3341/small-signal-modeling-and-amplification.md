---
author: "Anish Goyal"
title: "Small-Signal Modeling and Amplification"
description: "Amplifiers use electronic devices that are in the active region"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3341"
date: 2025-10-16T23:56:07
modified: 2025-11-02T10:48:23
readingtime: "2"
course: "EENG 3341"
course_slug: "eeng-3341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 8
weight: 80
slug: "small-signal-modeling-and-amplification"
links: []
sources:
  - "Course slides, chapter 13: Small-Signal Modeling and Linear Amplification"
generated: true
---

## Amplifier Introduction {#amplifier-introduction}
- Amplifiers use electronic devices that are in the *active region*
	- BJTs can be amplifiers when biased in forward-active
	- FET can be amplifiers if in the pinch-off/saturation region
	- We refer to these regions as *active regions*, as the transistors can be used as linear amplification devices
- In these regions, transistors provide high voltage/current/power gains
	- We will be asked to determine the voltage gain and input/output resistance, which will help calculate the lower/upper cutoff frequencies of amplifiers
- Bias is needed to stabilize the Q-point in the desired operation region
- The Q-Point tells us some important characteristics about the amplifier:
	- Small-signal parameters
	- Voltage gain, input/output resistance
	- Max input/output signal amplifiers
	- Power consumption

## Small-Signal Parameters {#small-signal-parameters}
- If a solid-state device or transistor is operating at the Q-Point, then it acts as a linear circuit element for "small AC signals" near that Q-Point 
	- Small-signal condition for Diode/BJT: $v_d \le 5$ mV
	- Small-signal condition for MOSFET: $v_{gs} \le 0.2 V_{OD}$
- In this case, a diode can be modeled as a resistor with $R_D =\frac{1}{g_{d}}$, where $g_d$ is the diode conductance
	- Near the origin, $g_d =\frac{I_{S}}{V_{T}},$ so $R_D =\frac{V_{T}}{I_{S}}$

## Early Voltage {#early-voltage}
- Extrapolated intercept of the near-linear part of the output characteristic extended back to the voltage axis
	- Magnitude is $V_A$
- Physical interpretation: the variation of effective channel/base width with drain or collector voltage causes output current to rise with output voltage even at fixed inputs
- Provides finite output resistance in small-signal analysis

<a class="zoom" href="/notes/img/early-voltage.png"><img src="/notes/img/early-voltage.png" alt="early voltage" loading="lazy"></a>

## Small-Signal Models {#small-signal-models}

### BJT (Common-Emitter) {#bjt-common-emitter}
- The small-signal parameters, which are determined by the Q-Point are:
	- Transconductance: $g_m  = 40i_C$
	- Input resistance: $r_{\pi} = \frac{\beta_{o}}{g_m}$
	- Output resistance: $r_{o} = \frac{V_{A} + V_{CE}}{i_C}$

<a class="zoom" href="/notes/img/bjt-small-signal-model.png"><img src="/notes/img/bjt-small-signal-model.png" alt="BJT small signal model" loading="lazy"></a>

### MOSFET (Common-Source) {#mosfet-common-source}
- Small-signal parameters:
	- Transconductance: $g_{m} = \frac{2 I_{D}}{V_{OD}}$
	- Output resistance: $r_{o} = \frac{1 + \lambda V_{DS}}{\lambda I_{D}}$

<a class="zoom" href="/notes/img/mosfet-small-signal-model.png"><img src="/notes/img/mosfet-small-signal-model.png" alt="mosfet small signal model" loading="lazy"></a>

## Small-Signal Analysis {#small-signal-analysis}
1. Find the Q-Point via DC Analysis
2. Calculate small-signal parameters
3. Analyze the AC equivalent circuit using the Hybrid-Pi models

## References {#references}
- <span class="cite cite-ref">Course slides, chapter 13: Small-Signal Modeling and Linear Amplification</span>
