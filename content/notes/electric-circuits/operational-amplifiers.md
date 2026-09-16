---
author: "Anish Goyal"
title: "Operational Amplifiers"
description: "Any input applied to the inverting terminal will appear inverted at the output"
tags:
  - "notes"
  - "electrical-engineering"
  - "electric-circuits"
date: 2025-06-26T11:41:46
modified: 2025-07-03T01:20:07
readingtime: "7"
course: "Fundamentals of Electric Circuits (Sadiku)"
course_slug: "electric-circuits"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 5
weight: 50
slug: "operational-amplifiers"
links: []
sources:
  - "Alexander & Sadiku, Fundamentals of Electric Circuits"
generated: true
---

## Operational Amplifiers {#operational-amplifiers-1}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="05.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 05.1</span> <span class="theorem-callout-subtitle">((Non-Ideal) Operational Amplifier)</span>.</div></div>
<div class="callout-content">

An active circuit element designed to perform mathematical operations of additional, subtraction, multiplication, division, differentiation, and integration. Consists of:
- Two inputs: inverting input $v_1$ and non-inverting input $v_2$
- Two power supplies: $V^+$ and $V^-$
- Input resistor $R_i$ with voltage drop $v_d$
- Voltage-controlled voltage source equal to $A v_d$
- Output resistor $R_o$
- Output terminal $v_0$

</div>
</div>

- Any input applied to the inverting terminal will appear inverted at the output
- The differential voltage input $v_d$ (voltage across $R_{i}$) is given by $v_{2}-v_{1}$
	- Therefore, the output voltage $v_{o}$ which is equal to the voltage of the VCVS, is given by $Av_d = A(v_{2}-v_{1})$, where $A$ is the *open-loop gain*
	- When there is feedback, the ratio $\frac{v_{o}}{v_{d}}$ is called the *closed-loop gain*
- Practically, $v_o \le |V_{\text{CC}}|$, which means there are three modes of operation:
	1. Positive saturation $(v_o = V_{\text{CC}})$
	2. Linear range $(-V_{\text{CC}} \le v_o = Av_{d} \le V_{\text{CC}})$
	3. Negative saturation $(v_{o} = -V_{\text{CC}})$
- We always assume that the op amps are linear and $v_o \in [-V_{\text{CC}}, V_{\text{CC}}]$

### Pin Configuration {#pin-configuration}
<a class="zoom" href="/notes/img/op-amp-pin-configuration.png"><img src="/notes/img/op-amp-pin-configuration.png" alt="op amp pin configuration" loading="lazy"></a>

### Circuit Symbol {#circuit-symbol}
<a class="zoom" href="/notes/img/op-amp-circuit-symbol.png"><img src="/notes/img/op-amp-circuit-symbol.png" alt="op amp circuit symbol" loading="lazy"></a>

### Circuit Symbol With Power {#circuit-symbol-with-power}
- By KCL, $i_o = i_{1} + i_{2} + i_{+} + i_{-}$
<a class="zoom" href="/notes/img/op-amp-circuit-symbol-with-power.png"><img src="/notes/img/op-amp-circuit-symbol-with-power.png" alt="op amp circuit symbol with power" loading="lazy"></a>

### Non-Ideal Op Amp {#non-ideal-op-amp}
<a class="zoom" href="/notes/img/nonideal-op-amp-diagram.png"><img src="/notes/img/nonideal-op-amp-diagram.png" alt="nonideal op amp diagram" loading="lazy"></a>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.2</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 5.1</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;203]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-operational-amplifiers-2025-07-01-22-29-22.svg"><img src="/notes/excalidraw/05-operational-amplifiers-2025-07-01-22-29-22.svg" alt="05 Operational Amplifiers 2025-07-01 22.29.22" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.3</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 5.1</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;204]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-operational-amplifiers-2025-07-01-23-39-15.svg"><img src="/notes/excalidraw/05-operational-amplifiers-2025-07-01-23-39-15.svg" alt="05 Operational Amplifiers 2025-07-01 23.39.15" loading="lazy"></a></figure>

</div>
</div>

## Ideal Op Amp {#ideal-op-amp}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="05.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 05.4</span> <span class="theorem-callout-subtitle">(Ideal Operational Amplifier)</span>.</div></div>
<div class="callout-content">

An op amp is considered ideal if it has:
- Infinite open-loop gain
- Infinite input resistance
- Zero output resistance

</div>
</div>

- This means: 
	- The op amp has zero current in both input terminals (*i.e.,* they are open circuits)
	- The voltage across the terminals, $v_d$, equals 0, which means $v_1 = v_2$

<a class="zoom" href="/notes/img/ideal-op-amp.png"><img src="/notes/img/ideal-op-amp.png" alt="ideal op amp" loading="lazy"></a>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.5</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 5.2</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;205]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-operational-amplifiers-2025-07-02-20-44-24.svg"><img src="/notes/excalidraw/05-operational-amplifiers-2025-07-02-20-44-24.svg" alt="05 Operational Amplifiers 2025-07-02 20.44.24" loading="lazy"></a></figure>

</div>
</div>

## Op Amp Configurations {#op-amp-configurations}
### Inverting Amplifier {#inverting-amplifier}
- Reverses the polarity of the input signal while amplifying it

$$v_{o} = -\frac{R_{f}}{R_{1}}v_{i}$$

<a class="zoom" href="/notes/img/inverting-amplifier.png"><img src="/notes/img/inverting-amplifier.png" alt="inverting amplifier" loading="lazy"></a>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.6</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 5.3</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;206]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-operational-amplifiers-2025-07-02-21-23-03.svg"><img src="/notes/excalidraw/05-operational-amplifiers-2025-07-02-21-23-03.svg" alt="05 Operational Amplifiers 2025-07-02 21.23.03" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.7</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 5.3</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;206]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-operational-amplifiers-2025-07-02-21-26-36.svg"><img src="/notes/excalidraw/05-operational-amplifiers-2025-07-02-21-26-36.svg" alt="05 Operational Amplifiers 2025-07-02 21.26.36" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.8</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 5.4</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;207]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-operational-amplifiers-2025-07-02-21-34-15.svg"><img src="/notes/excalidraw/05-operational-amplifiers-2025-07-02-21-34-15.svg" alt="05 Operational Amplifiers 2025-07-02 21.34.15" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.9</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 5.4</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;207]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-operational-amplifiers-2025-07-02-21-50-33.svg"><img src="/notes/excalidraw/05-operational-amplifiers-2025-07-02-21-50-33.svg" alt="05 Operational Amplifiers 2025-07-02 21.50.33" loading="lazy"></a></figure>

</div>
</div>

### Noninverting Amplifier {#noninverting-amplifier}
- Provides a positive voltage gain

$$v_{o} = \left( 1 + \frac{R_{f}}{R_{1}} \right)v_{i}$$ 

<a class="zoom" href="/notes/img/noninverting-amplifier.png"><img src="/notes/img/noninverting-amplifier.png" alt="noninverting amplifier" loading="lazy"></a>

- Special case: the gain becomes 1 if $R_f = 0$ (short circuit) or $R_1 = \infty$ (open circuit) or both
	- This is known as a **voltage follower** (or unity gain amplifier) because $v_o = v_i$
	- Useful to isolate two cascading stages of a circuit

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.10</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 5.5</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;208]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-operational-amplifiers-2025-07-02-23-12-12.svg"><img src="/notes/excalidraw/05-operational-amplifiers-2025-07-02-23-12-12.svg" alt="05 Operational Amplifiers 2025-07-02 23.12.12" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.11">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.11</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 5.5</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;209]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-operational-amplifiers-2025-07-02-23-33-41.svg"><img src="/notes/excalidraw/05-operational-amplifiers-2025-07-02-23-33-41.svg" alt="05 Operational Amplifiers 2025-07-02 23.33.41" loading="lazy"></a></figure>

</div>
</div>

### Summing Amplifier {#summing-amplifier}
- Variation of the inverting amplifier that outputs a weighted sum of inputs

$$v_{o} = -\left( \frac{R_{f}}{R_{1}}v_{1} + \frac{R_{f}}{R_{2}}v_{2} + \frac{R_{f}}{R_{3}}v_{3} \right)$$

<a class="zoom" href="/notes/img/summing-amplifier.png"><img src="/notes/img/summing-amplifier.png" alt="summing amplifier" loading="lazy"></a>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.12">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.12</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 5.6</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;210]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-operational-amplifiers-2025-07-03-00-12-05.svg"><img src="/notes/excalidraw/05-operational-amplifiers-2025-07-03-00-12-05.svg" alt="05 Operational Amplifiers 2025-07-03 00.12.05" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.13">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.13</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 5.6</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;211]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-operational-amplifiers-2025-07-03-00-17-16.svg"><img src="/notes/excalidraw/05-operational-amplifiers-2025-07-03-00-17-16.svg" alt="05 Operational Amplifiers 2025-07-03 00.17.16" loading="lazy"></a></figure>

</div>
</div>

### Differential Amplifier {#differential-amplifier}
- Amplifies the difference between two inputs

$$v_{o} = \left( 1+\frac{R_{f}}{R_{1}} \right)\left( \frac{R_{4}}{R_{3}+R_{4}} V_{2}\right) -\frac{R_{f}}{R_{1}}V_{1}$$

- If $\frac{R_{1}}{R_{f}} = \frac{R_{3}}{R_{4}}$:

$$v_{o} = \frac{R_{f}}{R_{1}}(v_{2} - v_{1})$$

- If $R_2 = R_1$ and $R_3 = R_4$, the gain is 1 and the output is a subtractor:

$$v_{o} = v_{2} - v_{1}$$

<a class="zoom" href="/notes/img/differential-amplifier.png"><img src="/notes/img/differential-amplifier.png" alt="differential amplifier" loading="lazy"></a>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.14">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.14</span> <span class="theorem-callout-subtitle">(Instrumentation Amplifier Example)</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 5.8</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;213]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-operational-amplifiers-2025-07-03-00-35-01.svg"><img src="/notes/excalidraw/05-operational-amplifiers-2025-07-03-00-35-01.svg" alt="05 Operational Amplifiers 2025-07-03 00.35.01" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.15">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.15</span> <span class="theorem-callout-subtitle">(Instrumental Amplifier Problem)</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 5.8</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;214]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-operational-amplifiers-2025-07-03-00-54-39.svg"><img src="/notes/excalidraw/05-operational-amplifiers-2025-07-03-00-54-39.svg" alt="05 Operational Amplifiers 2025-07-03 00.54.39" loading="lazy"></a></figure>

</div>
</div>

## Cascaded Op Amp Circuits {#cascaded-op-amp-circuits}
- A cascade is when the output of one is the output of the next, with each connection called a stage
- The overall gain is the product of the gains of the stages

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.16">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.16</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 5.9</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;216]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-operational-amplifiers-2025-07-03-01-10-20.svg"><img src="/notes/excalidraw/05-operational-amplifiers-2025-07-03-01-10-20.svg" alt="05 Operational Amplifiers 2025-07-03 01.10.20" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="05.17">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 05.17</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 5.10</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;218]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-operational-amplifiers-2025-07-03-01-14-23.svg"><img src="/notes/excalidraw/05-operational-amplifiers-2025-07-03-01-14-23.svg" alt="05 Operational Amplifiers 2025-07-03 01.14.23" loading="lazy"></a></figure>

</div>
</div>
