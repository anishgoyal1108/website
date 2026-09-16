---
author: "Anish Goyal"
title: "Law of Total Probability and Bayes' Theorem"
description: "Since S {i1}^m Bi"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-01-28T04:19:07
modified: 2026-01-28T04:29:00
readingtime: "3"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 3
weight: 30
slug: "law-of-total-probability-and-bayes-theorem"
links: []
sources:
  - "Course lecture slides 4"
generated: true
---

## Partitions {#partitions}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.1</span> <span class="theorem-callout-subtitle">(Partition of the Sample Space)</span>.</div></div>
<div class="callout-content">

A collection $\{B_1, B_2, \dots, B_m\}$ is a partition of $S$ if
- $B_i \cap B_j = \emptyset$ for $i \ne j$
- $\bigcup_{i=1}^m B_i = S$

</div>
</div>

- Let $A \subset S$
- Since $S = \bigcup_{i=1}^m B_i$

$$
A = A \cap S = \bigcup_{i=1}^m (A \cap B_i)
$$

- Define $C_i = A \cap B_i$
- Then $\{C_1, \dots, C_m\}$ is a disjoint collection with

$$
A = \bigcup_{i=1}^m C_i
$$

## Law of Total Probability {#law-of-total-probability}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="03.2" id="blk-a7145d">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 03.2</span> <span class="theorem-callout-subtitle">(Law of Total Probability)</span>.</div></div>
<div class="callout-content">

Let $\{B_1, \dots, B_m\}$ be a partition of $S$ with $P[B_i] > 0$ for all $i$
Then for any event $A$

$$
P[A] = \sum_{i=1}^m P[A \mid B_i] P[B_i]
$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/eeng-3421/law-of-total-probability-and-bayes-theorem/#blk-a7145d">Law of Total Probability</a>.</span>
Since $A = \bigcup_{i=1}^m (A \cap B_i)$ and the sets are disjoint

$$
P[A] = \sum_{i=1}^m P[A \cap B_i]
$$

By definition of conditional probability

$$
P[A \cap B_i] = P[A \mid B_i] P[B_i]
$$

<span class="math-booster-end-proof"></span>

</blockquote>

## Joint and Marginal Probabilities {#joint-and-marginal-probabilities}
- If events are classified by two partitions
	- Table entries represent $P[A \cap B]$
- Marginal probabilities obtained by summation

$$
P[A] = \sum_j P[A \cap B_j]
$$

## Bayes Theorem {#bayes-theorem}

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="03.3" id="blk-7a60c1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 03.3</span> <span class="theorem-callout-subtitle">(Bayes Theorem)</span>.</div></div>
<div class="callout-content">

For events $A$ and $B$ with $P[A] > 0$

$$
P[B \mid A] = \frac{P[A \mid B] P[B]}{P[A]}
$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/eeng-3421/law-of-total-probability-and-bayes-theorem/#blk-7a60c1">Bayes Theorem</a>.</span>
From the definition of conditional probability

$$
P[A \cap B] = P[B \mid A] P[A] = P[A \mid B] P[B]
$$

Solving for $P[B \mid A]$ yields the result
<span class="math-booster-end-proof"></span>

</blockquote>

## Bayes Theorem with a Partition {#bayes-theorem-with-a-partition}

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="03.4" id="blk-e56be9">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 03.4</span> <span class="theorem-callout-subtitle">(Bayes Theorem for Partitions)</span>.</div></div>
<div class="callout-content">

Let $\{B_1, \dots, B_m\}$ be a partition with $P[B_i] > 0$
Then

$$
P[B_k \mid A] = \frac{P[A \mid B_k] P[B_k]}{\sum_{i=1}^m P[A \mid B_i] P[B_i]}
$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof of <a class="internal-link ref-theorem" href="/notes/eeng-3421/law-of-total-probability-and-bayes-theorem/#blk-e56be9">Bayes Theorem for Partitions</a>.</span>
Apply Bayes theorem and substitute

$$
P[A] = \sum_{i=1}^m P[A \mid B_i] P[B_i]
$$

from the Law of Total Probability
<span class="math-booster-end-proof"></span>

</blockquote>

## Examples {#examples}

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.5</span>.</div></div>
<div class="callout-content">

Let $\{B_1, B_2, B_3\}$ denote machines producing resistors
Let $A$ denote the event a resistor is acceptable
Given

$$
P[A \mid B_1], \; P[A \mid B_2], \; P[A \mid B_3]
$$

and

$$
P[B_1], \; P[B_2], \; P[B_3]
$$

Then

$$
P[A] = \sum_{i=1}^3 P[A \mid B_i] P[B_i]
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.6</span>.</div></div>
<div class="callout-content">

Given $A$ occurred, the probability the resistor came from machine $B_3$ is

$$
P[B_3 \mid A] = \frac{P[A \mid B_3] P[B_3]}{P[A]}
$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 4</span>
