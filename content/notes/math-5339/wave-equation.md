---
author: "Anish Goyal"
title: "Wave Equation"
description: "If a PDE is dependent on time, it is called evolutionary"
tags:
  - "notes"
  - "mathematics"
  - "math-5339"
date: 2025-08-22T10:18:43
modified: 2025-08-29T10:56:43
readingtime: "3"
course: "MATH 5339"
course_slug: "math-5339"
subject: "mathematics"
kind: "lecture"
ordinal: 4
weight: 40
slug: "wave-equation"
links: []
sources: []
generated: true
---

## Plucked String {#plucked-string}
- If a PDE is dependent on time, it is called *evolutionary*
- Suppose there is a fixed string between two points that can only move transversely (up and down)
- We need to find an equation to describe the displacement of the string at a particular time $u(x, t)$

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-second-order-linear-pdes-2025-08-22-10-21-32.svg"><img src="/notes/excalidraw/04-second-order-linear-pdes-2025-08-22-10-21-32.svg" alt="04 Second-Order Linear PDEs 2025-08-22 10.21.32" loading="lazy"></a></figure>

### Generalizing for Higher Dimensions {#generalizing-for-higher-dimensions}
- Add extra partial derivatives in the equation for the extra space variables

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-second-order-linear-pdes-2025-08-22-10-50-51.svg"><img src="/notes/excalidraw/04-second-order-linear-pdes-2025-08-22-10-50-51.svg" alt="04 Second-Order Linear PDEs 2025-08-22 10.50.51" loading="lazy"></a></figure>

## What if the String is in Equilibrium? {#what-if-the-string-is-in-equilibrium}
- The displacement is no longer changing with respect to time, which implies $U_{tt} = 0$, which implies $\Delta U = 0$
- Thus, the string is no longer evolving with time
	- 1-D case: $U_{xx} = 0 \implies$ linear solution

## D'Alembert's Formula to Solve the Wave Equation {#d-alembert-s-formula-to-solve-the-wave-equation}

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-second-order-linear-pdes-2025-08-27-10-16-29.svg"><img src="/notes/excalidraw/04-second-order-linear-pdes-2025-08-27-10-16-29.svg" alt="04 Second-Order Linear PDEs 2025-08-27 10.16.29" loading="lazy"></a></figure>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.1</span>.</div></div>
<div class="callout-content">

Wave Equation D'Alembert's Example
- This is a standing wave, which means that it doesn't actually move laterally
	- Formed via the superposition of two traveling waves

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-second-order-linear-pdes-2025-08-27-10-24-21.svg"><img src="/notes/excalidraw/04-second-order-linear-pdes-2025-08-27-10-24-21.svg" alt="04 Second-Order Linear PDEs 2025-08-27 10.24.21" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.2</span>.</div></div>
<div class="callout-content">

Wave Equation (no Initial velocity) Example
- This is a plucked string where you hold the string in an initial configuration and then let go and see the effect

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-second-order-linear-pdes-2025-08-27-10-43-28.svg"><img src="/notes/excalidraw/04-second-order-linear-pdes-2025-08-27-10-43-28.svg" alt="04 Second-Order Linear PDEs 2025-08-27 10.43.28" loading="lazy"></a></figure>

</div>
</div>

## Principle of Causality {#principle-of-causality}
* Disturbances in the wave equation propagate cannot exceed $c$
* No effect can be felt outside the cone bounded by the characteristics $x = x_0 \pm ct$
* The solution at a point $(x_0,t_0)$ depends only on initial data in the interval $[x_0 - ct_0, x_0 + ct_0]$
* Signals do not travel instantaneously

## Domain of Influence {#domain-of-influence}
* For a point $(x_0,t_0)$ the domain of influence is the set of initial points that can affect $(x_0,t_0)$
* Bounded by the forward characteristics $x = x_0 \pm ct$
* Shows how information spreads forward in time

## Domain of Dependence {#domain-of-dependence}
* For a point $(x,t)$ the domain of dependence is the set of earlier points that determine the solution at $(x,t)$
* In 1D this region is the triangle bounded by the backward characteristics $x \pm ct$ traced back to $t=0$
* Encodes causality only data within this region can influence the solution at $(x,t)$

## Conservation of Energy {#conservation-of-energy}

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-wave-equation-2025-08-29-10-28-20.svg"><img src="/notes/excalidraw/04-wave-equation-2025-08-29-10-28-20.svg" alt="04 Wave Equation 2025-08-29 10.28.20" loading="lazy"></a></figure>

## Final Remarks {#final-remarks}
- Huygen's Principle: The Wave Equation in three dimensions (and odd-numbered dimensions) has an exact speed $c$
	- However, in even-numbered dimensions, this is not necessarily the case; you will then have a lagging term that changes the speed
