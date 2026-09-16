---
author: "Anish Goyal"
title: "More on Error (Phase) Correction"
description: "Logical qubits: {0{L}} {+ \\ + \\ +} and {1L} {- \\ - \\ -}"
tags:
  - "notes"
  - "physics"
  - "phys-3571"
date: 2026-03-03T11:29:20
modified: 2026-03-03T12:10:07
readingtime: "1"
course: "PHYS 3571"
course_slug: "phys-3571"
subject: "physics"
kind: "lecture"
ordinal: 9
weight: 90
slug: "more-on-error-phase-correction"
links: []
sources: []
generated: true
---

## Detecting Partial Phase Flip Errors With Ancilla Qubits {#detecting-partial-phase-flip-errors-with-ancilla-qubits}
- Logical qubits: $\ket{0_{L}} = \ket{+ \ + \ +}$ and $\ket{1_L} = \ket{- \ - \ -}$
- Encode: $\ket{\psi} = \alpha \ket{+ \ + \ +} + \beta{- \ - \ -}$
	- We use this encoding because a *complete* phase flip would switch $\ket{+}$ to $\ket{-}$

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-error-correction-2026-03-03-11-23-05.svg"><img src="/notes/excalidraw/08-error-correction-2026-03-03-11-23-05.svg" alt="08 Error Correction 2026-03-03 11.23.05" loading="lazy"></a></figure>

## Detection of Complete Phase Flip {#detection-of-complete-phase-flip}
- Measure parity of consecutive qubits *in the $X$-basis*

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="09.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 09.1</span> <span class="theorem-callout-subtitle">(Left-qubit flipped)</span>.</div></div>
<div class="callout-content">

Consider the following phase flip:

$$\ket{\psi} = \alpha \ket{- \ + \ +} + \beta \ket{+ \ - \ -}  $$

How can we encode the given state?

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/09-more-on-error-phase-correction-2026-03-03-11-42-50.svg"><img src="/notes/excalidraw/09-more-on-error-phase-correction-2026-03-03-11-42-50.svg" alt="09 More on Error (Phase) Correction 2026-03-03 11.42.50" loading="lazy"></a></figure>

</div>
</div>

## Partial Phase Flip {#partial-phase-flip}
- We want to obtain an exact mapping on how partial phase flips change $\ket{\psi}$
- Universal gate operator about $z$-axis with $\vec{n} = \left< 0, 0, 1 \right>$ and $\alpha = \frac{\pi}{2}$

$$\begin{align*}
\hat{U}(\theta) &= e^{i \pi/2}\left[ \cos \left( \frac{\theta}{2} \right) \hat{I} - i \sin \left( \frac{\theta}{2} \right) \hat{Z}  \right] \\
&= i\left[ \sqrt{ 1-\epsilon^2} \left( \begin{matrix}
1 & 0 \\0 & 1
\end{matrix} \right) - i \epsilon \left( \begin{matrix}
1 & 0 \\ 0 & -1
\end{matrix} \right) \right] \\
&= \left( \begin{matrix}
i \sqrt{ 1- \epsilon^2 } + \epsilon & 0 \\ \\
0  & i \sqrt{ 1 - \epsilon^2 } - \epsilon
\end{matrix} \right) 
\end{align*}$$
