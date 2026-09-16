---
author: "Anish Goyal"
title: "Relative Frequency and Conditional Probability"
description: "Nn(A): number of times event A occurs"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-01-21T09:18:08
modified: 2026-02-10T18:25:07
readingtime: "1"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 2
weight: 20
slug: "relative-frequency-and-conditional-probability"
links: []
sources:
  - "Course lecture slides 3"
generated: true
---

## Relative Frequency Approach {#relative-frequency-approach}

$$f_{A}(n) = \frac{N_{n}(A)}{n}$$

- $N_n(A)$: number of times event $A$ occurs
- $f_A(n)$: relative frequency of $A$ after $n$ repetitions

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="02.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 02.1</span> <span class="theorem-callout-subtitle">(Regularity of Statistics)</span>.</div></div>
<div class="callout-content">

Given unlimited repetitions, the relative frequency of $A$ will approach the true probability of $A$.

$$P[A] = \lim_{ n \to \infty } f_{A}(n) = \lim_{ n \to \infty } \frac{N_{n}(A)}{n}$$  

</div>
</div>

## Conditional Probability {#conditional-probability}
- Reducing the sample space once you have information about an experiment's outcome
- Conditional probability of event $A$ given the occurrence of event $B$:
	- Only defined for $P[B] > 0$
	- $P[A \cap B]$ is the joint probability of $A$ and $B$
	- $P[A|B]$ is the probability that $A$ occurs relative to a sample space of all the outcomes in $B$

$$P[A|B] = \frac{P[A \cap B]}{P[B]} = \frac{P[AB]}{P[B]}$$

- Useful shortcut if $A$ is contained in $B$: Since $A \subset B \implies AB = A$, $P[A | B] = \frac{P[A]}{P[B]}$
	- Example: if $A$ is the bottom of the deck being the ace of clubs and $B$ is the bottom of the deck being black, then $P[A|B] =\frac{P[A]}{P[B]}$ since all ace of clubs are black

## References {#references}
- <span class="cite cite-ref">Course lecture slides 3</span>
