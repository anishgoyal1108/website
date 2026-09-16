---
author: "Anish Goyal"
title: "Prism"
description: "Characterized by the apical angle , refractive index n, and incident angle {i,1}"
tags:
  - "notes"
  - "physics"
  - "photonics"
date: 2026-07-28T21:39:25
modified: 2026-07-29T13:13:28
readingtime: "1"
course: "Fundamentals of Photonics (Saleh & Teich)"
course_slug: "photonics"
subject: "physics"
kind: "concept"
weight: 9010
slug: "prism"
links: []
sources:
  - "Course handout, Cyclic Quadrilaterals"
  - "Course handout, Introduction to Visual Optics: A Light Approach"
  - "Saleh & Teich, Fundamentals of Photonics"
generated: true
---

##### Characterization {#characterization}
- Characterized by the apical angle $\alpha$, refractive index $n$, and incident angle $\theta_{i,1}$
- Derived values: first refracted ray $\theta_{r,1}$, first angle of deviation $\theta_{d,1}$, second incident ray $\theta_{i,2}$, second refracted ray $\theta_{r,2}$, second angle of deviation $\theta_{d,2}$, and total deviation $\theta_{d}$
	- Apex-interior relation (if you are solely working with first refracted/second incident rays---requires drawing normal lines): $\alpha = \theta_{r,1} + \theta_{i,2}$
		- Calculated using <cite class="cite cite-quote"><q>cyclic quadrilaterals</q> <span class="cite-src">[Course handout, <em>Introduction to Visual Optics: A Light Approach</em>, p.&nbsp;102]</span></cite> (more on them <cite class="cite">here <span class="cite-src">[Course handout, <em>Cyclic Quadrilaterals</em>]</span></cite>)
	- Total deviation relation (easier imo---extend the path light takes, and calculate each deviation angle individually, then sum): $\theta_{d} = \theta_{d,1} + \theta_{d,2}$

<a class="zoom" href="/notes/img/apex-interior-relation.png"><img src="/notes/img/apex-interior-relation.png" alt="apex-interior relation" loading="lazy"></a>

<a class="zoom" href="/notes/img/prism-total-deviation.png"><img src="/notes/img/prism-total-deviation.png" alt="prism total deviation" loading="lazy"></a>

##### Prism Equation {#prism-equation}

$$\begin{align}
\theta_{d} &= \theta-\alpha + \sin^{-1}\left[ \sqrt{ n^2 \sin^2 \theta} \sin \alpha - \sin \theta \cos \alpha \right] \\
&\approx (n-1)\alpha \text{ (if $\theta \ll 1$)}
\end{align}$$

- <cite class="cite cite-quote"><q>Derivation</q> <span class="cite-src">[Saleh &amp; Teich, <em>Fundamentals of Photonics</em>, p.&nbsp;172]</span></cite>

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-ray-optics-2026-06-10-23-35-36.svg"><img src="/notes/excalidraw/01-ray-optics-2026-06-10-23-35-36.svg" alt="01 Ray Optics 2026-06-10 23.35.36" loading="lazy"></a></figure>
