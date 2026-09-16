---
author: "Anish Goyal"
title: "Probability Mass Functions"
description: "We now move from events in a sample space to numerical descriptions of outcomes"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-02-23T15:13:57
modified: 2026-02-23T15:15:06
readingtime: "4"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 7
weight: 70
slug: "probability-mass-functions"
links: []
sources:
  - "Course lecture slides 11–12"
generated: true
---

## Random Variables {#random-variables}

- We now move from events in a sample space to numerical descriptions of outcomes
- A random variable assigns a real number to each outcome of an experiment
- The random variable is written with a capital letter such as $X$
- The set of possible values of $X$ is called the range of $X$
- We denote the range by $S_X$
- If multiple random variables are used then we similarly write $S_Y$ and so on

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="07.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 07.1</span> <span class="theorem-callout-subtitle">(Random Variable)</span>.</div></div>
<div class="callout-content">

A random variable consists of
- An experiment with probability measure $P[\cdot]$ defined on a sample space $S$
- A function that assigns a real number to each outcome in $S$

Equivalently

$$
X \colon S \to \mathbb R
$$

</div>
</div>

## Notation {#notation}

- Sometimes it is important to emphasize the mapping from sample outcomes to numerical values
- We write $X(s)$ for the value assigned to outcome $s \in S$
- The event $\{X = x\}$ means all sample points whose mapped value is $x$

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="07.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 07.2</span> <span class="theorem-callout-subtitle">(Event Induced by a Random Variable Value)</span>.</div></div>
<div class="callout-content">

For any real number $x$

$$
\{X = x\} = \{s \in S \mid X(s) = x\}
$$

</div>
</div>

## Discrete Random Variables {#discrete-random-variables}

- A discrete random variable is one whose range is countable
- This means its possible values can be listed as a finite or countably infinite sequence

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="07.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 07.3</span> <span class="theorem-callout-subtitle">(Discrete Random Variable)</span>.</div></div>
<div class="callout-content">

$X$ is a discrete random variable if the range of $X$ is a countable set

$$
S_X = \{x_1, x_2, \dots\}
$$

</div>
</div>

- In practice this lets us assign probabilities directly to individual values of $X$
- These point probabilities are the building blocks for probabilities of larger events involving $X$

## Probability Mass Function {#probability-mass-function}

- For a discrete random variable the main object is the probability mass function
- The PMF gives the probability that $X$ takes a specific value
- It is a function defined on values in the range of $X$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="07.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 07.4</span> <span class="theorem-callout-subtitle">(Probability Mass Function)</span>.</div></div>
<div class="callout-content">

The probability mass function of a discrete random variable $X$ is

$$
P_X(x) = P[X = x]
$$

</div>
</div>

- The PMF can be written as a formula
- The PMF can also be displayed as a table of values
- A bar plot is also common when visualizing the probability masses
- These are different representations of the same function

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="07.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 07.5</span> <span class="theorem-callout-subtitle">(Basic Properties of a PMF)</span>.</div></div>
<div class="callout-content">

Let $X$ be a discrete random variable with PMF $P_X(x)$ and range $S_X$

- Nonnegativity

$$
P_X(x) \ge 0 \quad \text{for all } x
$$

- Total mass

$$
\sum_{x \in S_X} P_X(x) = 1
$$

- Probability of an event in the range
For any event $B \subseteq S_X$

$$
P[B] = \sum_{x \in B} P_X(x)
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="07.6">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 07.6</span> <span class="theorem-callout-subtitle">(Probability of a Value Set)</span>.</div></div>
<div class="callout-content">

If $B = \{x_{i_1}, x_{i_2}, \dots\}$ is any subset of $S_X$ then its probability is obtained by summing the corresponding masses

$$
P[X \in B] = \sum_{x \in B} P_X(x)
$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-corollary theorem-callout-en theorem-callout-mathwiki" data-callout="corollary" data-theorem-index="07.7">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Corollary 07.7</span> <span class="theorem-callout-subtitle">(Complement in the Range)</span>.</div></div>
<div class="callout-content">

For any $B \subseteq S_X$

$$
P[X \in B^c] = 1 - P[X \in B]
$$

where $B^c$ is taken relative to $S_X$

</div>
</div>

<div class="callout" data-callout="note">
<div class="callout-title"><div class="callout-icon"><svg class="lucide lucide-pencil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#cicon-pencil"/></svg></div><div class="callout-title-inner">Note</div></div>
<div class="callout-content">

A candidate function is a valid PMF only if it satisfies
- $P_X(x) \ge 0$ for all $x$
- The total sum over the support equals $1$

If an unknown constant appears in a PMF formula then it is determined from

$$
\sum_{x \in S_X} P_X(x) = 1
$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 11–12</span>
