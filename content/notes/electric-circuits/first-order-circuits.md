---
author: "Anish Goyal"
title: "First-Order Circuits"
description: "Two ways to excite 1st order circuit:"
tags:
  - "notes"
  - "electrical-engineering"
  - "electric-circuits"
date: 2025-07-04T02:54:54
modified: 2025-07-04T23:36:23
readingtime: "8"
course: "Fundamentals of Electric Circuits (Sadiku)"
course_slug: "electric-circuits"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 7
weight: 70
slug: "first-order-circuits"
links: []
sources:
  - "Alexander & Sadiku, Fundamentals of Electric Circuits"
generated: true
---

## First-Order Circuit {#first-order-circuit}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="07.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 07.1</span> <span class="theorem-callout-subtitle">(First-Order Circuit)</span>.</div></div>
<div class="callout-content">

A circuit containing one energy storage device (resistor/capacitor) with a resistor. Characterized by a first-order differential equation. 

</div>
</div>

- Two ways to excite 1st order circuit:
	1. *Source-free circuit*: assume the energy storage element holds all the energy via initial condition
		- Although there are no independent sources, there may be dependent sources
	2. Independent sources

## Source-Free RC {#source-free-rc}
- Voltage response is an exponential decay of $V_o$
	- This is called the *natural response*, since it is due to the energy storage unit itself

$$v(t) = V_{0}e^{-\frac{t}{RC}}$$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="07.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 07.2</span> <span class="theorem-callout-subtitle">(Natural Response)</span>.</div></div>
<div class="callout-content">

The behavior of voltage and current with no external excitation.

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="07.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 07.3</span> <span class="theorem-callout-subtitle">(Time Constant)</span>.</div></div>
<div class="callout-content">

The time required for the response to decay to a factor of $\frac{1}{e}$ or 36.8% of its initial value.

$$\tau = RC$$

</div>
</div>

- Circuits with a small $\tau$ reach steady state (complete energy dissipation) quickly

- Current response by Ohm's Law:

$$i(t) = \frac{V_{0}}{R}e^{-\frac{t}{\tau}}$$

- Power dissipated by $R$:

$$p(t) = \frac{V_{0}^2}{R}e^{-\frac{2t}{\tau}}$$

- Energy absorbed by $R$:

$$w(t) = \frac{1}{2}CV_{0}^2 (1-e^{-\frac{2t}{\tau}})$$

- $R$ is often $R_{\text{th}}$ at the terminals of the capacitor

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.4</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 7.1</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;282]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-04-14-56-53.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-04-14-56-53.svg" alt="07 First-Order Circuits 2025-07-04 14.56.53" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.5</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 7.2</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;283]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-04-16-57-06.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-04-16-57-06.svg" alt="07 First-Order Circuits 2025-07-04 16.57.06" loading="lazy"></a></figure>

</div>
</div>

## Source-Free RL {#source-free-rl}
- Natural response is an exponential decay of $I_0$

$$i(t) = I_{0}e^{-t \frac{R}{L}}$$

- Time constant

$$\tau = \frac{L}{R}$$

- Voltage response by Ohm's Law:

$$v(t) = I_{0}R e^{-\frac{t}{\tau}}$$

- Power dissipated by $R$:

$$p(t) = I_{0}^2 R e^{-2\frac{t}{\tau}}$$

- Energy absorbed by $R$:

$$w(t) = \frac{1}{2} LI_{0}^2 (1 - e^{-2\frac{t}{\tau}})$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.6</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 7.3</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;287]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-04-17-43-23.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-04-17-43-23.svg" alt="07 First-Order Circuits 2025-07-04 17.43.23" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.7</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 7.4</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;288]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-04-17-53-38.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-04-17-53-38.svg" alt="07 First-Order Circuits 2025-07-04 17.53.38" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.8</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 7.5</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;289]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-04-18-19-50.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-04-18-19-50.svg" alt="07 First-Order Circuits 2025-07-04 18.19.50" loading="lazy"></a></figure>

</div>
</div>

## Singularity Functions {#singularity-functions}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="07.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 07.9</span> <span class="theorem-callout-subtitle">(Singularity Functions)</span>.</div></div>
<div class="callout-content">

Functions that are discontinuous or have discontinuous derivatives.

</div>
</div>

### Unit Step {#unit-step}

$$u(t) = \begin{cases}
0,& t < 0 \\
1,& t>0
\end{cases}$$

- Represents an abrupt change in voltage/current

### Unit Impulse {#unit-impulse}

$$\delta(t) = \frac{\mathrm{d}}{\mathrm{d}t}u(t) = \begin{cases}
0,& t<0 \\
\text{Undefined},& t=0 \\
0,& t>0
\end{cases}$$

- Zero everywhere except at $t=0$, where it spikes to a value, which is equal to its area:

$$\int_{0^-}^{0^+} \delta (t) \, \mathrm{d}t = 1$$

- Any function integrated with the impulse function is "sampled" at the point of impulse

$$\int_{a}^{b}f(t)\delta (t - t_{0}) \, \mathrm{d}t = f(t_{0})$$

### Unit Ramp {#unit-ramp}

$$r(t) = \int_{-\infty}^{t} u(\tau) \, \mathrm{d}\tau = \begin{cases}
0,& t \le 0 \\
t,& t \ge 0
\end{cases}$$

## Complete Response {#complete-response}
- The **complete response** is the sum of the response from the stored energy (natural response) and the response from the independent source (forced response)

$$v = v_{n} + v_{f}$$

where $v_n = V_0 e^{-t\frac{t}{\tau}}$ and $v_f = V_s(1 - e^{-\frac{t}{\tau}})$

- Alternatively: the sum of the transient response and the steady-state response
	- $v_t$ decays to zero as $t \rightarrow \infty$
	- $v_{ss}$ remains after $v_t$ has died 

$$v = v_{t} + v_{ss}$$

where $v_t = (V_0 - V_s)e^{-\frac{t}{\tau}}$ and $v_{ss} = V_s$

- Final equation (valid from both perspectives):

$$v(t) = v(\infty) + [v(0) - v(\infty)]e^{-\frac{t}{\tau}}$$

where $v(0)$ is the voltage at $t = 0^+$ and $v(\infty)$ is the steady-state value

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.10</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 7.10</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;301]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-04-19-09-25.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-04-19-09-25.svg" alt="07 First-Order Circuits 2025-07-04 19.09.25" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.11">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.11</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 7.10</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;302]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-04-19-20-42.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-04-19-20-42.svg" alt="07 First-Order Circuits 2025-07-04 19.20.42" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.12">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.12</span>.</div></div>
<div class="callout-content">

<cite class="cite cite-quote"><q>Example 7.11</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;302]</span></cite>

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-04-21-31-30.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-04-21-31-30.svg" alt="07 First-Order Circuits 2025-07-04 21.31.30" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.13">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.13</span>.</div></div>
<div class="callout-content">

<cite class="cite cite-quote"><q>Practice Problem 7.11</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;303]</span></cite>

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-04-22-00-35.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-04-22-00-35.svg" alt="07 First-Order Circuits 2025-07-04 22.00.35" loading="lazy"></a></figure>

</div>
</div>

## RC Step Response {#rc-step-response}
- Complete response:

$$v(t) = \begin{cases}
V_{0},& t < 0 \\
V_{s} + (V_{0}-V_{s})e^{-\frac{t}{\tau}},& t > 0
\end{cases}$$

- If capacitor uncharged:

$$v(t) = V_{s}(1-e^{-\frac{t}{\tau}})u(t)$$

- Current through capacitor:

$$\frac{V_{s}}{R} e^{-\frac{t}{\tau}}u(t)$$

## RL Step Response {#rl-step-response}
- Complete response:

$$i(t) = \frac{V_{s}}{R} + \left( I_{0} - \frac{V_{s}}{R} \right) e^{-\frac{t}{\tau}}$$

- If there is no $I_0$:

$$i(t) = \frac{V_{s}}{R} (1-e^{-\frac{t}{\tau}})u(t)$$

- Voltage across inductor:

$$v(t) = V_{s}e^{-\frac{t}{\tau}}u(t)$$

- Complete response (easy form):

$$i(t) = i(\infty) + [i(0) - i(\infty)]e^{-\frac{t}{\tau}}$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.14">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.14</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 7.12</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;306]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-04-22-35-15.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-04-22-35-15.svg" alt="07 First-Order Circuits 2025-07-04 22.35.15" loading="lazy"></a></figure> 

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.15">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.15</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 7.12</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;306]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-04-22-39-56.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-04-22-39-56.svg" alt="07 First-Order Circuits 2025-07-04 22.39.56" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.16">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.16</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 7.13</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;307]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-04-22-46-23.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-04-22-46-23.svg" alt="07 First-Order Circuits 2025-07-04 22.46.23" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.17">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.17</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 7.13</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;308]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-04-23-10-51.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-04-23-10-51.svg" alt="07 First-Order Circuits 2025-07-04 23.10.51" loading="lazy"></a></figure>

</div>
</div>

## First-Order Op Amps {#first-order-op-amps}
- Analyze with nodal analysis or reduce to Thevenin equivalent circuit

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.18">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.18</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 7.14</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;309]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-04-23-39-14.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-04-23-39-14.svg" alt="07 First-Order Circuits 2025-07-04 23.39.14" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.19">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.19</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 7.14</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;310]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-05-00-16-32.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-05-00-16-32.svg" alt="07 First-Order Circuits 2025-07-05 00.16.32" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.20">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.20</span>.</div></div>
<div class="callout-content">

<cite class="cite cite-quote"><q>Example 7.15</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;310]</span></cite>

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-05-00-41-04.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-05-00-41-04.svg" alt="07 First-Order Circuits 2025-07-05 00.41.04" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.21">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.21</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 7.15</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;311]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-05-01-38-03.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-05-01-38-03.svg" alt="07 First-Order Circuits 2025-07-05 01.38.03" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.22">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.22</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 7.16</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;312]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-05-02-10-24.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-05-02-10-24.svg" alt="07 First-Order Circuits 2025-07-05 02.10.24" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="07.23">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 07.23</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 7.16</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;313]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-first-order-circuits-2025-07-05-02-40-37.svg"><img src="/notes/excalidraw/07-first-order-circuits-2025-07-05-02-40-37.svg" alt="07 First-Order Circuits 2025-07-05 02.40.37" loading="lazy"></a></figure>

</div>
</div>
