---
author: "Anish Goyal"
title: "Euler-Lagrange"
description: "Two cases (hopefully, at least... I might have to update this as time goes on):"
tags:
  - "notes"
  - "physics"
  - "photonics"
date: 2026-08-02T14:37:08
modified: 2026-08-02T15:43:00
readingtime: "1"
course: "Fundamentals of Photonics (Saleh & Teich)"
course_slug: "photonics"
subject: "physics"
kind: "concept"
weight: 9001
slug: "euler-lagrange"
links: []
sources: []
generated: true
---

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-callout-metadata="*" id="blk-euler-lagrange-equation">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem</span> <span class="theorem-callout-subtitle">(Euler-Lagrange Equation)</span>.</div></div>
<div class="callout-content">

For a functional of the form

$$\int L(x, y, z, x^{'}, y^{'}, z^{'}) \ \mathrm{d}s,$$

the path that minimizes/maximizes the integral is determined by the following equations:

$$\frac{d}{ds}\left(\frac{\partial L}{\partial x'}\right) - \frac{\partial L}{\partial x} = 0 \quad \text{(and similarly for } y, z\text{)}.$$

</div>
</div>

- Two cases (hopefully, at least... I might have to update this as time goes on):
	1. **Easy case:** The path is parametrized in terms of the arc length, $s$, so that $L(\mathbf{r}) \coloneqq \langle x(s), y(s), z(s)\rangle$ 
		- Since $\left(\frac{\mathrm{d}x}{\mathrm{d}s}\right)^2 + \left(\frac{\mathrm{d}y}{\mathrm{d}s}\right)^2 + \left(\frac{\mathrm{d}z}{\mathrm{d}s}\right)^2 = 1$, which implies $|\mathrm{d}\mathbf{r}| = ds$
		- Thus, $L = n(\mathbf{r})$ with no velocity dependence. However, the arc-length constraint must still be accounted for (typically via Lagrange multipliers), and the EL equations yield the ray equations: $\frac{d}{ds}\left(n\frac{d\mathbf{r}}{ds}\right) = \nabla n$
	2. **Hard case:** The path is parametrized in terms of an arbitrary parameter (e.g., $t$ instead of $s$)
		- The Lagrangian includes the speed factor: $L = n(\mathbf{r}(t))\sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2}$, making the EL equations more complex due to the velocity dependence, though the resulting ray path is the same 
