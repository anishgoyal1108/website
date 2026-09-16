---
author: "Anish Goyal"
title: "Ray Optics"
description: "Light travels in the form of rays"
tags:
  - "notes"
  - "physics"
  - "photonics"
date: 2026-05-27T17:34:38
modified: 2026-08-26T22:17:56
readingtime: "27"
course: "Fundamentals of Photonics (Saleh & Teich)"
course_slug: "photonics"
subject: "physics"
kind: "lecture"
ordinal: 1
weight: 10
slug: "ray-optics"
links:
  - "/notes/photonics/elliptical-mirror/"
  - "/notes/photonics/euler-lagrange/"
  - "/notes/photonics/fermats-principle/"
  - "/notes/photonics/heros-principle/"
  - "/notes/photonics/law-of-reflection/"
  - "/notes/photonics/law-of-refraction/"
  - "/notes/photonics/optical-fiber/"
  - "/notes/photonics/paraboloidal-mirror/"
  - "/notes/photonics/paraxial-ray/"
  - "/notes/photonics/planar-mirror/"
  - "/notes/photonics/prism/"
  - "/notes/photonics/ray-equation/"
  - "/notes/photonics/snells-law/"
  - "/notes/photonics/spherical-lens/"
  - "/notes/photonics/spherical-mirror/"
  - "/notes/photonics/total-internal-reflection/"
sources:
  - "Course handout, Cyclic Quadrilaterals"
  - "Course handout, Introduction to Ophthalmic Optics"
  - "Course handout, Introduction to Visual Optics: A Light Approach"
  - "Saleh & Teich, Fundamentals of Photonics"
generated: true
---

## Postulates of Ray Optics {#postulates-of-ray-optics}
### Basic Postulates {#basic-postulates}
- Light travels in the form of rays
- Optical media are characterized by their refractive index $n = c_0 / c$ with the time taken to travel a distance $d = nd / c_0$
	- The quantity $nd$ is the optical pathlength and is directly proportional to the time taken
- Inhomogeneous media have $n(\bf{r})$ and the optical pathlength between $A$ and $B$ is therefore $\int_{A}^{B} n(\bf{r}) \ \mathrm{d}s$

- <div class="transclusion" data-source="04. Notes/Fundamentals of Photonics/Fermat’s Principle.md">
  <a class="transclusion-source" href="/notes/photonics/fermats-principle/" title="Open Fermat’s Principle"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  <div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-callout-metadata="*">
  <div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition</span> <span class="theorem-callout-subtitle">(Fermat’s Principle)</span>.</div></div>
  <div class="callout-content">

  Optical rays travel along the path of least time.

  $$\delta \int_{A}^{B} n (\bf{r}) \ \mathrm{d}s = 0$$

  where $\delta$ is “the variation of” and signifies the optical pathlength is a point of inflection/minima/maxima (almost always a minima)

  </div>
  </div>

  </div>

	- If there is a tie between many minimum-time paths, the rays take all paths simultaneously

### Homogeneous Media {#homogeneous-media}
- Rays travel in straight lines

- <div class="transclusion" data-source="04. Notes/Fundamentals of Photonics/Hero’s Principle.md">
  <a class="transclusion-source" href="/notes/photonics/heros-principle/" title="Open Hero’s Principle"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  <div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-callout-metadata="*">
  <div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition</span> <span class="theorem-callout-subtitle">(Hero’s Principle)</span>.</div></div>
  <div class="callout-content">

  In a homogeneous medium, the minimum-time path (required by <a class="internal-link" href="/notes/photonics/fermats-principle/">Fermat’s Principle</a>) is also the path of minimum distance

  </div>
  </div>

  </div>

### Reflection from a Mirror {#reflection-from-a-mirror}

<div class="transclusion" data-source="04. Notes/Fundamentals of Photonics/Law of Reflection.md">
<a class="transclusion-source" href="/notes/photonics/law-of-reflection/" title="Open Law of Reflection"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-callout-metadata="*">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition</span> <span class="theorem-callout-subtitle">(Law of Reflection)</span>.</div></div>
<div class="callout-content">

1. Reflected rays lie in the plane of incidence
2. The angle of reflection $\theta’$ equals the angle of incidence $\theta$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>
We will show that $\overline{AB} + \overline{BC}$ is the shortest possible path by <a class="internal-link" href="/notes/photonics/heros-principle/">Hero’s Principle</a>. 

Observe that $\overline{BC} = \overline{BC’}$; therefore, $\overline{AB} + \overline{BC’}$ must also be the shortest length. By coinciding $B$ with $B’$, we can see a straight line $\overline{AB’C’}$ connecting $A$ to $C’$. 

Thus, $\overline{AB} + \overline{BC}$ is the shortest path and $\theta = \theta’$.
<span class="math-booster-end-proof"></span>

</blockquote>

<a class="zoom" href="/notes/img/mirror-reflection.png"><img src="/notes/img/mirror-reflection.png" alt="mirror reflection" loading="lazy"></a>

</div>

### Refraction Between Media {#refraction-between-media}
- At the boundary between two media, an incident ray is split into two
	- One ray obeys the <a class="internal-link" href="/notes/photonics/law-of-reflection/">Law of Reflection</a>
	- The other ray obeys the

      <div class="transclusion" data-source="04. Notes/Fundamentals of Photonics/Law of Refraction.md">
      <a class="transclusion-source" href="/notes/photonics/law-of-refraction/" title="Open Law of Refraction"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

      <div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-callout-metadata="*">
      <div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition</span> <span class="theorem-callout-subtitle">(Law of Refraction)</span>.</div></div>
      <div class="callout-content">

      1. The refracted ray lies in the plane of incidence
      2. The angle of incidence $\theta_1$ and angle of refraction $\theta_2$ are related by <a class="internal-link ref-equation" href="/notes/photonics/snells-law/#blk-equation">Snell’s Law</a>
      	- Linear (small-angle) approximation: $n_1 \theta_{1} \approx n_{2} \theta_{2} \implies \theta_{2} \approx \left(\frac{n_{1}}{n_{2}}\right)\theta_{1}$
      3. A third angle, the angle of deviation, represents <cite class="cite cite-quote"><q>the difference between the angles of incidence and refraction</q> <span class="cite-src">[Course handout, <em>Introduction to Ophthalmic Optics</em>, p.&nbsp;15]</span></cite>
      	- Since it lies between $\theta_{1}$ and $\theta_{2}$, $\theta_{d} \coloneqq \theta_{1} - \theta_{2}$

      </div>
      </div>

      <a class="zoom" href="/notes/img/law-of-refraction.png"><img src="/notes/img/law-of-refraction.png" alt="law of refraction" loading="lazy"></a>

      </div>

## Simple Optical Components {#simple-optical-components}

### Mirrors {#mirrors}

- <div class="transclusion" data-source="04. Notes/Fundamentals of Photonics/Planar Mirror.md">
  <a class="transclusion-source" href="/notes/photonics/planar-mirror/" title="Open Planar Mirror"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  Reflects rays originating from the front of the mirror (*i.e.,* $P_1$) such that the reflected ray forms a directed line segment with a collinear point behind the mirror (*i.e.,* $P_2$)

  <a class="zoom" href="/notes/img/planar-mirror.png"><img src="/notes/img/planar-mirror.png" alt="planar mirror" loading="lazy"></a>

  </div>

- <div class="transclusion" data-source="04. Notes/Fundamentals of Photonics/Paraboloidal Mirror.md">
  <a class="transclusion-source" href="/notes/photonics/paraboloidal-mirror/" title="Open Paraboloidal Mirror"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  - The surface of this mirror is a paraboloid
  - Focuses rays that are parallel to its axis at a single point, called the *focus*
  	- The distance from the vertex to the focus is the focal length
  - Can be used as a collimator
  	- A point source/beam with divergent rays is placed near the focus of a paraboloidal mirror, which causes the rays to become parallel and form a straight line by the <a class="internal-link" href="/notes/photonics/law-of-reflection/">Law of Reflection</a>

  <a class="zoom" href="/notes/img/paraboloidal-mirror.png"><img src="/notes/img/paraboloidal-mirror.png" alt="paraboloidal mirror" loading="lazy"></a>

  </div>

- <div class="transclusion" data-source="04. Notes/Fundamentals of Photonics/Elliptical Mirror.md">
  <a class="transclusion-source" href="/notes/photonics/elliptical-mirror/" title="Open Elliptical Mirror"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  - Reflects all rays originating from one focus, $P_1$, into the other focus, $P_2$
  - All paths taken from $P_1$ to $P_2$ are the same distance and thus taken simultaneously by <a class="internal-link" href="/notes/photonics/heros-principle/">Hero’s Principle</a>

  <a class="zoom" href="/notes/img/elliptical-mirror.png"><img src="/notes/img/elliptical-mirror.png" alt="elliptical mirror" loading="lazy"></a>

  </div>

- <div class="transclusion" data-source="04. Notes/Fundamentals of Photonics/Spherical Mirror.md">
  <a class="transclusion-source" href="/notes/photonics/spherical-mirror/" title="Open Spherical Mirror"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  - Mirror in the shape of a sphere
  - Different parallel rays focus on the axis at different points
  	- Rays that are close enough to the axis will approximately focus at $\frac{R}{2}$ from the center
  	- This is due to the *small angle approximation* ($\sin \theta \approx \theta$), and the rays are known as <a class="internal-link" href="/notes/photonics/paraxial-ray/">paraxial rays</a>
  - Can be concave or convex
  	- The radius of curvature, $R$, is negative for concave mirrors and positive for convex mirrors
  - More on paraxial rays
  	- There is a one-to-one correspondence between paraxial rays originating from points on the mirror axis and their destination (image) points, which also lie on the mirror axis
  	- Using angle relationships, we have $\theta_{1} = \theta_{0}-\theta \implies 2\theta_{0} = \theta_{1} + (-\theta_{2})$
  		- If $\theta_0$ is small enough, $\tan \theta_{0} \approx \theta_{0}$, which gives $\frac{2y}{(-R)} \approx \theta_{1} + (-\theta_{2})$
  		- And if $\theta_1$ and $(-\theta_2)$ are small enough, we have $\frac{2}{(-R)} \approx \frac{1}{z_{1}} + \frac{1}{z_{2}}$
  			- If $z_1 = \infty$, then $z_2 = \frac{(-R)}{2} = f$. This results in the imaging equation for paraxial rays:

  $$\frac{1}{f} \approx \frac{1}{z_{1}} + \frac{1}{z_{2}}$$

  <a class="zoom" href="/notes/img/concave-spherical-mirror.png"><img src="/notes/img/concave-spherical-mirror.png" alt="concave spherical mirror" loading="lazy"></a>

  <a class="zoom" href="/notes/img/paraxial-correspondence.png"><img src="/notes/img/paraxial-correspondence.png" alt="paraxial correspondence" loading="lazy"></a>

  <figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/spherical-mirror-2026-06-08-17-16-54.svg"><img src="/notes/excalidraw/spherical-mirror-2026-06-08-17-16-54.svg" alt="Spherical Mirror 2026-06-08 17.16.54" loading="lazy"></a></figure>

  </div>

### Planar Boundaries {#planar-boundaries}
#### Types of Refraction {#types-of-refraction}
- **External refraction** ($n_1 < n_2 \implies \theta_{1} > \theta_{2}$) 
	- Incident ray from smaller refractive material
	- Refracted ray bends *away* from the boundary
- <span class="block-anchor" id="blk-27aa4c"></span>**Internal refraction** ($n_1 > n_2 \implies \theta_{1} < \theta_{2}$)
	- Incident ray from larger refractive material
	- Refracted ray bends *toward* the boundary

<a class="zoom" href="/notes/img/external-and-internal-refraction.png"><img src="/notes/img/external-and-internal-refraction.png" alt="external and internal refraction" loading="lazy"></a>

#### Total Internal Reflection {#total-internal-reflection}

<div class="transclusion" data-source="04. Notes/Fundamentals of Photonics/Total Internal Reflection.md">
<a class="transclusion-source" href="/notes/photonics/total-internal-reflection/" title="Open Total Internal Reflection"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

- A special case of <a class="internal-link" href="/notes/photonics/law-of-refraction/">Internal Refraction</a> in which <a class="internal-link" href="/notes/photonics/snells-law/">Snell’s Law</a> cannot be physically satisfied
	- This is because $\theta_2$ is capped at $\frac{\pi}{2}$ rad, so beyond some critical $\theta_{c} \coloneqq \sin^{-1} \frac{n_{2}}{n_{1}}$, the planar boundary is treated like a normal <a class="internal-link" href="/notes/photonics/law-of-reflection/">reflecting surface</a>

</div>

<a class="zoom" href="/notes/img/total-internal-reflection.png"><img src="/notes/img/total-internal-reflection.png" alt="total internal reflection" loading="lazy"></a>

#### Prisms {#prisms}

- <div class="transclusion" data-source="04. Notes/Fundamentals of Photonics/Prism.md">
  <a class="transclusion-source" href="/notes/photonics/prism/" title="Open Prism"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  ##### Characterization {#characterization-embed10}
  - Characterized by the apical angle $\alpha$, refractive index $n$, and incident angle $\theta_{i,1}$
  - Derived values: first refracted ray $\theta_{r,1}$, first angle of deviation $\theta_{d,1}$, second incident ray $\theta_{i,2}$, second refracted ray $\theta_{r,2}$, second angle of deviation $\theta_{d,2}$, and total deviation $\theta_{d}$
  	- Apex-interior relation (if you are solely working with first refracted/second incident rays---requires drawing normal lines): $\alpha = \theta_{r,1} + \theta_{i,2}$
  		- Calculated using <cite class="cite cite-quote"><q>cyclic quadrilaterals</q> <span class="cite-src">[Course handout, <em>Introduction to Visual Optics: A Light Approach</em>, p.&nbsp;102]</span></cite> (more on them <cite class="cite">here <span class="cite-src">[Course handout, <em>Cyclic Quadrilaterals</em>]</span></cite>)
  	- Total deviation relation (easier imo---extend the path light takes, and calculate each deviation angle individually, then sum): $\theta_{d} = \theta_{d,1} + \theta_{d,2}$

  <a class="zoom" href="/notes/img/apex-interior-relation.png"><img src="/notes/img/apex-interior-relation.png" alt="apex-interior relation" loading="lazy"></a>

  <a class="zoom" href="/notes/img/prism-total-deviation.png"><img src="/notes/img/prism-total-deviation.png" alt="prism total deviation" loading="lazy"></a>

  ##### Prism Equation {#prism-equation-embed10}

  $$\begin{align}
  \theta_{d} &= \theta-\alpha + \sin^{-1}\left[ \sqrt{ n^2 \sin^2 \theta} \sin \alpha - \sin \theta \cos \alpha \right] \\
  &\approx (n-1)\alpha \text{ (if $\theta \ll 1$)}
  \end{align}$$

  - <cite class="cite cite-quote"><q>Derivation</q> <span class="cite-src">[Saleh &amp; Teich, <em>Fundamentals of Photonics</em>, p.&nbsp;172]</span></cite>

  <figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-ray-optics-2026-06-10-23-35-36.svg"><img src="/notes/excalidraw/01-ray-optics-2026-06-10-23-35-36.svg" alt="01 Ray Optics 2026-06-10 23.35.36" loading="lazy"></a></figure>

  </div>

#### Beamsplitters {#beamsplitters}
- Splits rays into a reflected and transmitted ray
	- Proportions of light split are determined by Fresnel&#x27;s equations
- Also used to combine two rays into one
- Constructed via a thin metallic/dielectric film on a glass substrate

<a class="zoom" href="/notes/img/beamsplitter.png"><img src="/notes/img/beamsplitter.png" alt="beamsplitter" loading="lazy"></a>

#### Beam Directors {#beam-directors}
- Direct rays in arbitrary directions
- Biprism moves incident rays towards the central axis
	- *Simplest biprism* is a normal prism and inverted prism combined together into one isosceles triangle
	- *Fresnel biprism* is functionally identical to the simplest biprism but is formed from rows of adjacent, tiny prisms
	- Plano-convex *axicon* is a cone that collects incident rays in a circle and directs them towards the central axis (not just laterally like the first two; literally ALONG the central line)---shares the same cross section as simplest biprism (isosceles triangle)

<a class="zoom" href="/notes/img/beam-directors.png"><img src="/notes/img/beam-directors.png" alt="beam directors" loading="lazy"></a>

### Spherical Boundaries and Lenses {#spherical-boundaries-and-lenses}
#### Spherical Boundaries {#spherical-boundaries}
- Consider a spherical boundary with radius $R$ between two media with refractive indices $n_1$ and $n_2$
	- Recall sign convention: $R > 0$ for convex; $R < 0$ for concave (obtained using <a class="internal-link" href="/notes/photonics/snells-law/">Snell’s Law</a>)
- In the <a class="internal-link" href="/notes/photonics/paraxial-ray/">paraxial regime</a>, the following properties hold:
	- If the ray is not paraxial, there is additional deviation in the rays; this causes image distortion called *aberration*

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-callout-metadata="*" id="blk-property-1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem</span> <span class="theorem-callout-subtitle">(Property 1)</span>.</div></div>
<div class="callout-content">

$$
\theta_{2} \approx \frac{n_{1}}{n_{2}} \theta_{1} - \frac{n_{2}-n_{1}}{n_{2}} \frac{y}{R}
$$

- Measures how much the ray changes direction at the $z$-axis

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/photonics/ray-optics/#blk-property-1">Property 1</a>.</span> (<cite class="cite cite-quote"><q>EXERCISE 1.2-2</q> <span class="cite-src">[Saleh &amp; Teich, <em>Fundamentals of Photonics</em>, p.&nbsp;177]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-ray-optics-2026-07-29-16-09-02.svg"><img src="/notes/excalidraw/01-ray-optics-2026-07-29-16-09-02.svg" alt="01 Ray Optics 2026-07-29 16.09.02" loading="lazy"></a></figure>

<span class="math-booster-end-proof"></span>

</blockquote>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-callout-metadata="*" id="blk-property-2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem</span> <span class="theorem-callout-subtitle">(Property 2)</span>.</div></div>
<div class="callout-content">

$$
\frac{n_1}{z_{1}} + \frac{n_{2}}{z_{2}} \approx \frac{n_{2}-n_{1}}{R}
$$

- The image location is determined by the indices of refraction, surface curvature, and object location
- The refracting power (RHS) is directly proportional to the index difference and curvature ($1/R$)

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-callout-metadata="*" id="blk-property-3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem</span> <span class="theorem-callout-subtitle">(Property 3)</span>.</div></div>
<div class="callout-content">

$$
y_{2} = -\frac{n_{1}}{n_{2}} \frac{z_{2}}{z_{1}}y_{1}
$$

- Every point in the plane $z=z_1$ has an associated image in the plane $z=z_2$ with magnification $-\frac{n_{1}}{n_{2}} \frac{z_{2}}{z_{1}}$
- $z_1, z_2$ are thus said to be *conjugate planes*

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/photonics/ray-optics/#blk-property-2">Property 2</a> AND <a class="internal-link ref-theorem" href="/notes/photonics/ray-optics/#blk-property-3">Property 3</a>.</span> (<cite class="cite cite-quote"><q>EXERCISE 1.2-2</q> <span class="cite-src">[Saleh &amp; Teich, <em>Fundamentals of Photonics</em>, p.&nbsp;177]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-ray-optics-2026-07-30-00-55-40.svg"><img src="/notes/excalidraw/01-ray-optics-2026-07-30-00-55-40.svg" alt="01 Ray Optics 2026-07-30 00.55.40" loading="lazy"></a></figure> 

<span class="math-booster-end-proof"></span>

</blockquote>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-callout-metadata="*">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise</span> <span class="theorem-callout-subtitle">(Aberration-Free Imaging Surface)</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 1.2-3</q> <span class="cite-src">[Saleh &amp; Teich, <em>Fundamentals of Photonics</em>, p.&nbsp;177]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-ray-optics-2026-07-30-14-38-02.svg"><img src="/notes/excalidraw/01-ray-optics-2026-07-30-14-38-02.svg" alt="01 Ray Optics 2026-07-30 14.38.02" loading="lazy"></a></figure>

</div>
</div>

#### LED Collimators {#led-collimators}
- Combines a spherical and paraboloidal boundary
	- <a class="internal-link" href="/notes/photonics/total-internal-reflection/">TIR</a> is used at the paraboidal boundary causing the rays to reflect upward
	- Normal refraction is used at at the spherical boundary
- An example of a *catadioptric system*: combines reflection and refraction

<a class="zoom" href="/notes/img/led-collimator.png"><img src="/notes/img/led-collimator.png" alt="led collimator" loading="lazy"></a>

#### Spherical Lenses {#spherical-lenses}

<div class="transclusion" data-source="04. Notes/Fundamentals of Photonics/Spherical Lens.md">
<a class="transclusion-source" href="/notes/photonics/spherical-lens/" title="Open Spherical Lens"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

##### Construction {#construction-embed11}
- Two spherical surfaces with radii $R_1$ and $R_2$
- Refractive index $n$
- Thickness $\Delta$

<a class="zoom" href="/notes/img/biconvex-spherical-lens.png"><img src="/notes/img/biconvex-spherical-lens.png" alt="biconvex spherical lens" loading="lazy"></a>

##### Tracing {#tracing-embed11}
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

##### "Thin Lens" Assumption {#thin-lens-assumption-embed12}
- If the lens is thin, we may assume the emergent ray has approximately the same $y$ as the incident ray. In addition to simplifying things (we only have to track two angles, not four), this yields the following properties:

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-callout-metadata="*" data-embed-of="blk-property-1">
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

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-callout-metadata="*" data-embed-of="blk-property-2">
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

</div>

#### Convex and Concave Lenses {#convex-and-concave-lenses}
##### Types {#types}
- Materials
	- Made of one material: *simple* lens
	- Made of multiple simple materials (usually along a common axis): *compound* lens
- Surface
	- Convex: projects out of the lens body
	- Concave: recedes into the lens body
	- Planar: flat surface
	- **Cylindrical**: curved in only one direction
		- Only has focusing power for $y-z$ plane (not $x-z$ plane) as a result
	- **Meniscus**: One surface is convex and the other concave
	- **Aspheric**: One or both surfaces are neither spherical/cylindrical
	
- Utility
	- Biconvex/plano-convex: ray convergenceimage formation
	- Biconcave/plano-concave: ray divergence/projection/focal-length expansion
	- **Fresnel**: remove all nonrefracting parts of a conventional lens (a full)
		- Example: Fresnel equivalent of a plano-convex lens is a flattened set of concentric surfaces with identical curvature at all locations
		- Allows for construction of thin/light/inexpensive plastic lenses with variable size and short foci
		- Can be converging/diverging/cylindrical

<a class="zoom" href="/notes/img/different-lenses.png"><img src="/notes/img/different-lenses.png" alt="different lenses" loading="lazy"></a>

#### Light Guides {#light-guides}
- Using mirrors and lenses to guide rays from one location to another
- Optical power losses occur as more elements are added to the system, since lenses are partially reflective and mirrors are partially absorptive

<div class="transclusion" data-source="04. Notes/Fundamentals of Photonics/Optical Fiber.md">
<a class="transclusion-source" href="/notes/photonics/optical-fiber/" title="Open Optical Fiber"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

##### Characterization {#characterization-embed13}
- Conduits made of two concentric glass/plastic cylinders
	- Core and cladding have indices $n_1$ and $n_2$ with $n_2 < n_1$ (but only slightly)
- Uses <a class="internal-link" href="/notes/photonics/total-internal-reflection/">Total Internal Reflection</a> to keep the rays confined within the core 
- Often made with silica glass (*a.k.a.* fused silica/amorphous silicon dioxide ($\text{SiO}_{2}$)) due to its excellent optical/mechanical properties
- Refractive index can be modified via doping (often with $\text{GeO}_{2}$)
 
##### TIR Reflection Condition {#tir-reflection-condition-embed13}

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

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-callout-metadata="*" data-embed-of="blk-theorem-cone-acceptable-rays">
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

</div>

#### Light Trapping {#light-trapping}
- Light inside a medium with $n \gg 0$ can be "trapped" from entering air if the surfaces of the medium are parallel
	- The rays can undergo multiple <a class="internal-link" href="/notes/photonics/total-internal-reflection/">TIRs</a> without refracting into air 

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-callout-metadata="*">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise</span> <span class="theorem-callout-subtitle">(Light Trapped in an LED)</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 1.2-6</q> <span class="cite-src">[Saleh &amp; Teich, <em>Fundamentals of Photonics</em>, p.&nbsp;189]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-ray-optics-2026-07-31-16-17-02.svg"><img src="/notes/excalidraw/01-ray-optics-2026-07-31-16-17-02.svg" alt="01 Ray Optics 2026-07-31 16.17.02" loading="lazy"></a></figure>

</div>
</div>

## Graded-Index Optics {#graded-index-optics}
- Graded-index (GRIN) materials have $n \equiv n(\bf{r})$
	- This causes curvature in light rays
- Fabricated via impurities of controlled concentrations
- Based on the $n(\bf{r})$, the GRIN can emulate a conventional optical component (prism/lens)

### The Ray Equation {#the-ray-equation}

<div class="transclusion" data-source="04. Notes/Fundamentals of Photonics/Ray Equation.md">
<a class="transclusion-source" href="/notes/photonics/ray-equation/" title="Open Ray Equation"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

#### Main Equation {#main-equation-embed14}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-callout-metadata="*" data-embed-of="blk-ray-equation">
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

#### Paraxial Regime {#paraxial-regime-embed15}

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-callout-metadata="*" data-embed-of="blk-paraxial-ray-eqs">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary</span> <span class="theorem-callout-subtitle">(Paraxial Ray Equations)</span>.</div></div>
<div class="callout-content">

Under the paraxial approximation, the trajectory is nearly parallel to the $z$-axis, such that $\mathrm{d}s \approx \mathrm{d}z$. This simplifies the Ray Equation to:

$$\frac{\mathrm{d}}{\mathrm{d}z}\left( n \frac{\mathrm{d}x}{\mathrm{d}z} \right) \approx \frac{\partial n}{\partial x}, \ \ \ \frac{\mathrm{d}}{\mathrm{d}z}\left( n \frac{\mathrm{d}y}{\mathrm{d}z} \right) \approx \frac{\partial n}{\partial y}$$

which are much easier to solve for $x(z)$ and $y(z)$.

</div>
</div>

</div>

### Graded-Index Optical Components {#graded-index-optical-components}
- GRIN Slab
	- A slab of material with $n$ uniform in the $x$ and $z$ directions and varying in the $y$ direction
	- Special variant: SELFOC Slabs have a parabolic profile with $\alpha^2 y^2 \ll 1$
- GRIN Fiber
	- A glass cylinder with $n$ dependent on radial distance
	- Commonly used in optical fibers

#### Graded-Index Slab {#graded-index-slab}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-callout-metadata="*" id="blk-grin-relation">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition</span> <span class="theorem-callout-subtitle">(GRIN Slab Relation)</span>.</div></div>
<div class="callout-content">

For a slab with $n=n(y)$, the rays in the $yz$-plane are described by:

$$\frac{\mathrm{d}}{\mathrm{d}z}\left( n \frac{\mathrm{dy}}{\mathrm{d}z} \right) = \frac{\mathrm{d}n}{\mathrm{d}y}, $$

which implies

$$\frac{\mathrm{d}^2y}{\mathrm{d}z^2} = \frac{1}{n(y)} \frac{\mathrm{d}n(y)}{\mathrm{d}y},$$

which may be solved from ICs ($y(0)=y_0,\frac{\mathrm{d}y}{\mathrm{d}z}(0)=\theta_0$) to solve for $y(z)$.

</div>
</div>

<a class="zoom" href="/notes/img/grin-slab.png"><img src="/notes/img/grin-slab.png" alt="GRIN slab" loading="lazy"></a>

##### Alternative Derivation of GRIN Slab Relation {#alternative-derivation-of-grin-slab-relation}
-  Using <a class="internal-link" href="/notes/photonics/snells-law/">Snell’s Law</a>, we can arrive at the same result:

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-ray-optics-2026-08-02-15-57-54.svg"><img src="/notes/excalidraw/01-ray-optics-2026-08-02-15-57-54.svg" alt="01 Ray Optics 2026-08-02 15.57.54" loading="lazy"></a></figure>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-callout-metadata="*">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example</span> <span class="theorem-callout-subtitle">(Slab with Parabolic Index Profile)</span>.</div></div>
<div class="callout-content">

A common distribution for GRIN slabs is parabolic, known by the trade name SELFOC:

$$n^2(y) = n_{0}^2(1-\alpha^2y^2)$$

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-ray-optics-2026-08-02-17-53-08.svg"><img src="/notes/excalidraw/01-ray-optics-2026-08-02-17-53-08.svg" alt="01 Ray Optics 2026-08-02 17.53.08" loading="lazy"></a></figure>

- It's symmetric in $y$ and maxes at $y=0$
- $n_{0}$ decreases radially/transversely from the center to the edges
	- Since the drop off is substantial, $\frac{n_{0}}{n} \ll 1$
- $\alpha$ is chosen to be sufficiently small such that $\alpha^2y^2 \ll 1$
	- This allows for $n(y) = n_{0}\sqrt{ 1-\alpha^2y^2 } \approx n_{0}\left( 1-\frac{1}{2}\alpha^2 y^2\right)$

We solve for the final ray trajectory below:

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-ray-optics-2026-08-02-19-27-48.svg"><img src="/notes/excalidraw/01-ray-optics-2026-08-02-19-27-48.svg" alt="01 Ray Optics 2026-08-02 19.27.48" loading="lazy"></a></figure>

The ray oscillates around $y_0$ with a period $\frac{2\pi}{\alpha}$, known as the *pitch*
<a class="zoom" href="/notes/img/parabolic-grin-slab-ray-trajectory.png"><img src="/notes/img/parabolic-grin-slab-ray-trajectory.png" alt="parabolic grin slab ray trajectory" loading="lazy"></a>
- Additional important characteristics of note:
	- $y_{\text{max}} = \sqrt{ y_{0}^2 + \left( \frac{\theta_{0}}{\alpha} \right)^2  }$
	- $\theta_{\text{max}} = \alpha y_{\text{max}}$
	- *Ray confinement:* the rays stay confined to the SELFOC slab via <a class="internal-link" href="/notes/photonics/total-internal-reflection/">TIR</a> iff $2y_{\text{max}} < \text{slab thickness}$
- One important condition for this analysis to hold:
	- **$\theta_{\text{max}}$ is still paraxial**: the max angle maintaining paraxiality implies that the ray trajectory approximation is indeed valid for all values of $z$ (*i.e.,* $theta$ doesn't grow unbounded)  

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-callout-metadata="*">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise</span> <span class="theorem-callout-subtitle">(The GRIN Slab as a Lens)</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 1.3-1</q> <span class="cite-src">[Saleh &amp; Teich, <em>Fundamentals of Photonics</em>, p.&nbsp;197]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-ray-optics-2026-08-02-20-45-50.svg"><img src="/notes/excalidraw/01-ray-optics-2026-08-02-20-45-50.svg" alt="01 Ray Optics 2026-08-02 20.45.50" loading="lazy"></a></figure>

</div>
</div>

#### Graded-Index Fibers {#graded-index-fibers}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-callout-metadata="*">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition</span> <span class="theorem-callout-subtitle">(GRIN Fiber Relation)</span>.</div></div>
<div class="callout-content">

Consider the sample distribution $n^2 = n_{0}^{2}\left[ 1-\alpha^2(x^2 + y^2) \right].$
Plugging it into the <a class="internal-link ref-theorem" href="/notes/photonics/ray-equation/#blk-paraxial-ray-eqs">Ray Equation &gt; Paraxial Ray Equations</a> and assuming $\alpha_{2}(x+y_{2}) \ll 1$ for all $(x, y)$ of interest, we obtain:

$$\frac{\mathrm{d}^2 x}{\mathrm{d}z^2} \approx -\alpha^2 x, \ \ \ \frac{\mathrm{d^2 y}}{\mathrm{d}z^2}\approx-\alpha^2 y.$$

Thus, both $x(z), y(z)$ are harmonic with $T=\frac{2\pi}{\alpha}$.
The ICs $(x_0, y_0)$ and $(\theta_{x, 0}, \theta_{y, 0})$ determine the amplitude and phase.

If we let $x_0 = 0$ (valid because the solutions are axially symmetric), our solutions take the form:

$$\begin{align}
x(z) &= \frac{\theta_{x, 0}}{\alpha} \sin \alpha z \\
y(z) &= \frac{\theta_{y,0}}{\alpha} \sin \alpha z + y_{0} \cos \alpha z.
\end{align}$$

</div>
</div>

- Two cases:
	1. If $\theta_{x,0}=0$, the ray lines in a meridional plane through the cylinder axis; it follows a sinusoid like the <a class="internal-link" href="/notes/photonics/ray-optics/#graded-index-slab">Graded-Index Slab</a>
	2. If $\theta_{y,0}=0$ and $\theta_{x,0}=\alpha y_0$, then the ray becomes a helix that wraps a cylinder with radius $y_0$. In this case, $x(z) = y_0 \sin \alpha z$ and $y(z) = y_0 \cos \alpha z$.

<a class="zoom" href="/notes/img/grin-fiber.png"><img src="/notes/img/grin-fiber.png" alt="GRIN fiber" loading="lazy"></a>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-callout-metadata="*">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise</span> <span class="theorem-callout-subtitle">(Numerical Aperture of the Graded-Index Fiber)</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 1.3-2</q> <span class="cite-src">[Saleh &amp; Teich, <em>Fundamentals of Photonics</em>, p.&nbsp;200]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-ray-optics-2026-08-03-00-40-37.svg"><img src="/notes/excalidraw/01-ray-optics-2026-08-03-00-40-37.svg" alt="01 Ray Optics 2026-08-03 00.40.37" loading="lazy"></a></figure>

</div>
</div>

### The Eikonal Equation {#the-eikonal-equation}
- Ray trajectories are often characterized by the surface normal
- The **eikonal** is a scalar function whose level surfaces define the direction of the ray trajectories via the normal
	- This follows from the fact that the normal to any level surface is always the gradient

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-callout-metadata="*">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition</span> <span class="theorem-callout-subtitle">(The Eikonal Equation)</span>.</div></div>
<div class="callout-content">

In order to obey <a class="internal-link" href="/notes/photonics/fermats-principle/">Fermat’s Principle</a>, the eikonal must satisfy:

$$|\nabla S|^2 = n^2.$$

For this reason, ray optics can be derived *ab initio* via Fermat's Principle or the Eikonal Equation. By the Fundamental Theorem of Line Integrals, we have $S(\bf{r}_B)-S(\bf{r}_A)$ as the optical path length (line integral of $n$ from $A$ to $B$).

</div>
</div>

<a class="zoom" href="/notes/img/level-surfaces-eikonal.png"><img src="/notes/img/level-surfaces-eikonal.png" alt="level surfaces eikonal" loading="lazy"></a>

## Matrix Optics {#matrix-optics}
- Matrix optics is a technique for ray tracing
- Under this formalism, all rays are assumed to lie within a single plane and be paraxial
	- The positions and angles of the input and output planes are related by linear equations, which can then be encoded as a *ray-transfer matrix*
- Highly convenient because the procedure generalizes for wider systems
	- The RT matrix for a cascade of optical components/systems is a product of the RT matrices of the individual components

### The RT Matrix {#the-rt-matrix}
- Consider a circularly symmetric system with many optical components centered around the $z$-axis
	- Rays in the $yz$-plane containing the optical axis cross two transverse planes at $z_1$ and $z_2$ are different axial distances
	- These rays are characterized by the $y$-coordinate of the crossing point and angle with the normal, $\theta$

<a class="zoom" href="/notes/img/optical-system.png"><img src="/notes/img/optical-system.png" alt="optical system" loading="lazy"></a>

- The system may be written as:

$$\begin{align}
y_{2}&=Ay_{1}+B\theta_{1} \\
\theta_{2} &= Cy_{1} + D\theta_{1}
\end{align}$$

- Which is equal to:

$$\begin{bmatrix}
y_{2} \\ \theta_{2}
\end{bmatrix} = \begin{bmatrix}
A & B \\ C & D
\end{bmatrix} \begin{bmatrix}
y_{1} \\ \theta_{1}
\end{bmatrix}$$

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-callout-metadata="*">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise</span> <span class="theorem-callout-subtitle">(Special Forms of the Ray-Transfer Matrix)</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Special Forms of the Ray-Transfer Matrix</q> <span class="cite-src">[Saleh &amp; Teich, <em>Fundamentals of Photonics</em>, p.&nbsp;207]</span></cite>)
Part 1: $A$ in a focusing system is 0.

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-ray-optics-2026-08-04-02-23-32.svg"><img src="/notes/excalidraw/01-ray-optics-2026-08-04-02-23-32.svg" alt="01 Ray Optics 2026-08-04 02.23.32" loading="lazy"></a></figure>

Part 2: $B$ in an imaging system is 0.

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-ray-optics-2026-08-09-19-50-28.svg"><img src="/notes/excalidraw/01-ray-optics-2026-08-09-19-50-28.svg" alt="01 Ray Optics 2026-08-09 19.50.28" loading="lazy"></a></figure>

Part 3: $C=0$ and $D=0$

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-ray-optics-2026-08-16-06-02-51.svg"><img src="/notes/excalidraw/01-ray-optics-2026-08-16-06-02-51.svg" alt="01 Ray Optics 2026-08-16 06.02.51" loading="lazy"></a></figure>

</div>
</div>

### Matrices of Optical Components {#matrices-of-optical-components}

#### Free-Space Propagation {#free-space-propagation}
- Free space: $\begin{bmatrix}1 & d \\ 0 & 1\end{bmatrix}$
- <a class="internal-link" href="/notes/photonics/snells-law/">Planar Boundary</a>: $\begin{bmatrix}1 & 0 \\ 0 & \frac{n_{1}}{n_{2}} \end{bmatrix}$
- <a class="internal-link" href="/notes/photonics/spherical-lens/">Spherical Lens</a>: $\begin{bmatrix}1 & 0 \\ -\frac{n_{2}-n_{1}}{n_{2}R} & \frac{n_{1}}{n_{2}}\end{bmatrix}$
- <a class="internal-link" href="/notes/photonics/spherical-lens/#thin-lens-assumption">Thin Lens</a>: $\begin{bmatrix}1 & 0 \\ -\frac{1}{f} & 1\end{bmatrix}$
- <a class="internal-link" href="/notes/photonics/planar-mirror/">Planar Mirror</a> Reflection: $\begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix}$
- <a class="internal-link" href="/notes/photonics/spherical-mirror/">Spherical Mirror</a> Reflection (unverified): $\begin{bmatrix}1 & 0 \\ \frac{2}{R} & 1\end{bmatrix}$

#### Cascaded Optical Systems {#cascaded-optical-systems}
- Read the system left to right normally, but write and apply the matrices from right to left

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-callout-metadata="*">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise</span> <span class="theorem-callout-subtitle">(A Set of Parallel Transparent Plates)</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 1.4-2</q> <span class="cite-src">[Saleh &amp; Teich, <em>Fundamentals of Photonics</em>, p.&nbsp;212]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-ray-optics-2026-08-16-06-48-21.svg"><img src="/notes/excalidraw/01-ray-optics-2026-08-16-06-48-21.svg" alt="01 Ray Optics 2026-08-16 06.48.21" loading="lazy"></a></figure>

</div>
</div>
