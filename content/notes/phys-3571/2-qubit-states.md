---
author: "Anish Goyal"
title: "2-Qubit States"
description: "Subscript tells you which qubit each ket is apart of"
tags:
  - "notes"
  - "physics"
  - "phys-3571"
date: 2026-02-05T11:25:27
modified: 2026-02-10T18:16:25
readingtime: "2"
course: "PHYS 3571"
course_slug: "phys-3571"
subject: "physics"
kind: "lecture"
ordinal: 5
weight: 50
slug: "2-qubit-states"
links: []
sources: []
generated: true
---

## 2-Qubit Basis {#2-qubit-basis}
- Subscript tells you which qubit each ket is apart of
	- Qubit 0: $\left\{ \ket{0}_{0}, \ket{1}_{0} \right\} \to \left\{ \left( \begin{matrix}1 \\ 0\end{matrix} \right)_{0}, \left( \begin{matrix}0 \\ 1\end{matrix} \right)_{0} \right\}$
	- Qubit 1: $\left\{ \ket{0}_{1}, \ket{1}_{1} \right\}\to \left\{ \left( \begin{matrix}1 \\ 0\end{matrix} \right)_{1}, \left( \begin{matrix}0 \\ 1\end{matrix} \right)_{1} \right\}$
- To form the 2-qubit basis, take the tensor product of the single-qubit bases:
- The topmost line of the quantum circuit is the rightmost bit of the bitstring
	- "Little endian" => LSB is the rightmost

$$
\begin{align}
\ket{0}_{1} \otimes \ket{0}_{0} &= \ket{0 \ 0} = \left( \begin{matrix}
1 \\ 0 \\ 0 \\ 0
\end{matrix} \right)  \\
\ket{0}_{1} \otimes \ket{1}_{0} &= \ket{0 \ 1} = \left( \begin{matrix}
0 \\ 1 \\ 0 \\ 0
\end{matrix} \right) \\
\ket{1}_{1} \otimes \ket{0}_{0} &= \ket{1 \ 0} = \left( \begin{matrix}
0 \\ 0 \\ 1 \\ 0
\end{matrix} \right)  \\
\ket{1}_{1} \otimes \ket{1}_{0} &= \ket{1 \ 1} =  \left( \begin{matrix}
0 \\ 0 \\ 0 \\ 1
\end{matrix} \right) 
\end{align}
$$

- Constructing the matrices for tensor product basis:

$$\ket{0}_{1} \otimes \ket{0}_{0} = \left( \begin{matrix}
1 \\ 0
\end{matrix} \right) \otimes \left( \begin{matrix}
0 \\ 1
\end{matrix} \right) = \left( \begin{matrix}
1 \left( \begin{matrix}
1 \\ 0
\end{matrix} \right)_{0} \\ 0 \left( \begin{matrix} 1 \\ 0
\end{matrix} \right)_{0}  
\end{matrix} \right) = \left( \begin{matrix}
1 \\ 0 \\ 0 \\ 0
\end{matrix} \right) = \ket{0 \ 0}$$

## Inner Product {#inner-product}
- Take the single-qubit inner product, grouping by the qubit index

$$\braket{ 0 \ 0 | 0 \ 0 } = (\bra{0}_{1} \otimes \bra{0}_{0})(\ket{0}_{1} \otimes \ket{0}_{0}) = \braket{ 0 | 0 }_{1} \braket{ 0 | 0 }_{0} = 1    $$

### CNOT Example {#cnot-example}

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-2-qubit-states-2026-02-05-11-51-07.svg"><img src="/notes/excalidraw/05-2-qubit-states-2026-02-05-11-51-07.svg" alt="05 2-Qubit States 2026-02-05 11.51.07" loading="lazy"></a></figure>

### CNOT With Haddamard Example {#cnot-with-haddamard-example}

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/05-2-qubit-states-2026-02-05-12-10-24.svg"><img src="/notes/excalidraw/05-2-qubit-states-2026-02-05-12-10-24.svg" alt="05 2-Qubit States 2026-02-05 12.10.24" loading="lazy"></a></figure>

## Measuring Individual Qubits from 2-Qubit State {#measuring-individual-qubits-from-2-qubit-state}
- Projection operator onto state $\ket{0}_{1}$:

$$\hat{\mathbb{P}}(\ket{0}_{1} ) = (\ket{0}_{1}\bra{0}_{1}  ) \otimes \hat{I}_{0}$$

- The probability is:

$$P(\ket{0}_{1} ) = \braket{ \psi | \hat{\mathbb{P}}(\ket{0}_{1} ) | \psi  }$$ 

- Shortcut: it's the sum of the squares of the coefficients for any 2-qubit whose first is 0/1
- Q: If we measured $q_1$ and got $\ket{0}_{1}$, what is the new wave function?
- A:

$$\ket{\psi_{\text{new}}} = \frac{\ket{\hat{\mathbb{P}}}}{\sqrt{ \braket{ \psi | \hat{\mathbb{P}}(\ket{0}_{1} ) | \psi  }  }}$$

## Entangled States {#entangled-states}
- A 2-qubit state is entangled if it can't be written as the product of 2 single-qubit states
- General unentangled state:

$$\begin{align}
\ket{\psi} &= (\alpha_{1}\ket{0}_{1} + \beta_{1} \ket{1}_{1}  ) \otimes (\alpha_{0}\ket{0}_{0} + \beta_{0 \ket{1}_{0} } ) \\
&= \alpha_{1} \alpha_{0} \ket{0 \ 0} + \alpha_{1} \beta_{0}\ket{0 \ 1} + \beta_{1} \alpha_{0} \ket{1 \ 0} + \beta_{1} \beta_{0} \ket{1 \ 1}    
\end{align}$$

- Entangled state
	- Entangled because there's no solution to get it into the unentangled state

$$\ket{\psi_{+}} =  \frac{1}{\sqrt{ 2 }} \ket{0 \ 0} + \frac{1}{\sqrt{ 2 }} \ket{1 \ 1}   $$
