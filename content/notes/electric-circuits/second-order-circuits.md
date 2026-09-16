---
author: "Anish Goyal"
title: "Second-Order Circuits"
description: "Remember that capacitor voltage and inductor current are continuous"
tags:
  - "notes"
  - "electrical-engineering"
  - "electric-circuits"
date: 2025-07-05T15:37:19
modified: 2025-07-16T15:53:42
readingtime: "7"
course: "Fundamentals of Electric Circuits (Sadiku)"
course_slug: "electric-circuits"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 8
weight: 80
slug: "second-order-circuits"
links: []
sources:
  - "Alexander & Sadiku, Fundamentals of Electric Circuits"
generated: true
---

## Second-Order Circuit {#second-order-circuit}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="08.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 08.1</span> <span class="theorem-callout-subtitle">(Second-Order Circuit)</span>.</div></div>
<div class="callout-content">

Circuits with a response characterized by a second-order differential equation, containing two energy storage devices.

</div>
</div>

## Finding Initial and Final Values {#finding-initial-and-final-values}
- Remember that capacitor voltage and inductor current are continuous
- Analyze the values right before and after the switching event

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.2</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 8.1</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;339]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-05-15-40-05.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-05-15-40-05.svg" alt="08 Second-Order Circuits 2025-07-05 15.40.05" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.3</span>.</div></div>
<div class="callout-content">

<cite class="cite cite-quote"><q>Practice Problem 8.1</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;340]</span></cite>

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-05-16-02-10.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-05-16-02-10.svg" alt="08 Second-Order Circuits 2025-07-05 16.02.10" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.4</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 8.2</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;341]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-05-16-17-33.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-05-16-17-33.svg" alt="08 Second-Order Circuits 2025-07-05 16.17.33" loading="lazy"></a></figure>

</div>
</div>

 
<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.5</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 8.2</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;343]</span></cite>) 

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-05-18-17-16.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-05-18-17-16.svg" alt="08 Second-Order Circuits 2025-07-05 18.17.16" loading="lazy"></a></figure>

</div>
</div>

## Natural Response of Series RLC Circuit {#natural-response-of-series-rlc-circuit}
- Use KVL to obtain the characteristic equation
- Use initial conditions to solve for $A_{1}$ and $A_{2}$
- Trying to solve for the shared current, $i(t)$

- Characteristic equation:

$$s^2 + \frac{R}{L}s + \frac{1}{LC} = 0$$

- Roots (natural frequencies):
$s_{1, 2} = -\alpha \pm \sqrt{ a^2 - \omega_{0}^2}$
where $\alpha = \frac{1}{2} \frac{R}{L}$ and $\omega_{0} = \frac{1}{\sqrt{ LC }}$

## Damping {#damping}
- The gradual loss of initial stored energy, evidenced by the decrease in the amplitude of the response
- Dependent on the value of $R$; if there is no $R$, $\alpha = 0$

### Overdamped $(\alpha > \omega_{0})$ {#overdamped-0}
- Both roots are negative and real
- Decays the slowest

$$i(t) = A_{1}e^{s_{1}t} + A_{2}e^{s_{2}t}$$

### Critically Damped $(\alpha = \omega_{0})$ {#critically-damped-0}
- Decays the quickest without any ringing

$$i(t) = e^{-\alpha t}(A_{1}+A_{2}t)$$

### Underdamped $(\alpha < \omega_{0})$ {#underdamped-0}
- Two imaginary roots
- Oscillatory response (ringing) due to the storage devices transferring energy to each other
- This means $s_{1, 2} = -\alpha \pm \sqrt{-(\omega_{0}^2 - \alpha^2)} = -\alpha \pm j \omega_{d}$

$$i(t) = e^{-\alpha t}(A_{1}\cos \omega_{d}t + A_{2}\sin \omega_{d}t)$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.6</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 8.3</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;348]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-06-02-34-17.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-06-02-34-17.svg" alt="08 Second-Order Circuits 2025-07-06 02.34.17" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.7</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 8.3</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;348]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-06-02-44-17.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-06-02-44-17.svg" alt="08 Second-Order Circuits 2025-07-06 02.44.17" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.8</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 8.4</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;348]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-06-02-50-12.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-06-02-50-12.svg" alt="08 Second-Order Circuits 2025-07-06 02.50.12" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.9</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 8.4</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;350]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-06-03-20-13.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-06-03-20-13.svg" alt="08 Second-Order Circuits 2025-07-06 03.20.13" loading="lazy"></a></figure>

</div>
</div>

## Natural Response of Parallel RLC Circuit {#natural-response-of-parallel-rlc-circuit}
- Use KCL to obtain the characteristic equation
- Use initial conditions to solve for $A_{1}$ and $A_{2}$
- Dampening cases remain the same
- Trying to solve for the shared voltage, $v(t)$

- Characteristic equation:

$$s^2 + \frac{1}{RC}s + \frac{1}{LC} = 0$$

- Natural frequencies:
$s_{1, 2} = -\alpha \pm \sqrt{ a^2 - \omega_{0}^2}$
where $\alpha = \frac{1}{2} \frac{1}{RC}$ and $\omega_{0} = \frac{1}{\sqrt{ LC }}$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.10</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 8.5</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;352]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-06-03-54-01.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-06-03-54-01.svg" alt="08 Second-Order Circuits 2025-07-06 03.54.01" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.11">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.11</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 8.5</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;354]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-06-04-31-31.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-06-04-31-31.svg" alt="08 Second-Order Circuits 2025-07-06 04.31.31" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.12">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.12</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 8.6</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;354]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-06-16-05-26.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-06-16-05-26.svg" alt="08 Second-Order Circuits 2025-07-06 16.05.26" loading="lazy"></a></figure> 

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.13">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.13</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 8.6</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;355]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-06-16-25-18.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-06-16-25-18.svg" alt="08 Second-Order Circuits 2025-07-06 16.25.18" loading="lazy"></a></figure>

</div>
</div>

## Step Response of Series RLC Circuit {#step-response-of-series-rlc-circuit}
- Superposition of the natural response (transient response) and steady-state response $v(\infty)$
- However, we are now evaluating the voltage response of the capacitor and not the shared current 

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.14">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.14</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 8.7</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;357]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-06-18-46-56.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-06-18-46-56.svg" alt="08 Second-Order Circuits 2025-07-06 18.46.56" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.15">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.15</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 8.7</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;360]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-06-20-23-42.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-06-20-23-42.svg" alt="08 Second-Order Circuits 2025-07-06 20.23.42" loading="lazy"></a></figure>

</div>
</div>

## Step Response of Parallel RLC Circuit {#step-response-of-parallel-rlc-circuit}
- Current response is equal to the transient response and the steady-state response $i(\infty)$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.16">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.16</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 8.8</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;361]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-06-23-27-25.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-06-23-27-25.svg" alt="08 Second-Order Circuits 2025-07-06 23.27.25" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.17">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.17</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 8.8</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;363]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-16-11-00-01.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-16-11-00-01.svg" alt="08 Second-Order Circuits 2025-07-16 11.00.01" loading="lazy"></a></figure>

</div>
</div>

## General Second-Order Circuits {#general-second-order-circuits}
- Our approach for analyzing series/parallel RLC circuits may be extended for any second-order circuit:
	- Evaluate the initial conditions $(x(0), \frac{\mathrm{d}x}{\mathrm{d}t}(0))$ and steady-state response $(x(\infty))$
	- Turn off all independent sources and obtain the transient response using KCL/KVL
	- Determine the characteristic roots of the resulting differential equation
	- The entire response is the sum of the transient response and steady-state response

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.18">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.18</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 8.9</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;363]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-second-order-circuits-2025-07-16-15-55-43.svg"><img src="/notes/excalidraw/08-second-order-circuits-2025-07-16-15-55-43.svg" alt="08 Second-Order Circuits 2025-07-16 15.55.43" loading="lazy"></a></figure>

</div>
</div>
