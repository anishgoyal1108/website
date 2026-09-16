---
author: "Anish Goyal"
title: "Circuit Theorems"
description: "Combination of two properties: homogeneity and additivity"
tags:
  - "notes"
  - "electrical-engineering"
  - "electric-circuits"
date: 2025-06-23T18:21:35
modified: 2025-06-26T10:33:35
readingtime: "8"
course: "Fundamentals of Electric Circuits (Sadiku)"
course_slug: "electric-circuits"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 4
weight: 40
slug: "circuit-theorems"
links: []
sources:
  - "Alexander & Sadiku, Fundamentals of Electric Circuits"
generated: true
---

## Linearity {#linearity}
- Combination of two properties: homogeneity and additivity
- Homogeneity requires that if the excitation is multiplied by a constant, the output is multiplied by the same constant
- Additivity requires that the response to a sum of excitations is the sum of the responses if each excitation was applied separately

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="04.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 04.1</span> <span class="theorem-callout-subtitle">(Linear Circuit)</span>.</div></div>
<div class="callout-content">

A circuit whose output is linearly related (directly proportional) to its input. Satisfies the homogeneity and additivity properties.

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.2</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 4.1</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;154]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/circuit-theorems-2025-06-23-18-28-25.svg"><img src="/notes/excalidraw/circuit-theorems-2025-06-23-18-28-25.svg" alt="Circuit Theorems 2025-06-23 18.28.25" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.3</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 4.2</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;154]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/circuit-theorems-2025-06-23-18-38-59.svg"><img src="/notes/excalidraw/circuit-theorems-2025-06-23-18-38-59.svg" alt="Circuit Theorems 2025-06-23 18.38.59" loading="lazy"></a></figure>

</div>
</div>

## Superposition {#superposition}
- For circuits with more than one independent source, you can determine voltage/current of an element by summing the contribution of each source to the variable

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="04.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 04.4</span> <span class="theorem-callout-subtitle">(Superposition Principle)</span>.</div></div>
<div class="callout-content">

The voltage across (or current through) an element of a linear circuit is the algebraic sum of the voltages across (or currents through) that element due to each independent source acting alone. Employ the following:
- Voltage sources are 0V with a short circuit
- Current sources are 0A with an open circuit
- Dependent sources are left intact, since they are controlled by circuit variables

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.5</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 4.3</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;156]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/circuit-theorems-2025-06-23-19-11-32.svg"><img src="/notes/excalidraw/circuit-theorems-2025-06-23-19-11-32.svg" alt="Circuit Theorems 2025-06-23 19.11.32" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.6</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 4.3</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;156]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/circuit-theorems-2025-06-23-19-12-04.svg"><img src="/notes/excalidraw/circuit-theorems-2025-06-23-19-12-04.svg" alt="Circuit Theorems 2025-06-23 19.12.04" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.7</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 4.4</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;156]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/circuit-theorems-2025-06-23-19-19-46.svg"><img src="/notes/excalidraw/circuit-theorems-2025-06-23-19-19-46.svg" alt="Circuit Theorems 2025-06-23 19.19.46" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.8</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 4.4</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;158]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-23-20-10-38.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-23-20-10-38.svg" alt="04 Circuit Theorems 2025-06-23 20.10.38" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.9</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 4.5</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;159]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-23-21-36-46.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-23-21-36-46.svg" alt="04 Circuit Theorems 2025-06-23 21.36.46" loading="lazy"></a></figure>

</div>
</div>

## Source Transformation {#source-transformation}
- Replacing a voltage source in series with a resistor by a current source in parallel with a resistor (or vice versa)

$$V_{s} = R i_{s} \ \text{or} \ i_{s} = \frac{V_{s}}{R}$$

- Can be applied to dependent sources if the equation is kept satisfied

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.10</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 4.6</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;161]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-24-17-28-00.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-24-17-28-00.svg" alt="04 Circuit Theorems 2025-06-24 17.28.00" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.11">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.11</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 4.6</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;161]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-24-18-09-01.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-24-18-09-01.svg" alt="04 Circuit Theorems 2025-06-24 18.09.01" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.12">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.12</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 4.7</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;162]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-24-18-26-33.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-24-18-26-33.svg" alt="04 Circuit Theorems 2025-06-24 18.26.33" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.13">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.13</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 4.7</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;162]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-24-18-57-00.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-24-18-57-00.svg" alt="04 Circuit Theorems 2025-06-24 18.57.00" loading="lazy"></a></figure>

</div>
</div>

## Thevenin's Theorem {#thevenin-s-theorem}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="04.14">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 04.14</span>.</div></div>
<div class="callout-content">

Any linear two-terminal circuit can be replaced by a voltage source $V_{\text{th}}$ in series with a resistor $R_{\text{th}}$.
- $V_{\text{th}} = V_{\text{oc}}$
- $R_{\text{th}} = R_{\text{eq}}$ with independent sources off

</div>
</div>

### Finding $R_{\text{th}}$ {#finding-r-th}
- Two cases:
	1. The network has no dependent sources. Then, turn off all independent sources, and $R_{\text{th}} = R_{\text{eq}}$
	2. The network has dependent sources. Then, turn off all independent sources, and apply a voltage source $v_o$ at the terminals. Determine $i_o$, and $R_{\text{th}} = \frac{v_o}{i_o}$
		- Alternatively, apply a current source $i_o$ at the terminals and find the terminal voltage $v_o$
- If $R_{\text{th}} < 0$, the circuit is supplying power 

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.15">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.15</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 4.8</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;164]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-24-20-11-29.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-24-20-11-29.svg" alt="04 Circuit Theorems 2025-06-24 20.11.29" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.16">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.16</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 4.8</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;166]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-24-20-33-24.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-24-20-33-24.svg" alt="04 Circuit Theorems 2025-06-24 20.33.24" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.17">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.17</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 4.9</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;166]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-24-21-01-07.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-24-21-01-07.svg" alt="04 Circuit Theorems 2025-06-24 21.01.07" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.18">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.18</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 4.9</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;167]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-24-21-52-40.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-24-21-52-40.svg" alt="04 Circuit Theorems 2025-06-24 21.52.40" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.19">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.19</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 4.10</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;169]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-25-19-31-45.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-25-19-31-45.svg" alt="04 Circuit Theorems 2025-06-25 19.31.45" loading="lazy"></a></figure>

</div>
</div>

## Norton's Theorem {#norton-s-theorem}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="04.20">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 04.20</span>.</div></div>
<div class="callout-content">

Any linear two-terminal circuit can be replaced by a current source $i_{N}$ in parallel with a resistor $R_{N}$.
- $i_{N} = i_{\text{sc}}$
- $R_{\text{N}} = R_{\text{eq}}$ with independent sources off

</div>
</div>

- An implication from this is $R_{N} = R_{\text{th}}$; this is true when we looked at source transformations previously
- Another implication is that Thevenin and Norton's Theorems are related by:

$$V_{\text{th}} = I_{N} R_{\text{th}} \ \text{or} \ V_{\text{oc}} = i_{\text{sc}}R_{N}$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.21">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.21</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 4.11</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;170]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-25-20-21-44.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-25-20-21-44.svg" alt="04 Circuit Theorems 2025-06-25 20.21.44" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.22">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.22</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 4.11</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;171]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-25-21-43-09.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-25-21-43-09.svg" alt="04 Circuit Theorems 2025-06-25 21.43.09" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.23">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.23</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 4.12</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;172]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-25-22-35-49.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-25-22-35-49.svg" alt="04 Circuit Theorems 2025-06-25 22.35.49" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.24">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.24</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 4.12</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;172]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-25-23-09-20.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-25-23-09-20.svg" alt="04 Circuit Theorems 2025-06-25 23.09.20" loading="lazy"></a></figure>

</div>
</div>

## Maximum Power Transfer {#maximum-power-transfer}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="04.25">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 04.25</span> <span class="theorem-callout-subtitle">(Maximum Power Theorem)</span>.</div></div>
<div class="callout-content">

**Maximum power** is transferred to $R_{L}$ iff ${R_{L} = R_{\text{th}}}$. In terms of $V_{\text{th}}$:

$$p_{\text{max}} = \frac{V_{\text{th}}^2}{4R_{\text{th}}}$$

In terms of $I_{N}$:

$$p_{\text{max}} = \frac{I_{N}^2 R_{N}}{4}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.26">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.26</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 4.13</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;175]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-26-10-36-34.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-26-10-36-34.svg" alt="04 Circuit Theorems 2025-06-26 10.36.34" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.27">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.27</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 4.13</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;176]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-circuit-theorems-2025-06-26-10-48-59.svg"><img src="/notes/excalidraw/04-circuit-theorems-2025-06-26-10-48-59.svg" alt="04 Circuit Theorems 2025-06-26 10.48.59" loading="lazy"></a></figure>

</div>
</div>
