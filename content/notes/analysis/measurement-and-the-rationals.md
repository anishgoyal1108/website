---
author: "Anish Goyal"
title: "Measurement and the Rationals"
description: "Any given amount is really a chosen unit amount a certain \"number\" of times"
tags:
  - "notes"
  - "mathematics"
  - "analysis"
date: 2025-08-01T13:58:03
modified: 2025-08-01T14:01:35
readingtime: "17"
course: "A First Course in Analysis (Pedrick)"
course_slug: "analysis"
subject: "mathematics"
kind: "lecture"
ordinal: 2
weight: 20
slug: "measurement-and-the-rationals"
links: []
sources:
  - "Pedrick, A First Course in Analysis"
generated: true
---

## Measurement Theory {#measurement-theory}
- Any given amount is really a chosen **unit amount** a certain "number" of times
- Two amounts are **commensurable** if they share a unit amount (e.g. $mu$ and $nu$ for $m, n \in \mathbb{Z}$)

### Directed Segments {#directed-segments}
- A single point is a segment of length 0 for all units
- For segments with more than one point, they exist in pairs called **directed segments**
	- Expressed as arrows, one going to the left and the other going to the right
	- Left-directed segments have negatives of their lengths as measures
- All directed segments lie on a single line with initial endpoint at the **origin** $\mathcal{o}$

<a class="zoom" href="/notes/img/directed-segment-example.png"><img src="/notes/img/directed-segment-example.png" alt="directed segment example" loading="lazy"></a>

### Need for Division {#need-for-division}
- If $\alpha$ and $\beta$ are mutually commensurable points with shared unit $u$, then we need to define a number $x$ such that $\beta$ may be expressed in terms of $\alpha$
	- Since $\alpha = nu$ and $\beta = mu$, then $\beta = x\alpha$ and $mu = x \cdot nu \implies m = xn$
- We need to create a number system in which $m = nx$ always has a unique solution
	- Exception: division by zero, so $n \ne 0$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.1</span> <span class="theorem-callout-subtitle">(Division Equivalence)</span>.</div></div>
<div class="callout-content">

The equations $nx = m$ and $qx = p$ $(n, q \ne 0)$ in $\mathbb{Z}$ are **equivalent** if $mq = pn$. Alternatively, it means $\frac{m}{n} = \frac{p}{q}$.

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.2">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.2</span>.</div></div>
<div class="callout-content">

<cite class="cite cite-quote"><q>EXERCISE 1</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;33]</span></cite>
<a class="zoom" href="/notes/img/exercise-1-division-equivalence.png"><img src="/notes/img/exercise-1-division-equivalence.png" alt="exercise 1 division equivalence" loading="lazy"></a>

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.3">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.3</span>.</div></div>
<div class="callout-content">

<cite class="cite cite-quote"><q>EXERCISE 2</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;34]</span></cite>
All numbers can be expressed as products of primes. For a fully simplified fraction, $\frac{a}{b}$, $\gcd(a, b) = 1$, since $a$ and $b$ do not share any factors.

</div>
</div>

## Defining $\mathbb{Q}$ {#defining-q}
- The set of fully simplified fractions forms $\mathbb{Q}$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.4</span> <span class="theorem-callout-subtitle">(Sum of Fractions)</span>.</div></div>
<div class="callout-content">

$$\frac{m}{n} + \frac{p}{q} = \frac{mq + np}{nq}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.5">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.5</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 3</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;34]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-09-21-15-22.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-09-21-15-22.svg" alt="01 Number Systems 2025-06-09 21.15.22" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.6">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.6</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 4</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;34]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-09-21-40-30.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-09-21-40-30.svg" alt="01 Number Systems 2025-06-09 21.40.30" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.7</span> <span class="theorem-callout-subtitle">(Product of Fractions)</span>.</div></div>
<div class="callout-content">

$$\frac{m}{n} \cdot \frac{p}{q} = \frac{m \cdot p}{n \cdot q}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.8">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.8</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 5</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;35]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-09-21-53-38.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-09-21-53-38.svg" alt="01 Number Systems 2025-06-09 21.53.38" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.9">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.9</span>.</div></div>
<div class="callout-content">

<cite class="cite cite-quote"><q>EXERCISE 6.</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;35]</span></cite>

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-09-22-11-59.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-09-22-11-59.svg" alt="01 Number Systems 2025-06-09 22.11.59" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.10">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.10</span>.</div></div>
<div class="callout-content">

<cite class="cite cite-quote"><q>EXERCISE 7.</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;35]</span></cite>

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-09-22-16-23.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-09-22-16-23.svg" alt="01 Number Systems 2025-06-09 22.16.23" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="02.11">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 02.11</span> <span class="theorem-callout-subtitle">(Division of Fractions)</span>.</div></div>
<div class="callout-content">

Any equation in $\mathbb{Q}$ of the form

$$\frac{m}{n} \cdot x = \frac{p}{q}, m \ne 0$$

has the unique solution $\frac{np}{mq}$.

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.12">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.12</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 8.</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;35]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-09-22-27-57.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-09-22-27-57.svg" alt="01 Number Systems 2025-06-09 22.27.57" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.13">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.13</span> <span class="theorem-callout-subtitle">(Order of Fractions)</span>.</div></div>
<div class="callout-content">

The **order** between fractions is given by

$$\frac{m}{n} < \frac{p}{q} \implies mq < np$$

if $n, q > 0$.

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.14">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.14</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 9.</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;35]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-09-22-33-09.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-09-22-33-09.svg" alt="01 Number Systems 2025-06-09 22.33.09" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.15">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.15</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 10</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;35]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-10-12-36-10.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-10-12-36-10.svg" alt="01 Number Systems 2025-06-10 12.36.10" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.16">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.16</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE  11</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;35]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-10-14-15-51.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-10-14-15-51.svg" alt="01 Number Systems 2025-06-10 14.15.51" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.17">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.17</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 12</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;35]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-26-21-28-30.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-26-21-28-30.svg" alt="01 Number Systems 2025-07-26 21.28.30" loading="lazy"></a></figure>

</div>
</div>

## Measurement of Directed Segments {#measurement-of-directed-segments}
- If $\alpha$ and $\beta$ are commensurable, and $\beta$ is not a point ($\alpha = mu, \beta = nu, n \ne 0$), you may express $\alpha$ in terms of $\beta$ using $\mathbb{Q}$ and determine the unit $u$
	- *Only* commensurable lengths can be expressed in terms of each other using $\mathbb{Q}$

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="02.18">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 02.18</span> <span class="theorem-callout-subtitle">(Archimedean Property)</span>.</div></div>
<div class="callout-content">

$\forall y > 0 \in \mathbb{Q}, \exists m \in \mathbb{N} | y \le m$.
Alternative definitions with directed segments: $\forall y > 0 \in \mathbb{Q} \exists k \in \mathbb{N} | y \le k \cdot u$.
“There are arbitrarily large natural numbers.”

</div>
</div>

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="02.19">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 02.19</span> <span class="theorem-callout-subtitle">(Reverse Archimedean Property)</span>.</div></div>
<div class="callout-content">

$\forall x > 0 \in \mathbb{Q}, \exists n \in \mathbb{N} | \frac{1}{n} < x$.
“The reciprocals of the natural numbers can be arbitrarily small.”

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.20">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.20</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 14</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;37]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-26-23-36-56.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-26-23-36-56.svg" alt="01 Number Systems 2025-07-26 23.36.56" loading="lazy"></a></figure>

</div>
</div>

## Axioms of Ordered Fields {#axioms-of-ordered-fields}
- Any number system that satisfies the below properties is called an **ordered field**
	- Number systems that are ordered fields and satisfy the Archimedean property are called **Archimedean ordered fields**

<div class="callout theorem-callout theorem-callout-axiom theorem-callout-en theorem-callout-mathwiki" data-callout="axiom" data-theorem-index="02.21">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-lock"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Axiom 02.21</span> <span class="theorem-callout-subtitle">(Axioms for Addition)</span>.</div></div>
<div class="callout-content">

- Associative and Commutative
- $\exists 0 \in F$ that is neutral under addition.
- $\exists$ additive inverse “negative $x$” $\forall x \in F$.

</div>
</div>

<div class="callout theorem-callout theorem-callout-axiom theorem-callout-en theorem-callout-mathwiki" data-callout="axiom" data-theorem-index="02.22">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-lock"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Axiom 02.22</span> <span class="theorem-callout-subtitle">(Axioms for Multiplication)</span>.</div></div>
<div class="callout-content">

- Associative and Commutative
- $\exists 1 \in F$ that is neutral under multiplication.
- $\exists$ multiplicative inverse $1/x$ $\forall x \in F, x \ne 0$.

</div>
</div>

<div class="callout theorem-callout theorem-callout-axiom theorem-callout-en theorem-callout-mathwiki" data-callout="axiom" data-theorem-index="02.23">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-lock"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Axiom 02.23</span> <span class="theorem-callout-subtitle">(Distributive Laws)</span>.</div></div>
<div class="callout-content">

Multiplication and Addition are connected by the distributive laws.

</div>
</div>

<div class="callout theorem-callout theorem-callout-axiom theorem-callout-en theorem-callout-mathwiki" data-callout="axiom" data-theorem-index="02.24">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-lock"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Axiom 02.24</span> <span class="theorem-callout-subtitle">(Order)</span>.</div></div>
<div class="callout-content">

- Order of $F$ is transitive and trichotomy holds.
- Multiplication by $x > 0$ preserves order.

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.25">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.25</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 15</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;38]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-27-00-06-01.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-27-00-06-01.svg" alt="01 Number Systems 2025-07-27 00.06.01" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.26">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.26</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 16</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;38]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-27-14-09-36.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-27-14-09-36.svg" alt="01 Number Systems 2025-07-27 14.09.36" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.27">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.27</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 17</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;38]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-27-14-22-13.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-27-14-22-13.svg" alt="01 Number Systems 2025-07-27 14.22.13" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.28">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.28</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 18</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;38]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-27-15-09-33.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-27-15-09-33.svg" alt="01 Number Systems 2025-07-27 15.09.33" loading="lazy"></a></figure>

</div>
</div>

## Measurement Density {#measurement-density}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.29">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.29</span> <span class="theorem-callout-subtitle">(Density)</span>.</div></div>
<div class="callout-content">

A number system, $V$, is **dense** in a field, $F$, if:
$\forall x < y \in F, \exists m \in V | x < m < y$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.30">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.30</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 19</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;38]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-27-15-45-39.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-27-15-45-39.svg" alt="01 Number Systems 2025-07-27 15.45.39" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="02.31">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 02.31</span> <span class="theorem-callout-subtitle">(Density of $\mathbb{Q}$ in Archimedean Ordered Fields)</span>.</div></div>
<div class="callout-content">

$\mathbb{Q}$ is dense in any Archimedean ordered field $F$.
<cite class="cite cite-quote"><q>Proof</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;39]</span></cite>

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.32">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.32</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 20</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;40]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-28-08-58-59.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-28-08-58-59.svg" alt="01 Number Systems 2025-07-28 08.58.59" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.33">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.33</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 21</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;40]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-28-10-40-11.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-28-10-40-11.svg" alt="01 Number Systems 2025-07-28 10.40.11" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.34">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.34</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 22</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;40]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-28-10-57-31.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-28-10-57-31.svg" alt="01 Number Systems 2025-07-28 10.57.31" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.35">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.35</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 23</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;40]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-28-13-40-30.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-28-13-40-30.svg" alt="01 Number Systems 2025-07-28 13.40.30" loading="lazy"></a></figure>

</div>
</div>

## Expanding the Definitions of Exponentiation {#expanding-the-definitions-of-exponentiation}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.36">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.36</span> <span class="theorem-callout-subtitle">(Extension of Powers to $\mathbb{Z}$)</span>.</div></div>
<div class="callout-content">

$$x^{0} = 1 \quad \text{and} \quad x^{-n}=\frac{1}{x^n}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.37">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.37</span> <span class="theorem-callout-subtitle">(Extension of Powers to $\mathbb{Q}$)</span>.</div></div>
<div class="callout-content">

$$x^{p/q} = \sqrt[q]{x^p}, q \ne 0$$

- $x^{1/q} = \sqrt[q]{x}$ is the member(s) of $F$ whose $q$th power is $x$. 
	- If $q$ is odd, there is one positive member in $F$.
	- If $q$ is even, there are two members in $F$, one positive and one negative, in pairs. We use the current notation to refer to the positive member unless explicitly denoted otherwise.
- For this extension, we assume the member is defined to begin with. If $\sqrt[q]{x^p}$ is not a member of $F$ (*i.e.,* irrational), we do not consider it.

</div>
</div>

## Interval Notation {#interval-notation}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.38">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.38</span> <span class="theorem-callout-subtitle">(Interval)</span>.</div></div>
<div class="callout-content">

An **interval** is a subset defined using the order of $F$ for $a \le b$ in $F$. The interval may either be open, closed, left-closed right-open, or left-open right-closed. *Open* means you don’t consider the endpoint, and vice-versa. The *length* of the interval is $b-a$.

</div>
</div>

- We use brackets to denote closed interval and parenthesis for open interval
	- For example, the notation for the open interval on $(a, b) \in F$ is:

$$(a, b) =\{x \in F : a < x < b\}$$

- If $a=b$, the closed interval reduces to a point, and all other cases are $\emptyset$
- You can also use $\infty$ in interval notation to denote “half-lines” or a “full line” (which is really just the entire set of points on $F$):
	- For example, the left half-line of the point $a$ (excluding the point $a$ itself) is:

$$(\infty, a) = \{x \in F:x<a\}$$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.39">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.39</span> <span class="theorem-callout-subtitle">(Absolute Value)</span>.</div></div>
<div class="callout-content">

We denote the **absolute value** of $x \in F$ by:

$$|x| = \begin{cases}
x, & x>0 \\
-x, & x<0
\end{cases}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.40">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.40</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 24</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;41]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-28-14-20-10.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-28-14-20-10.svg" alt="01 Number Systems 2025-07-28 14.20.10" loading="lazy"></a></figure>

</div>
</div>

- Since $|x|$ is the distance of $x$ from the origin, we can conclude that $|b-a|$ is the distance between $a, b \in F$
- $\forall x \in F, -|x| \le x \le |x|$, and one of the equality signs must hold

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.41">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.41</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 25</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;41]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-28-14-29-48.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-28-14-29-48.svg" alt="01 Number Systems 2025-07-28 14.29.48" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="02.42">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 02.42</span> <span class="theorem-callout-subtitle">(Triangle Inequality)</span>.</div></div>
<div class="callout-content">

$$|x + y| \le |x| + |y|$$

<cite class="cite cite-quote"><q>Proof</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;41]</span></cite> (using the result from the previous Exercise)

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.43">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.43</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 26</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;41]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-28-14-43-12.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-28-14-43-12.svg" alt="01 Number Systems 2025-07-28 14.43.12" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.44">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.44</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 27</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;41]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-28-16-10-41.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-28-16-10-41.svg" alt="01 Number Systems 2025-07-28 16.10.41" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.45">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.45</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 28</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;41]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-28-16-14-45.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-28-16-14-45.svg" alt="01 Number Systems 2025-07-28 16.14.45" loading="lazy"></a></figure>

</div>
</div>

## Boundedness {#boundedness}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.46">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.46</span> <span class="theorem-callout-subtitle">(Boundedness)</span>.</div></div>
<div class="callout-content">

$S \subset F$ is **bounded above** if:

$$\exists b \in F | x \in S \implies x\le b.$$

Alternatively:

$$\exists b \in F | x \le b \forall x \in S.$$

- Any such $b$ is called an *upper bound* of $F$. 
- Any member of $F$ larger than an upper bound of $S$ is also an upper bound of $S$.

Similar logic applies for **bounded below**:

$$\exists b \in F | x \ge b \forall x \in S.$$

If $S$ is bounded above and below in $F$, it is *bounded*.

</div>
</div>

- The Archimedean property really just says that $\mathbb{N}$ is not bounded above in $F$ for any choice of unit

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.47">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.47</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 31</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;42]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-28-17-18-17.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-28-17-18-17.svg" alt="01 Number Systems 2025-07-28 17.18.17" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.48">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.48</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 32</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;42]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-28-17-35-51.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-28-17-35-51.svg" alt="01 Number Systems 2025-07-28 17.35.51" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.49">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.49</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 33</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;42]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-28-18-06-40.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-28-18-06-40.svg" alt="01 Number Systems 2025-07-28 18.06.40" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.50">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.50</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 34</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;42]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-28-19-04-37.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-28-19-04-37.svg" alt="01 Number Systems 2025-07-28 19.04.37" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.51">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.51</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 35</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;42]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-07-30-15-12-50.svg"><img src="/notes/excalidraw/01-number-systems-2025-07-30-15-12-50.svg" alt="01 Number Systems 2025-07-30 15.12.50" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.52">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.52</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 36</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;42]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-08-01-12-42-11.svg"><img src="/notes/excalidraw/01-number-systems-2025-08-01-12-42-11.svg" alt="01 Number Systems 2025-08-01 12.42.11" loading="lazy"></a></figure>

</div>
</div>

## Division Algorithm {#division-algorithm}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.53">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.53</span> <span class="theorem-callout-subtitle">(Division Algorithm)</span>.</div></div>
<div class="callout-content">

For a *dividend* $n \in F$ and a *divisor* $d > 0 \in F$, there exists a *quotient* $q \in \mathbb{Z}$ and a *remainder* $0 \le r < d$ such that:

$$n = qd + r.$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="02.54">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 02.54</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 37</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;43]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-08-01-13-41-01.svg"><img src="/notes/excalidraw/01-number-systems-2025-08-01-13-41-01.svg" alt="01 Number Systems 2025-08-01 13.41.01" loading="lazy"></a></figure>

</div>
</div>
