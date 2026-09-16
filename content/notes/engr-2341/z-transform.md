---
author: "Anish Goyal"
title: "z-Transform"
description: "Transforms a discrete-time sequence into the z-domain"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-04-17T21:20:14
modified: 2025-04-17T21:21:14
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 21
weight: 210
slug: "z-transform"
links: []
sources:
  - "Z-transform"
  - "Z-transform table (course handout)"
generated: true
---

# $z$-Transform {#z-transform}

## $z$-Transform {#z-transform-1}
- Transforms a discrete-time sequence into the $z$-domain

$$X(z) = \sum_{k=0}^{N} x[k] z^{-k}$$

## Inverse $z$-Transform {#inverse-z-transform}
- Transforms from the $z$-domain to a discrete-time sequence
- Neither inverse nor regular $z$-transforms are practical to evaluate by hand (except with some limited summations), so use a <cite class="cite">Z-transform table (course handout)</cite> instead

$$x[n] = \frac{1}{j 2\pi} \int X(z) z^{n-1} \mathrm{d}z$$

## Partial Fraction Decomposition With MATLAB {#partial-fraction-decomposition-with-matlab}
- When working in the $z$-domain to compute inverse transform, use `residuez` instead of normal `residue` from Laplace Transform
 
<a class="zoom" href="/notes/img/ztransform-pfe-with-matlab.png"><img src="/notes/img/ztransform-pfe-with-matlab.png" alt="ztransform pfe with matlab" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Z-transform (course handout)</span>
