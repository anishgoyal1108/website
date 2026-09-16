---
author: "Anish Goyal"
title: "Solid-State Diodes and Diode Circuits"
description: "Circuit element that only permits current in one direction"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3341"
date: 2025-08-22T08:28:41
modified: 2025-09-30T20:54:09
readingtime: "2"
course: "EENG 3341"
course_slug: "eeng-3341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 3
weight: 30
slug: "solid-state-diodes-and-diode-circuits"
links: []
sources:
  - "Course slides, chapter 3: Solid-State Diode and Diode Circuits"
generated: true
---

## Diode {#diode}
- Circuit element that only permits current in one direction 
- Turn-on voltage is ~0.7 V at room temp

## Diode Current {#diode-current}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.1</span> <span class="theorem-callout-subtitle">(The Diode Equation)</span>.</div></div>
<div class="callout-content">

$$i_{D} = I_{S}\left[ \exp \left(\frac{q v_{S}}{nkT} \right) - 1 \right] = I_{S} \left[ \exp \left( \frac{v_{S}}{n V_{T}} \right)  \right]$$

where:
- $I_S$ = reverse saturation current (A)
- $v_S$ = voltage applied to diode (V)
- $q$ = fundamental charge unit (1.602e-19 C)
- $k$ = Boltzmann constant (1.38e-23 J/K)
- $T$ = absolute temperature (K)
- $n$ = non-ideality factor (dimensionless, usually assumed to be 1)
- $V_T$ = kT/q = thermal voltage (V) (25 mV at room temp)

</div>
</div>

### Diode Modes {#diode-modes}
- Reverse bias
	- $V_D < 0$
	- $i_{D} \approx -I_S$
- Zero bias
	- $V_D = 0$
	- $i_{D} \approx 0$
- Forward bias
	- $V_D = 0$
	- $i_{D} \approx I_S \exp \left( \frac{v_{D}}{nV_{T}} \right)$

## Reverse Breakdown {#reverse-breakdown}
- $i_D$ sharply increases with enough negative voltage in the reverse direction
	- This is called the breakdown voltage, $V_Z$

### Avalanche Breakdown {#avalanche-breakdown}
- As the E-field increases, the energy of charge carriers cause ionization of atoms, which turn into charge carriers and cause a positive feedback loop
- $V_Z$ = -5.6 V in normal silicon diodes

### Zener Breakdown {#zener-breakdown}
- The E-field is strong enough to tunnel electrons from covalent bonds through the depletion region
- Occurs at higher voltages than avalanche
- Allows for voltage regulation, since $V_D$

## Diode DC Analysis {#diode-dc-analysis}
- Find the quiescent operating point $(I_D, V_D)$ for the diode
- KVL equation characterizing diode behavior is known as the load line
	- Many methods to find the load line

$$v_{S} = I_{D}R + V_{D}$$

<a class="zoom" href="/notes/img/diode-circuit-analysis.png"><img src="/notes/img/diode-circuit-analysis.png" alt="diode circuit analysis" loading="lazy"></a>

### Load-Line Method {#load-line-method}
- Q-point is the graphical intersection of IV curve and load line 

### Mathematical Model {#mathematical-model}
- Numerically solve for Q-Point using Diode Equation and Load-Line

### Ideal Model {#ideal-model}
- Diode is a perfect switch when $v_S > 0.7$
- Unrealistic because the existence of a potential barrier implies that diodes must have a potential difference
	- Useful nonetheless since you can solve systems containing multiple diodes without much computational overhead (effectively becomes a 3SAT problem)

### Constant Voltage Drop Model {#constant-voltage-drop-model}
- $V_D = 0.7$ when $v_S > 0.7$
- More realistic because it accounts for the potential difference across the barrier

## References {#references}
- <span class="cite cite-ref">Course slides, chapter 3: Solid-State Diode and Diode Circuits</span>
