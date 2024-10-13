---
author: "Anish Goyal"
title: "Breaking Down the Inequality"
description: "A challenging inequality proposed is proven by induction."
summary: "An in-depth exploration of a challenging inequality proposed by Sela Fried, tackled through induction. We break down the problem step by step, revealing how powers of $x$ interact with $(1−x)$ over a specific interval."
eyeCatcher: "Can you prove that the inequality holds $\\forall n \\ge 2$ if $x \\in \\left[\\frac{3}{5}, 1 \\right]$ and $n \\in \\mathbb{N}$?"
tags: [math, induction, proof, problem-solving, inequality]
readingtime: "8"
date: 2024-10-08
modified: 2024-10-13
---

## The Problem
*From VOL. 55, NO. 22, MARCH 2024 edition of **THE COLLEGE MATHEMATICS JOURNAL:***
> Let  $n \ge 2$ be an integer and let $x \in \left[\frac{3}{5}, 1 \right]$. Prove that $x^n \ge (1-x)^n + x^{2n}$. <br>
> --- Sela Fried, Israel Academic College, Ramat Gan, Israel

## Classifying the Problem
When I first read this problem, I instantly recognized that the solution would involve *mathematical induction.* 

This is clear because we are working with powers of $n$, a strong indicator that induction could be useful. Additionally, problems involving sequences or expressions that evolve as $n$ increases often lend themselves well to this technique.

Induction is a powerful tool for these problems because it allows us to first verify the base case (often a small starting value of $n$, such as $n = 2$ or $n = 1$) and then build from there by assuming the result generally holds for $n$ and proving it for $n + 1$.

## Simplifying the Inequality
The first thing I did to tackle this problem was to rearrange the inequality. I moved $x^n$ to the right-hand side of the inequality, which gave me a more structured form that was easier to work with:

$$ p_n(x) = x^{2n} - x^n + (1 - x)^n $$

Now we can focus on proving that $p_n(x) \leq 0 \ \forall \ x \in \left[\frac{3}{5}, 1\right]$ if $n \ge 2$ via induction. 

## The Base Case
We start by verifying the base case $n = 2$:

$$ 
\begin{align*}
p_2(x) &= x^4 - x^2 + (1 - x)^2 && \text{Plugging $n=2$ into $p_n(x)$} \\
p_2(x) &= x^4 - x^2 + 1 - 2x + x^2 && \text{Expanding the binomial} \\
p_2(x) &= x^4 - 2x + 1 && \text{Rearranging the expression}
\end{align*}
$$

We must prove that $p_2(x)$ holds $\forall \ x \in \left[\frac{3}{5}, 1 \right]$.

### The First Derivative Test
To prove that $p_2(x) \le 0$ on the interval, an unlikely contender arises: *the first derivative test*. The idea is to identify critical points of the function and analyze its behavior in the interval.

Let's find the critical points of $p_{2}(x)$ by finding the roots of $p_{2}'(x) = 4x^3 - 2$:

$$ 
\begin{align*}
4x^3 -2 &= 0 \\
4x^3 &= 2 \\
x^3 &= \frac{1}{2} \\
x &= \sqrt[3]{\frac{1}{2}} \approx 0.7937
\end{align*}
$$

Since $\frac{3}{5} \le \sqrt[3]{\frac{1}{2}} \le 1$, we have a critical point in our interval of interest. If there had been no critical points in the interval, we would only need to check the endpoints. However, since we *do* have a critical point in the interval, we need to use *the second derivative test* to determine whether $p_2\left(\sqrt[3]{\frac{1}{2}}\right)$ is a relative maximum or minimum.

### The Second Derivative Test
Let's evaluate $p_{2}''(x) = 12x^2$ at $x = \sqrt[3]{\frac{1}{2}}$:

$$ p_{2}''\left( \sqrt[3]{\frac{1}{2}} \right) = 12 \left( \sqrt[3]{\frac{1}{2}} \right)^2 $$

Since $p_{2}''(x) > 0$ for all $x \in \left[\frac{3}{5}, 1\right]$, the function $p_{2}(x) = x^4 - 2x + 1$ is **concave up** throughout the interval, meaning $p_{2}\left(\sqrt[3]{\frac{1}{2}}\right)$ is a **local minimum**. 

Unfortunately, just showing that $p_2(x)$ is concave up is not enough to prove that the inequality holds. However, since $p_2(x)$ is concave up, it follows that $p_{2}(x)$ is decreasing on $\left(\frac{3}{5}, \sqrt[3]{\frac{1}{2}}\right)$ and increasing on $\left(\sqrt[3]{\frac{1}{2}}, 1\right)$.

To finish proving the base case, we must show that $0 \ge \{p\left(\frac{3}{5}\right),p(1)\}$. In other words, we have to ensure that both endpoints are negative or zero.

### Evaluating the Endpoints
So, let's evaluate $p_{2}(x)$ at the endpoints of the interval $x = \frac{3}{5}$ and $x = 1$: 

At $x = \frac{3}{5}$:

$$
\begin{align}
p_{2}\left( \frac{3}{5} \right) &= \left( \frac{3}{5} \right)^4 - 2\left(\frac{3}{5}\right) + 1 \\
&= \frac{81}{625} - \frac{6}{5} + 1 \\
&= -\frac{44}{625}
\end{align}
$$ 

At $x = 1$:

$$ p_{2}(1) = 1^4 - 2(1) + 1 = 0 $$

Thus, since $p_{2}(x) \le 0$ at the endpoints and is concave up throughout the interval, we conclude that $p_{2}(x) \le 0 \ \forall \ x \in \left[\frac{3}{5}, 1\right]$, and the base case $n = 2$ holds. 

## Inductive Hypothesis
Let's begin our induction by assuming that the inequality is true for some $k \geq 2$ and substitute $k$ into $n$:

$$ p_k(x) = x^{2k} - x^k + (1 - x)^k \leq 0 $$

The above expression is our **inductive hypothesis**.

We aim to show that it remains true for $n = k + 1$, which simplifies to:

$$
\begin{align*}
p_{k+1}(x) &= x^{2(k+1)} - x^{k+1} + (1 - x)^{k+1} \leq 0 \\
&= x^{2k+2} - x^{k+1} + (1-x)^{k+1}
\end{align*}
$$

## Inductive Step
 In the inductive step, we have to prove that $p_{k+1}(x)$ must hold if $p_k(x)$ holds, assuming $x \in \left[\frac{3}{5}, 1\right]$ and $k \in \mathbb{N}$.

For the inductive step to work, we need to show that the function $p_n(x)$ is **monotonically decreasing**---that is, either continually decreasing or remaining constant $\forall \ x \in \left[ \frac{3}{5}, 1\right]$. If we can show that $p_k(x) \ge p_{k+1}(x)$, then $p_n(x)$ *must* decrease or stay the same with increasing $n$, ensuring that the inequality holds.

### Setting Up the Inductive Step
We begin the inductive step by multiplying $p_k(x)$ by $x$ to obtain $x \cdot p_k(x)$.

From the inductive hypothesis, we know that:

$$
p_{k}(x) = x^{2k} - x^k + (1-x)^k \le 0
$$

Multiplying the entire expression by $x$ gives us:

$$
\begin{align*}
x \cdot p_k(x) &= x \left(x^{2k} - x^k + (1 - x)^k \right) \\
&= x^{2k+1} - x^{k+1} + x(1 - x)^k
\end{align*}
$$

...which we will use to compare $p_{k+1}(x)$ and $p_k(x)$.

### Simplifying the Inductive Step
Recall that we want to show that $p_{k+1}(x) \le p_k(x)$. We will instead show that $p_{k+1}(x) \le x \cdot p_k(x)$, and if the new inequality holds, then the original must also be true because $x$ is a constant multiple that decreases the value of $p_k(x)$ (except at $x=1$ where $p_k(x)$ stays the same). 

In other words, if we can prove $p_{k+1}(x) \le x \cdot p_k(x)$, then the inequality $p_{k+1}(x) \le p_k(x)$ will naturally follow, since multiplying $p_k(x)$ by $x$ will always yield a smaller or equal value.

It may not be immediately obvious why I multiplied $p_k(x)$ by $x$, so consider the following:

$$
\begin{align*}
p_{k+1}(x) &\le x \cdot p_{k}(x) \\
x^{2k+2} - x^{k+1} + (1-x)^{k+1} &\le x^{2k+1} - x^{k+1} + x(1 - x)^k \\
x^{2k+2}+(1-x)^{k+1} &\le x^{2k+1} + x(1-x)^k
\end{align*}
            $$

From the above expressions, we can see that the term $-x^{k+1}$ cancels on both sides.

Therefore, it suffices to show that:

$$(1 - x)^{k+1} + x^{2k+2} \le x(1 - x)^k + x^{2k+1}$$

We can show that the above inequality is true by grouping each term on the left-hand side with a corresponding term on the right-hand side. If we show that all groupings are valid, the inequality must also be true. This inequality can be broken down into two parts:

1.  $(1 - x)^{k+1} \le x(1 - x)^k$
2. $x^{2k+2} \le x^{2k+1}$

For the groupings, I chose pairs of terms that looked related on both sides. This makes them easier to compare.

### First Part

To show that $(1 - x)^{k+1} \le x(1 - x)^k$, we divide both sides by $(1 - x)^k$, leading to:

$$
\begin{align*}
1-x &\le x \\
1 &\le 2x \\
\frac{1}{2} &\le x
\end{align*}
$$

This inequality is true $\forall \ x \in \left[\frac{3}{5}, 1\right]$, so the first part holds.

### Second Part

For the second part, $x^{2k+2} \le x^{2k+1}$, we divide both sides by $x^{2k+1}$, which leads to:

$$ x \le 1 $$

This is clearly true $\forall \ x \in \left[\frac{3}{5}, 1\right]$, so the second part also holds.

Since both parts of the inequality are satisfied, so $p_{k}(x) \ge p_{k+1}(x) \ \forall \ x \in \left[\frac{3}{5}, 1\right]$ **by induction!**

## `<EOF>`

The only prerequisites for solving this problem were:
1. Proof by induction
2. Basic Calculus I techniques 

This means that an undergraduate student familiar with proofs and taking an introductory calculus course probably have probably could have solved this problem if they thought about it enough. Pretty inspiring, eh?