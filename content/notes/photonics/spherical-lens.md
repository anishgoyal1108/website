---
author: "Anish Goyal"
title: "Spherical Lens"
description: "Two spherical surfaces with radii R1 and R2"
tags:
  - "notes"
  - "physics"
  - "photonics"
date: 2026-07-30T18:04:21
modified: 2026-08-16T06:19:35
readingtime: "2"
course: "Fundamentals of Photonics (Saleh & Teich)"
course_slug: "photonics"
subject: "physics"
kind: "concept"
weight: 9013
slug: "spherical-lens"
links:
  - "/notes/photonics/ray-optics/"
  - "/notes/photonics/spherical-mirror/"
sources:
  - "Saleh & Teich, Fundamentals of Photonics"
generated: true
---

##### Construction {#construction}
- Two spherical surfaces with radii $R_1$ and $R_2$
- Refractive index $n$
- Thickness $\Delta$

<a class="zoom" href="/notes/img/biconvex-spherical-lens.png"><img src="/notes/img/biconvex-spherical-lens.png" alt="biconvex spherical lens" loading="lazy"></a>

##### Tracing {#tracing}
- Ray crosses the first boundary at height $y$ with angle $\theta_1$
- $\theta_2$ is obtained via

  <div class="transclusion" data-source="04. Notes/Fundamentals of Photonics/01 Ray Optics.md">
  <a class="transclusion-source" href="/notes/photonics/ray-optics/#blk-property-1" title="Open Ray Optics"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  <div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-callout-metadata="*" data-embed-of="blk-property-1">
  <div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem</span> <span class="theorem-callout-subtitle">(Property 1)</span>.</div></div>
  <div class="callout-content">

  $$
  \theta_{2} \approx \frac{n_{1}}{n_{2}} \theta_{1} - \frac{n_{2}-n_{1}}{n_{2}} \frac{y}{R}
  $$

  - Measures how much the ray changes direction at the $z$-axis

  </div>
  </div>

  </div>

and the resulting ray is extended until the second boundary
- $\theta_2$ then becomes $\theta_1$ and the property is applied again for the exiting ray

##### "Thin Lens" Assumption {#thin-lens-assumption}
- If the lens is thin, we may assume the emergent ray has approximately the same $y$ as the incident ray. In addition to simplifying things (we only have to track two angles, not four), this yields the following properties:

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-callout-metadata="*" id="blk-property-1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem</span> <span class="theorem-callout-subtitle">(Angle Relationships and Focal Length)</span>.</div></div>
<div class="callout-content">

$$
\theta_{2} = \theta_{1} - \frac{y}{f} \quad \quad \quad \frac{1}{f} = (n-1)\left( \frac{1}{R_{1}} - \frac{1}{R_{2}} \right) 
$$

- Sign convention for $R$:
	- Convex: $R > 0$
	- Concave: $R < 0$
- For a biconvex lens, $R_1 > 0$ and $R_2 < 0$, which implies $f > 0$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/photonics/spherical-lens/#blk-property-1">Angle Relationships and Focal Length</a>.</span> (<cite class="cite cite-quote"><q>EXERCISE 1.2-4</q> <span class="cite-src">[Saleh &amp; Teich, <em>Fundamentals of Photonics</em>, p.&nbsp;181]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/spherical-lens-2026-07-30-18-17-01.svg"><img src="/notes/excalidraw/spherical-lens-2026-07-30-18-17-01.svg" alt="Spherical Lens 2026-07-30 18.17.01" loading="lazy"></a></figure>

<span class="math-booster-end-proof"></span>

</blockquote>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-callout-metadata="*" id="blk-property-2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem</span> <span class="theorem-callout-subtitle">(Imaging Equation and Magnification)</span>.</div></div>
<div class="callout-content">

For $P_1 \coloneqq (y_1, z_1)$ and $P_2 \coloneqq (y_2, z_2)$, we have:

$$
\frac{1}{z_{1}} + \frac{1}{z_{2}} = \frac{1}{f} \quad \quad \quad y_{2} = -\frac{z_{2}}{z_{1}} y_{1}
$$

- These results are identical to the <a class="internal-link" href="/notes/photonics/spherical-mirror/">Spherical Mirror</a>:
	- There is a one-to-one correspondence between the conjugate planes $(z=z_1, z=z_2) \mapsto (P_1, P_2)$ with magnification factor $m=-z_2/z_1$
	- $m=1 \iff z_1=z_2=2f$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/photonics/spherical-lens/#blk-property-2">Imaging Equation and Magnification</a>.</span> (<cite class="cite cite-quote"><q>EXERCISE 1.2-4</q> <span class="cite-src">[Saleh &amp; Teich, <em>Fundamentals of Photonics</em>, p.&nbsp;181]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/spherical-lens-2026-07-30-18-20-06.svg"><img src="/notes/excalidraw/spherical-lens-2026-07-30-18-20-06.svg" alt="Spherical Lens 2026-07-30 18.20.06" loading="lazy"></a></figure>

<span class="math-booster-end-proof"></span>

</blockquote>
