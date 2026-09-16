---
author: "Anish Goyal"
title: "AC Steady State Power, Mutual Inductance, Ideal Transformer"
description: "For v(t) and i(t) we use RMS; for p(t), we use average"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3345"
date: 2025-07-01T10:04:29
modified: 2025-07-21T10:40:23
readingtime: "4"
course: "EENG 3345"
course_slug: "eeng-3345"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 5
weight: 50
slug: "ac-steady-state-power-mutual-inductance-ideal-transformer"
links: []
sources:
  - "AC Steady-State Power, Mutual Inductance, and"
  - "Alexander & Sadiku, Fundamentals of Electric Circuits"
generated: true
---

## RMS and Average Quantities {#rms-and-average-quantities}
- For $v(t)$ and $i(t)$ we use RMS; for $p(t)$, we use average

$$V_{\text{rms}} = \sqrt{\frac{1}{2\pi}\int_{0}^{2\pi} v^2(t) \, \mathrm{d}t} = \frac{V_{m}}{\sqrt{2}}$$

$$I_{\text{rms}} = \frac{I_{m}}{\sqrt{2}}$$

$$\begin{align}
P_{\text{avg}} &= \frac{1}{T}\int_{0}^{T} p(t) \, \mathrm{d}t  \\
&= \frac{V_{m}I_{m}}{2}\cos(\theta_{v} - \theta_{i}) \\
&= \frac{V_{m}I_{m}}{2}\cos(\phi)
\end{align}$$

- For purely resistive loads, $p_{\text{avg}} = V_{\text{rms}} I_{\text{rms}}$
- For purely reactive loads (inductor/capacitor), $p_{\text{avg}} = 0$
- $\phi$ is the phase between V and I

## Types of Electric Power {#types-of-electric-power}
- ALWAYS USE RMS VALUES FOR CURRENT AND VOLTAGE OR YOU WILL GET THE QUESTION WRONG!
- Real/Active Power $(P)$: Actual power consumed, measured in watts (W)

$$\begin{align}
P &= V I \cos(\phi_{V_{C}}-\phi_{I_{C}}) \\
&= VI\cos(\phi) \\
&= \Re(VI^*)
\end{align}$$

- Reactive Power $(Q)$: Power stored/released by inductors and capacitors, measured in Volt-Amps-Reactive (VAR)

$$\begin{align}
Q &= V I \sin(\phi_{V_{C}}-\phi_{I_{C}}) \\
&= VI\sin(\phi) \\
&= \mathrm{Im}(V I^*)
\end{align}$$

- Apparent Power $(|S|)$: Combination of reactive power and true power, measured in Volt-Amps (VA)
	- Magnitude of complex power, $S$

$$\begin{align}
|S| &= |V||I| \\
&= |V I^*|
\end{align}$$

<a class="zoom" href="/notes/img/power-triangle.png"><img src="/notes/img/power-triangle.png" alt="power triangle" loading="lazy"></a>

## Complex Power {#complex-power}
- Shows the total power running through the AC circuit, measured in Volt-Amps

$$\begin{align}
S &= P + jQ \\
&= V I^*
\end{align}$$

$$ |S| = \sqrt{P^2 + Q^2}$$

## Power Factor {#power-factor}
- Ratio of real power to apparent power
- Shows how effectively electrical power is being used

$$PF = \frac{P}{|S|}$$

## Mutual Inductance {#mutual-inductance}
- The property of two coils or inductors that enables energy transfer through a shared magnetic field
- When the current in one coil changes, it generates a time-varying magnetic field that links with the second coil, inducing an emf
- Dependent on
  - The number of turns in each coil
  - The core material (permeability)
  - The geometrical arrangement of the coils
  - The degree of magnetic coupling

- Magnetic flux linkage definition:

$$
M = \frac{N_2 \Phi_{21}}{I_1} = \frac{N_1 \Phi_{12}}{I_2}
$$

Where:
- $M$ is the mutual inductance in Henries (H)
- $\Phi_{21}$ is the magnetic flux in coil 2 due to current in coil 1
- $\Phi_{12}$ is the magnetic flux in coil 1 due to current in coil 2
- $N_1, N_2$ are the number of turns in coils 1 and 2
- $I_1, I_2$ are the respective coil currents

- Induced voltage in coil 1 from changing current in coil 2:

$$
\varepsilon_1 = M \frac{dI_2}{dt}
$$

- Induced voltage in coil 2 from changing current in coil 1:

$$
\varepsilon_2 = M \frac{dI_1}{dt}
$$

- When the two coils are part of the same circuit, the mutual inductance also affects the total voltage across each inductor

- Voltage across the first inductor:

$$
v_1 = L_1 \frac{di_1}{dt} \pm M \frac{di_2}{dt}
$$

- Voltage across the second inductor:

$$
v_2 = L_2 \frac{di_2}{dt} \pm M \frac{di_1}{dt}
$$

- The sign depends on the relative orientation of the coils, determined by the **dot convention**
	- A positive sign is used if current enters the dotted terminal of both coils and negative otherwise

## Ideal Transformer {#ideal-transformer}
- Theoretical device that models perfect magnetic coupling between two coils to step up or step down voltage/current while maintaining constant apparent power. It assumes:
	- No energy losses (no winding resistance, no core losses)
	- Perfect magnetic coupling (coupling coefficient $k = 1$)
	- All magnetic flux produced by the primary winding links with the secondary winding
	- Infinite core permeability (zero magnetizing current)

- An ideal transformer is used to:
	- Match impedances
	- Change voltage levels between circuits
	- Isolate different parts of a system electrically

- Turns ratio definition:

$$
\frac{N_1}{N_2} = a
$$

Where $a$ is the turns ratio (primary to secondary).

- Voltage transformation:

$$
\frac{V_1}{V_2} = \frac{N_1}{N_2}
$$

- Current transformation:

$$
\frac{I_1}{I_2} = \frac{N_2}{N_1}
$$

- Conservation of power:

$$
V_1 I_1 = V_2 I_2
$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.1</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 13.1</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;585]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-ac-steady-state-analysis-mutual-inductance-ideal-transformer-2025-07-07-08-01-13.svg"><img src="/notes/excalidraw/05-ac-steady-state-analysis-mutual-inductance-ideal-transformer-2025-07-07-08-01-13.svg" alt="05 AC Steady State Analysis, Mutual Inductance, Ideal Transformer 2025-07-07 08.01.13" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.2</span>.</div></div>
<div class="callout-content">

(From Quiz 3 - Ch11)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-ac-steady-state-analysis-mutual-inductance-ideal-transformer-2025-07-07-08-32-49.svg"><img src="/notes/excalidraw/05-ac-steady-state-analysis-mutual-inductance-ideal-transformer-2025-07-07-08-32-49.svg" alt="05 AC Steady State Analysis, Mutual Inductance, Ideal Transformer 2025-07-07 08.32.49" loading="lazy"></a></figure>

</div>
</div>

## References {#references}
- <span class="cite cite-ref">AC Steady-State Power, Mutual Inductance, and (course handout)</span>
