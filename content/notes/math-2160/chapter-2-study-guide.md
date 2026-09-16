---
author: "Anish Goyal"
title: "Chapter 2 Study Guide"
description: "Covers §2.1–2.3. Full problems and recorded answers in 2160 Compendium."
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
ordinal: 2
weight: 5020
slug: "chapter-2-study-guide"
links:
  - "/notes/math-2160/2160-compendium/"
  - "/notes/math-2160/chapter-1-study-guide/"
  - "/notes/math-2160/chapter-3-study-guide/"
sources: []
generated: true
---

# Chapter 2 — Matrix Algebra {#chapter-2-matrix-algebra}

Covers **§2.1–2.3**. Full problems and recorded answers in <a class="internal-link" href="/notes/math-2160/2160-compendium/">2160 Compendium</a>.

<div class="callout" data-callout="abstract">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-clipboard-list" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-clipboard-list"/></svg></div><div class="callout-title-inner">Weighting</div></div>
<div class="callout-content">

**54 questions**, of which **16 (29%) are true/false**. This chapter is where matrix algebra stops behaving like ordinary arithmetic, and almost every conceptual question probes one of those failures.

</div>
</div>

---

## §2.1 Matrix Operations {#2-1-matrix-operations}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 1</span> <span class="theorem-callout-subtitle">(The operations)</span>.</div></div>
<div class="callout-content">

**Sum** $A+B$ — defined only when $A$ and $B$ have the **same size**; entrywise.
**Scalar multiple** $rA$ — entrywise.
**Product** $AB$ — defined only when $\text{cols}(A)=\text{rows}(B)$. If $A$ is $m\times n$ and $B$ is $n\times p$, then $AB$ is $m\times p$.
**Column rule:** $AB=[\,A\mathbf{b}_1\ \ A\mathbf{b}_2\ \cdots\ A\mathbf{b}_p\,]$ — each column of $AB$ is $A$ times the corresponding column of $B$.

</div>
</div>

<div class="callout" data-callout="warning">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-alert-triangle" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-alert-triangle"/></svg></div><div class="callout-title-inner">Where matrix algebra breaks</div></div>
<div class="callout-content">

These are the source of nearly every true/false question in §2.1:
- $AB \neq BA$ in general — **not** commutative
- $AB=AC$ does **not** imply $B=C$ — no cancellation
- $AB=0$ does **not** imply $A=0$ or $B=0$
- $(A+B)^2 \neq A^2+2AB+B^2$ unless $A$ and $B$ commute
- $(AB)^T = B^T A^T$ — the transpose **reverses** the order

</div>
</div>

**Tested as**
- Compute sums/products, or explain why undefined — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-1-1">2.1.1</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-1-2">2.1.2</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-1-4">2.1.4</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-1-5">2.1.5</a>
- Size arithmetic — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-1-7">2.1.7</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-1-8">2.1.8</a>
- Find $k$ making $AB=BA$ — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-1-9">2.1.9</a>
- Verify $AB=AC$ with $B\neq C$ — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-1-10">2.1.10</a>
- Transpose identities — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-1-23">2.1.23</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-1-24">2.1.24</a>
- Column-relation reasoning — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-1-26">2.1.26</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-1-27">2.1.27</a>
- Powers $A^k$ — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-1-47">2.1.47</a>

<div class="callout" data-callout="tip">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-lightbulb" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-lightbulb"/></svg></div><div class="callout-title-inner">Reasoning about columns without computing</div></div>
<div class="callout-content">

If two columns of $B$ are equal, the corresponding columns of $AB$ are equal (by the column rule). If column 4 of $B$ is the sum of columns 1 and 5, the same relation holds in $AB$. These follow immediately from $AB=[A\mathbf{b}_1\ \cdots]$ — no arithmetic needed.

</div>
</div>

---

## §2.2 The Inverse of a Matrix {#2-2-the-inverse-of-a-matrix}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 2</span> <span class="theorem-callout-subtitle">(Invertibility)</span>.</div></div>
<div class="callout-content">

$A$ ($n\times n$) is **invertible** if there is $A^{-1}$ with $AA^{-1}=A^{-1}A=I_n$. A non-square matrix is **never** invertible.

</div>
</div>

<div class="callout" data-callout="important">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-flame"/></svg></div><div class="callout-title-inner">The $2\times2$ formula</div></div>
<div class="callout-content">

For $A=\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ with $\det A = ad-bc \neq 0$:

$$A^{-1}=\frac{1}{ad-bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

Swap the diagonal, negate the off-diagonal, divide by the determinant. If $ad-bc=0$, $A$ is **not** invertible.

</div>
</div>

<div class="callout" data-callout="note">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner">The row-reduction algorithm</div></div>
<div class="callout-content">

To invert a larger matrix, row reduce $[\,A \mid I\,]$. If $A$ reduces to $I$, the right half is $A^{-1}$:

$$[\,A \mid I\,] \sim [\,I \mid A^{-1}\,]$$

If $A$ does **not** reduce to $I$, then $A$ is not invertible.

</div>
</div>

<div class="callout" data-callout="warning">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-alert-triangle" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-alert-triangle"/></svg></div><div class="callout-title-inner">Order-reversing identities</div></div>
<div class="callout-content">

$(AB)^{-1} = B^{-1}A^{-1}$ and $(A^{T})^{-1} = (A^{-1})^{T}$.
A product of invertible matrices is invertible; a **sum** of invertible matrices need not be.

</div>
</div>

**Tested as**
- Invert by formula — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-2-1">2.2.1</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-2-3">2.2.3</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-2-4">2.2.4</a>
- Invert by row reduction — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-2-39">2.2.39</a> – <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-2-42">2.2.42</a>
- Solve $A\mathbf{x}=\mathbf{b}$ via $A^{-1}$ — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-2-9">2.2.9</a>
- Prove $ABC$ invertible — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-2-25">2.2.25</a>
- Why invertibility gives independent / spanning columns — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-2-31">2.2.31</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-2-32">2.2.32</a>
- True/false on inverse algebra — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-2-11">2.2.11</a> – <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-2-19">2.2.19</a>

---

## §2.3 Characterizations of Invertible Matrices {#2-3-characterizations-of-invertible-matrices}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 3</span> <span class="theorem-callout-subtitle">(The Invertible Matrix Theorem)</span>.</div></div>
<div class="callout-content">

For a **square** $n\times n$ matrix $A$, the following are **equivalent** — all true or all false together:
1. $A$ is invertible
2. $A$ is row equivalent to $I_n$
3. $A$ has $n$ pivot positions
4. $A\mathbf{x}=\mathbf{0}$ has only the trivial solution
5. The columns of $A$ are linearly independent
6. $\mathbf{x}\mapsto A\mathbf{x}$ is one-to-one
7. $A\mathbf{x}=\mathbf{b}$ has a solution for every $\mathbf{b}\in\mathbb{R}^n$
8. The columns of $A$ span $\mathbb{R}^n$
9. $\mathbf{x}\mapsto A\mathbf{x}$ is onto
10. There is $C$ with $CA=I$; there is $D$ with $AD=I$
11. $A^{T}$ is invertible
12. $\det A \neq 0$ (from Chapter 3)

**This theorem is the spine of the whole course.** It is why §1.4 spanning and §1.7 independence collapse into one condition for square matrices, and it reappears in Chapters 3, 4, 5, and 6.

</div>
</div>

<div class="callout" data-callout="warning">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-alert-triangle" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-alert-triangle"/></svg></div><div class="callout-title-inner">The one restriction that matters</div></div>
<div class="callout-content">

Every statement above assumes $A$ is **square**. For non-square matrices, independence and spanning remain genuinely different — this is the trap in most §2.3 true/false problems.

</div>
</div>

<div class="callout" data-callout="tip">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-lightbulb" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-lightbulb"/></svg></div><div class="callout-title-inner">"Use as few calculations as possible"</div></div>
<div class="callout-content">

Six §2.3 problems are phrased this way. The intent is *not* to row reduce. Look for a shortcut:
- a **zero row or column** ⇒ not invertible
- two identical or proportional rows/columns ⇒ not invertible
- **triangular** matrix ⇒ invertible $\iff$ no zero on the main diagonal
- $2\times2$ ⇒ just check $ad-bc$

</div>
</div>

**Tested as**
- Invertible with minimal computation — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-3-1">2.3.1</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-3-3">2.3.3</a> – <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-3-8">2.3.8</a>
- IMT-based true/false — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-3-11">2.3.11</a> – <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-3-20">2.3.20</a>
- Triangular matrices — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-3-21">2.3.21</a>
- Inconsistency ⇒ what about $H$? — <a class="internal-link" href="/notes/math-2160/2160-compendium/#2-3-30">2.3.30</a>

Related: <a class="internal-link" href="/notes/math-2160/chapter-1-study-guide/">Chapter 1 Study Guide</a> · <a class="internal-link" href="/notes/math-2160/chapter-3-study-guide/">Chapter 3 Study Guide</a> · <a class="internal-link" href="/notes/math-2160/2160-compendium/">2160 Compendium</a>
