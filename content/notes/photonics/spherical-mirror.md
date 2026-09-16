---
author: "Anish Goyal"
title: "Spherical Mirror"
description: "Mirror in the shape of a sphere"
tags:
  - "notes"
  - "physics"
  - "photonics"
date: 2026-05-27T21:14:38
modified: 2026-07-28T21:38:28
readingtime: "1"
course: "Fundamentals of Photonics (Saleh & Teich)"
course_slug: "photonics"
subject: "physics"
kind: "concept"
weight: 9014
slug: "spherical-mirror"
links:
  - "/notes/photonics/paraxial-ray/"
sources: []
generated: true
---

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
