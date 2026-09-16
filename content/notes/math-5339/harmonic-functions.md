---
author: "Anish Goyal"
title: "Harmonic Functions"
description: "Any function whose Laplacian sum to zero"
tags:
  - "notes"
  - "mathematics"
  - "math-5339"
date: 2025-10-20T10:32:01
modified: 2025-10-22T10:38:09
readingtime: "1"
course: "MATH 5339"
course_slug: "math-5339"
subject: "mathematics"
kind: "lecture"
ordinal: 6
weight: 60
slug: "harmonic-functions"
links: []
sources: []
generated: true
---

## Harmonic Functions {#harmonic-functions-1}
- Any function whose Laplacian sum to zero
- For any simple region that is connected, open, and bounded, then you will know the behavior of the function of the inside if you know the behavior along the boundary (Dirichlet problem)
	- Similarly for the derivative of the function along the boundary (Neumann) or the derivative plus the original function along the boundary

## Max/Min Principle {#max-min-principle}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="06.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 06.1</span> <span class="theorem-callout-subtitle">(Max/Min Principle)</span>.</div></div>
<div class="callout-content">

Let $D$ be a connected bounded open set. Let $u$ be a harmonic function. Then, $u$ attains its maximum and minimum values on the boundary of $D$.

</div>
</div>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="06.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 06.2</span> <span class="theorem-callout-subtitle">(Two harmonic functions)</span>.</div></div>
<div class="callout-content">

If $u$ and $v$ solve 

$$\begin{cases}
\delta u = f, &(x, y) \in D \\
u |_{\nabla D} = h
\end{cases}$$

then $u=v$ on $D$

</div>
</div>

## 6.2 Mixed Boundary Conditions {#6-2-mixed-boundary-conditions}

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/06-harmonic-functions-2025-10-22-10-38-21.svg"><img src="/notes/excalidraw/06-harmonic-functions-2025-10-22-10-38-21.svg" alt="06 Harmonic Functions 2025-10-22 10.38.21" loading="lazy"></a></figure>

### Example {#example}

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/06-harmonic-functions-2025-10-22-10-47-11.svg"><img src="/notes/excalidraw/06-harmonic-functions-2025-10-22-10-47-11.svg" alt="06 Harmonic Functions 2025-10-22 10.47.11" loading="lazy"></a></figure>
