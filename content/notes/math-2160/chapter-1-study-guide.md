---
author: "Anish Goyal"
title: "Chapter 1 Study Guide"
description: "Covers §1.1–1.7 (§1.6 not assigned). Based on Lay, Linear Algebra and Its Applications, 6e. Every problem referenced here is transcribed in full with its…"
tags:
  - "notes"
  - "mathematics"
  - "math-2160"
date: 2026-08-09T10:50:49
modified: 2026-08-09T10:50:49
readingtime: "9"
course: "MATH 2160"
course_slug: "math-2160"
subject: "mathematics"
kind: "guide"
ordinal: 1
weight: 5010
slug: "chapter-1-study-guide"
links:
  - "/notes/math-2160/2160-compendium/"
  - "/notes/math-2160/chapter-2-study-guide/"
sources: []
generated: true
---

# Chapter 1 — Linear Equations in Linear Algebra {#chapter-1-linear-equations-in-linear-algebra}

Covers **§1.1–1.7** (§1.6 not assigned). Based on Lay, *Linear Algebra and Its Applications*, 6e. Every problem referenced here is transcribed in full with its recorded answer in <a class="internal-link" href="/notes/math-2160/2160-compendium/">2160 Compendium</a>.

<div class="callout" data-callout="abstract">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-clipboard-list" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-clipboard-list"/></svg></div><div class="callout-title-inner">Weighting</div></div>
<div class="callout-content">

**104 questions** — the largest chapter by far, and **30 of them (28%) are true/false conceptual statements**. Computation alone will not carry this chapter; the definitions have to be precise enough to judge a sentence.

</div>
</div>

---

## §1.1 Systems of Linear Equations {#1-1-systems-of-linear-equations}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 1</span> <span class="theorem-callout-subtitle">(Core vocabulary)</span>.</div></div>
<div class="callout-content">

A system is **consistent** if it has at least one solution, **inconsistent** if none.
Two matrices are **row equivalent** if a sequence of elementary row operations turns one into the other. Row equivalent systems have the **same solution set**.

</div>
</div>

<div class="callout" data-callout="note">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner">The three elementary row operations</div></div>
<div class="callout-content">

1. **Replacement** — add a multiple of one row to another
2. **Interchange** — swap two rows
3. **Scaling** — multiply a row by a nonzero constant

All three are **reversible**. That reversibility is what makes row equivalence an equivalence relation, and it is the single most-tested idea in the §1.1 true/false problems.

</div>
</div>

**Existence and uniqueness.** A system is inconsistent exactly when an echelon form has a row $[\,0\ \cdots\ 0\ \mid b\,]$ with $b \neq 0$. If consistent, the solution is unique when there are no free variables, and infinite otherwise.

**Tested as**
- Solve a $2\times2$ system by elimination — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-1-1">1.1.1</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-1-2">1.1.2</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-1-13">1.1.13</a>
- Intersection of two lines / three planes — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-1-3">1.1.3</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-1-22">1.1.22</a>
- Read consistency off a reduced augmented matrix — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-1-7">1.1.7</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-1-10">1.1.10</a>
- Name the row operation that transforms one matrix into another — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-1-39">1.1.39</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-1-41">1.1.41</a>
- True/false on row operations and row equivalence — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-1-27">1.1.27</a> – <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-1-31">1.1.31</a>

<div class="callout" data-callout="warning">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-alert-triangle" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-alert-triangle"/></svg></div><div class="callout-title-inner">Traps</div></div>
<div class="callout-content">

"Row equivalent" is about the **matrices**, not the solution sets — two systems can share a solution set without being row equivalent.
Elementary row operations are reversible, so no information is lost; a scaling by **zero** is not an elementary operation.

</div>
</div>

---

## §1.2 Row Reduction and Echelon Forms {#1-2-row-reduction-and-echelon-forms}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 2</span> <span class="theorem-callout-subtitle">(Echelon vs. reduced echelon)</span>.</div></div>
<div class="callout-content">

**Echelon form:** all nonzero rows above any zero rows; each leading entry strictly right of the one above; entries below a leading entry are zero.
**Reduced echelon form (RREF):** additionally each leading entry is $1$ and is the *only* nonzero entry in its column.

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 3</span> <span class="theorem-callout-subtitle">(Uniqueness of the reduced echelon form)</span>.</div></div>
<div class="callout-content">

Each matrix is row equivalent to **exactly one** reduced echelon matrix. Echelon form is *not* unique — RREF is. This distinction is tested directly.

</div>
</div>

**Pivots.** A **pivot position** is the location of a leading 1 in the RREF; its column is a **pivot column**. Variables in pivot columns are **basic**; the rest are **free**. The general solution is written by solving each basic variable in terms of the free ones.

**Tested as**
- Classify matrices as echelon / reduced echelon — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-2-2">1.2.2</a>
- Row reduce and identify pivots — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-2-3">1.2.3</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-2-4">1.2.4</a>
- General solution from an augmented matrix — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-2-8">1.2.8</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-2-9">1.2.9</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-2-11">1.2.11</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-2-13">1.2.13</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-2-14">1.2.14</a>
- Consistency from pivot counts — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-2-35">1.2.35</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-2-36">1.2.36</a>

<div class="callout" data-callout="warning">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-alert-triangle" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-alert-triangle"/></svg></div><div class="callout-title-inner">Trap</div></div>
<div class="callout-content">

The system is inconsistent exactly when the **augmented (last) column is a pivot column**. A free variable means infinitely many solutions *only if the system is consistent first*.

</div>
</div>

---

## §1.3 Vector Equations {#1-3-vector-equations}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 4</span> <span class="theorem-callout-subtitle">(Linear combination and Span)</span>.</div></div>
<div class="callout-content">

Given $\mathbf{v}_1,\dots,\mathbf{v}_p$ and scalars $c_1,\dots,c_p$, the vector $c_1\mathbf{v}_1+\cdots+c_p\mathbf{v}_p$ is a **linear combination**. $\text{Span}\{\mathbf{v}_1,\dots,\mathbf{v}_p\}$ is the set of *all* such combinations.

</div>
</div>

<div class="callout" data-callout="important">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-flame"/></svg></div><div class="callout-title-inner">The central translation</div></div>
<div class="callout-content">

These three questions are **the same question**:

$$\mathbf{b} \in \text{Span}\{\mathbf{a}_1,\dots,\mathbf{a}_n\} \iff x_1\mathbf{a}_1+\cdots+x_n\mathbf{a}_n=\mathbf{b} \text{ is consistent} \iff [\,\mathbf{a}_1\ \cdots\ \mathbf{a}_n \mid \mathbf{b}\,] \text{ is consistent}$$

Nearly every §1.3 problem is an application of this equivalence.

</div>
</div>

**Geometry.** $\text{Span}\{\mathbf{v}\}$ is a line through the origin; $\text{Span}\{\mathbf{u},\mathbf{v}\}$ with $\mathbf{u},\mathbf{v}$ not multiples is a plane through the origin. Every span **contains $\mathbf{0}$**.

**Tested as**
- Vector arithmetic — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-3-1">1.3.1</a>
- Convert between vector equations and systems — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-3-5">1.3.5</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-3-6">1.3.6</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-3-9">1.3.9</a>
- Is $\mathbf{b}$ a linear combination? — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-3-11">1.3.11</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-3-13">1.3.13</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-3-14">1.3.14</a>
- Solve for a parameter $h$ so $\mathbf{b}$ lies in a plane — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-3-17">1.3.17</a>
- Center of mass / physical application — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-3-37">1.3.37</a>
- True/false on span notation — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-3-23">1.3.23</a> – <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-3-33">1.3.33</a>

---

## §1.4 The Matrix Equation $A\mathbf{x}=\mathbf{b}$ {#1-4-the-matrix-equation-a-x-b}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 5</span> <span class="theorem-callout-subtitle">(Definition of $A\mathbf{x}$)</span>.</div></div>
<div class="callout-content">

For $A$ with columns $\mathbf{a}_1,\dots,\mathbf{a}_n$ and $\mathbf{x}\in\mathbb{R}^n$:

$$A\mathbf{x}=x_1\mathbf{a}_1+x_2\mathbf{a}_2+\cdots+x_n\mathbf{a}_n$$

$A\mathbf{x}$ is defined only when the number of **columns of $A$** equals the number of **entries of $\mathbf{x}$**.

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 6</span> <span class="theorem-callout-subtitle">(Theorem 4 — the four equivalent statements)</span>.</div></div>
<div class="callout-content">

For an $m\times n$ matrix $A$, these are **all true or all false** together:
1. For each $\mathbf{b}\in\mathbb{R}^m$, $A\mathbf{x}=\mathbf{b}$ has a solution
2. Each $\mathbf{b}\in\mathbb{R}^m$ is a linear combination of the columns of $A$
3. The columns of $A$ span $\mathbb{R}^m$
4. $A$ has a **pivot position in every row**

Note this is about **rows**, not columns — a very common slip.

</div>
</div>

**Tested as**
- Compute $A\mathbf{x}$ two ways — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-4-1">1.4.1</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-4-4">1.4.4</a>
- Translate system ↔ vector equation ↔ matrix equation — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-4-6">1.4.6</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-4-8">1.4.8</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-4-9">1.4.9</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-4-10">1.4.10</a>
- Does $A\mathbf{x}=\mathbf{b}$ have a solution for **every** $\mathbf{b}$? — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-4-15">1.4.15</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-4-17">1.4.17</a>
- Do given vectors span $\mathbb{R}^3$? — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-4-21">1.4.21</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-4-22">1.4.22</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-4-42">1.4.42</a>

<div class="callout" data-callout="warning">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-alert-triangle" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-alert-triangle"/></svg></div><div class="callout-title-inner">Trap</div></div>
<div class="callout-content">

Three vectors in $\mathbb{R}^4$ can **never** span $\mathbb{R}^4$ — you cannot get a pivot in all four rows from three columns. Spanning needs a pivot in every **row**; independence needs a pivot in every **column**.

</div>
</div>

---

## §1.5 Solution Sets of Linear Systems {#1-5-solution-sets-of-linear-systems}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 7</span> <span class="theorem-callout-subtitle">(Homogeneous vs. nonhomogeneous)</span>.</div></div>
<div class="callout-content">

$A\mathbf{x}=\mathbf{0}$ is **homogeneous** and is *always* consistent — $\mathbf{x}=\mathbf{0}$ (the **trivial solution**) always works.
It has a **nontrivial** solution $\iff$ the system has at least one **free variable**.

</div>
</div>

<div class="callout" data-callout="important">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-flame"/></svg></div><div class="callout-title-inner">Parametric vector form</div></div>
<div class="callout-content">

Solutions of $A\mathbf{x}=\mathbf{0}$ are written $\mathbf{x}=s\mathbf{u}+t\mathbf{v}$ — a span through the origin.
Solutions of a consistent $A\mathbf{x}=\mathbf{b}$ are $\mathbf{x}=\mathbf{p}+\mathbf{v}_h$ where $\mathbf{p}$ is one particular solution and $\mathbf{v}_h$ ranges over solutions of the homogeneous equation.

Geometrically: the solution set of $A\mathbf{x}=\mathbf{b}$ is the solution set of $A\mathbf{x}=\mathbf{0}$ **translated** by $\mathbf{p}$. It passes through the origin only when $\mathbf{b}=\mathbf{0}$.

</div>
</div>

**Tested as**
- Nontrivial solutions? — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-5-1">1.5.1</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-5-2">1.5.2</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-5-3">1.5.3</a>
- Parametric vector form — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-5-8">1.5.8</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-5-9">1.5.9</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-5-10">1.5.10</a>
- Line through $\mathbf{a}$ parallel to $\mathbf{b}$ — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-5-23">1.5.23</a>
- Pivot-count reasoning — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-5-41">1.5.41</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-5-42">1.5.42</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-5-44">1.5.44</a>

---

## §1.7 Linear Independence {#1-7-linear-independence}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 8</span> <span class="theorem-callout-subtitle">(Linear independence)</span>.</div></div>
<div class="callout-content">

$\{\mathbf{v}_1,\dots,\mathbf{v}_p\}$ is **linearly independent** if $x_1\mathbf{v}_1+\cdots+x_p\mathbf{v}_p=\mathbf{0}$ forces $x_1=\cdots=x_p=0$.
Equivalently: the columns of $A$ are independent $\iff$ $A\mathbf{x}=\mathbf{0}$ has **only** the trivial solution $\iff$ $A$ has a pivot in **every column**.

</div>
</div>

<div class="callout" data-callout="tip">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-lightbulb" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-lightbulb"/></svg></div><div class="callout-title-inner">Independence by inspection</div></div>
<div class="callout-content">

Several problems are answerable with no row reduction at all:
- A set containing the **zero vector** is always dependent
- **Two** vectors are dependent $\iff$ one is a scalar multiple of the other
- **More vectors than entries** ($p>n$ in $\mathbb{R}^n$) forces dependence

These cover <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-7-15">1.7.15</a> – <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-7-19">1.7.19</a> outright.

</div>
</div>

**Tested as**
- Independence of a vector set — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-7-2">1.7.2</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-7-4">1.7.4</a>
- Independence of matrix columns — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-7-5">1.7.5</a> – <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-7-8">1.7.8</a>
- By inspection — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-7-15">1.7.15</a> – <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-7-19">1.7.19</a>
- Pivot counts for independence vs. spanning — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-7-33">1.7.33</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-7-34">1.7.34</a>
- Build a dependence relation from a stated column relation — <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-7-37">1.7.37</a>, <a class="internal-link" href="/notes/math-2160/2160-compendium/#1-7-38">1.7.38</a>

<div class="callout" data-callout="warning">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-alert-triangle" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-alert-triangle"/></svg></div><div class="callout-title-inner">The distinction to memorize</div></div>
<div class="callout-content">

**Spanning** ⇒ pivot in every **row**. **Independence** ⇒ pivot in every **column**.
For a square matrix these coincide; otherwise they are genuinely different conditions, and the true/false problems exploit exactly that confusion.

</div>
</div>

---

## Chapter 1 in one page {#chapter-1-in-one-page}

| Question | Condition on $A$ |
|---|---|
| Is $A\mathbf{x}=\mathbf{b}$ consistent? | last column of $[A\mid\mathbf{b}]$ is **not** a pivot column |
| Solution unique? | no free variables (pivot in every column) |
| Do columns span $\mathbb{R}^m$? | pivot in every **row** |
| Are columns independent? | pivot in every **column** |
| Nontrivial solution to $A\mathbf{x}=\mathbf{0}$? | at least one free variable |

Related: <a class="internal-link" href="/notes/math-2160/chapter-2-study-guide/">Chapter 2 Study Guide</a> · <a class="internal-link" href="/notes/math-2160/2160-compendium/">2160 Compendium</a>
