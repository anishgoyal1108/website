---
author: "Anish Goyal"
title: "Quantum Circuits"
description: "Represented by a line with a starting state and the gates as operators on the state"
tags:
  - "notes"
  - "physics"
  - "phys-3571"
date: 2026-02-03T11:13:08
modified: 2026-02-05T11:23:02
readingtime: "2"
course: "PHYS 3571"
course_slug: "phys-3571"
subject: "physics"
kind: "lecture"
ordinal: 4
weight: 40
slug: "quantum-circuits"
links: []
sources: []
generated: true
---

## Quantum Circuits {#quantum-circuits-1}
- Represented by a line with a starting state and the gates as operators on the state
- CNOT gate is a 2-qubit gate with one qubit acting as a control to see if the other qubit state is NOTed
- The gates are applied from left to right, but the operators are written in right to left order

## Matrix Representation {#matrix-representation}
- Goal: represent states with column matrices

### Ket {#ket}

$$\ket{0} \doteq \left( \begin{matrix}
1 \\ 0
\end{matrix} \right), \ \ \ \ \ \ket{1} \doteq \left( \begin{matrix}
0 \\ 1
\end{matrix} \right)$$

- For any state $\ket{\psi} = \alpha \ket{0} + \beta \ket{1}$:

$$\ket{\psi} = \alpha \left( \begin{matrix}
1 \\ 0
\end{matrix} \right) + \beta \left( \begin{matrix}
0 \\ 1
\end{matrix} \right) = \left( \begin{matrix}
\alpha \\ 0
\end{matrix} \right)  + \left( \begin{matrix}
0 \\ \beta
\end{matrix} \right) = \left( \begin{matrix}
\alpha \\ \beta
\end{matrix} \right) $$

### Bra {#bra}
- What is $\bra{0}$?

$$\bra{0} = (\ket{0}^T)^{*} = (1 \ 0)$$

- What about $\bra{1}$?

$$\bra{1} = (\ket{1}^T)^{*} = (0 \ 1)$$

- What about $\bra{\psi}$?
	- Interchange the rows and columns

$$\bra{\psi} = (\alpha^* \ \beta^*)$$ 

### Inner Product {#inner-product}
- What is the inner product of $\psi$ onto itself?

$$\braket{ \psi | \psi }= (\alpha^* \ \beta^*)\left( \begin{matrix}
\alpha \\ \beta
\end{matrix} \right) = \alpha^*\alpha + \beta^* \beta = |\alpha|^2 + |\beta|^2$$

#### Inner Product Example {#inner-product-example}

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-quantum-circuits-2026-02-03-12-01-36.svg"><img src="/notes/excalidraw/04-quantum-circuits-2026-02-03-12-01-36.svg" alt="04 Quantum Circuits 2026-02-03 12.01.36" loading="lazy"></a></figure>

### Operators {#operators}
- Represented by $2 \times 2$ matrices

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="04.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 04.1</span> <span class="theorem-callout-subtitle">(Hermitian)</span>.</div></div>
<div class="callout-content">

The transpose of the conjugate matrix, denoted $M^{^{\dagger}}$. Has the following property:

$$\hat{U}^{\dagger} \hat{U} = \hat{U} \hat{U}^{\dagger} = \hat{I}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="04.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 04.2</span> <span class="theorem-callout-subtitle">(Unitary Operators)</span>.</div></div>
<div class="callout-content">

Any operator with the property $\hat{U}^{-1}=\hat{U}^{\dagger}$.

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="04.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 04.3</span> <span class="theorem-callout-subtitle">(Reversible Operators)</span>.</div></div>
<div class="callout-content">

Given any operator $\hat{M}$, we say $\hat{M}$ is invertible (reversible) if $\exists \hat{M}^{-1}$ st:

$$\hat{M} \hat{M}^{-1} = I = \hat{M}^{-1}\hat{M}$$

</div>
</div>

## References {#references}
- [quirk quantum simulator](https://algassert.com/quirk)
