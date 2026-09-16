---
author: "Anish Goyal"
title: "Independence and Tree Diagrams"
description: "Bayes rule used for inference"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-02-04T04:00:13
modified: 2026-02-04T04:09:51
readingtime: "4"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 4
weight: 40
slug: "independence-and-tree-diagrams"
links: []
sources:
  - "Course lecture slides 5"
generated: true
---

## Comments on Bayes Theorem {#comments-on-bayes-theorem}

- Bayes rule used for inference
- Observe an effect and infer a cause
- Events $A_1, \dots, A_n$ represent causes
- Event $B$ represents the observed effect

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="04.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 04.1</span> <span class="theorem-callout-subtitle">(Prior and Posterior Probabilities)</span>.</div></div>
<div class="callout-content">

- $P[A_i]$ prior probability of cause $A_i$
- $P[A_i \mid B]$ posterior probability of cause $A_i$ given effect $B$

</div>
</div>

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="04.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 04.2</span> <span class="theorem-callout-subtitle">(Bayes Theorem for Causes)</span>.</div></div>
<div class="callout-content">

Let $\{A_1, \dots, A_n\}$ be mutually exclusive and collectively exhaustive

$$
P[A_i \mid B] =
\frac{P[A_i] P[B \mid A_i]}{\sum_{j=1}^n P[A_j] P[B \mid A_j]}
$$

</div>
</div>

## Independence {#independence}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="04.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 04.3</span> <span class="theorem-callout-subtitle">(Two Independent Events)</span>.</div></div>
<div class="callout-content">

Events $A$ and $B$ are independent if and only if

$$
P[A \cap B] = P[A] P[B]
$$

</div>
</div>

- Equivalent statements when probabilities are nonzero
	- $P[A \mid B] = P[A]$
	- $P[B \mid A] = P[B]$

## Independent Vs Mutually Exclusive {#independent-vs-mutually-exclusive}

<div class="callout" data-callout="comment">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-message-square" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-message-square"/></svg></div><div class="callout-title-inner">Comment</div></div>
<div class="callout-content">

Independent and mutually exclusive are not synonymous

</div>
</div>

- Mutually exclusive
	- $A \cap B = \emptyset$
	- $P[A \cap B] = 0$
- Independent
	- Intersection probability factors
- Independent events are not mutually exclusive except when
	- $P[A] = 0$ or $P[B] = 0$

## Example {#example}

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.4</span>.</div></div>
<div class="callout-content">

Draw one card from a standard deck
- $A$ event card is a spade
- $B$ event card is a queen

$$
P[A] = \frac{13}{52}, \quad P[B] = \frac{4}{52}
$$

$$
P[A \cap B] = \frac{1}{52}
$$

Since $P[A \cap B] = P[A] P[B]$, the events are independent

</div>
</div>

## Three Independent Events {#three-independent-events}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="04.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 04.5</span> <span class="theorem-callout-subtitle">(Three Independent Events)</span>.</div></div>
<div class="callout-content">

Events $A_1, A_2, A_3$ are mutually independent if and only if
- $A_1$ and $A_2$ are independent
- $A_1$ and $A_3$ are independent
- $A_2$ and $A_3$ are independent
- $$
  P[A_1 \cap A_2 \cap A_3] = P[A_1] P[A_2] P[A_3]
  $$

</div>
</div>

## Example {#example-1}

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.6</span>.</div></div>
<div class="callout-content">

Let $S = \{1,2,3,4\}$ with equiprobable outcomes
- $A_1 = \{1,3,4\}$
- $A_2 = \{2,3,4\}$
- $A_3 = \emptyset$

Although

$$
P[A_1 \cap A_2 \cap A_3] = P[A_1] P[A_2] P[A_3]
$$

the events are not mutually independent since $A_1$ and $A_2$ are not independent

</div>
</div>

## More Than Three Events {#more-than-three-events}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="04.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 04.7</span> <span class="theorem-callout-subtitle">(Mutual Independence)</span>.</div></div>
<div class="callout-content">

For $n \ge 3$, events $A_1, \dots, A_n$ are mutually independent if and only if
- Every collection of $n-1$ events is mutually independent
- $$
  P\!\left[\bigcap_{i=1}^n A_i\right] = \prod_{i=1}^n P[A_i]
  $$

</div>
</div>

## Tree Diagrams {#tree-diagrams}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="04.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 04.8</span> <span class="theorem-callout-subtitle">(Tree Diagram)</span>.</div></div>
<div class="callout-content">

A tree diagram represents a sequential experiment
- Branch labels are probabilities or conditional probabilities
- Each path corresponds to a joint event
- Path probability is the product of branch probabilities

</div>
</div>

$$
P[\text{path}] = \prod \text{branch probabilities}
$$

## Example {#example-2}

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.9</span>.</div></div>
<div class="callout-content">

Radar detection
- $A$ aircraft present
- $B$ alarm generated

$$
P[A] = 0.05
$$

$$
P[B \mid A] = 0.99, \quad P[B \mid A^c] = 0.10
$$

Joint probabilities computed along tree paths

</div>
</div>

## Example {#example-3}

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.10</span>.</div></div>
<div class="callout-content">

False positive test
- $A$ person has disease
- $B$ test positive

$$
P[A] = 0.001
$$

$$
P[B \mid A] = 0.95, \quad P[B^c \mid A^c] = 0.95
$$

Using Bayes theorem

$$
P[A \mid B] =
\frac{P[B \mid A] P[A]}{P[B \mid A] P[A] + P[B \mid A^c] P[A^c]}
$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 5</span>
