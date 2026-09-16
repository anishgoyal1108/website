---
author: "Anish Goyal"
title: "Optical Fiber"
description: "Conduits made of two concentric glass/plastic cylinders"
tags:
  - "notes"
  - "physics"
  - "photonics"
date: 2026-07-31T01:29:44
modified: 2026-07-31T16:08:48
readingtime: "2"
course: "Fundamentals of Photonics (Saleh & Teich)"
course_slug: "photonics"
subject: "physics"
kind: "concept"
weight: 9006
slug: "optical-fiber"
links:
  - "/notes/photonics/total-internal-reflection/"
sources:
  - "Saleh & Teich, Fundamentals of Photonics"
generated: true
---

##### Characterization {#characterization}
- Conduits made of two concentric glass/plastic cylinders
	- Core and cladding have indices $n_1$ and $n_2$ with $n_2 < n_1$ (but only slightly)
- Uses <a class="internal-link" href="/notes/photonics/total-internal-reflection/">Total Internal Reflection</a> to keep the rays confined within the core 
- Often made with silica glass (*a.k.a.* fused silica/amorphous silicon dioxide ($\text{SiO}_{2}$)) due to its excellent optical/mechanical properties
- Refractive index can be modified via doping (often with $\text{GeO}_{2}$)
 
##### TIR Reflection Condition {#tir-reflection-condition}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-callout-metadata="*">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition</span> <span class="theorem-callout-subtitle">(Notation peculiarities in this section)</span>.</div></div>
<div class="callout-content">

- My notation:
	- Overbar $\coloneqq$ *measured from the surface normal*
	- Unbarred $\coloneqq$ *measured from the optical axis*
	- Subscript $c$ marks the critical value **of the variable it is attached to**.
- This **reverses Saleh's notation in the book** (<cite class="cite">p. 185 <span class="cite-src">[Saleh &amp; Teich, <em>Fundamentals of Photonics</em>, p.&nbsp;185]</span></cite>), where $\theta_c \coloneqq \sin^{-1}(n_2/n_1)$ and $\bar{\theta}_c \coloneqq 90^\circ - \theta_c$.
	- In other words: $\bar{\theta}_{c}$ here $=$ $\theta_{c}$ in the <a class="internal-link" href="/notes/photonics/total-internal-reflection/">main TIR note</a>. The unbarred $\theta_c$ here is fiber-specific and has no counterpart there.

</div>
</div>

- Surface normal POV
	- $\bar{\theta} > \left[\overline{\theta}_{c} \coloneqq \sin^{-1}\left(\frac{n_2}{n_1}\right)\right]$
- Optical axis POV
	- $\left[\theta \coloneqq 90^{\circ} - \bar{\theta}\right] < \left[\theta_c \coloneqq 90^{\circ} - \overline{\theta}_{c} = \cos^{-1}\left(\frac{n_2}{n_1}\right)\right]$

<a class="zoom" href="/notes/img/fiber-optic.png"><img src="/notes/img/fiber-optic.png" alt="fiber optic" loading="lazy"></a>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-callout-metadata="*" id="blk-theorem-cone-acceptable-rays">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem</span> <span class="theorem-callout-subtitle">(Cone of Acceptable Rays)</span>.</div></div>
<div class="callout-content">

The cone of acceptable rays without undergoing refraction at the cladding is characterized by the half-angle, $\theta_a$, (*a.k.a.* the **acceptance angle**):

$$\theta_{a} = \sin^{-1}\left( \sqrt{ n_{1}^2 - n_{2}^2} \right)$$ 

with the **numerical aperture** equal to

$$\text{NA} = \sin \theta_{a} = \sqrt{ n_{1}^2 - n_{2}^2}.$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/photonics/optical-fiber/#blk-theorem-cone-acceptable-rays">Cone of Acceptable Rays</a>.</span> (<cite class="cite cite-quote"><q>EXERCISE 1.2-5</q> <span class="cite-src">[Saleh &amp; Teich, <em>Fundamentals of Photonics</em>, p.&nbsp;187]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/optical-fiber-2026-07-31-01-47-42.svg"><img src="/notes/excalidraw/optical-fiber-2026-07-31-01-47-42.svg" alt="Optical Fiber 2026-07-31 01.47.42" loading="lazy"></a></figure>

<span class="math-booster-end-proof"></span>

</blockquote>
