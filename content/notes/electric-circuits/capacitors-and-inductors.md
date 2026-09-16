---
author: "Anish Goyal"
title: "Capacitors and Inductors"
description: "Passive element that stores energy in its E-field"
tags:
  - "notes"
  - "electrical-engineering"
  - "electric-circuits"
date: 2025-07-03T18:04:08
modified: 2025-07-04T00:36:52
readingtime: "3"
course: "Fundamentals of Electric Circuits (Sadiku)"
course_slug: "electric-circuits"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 6
weight: 60
slug: "capacitors-and-inductors"
links:
  - "/notes/electric-circuits/operational-amplifiers/"
sources: []
generated: true
---

## Capacitors {#capacitors}
- Passive element that stores energy in its E-field
- Consists of two conducting plates separated by a dielectric
- When a voltage source is connected to the capacitor, each plate stores a charge $q$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="06.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 06.1</span> <span class="theorem-callout-subtitle">(Capacitance)</span>.</div></div>
<div class="callout-content">

The ratio of a capacitor's plate charge to the potential difference between the plates, measured in farads (F):

$$q = Cv.$$

In practice, $C$ is dependent on neither $q$ or $v$; it is dependent on capacitor's physical dimensions (surface area, spacing, and permittivity). For a parallel plate capacitor:

$$ C = \frac{\epsilon A}{d}.$$

Two important properties:
1. Acts as an open circuit when the voltage is no longer changing with time; for ideal DC circuits, this occurs instantaneously.
2. The voltage across the capacitor is continuous.

</div>
</div>

- Taking the derivative of both sides:

$$ i = C \frac{\mathrm{d}v}{\mathrm{d}t}$$

- Taking the integral of that:

$$v = \frac{1}{C}\int_{t_{0}}^{t} i(\tau) \, \mathrm{d}\tau + v(t_{o})$$

- Power delivered:
	- If $p > 0$, the capacitor is charging (and vice-versa)

$$ p = vi = Cv \frac{\mathrm{d}v}{\mathrm{d}t}$$

- Energy stored:

$$w = \frac{1}{2}Cv^2 = \frac{q^2}{2C}$$

### Equivalent Capacitance {#equivalent-capacitance}
- Series:
	- Share $q$ and $i$

$$C_{\text{eq}} = \left(\sum_{n=1}^{N} \frac{1}{C_{n}}\right)^{-1}$$

- Parallel:

$$C_{\text{eq}} = \sum_{n = 1}^{N} C_{n}$$

## Inductors {#inductors}
- Passive element that stores energy in its B-field
- Consists of a coil of conducting wire
- If current passes through the inductor, the potential difference is directly proportional to the change in current

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="06.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 06.2</span> <span class="theorem-callout-subtitle">(Inductance)</span>.</div></div>
<div class="callout-content">

The property of an inductor to oppose the change of current through it, measured in henrys (H):

$$v = L \frac{\mathrm{d}i}{\mathrm{d}t}.$$

In practice, $L$ is dependent on neither $v$ nor $i$:

$$L = \frac{N^2 \mu A}{\ell},$$

where $N$ is the turns, $\ell$ is length, $A$ is cross-sectional area, and $\mu$ is permeability of the core.

Two important properties:
1. Acts as a closed circuit when the current is no longer changing with time; for ideal DC circuits, this occurs instantaneously.
2. The current through an inductor is continuous.

</div>
</div>

- Integrating both sides:

$$ i = \frac{1}{L} \int_{t_{0}}^{t} v(\tau) \, \mathrm{d}\tau + i(t_{0})$$

- Power delivered:

$$p = vi = \left( L \frac{\mathrm{d}i}{\mathrm{d}t} \right) i$$

- Energy stored:

$$w = \frac{1}{2} Li^2$$

### Equivalent Inductance {#equivalent-inductance}
- Series

$$L_{\text{eq}} = \sum_{n=1}^{N} L_{n}$$

- Parallel

$$L_{\text{eq}} = \left(\sum_{n=1}^{N} \frac{1}{L_{n}}\right)^{-1}$$

## Integrator and Differentiator {#integrator-and-differentiator}
### Integrator {#integrator}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="06.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 06.3</span> <span class="theorem-callout-subtitle">(Integrator)</span>.</div></div>
<div class="callout-content">

An <a class="internal-link" href="/notes/electric-circuits/operational-amplifiers/">op amp</a> with $v_o \propto \int v_{i}$ by replacing $R_f$ with a capacitor in an <a class="internal-link" href="/notes/electric-circuits/operational-amplifiers/#inverting-amplifier">inverting amplifier</a>.

$$ v_{o} = -\frac{1}{RC} \int_{0}^{t} v_{i}(\tau) \, \mathrm{d}\tau$$

</div>
</div>

<a class="zoom" href="/notes/img/integrator.png"><img src="/notes/img/integrator.png" alt="integrator" loading="lazy"></a>

### Differentiator {#differentiator}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="06.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 06.4</span> <span class="theorem-callout-subtitle">(Differentiator)</span>.</div></div>
<div class="callout-content">

An <a class="internal-link" href="/notes/electric-circuits/operational-amplifiers/">op amp</a> with $v_o \propto \frac{\mathrm{d}v_{i}}{\mathrm{d}t}$ by replacing $R_i$ with a capacitor in an <a class="internal-link" href="/notes/electric-circuits/operational-amplifiers/#inverting-amplifier">inverting amplifier</a>.

$$v_{o} = -RC \frac{\mathrm{d}v_{i}}{\mathrm{d}t}$$

</div>
</div>
