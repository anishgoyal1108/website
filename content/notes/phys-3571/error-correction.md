---
author: "Anish Goyal"
title: "Error Correction"
description: "Kinds of errors"
tags:
  - "notes"
  - "physics"
  - "phys-3571"
date: 2026-02-19T09:47:17
modified: 2026-09-04T13:25:20
readingtime: "6"
course: "PHYS 3571"
course_slug: "phys-3571"
subject: "physics"
kind: "lecture"
ordinal: 8
weight: 80
slug: "error-correction"
links: []
sources:
  - "Wong, Introduction to Classical and Quantum Computing"
generated: true
---

## Errors {#errors}
- Kinds of errors
	- Bit flip
	- Phase flip
	- Both error
		- Need to use Shor's Error-correcting code

### Bit Flip {#bit-flip}
- Partial bit flip 
	- Occurs when one of the points on the Bloch sphere moves towards the other point instead of completely swapping states
	- Assuming $\psi$ was unchanged and $\theta$ small:

$$\ket{\psi} \approx\frac{\ket{0} + \frac{\theta}{2} \ket{1} }{\sqrt{ 1 + \left( \frac{\theta}{2} \right)^2 } }$$

- To get an exact mapping of how the partial bit flip affects $\ket{\psi}$, we can parameterize the universal gate operator
	- Partial bit flip = rotation about the $x$-axis by angle $\theta$, so $\hat{n} = (1, 0, 0)$
	- Choose global phase $\alpha = \pi/2$, so the general rotation operator reduces to:

$$\hat{U}_{\text{partial flip}} = i\cos\left(\frac{\theta}{2}\right)\hat{I} + \sin\left(\frac{\theta}{2}\right)\hat{X}$$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="08.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 08.1</span> <span class="theorem-callout-subtitle">(Partial Bit Flip Operator)</span>.</div></div>
<div class="callout-content">

Let $\varepsilon = \sin(\theta/2)$, so $\cos(\theta/2) = \sqrt{1 - \varepsilon^2}$. The partial bit flip operator is:

$$i\sqrt{1-\varepsilon^2}\,\hat{I} + \varepsilon\hat{X} = \begin{pmatrix} i\sqrt{1-\varepsilon^2} & \varepsilon \\ \varepsilon & i\sqrt{1-\varepsilon^2} \end{pmatrix}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="08.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 08.2</span> <span class="theorem-callout-subtitle">(Action of Partial Bit Flip on Basis States)</span>.</div></div>
<div class="callout-content">

$$\ket{0} \to i\sqrt{1-\varepsilon^2}\,\ket{0} + \varepsilon\ket{1}$$

$$\ket{1} \to \varepsilon\ket{0} + i\sqrt{1-\varepsilon^2}\,\ket{1}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="08.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 08.3</span> <span class="theorem-callout-subtitle">(Error Parameter $\varepsilon$)</span>.</div></div>
<div class="callout-content">

$$\varepsilon = \sin\left(\frac{\theta}{2}\right)$$

where $\theta$ is the Bloch sphere rotation angle of the partial flip.
- Small physical disturbance $\implies$ small $\theta$ $\implies$ $\varepsilon \ll 1$
- $\varepsilon^2$: probability ancilla measurement collapses into error branch
- $1 - \varepsilon^2$: probability ancilla measurement collapses into no-error branch

</div>
</div>

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="08.4" id="blk-44dfe0">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 08.4</span> <span class="theorem-callout-subtitle">(Action on General State)</span>.</div></div>
<div class="callout-content">

For $\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$ with $\alpha, \beta \in \mathbb{C}$:

$$\ket{\psi} \to \left(i\sqrt{1-\varepsilon^2}\,\alpha + \varepsilon\beta\right)\ket{0} + \left(\varepsilon\alpha + i\sqrt{1-\varepsilon^2}\,\beta\right)\ket{1}$$

When $\theta = \pi$, $\varepsilon = 1$, recovering the full $\hat{X}$ gate: $\alpha\ket{0}+\beta\ket{1} \to \beta\ket{0}+\alpha\ket{1}$

</div>
</div>

### Phase Flip {#phase-flip}
- A rotation through angle $\theta$ around the $z$-axis

## Solutions {#solutions}

### Problems with Naive Approaches {#problems-with-naive-approaches}
- Can't use a parity bit because that would require that you measure the physical state of the qubit which would collapse its wave function
- You also can't *copy* the state from one qubit to the other because of the <cite class="cite cite-quote"><q>4.4.4 No-Cloning Theorem</q> <span class="cite-src">[Wong, <em>Introduction to Classical and Quantum Computing</em>, p.&nbsp;177]</span></cite>

### Error-Correcting Codes {#error-correcting-codes}
- Assign 3 *logical* qubits that we use to encode a *real* qubit

$$\begin{align}
\ket{0_{L}} &= \ket{0 \ 0 \ 0}   \\
\ket{1_{L}} &= \ket{1 \ 1 \ 1} \\
\ket{\psi_{L}} &=\alpha \ket{0_{L}} + \beta \ket{1_{L}}     
\end{align}$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.5</span> <span class="theorem-callout-subtitle">(Left bit-flip)</span>.</div></div>
<div class="callout-content">

Consider a left-qubit bit-flip:

$$\ket{\psi} = \alpha \ket{1 \ 0 \ 0} + \beta \ket{0 \ 1 \ 1}$$

How can we encode the given state?

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-error-correction-2026-02-19-11-36-08.svg"><img src="/notes/excalidraw/08-error-correction-2026-02-19-11-36-08.svg" alt="08 Error Correction 2026-02-19 11.36.08" loading="lazy"></a></figure>

We know there's an error if the parity between consecutive qubits differs! This is done by chaining the line with $\ket{\psi}$ to all the other qubits with a CNOT gate (which is like XOR in classical computing).

$$\text{CNOT}(\ket{a}\ket{b}) = \ket{a}\ket{a \oplus b}    $$

</div>
</div>

### Ancilla Qubits {#ancilla-qubits}
- To carry out error detection in general, we need ancilla qubits
	- If both qubits flipped, then the error correction scheme 
- Based on the results of the measurement, you apply the rotation (depending on which qubit flipped), then apply a 180 degree rotation to $\theta$, and flip it

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/08-error-correction-2026-02-19-12-04-33.svg"><img src="/notes/excalidraw/08-error-correction-2026-02-19-12-04-33.svg" alt="08 Error Correction 2026-02-19 12.04.33" loading="lazy"></a></figure>

#### Detecting Partial Bit Flip Errors With Ancilla Qubits {#detecting-partial-bit-flip-errors-with-ancilla-qubits}
- Ancilla qubits initialized to $\ket{00}$, so the full initial state is:

$$\ket{00} \otimes \ket{\psi_L} = \ket{00}\left(\alpha\ket{000} + \beta\ket{111}\right)$$

- Apply a partial bit flip to the first (leftmost) logical qubit using <a class="internal-link ref-theorem" href="/notes/phys-3571/error-correction/#blk-44dfe0">Action on General State</a>:

$$\ket{000} = \ket{0}_{\text{flip}}\ket{00} \to \left(i\sqrt{1-\varepsilon^2}\ket{0} + \varepsilon\ket{1}\right)\ket{00} = i\sqrt{1-\varepsilon^2}\ket{000} + \varepsilon\ket{100}$$

$$\ket{111} = \ket{1}_{\text{flip}}\ket{11} \to \left(\varepsilon\ket{0} + i\sqrt{1-\varepsilon^2}\ket{1}\right)\ket{11} = \varepsilon\ket{011} + i\sqrt{1-\varepsilon^2}\ket{111}$$

- Applying linearity to the full logical state and tensoring in the ancilla:

$$\boxed{\ket{\Psi} = i\alpha\sqrt{1-\varepsilon^2}\ket{00}\ket{000} + \alpha\varepsilon\ket{00}\ket{100} + \beta\varepsilon\ket{00}\ket{011} + i\beta\sqrt{1-\varepsilon^2}\ket{00}\ket{111}}$$

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="08.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 08.6</span> <span class="theorem-callout-subtitle">(Interpretation of Outcomes)</span>.</div></div>
<div class="callout-content">

- $i\alpha\sqrt{1-\varepsilon^2}\ket{00}\ket{000}$: no error on $\alpha$ branch
- $\alpha\varepsilon\ket{00}\ket{100}$: first qubit flipped on $\alpha$ branch
- $\beta\varepsilon\ket{00}\ket{011}$: first qubit flipped on $\beta$ branch
- $i\beta\sqrt{1-\varepsilon^2}\ket{00}\ket{111}$: no error on $\beta$ branch
- When $\varepsilon = 1$ (full $\hat{X}$), the no-error terms vanish and full flip is recovered

</div>
</div>

- We can entangle each ancilla qubit with each consecutive pair in the logical qubit to get the following readings
	- Ancilla reads $\ket{0 \ 0}$: no error; state collapses to $\alpha \ket{0 \ 0 \ 0} + \beta \ket{1 \ 1 \ 1}$
	- Ancilla reads $\ket{1 \ 0}$: first qubit flipped
	- Ancilla reads $\ket{1 \ 1}$: second qubit flipped
	- Ancilla reads $\ket{0 \ 1}$: third qubit flipped

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="08.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 08.7</span> <span class="theorem-callout-subtitle">(Ancilla Measurement Outcomes (First Qubit Partial Flip))</span>.</div></div>
<div class="callout-content">

| $a_{01}$ | $a_{12}$ | Probability | Post-measurement $\ket{\psi}$ |
|---|---|---|---|
| 0 | 0 | $1-\varepsilon^2$ | $\alpha\ket{000} + \beta\ket{111}$ |
| 0 | 1 | $0$ | — |
| 1 | 0 | $\varepsilon^2$ | $\alpha\ket{100} + \beta\ket{011}$ |
| 1 | 1 | $0$ | — |
Apply $\hat{X}$ to the first qubit if ancilla reads $\ket{10}$ to recover $\alpha\ket{000}+\beta\ket{111}$.

</div>
</div>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="08.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 08.8</span> <span class="theorem-callout-subtitle">(Role of Measurement in Error Correction)</span>.</div></div>
<div class="callout-content">

The ancilla measurement forces the partial rotation to commit to one of two outcomes:
- **No-error branch** ($\ket{00}$): state collapses to $\alpha\ket{000}+\beta\ket{111}$, up to global phase $i\sqrt{1-\varepsilon^2}$, which has no physical consequence
- **Error branch** ($\ket{10}$): state collapses to $\alpha\ket{100}+\beta\ket{011}$, corrected by applying $\hat{X}$ to the first qubit

This is why error correction works: measuring the ancilla collapses the superposition into a definite, correctable form without ever revealing $\alpha$ or $\beta$.

</div>
</div>
