---
author: "Anish Goyal"
title: "Chapter 4 Study Guide"
description: "Covers §4.1, 4.2, 4.3, 4.5 (§4.4 and §4.6 not assigned). Full problems and recorded answers in 2160 Compendium."
tags:
  - "notes"
  - "mathematics"
  - "math-2160"
date: 2026-08-09T10:50:49
modified: 2026-08-09T10:50:49
readingtime: "6"
course: "MATH 2160"
course_slug: "math-2160"
subject: "mathematics"
kind: "guide"
ordinal: 4
weight: 5040
slug: "chapter-4-study-guide"
links:
  - "/notes/math-2160/2160-compendium/"
  - "/notes/math-2160/chapter-3-study-guide/"
  - "/notes/math-2160/chapter-5-study-guide/"
sources: []
generated: true
---

# Chapter 4 — Vector Spaces {#chapter-4-vector-spaces}

Covers **§4.1, 4.2, 4.3, 4.5** (§4.4 and §4.6 not assigned). Full problems and recorded answers in <a class="internal-link" href="/notes/math-2160/2160-compendium/">2160 Compendium</a>.

<div class="callout" data-callout="abstract">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-clipboard-list" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-clipboard-list"/></svg></div><div class="callout-title-inner">Weighting</div></div>
<div class="callout-content">

**67 questions**, **13 true/false (19%)**. This is the abstraction step of the course: everything from Chapters 1–2 gets restated without reference to $\mathbb{R}^n$. §4.3 alone carries 23 questions, the largest single section in the course.

</div>
</div>

---

## §4.1 Vector Spaces and Subspaces {#4-1-vector-spaces-and-subspaces}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 1</span> <span class="theorem-callout-subtitle">(Subspace)</span>.</div></div>
<div class="callout-content">

A subset $H$ of a vector space $V$ is a **subspace** if:
1. $\mathbf{0} \in H$
2. $H$ is closed under **addition** — $\mathbf{u},\mathbf{v}\in H \Rightarrow \mathbf{u}+\mathbf{v}\in H$
3. $H$ is closed under **scalar multiplication** — $\mathbf{u}\in H, c$ scalar $\Rightarrow c\mathbf{u}\in H$

All three must hold. To *disprove* a subspace, a **single counterexample** to any one is enough.

</div>
</div>

<div class="callout" data-callout="tip">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-lightbulb" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-lightbulb"/></svg></div><div class="callout-title-inner">The fastest disqualifiers</div></div>
<div class="callout-content">

- Does the set contain $\mathbf{0}$? If not, done — not a subspace.
- Any **nonlinear** condition ($x^2$, $xy$, $|x|$) or **inequality** ($\le$, $\ge$) almost always breaks closure. A set defined by $6x^2+y^2 \le 4$ fails scalar multiplication immediately — scale a point up and you leave the region.
- A condition like $x_1 + x_2 = 1$ (nonzero constant) excludes $\mathbf{0}$.

These dispose of <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-3">4.1.3</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-5">4.1.5</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-7">4.1.7</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-8">4.1.8</a> on sight.

</div>
</div>

<div class="callout" data-callout="note">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner">The reliable way to prove a subspace</div></div>
<div class="callout-content">

Show the set is a **span**. Theorem 1: $\text{Span}\{\mathbf{v}_1,\dots,\mathbf{v}_p\}$ is always a subspace. So write the general element in terms of its free parameters and factor:

$$\begin{bmatrix} a+b \\ b-c \\ a \end{bmatrix} = a\begin{bmatrix}1\\0\\1\end{bmatrix} + b\begin{bmatrix}1\\1\\0\end{bmatrix} + c\begin{bmatrix}0\\-1\\0\end{bmatrix}$$

This is the intended method for <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-10">4.1.10</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-12">4.1.12</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-15">4.1.15</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-17">4.1.17</a>.

</div>
</div>

**Tested as** — subspace or not <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-3">4.1.3</a>–<a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-8">4.1.8</a> · show a set is a subspace <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-9">4.1.9</a>–<a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-17">4.1.17</a> · membership in a span <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-13">4.1.13</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-14">4.1.14</a> · true/false <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-24">4.1.24</a>–<a class="internal-link" href="/notes/math-2160/2160-compendium/#4-1-30">4.1.30</a>

---

## §4.2 Null Spaces, Column Spaces, and Row Spaces {#4-2-null-spaces-column-spaces-and-row-spaces}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 2</span> <span class="theorem-callout-subtitle">(The three spaces)</span>.</div></div>
<div class="callout-content">

| Space | Definition | Lives in | Found by |
|---|---|---|---|
| $\text{Nul}\,A$ | $\{\mathbf{x} : A\mathbf{x}=\mathbf{0}\}$ | $\mathbb{R}^{n}$ (cols) | solve $A\mathbf{x}=\mathbf{0}$, parametric form |
| $\text{Col}\,A$ | span of the columns of $A$ | $\mathbb{R}^{m}$ (rows) | pivot columns of **original** $A$ |
| $\text{Row}\,A$ | span of the rows of $A$ | $\mathbb{R}^{n}$ | nonzero rows of the echelon form |

</div>
</div>

<div class="callout" data-callout="warning">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-alert-triangle" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-alert-triangle"/></svg></div><div class="callout-title-inner">The two traps</div></div>
<div class="callout-content">

**$\text{Nul}\,A$ and $\text{Col}\,A$ live in different spaces** unless $A$ is square. For a $3\times5$ matrix, $\text{Nul}\,A \subseteq \mathbb{R}^5$ but $\text{Col}\,A \subseteq \mathbb{R}^3$.

Testing membership differs fundamentally:
- Is $\mathbf{w}\in\text{Nul}\,A$? — just **compute $A\mathbf{w}$** and check it is $\mathbf{0}$.
- Is $\mathbf{w}\in\text{Col}\,A$? — **solve** $A\mathbf{x}=\mathbf{w}$ and check consistency.

That contrast is precisely what <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-2-23">4.2.23</a> and <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-2-24">4.2.24</a> ask.

</div>
</div>

**Tested as** — membership in $\text{Nul}\,A$ <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-2-1">4.2.1</a> · spanning set for $\text{Nul}\,A$ <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-2-3">4.2.3</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-2-5">4.2.5</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-2-6">4.2.6</a> · is $W$ a vector space <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-2-8">4.2.8</a>–<a class="internal-link" href="/notes/math-2160/2160-compendium/#4-2-13">4.2.13</a> · find $A$ with a given $\text{Col}\,A$ <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-2-15">4.2.15</a> · vectors in each space <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-2-21">4.2.21</a>

---

## §4.3 Linearly Independent Sets; Bases {#4-3-linearly-independent-sets-bases}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 3</span> <span class="theorem-callout-subtitle">(Basis)</span>.</div></div>
<div class="callout-content">

$\mathcal{B}=\{\mathbf{b}_1,\dots,\mathbf{b}_p\}$ is a **basis** for subspace $H$ if it is **linearly independent** *and* **spans $H$**. Both conditions — a spanning set that is dependent is not a basis, and an independent set that is too small is not either.

</div>
</div>

<div class="callout" data-callout="important">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-flame"/></svg></div><div class="callout-title-inner">Finding bases — three different procedures</div></div>
<div class="callout-content">

**Basis for $\text{Nul}\,A$:** solve $A\mathbf{x}=\mathbf{0}$, write in parametric vector form; the vectors attached to the free variables form the basis.

**Basis for $\text{Col}\,A$:** row reduce to find which columns are pivot columns, then take **those columns of the original $A$** — never the reduced ones. Row reduction preserves *which* columns are pivotal, not the column space itself.

**Basis for $\text{Row}\,A$:** take the **nonzero rows of the echelon form**. Here the reduced version *is* correct, because row operations preserve the row space.

The asymmetry between $\text{Col}$ and $\text{Row}$ is the most commonly tested subtlety in the chapter — <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-3-13">4.3.13</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-3-14">4.3.14</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-3-28">4.3.28</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-3-30">4.3.30</a> all turn on it.

</div>
</div>

<div class="callout" data-callout="tip">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-lightbulb" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-lightbulb"/></svg></div><div class="callout-title-inner">"Describe the set" problems</div></div>
<div class="callout-content">

Eight problems open with *"Describe the set $\{\mathbf{v}_1,\mathbf{v}_2,\dots\}$"*. They are asking for the **geometric** object spanned: a line through the origin, a plane through the origin, or all of $\mathbb{R}^n$. Count the independent vectors — that is the dimension of the span.

</div>
</div>

**Tested as** — describe a span <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-3-1">4.3.1</a>–<a class="internal-link" href="/notes/math-2160/2160-compendium/#4-3-8">4.3.8</a> · basis for $\text{Nul}\,A$ <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-3-9">4.3.9</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-3-10">4.3.10</a> · basis for a plane/line <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-3-11">4.3.11</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-3-12">4.3.12</a> · bases for all three spaces <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-3-13">4.3.13</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-3-14">4.3.14</a> · basis for a spanned space <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-3-16">4.3.16</a> · function and polynomial spaces <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-3-36">4.3.36</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-3-44">4.3.44</a>

---

## §4.5 The Dimension of a Vector Space {#4-5-the-dimension-of-a-vector-space}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 4</span> <span class="theorem-callout-subtitle">(Dimension, rank, nullity)</span>.</div></div>
<div class="callout-content">

$\dim H$ is the number of vectors in **any** basis for $H$ (all bases have the same size).

$$\operatorname{rank}A=\dim\text{Col}\,A=\dim\text{Row}\,A=\#\text{pivots}$$

$$\operatorname{nullity}A=\dim\text{Nul}\,A=\#\text{free variables}$$

</div>
</div>

<div class="callout" data-callout="important">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-flame"/></svg></div><div class="callout-title-inner">The Rank–Nullity Theorem</div></div>
<div class="callout-content">

For an $m\times n$ matrix $A$:

$$\operatorname{rank}A+\dim\text{Nul}\,A=n \quad (\text{the number of \textbf{columns}})$$

Every §4.5 dimension problem is an application. Note it is $n$ — the columns — not $m$.

Also: $\dim\text{Row}\,A=\dim\text{Col}\,A$ always, even for non-square $A$. Row rank equals column rank.

</div>
</div>

<div class="callout" data-callout="tip">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-lightbulb" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-lightbulb"/></svg></div><div class="callout-title-inner">Worked instance</div></div>
<div class="callout-content">

If $A$ is $5\times7$ with $\dim\text{Nul}\,A=3$, then $\operatorname{rank}A=7-3=4$, so $\dim\text{Col}\,A=\dim\text{Row}\,A=4$. That is <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-5-37">4.5.37</a> in one line.

</div>
</div>

**Tested as** — basis and dimension of a subspace <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-5-6">4.5.6</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-5-8">4.5.8</a> · dimension of a span <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-5-9">4.5.9</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-5-10">4.5.10</a> · all three dimensions from a matrix <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-5-11">4.5.11</a>–<a class="internal-link" href="/notes/math-2160/2160-compendium/#4-5-15">4.5.15</a> · rank–nullity <a class="internal-link" href="/notes/math-2160/2160-compendium/#4-5-37">4.5.37</a>

Related: <a class="internal-link" href="/notes/math-2160/chapter-3-study-guide/">Chapter 3 Study Guide</a> · <a class="internal-link" href="/notes/math-2160/chapter-5-study-guide/">Chapter 5 Study Guide</a> · <a class="internal-link" href="/notes/math-2160/2160-compendium/">2160 Compendium</a>
