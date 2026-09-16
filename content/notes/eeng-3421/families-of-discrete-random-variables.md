---
author: "Anish Goyal"
title: "Families of Discrete Random Variables"
description: "Certain families of random variables make multiple appearances in experiments"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-02-25T09:13:41
modified: 2026-04-03T13:33:08
readingtime: "9"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 8
weight: 80
slug: "families-of-discrete-random-variables"
links: []
sources:
  - "Course lecture slides 11–12"
  - "Course lecture slides 13–14"
generated: true
---

## Families of Random Variables {#families-of-random-variables}
- Certain families of random variables make multiple appearances in experiments
- The PMF has the same mathematical form, but has a different shape or number of parameters

## Bernoulli $(p)$ Random Variable {#bernoulli-p-random-variable}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="08.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 08.1</span> <span class="theorem-callout-subtitle">(Bernoulli $(p)$ Random Variable)</span>.</div></div>
<div class="callout-content">

$X$ is a Bernoulli $(p)$ random variable if the PMF of $X$ has the form

$$P_X(x) = \begin{cases} 1-p & x = 0 \\ p & x = 1 \\ 0 & \text{otherwise} \end{cases}$$

where $0 < p < 1$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.2</span> <span class="theorem-callout-subtitle">(Circuit Rejection)</span>.</div></div>
<div class="callout-content">

Test one circuit and observe $X$, the number of rejects. Since there are only two outcomes, $X = 1$ with probability $p$ and $X = 0$ with probability $1-p$, so the number of rejects is a Bernoulli $(p)$ random variable

</div>
</div>

## Binomial $(n, p)$ Random Variable {#binomial-n-p-random-variable}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="08.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 08.3</span> <span class="theorem-callout-subtitle">(Binomial $(n, p)$ Random Variable)</span>.</div></div>
<div class="callout-content">

$X$ is a binomial $(n, p)$ random variable if the PMF of $X$ has the form

$$P_X(x) = \binom{n}{x} p^x (1-p)^{n-x}$$

where $0 < p < 1$ and $n$ is an integer such that $n \ge 1$

</div>
</div>

- Counts the number of successes in $n$ independent Bernoulli trials
- Bernoulli $(p)$ is the special case Binomial $(1, p)$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.4</span> <span class="theorem-callout-subtitle">(Circuit Rejection ($n$ Tests))</span>.</div></div>
<div class="callout-content">

In $n$ independent tests each rejected with probability $p$, let $K$ equal the number of rejects. Then $K$ is Binomial $(n, p)$ with

$$P_K(k) = \binom{n}{k} p^k (1-p)^{n-k}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.5</span> <span class="theorem-callout-subtitle">(Multiple Choice Exam)</span>.</div></div>
<div class="callout-content">

A 10-question exam has four choices per question. A student guesses every answer. Let $X$ be the number of correct answers, then $X$ is Binomial with $n = 10$, $p = 0.25$

$$P_X(2) = \binom{10}{2}(0.25)^2(0.75)^8 = 0.281$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.6</span> <span class="theorem-callout-subtitle">(Defective Components)</span>.</div></div>
<div class="callout-content">

Components are defective with probability $0.001$ independently. Let $X$ be the number of defective components in $n$ produced. Then:

$$P[\text{at least one defective}] = 1 - P[X=0] = 1 - (0.999)^n$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.7</span> <span class="theorem-callout-subtitle">(Light Bulbs)</span>.</div></div>
<div class="callout-content">

20 bulbs each function more than three months with probability $0.2$. Let $X$ be the number that function. Then $X$ is Binomial with $n = 20$, $p = 0.2$

$$P[X \ge 5] = 1 - \sum_{x=0,1,2,3,4} \binom{20}{x} (0.2)^x (0.8)^{20-x} = 1 - (0.0115 + 0.0576 + 0.137 + 0.205 + 0.218) = 0.37$$

</div>
</div>

## Geometric $(p)$ Random Variable {#geometric-p-random-variable}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="08.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 08.8</span> <span class="theorem-callout-subtitle">(Geometric $(p)$ Random Variable)</span>.</div></div>
<div class="callout-content">

$X$ is a geometric $(p)$ random variable if the PMF of $X$ has the form

$$P_X(x) = \begin{cases} p(1-p)^{x-1} & x = 1, 2, \dots \\ 0 & \text{otherwise} \end{cases}$$

where $0 < p < 1$

</div>
</div>

- Counts the number of trials until the first success
- PMF forms a geometric series, hence the name

<div class="callout theorem-callout theorem-callout-proposition theorem-callout-en theorem-callout-mathwiki" data-callout="proposition" data-theorem-index="08.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-calculator"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Proposition 08.9</span> <span class="theorem-callout-subtitle">(Tail Probability)</span>.</div></div>
<div class="callout-content">

$$P[X > k] = (1-p)^k$$

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>

$$P[X > k] = 1 - P[X \le k] = 1 - \sum_{x=1}^{k} p(1-p)^{x-1} = 1 - p \cdot \frac{1-(1-p)^k}{1-(1-p)} = (1-p)^k$$

<span class="math-booster-end-proof"></span>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.10</span> <span class="theorem-callout-subtitle">(Parking Space)</span>.</div></div>
<div class="callout-content">

Five cars ahead each take a space with probability $0.2$. Let $X$ be the number of trials to fill the space, then $X$ is Geometric with $p = 0.2$

$$P_X(5) = (0.8)^4(0.2) = 0.082$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.11">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.11</span> <span class="theorem-callout-subtitle">(Paging System (Problem 3.3.7))</span>.</div></div>
<div class="callout-content">

A two-way paging system retransmits until an ACK is received. Each attempt succeeds with probability $p$

**(a)** $N$ is the number of times the message is sent. Since $N = n$ requires $n-1$ failures then a success, $N$ is Geometric:

$$P_N(n) = \begin{cases}(1-p)^{n-1}p & n = 1, 2, \dots \\ 0 & \text{otherwise}\end{cases}$$

**(b)** The goal $P[N \le 3] \ge 0.95$ requires:

$$P[N \le 3] = 1 - P[N > 3] = 1 - (1-p)^3 \ge 0.95$$

$$(1-p)^3 \le 0.05 \implies p \ge 1 - (0.05)^{1/3} \approx 0.6316$$

</div>
</div>

## Pascal $(k, p)$ Random Variable {#pascal-k-p-random-variable}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="08.12">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 08.12</span> <span class="theorem-callout-subtitle">(Pascal $(k, p)$ Random Variable)</span>.</div></div>
<div class="callout-content">

$X$ is a Pascal $(k, p)$ random variable if the PMF of $X$ has the form

$$P_X(x) = \binom{x-1}{k-1} p^k (1-p)^{x-k}$$

where $0 < p < 1$ and $k$ is an integer such that $k \ge 1$

</div>
</div>

- Counts the number of trials until the $k$th success
- Geometric $(p)$ is the special case Pascal $(1, p)$
- Derivation: $X = l$ iff there are $k-1$ successes in the first $l-1$ trials AND a success on trial $l$, and these events are independent, so:

$$P_X(l) = \underbrace{\binom{l-1}{k-1}p^{k-1}(1-p)^{l-k}}_{\text{binomial: }k-1\text{ successes in }l-1\text{ trials}} \cdot \underbrace{p}_{\text{success on trial }l}$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.13">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.13</span> <span class="theorem-callout-subtitle">(Coin Flips Until Four Heads)</span>.</div></div>
<div class="callout-content">

A fair coin is tossed until heads appears four times. Let $X$ be the number of flips, then $X$ is Pascal $(4, 0.5)$

$$P[X = 10] = \binom{9}{3}(0.5)^4(0.5)^6 = 0.082$$

</div>
</div>

## Poisson $(\alpha)$ Random Variable {#poisson-random-variable}
- Models the number of occurrences of an event in a fixed time or space interval
	- The parameter $\alpha$ represents the average or expected number of occurrences
	- Often written as:
		- $\lambda$ is the average rate of occurrences of the event
		- $T$ is the length of the time or space interval

$$\alpha = \lambda T$$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="08.14">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 08.14</span> <span class="theorem-callout-subtitle">(Poisson $(\alpha)$ Random Variable)</span>.</div></div>
<div class="callout-content">

$X$ is a Poisson $(\alpha)$ random variable if the PMF of $X$ has the form

$$P_X(x) = \begin{cases} \dfrac{\alpha^x e^{-\alpha}}{x!} & x = 0,1,2,\dots \ 0 & \text{otherwise} \end{cases}$$

where the parameter $\alpha$ is such that $\alpha > 0$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.15">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.15</span> <span class="theorem-callout-subtitle">(Website Hits)</span>.</div></div>
<div class="callout-content">

The number of hits at a website in a time interval is a Poisson random variable. Suppose a site receives on average $\lambda = 2$ hits per second.

In an interval of $T = 0.25$ seconds,

$$\alpha = \lambda T = (2)(0.25) = 0.5$$

Let $H$ be the number of hits in $0.25$ seconds. Then

$$P_H(h) = \frac{(0.5)^h e^{-0.5}}{h!}, \quad h = 0,1,2,\dots$$

The probability of no hits is

$$P[H=0] = \frac{(0.5)^0 e^{-0.5}}{0!} = e^{-0.5} = 0.607$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.16">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.16</span> <span class="theorem-callout-subtitle">(Website Hits in One Second)</span>.</div></div>
<div class="callout-content">

If the same website receives $\lambda = 2$ hits per second, let $J$ be the number of hits in one second. Then

$$\alpha = \lambda T = (2)(1) = 2$$

$$P_J(j) = \frac{2^j e^{-2}}{j!}, \quad j = 0,1,2,\dots$$

The probability of no more than two hits is

$$P[J \le 2] = P[J=0] + P[J=1] + P[J=2]$$

$$= e^{-2} + 2e^{-2} + \frac{2^2}{2!}e^{-2} = 0.677$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.17">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.17</span> <span class="theorem-callout-subtitle">(Database Queries)</span>.</div></div>
<div class="callout-content">

The number of database queries processed in a 10-second interval is Poisson with $\alpha = 5$. Let $K$ be the number of queries.

$$P_K(k) = \frac{5^k e^{-5}}{k!}, \quad k = 0,1,2,\dots$$

The probability of no queries in 10 seconds is

$$P[K=0] = e^{-5} = 0.0067$$

The average rate is

$$\lambda = \frac{\alpha}{T} = \frac{5}{10} = 0.5 \text{ queries/sec}$$

In a 2-second interval

$$\alpha = \lambda T = (0.5)(2) = 1$$

Let $N$ be the number of queries in 2 seconds:

$$P_N(n) = \frac{1^n e^{-1}}{n!}, \quad n = 0,1,2,\dots$$

The probability of at least two queries is

$$P[N \ge 2] = 1 - P[N=0] - P[N=1]$$

$$= 1 - e^{-1} - e^{-1} = 0.264$$

</div>
</div>

## Discrete Uniform $(k,l)$ Random Variable {#discrete-uniform-k-l-random-variable}
- All outcomes in the range ${k,k+1,\dots,l}$ are equally likely

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="08.18">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 08.18</span> <span class="theorem-callout-subtitle">(Discrete Uniform $(k,l)$ Random Variable)</span>.</div></div>
<div class="callout-content">

$X$ is a discrete uniform $(k,l)$ random variable if the PMF of $X$ has the form

$$P_X(x) = \begin{cases} \dfrac{1}{l-k+1} & x = k, k+1, k+2, \dots, l \\
0 & \text{otherwise} \end{cases}$$

where the parameters $k$ and $l$ are integers such that $k < l$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.19">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.19</span> <span class="theorem-callout-subtitle">(Roll of a Fair Die)</span>.</div></div>
<div class="callout-content">

Roll a fair die. Let $N$ be the number on the face that appears.
Then $N$ is a discrete uniform $(1,6)$ random variable.

$$P_N(n) = \begin{cases} \frac{1}{6} & n = 1,2,3,4,5,6 \\
0 & \text{otherwise} \end{cases}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="08.20">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 08.20</span> <span class="theorem-callout-subtitle">(Number of Yellow M&Ms)</span>.</div></div>
<div class="callout-content">

In a package of M&Ms, let $Y$ be the number of yellow M&Ms, uniformly distributed between 5 and 15.

The PMF is

$$P_Y(y) = \begin{cases} \frac{1}{11} & y = 5,6,7,\dots,15 \\
0 & \text{otherwise} \end{cases}$$

(a) Probability that $Y < 10$:

$$P[Y < 10] = P_Y(5)+P_Y(6)+P_Y(7)+P_Y(8)+P_Y(9) = \frac{5}{11}$$

(b) Probability that $Y > 12$:

$$P[Y > 12] = P_Y(13)+P_Y(14)+P_Y(15) = \frac{3}{11}$$

(c) Probability that $8 \le Y \le 12$:

$$P[8 \le Y \le 12] = P_Y(8)+P_Y(9)+P_Y(10)+P_Y(11)+P_Y(12) = \frac{5}{11}$$

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course lecture slides 11–12</span>
- <span class="cite cite-ref">Course lecture slides 13–14</span>
