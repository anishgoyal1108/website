---
author: "Anish Goyal"
title: "Number Systems"
description: "Ordinal: Arranging things sequentially or making lists"
tags:
  - "notes"
  - "mathematics"
  - "analysis"
date: 2025-05-17T12:06:28
modified: 2025-08-01T13:59:08
readingtime: "30"
course: "A First Course in Analysis (Pedrick)"
course_slug: "analysis"
subject: "mathematics"
kind: "lecture"
ordinal: 1
weight: 10
slug: "number-systems"
links:
  - "/notes/math-2130/injection/"
sources:
  - "Pedrick, A First Course in Analysis"
generated: true
---

## Ways to Count {#ways-to-count}
- Ordinal: Arranging things sequentially or making lists
- Cardinal: Responding to the question "how many?"

## Counting {#counting}
- The establishment of a one-to-one correspondence between objects and a set of numerals
- Make steps from a numeral to the successive numeral
- For a successor to be defined:

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.1</span> <span class="theorem-callout-subtitle">(Successor Properties)</span>.</div></div>
<div class="callout-content">

a. Every object has a unique successor
b. Different objects have different successors
c. There is an object that is not the successor of any object (the "first" object)

</div>
</div>

## The Abstract Number System {#the-abstract-number-system}
- A set of objects $\mathbb{N}$ in which there is a successor operation $*$ satisfying the successor properties
- Each number system must be a realization of this system

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.2</span> <span class="theorem-callout-subtitle">(Complete Matching)</span>.</div></div>
<div class="callout-content">

Identify the "first" elements of both sets, then their successors with each other, then identify the successors of any pair that is already identified. This is a *complete matching* of the two sets.

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.3</span> <span class="theorem-callout-subtitle">(Extended Successor Property)</span>.</div></div>
<div class="callout-content">

A subset of $\mathbb{N}$ is *all* of $\mathbb{N}$ if it includes the initial element and the successor of each element of $\mathbb{N}$.

</div>
</div>

## Peano Axioms {#peano-axioms}

<div class="callout theorem-callout theorem-callout-axiom theorem-callout-en theorem-callout-mathwiki" data-callout="axiom" data-callout-metadata="*">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-lock"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Axiom</span> <span class="theorem-callout-subtitle">(Peano Axiom 1)</span>.</div></div>
<div class="callout-content">

Every $n \in \mathbb{N}$ has a unique successor $n^{*} \in \mathbb{N}$.

</div>
</div>

<div class="callout theorem-callout theorem-callout-axiom theorem-callout-en theorem-callout-mathwiki" data-callout="axiom" data-callout-metadata="*">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-lock"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Axiom</span> <span class="theorem-callout-subtitle">(Peano Axiom 2)</span>.</div></div>
<div class="callout-content">

$n \ne m \implies n^{*} \ne m^{*}$

</div>
</div>

<div class="callout theorem-callout theorem-callout-axiom theorem-callout-en theorem-callout-mathwiki" data-callout="axiom" data-callout-metadata="*">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-lock"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Axiom</span> <span class="theorem-callout-subtitle">(Peano Axiom 3)</span>.</div></div>
<div class="callout-content">

There exists an element (denoted 1), in $\mathbb{N}$ such that $1 \ne n^{*} \ \forall \ n \in \mathbb{N}$.

</div>
</div>

<div class="callout theorem-callout theorem-callout-axiom theorem-callout-en theorem-callout-mathwiki" data-callout="axiom" data-callout-metadata="*">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-lock"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Axiom</span> <span class="theorem-callout-subtitle">(Peano Axiom 4 (Induction Axiom))</span>.</div></div>
<div class="callout-content">

If $S \subset \mathbb{N}$ satisfies
$1 \in S \quad \text{(One-Case)}$
and
$n \in S \Rightarrow n^{*} \in S \quad \text{(Inductive Step)},$
then $S = \mathbb{N}$.

</div>
</div>

## Addition {#addition}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.4</span> <span class="theorem-callout-subtitle">(Addition)</span>.</div></div>
<div class="callout-content">

$$
\begin{align}
m + 1 &= m^{*}, \\
m + n^{*} &= (m + n)^{*}
\end{align}
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="01.5" id="blk-794319">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 01.5</span> <span class="theorem-callout-subtitle">(Associativity of Addition)</span>.</div></div>
<div class="callout-content">

$$(m + n) + k = m + (n + k)$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="01.6" id="blk-f3102b">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 01.6</span> <span class="theorem-callout-subtitle">(Commutativity of Addition)</span>.</div></div>
<div class="callout-content">

$$m + n = n + m$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-794319">Associativity of Addition</a>.</span>
One-Case $(k = 1)$:

$$(m + n)^* = m + n^* $$

RHS

$$m + n^{*}$$

LHS

$$(m + n)^* = m + n^{*}$$

Since LHS = RHS, the One-Case is complete.

**Inductive Step $(k = k^{*})$:**

$$
\begin{align}
(m + n) + k^* &= [(m + n) + k]^* && \text{by the one-case} \\
&= [m + (n + k)]^* && \text{by the induction hypothesis} \\
&= m + (n + k)^* && \text{by the one-case} \\
&= m + (n + k^*) && \text{by the one-case}
\end{align}
$$

We have shown that $(m + n) + k^{*} = m + (n + k^{*})$; thus, the Inductive Step is complete and so is the proof.
<span class="math-booster-end-proof"></span>

</blockquote>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-f3102b">Commutativity of Addition</a>.</span>(<cite class="cite cite-quote"><q>Exercises 8 and 9</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;22]</span></cite>)
One-Case $(n = 1)$:

$$1 + 1 = 1 + 1$$

This is trivially true.

Inductive Step $(n = n^{*})$:

$$1 + n^{*} = n^{*} + 1$$

RHS:

$$\begin{align}
n^* + 1 &= (n + 1) + 1 \\
&= (n + 1)^{*}
\end{align}$$

LHS:

$$\begin{align}
1 + n^* &= (1 + n)^* &&\\
&= (n + 1)^* && \text{by the inductive hypothesis}
\end{align}$$

Since, RHS = LHS, the Inductive Step is complete and so concludes the proof.
<span class="math-booster-end-proof"></span>

</blockquote>

## Multiplication {#multiplication}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.7" id="blk-5622a8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.7</span> <span class="theorem-callout-subtitle">(Multiplication)</span>.</div></div>
<div class="callout-content">

$$
\begin{align}
1 \cdot m &= m, \\
m \cdot n^* &= m \cdot n + m
\end{align}
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="01.8" id="blk-578c05">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 01.8</span> <span class="theorem-callout-subtitle">(Left Distributive Law)</span>.</div></div>
<div class="callout-content">

$$m \cdot (n + k) = m \cdot n + m \cdot k$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="01.9" id="blk-688f1f">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 01.9</span> <span class="theorem-callout-subtitle">(Right Distributive Law)</span>.</div></div>
<div class="callout-content">

$$(n + k) \cdot m = n \cdot m + k \cdot m$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="01.10" id="blk-1ba8eb">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 01.10</span>.</div></div>
<div class="callout-content">

$$1 \cdot n = n \ \forall \ n \in \mathbb{N}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="01.11" id="blk-876eba">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 01.11</span> <span class="theorem-callout-subtitle">(Associativity of Multiplication)</span>.</div></div>
<div class="callout-content">

$$m \cdot (n \cdot k) = (m \cdot n) \cdot k$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="01.12" id="blk-23656f">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 01.12</span> <span class="theorem-callout-subtitle">(Commutativity of Multiplication)</span>.</div></div>
<div class="callout-content">

$$m \cdot n = n \cdot m$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-1ba8eb">Proposition 01.10</a>.</span>(<cite class="cite cite-quote"><q>Exercise 10</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;23]</span></cite>)
One-Case $(m = 1)$:

$$1 \cdot 1 = 1$$

Trivially true.

Inductive Step $(m = m^{*})$:

$$1 \cdot m^{*} = m^{*}$$

RHS:

$$n^{*} = n+1$$

LHS:

$$\begin{align}
1 \cdot (n+1) &= 1 \cdot n + 1
\end{align}$$

Since RHS = LHS, the Inductive Step is complete, and so is the proof.

This shows commutativity holds for the first part of the definition of multiplication. 1 is a **neutral element under multiplication** since $1 \cdot m = m \cdot 1 = m \ \forall \ m \in \mathbb{N}$
<span class="math-booster-end-proof"></span>

</blockquote>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-578c05">Left Distributive Law</a>.</span>
One-Case $(k = 1)$:

$$m \cdot (n + 1) = m + n + m \cdot 1$$

RHS:

$$m \cdot n + m \cdot 1 = m \cdot n + m$$

LHS:

$$\begin{align}
m \cdot (n + 1) &= m \cdot n^*  \\
&= m \cdot n + m
\end{align}$$

Since RHS = LHS, the One-Case is complete.

Inductive Step $(k = k^*)$:

$$m \cdot (n + k^*) = m \cdot n + m \cdot k^*$$

RHS:

$$m \cdot n + m \cdot k^*$$

LHS:

$$\begin{align}
m \cdot (n + k^*) &= m \cdot (n+k)^* \\
&= m \cdot (n + k) + m \\
&= m \cdot n + m \cdot k + m \\
&= m \cdot n + m \cdot k^* \\
\end{align}$$

Since RHS = LHS, the Inductive Step is complete and so is the proof.
<span class="math-booster-end-proof"></span>

</blockquote>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-688f1f">Right Distributive Law</a>.</span>(<cite class="cite cite-quote"><q>Exercise 11</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;23]</span></cite>)
One-Case $(m = 1)$:

$$(n + k) \cdot 1 = n \cdot 1 + k \cdot 1$$

RHS:

$$n \cdot 1 + k \cdot 1 = n + k$$

LHS:

$$(n + k) \cdot 1 = n + k$$

Since RHS = LHS, the One-Case is complete.

Inductive Step $(m = m^*)$:

$$(n + k) \cdot m^* = n \cdot m^* + k \cdot m^*$$

RHS:

$$\begin{align}
n \cdot m^* + k \cdot m^* &= n \cdot m + n + k \cdot m + k \\
&= n \cdot m + k \cdot m + n + k
\end{align}$$

LHS:

$$\begin{align}
(n + k) \cdot m^* &= (n + k) \cdot m + (n + k) \\
&= n \cdot m + k \cdot m + n + k
\end{align}$$

Since the RHS = LHS, the Inductive Step is complete, and so is the proof.
<span class="math-booster-end-proof"></span>

</blockquote>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-876eba">Associativity of Multiplication</a>.</span>(<cite class="cite cite-quote"><q>Exercise 12</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;23]</span></cite>)
One-Case $(k = 1)$:

$$m \cdot (n \cdot 1) = (m \cdot n) \cdot 1$$

RHS:

$$(m \cdot n) \cdot 1 = m \cdot n$$

LHS:

$$m \cdot (n \cdot 1) = m \cdot n$$

Since RHS = LHS, the One-Case holds.

Inductive Step $(k = k^*)$:

$$m \cdot (n \cdot k^*) = (m \cdot n) \cdot k^*$$

RHS:

$$(m \cdot n) \cdot k^* = m \cdot n \cdot k + m \cdot n$$

LHS:

$$\begin{align}
m \cdot (n \cdot k^*) &= m \cdot (n \cdot k + n) \\
&= m \cdot n \cdot k + m \cdot n
\end{align}$$

Since RHS = LHS, the Inductive Step is complete and so is the proof.
<span class="math-booster-end-proof"></span>

</blockquote>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-23656f">Commutativity of Multiplication</a>.</span>(<cite class="cite cite-quote"><q>Exercise 12</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;23]</span></cite>)
One-Case $(n = 1)$:
Already proven in Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-1ba8eb">Proposition 01.10</a>.

Inductive Step $(n = n^*)$:

$$m \cdot n^* = n^* \cdot m$$

RHS:

$$\begin{align}
n^* \cdot m &= (n + 1) \cdot m \\
&= n \cdot m + 1 \cdot m \\
&= n \cdot m + m
\end{align}$$

LHS:

$$\begin{align}
m \cdot n^* &= m \cdot n + m \\
&= n \cdot m + m
\end{align}$$

Since RHS = LHS, the Inductive Step is complete and so is the proof.
<span class="math-booster-end-proof"></span>

</blockquote>

## Ordering {#ordering}
- $\mathbb{N}$ is naturally ordered
- $m < n \implies \exists k \in \mathbb{N} : m + k = n$

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="01.13">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 01.13</span> <span class="theorem-callout-subtitle">(Transitive Law)</span>.</div></div>
<div class="callout-content">

$l < m \land m < n \Rightarrow l < n$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="01.14" id="blk-70680e">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 01.14</span> <span class="theorem-callout-subtitle">(Trichotomy Property)</span>.</div></div>
<div class="callout-content">

$m = n \lor m < n \lor n < m \ \forall \ (m, n) \in \mathbb{N}$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-70680e">Trichotomy Property</a>.</span>(<cite class="cite cite-quote"><q>EXERCISE 13</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;24]</span></cite>)
The <a class="internal-link" href="/notes/analysis/number-systems/#peano-axioms">Peano Axioms</a> imply that $\mathbb{N}$ can be decomposed into three distinct sets:
- $\{m \in \mathbb{N}: m < n\}$
- $\{n\}$
- $\{m \in \mathbb{N}: n < m\}$

Fix $n \in \mathbb{N}$. Define $T = \{ m \in \mathbb{N} : m = n \lor m < n \lor n < m \}$.

**One-Case**: $1 \in T$
- If $n = 1$, then $1 = n$.
- If $n \ne 1$, then $1 < n$.

So $1 \in T$.

**Inductive Step**: Assume $m \in T$. Then one of the following holds:

- If $m = n$, then $m^* = n^*$, so $n < m^*$, hence $m^* \in T$.
- If $m < n$, then $\exists k \in \mathbb{N}$ such that $m + k = n$.

Then $m^* + k = (m + 1) + k = m + (1 + k) = m + k + 1 = n + 1 = n^*$, so $m^* < n^*$, hence $m^* < n \lor m^* = n \lor n < m^*$, thus $m^* \in T$.

- If $n < m$, then $\exists k \in \mathbb{N}$ such that $n + k = m$. Then $n + k + 1 = m^*$, so $n < m^*$, hence $m^* \in T$.

By induction, $T = \mathbb{N}$. Therefore, $m = n \lor m < n \lor n < m$ for all $m, n \in \mathbb{N}$.
<span class="math-booster-end-proof"></span>

</blockquote>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="01.15" id="blk-4af6cd">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 01.15</span> <span class="theorem-callout-subtitle">(Addition preserves order)</span>.</div></div>
<div class="callout-content">

$$m < n \implies m + k < n + k$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="01.16" id="blk-64af07">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 01.16</span> <span class="theorem-callout-subtitle">(Multiplication preserves order)</span>.</div></div>
<div class="callout-content">

$$m < n \implies m \cdot k < n \cdot k$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-4af6cd">Addition preserves order</a>.</span>(<cite class="cite cite-quote"><q>EXERCISE 14</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;24]</span></cite>)
$m < n \implies \exists \ b \in \mathbb{N}: n = m + b$

$k \in \mathbb{N} \implies m + k = n - b + k$

$n - b + k$ is trivially less than $n + k$, so the proof is complete. 
<span class="math-booster-end-proof"></span>

</blockquote>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-64af07">Multiplication preserves order</a>.</span>(<cite class="cite cite-quote"><q>EXERCISE 14</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;24]</span></cite>)
$m < n \implies \exists \ b \in \mathbb{N}: n = m + b$

$k \in \mathbb{N} \implies m \cdot k = (n - b) \cdot k$

$(n-b) \cdot k$ is trivially less than $n \cdot k$, so the proof is complete.
<span class="math-booster-end-proof"></span>

</blockquote>

### Remark on Induction {#remark-on-induction}
- Authors use ellipse or etc. when writing proofs, an implicit use of induction
- We can create a "careful" definition that uses induction for these omitted details 
- <cite class="cite cite-quote"><q>Factorial example</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;24]</span></cite>

## Exponentiation {#exponentiation}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.17">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.17</span> <span class="theorem-callout-subtitle">(Exponentiation)</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 15</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;24]</span></cite>) 

$$\begin{align}
m ^ 1 &= m \\
m^{n^*} &=m^n \cdot m
\end{align}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="01.18" id="blk-681f6f">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 01.18</span> <span class="theorem-callout-subtitle">(Exponent Addition Law)</span>.</div></div>
<div class="callout-content">

$$m^n \cdot m^k = m^{n + k}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="01.19" id="blk-d506f2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 01.19</span> <span class="theorem-callout-subtitle">(Exponent Distributive Law)</span>.</div></div>
<div class="callout-content">

$$(m \cdot n)^k = m^k \cdot n^k$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="01.20" id="blk-e55740">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 01.20</span> <span class="theorem-callout-subtitle">(Exponent Multiplication Law)</span>.</div></div>
<div class="callout-content">

$$\left(m^n\right)^k = m^{n \cdot k}$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-681f6f">Exponent Addition Law</a>.</span>(<cite class="cite cite-quote"><q>EXERCISE 16</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;24]</span></cite>) 
One-Case $(k = 1)$:

$$m^n \cdot m^1 = m^{n + 1}$$

RHS:

$$m^{n+1} = m^{n^*}$$

LHS:

$$\begin{align}
m^{n} \cdot m^1 &= m^n \cdot m \\
&= m^{n^*}
\end{align}$$

Since RHS = LHS, the One-Case holds.

Inductive Step $(k = k^{*})$:

$$m^{n} \cdot m^{k^*} = m^{n + k^*}$$

RHS:

$$m^{n + k^*}$$

LHS:

$$\begin{align}

</blockquote>

m^n \cdot m^{k^*} &= m^n \cdot m^k \cdot m \\
&= (m^n \cdot m^k) \cdot m \\
&= m^{n+k} \cdot m \\
&= m^{(n + k)^*} \\
&= m^{n + k^*}
\end{align}$$

<blockquote>

Since RHS = LHS, the Inductive Step is complete and so is the proof.
<span class="math-booster-end-proof"></span>

</blockquote>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-d506f2">Exponent Distributive Law</a>.</span>(<cite class="cite cite-quote"><q>EXERCISE 16</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;24]</span></cite>) 
One-Case $(k = 1)$:

$$(m \cdot n)^1 = m^1 \cdot n^1$$

RHS:

$$m^1 \cdot n^1 = m \cdot n$$

LHS:

$$(m \cdot n)^1 = m \cdot n$$

Since RHS = LHS, the One-Case holds.

Inductive Step $(k = k^*)$:

$$(m \cdot n)^{k^*} = m^{k^*} \cdot n^{k^*}$$

RHS:

$$\begin{align}
m^{k^*} \cdot n^{k^*} &= (m^k \cdot m) \cdot (n^k \cdot n) \\
&= (m^k \cdot n^k) \cdot (m \cdot n)
\end{align}$$

LHS:

$$\begin{align}
(m \cdot n)^{k^*} &= (m \cdot n)^k \cdot (m \cdot n) \\
&= (m^k \cdot n^k) \cdot (m \cdot n) \\
&= (m^k \cdot n^k) \cdot (m \cdot n)
\end{align}$$

Since RHS = LHS, the Inductive Step is complete and so is the proof.
<span class="math-booster-end-proof"></span>

</blockquote>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-e55740">Exponent Multiplication Law</a>.</span>(<cite class="cite cite-quote"><q>EXERCISE 16</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;24]</span></cite>) 
One-Case $(k=1)$:

$$(m^n)^1 = m^{n \cdot 1}$$

RHS:

$$m^{n \cdot 1} = m^{n}$$

LHS:

$$(m^n)^1 = m^n$$

Since RHS = LHS, the One-Case holds.

Inductive Step $(k = k^*)$:

$$(m^n)^{k^*} = m^{n \cdot k^*}$$

RHS:

$$\begin{align}
m^{n \cdot k^*} &= m^{n \cdot k + n} \\
&= m^{n \cdot k} \cdot m^n
\end{align}$$

LHS:

$$\begin{align}
(m^n)^{k^*} &= (m^n)^k \cdot m^n \\
&= m^{n \cdot k} \cdot m^n
\end{align}$$

Since RHS = LHS, the Inductive Step is complete and so is the proof.
<span class="math-booster-end-proof"></span>

</blockquote>

## Miscellaneous Proofs with Induction {#miscellaneous-proofs-with-induction}

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>(<cite class="cite cite-quote"><q>EXERCISE  17</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;26]</span></cite>)
One-Case $(n = 1)$:

$$(1 + x)^1 \ge 1 + 1 \cdot x$$

RHS:

$$1 + 1 \cdot x = 1 + x$$

LHS:

$$(1 + x)^1 = 1 + x$$

Since RHS = LHS, $\ge$ can be refined to =, and the One-Case holds. This also implies all choices of $x$ work when $n=1$.

Inductive Step $(n = n^*)$:

$$(1 + x)^{n^*} \ge 1 + n^* \cdot x$$

RHS:

$$1 + n^* \cdot x = 1 + n \cdot x + x$$

LHS:

$$\begin{align}
(1 + x)^{n^*} &= (1+x)^n(1+x) \\
&\ge (1+ n \cdot x)(1+x) \\
&= 1 + n \cdot x + x + n \cdot x^2
\end{align}$$

Since LHS contains an extra $n \cdot x^2$ than the RHS, which is guaranteed to be positive for $x \ge -1$, the Inductive Step is complete and so is the proof. The inequality does not hold for $x < -1$ because $(1 + x)$ would be negative, reversing the inequality.
<span class="math-booster-end-proof"></span>

</blockquote>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span><cite class="cite cite-quote"><q>EXERCISE 18</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;26]</span></cite>
One-Case $(n=1)$:

$$1^2 = \frac{1 (1+1)(2\cdot 1 + 1)}{6}$$

RHS:

$$\begin{align}
\frac{1 (1+1)(2\cdot 1 + 1)}{6} &=\frac{1 \cdot 2 \cdot 3}{6} \\
&= \frac{6}{6} \\
&=1
\end{align}$$

LHS:

$$1^2 = 1$$

Since RHS = LHS, the One-Case holds.

Inductive Step $(n=n^*)$:

$$1^2 + 2^2 + \dots + n^2 + (n^*)^2 = \frac{n^*(n^* + 1)(2n^* + 1)}{6}$$

RHS:

$$\frac{n^*(n^* + 1)(2n^* + 1)}{6}$$

LHS:

$$\begin{align}
1^2 + 2^2 + \dots + n^2 + (n^*)^2 &= (1^2 + 2^2 + \dots + n^2) + (n^*)^2 \\
&= \frac{n(n+1)(2n+1)}{6} + (n^*)^2 \\
&= \frac{n(n^*)(2n + 1)}{6} +(n^*)^2 \\
&= \frac{n^*}{6}\left(n(2n+1) + 6n^*\right) \\
&= \frac{n^*}{6}\left((n^*-1)(2n^*-1)+6n^*\right) \\
&= \frac{n^*}{6}\left(2(n^*)^2 + 3n^* + 1\right) \\
&= \frac{n^*}{6}\left((2n^*+1)(n^*+1)\right) \\
&= \frac{n^*(2n^*+1)(n^*+1)}{6} \\
&=\frac{n^*(n^*+1)(2n^*+1)}{6}
\end{align}$$

Since RHS = LHS, the Inductive Step is complete and so is the proof.
<span class="math-booster-end-proof"></span>

</blockquote>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span><cite class="cite cite-quote"><q>EXERCISE 19</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;26]</span></cite>
One-Case $(n = 1)$:

$$2 \cdot 1 - 1 = 1^2$$

RHS:

$$1^2 = 1$$

LHS:

$$\begin{align}
2 \cdot 1 - 1 &= 2 - 1 \\
&= 1
\end{align}$$

Since RHS = LHS, the One-Case holds.

Inductive Step $(n = n^*)$:

$$1 + 3 + 5 + \dots + (2n - 1) + (2n^* - 1) = (n^*)^2$$

RHS:

$$\begin{align}
(n^*)^2 &= (n+1)^2  \\
&= n^2 + 2n + 1 \\
&= n^2 + (2n + 1) \\
&=n^2 + (2n^* - 1)
\end{align}$$

LHS:

$$\begin{align}
1 + 3 + 5 + \dots + (2n - 1) + (2n^* - 1) &= (1 + 3 + 5 + \dots + (2n - 1)) + (2n^* - 1) \\
&= n^2 + (2n^* - 1)
\end{align}$$

Since RHS = LHS, the Inductive Step is complete and so is the proof.
<span class="math-booster-end-proof"></span>

</blockquote>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="01.21">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 01.21</span> <span class="theorem-callout-subtitle">(Summation up to $n$)</span>.</div></div>
<div class="callout-content">

$$1 + 2 + \dots + n = \frac{n(n+1)}{2} =\frac{n^2 + n}{2}$$

Proven in <cite class="cite cite-quote"><q>This example</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;25]</span></cite>

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span><cite class="cite cite-quote"><q>EXERCISE 20</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;26]</span></cite>
One-Case $(n = 1)$:

$$1^3 = 1^2$$

Trivially true.

Inductive Step $(n = n^*)$:

$$1^3 + 2^3 + \dots + n^3 + (n^*)^3 = (1 + 2 + \dots + n + n^*)^2$$

RHS:

$$\begin{align}
(1 + 2 + \dots + n + n^*)^2 &= \left(\frac{(n^*)^2 + n^*}{2}\right)^2 \\
&= \frac{(n^*)^4 + 2(n^*)^3 + (n^*)^2}{4} \\ \\
&= \frac{(n+1)^4 + 2(n+1)^3 + (n+1)^2}{4}
\end{align}$$

By the Binomial Theorem (which is covered later, but just as a shortcut):

$$
\begin{align}
(n+1)^4 &= \binom{4}{0}n^4 + \binom{4}{1}n^3 + \binom{4}{2}n^2 + \binom{4}{3}n + \binom{4}{4} \\
&= n^4 + 4n^3 + 6n^2 + 4n + 1\\
(n+1)^3 &= \binom{3}{0}n^3 + \binom{3}{1}n^2 + \binom{3}{2}n + \binom{3}{3} \\
&= n^3 + 3n^2 + 3n + 1
\end{align}
$$

Therefore:

$$\begin{align}
\frac{(n+1)^4 + 2(n+1)^3 + (n+1)^2}{4} &= \frac{(n^4 + 4n^3 + 6n^2 + 4n + 1)}{4} \\ \\
&+ \frac{2(n^3 + 3n^2 + 3n + 1) + (n^2 + 2n + 1)}{4} \\
&= \frac{n^4 + 6n^3 + 13n^2 + 12n + 4}{4}
\end{align}$$

LHS:

$$\begin{align}
1^3 + 2^3 + \dots + n^3 + (n^*)^3 &= (1^3 + 2^3 + \dots + n^3) + (n^*)^3 \\
&= \left(\frac{n^2 + n}{2}\right)^2 + (n^*)^3 \\
&= \frac{n^4 + 2n^3 + n^2}{4} + n^3 + 3n^2 + 3n + 1 \\
&= \frac{n^4 + 2n^3 + n^2}{4} + \frac{4n^3 + 12n^2 + 12n + 4}{4} \\
&= \frac{n^4 + 6n^3 + 13n^2 + 12n + 4}{4}
\end{align}$$

Since RHS = LHS, the Inductive Step is complete and so is the proof.
<span class="math-booster-end-proof"></span>

</blockquote>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="01.22">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 01.22</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 21</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;26]</span></cite>)
Inductive Step $(n = n^*)$:

$$(n^*)^2 + 3n^* + 1 \equiv 0 \pmod 2$$

RHS:

$$0\pmod 2$$ 

LHS:

$$\begin{align}
(n^*)^2 + 3n^* + 1 &= (n+1)^2 + 3(n+1) + 1 \\
&= n^2 + 2n + 1 + 3n + 3 + 1 \\
&= (n^2 + 3n + 1) + 2n + 4
\end{align}$$

Taking everything mod 2:

$$\begin{align}
(n^2 + 3n + 1) + 2n + 4 &\equiv 2n + 4 \pmod 2 \\
&\equiv 2(n+4) \pmod 2 \\
&= 0 \pmod 2
\end{align}$$

Since RHS = LHS, the Inductive Step is complete. However, the One-Case fails for any arbitrary $n$. This is why the One-Case should never be overlooked in an inductive proof.

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="01.23">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 01.23</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 22</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;26]</span></cite>)
One-Case $(n = 1)$:

$$2^{1} > 1$$

This is trivially true.

Inductive Step $(n = n^*)$:

$$2^{n^*} > n^*$$

RHS:

$$n^* = n+1$$

LHS:

$$\begin{align}
2^{n^*} &= 2^n \cdot 2 \\
&> 2n  \\
\end{align}$$

By transitivity, we obtain $2n \ge n +1$, which holds $\forall n \in \mathbb{N}$. Thus, the Inductive Step is complete and so is the proof.

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="01.24">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 01.24</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 23</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;26]</span></cite>)
One-Case $(n=1)$:

$$11^1 - 4^1 \equiv 0 \pmod 7$$

This is trivially true.

Inductive Step $(n = n^*)$:

$$11^{n^*} - 4^{n^*} \equiv 0 \pmod 7$$

RHS:

$$0 \pmod 7$$

LHS:

$$11^{n^*} - 4^{n^*} = 11^n \cdot 11 - 4^n \cdot 4$$

Taking everything mod 7:

$$\begin{align}
11^n \cdot 11 - 4^n \cdot 4 &= 4^n \cdot 11 - 4^n \cdot 4 \pmod 7\\
&= 4^n (11-4) \pmod 7 \\
&= 0 \pmod 7
\end{align}$$

Since RHS = LHS, the Inductive Step is complete and so is the proof.

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="01.25">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 01.25</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 24</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;26]</span></cite>)
Since we are proving this for $n \ge 4$, we will make the One-Case at $n=4$.

One-Case $(n=4)$:

$$4! > 2^4$$

RHS:

$$2^4 = 16$$

LHS:

$$4! = 24$$

Since $24 > 16$, the One-Case holds.

Inductive Step $(n = n^*)$:

$$n^*! > 2^{n^*}$$

RHS:

$$2^{n^*} = 2^n \cdot 2$$

LHS:

$$\begin{align}
n^*! &= n^* \cdot n! \\
&> n^* \cdot 2^n
\end{align}$$

We obtain $n^* \cdot 2^n \ge 2^n \cdot 2$. This simplifies to

$$n^* \ge 2$$

which is true $\forall n \in \mathbb{N}$. Therefore, the Inductive Step is complete and so is the proof.

</div>
</div>

### Reduction Formulas {#reduction-formulas}
- Complicated formulas may be replaced with the formula for the inductive step of its proof

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="01.26">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 01.26</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 26</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;26]</span></cite>)
One-Case $(n = 0)$:

$$\int x^0 e^x \ \mathrm{d}x = x^0 e^x - 0\int x^{n-1}e^x \ \mathrm{d}x$$

RHS:

$$\begin{align}
x^0 e^x - 0\int x^{n-1}e^x \ \mathrm{d}x &= 1 \cdot e^x \\
&= e^x
\end{align}$$

LHS:

$$\begin{align}
\int x^0 e^x \ \mathrm{dx} &= \int 1 \cdot e^x \ \mathrm{d}x \\
&= \int e^x \ \mathrm{d}x \\
&= e^x
\end{align}$$

Since RHS = LHS, the One-Case holds.

Inductive Step $(n=n^*)$:

$$\int x^{n^*} e^x \ \mathrm{d}x = x^{n^*} e^x - n^*\int x^{n^* - 1}e^x \ \mathrm{d}x$$

RHS:

$$
x^{n^*} e^x - n^*\int x^{n^* - 1}e^x \ \mathrm{d}x = x^{n^*} e^x - n^*\int x^{n}e^x \ \mathrm{d}x
$$

LHS:

$$
\begin{align}
\int x^{n^*} e^x \ \mathrm{d}x &= \int x^{n+1} e^x \ \mathrm{d}x &&\\
&= x^{n+1}e^x - \int e^x \cdot (n+1)x^n \ \mathrm{d}x &&\text{IBP}\\
&= x^{n+1}e^x - (n+1)\int x^ne^x \ \mathrm{d}x \\
&= x^{n^*}e^x - n^* \int x^n e^x \ \mathrm{d}x
\end{align}
$$

Since RHS = LHS, the Inductive Step is complete and so is the proof. Using this reduction formula, we can write the general formula:

$$\int x^n e^x \ \mathrm{d}x = e^x \left[\sum_{i=0}^n (-1)^i \frac{n!}{(n-i)!}x^{n-i}\right].$$

</div>
</div>

## Complete Induction {#complete-induction}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.27">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.27</span> <span class="theorem-callout-subtitle">(Complete (Strong) Induction)</span>.</div></div>
<div class="callout-content">

$S \subset \mathbb{N}$ is all of $\mathbb{N}$ if $1 \in S$ and $\{1, 2, \dots , k\} \subset S$ implies $k+1 \in S$
This is a type of induction that uses all numbers up to and including $n$ to imply $n^*$ rather than just $n$

</div>
</div>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="01.28">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 01.28</span>.</div></div>
<div class="callout-content">

Every nonempty set of natural numbers has a first member.
<cite class="cite cite-quote"><q>Proof</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;27]</span></cite>

</div>
</div>

## Sequence {#sequence}
- A **sequence** of a set $S$ maps $n \in \mathbb{N}$ to $x \in S$
	- They are infinite by definition and repetition of values in $S$ is allowed
- The $n$th value of the sequence is denoted $x_n$
- The sequence itself is indicated by writing its typical value in brackets (e.g. $\{1/n\}$ or $\{x_n\}$)

<a class="zoom" href="/notes/img/sequence-diagram-example.png"><img src="/notes/img/sequence-diagram-example.png" alt="sequence diagram example" loading="lazy"></a>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="01.29">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 01.29</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 28</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;28]</span></cite>)

Part I:

One-Case $(n = 1)$:

$$a ^ 1 - b ^ 1 = k_{1}(a - b)$$

This is trivially true with $k_{1} =1 \in \mathbb{N}$
Inductive Step $(n = n^*)$:

$$a^{n^*} - b^{n^*} = k_{n^*}(a - b)$$

RHS:

$$\begin{align}
k_{n^*}(a-b) &= (k_{n^*} + 1)(a-b) &&\text{add $a-b$}
\end{align}$$

LHS:

$$\begin{align}
a^{n^*} - b^{n^*} &= a \cdot a^n - b \cdot b^n \\
&= (a \cdot a^n + a) - (b \cdot b^n + b) &&\text{add $a - b$} \\
&= a(k_{n}(a-b) + b^n) + a - b \cdot b^n - b \\
&= a \cdot k_{n}(a-b) + a \cdot b^n + a - b \cdot b^n - b \\
&= ak_{n}(a-b) + ab^n - bb^n + a - b \\
&= ak_{n}(a-b)+b_{n}(a-b) + 1(a - b) \\
&= (ak_{n} + b^n + 1)(a-b)
\end{align}$$

Dividing RHS and LHS by $(a-b)$:

$$ak_{n} + b^n + 1 = k_{n^*} + 1 \implies ak_{n} + b^n = k_{n^*}$$

Since $k_{n^*} \in \mathbb{N}$, the Inductive Hypothesis is complete and so is the proof.

Part II:

Important note: I changed the LHS of this identity to $$(a-b)\sum_{i=0}^{n-1}a^ib^{n-1-i}$$

One-Case $(n = 1)$:

$$a^1 - b^1 = (a-b)\sum_{i=0}^{0}a^ib^{0-i}$$

From this, we have $a-b$ on both sides, so the One-Case holds.

Inductive Step $(n = n^*)$:

$$a^{n^*} - b^{n^*} = (a-b)\sum_{i=0}^{n} a^i b^{n-i}$$

RHS:

$$\begin{align}
(a-b)\sum_{i=0}^{n} a^i b^{n-i} &= (a-b)\left( a\sum_{i=0}^{n-1}a^ib^{n-1} + b^n \right)  \\
&= a(a-b)\sum_{i=0}^{n-1}a^ib^{n-1} + b^n(a-b) \\
&=aa^n - ab^n +ab^n - bb^n \\
&= aa^n - bb^n \\
&= a^{n^*} - b^{n^*}
\end{align}$$

LHS:

$$a^{n^*} - b^{n^*}$$

Since RHS = LHS, the Inductive Step is complete, and so is the proof.

</div>
</div>

### More on Sequences {#more-on-sequences}
- The **value set** of a sequence is the set of all points of $x_n$ (the range)
	- If the value set has one point, $x_n$ is a **constant sequence**
- $x_n$ may be restricted to an infinite subset of $\mathbb{N}$ to create a **subsequence**
	- "Infinite" means the sequence extends beyond $m$ for any $m \in \mathbb{N}$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.30">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.30</span>.</div></div>
<div class="callout-content">

Every infinite subset, $\mathbf{K}$, of $\mathbb{N}$ is <a class="internal-link" href="/notes/math-2130/injection/">injective</a> over $\mathbb{N}$, starting with $n_1 =$ the first element of $\mathbf{K}$. The notation is $\{x_{n_k}\}$, where $n_k$ is the first unmatched integer.

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>(<cite class="cite cite-quote"><q>EXERCISE 29</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;29]</span></cite>)
Consider any finite list of prime numbers $p_1, p_2, \ldots, p_n$. It will be shown that there exists at least one additional prime number not included in this list.

Let $P$ be the product of all the prime numbers in the list:

$$
P = p_1 p_2 \cdots p_n.
$$

Let $q = P + 1$. Then $q$ is either prime or not:

- If $q$ is prime, then there is at least one more prime that is not in the list, namely, $q$ itself.
- If $q$ is not prime, then some prime factor $p$ divides $q$. If this factor $p$ were in our list, then it would also divide $P$ (since $P$ is the product of every number in the list). If $p$ divides both $P$ and $q$, then $p$ must also divide the difference of the two numbers:
  $$
  q - P = (P + 1) - P = 1.
  $$
  Since no prime number divides 1, $p$ cannot be in the list. This means that at least one more prime number exists that is not in the list.
<span class="math-booster-end-proof"></span>

</blockquote>

## Extending $\mathbb{N}$ to $\mathbb{Z}$ {#extending-n-to-z}
- Given $m, n \in \mathbb{N}$, solve $m + x = n$
	- There is no such $x \in \mathbb{N}$ when $n \le m$

### $\mathbb{N} \cup \{0\}$ {#n-0}
Adjoining 0 to $\mathbb{N}$ gives us the solution for the equations $n + x = n$, for any $n$ in this new set of numbers.
$\forall \ n \in \mathbb{N} \cup 0$:
- $0 + n = n + 0 = n$
- $0 \cdot n = n \cdot 0 = 0$
- $0 < n$

### Creating $\mathbb{Z}$ {#creating-z}
- We create a “negative $k$” that solves $m + x = n$ when $n < m$
- This results in $\mathbb{Z} = \{-k: k \in \mathbb{N}\} \cup \{0\} \cup \mathbb{N}$ for which the solution is denoted $n-m$
- $\forall \ z \in \mathbb{Z}$, the solution $x$ of $z + x = 0$ is the **additive inverse** of $z$

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="01.31">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 01.31</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 30</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;30]</span></cite>)
Using the definition of additive inverse:

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-03-15-00-54.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-03-15-00-54.svg" alt="01 Number Systems 2025-06-03 15.00.54" loading="lazy"></a></figure>

Therefore, $(-k) \cdot l = -(k \cdot l)$

</div>
</div>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="01.32">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 01.32</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 31</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;30]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-03-15-27-35.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-03-15-27-35.svg" alt="01 Number Systems 2025-06-03 15.27.35" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.33">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.33</span> <span class="theorem-callout-subtitle">(Cancellation Law for Addition)</span>.</div></div>
<div class="callout-content">

$$m + k = n + k \implies m = n$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>(<cite class="cite cite-quote"><q>EXERCISE 32</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;30]</span></cite>)
<a class="zoom" href="/notes/img/exercise-32-cancellation-law.png"><img src="/notes/img/exercise-32-cancellation-law.png" alt="exercise 32 cancellation law" loading="lazy"></a>
<span class="math-booster-end-proof"></span>

</blockquote>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.34">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.34</span> <span class="theorem-callout-subtitle">(Cancellation Law for Multiplication)</span>.</div></div>
<div class="callout-content">

$$m \cdot k = n \cdot k \implies m = n; k \ne 0$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>(<cite class="cite cite-quote"><q>EXERCISE 33</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;30]</span></cite>)

</blockquote>

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-03-16-29-49.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-03-16-29-49.svg" alt="01 Number Systems 2025-06-03 16.29.49" loading="lazy"></a></figure>

<span class="math-booster-end-proof"></span>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.35">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.35</span> <span class="theorem-callout-subtitle">(Inequality Reversing)</span>.</div></div>
<div class="callout-content">

$$m < n \implies -m > -n$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>(<cite class="cite cite-quote"><q>EXERCISE 34</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;30]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-03-16-47-29.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-03-16-47-29.svg" alt="01 Number Systems 2025-06-03 16.47.29" loading="lazy"></a></figure>

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-03-16-56-22.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-03-16-56-22.svg" alt="01 Number Systems 2025-06-03 16.56.22" loading="lazy"></a></figure>

<span class="math-booster-end-proof"></span>

</blockquote>

## Binomial {#binomial}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.36">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.36</span> <span class="theorem-callout-subtitle">(Binomial Coefficients)</span>.</div></div>
<div class="callout-content">

Define $0! = 1$ and

$${n\choose k} = \frac{n!}{k!(n-k)!}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="01.37" id="blk-361032">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 01.37</span> <span class="theorem-callout-subtitle">(Addition of Binomial Coefficients)</span>.</div></div>
<div class="callout-content">

$${n \choose k} + {n \choose k-1} = {n+1 \choose k}$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-361032">Addition of Binomial Coefficients</a>.</span>(<cite class="cite cite-quote"><q>EXERCISE 35.</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;31]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-03-17-14-48.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-03-17-14-48.svg" alt="01 Number Systems 2025-06-03 17.14.48" loading="lazy"></a></figure>

<span class="math-booster-end-proof"></span>

</blockquote>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="01.38" id="blk-c53d3a">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 01.38</span> <span class="theorem-callout-subtitle">(Binomial Theorem)</span>.</div></div>
<div class="callout-content">

$$(a+b)^n = \sum_{k=0}^n {n \choose k} a^{n-k} b^k$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/analysis/number-systems/#blk-c53d3a">Binomial Theorem</a>.</span>(<cite class="cite cite-quote"><q>EXERCISE 36</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;31]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-07-18-42-34.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-07-18-42-34.svg" alt="01 Number Systems 2025-06-07 18.42.34" loading="lazy"></a></figure>

<span class="math-booster-end-proof"></span>

</blockquote>

<div class="callout theorem-callout theorem-callout-exercise theorem-callout-en theorem-callout-mathwiki" data-callout="exercise" data-theorem-index="01.39">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Exercise 01.39</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>EXERCISE 38</q> <span class="cite-src">[Pedrick, <em>A First Course in Analysis</em>, p.&nbsp;31]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-number-systems-2025-06-07-21-05-59.svg"><img src="/notes/excalidraw/01-number-systems-2025-06-07-21-05-59.svg" alt="01 Number Systems 2025-06-07 21.05.59" loading="lazy"></a></figure>

</div>
</div>
