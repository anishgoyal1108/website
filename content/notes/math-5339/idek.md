---
author: "Anish Goyal"
title: "Transport and Wave Equations"
description: "Characteristic lines are of the form bx-ayC for an arbitrary equation a Ux + b Uy 0"
tags:
  - "notes"
  - "mathematics"
  - "math-5339"
date: 2025-08-20T10:15:34
modified: 2025-08-20T10:59:34
readingtime: "2"
course: "MATH 5339"
course_slug: "math-5339"
subject: "mathematics"
kind: "lecture"
ordinal: 3
weight: 30
slug: "idek"
links: []
sources: []
generated: true
---

Characteristic lines are of the form $bx-ay=C$ for an arbitrary equation $a U_x + b U_y = 0$

## Transport Equation {#transport-equation}

$$U_{t} + C U_{x} = 0$$ where $C$ is the speed of the fluid
- The solution is $u(x, t) = f(x-ct)$
	- On each of the characteristic lines, the function $u$ remains constant
	- As time progresses, the information contained in $u$ will be transported to the right at the speed $C$

WHAT THE FREAK IS A NONDEGENERATE LINEAR TRANSFORM for $… = ax+by$ and $\eta = bx-ay$ (jacobian nonzero)

## Wave Equation
- Suppose $U_x + y U_y = 0$. Then, you can represent it as:
$$\langle 1, y\rangle \cdot \nabla U = 0$$

- Thus, the vectors get steeper as $y$ increases
- We want to find a curve such that, for every point along the curve, its slope matches the vector

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-idek-2025-08-20-10-28-21.svg"><img src="/notes/excalidraw/03-idek-2025-08-20-10-28-21.svg" alt="03 idek 2025-08-20 10.28.21" loading="lazy"></a></figure>

- Therefore, as long as $C$ is fixed, $U$ is constant. Proof:

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-idek-2025-08-20-10-33-54.svg"><img src="/notes/excalidraw/03-idek-2025-08-20-10-33-54.svg" alt="03 idek 2025-08-20 10.33.54" loading="lazy"></a></figure>

- We can claim, then, that our solution is only dependent on $C$

$$U(x, y) = f(C) = f(\frac{y}{e^x})$$

### Change of Variable {#change-of-variable}
- Alternatively, we can find new coordinates to express the solution in the form of one derivative
	- This method is good because it allows us to solve a first-order ODE with more terms (e.g. some forcing/external thing on a system which makes it inhomogeneous)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-idek-2025-08-20-10-39-54.svg"><img src="/notes/excalidraw/03-idek-2025-08-20-10-39-54.svg" alt="03 idek 2025-08-20 10.39.54" loading="lazy"></a></figure>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.1</span> <span class="theorem-callout-subtitle">(Adding another term)</span>.</div></div>
<div class="callout-content">

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-idek-2025-08-20-10-51-32.svg"><img src="/notes/excalidraw/03-idek-2025-08-20-10-51-32.svg" alt="03 idek 2025-08-20 10.51.32" loading="lazy"></a></figure>

</div>
</div>

- If the RHS is nonzero, you have to solve a first-order system using integrating factor since it’s no longer separable
