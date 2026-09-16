---
author: "Anish Goyal"
title: "Quantum Gates"
description: "A gate is mathematically formalized as an operator that turns some ket into another ket"
tags:
  - "notes"
  - "physics"
  - "phys-3571"
date: 2026-01-29T11:23:32
modified: 2026-02-03T11:31:18
readingtime: "3"
course: "PHYS 3571"
course_slug: "phys-3571"
subject: "physics"
kind: "lecture"
ordinal: 3
weight: 30
slug: "quantum-gates"
links: []
sources: []
generated: true
---

## Gate {#gate}
- A gate is mathematically formalized as an operator that turns some ket into another ket
	- Linear mapping that preserves the norm
- Two categories:
	- 1-qubit gates
	- 2-qubit gates
- For quantum computers, the universal gate set is comprised of all the 1-qubit gates and at least one 2-qubit gate

## 1-qubit Gate {#1-qubit-gate}
- Takes an arbitrary point on the Bloch Sphere and moves it to another point
	- This is done via rotation
- Defined by what it does to $\ket{0}$ and $\ket{1}$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.1</span> <span class="theorem-callout-subtitle">(Identity Gate)</span>.</div></div>
<div class="callout-content">

A gate that returns the original wavefunction.
$\hat{I}\ket{0} = \ket{0}$ and $\hat{I}\ket{1} = \ket{1}$

$$\begin{align}
\hat{I}\ket{\psi} &= \hat{I}(\alpha \ket{0} + \beta \ket{1}  ) \\
&= \alpha\hat{I} \ket{0} + \beta \hat{I} \ket{1} \\
&= \alpha \ket{0} + \beta \ket{1}   \\
&= \ket{\psi} 
\end{align}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.2</span> <span class="theorem-callout-subtitle">(Pauli X Gate)</span>.</div></div>
<div class="callout-content">

A gate that rotates 180 degrees about the +x-axis on the Bloch Sphere.
$\hat{X}\ket{0} = \ket{1}$ and $\hat{X} \ket{1} = \ket{0}$

$$\begin{align}
\hat{X} \ket{\psi} &= \hat{X} (\alpha \ket{0} + \beta \ket{1}  ) \\
&= \alpha \ket{1} + \beta \ket{0}  
\end{align}$$

The same effect (switching) occurs in the $i$ basis, since the reflection also affects the $y$-axis.

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.3</span> <span class="theorem-callout-subtitle">(Pauli Y Gate)</span>.</div></div>
<div class="callout-content">

Rotates 180 degrees about the +y-axis.
$\hat{Y}\ket{0} = i\ket{1}$ and $\hat{Y}\ket{1} = -i\ket{0}$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.4</span> <span class="theorem-callout-subtitle">(Pauli Z Gate)</span>.</div></div>
<div class="callout-content">

Rotates 180 degrees about the +z-axis.
$\hat{Z}\ket{0} = \ket{0}$ and $\hat{Z} \ket{1} = -\ket{1}$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.5</span> <span class="theorem-callout-subtitle">(Hadamard Gate)</span>.</div></div>
<div class="callout-content">

180 degree rotation about 45 degrees in the $xz$-plane
$\hat{H}\ket{0} =\frac{\sqrt{ 2 }}{2}(\ket{0} + \ket{1}) = \ket{+}$ and $\hat{H} \ket{1} = \frac{\sqrt{ 2 }}{2}(\ket{0} - \ket{1}) = \ket{-}$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.6</span> <span class="theorem-callout-subtitle">(Phase Gate)</span>.</div></div>
<div class="callout-content">

Rotates 90 degrees about the +z-axis. Square root of the $\hat{Z}$ gate, or the fourth root of the $\hat{I}$ gate.
$\hat{S}\ket{0}=\ket{0}$ and $\hat{S}\ket{1} = i\ket{1}$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.7</span> <span class="theorem-callout-subtitle">($\hat{T}$-Gate $(\frac{\pi}{8} Gate)$)</span>.</div></div>
<div class="callout-content">

Rotates 45 degrees about the +z-axis. Square root of the $\hat{S}$ gate, or the fourth root of the $\hat{Z} gate$
$\hat{T}\ket{0} = \ket{0}$ and $\hat{T}\ket{1} = e^{i \frac{\pi}{4}}\ket{1}$

</div>
</div>

## Generalization of Bloch Sphere Rotation {#generalization-of-bloch-sphere-rotation}
- The rotation of some $\theta$ about a given direction is:

$$\hat{n} = n_{x} \hat{x} + n_{y} \hat{y} + n_{z} \hat{z}$$

where $||\vec{n}||=1$
- Universal rotation operator $\hat{U}$

$$\hat{U} = e^{i \gamma} \left[ \cos \left( \frac{\theta}{2} \right)\hat{I} - i \left( n_{x} \hat{X} + n_{y} \hat{Y} + n_{z} \hat{Z} \right) \sin \left( \frac{\theta}{2} \right)   \right] $$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.8</span> <span class="theorem-callout-subtitle">(Write $\hat{X}$ in the form of $\hat{U}$)</span>.</div></div>
<div class="callout-content">

$$\begin{align}
e^{i \gamma} \left[ \cos \left( \frac{\pi}{2} \right) \hat{I} - i \sin \left( \frac{\pi}{2} \right) \hat{X}  \right]  \\
= -i e^{i \gamma} \hat{X} = \hat{X}
\end{align}$$

</div>
</div>
