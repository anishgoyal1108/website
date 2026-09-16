---
author: "Anish Goyal"
title: "Measurement of a Qubit"
description: "Computational basis"
tags:
  - "notes"
  - "physics"
  - "phys-3571"
date: 2026-01-27T11:40:06
modified: 2026-01-29T11:42:23
readingtime: "4"
course: "PHYS 3571"
course_slug: "phys-3571"
subject: "physics"
kind: "lecture"
ordinal: 2
weight: 20
slug: "measurement-of-a-qubit"
links: []
sources: []
generated: true
---

## Measurement and Basis {#measurement-and-basis}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.1</span> <span class="theorem-callout-subtitle">(Measurement)</span>.</div></div>
<div class="callout-content">

A measurement is defined relative to a chosen orthonormal basis of the qubit Hilbert space.

</div>
</div>

- Computational basis
	- Z basis $\{\ket{0}, \ket{1}\}$

## State Representation {#state-representation}
- General pure qubit state

$$
\ket{\psi} = \alpha \ket{0} + \beta \ket{1}\ \ \ \alpha, \beta \in \mathbb{C}
$$

- Normalization (always check this first!)

$$
|\alpha|^2 + |\beta|^2 = 1
$$

## Z Basis Measurement {#z-basis-measurement}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.2</span> <span class="theorem-callout-subtitle">(Projection Operators)</span>.</div></div>
<div class="callout-content">

$$
\hat{P}(0) = \ket{0}\bra{0}
$$

$$
\hat{P}(1) = \ket{1}\bra{1}
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="02.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 02.3</span> <span class="theorem-callout-subtitle">(Measurement Probabilities)</span>.</div></div>
<div class="callout-content">

$$
P(0) = \bra{\psi}\hat{P}(0)\ket{\psi} = |\bra{0}\ket{\psi}|^2
$$

$$
P(1) = \bra{\psi}\hat{P}(1)\ket{\psi} = |\bra{1}\ket{\psi}|^2
$$

Explicitly:

$$
P(0) = |\alpha|^2
$$

$$
P(1) = |\beta|^2
$$

</div>
</div>

## Bloch Sphere Parameterization {#bloch-sphere-parameterization}
Any pure qubit state may be written as

$$
\ket{\psi} = \cos\left(\frac{\theta}{2}\right)\ket{0} + e^{i\phi}\sin\left(\frac{\theta}{2}\right)\ket{1}
$$

with the corresponding measurement probabilities:

$$
P(\ket{0}) = \cos^2\left(\frac{\theta}{2}\right)
$$

$$
P(\ket{1}) = \sin^2\left(\frac{\theta}{2}\right)
$$

## Repeated Measurements {#repeated-measurements}

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="02.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 02.4</span> <span class="theorem-callout-subtitle">(Repeatability)</span>.</div></div>
<div class="callout-content">

If a qubit is measured in a basis and immediately remeasured in the same basis, the outcome is identical with probability 1.

</div>
</div>

### Post-Measurement (State Collapse) {#post-measurement-state-collapse}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="02.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 02.5</span> <span class="theorem-callout-subtitle">(State Collapse)</span>.</div></div>
<div class="callout-content">

If outcome $i$ is observed, the post measurement state is

$$
\ket{\psi_{\text{new}}}
=
\frac{\hat{P}(i)\ket{\psi_{\text{old}}}}
{\|\hat{P}(i)\ket{\psi_{\text{old}}}\|}
$$

In other words, the new wavefunction is the projection of the observed outcome onto the old wavefunction.

</div>
</div>

- For the Z basis:

$$
\ket{\psi_{\text{new}}} = \ket{i}
$$

- The projection formula for state collapse would really only be useful if you were applying a change-of-basis for subsequent measurements, since if you already observed the outcome in a particular basis, the outcome is never going to change if you observe it again

## Measurement in Other Bases {#measurement-in-other-bases}

### X Basis {#x-basis}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.6</span> <span class="theorem-callout-subtitle">(X Basis States)</span>.</div></div>
<div class="callout-content">

$$
\ket{+} = \frac{1}{\sqrt{2}}(\ket{0} + \ket{1})
$$

$$
\ket{-} = \frac{1}{\sqrt{2}}(\ket{0} - \ket{1})
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.7</span> <span class="theorem-callout-subtitle">(X Basis Projectors)</span>.</div></div>
<div class="callout-content">

$$
\hat{P}(+) = \ket{+}\bra{+}
$$

$$
\hat{P}(-) = \ket{-}\bra{-}
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="02.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 02.8</span> <span class="theorem-callout-subtitle">(X Basis Measurement)</span>.</div></div>
<div class="callout-content">

$$
P(\pm) = |\bra{\pm}\ket{\psi}|^2
$$

</div>
</div>

- Inner product

$$\bra{+}\ket{\psi} = \frac{1}{\sqrt{2}} \left(\cos\left(\frac{\theta}{2}\right) + e^{i\phi}\sin\left(\frac{\theta}{2}\right)\right)
$$

- Probability

$$
P(+)
=
\frac{1}{2}
\left|
\cos\left(\frac{\theta}{2}\right)
e^{i\phi}\sin\left(\frac{\theta}{2}\right)
\right|^2
$$

### Y Basis {#y-basis}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.9</span> <span class="theorem-callout-subtitle">(Y Basis States)</span>.</div></div>
<div class="callout-content">

$$
\ket{+i} = \frac{1}{\sqrt{2}}(\ket{0} + i\ket{1})
$$

$$
\ket{-i} = \frac{1}{\sqrt{2}}(\ket{0} - i\ket{1})
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.10</span> <span class="theorem-callout-subtitle">(Y Basis Projectors)</span>.</div></div>
<div class="callout-content">

$$
\hat{P}(+i) = \ket{+i}\bra{+i}
$$

$$
\hat{P}(-i) = \ket{-i}\bra{-i}
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="02.11">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 02.11</span> <span class="theorem-callout-subtitle">(Y Basis Measurement)</span>.</div></div>
<div class="callout-content">

$$
P(\pm i) = |\bra{\pm i}\ket{\psi}|^2
$$

</div>
</div>

## General Projective Measurement {#general-projective-measurement}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="02.12">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 02.12</span> <span class="theorem-callout-subtitle">(Projective Measurement Rule)</span>.</div></div>
<div class="callout-content">

Let $\{\ket{\phi_k}\}$ be an orthonormal basis
- Projection operators

$$
\hat{P}_k = \ket{\phi_k}\bra{\phi_k}
$$

- Probability of outcome $k$

$$
P(k) = |\bra{\phi_k}\ket{\psi}|^2
$$

- Post measurement state

$$
\ket{\psi_{\text{new}}}
=
\frac{\hat{P}_k\ket{\psi}}
{\sqrt{P(k)}}
$$

</div>
</div>

## Completeness of Basis Sets {#completeness-of-basis-sets}
- If you let $\ket{0}\bra{0} + \ket{1}\bra{1} = \hat{I}$, then $\hat{I}\ket{0} = \ket{0}$ and $\hat{I}\ket{1} = \ket{1}$
- For any arbitrary point on the Bloch Sphere:

$$
\begin{align}
\ket{\psi} &= \cos \left( \frac{\theta}{2} \right) \ket{0} + e^{i \psi} \sin \left( \frac{\theta}{2} \right) \ket{1} \\
\ket{\psi'} &= \cos \left( \frac{\pi - \theta}{2} \right) \ket{0}  + e^{i(\pi+\phi)}\sin \left( \frac{\pi-\theta}{2} \right) \ket{1} \\
&=\sin\left( \frac{\theta}{2} \right) \ket{0} - e^{i \psi} \sin \left( \frac{\theta}{2} \right) \ket{1}   
\end{align}
$$

Letting $\hat{u} = \ket{\psi}\bra{\psi} + \ket{\psi'}\bra{\psi'}$ and letting $\cos{\left( \frac{\theta}{2} \right), \sin{\left( \frac{\theta}{2} \right)} = c, s}$, we have:

$$
\begin{align}
\hat{u} &= (c\ket{0} + e^{i\psi} s\ket{1}  )(c \bra{0}  + e^{-i \psi} s \bra{1}   ) + (s\ket{0}-e^{i \psi} c\ket{1})(s \bra{0} - e^{-i \psi} c \ket{1}) \\
&= (s^2 + c^2)\ket{0}\bra{0} + (s^2 + c^2)\ket{1}\bra{1} \\
&= \ket{0}\bra{0} + \ket{1}\bra{1} \\
&= \hat{I}         
\end{align}
$$

- You can use this property to perform a change-of-basis, since $\ket{\psi} = \hat{I}\ket{\psi}$, and plug in the values from the other basis
