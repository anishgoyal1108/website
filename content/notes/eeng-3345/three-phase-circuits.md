---
author: "Anish Goyal"
title: "Three-Phase Circuits"
description: "Balanced condition: V{aa^{'}} + V{bb^{'}} + V{cc^{'}} 0"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3345"
date: 2025-07-02T10:02:27
modified: 2025-07-07T09:10:06
readingtime: "3"
course: "EENG 3345"
course_slug: "eeng-3345"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 6
weight: 60
slug: "three-phase-circuits"
links: []
sources:
  - "Three-Phase Circuits"
generated: true
---

## Three-Phase Circuits {#three-phase-circuits-1}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="06.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 06.1</span> <span class="theorem-callout-subtitle">(Three-Phase Voltages)</span>.</div></div>
<div class="callout-content">

Consists of three sinusoidal voltages of equal magnitude but phase-shifted by $120^{\circ}$. Advantage: constant power transmission.

</div>
</div>

- Balanced condition: $V_{aa^{'}} + V_{bb^{'}} + V_{cc^{'}} = 0$
	- This also implies the resistive loads in each branch are the same, since the potential at each point is identical
- For notational simplicity: $V_{aa^{'}} = V_a$ and so forth

<a class="zoom" href="/notes/img/line-to-line-and-phase-voltages.png"><img src="/notes/img/line-to-line-and-phase-voltages.png" alt="line to line and phase voltages" loading="lazy"></a>

- For any balanced bridge circuit, the phase voltages should be the same

## Current Relationships {#current-relationships}
- Line currents: $I_a, I_b, I_c$
- Phase currents: $I_{ab}, I_{bc}, I_{ca}$
- Phase to line current: $I_{m}\sqrt{3} \angle -30^{\circ}$

$$\begin{align}
I_{ab} &= I_{m} \cos \omega t \\
&= I_{m} \angle 0^{\circ} \\
I_{bc} &= I_{m} \cos(\omega t - 120^{\circ}) \\
&= I_{m} \angle -120^{\circ} \\
I_{ca} &= I_{m} \cos(\omega t + 120^{\circ}) \\
&= I_{m} \angle 120^{\circ}
\end{align}$$

- For Delta Configuration:

$$I_{a} = I_{ab} - I_{ca} = \sqrt{3} I_{m} \angle -30^{\circ}$$

<a class="zoom" href="/notes/img/current-triangle.png"><img src="/notes/img/current-triangle.png" alt="current triangle" loading="lazy"></a>

## Voltage Relationships {#voltage-relationships}
- Line voltages: $V_{ab}, V_{bc}, V_{ca}$
- Phase voltages: $V_a, V_b, V_c$
- Phase to line voltage: $V_{m} \sqrt{3} \angle 30^{\circ}$

Line voltages:

$$\begin{align}
V_{aa^{'}} &= V_{m}\cos \omega t  \\
&= Vm \angle 0^{\circ}\\
V_{bb^{'}} &= V_{m}\cos(\omega t - 120^{\circ}) \\
&= Vm \angle -120^{\circ}\\
V_{cc^{'}} &= V_{m}\cos(\omega t - 240^{\circ}) \\
&= Vm \angle 120^{\circ}\\
\end{align}$$

- For Delta Configuration:

$$V_{ab} = V_{a} - V_{b} = \sqrt{3} V_{m} \angle 30^{\circ}$$

<a class="zoom" href="/notes/img/voltage-triangle.png"><img src="/notes/img/voltage-triangle.png" alt="voltage triangle" loading="lazy"></a>

## Bridge Circuits {#bridge-circuits}
### Y-to-Y Circuit {#y-to-y-circuit}
- Three voltage sources connected in a Y configuration to three impedances in a Y configuration
- Assuming the voltage sources are three-phase and the impedances match, then the neutral current in the middle $i_N$ is zero
- Otherwise, use nodal analysis to determine the currents
- Phase currents equal line currents

<a class="zoom" href="/notes/img/y-to-y-circuit.png"><img src="/notes/img/y-to-y-circuit.png" alt="y to y circuit" loading="lazy"></a>

### D-to-D Circuit {#d-to-d-circuit}
- Three voltage sources connected in a D configuration to three impedances in a D configuration
- The current through each impedance is the corresponding voltage source times the admittance

<a class="zoom" href="/notes/img/d-to-d-circuit.png"><img src="/notes/img/d-to-d-circuit.png" alt="d to d circuit" loading="lazy"></a>

### Y-to-D Circuit {#y-to-d-circuit}
- Use KCL and KVL

<a class="zoom" href="/notes/img/y-to-d-circuit.png"><img src="/notes/img/y-to-d-circuit.png" alt="y to d circuit" loading="lazy"></a>

## Power {#power}
- Total real power (balanced load)

$$P_{\text{total}} = \sqrt{3} V_{L} I_{L} \cos(\phi)$$

- Apparent power:

$$ |S| = \sqrt{3} V_{L} I_{L}$$

- Reactive power:

$$ Q = \sqrt{3} V_{L} I_{L}\sin(\phi)$$

## Examples {#examples}

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="06.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 06.2</span>.</div></div>
<div class="callout-content">

In a purely resistive circuit, the voltage and current are:

$$v(t) = 230\cos(\omega t), i(t) = 10\cos(\omega t)$$

- Calculate the **real power** consumed by the circuit
- Determine the **apparent power**
- What is the **power factor**?

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/06-three-phase-circuits-2025-07-02-11-27-11.svg"><img src="/notes/excalidraw/06-three-phase-circuits-2025-07-02-11-27-11.svg" alt="06 Three-Phase Circuits 2025-07-02 11.27.11" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="06.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 06.3</span>.</div></div>
<div class="callout-content">

A balanced Y-Y system has a phase voltage $V_{ph} = 120V$ and resistive load $Z = 10\Omega$. Find the line current and the total power consumed.

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/06-three-phase-circuits-2025-07-03-09-46-08.svg"><img src="/notes/excalidraw/06-three-phase-circuits-2025-07-03-09-46-08.svg" alt="06 Three-Phase Circuits 2025-07-03 09.46.08" loading="lazy"></a></figure>

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Three-Phase Circuits (course handout)</span>
