---
author: "Anish Goyal"
title: "Op-Amps"
description: "Voltage gain:"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3345"
date: 2025-06-25T11:39:09
modified: 2025-07-01T10:06:30
readingtime: "2"
course: "EENG 3345"
course_slug: "eeng-3345"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 4
weight: 40
slug: "op-amps"
links: []
sources:
  - "Course handout 4: Applications of Operational Amplifiers in AC Circuits"
generated: true
---

## Introduction {#introduction}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="04.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 04.1</span> <span class="theorem-callout-subtitle">(Operational Amplifier)</span>.</div></div>
<div class="callout-content">

High-gain voltage amplifiers with differential inputs and a single-ended output. Features:
- High input impedance
- Low output impedance
- High gain
- Differential input

</div>
</div>

## Types of Op-Amps {#types-of-op-amps}

### Inverting Amplifier {#inverting-amplifier}
- Voltage gain:

$$ V_{\text{out}} = -V_{\text{in}}\frac{R_{f}}{R_{\text{in}}}$$

- Frequency response:

$$ V_{\text{out}} = -V_{\text{in}} \frac{Z_{f}}{Z_{\text{in}}}$$

<a class="zoom" href="/notes/img/inverting-amplifier-diagram.png"><img src="/notes/img/inverting-amplifier-diagram.png" alt="inverting amplifier diagram" loading="lazy"></a>

### Non-Inverting Amplifier {#non-inverting-amplifier}
- Voltage gain:

$$V_{\text{out}} = V_{\text{in}}\left(1+\frac{R_{f}}{R_{\text{in}}}\right)$$

- Frequency response:

$$V_{\text{out}} = V_{\text{in}}\left(1+\frac{Z_{f}}{Z_{\text{in}}}\right)$$

<a class="zoom" href="/notes/img/noninverting-amplifier-diagram.png"><img src="/notes/img/noninverting-amplifier-diagram.png" alt="noninverting amplifier diagram" loading="lazy"></a>

### Voltage Follower/Buffer {#voltage-follower-buffer}
- Voltage gain:

$$V_{\text{out}} = V_{\text{in}}$$

<a class="zoom" href="/notes/img/voltage-follower-diagram.png"><img src="/notes/img/voltage-follower-diagram.png" alt="voltage follower diagram" loading="lazy"></a>

### Differential Amplifier {#differential-amplifier}
- Voltage gain:

$$V_{\text{out}} = \frac{R_{f}}{R_{\text{in}}} \left(V_{2}-V_{1}\right)$$

<a class="zoom" href="/notes/img/differential-amplifier-diagram.png"><img src="/notes/img/differential-amplifier-diagram.png" alt="differential amplifier diagram" loading="lazy"></a>

### Integrator {#integrator}
- Voltage gain:

$$V_{\text{out}} = -\frac{1}{R_{\text{in}}C}\int V_{\text{in}} \, \mathrm{d}t$$

<a class="zoom" href="/notes/img/integrator-diagram.png"><img src="/notes/img/integrator-diagram.png" alt="integrator diagram" loading="lazy"></a>

### Differentiator {#differentiator}
- Voltage gain:

$$V_{\text{out}} = -R_{f}C \frac{\mathrm{d}V_{\text{in}}}{\mathrm{d}t}$$

<a class="zoom" href="/notes/img/differentiator-diagram.png"><img src="/notes/img/differentiator-diagram.png" alt="differentiator diagram" loading="lazy"></a>

## Filter Design {#filter-design}
- Types:
	- Low-pass, High-pass, Band-pass, Band-stop

$$V_{\text{out}} = -V_{\text{in}}\left(\frac{Z_{f}}{Z_{\text{in}}}\right)$$

### Low-Pass Filter Diagram {#low-pass-filter-diagram}
<a class="zoom" href="/notes/img/low-pass-filter-diagram.png"><img src="/notes/img/low-pass-filter-diagram.png" alt="low-pass filter diagram" loading="lazy"></a>

### High-Pass Filter Diagram {#high-pass-filter-diagram}
<a class="zoom" href="/notes/img/high-pass-filter-diagram.png"><img src="/notes/img/high-pass-filter-diagram.png" alt="high-pass filter diagram" loading="lazy"></a>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.2</span>.</div></div>
<div class="callout-content">

Inverting Amplifier Frequency Response Worked Out Example
<a class="zoom" href="/notes/img/inverting-op-amplifier-worked-out-example.png"><img src="/notes/img/inverting-op-amplifier-worked-out-example.png" alt="inverting op amplifier worked out example" loading="lazy"></a>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.3</span>.</div></div>
<div class="callout-content">

Non-Inverting Amplifier Frequency Response Worked Out Example

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-op-amps-2025-06-26-11-13-10.svg"><img src="/notes/excalidraw/04-op-amps-2025-06-26-11-13-10.svg" alt="04 Op-Amps 2025-06-26 11.13.10" loading="lazy"></a></figure>

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course handout 4: Applications of Operational Amplifiers in AC Circuits</span>
