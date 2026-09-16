---
author: "Anish Goyal"
title: "Ray Equation"
description: "In general, the way you would solve the Ray Equation is by describing the trajectory by two functions and writing {d}s {d}z { 1 + ( {{d}x}{{d}z} )^2 + (…"
tags:
  - "notes"
  - "physics"
  - "photonics"
date: 2026-08-02T13:56:15
modified: 2026-08-03T00:01:30
readingtime: "2"
course: "Fundamentals of Photonics (Saleh & Teich)"
course_slug: "photonics"
subject: "physics"
kind: "concept"
weight: 9011
slug: "ray-equation"
links:
  - "/notes/photonics/euler-lagrange/"
  - "/notes/photonics/fermats-principle/"
sources: []
generated: true
---

#### Main Equation {#main-equation}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-callout-metadata="*" id="blk-ray-equation">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem</span> <span class="theorem-callout-subtitle">(Ray Equation)</span>.</div></div>
<div class="callout-content">

Determines the trajectories of light rays in an inhomogeneous medium.

$$\frac{\mathrm{d}}{\mathrm{d}s} \left( n \frac{\mathrm{d}\mathbf{r}}{\mathrm{d}s} \right) = \nabla n $$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/photonics/ray-equation/#blk-ray-equation">Ray Equation</a>.</span>
Assume the path is parametrized by $\bf{r}(s) \coloneqq \langle x(s), y(s), z(s) \rangle$. Using

<div class="transclusion" data-source="04. Notes/Fundamentals of Photonics/Euler-Lagrange.md">
<a class="transclusion-source" href="/notes/photonics/euler-lagrange/#blk-euler-lagrange-equation" title="Open Euler-Lagrange"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-callout-metadata="*" data-embed-of="blk-euler-lagrange-equation">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem</span> <span class="theorem-callout-subtitle">(Euler-Lagrange Equation)</span>.</div></div>
<div class="callout-content">

For a functional of the form

$$\int L(x, y, z, x^{'}, y^{'}, z^{'}) \ \mathrm{d}s,$$

the path that minimizes/maximizes the integral is determined by the following equations:

$$\frac{d}{ds}\left(\frac{\partial L}{\partial x'}\right) - \frac{\partial L}{\partial x} = 0 \quad \text{(and similarly for } y, z\text{)}.$$

</div>
</div>

</div>

on <a class="internal-link" href="/notes/photonics/fermats-principle/">Fermat’s Principle</a>, we account for the arc-length constraint $\left(\frac{dx}{ds}\right)^2 + \left(\frac{dy}{ds}\right)^2 + \left(\frac{dz}{ds}\right)^2 = 1$ via Lagrange multipliers. The augmented Lagrangian is:

$$\tilde{L} = n(\mathbf{r}) + \lambda(s) \left[\left(\frac{dx}{ds}\right)^2 + \left(\frac{dy}{ds}\right)^2 + \left(\frac{dz}{ds}\right)^2 - 1\right]$$

Computing $\frac{\partial \tilde{L}}{\partial x’} = 2\lambda(s) \frac{dx}{ds}$ and applying the <a class="internal-link ref-theorem" href="/notes/photonics/euler-lagrange/#blk-euler-lagrange-equation">Euler-Lagrange equation</a>, we get:

$$\frac{d}{ds}\left(2\lambda(s) \frac{dx}{ds}\right) = \frac{\partial n}{\partial x}$$

For the actual ray trajectory, the Lagrange multiplier identifies with the refractive index: $\lambda(s) = \frac{n(\mathbf{r}(s))}{2}$. This yields three separate PDEs:

$$\begin{align}
\frac{\mathrm{d}}{\mathrm{d}s} \left( n \frac{\mathrm{d}x}{\mathrm{d}s} \right) &= \frac{\partial n}{\partial x} \\
\frac{\mathrm{d}}{\mathrm{d}s} \left( n \frac{\mathrm{d}y}{\mathrm{d}s} \right) &= \frac{\partial n}{\partial y}  \\
\frac{\mathrm{d}}{\mathrm{d}s} \left( n \frac{\mathrm{d}z}{\mathrm{d}s} \right) &= \frac{\partial n}{\partial z} 
\end{align}$$

These three equations can be compactly written as the vector equation: $\frac{d}{ds}\left(n\frac{d\mathbf{r}}{ds}\right) = \nabla n$.
<span class="math-booster-end-proof"></span>

</blockquote>

- In general, the way you would solve the Ray Equation is by describing the trajectory by two functions and writing $\mathrm{d}s = \mathrm{d}z \sqrt{ 1 + \left( \frac{\mathrm{d}x}{\mathrm{d}z} \right)^2 + \left( \frac{\mathrm{d}y}{\mathrm{d}z} \right)^2 }$

#### Paraxial Regime {#paraxial-regime}

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-callout-metadata="*" id="blk-paraxial-ray-eqs">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary</span> <span class="theorem-callout-subtitle">(Paraxial Ray Equations)</span>.</div></div>
<div class="callout-content">

Under the paraxial approximation, the trajectory is nearly parallel to the $z$-axis, such that $\mathrm{d}s \approx \mathrm{d}z$. This simplifies the Ray Equation to:

$$\frac{\mathrm{d}}{\mathrm{d}z}\left( n \frac{\mathrm{d}x}{\mathrm{d}z} \right) \approx \frac{\partial n}{\partial x}, \ \ \ \frac{\mathrm{d}}{\mathrm{d}z}\left( n \frac{\mathrm{d}y}{\mathrm{d}z} \right) \approx \frac{\partial n}{\partial y}$$

which are much easier to solve for $x(z)$ and $y(z)$.

</div>
</div>
