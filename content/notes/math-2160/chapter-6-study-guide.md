---
author: "Anish Goyal"
title: "Chapter 6 Study Guide"
description: "Covers §6.1–6.3. Full problems and recorded answers in 2160 Compendium."
tags:
  - "notes"
  - "mathematics"
  - "math-2160"
date: 2026-08-09T10:50:49
modified: 2026-08-09T10:50:49
readingtime: "5"
course: "MATH 2160"
course_slug: "math-2160"
subject: "mathematics"
kind: "guide"
ordinal: 6
weight: 5060
slug: "chapter-6-study-guide"
links:
  - "/notes/math-2160/2160-compendium/"
  - "/notes/math-2160/chapter-5-study-guide/"
sources: []
generated: true
---

# Chapter 6 — Orthogonality and Least Squares {#chapter-6-orthogonality-and-least-squares}

Covers **§6.1–6.3**. Full problems and recorded answers in <a class="internal-link" href="/notes/math-2160/2160-compendium/">2160 Compendium</a>.

<div class="callout" data-callout="abstract">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-clipboard-list" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-clipboard-list"/></svg></div><div class="callout-title-inner">Weighting</div></div>
<div class="callout-content">

**33 questions**, **6 true/false (18%)** — the smallest chapter, and the last material before the final. It was also the most recently studied (all three sections worked on 07/13), so it is the freshest but least reviewed.

</div>
</div>

---

## §6.1 Inner Product, Length, and Orthogonality {#6-1-inner-product-length-and-orthogonality}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 1</span> <span class="theorem-callout-subtitle">(Inner product, norm, distance)</span>.</div></div>
<div class="callout-content">

$$\mathbf{u}\cdot\mathbf{v}=\mathbf{u}^{T}\mathbf{v}=u_1v_1+u_2v_2+\cdots+u_nv_n$$

$$\|\mathbf{v}\|=\sqrt{\mathbf{v}\cdot\mathbf{v}}=\sqrt{v_1^{2}+\cdots+v_n^{2}}, \qquad \|\mathbf{v}\|^{2}=\mathbf{v}\cdot\mathbf{v}$$

$$\operatorname{dist}(\mathbf{u},\mathbf{v})=\|\mathbf{u}-\mathbf{v}\|$$

The dot product returns a **scalar**. It is commutative and distributive, and $(c\mathbf{u})\cdot\mathbf{v}=c(\mathbf{u}\cdot\mathbf{v})$.

</div>
</div>

<div class="callout" data-callout="important">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-flame"/></svg></div><div class="callout-title-inner">Orthogonality</div></div>
<div class="callout-content">

$$\mathbf{u}\perp\mathbf{v} \iff \mathbf{u}\cdot\mathbf{v}=0$$

That is the entire test — compute the dot product and compare to zero. The zero vector is orthogonal to **everything**.

**Pythagorean Theorem:** $\|\mathbf{u}+\mathbf{v}\|^{2}=\|\mathbf{u}\|^{2}+\|\mathbf{v}\|^{2}$ holds **exactly when** $\mathbf{u}\perp\mathbf{v}$.

</div>
</div>

<div class="callout" data-callout="note">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner">Unit vectors — normalizing</div></div>
<div class="callout-content">

$$\mathbf{u}=\frac{\mathbf{v}}{\|\mathbf{v}\|}$$

Divide by the length; the result has norm 1 and points the same direction. Expect an irrational $\|\mathbf{v}\|$ — leave the radical in place rather than decimalizing.

</div>
</div>

**Tested as** — dot products and the ratio $\frac{\mathbf{u}\cdot\mathbf{v}}{\mathbf{v}\cdot\mathbf{v}}$ <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-1-1">6.1.1</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-1-2">6.1.2</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-1-5">6.1.5</a> · norm <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-1-7">6.1.7</a> · unit vector <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-1-9">6.1.9</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-1-10">6.1.10</a> · distance <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-1-14">6.1.14</a> · orthogonality check <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-1-15">6.1.15</a>–<a class="internal-link" href="/notes/math-2160/2160-compendium/#6-1-18">6.1.18</a>

<div class="callout" data-callout="tip">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-lightbulb" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-lightbulb"/></svg></div><div class="callout-title-inner">Watch for $\frac{\mathbf{u}\cdot\mathbf{v}}{\mathbf{v}\cdot\mathbf{v}}$</div></div>
<div class="callout-content">

Three §6.1 problems ask for this quotient specifically. It is not idle arithmetic — it is exactly the coefficient in the orthogonal projection formula of §6.2. Recognizing it early makes the next section trivial.

</div>
</div>

---

## §6.2 Orthogonal Sets {#6-2-orthogonal-sets}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 2</span> <span class="theorem-callout-subtitle">(Orthogonal and orthonormal sets)</span>.</div></div>
<div class="callout-content">

A set is **orthogonal** if every *distinct* pair is orthogonal: $\mathbf{u}_i\cdot\mathbf{u}_j=0$ for $i\neq j$.
It is **orthonormal** if additionally every vector is a **unit** vector.

For three vectors that means checking **three** pairs — $(1,2)$, $(1,3)$, $(2,3)$. Missing one is the standard error.

</div>
</div>

<div class="callout" data-callout="important">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-flame"/></svg></div><div class="callout-title-inner">Why orthogonal bases are worth having</div></div>
<div class="callout-content">

If $\{\mathbf{u}_1,\dots,\mathbf{u}_p\}$ is an orthogonal basis for $W$, then any $\mathbf{y}\in W$ expands as

$$\mathbf{y}=c_1\mathbf{u}_1+\cdots+c_p\mathbf{u}_p, \qquad c_j=\frac{\mathbf{y}\cdot\mathbf{u}_j}{\mathbf{u}_j\cdot\mathbf{u}_j}$$

**No system to solve** — each coefficient is an independent quotient. Compare §1.3, where finding coefficients meant row reducing an augmented matrix. This is the payoff of orthogonality.

</div>
</div>

<div class="callout" data-callout="note">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner">Orthogonal projection onto a line</div></div>
<div class="callout-content">

The projection of $\mathbf{y}$ onto the line through $\mathbf{u}$ and the origin:

$$\hat{\mathbf{y}}=\operatorname{proj}_{\mathbf{u}}\mathbf{y}=\frac{\mathbf{y}\cdot\mathbf{u}}{\mathbf{u}\cdot\mathbf{u}}\,\mathbf{u}$$

The **orthogonal decomposition** is then

$$\mathbf{y}=\hat{\mathbf{y}}+\mathbf{z}, \qquad \mathbf{z}=\mathbf{y}-\hat{\mathbf{y}} \perp \mathbf{u}$$

$\hat{\mathbf{y}}$ lies in $\text{Span}\{\mathbf{u}\}$ and $\mathbf{z}$ is orthogonal to it. Always sanity-check that $\mathbf{z}\cdot\mathbf{u}=0$.

</div>
</div>

<div class="callout" data-callout="tip">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-lightbulb" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-lightbulb"/></svg></div><div class="callout-title-inner">Orthogonal ⇒ independent</div></div>
<div class="callout-content">

An orthogonal set of **nonzero** vectors is automatically linearly independent. So an orthogonal set of $n$ nonzero vectors in $\mathbb{R}^n$ is immediately a basis — no row reduction required.

</div>
</div>

**Tested as** — is the set orthogonal <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-2-2">6.2.2</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-2-3">6.2.3</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-2-5">6.2.5</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-2-6">6.2.6</a> · orthogonal basis and coordinates <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-2-7">6.2.7</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-2-10">6.2.10</a> · projection onto a line <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-2-11">6.2.11</a> · orthogonal decomposition <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-2-13">6.2.13</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-2-14">6.2.14</a> · orthonormal / normalize <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-2-17">6.2.17</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-2-19">6.2.19</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-2-21">6.2.21</a>

---

## §6.3 Orthogonal Projections {#6-3-orthogonal-projections}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 3</span> <span class="theorem-callout-subtitle">(The Orthogonal Decomposition Theorem)</span>.</div></div>
<div class="callout-content">

Let $W$ be a subspace of $\mathbb{R}^n$. Every $\mathbf{y}\in\mathbb{R}^n$ can be written **uniquely** as

$$\mathbf{y}=\hat{\mathbf{y}}+\mathbf{z}, \qquad \hat{\mathbf{y}}\in W,\ \ \mathbf{z}\in W^{\perp}$$

If $\{\mathbf{u}_1,\dots,\mathbf{u}_p\}$ is an **orthogonal** basis for $W$:

$$\hat{\mathbf{y}}=\operatorname{proj}_{W}\mathbf{y}=\frac{\mathbf{y}\cdot\mathbf{u}_1}{\mathbf{u}_1\cdot\mathbf{u}_1}\mathbf{u}_1+\cdots+\frac{\mathbf{y}\cdot\mathbf{u}_p}{\mathbf{u}_p\cdot\mathbf{u}_p}\mathbf{u}_p$$

The formula **requires an orthogonal basis** — that is why every problem says "verify the set is orthogonal, *then* project."

</div>
</div>

<div class="callout" data-callout="important">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-flame"/></svg></div><div class="callout-title-inner">Best Approximation Theorem</div></div>
<div class="callout-content">

$\hat{\mathbf{y}}$ is the **closest point in $W$ to $\mathbf{y}$**: for every other $\mathbf{v}\in W$,

$$\|\mathbf{y}-\hat{\mathbf{y}}\| < \|\mathbf{y}-\mathbf{v}\|$$

The distance from $\mathbf{y}$ to $W$ is $\|\mathbf{z}\|=\|\mathbf{y}-\hat{\mathbf{y}}\|$. This is the idea least-squares is built on.

</div>
</div>

<div class="callout" data-callout="note">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner">Two useful special cases</div></div>
<div class="callout-content">

- If $\mathbf{y}$ is **already in** $W$, then $\operatorname{proj}_W\mathbf{y}=\mathbf{y}$ and $\mathbf{z}=\mathbf{0}$
- If $\mathbf{y}\perp W$, then $\operatorname{proj}_W\mathbf{y}=\mathbf{0}$

Several §6.3 true/false items are exactly these degenerate cases.

</div>
</div>

**Tested as** — verify orthogonal then project <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-3-4">6.3.4</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-3-5">6.3.5</a> · decompose $\mathbf{y}$ into $W$ and $W^{\perp}$ parts <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-3-8">6.3.8</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-3-9">6.3.9</a> · true/false <a class="internal-link" href="/notes/math-2160/2160-compendium/#6-3-21">6.3.21</a>–<a class="internal-link" href="/notes/math-2160/2160-compendium/#6-3-28">6.3.28</a>

---

## The through-line {#the-through-line}

Chapter 6 is Chapter 1 with a better basis. Finding coordinates went from *solve an augmented system* (§1.3) to *compute independent quotients* (§6.2), purely because the basis is orthogonal. Everything in §6.3 follows from that one simplification.

Related: <a class="internal-link" href="/notes/math-2160/chapter-5-study-guide/">Chapter 5 Study Guide</a> · <a class="internal-link" href="/notes/math-2160/2160-compendium/">2160 Compendium</a>
