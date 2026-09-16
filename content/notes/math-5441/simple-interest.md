---
author: "Anish Goyal"
title: "Simple Interest"
description: "Already covered in 01 Interest Theory Basics"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-10-01T12:13:48
modified: 2025-10-06T13:04:30
readingtime: "4"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 4
weight: 40
slug: "simple-interest"
links:
  - "/notes/math-5441/accumulation-and-amount-functions/"
  - "/notes/math-5441/interest-theory-basics/"
sources:
  - "Finan, A Basic Course in the Theory of Interest and Derivatives Markets"
generated: true
---

## Simple Interest {#simple-interest-1}
- Already covered in

  <div class="transclusion" data-source="04. Notes/Undergraduate Courses/MATH 5441/01 Interest Theory Basics.md">
  <a class="transclusion-source" href="/notes/math-5441/interest-theory-basics/#types-of-interest" title="Open Interest Theory Basics › Types of Interest"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  ## Types of Interest {#types-of-interest-embed1}

  <div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.2">
  <div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.2</span> <span class="theorem-callout-subtitle">(Simple Interest)</span>.</div></div>
  <div class="callout-content">

  **Simple interest** occurs when interest is only calculated using the *original* principal; that is, interest earned from prior periods is not required for interest calculations for consecutive periods. 
  - It is characterized by $P$, the interest rate per measurement period $(i)$ and number of measurement periods $(t)$
  - The amount value is linear in $t$

  $$A(t)=P \cdot(1+it)$$

  </div>
  </div>

  <div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.3">
  <div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.3</span> <span class="theorem-callout-subtitle">(Compound Interest)</span>.</div></div>
  <div class="callout-content">

  **Compound interest** occurs when interest is accumulated on the principal in discrete subintervals of the measurement period. 
  - It is characterized by $P$, the nominal interest rate $(r)$, the number of subdivisions for a single measurement period $(n)$, and the number of measurement periods $(t)$
  - The amount value is exponential in $t$ (assuming $n > 1$)

  The *accumulated amount* for one measurement period is:

  $$
  A(n) = P\left(1+\frac{r}{n}\right)^n.
  $$

  For multiple periods:

  $$
  A(n, t) = P\left(1+\frac{r}{n}\right)^{nt}.
  $$

  The *effective interest rate (ER)* for one measurement period is

  $$
  ER(n) = \left[ \left(1+\frac{r}{n}\right)^n - 1 \right] \cdot 100\%. 
  $$

  For multiple periods:

  $$
  ER(n,t) = \left[\left(1+\frac{r}{n}\right)^{nt} - 1\right] \cdot 100\%.
  $$

  Example: If $r=0.10$ is compounded semi-annually ($n=2$), then after one year ($t=1$):

  $$
  A(2, 1) = P\left(1+\frac{0.10}{2}\right)^2 = 1.1025P,
  $$

  so:

  $$
  ER(2,1) = 1.1025 - 1 = 0.1025 = 10.25\%.
  $$

  </div>
  </div>

  </div>

- The effective interest rate $a(1) - 1$ is sometimes called the *simple interest rate*
	- The effective interest rate is decreasing in each consecutive period and converges to zero
- $n$th effective interest rate

$$i_{n} = \frac{i}{1+i(n-1)}$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.1</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 4.1</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;32]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-simple-interest-2025-10-01-12-45-47.svg"><img src="/notes/excalidraw/04-simple-interest-2025-10-01-12-45-47.svg" alt="04 Simple Interest 2025-10-01 12.45.47" loading="lazy"></a></figure>

</div>
</div>

## Absolute Interest Earned {#absolute-interest-earned}
- Absolute interest, $I_n=A(n)-A(n-1)$, is constant since the accumulation function is linear

## $\mathbb{R}^+$ Extension of Simple Interest {#r-extension-of-simple-interest}
- So far, we have treated simple interest as discrete unit steps, but we can make it integrable
- We can extend this definition to all positive real numbers
	- The interest earned for any time period $t+s$ is the sum of the interests earned in $t$ and $s$ (assuming a principal of $1)
	- Therefore, the simple interest equation holds for any nonnegative real number

$$a(t+s) = a(t) + a(s) - a(0)$$

- Simple interest is the only accumulation function in which the above property holds

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.2</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 4.2</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;34]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-simple-interest-2025-10-01-12-58-38.svg"><img src="/notes/excalidraw/04-simple-interest-2025-10-01-12-58-38.svg" alt="04 Simple Interest 2025-10-01 12.58.38" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.3</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 4.3</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;34]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-simple-interest-2025-10-01-13-05-52.svg"><img src="/notes/excalidraw/04-simple-interest-2025-10-01-13-05-52.svg" alt="04 Simple Interest 2025-10-01 13.05.52" loading="lazy"></a></figure>

</div>
</div>

## Approximating Compound Interest {#approximating-compound-interest}
- For $t \in [0, 1]$, simple interest is approximately equal to compound interest

$$(1+i)^t \approx 1+it$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="04.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 04.4</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 4.4</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;35]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/04-simple-interest-2025-10-01-13-09-24.svg"><img src="/notes/excalidraw/04-simple-interest-2025-10-01-13-09-24.svg" alt="04 Simple Interest 2025-10-01 13.09.24" loading="lazy"></a></figure>

</div>
</div>

- Need to use <a class="internal-link" href="/notes/math-5441/accumulation-and-amount-functions/#accumulation-factor">Accumulation Factor</a> formula if there is a deposit/withdrawal midway and add that on (<cite class="cite cite-quote"><q>Example 4.5</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;36]</span></cite>)

## Practice {#practice}
