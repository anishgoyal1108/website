---
author: "Anish Goyal"
title: "Chapter 5 Study Guide"
description: "Covers §5.1–5.3. Full problems and recorded answers in 2160 Compendium."
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
ordinal: 5
weight: 5050
slug: "chapter-5-study-guide"
links:
  - "/notes/math-2160/2160-compendium/"
  - "/notes/math-2160/chapter-4-study-guide/"
  - "/notes/math-2160/chapter-6-study-guide/"
sources: []
generated: true
---

# Chapter 5 — Eigenvalues and Eigenvectors {#chapter-5-eigenvalues-and-eigenvectors}

Covers **§5.1–5.3**. Full problems and recorded answers in <a class="internal-link" href="/notes/math-2160/2160-compendium/">2160 Compendium</a>.

<div class="callout" data-callout="abstract">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-clipboard-list" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-clipboard-list"/></svg></div><div class="callout-title-inner">Weighting</div></div>
<div class="callout-content">

**44 questions**, **6 true/false (13%)**. Highly procedural: find eigenvalues, find eigenvectors, assemble $P$ and $D$. The procedures chain together, so an error in §5.2 propagates through §5.3.

</div>
</div>

---

## §5.1 Eigenvectors and Eigenvalues {#5-1-eigenvectors-and-eigenvalues}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 1</span> <span class="theorem-callout-subtitle">(Eigenvector and eigenvalue)</span>.</div></div>
<div class="callout-content">

A **nonzero** vector $\mathbf{x}$ is an **eigenvector** of $A$ if

$$A\mathbf{x}=\lambda\mathbf{x}$$

for some scalar $\lambda$, the corresponding **eigenvalue**.

$\mathbf{x}=\mathbf{0}$ is **never** an eigenvector — but $\lambda=0$ **is** a legitimate eigenvalue (it occurs exactly when $A$ is singular).

</div>
</div>

<div class="callout" data-callout="important">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-flame"/></svg></div><div class="callout-title-inner">The two verification questions are different</div></div>
<div class="callout-content">

**"Is $\mathbf{v}$ an eigenvector of $A$?"** — compute $A\mathbf{v}$ and check whether the result is a scalar multiple of $\mathbf{v}$. If $A\mathbf{v}=\lambda\mathbf{v}$, that $\lambda$ is the eigenvalue. Pure multiplication, no solving.

**"Is $\lambda$ an eigenvalue of $A$?"** — check whether $(A-\lambda I)\mathbf{x}=\mathbf{0}$ has a **nontrivial** solution, i.e. whether $A-\lambda I$ is singular. Equivalently $\det(A-\lambda I)=0$.

Confusing these wastes significant time — <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-1-4">5.1.4</a> and <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-1-6">5.1.6</a> are the first kind, <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-1-2">5.1.2</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-1-7">5.1.7</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-1-8">5.1.8</a> the second.

</div>
</div>

<div class="callout" data-callout="note">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner">Eigenspace</div></div>
<div class="callout-content">

The **eigenspace** for $\lambda$ is $\text{Nul}(A-\lambda I)$ — all eigenvectors for $\lambda$, together with $\mathbf{0}$.

**To find a basis:** form $A-\lambda I$, row reduce, solve the homogeneous system, and read off the parametric vector form. This is a §1.5 null-space computation wearing a new name.

</div>
</div>

<div class="callout" data-callout="tip">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-lightbulb" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-lightbulb"/></svg></div><div class="callout-title-inner">Triangular matrices</div></div>
<div class="callout-content">

The eigenvalues of a **triangular** matrix are exactly its **diagonal entries** — no characteristic polynomial needed.

</div>
</div>

**Tested as** — is $\lambda$ an eigenvalue <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-1-2">5.1.2</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-1-7">5.1.7</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-1-8">5.1.8</a> · is $\mathbf{v}$ an eigenvector <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-1-4">5.1.4</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-1-6">5.1.6</a> · basis for an eigenspace <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-1-9">5.1.9</a>–<a class="internal-link" href="/notes/math-2160/2160-compendium/#5-1-16">5.1.16</a> · eigenvalues directly <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-1-17">5.1.17</a>

---

## §5.2 The Characteristic Equation {#5-2-the-characteristic-equation}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 2</span> <span class="theorem-callout-subtitle">(Characteristic polynomial)</span>.</div></div>
<div class="callout-content">

$$\det(A-\lambda I)=0$$

The left side is the **characteristic polynomial**; its roots are the eigenvalues. For $n\times n$ it has degree $n$.

</div>
</div>

<div class="callout" data-callout="important">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-flame"/></svg></div><div class="callout-title-inner">The $2\times2$ shortcut</div></div>
<div class="callout-content">

For $A=\begin{bmatrix} a & b \\ c & d\end{bmatrix}$:

$$\det(A-\lambda I)=\lambda^{2}-(a+d)\lambda+(ad-bc)=\lambda^{2}-(\operatorname{tr}A)\lambda+\det A$$

Worth memorizing — it turns most $2\times2$ eigenvalue problems into a quadratic you can write down immediately.

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 3</span> <span class="theorem-callout-subtitle">(Algebraic vs. geometric multiplicity)</span>.</div></div>
<div class="callout-content">

**Algebraic multiplicity** — the multiplicity of $\lambda$ as a root of the characteristic polynomial.
**Geometric multiplicity** — $\dim$ of the eigenspace, i.e. $\dim\text{Nul}(A-\lambda I)$.

Always $1 \le \text{geometric} \le \text{algebraic}$. When they differ for some eigenvalue, the matrix is **not diagonalizable** — this is the bridge into §5.3 and what <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-2-18">5.2.18</a> is checking.

</div>
</div>

<div class="callout" data-callout="warning">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-alert-triangle" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-alert-triangle"/></svg></div><div class="callout-title-inner">Listing "with multiplicity"</div></div>
<div class="callout-content">

When asked to list eigenvalues *repeated according to multiplicity*, a double root must appear **twice**. The total count must equal $n$ (counting complex roots).

</div>
</div>

**Tested as** — characteristic polynomial and eigenvalues <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-2-1">5.2.1</a>–<a class="internal-link" href="/notes/math-2160/2160-compendium/#5-2-6">5.2.6</a> · characteristic polynomial only <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-2-9">5.2.9</a>–<a class="internal-link" href="/notes/math-2160/2160-compendium/#5-2-14">5.2.14</a> · eigenvalues with multiplicity <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-2-15">5.2.15</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-2-16">5.2.16</a> · multiplicity comparison <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-2-18">5.2.18</a>

---

## §5.3 Diagonalization {#5-3-diagonalization}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 4</span> <span class="theorem-callout-subtitle">(The Diagonalization Theorem)</span>.</div></div>
<div class="callout-content">

$A$ ($n\times n$) is **diagonalizable** $\iff$ $A$ has $n$ **linearly independent eigenvectors**.
In that case $A=PDP^{-1}$, where
- $P$ has the eigenvectors as its **columns**
- $D$ is diagonal with the corresponding eigenvalues **in the same order**

The order must match: column $j$ of $P$ pairs with entry $(j,j)$ of $D$.

</div>
</div>

<div class="callout" data-callout="note">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner">The procedure</div></div>
<div class="callout-content">

1. Find the eigenvalues from $\det(A-\lambda I)=0$
2. Find a basis for each eigenspace
3. Count: if the eigenvectors total $n$, build $P$ and $D$; otherwise report **not diagonalizable**
4. Verify if time permits — check $AP=PD$, which avoids inverting $P$

</div>
</div>

<div class="callout" data-callout="tip">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-lightbulb" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-lightbulb"/></svg></div><div class="callout-title-inner">Sufficient condition</div></div>
<div class="callout-content">

If an $n\times n$ matrix has $n$ **distinct** eigenvalues, it is automatically diagonalizable — eigenvectors from distinct eigenvalues are always independent.

The converse fails: repeated eigenvalues **may** still diagonalize, provided each eigenspace is big enough to match its algebraic multiplicity. A $3\times3$ with two eigenvalues and both eigenspaces one-dimensional gives only $2 < 3$ independent eigenvectors — not diagonalizable (<a class="internal-link" href="/notes/math-2160/2160-compendium/#5-3-30">5.3.30</a>).

</div>
</div>

<div class="callout" data-callout="important">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-flame"/></svg></div><div class="callout-title-inner">Why diagonalize — computing powers</div></div>
<div class="callout-content">

$$A^{k}=PD^{k}P^{-1}, \qquad D^{k}=\begin{bmatrix} \lambda_1^{k} & 0 \\ 0 & \lambda_2^{k}\end{bmatrix}$$

Raising a diagonal matrix to a power is entrywise, so $A^{4}$ or even $A^{k}$ for symbolic $k$ becomes tractable. This is the point of <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-3-1">5.3.1</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-3-2">5.3.2</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-3-3">5.3.3</a>.

</div>
</div>

**Tested as** — diagonalize with eigenvalues given <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-3-11">5.3.11</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-3-12">5.3.12</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-3-15">5.3.15</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-3-16">5.3.16</a> · diagonalize from scratch <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-3-17">5.3.17</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-3-19">5.3.19</a> · compute $A^k$ from $PDP^{-1}$ <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-3-1">5.3.1</a>–<a class="internal-link" href="/notes/math-2160/2160-compendium/#5-3-3">5.3.3</a> · diagonalizability true/false <a class="internal-link" href="/notes/math-2160/2160-compendium/#5-3-21">5.3.21</a>–<a class="internal-link" href="/notes/math-2160/2160-compendium/#5-3-30">5.3.30</a>

Related: <a class="internal-link" href="/notes/math-2160/chapter-4-study-guide/">Chapter 4 Study Guide</a> · <a class="internal-link" href="/notes/math-2160/chapter-6-study-guide/">Chapter 6 Study Guide</a> · <a class="internal-link" href="/notes/math-2160/2160-compendium/">2160 Compendium</a>
