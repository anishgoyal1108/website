---
author: "Anish Goyal"
title: "Decimal Notation and the Irrationals"
description: "A digit is a symbol contained in \\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\\}"
tags:
  - "notes"
  - "mathematics"
  - "analysis"
date: 2025-08-01T14:03:26
modified: 2025-08-05T23:36:50
readingtime: "6"
course: "A First Course in Analysis (Pedrick)"
course_slug: "analysis"
subject: "mathematics"
kind: "lecture"
ordinal: 3
weight: 30
slug: "decimal-notation-and-the-irrationals"
links: []
sources:
  - "Pedrick, A First Course in Analysis"
generated: true
---

## Decimal Representation {#decimal-representation}
- A *digit* is a symbol contained in $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$
- A *number* is a member of an Archimedean ordered field $F$, and may be used interchangeably with *point*

<div class="callout theorem-callout theorem-callout-lemma theorem-callout-en theorem-callout-mathwiki" data-callout="lemma" data-theorem-index="03.1" id="blk-343144">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Lemma 03.1</span> <span class="theorem-callout-subtitle">(Largest Integer $\le x$)</span>.</div></div>
<div class="callout-content">

$\forall x \in F, \exists$ a largest integer $\le x$, denoted $[x]$. 

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/decimal-notation-and-the-irrationals/#blk-343144">Largest Integer $\le x$</a>.</span>(<cite class="cite cite-quote"><q>EXERCISE 1</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;43]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-decimal-notation-and-the-irrationals-2025-08-01-14-08-06.svg"><img src="/notes/excalidraw/03-decimal-notation-and-the-irrationals-2025-08-01-14-08-06.svg" alt="03 Decimal Notation and the Irrationals 2025-08-01 14.08.06" loading="lazy"></a></figure>

<span class="math-booster-end-proof"></span>

</blockquote>

- $[x]$ is the *integer part* of $x$ and $x-[x]$ is the *fractional part* of $x$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.2</span> <span class="theorem-callout-subtitle">(Decimal Representation)</span>.</div></div>
<div class="callout-content">

Let each $b_i$ and $a_i$ be a digit. Then:

$$\begin{align}
[x] &= b_{k}b_{k-1}\dots b_{1}b_{0} \\
x - [x] &= a_{1}a_{2}a_{3} \dots \\
x &= b_{k}b_{k-1}\dots b_{1}b_{0}.a_{1}a_{2}a_{3}\dots
\end{align}$$

If $x < 0$, the representation is $|x|$ prefixed by a minus sign.

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="03.3">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 03.3</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 2</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;43]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-decimal-notation-and-the-irrationals-2025-08-01-14-33-30.svg"><img src="/notes/excalidraw/03-decimal-notation-and-the-irrationals-2025-08-01-14-33-30.svg" alt="03 Decimal Notation and the Irrationals 2025-08-01 14.33.30" loading="lazy"></a></figure> 

</div>
</div>

## Decimal Expansion {#decimal-expansion}
### Integer Part {#integer-part}
- Suppose $k$ is the total number of digits of $[x]$. Then, $10^{k}$ is the upper bound of $[x]$, and we may represent $[x]$ as a unique expansion of $k$ digits multiplied by powers of ten
- Dividing the interval $[0, 10^k)$ into ten equal subintervals that map to digits:

$$
[0, 10^{k-1}), [10^{k-1}, 2\cdot10^{k-1}), \dots, [9\cdot10^{k-1}, 10^k)
$$

- Let $b_k$ be the digit corresponding to the subinterval that contains $[x]$:
	- The use of half-open intervals ensures that at exactly one subinterval contains $[x]$, so each $b_i$ is uniquely determined

$$
[x] \in [b_k 10^{k-1}, (b_k + 1)10^{k-1})
$$

- Divide the selected subinterval again into 10 equal parts of length $10^{k-2}$, and choose $b_{k-1}$ so that:

$$
[x] \in [b_k 10^{k-1} + b_{k-1} 10^{k-2}, b_k 10^{k-1} + (b_{k-1} + 1)10^{k-2})
$$

- Repeat this process down to length $10^0 = 1$, determining each digit $b_i$ such that:

$$
[x] = b_k 10^{k} + b_{k-1} 10^{k-1} + \dots + b_0
$$

- If all $b_i = 0$, then $[x] = 0$. Otherwise, the decimal representation of $[x]$ drops leading zeros and may be simplified to:

$$
[x] = b_k b_{k-1} \dots b_0 \quad \text{with} \quad b_k \ne 0
$$

### Fractional Part {#fractional-part}
- Our goal is to choose digits $a_1, a_2, a_3, \dots$ for which
  $$
  x - [x] = \frac{a_1}{10} + \frac{a_2}{10^2} + \frac{a_3}{10^3} + \dots
  $$
- Divide the interval $[0, 1)$, which contains $x - [x]$, into ten equal parts
  $$
  [0, \tfrac{1}{10}), [\tfrac{1}{10}, \tfrac{2}{10}), \dots, [\tfrac{9}{10}, 1)
  $$
- Choose $a_1$ as the digit such that $x - [x] \in [\tfrac{a_1}{10}, \tfrac{a_1 + 1}{10})$
- Divide $[\tfrac{a_1}{10}, \tfrac{a_1 + 1}{10})$ into ten equal parts
  $$
  \left[\tfrac{a_1}{10}, \tfrac{a_1}{10} + \tfrac{1}{10^2}\right), \left[\tfrac{a_1}{10} + \tfrac{1}{10^2}, \tfrac{a_1}{10} + \tfrac{2}{10^2}\right), \dots, \left[\tfrac{a_1}{10} + \tfrac{9}{10^2}, \tfrac{a_1 + 1}{10}\right)
  $$
- Choose $a_2$ as the digit such that $x - [x]$ lies in the subinterval of length $1/10^2$
- Continue dividing the current subinterval into ten parts of length $1/10^n$ to choose $a_n$ such that $x - [x]$ lies in the $n$th level subinterval
- If $x$ is an endpoint of one of the subintervals, then all $a_n = 0$ from some stage onward and the expansion of $x$ is a finite sum

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="03.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 03.4</span> <span class="theorem-callout-subtitle">(Uniqueness of Decimal Expansion)</span>.</div></div>
<div class="callout-content">

Distinct numbers have distinct decimal expansions. 
<cite class="cite cite-quote"><q>Proof</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;45]</span></cite>

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.5</span> <span class="theorem-callout-subtitle">(Terminating Decimal)</span>.</div></div>
<div class="callout-content">

The endpoints of each subinterval of any decimal expansion may be assigned a decimal that is **terminating** (*i.e.,* concluding with an infinite repetition of the digit 0).

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.6</span> <span class="theorem-callout-subtitle">(Recurring Decimal)</span>.</div></div>
<div class="callout-content">

A decimal expansion $a_0, a_1, a_2, …$ is **recurring** if $\exists N \ge 0 \land k \ge 1 | \forall k > N$, $a_k = a_{k+p}$. That is, the digits repeat with periodicity $p$ at position $N$. 
- The repeating portion has an overline above it.
- *Terminating decimals* are a special case of recurring decimals.

</div>
</div>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="03.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 03.7</span> <span class="theorem-callout-subtitle">(Recurring Decimals and Rationals)</span>.</div></div>
<div class="callout-content">

Every recurring decimal represents a rational number. (<cite class="cite cite-quote"><q>EXERCISE 4</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;46]</span></cite>)
Proof:

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-decimal-notation-and-the-irrationals-2025-08-05-18-25-49.svg"><img src="/notes/excalidraw/03-decimal-notation-and-the-irrationals-2025-08-05-18-25-49.svg" alt="03 Decimal Notation and the Irrationals 2025-08-05 18.25.49" loading="lazy"></a></figure>

The converse that every rational number represents a recurring decimal is also true. <cite class="cite cite-quote"><q>Proof</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;46]</span></cite>

</div>
</div>

## Base-B Expansions {#base-b-expansions}
- It’s possible to create $B$ subdivisions with a max digit of $B-1$
	- The result is called a **Base-$B$** expansion

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.8</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 6</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;47]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-decimal-notation-and-the-irrationals-2025-08-05-19-33-26.svg"><img src="/notes/excalidraw/03-decimal-notation-and-the-irrationals-2025-08-05-19-33-26.svg" alt="03 Decimal Notation and the Irrationals 2025-08-05 19.33.26" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.9</span> <span class="theorem-callout-subtitle">(Sequence Convergence)</span>.</div></div>
<div class="callout-content">

A sequence of numbers, $\{x_{n}\}$, in an Archimedean ordered field $F$ **converges** to $m$, written $x_n \rightarrow m$, if $\forall \epsilon > 0 \in F \exists$ an index $N_{\epsilon}$ such that:

$$|x_{m}| < \epsilon \ \text{if} \ m > N_{\epsilon}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.10</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 7</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;48]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-decimal-notation-and-the-irrationals-2025-08-05-20-09-50.svg"><img src="/notes/excalidraw/03-decimal-notation-and-the-irrationals-2025-08-05-20-09-50.svg" alt="03 Decimal Notation and the Irrationals 2025-08-05 20.09.50" loading="lazy"></a></figure>

</div>
</div>
