---
author: "Anish Goyal"
title: "Chapter 3 Study Guide"
description: "Covers §3.1–3.3. Full problems and recorded answers in 2160 Compendium."
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
ordinal: 3
weight: 5030
slug: "chapter-3-study-guide"
links:
  - "/notes/math-2160/2160-compendium/"
  - "/notes/math-2160/chapter-2-study-guide/"
  - "/notes/math-2160/chapter-4-study-guide/"
sources: []
generated: true
---

# Chapter 3 — Determinants {#chapter-3-determinants}

Covers **§3.1–3.3**. Full problems and recorded answers in <a class="internal-link" href="/notes/math-2160/2160-compendium/">2160 Compendium</a>.

<div class="callout" data-callout="abstract">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-clipboard-list" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-clipboard-list"/></svg></div><div class="callout-title-inner">Weighting</div></div>
<div class="callout-content">

**41 questions**, only **3 true/false (7%)** — the most computational chapter in the course. Points here come from executing cofactor expansion and row reduction cleanly, not from conceptual argument.

</div>
</div>

---

## §3.1 Introduction to Determinants {#3-1-introduction-to-determinants}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 1</span> <span class="theorem-callout-subtitle">(Cofactor expansion)</span>.</div></div>
<div class="callout-content">

The **$(i,j)$ minor** $M_{ij}$ is the determinant of the matrix with row $i$ and column $j$ deleted. The **cofactor** is

$$C_{ij}=(-1)^{i+j}M_{ij}$$

Expansion across row $i$: $\ \det A=a_{i1}C_{i1}+a_{i2}C_{i2}+\cdots+a_{in}C_{in}$
Expansion down column $j$: $\ \det A=a_{1j}C_{1j}+a_{2j}C_{2j}+\cdots+a_{nj}C_{nj}$

**Any row or column gives the same answer.** That freedom is the whole strategy.

</div>
</div>

<div class="callout" data-callout="tip">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-lightbulb" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-lightbulb"/></svg></div><div class="callout-title-inner">The sign pattern</div></div>
<div class="callout-content">

$$\begin{bmatrix} + & - & + \\ - & + & - \\ + & - & + \end{bmatrix}$$

Start with $+$ at the top-left and alternate. Forgetting a sign is the single most common arithmetic error in this chapter.

</div>
</div>

<div class="callout" data-callout="important">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-flame"/></svg></div><div class="callout-title-inner">Choose the row or column with the most zeros</div></div>
<div class="callout-content">

Six §3.1 problems say "at each step, choose a row or column that involves the least amount of computation." A zero entry kills its entire cofactor term, so expanding along a row with two zeros in a $4\times4$ turns four $3\times3$ determinants into one.

</div>
</div>

<div class="callout" data-callout="note">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner">Triangular shortcut</div></div>
<div class="callout-content">

If $A$ is triangular, $\det A$ is the **product of the diagonal entries**. This is why elementary matrices have such easy determinants.

</div>
</div>

**Tested as**
- Expansion across row 1 and down column 2 — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-1-1">3.1.1</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-1-3">3.1.3</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-1-4">3.1.4</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-1-5">3.1.5</a>
- Strategic expansion for minimal work — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-1-9">3.1.9</a> – <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-1-14">3.1.14</a>
- Determinant of an elementary matrix — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-1-25">3.1.25</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-1-26">3.1.26</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-1-29">3.1.29</a>
- Effect of a row operation on $\det$ — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-1-21">3.1.21</a>
- Is $\det(3A)=3\det A$? — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-1-37">3.1.37</a>

---

## §3.2 Properties of Determinants {#3-2-properties-of-determinants}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 2</span> <span class="theorem-callout-subtitle">(Row operations and the determinant)</span>.</div></div>
<div class="callout-content">

| Operation | Effect on $\det$ |
|---|---|
| **Replacement** (add a multiple of one row to another) | **unchanged** |
| **Interchange** two rows | multiplied by $-1$ |
| **Scale** a row by $k$ | multiplied by $k$ |

Replacement being free is what makes row reduction the efficient way to compute a large determinant.

</div>
</div>

<div class="callout" data-callout="important">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-flame"/></svg></div><div class="callout-title-inner">Multiplicative properties</div></div>
<div class="callout-content">

$$\det(AB)=(\det A)(\det B) \qquad \det(A^{T})=\det A \qquad \det(A^{-1})=\frac{1}{\det A}$$

But **$\det(A+B) \neq \det A + \det B$** — the determinant is not linear in the matrix.

For an $n\times n$ matrix and scalar $r$: $\ \det(rA)=r^{n}\det A$ — the scalar comes out **once per row**, hence the exponent $n$. This is exactly what <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-1-37">3.1.37</a> and <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-2-42">3.2.42</a> are testing.

</div>
</div>

<div class="callout" data-callout="note">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner">Invertibility</div></div>
<div class="callout-content">

$A$ is invertible $\iff \det A \neq 0$. This is statement 12 of the <a class="internal-link" href="/notes/math-2160/chapter-2-study-guide/">Invertible Matrix Theorem</a>.

</div>
</div>

**Tested as**
- Name the property illustrated — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-2-1">3.2.1</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-2-2">3.2.2</a>
- Determinant by row reduction to echelon form — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-2-5">3.2.5</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-2-6">3.2.6</a>
- Row reduction combined with cofactor expansion — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-2-12">3.2.12</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-2-14">3.2.14</a>
- Invertibility via determinant — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-2-21">3.2.21</a> – <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-2-23">3.2.23</a>
- Formula for $\det(rA)$ — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-2-42">3.2.42</a>
- Verify $\det AB=(\det A)(\det B)$ — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-2-43">3.2.43</a>
- Combine properties to evaluate — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-2-45">3.2.45</a>

---

## §3.3 Cramer's Rule, Volume, and the Adjugate {#3-3-cramer-s-rule-volume-and-the-adjugate}

<div class="callout" data-callout="important">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-flame"/></svg></div><div class="callout-title-inner">Cramer's Rule</div></div>
<div class="callout-content">

For an **invertible** $n\times n$ matrix $A$, the unique solution of $A\mathbf{x}=\mathbf{b}$ has

$$x_i=\frac{\det A_i(\mathbf{b})}{\det A}$$

where $A_i(\mathbf{b})$ is $A$ with its **$i$-th column replaced by $\mathbf{b}$**.

Requires $\det A \neq 0$. Practical only for small systems, but it is the standard $2\times2$/$3\times3$ exam computation.

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 3</span> <span class="theorem-callout-subtitle">(Adjugate and the inverse formula)</span>.</div></div>
<div class="callout-content">

The **adjugate** is the transpose of the cofactor matrix:

$$\operatorname{adj}A=\begin{bmatrix} C_{11} & C_{21} & \cdots & C_{n1} \\ C_{12} & C_{22} & \cdots & C_{n2} \\ \vdots & & & \vdots \\ C_{1n} & C_{2n} & \cdots & C_{nn} \end{bmatrix}, \qquad A^{-1}=\frac{1}{\det A}\operatorname{adj}A$$

**Note the transpose** — cofactor $C_{ij}$ lands in position $(j,i)$. Forgetting it is the classic error here.

</div>
</div>

<div class="callout" data-callout="note">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner">Determinants as area and volume</div></div>
<div class="callout-content">

- The area of the **parallelogram** determined by columns of a $2\times2$ matrix $A$ is $|\det A|$
- The volume of the **parallelepiped** determined by columns of a $3\times3$ matrix is $|\det A|$

For a parallelogram given by four **vertices**, first translate one vertex to the origin by subtracting it from the others, then take the two edge vectors as columns. Take the **absolute value** — area is never negative.

</div>
</div>

**Tested as**
- Cramer's Rule — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-3-1">3.3.1</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-3-2">3.3.2</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-3-3">3.3.3</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-3-5">3.3.5</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-3-6">3.3.6</a>
- Adjugate and inverse formula — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-3-12">3.3.12</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-3-13">3.3.13</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-3-15">3.3.15</a>
- Area of a parallelogram from vertices — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-3-19">3.3.19</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-3-21">3.3.21</a>
- Volume of a parallelepiped — <a class="internal-link" href="/notes/math-2160/2160-compendium/#3-3-23">3.3.23</a>

Related: <a class="internal-link" href="/notes/math-2160/chapter-2-study-guide/">Chapter 2 Study Guide</a> · <a class="internal-link" href="/notes/math-2160/chapter-4-study-guide/">Chapter 4 Study Guide</a> · <a class="internal-link" href="/notes/math-2160/2160-compendium/">2160 Compendium</a>
