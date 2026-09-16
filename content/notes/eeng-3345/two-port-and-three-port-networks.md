---
author: "Anish Goyal"
title: "Two-Port and Three-Port Networks"
description: "Define a matrix model for the system using the network type"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3345"
date: 2025-07-21T10:08:05
modified: 2025-07-22T11:40:23
readingtime: "3"
course: "EENG 3345"
course_slug: "eeng-3345"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 10
weight: 100
slug: "two-port-and-three-port-networks"
links:
  - "/notes/electric-circuits/basic-laws/"
sources:
  - "Alexander & Sadiku, Fundamentals of Electric Circuits"
  - "Two-Port and Three-Port Networks"
generated: true
---

<div class="transclusion" data-source="04. Notes/Fundamentals of Electric Circuits/02 Basic Laws.md">
<a class="transclusion-source" href="/notes/electric-circuits/basic-laws/#wye-delta-transformations" title="Open Basic Laws › Wye-Delta Transformations"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

## Wye-Delta Transformations {#wye-delta-transformations-embed1}
- Resistive networks that aren't in series or parallel may be simplified to a three-terminal equivalent network
	- Either the Wye/Tee network or the Delta/Pi network

### Delta-Wye Conversion {#delta-wye-conversion-embed1}
- Superimpose Y onto $\Delta$ by adding an extra node $n$. Each resistor in Y is the product of the resistors in the two adjacent $\Delta$ branches divided by the sum of the three $\Delta$ resistors
- For the network below:

$$\begin{align}
R_{1} &= \frac{R_{b}R_{c}}{R_{a}+R_{b}+R_{c}} \\
R_{2} &= \frac{R_{c}R_{a}}{R_{a}+R_{b}+R_{c}} \\
R_{3} &= \frac{R_{a}R_{b}}{R_{a}+R_{b}+R_{c}}
\end{align}
$$

<a class="zoom" href="/notes/img/delta-wye-conversion-example.png"><img src="/notes/img/delta-wye-conversion-example.png" alt="delta wye conversion example" loading="lazy"></a>

### Wye-Delta Conversion {#wye-delta-conversion-embed1}
- Each resistor in the $\Delta$ network is the sum of all products of Y resistors divided by the opposite Y resistor
- For the superimposed network:

$$\begin{align}
R_{a} &= \frac{R_{1}R_{2}+R_{2}R_{3}+R_{3}R_{1}}{R_{1}} \\
R_{b} &= \frac{R_{1}R_{2}+R_{2}R_{3}+R_{3}R_{1}}{R_{2}} \\
R_{c} &= \frac{R_{1}R_{2}+R_{2}R_{3}+R_{3}R_{1}}{R_{3}}
\end{align}$$

### Balanced Condition {#balanced-condition-embed1}
- If all the Y resistances are equal AND all the $\Delta$ resistances are equal, then:

$$R_{Y} = \frac{R_{\Delta}}{3} \ \text{or} \ R_{\Delta}= 3R_{Y}$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.25">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.25</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 2.14</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;80]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/basic-laws-2025-06-21-11-14-16.svg"><img src="/notes/excalidraw/basic-laws-2025-06-21-11-14-16.svg" alt="Basic Laws 2025-06-21 11.14.16" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.26">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.26</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 2.15</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;83]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/basic-laws-2025-06-21-11-28-20.svg"><img src="/notes/excalidraw/basic-laws-2025-06-21-11-28-20.svg" alt="Basic Laws 2025-06-21 11.28.20" loading="lazy"></a></figure>

</div>
</div>

</div>

## Two-Port Networks {#two-port-networks}
### Overview {#overview}
1. Define a matrix model for the system using the network type
2. Selectively zero out each parameter
3. Use methods of analysis to rewrite the output equations in terms of the input variables
4. Solve the output equations

### Network Parameters {#network-parameters}
#### Impedance {#impedance}

$$

\begin{bmatrix}

V_1 \\

V_2

\end{bmatrix}

=

\begin{bmatrix}

Z_{11} & Z_{12} \\

Z_{21} & Z_{22}

\end{bmatrix}

\begin{bmatrix}

I_1 \\

I_2

\end{bmatrix}

$$

<a class="zoom" href="/notes/img/impedance-2port.png"><img src="/notes/img/impedance-2port.png" alt="impedance 2port" loading="lazy"></a>

#### Admittance {#admittance}

$$

\begin{bmatrix}

I_1 \\

I_2

\end{bmatrix}

=

\begin{bmatrix}

Y_{11} & Y_{12} \\

Y_{21} & Y_{22}

\end{bmatrix}

\begin{bmatrix}

V_1 \\

V_2

\end{bmatrix}

$$

<a class="zoom" href="/notes/img/admittance-2port.png"><img src="/notes/img/admittance-2port.png" alt="admittance 2port" loading="lazy"></a>

#### Hybrid {#hybrid}

$$

\begin{bmatrix}

V_1 \\

I_2

\end{bmatrix}

=

\begin{bmatrix}

h_{11} & h_{12} \\

h_{21} & h_{22}

\end{bmatrix}

\begin{bmatrix}

I_1 \\

V_2

\end{bmatrix}

$$

<a class="zoom" href="/notes/img/hybrid-2port.png"><img src="/notes/img/hybrid-2port.png" alt="hybrid 2port" loading="lazy"></a>

#### Inverse Hybrid {#inverse-hybrid}

$$

\begin{bmatrix}

I_1 \\

V_2

\end{bmatrix}

=

\begin{bmatrix}

g_{11} & g_{12} \\

g_{21} & g_{22}

\end{bmatrix}

\begin{bmatrix}

V_1 \\

I_2

\end{bmatrix}

$$

<a class="zoom" href="/notes/img/inverse-hybrid-2port.png"><img src="/notes/img/inverse-hybrid-2port.png" alt="inverse hybrid 2port" loading="lazy"></a>

#### Transmission {#transmission}

$$

\begin{bmatrix}

V_1 \\

I_1

\end{bmatrix}

=

\begin{bmatrix}

A & B \\

C & D

\end{bmatrix}

\begin{bmatrix}

V_2 \\

- I_2

\end{bmatrix}

$$

<a class="zoom" href="/notes/img/transmission-2port.png"><img src="/notes/img/transmission-2port.png" alt="transmission 2port" loading="lazy"></a>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="10.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 10.1</span> <span class="theorem-callout-subtitle">(A two-port network is given below. Find the parameters $Z_{11}, Z_{12}, Z_{21}, Z_{22}$ that relate the currents and voltages of the circuit through the equations $V_1 = Z_{11}I_1 + Z_{12}I_2$ and $V_2 = Z_{21}I_1 + Z_{22}I_2$)</span>.</div></div>
<div class="callout-content">

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/10-two-port-and-three-port-networks-2025-07-22-10-08-40.svg"><img src="/notes/excalidraw/10-two-port-and-three-port-networks-2025-07-22-10-08-40.svg" alt="10 Two-Port and Three-Port Networks 2025-07-22 10.08.40" loading="lazy"></a></figure>

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Two-Port and Three-Port Networks (course handout)</span>
