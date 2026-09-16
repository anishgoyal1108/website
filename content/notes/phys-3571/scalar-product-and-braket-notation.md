---
author: "Anish Goyal"
title: "Scalar Product and Braket Notation"
description: "Qubit states are \\{{0}, {1}\\}"
tags:
  - "notes"
  - "physics"
  - "phys-3571"
date: 2026-01-22T11:15:56
modified: 2026-02-05T09:55:33
readingtime: "2"
course: "PHYS 3571"
course_slug: "phys-3571"
subject: "physics"
kind: "lecture"
ordinal: 1
weight: 10
slug: "scalar-product-and-braket-notation"
links: []
sources: []
generated: true
---

## Scalar Product {#scalar-product}
- Qubit states are $\{\ket{0}, \ket{1}\}$
	- Each state corresponds to a basis for the $\hat{i}$ and $\hat{j}$ unit vectors
- Scalar product notation: 
	- $\bra{0}\ket{0} = \hat{i} \cdot \hat{i} = 1$
	- $\bra{1}\ket{0}$ = 0
	- $\ket{\psi} = \alpha \ket{0} + \beta \ket{1}$ ($\alpha, \beta$ complex-valued)
- Conjugate property:
	- $\ket{\psi} = \alpha \ket{0} + \beta \ket{1}\implies \bra{\psi} = \alpha^* \bra{0} + \beta^* \bra{1}$
	- $\bra{\psi}\ket{\psi} = \alpha^*\alpha + \beta^* \beta$
- Normalization property:
	- $\bra{\psi}\ket{\psi} = 1$ means $\ket{\psi}$ is normalized
	- $\bra{\psi}\ket{\phi} = 0$ means $\ket{\psi}$ and $\ket{\phi}$ are orthogonal
	- If both properties hold for a set of bases, the set is orthonormal

## Properties of the Scalar Product {#properties-of-the-scalar-product}
1. For any 2 vectors $\ket{\psi}$ and $\ket{\phi}$:

$$\bra{\psi}\ket{\phi} = \bra{\phi}\ket{\psi}^*$$

2. For any vector $\ket{\psi}$:
	- Only 0 iff $\ket{\psi} = \mathbf{0}$ 

$$\bra{\psi}\ket{\psi} \ge 0$$

3. For any two vectors $\ket{\psi}$ and $\ket{\phi}$ (Schwarz/Triangle Inequality):
	- Basically only used to prove the Uncertainty Principle

$$|\bra{\psi}\ket{\phi}|^2 \le \bra{\psi}\ket{\psi} \bra{\phi}\ket{\phi}$$

## BraKet Notation {#braket-notation}
- How to turn $\ket{\psi}$ into $\bra{\psi}$?
	- $\hat{A}, \hat{B}$ are operators
	- $\hat{A} ^{\dagger}$ is the Hermitian conjugate of $\hat{A}$ defined as: $\ket{\phi} = \hat{A} \ket{\psi} \implies \bra{\phi} = \bra{\psi}\hat{A} ^{\dagger}$
		- If $\hat{A} = \hat{A}^{\dagger}$, then $\hat{A}$ is Hermitian

$$\ket{\psi} = \alpha \hat{A} \ket{\phi_{1}} + \beta  \hat{B} \ket{\phi_{2}}$$

$$\bra{\psi} = \alpha^* \bra{\phi} \hat{A}^{\dagger} + \beta^* \bra{\phi_{2}} \hat{B ^{\dagger}}$$

## Bloch Sphere {#bloch-sphere}
- Recall $z = re^{i \theta}$ where $|z| = r$ and $\theta = \tan^{-1}\left( \frac{z_{y}}{z_{x}} \right)$
- Therefore:

$$\begin{align}
\ket{\psi} = \alpha \ket{0} + \beta \ket{1} &= |\alpha| e^{i \theta_{\alpha}} \ket{0} + |\beta| e^{i \theta_{\beta}} \ket{1} \\
&= e^{i \theta_{\alpha}} \left( |\alpha| \ket{0} + |\beta| e^{i (\theta_{\beta} - \theta_{\alpha})} \ket{1}\right)  \\
&= |\alpha| \ket{0} + |\beta| e^{i \phi} \ket{1}   
\end{align}$$

- If we denoted $\theta_\alpha$ as the overall phase, then no prediction of QM depends on the overall phase, since it's a scalar multiple
- If $\ket{\psi}$ is normalized (which it must be to represent a quantum system), then:

$$\bra{\psi} \ket{\psi} = 1 = |\alpha|^2 + |\beta|^2$$

- We can parameterize the previous result with $|\alpha| = \cos \left( \frac{\theta}{2} \right), |\beta| = \sin\left( \frac{\theta}{2} \right)$ such that $\ket{\psi}$ only depends on $\theta, \phi$:
	- $\theta$ is the angle formed from the $z$-axis to the point's displacement vector
	- $\phi$ is the angle formed from the $x$-axis to the projection of the point on the $xy$-plane

$$\ket{\psi} = \cos \left( \frac{\phi}{2} \right) \ket{0} + e^{i \psi} \sin \left( \frac{\theta}{2} \right) \ket{1}; \theta \in [0, \pi], \phi \in [0, 2\pi)$$

- Which point $(\theta, \phi)$ is $\ket{0}$?
	- $(0, \_)$
- Which point is $\ket{1}$?
	- $(\pi, \_)$
- This is why $\{\ket{0}, \ket{1}\}$ are called $z$-basis, since they both intersect the sphere at the $z$-axis
	- $x$-basis is $\{\ket{+}, \ket{-}\} = \left\{ \left( \frac{\pi}{2}, 0 \right), \left( \frac{\pi}{2}, \pi \right) \right\}$
