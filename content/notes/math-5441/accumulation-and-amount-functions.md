---
author: "Anish Goyal"
title: "Accumulation and Amount Functions"
description: "Characterizes the amount value A with time t"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-08-21T00:04:17
modified: 2025-08-27T20:08:57
readingtime: "9"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 2
weight: 20
slug: "accumulation-and-amount-functions"
links: []
sources:
  - "Finan, A Basic Course in the Theory of Interest and Derivatives Markets"
generated: true
---

## Amount Function {#amount-function}
- Characterizes the amount value $A$ with time $t$
- $A(0) = P$

## Accumulation Function {#accumulation-function}
- Characterizes how much the principal has accumulated with time

$$a(t) = \frac{A(t)}{A(0)}$$

- A simple ratio of the amount function and the principal
	- Represents the factor by which the principal has grown
	- This means $A(t)$ is just a constant multiple of $a(t)$; specifically, the proportionality constant is $A(0)=P$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.1</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 2.1</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;15]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-18-33-48.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-18-33-48.svg" alt="02 Accumulation and Amount Functions 2025-08-21 18.33.48" loading="lazy"></a></figure>

</div>
</div>

### Properties {#properties}
1. $a(0) = 1$ by definition
2. Always monotonically increasing
	- Decreasing $a(t)$ implies negative interest
	- $a(t) = C$ for all $t$ implies zero interest
3. May be continuous or discontinuous
	- If $a(t)$ is continuous, then interest accrues for fractional values of $t$
	- If $a(t)$ is discontinuous, then interest does not accrue between payment dates; the function will stay constant between measurement periods and then jump when interest is added as a step function
- Since $A(t)$ is a positive multiple of $a(t)$ and $a(t)$ is increasing, properties 2/3 must hold for $A(t)$ as well

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.2</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 2.2</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;16]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-19-28-35.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-19-28-35.svg" alt="02 Accumulation and Amount Functions 2025-08-21 19.28.35" loading="lazy"></a></figure>

</div>
</div>

## Accumulation Factor {#accumulation-factor}
- Suppose we want to deposit a principal $k$ at a non-zero time $s$
	- Then, the accumulated value of $k$ for any $t > s$ is $k \frac{a(t)}{a(s)}$
	- This ratio is referred to as the **accumulation factor**, and it represents the factor at which the principal grew from time $s$ to $t$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.3</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 2.4</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;17]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-21-31-09.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-21-31-09.svg" alt="02 Accumulation and Amount Functions 2025-08-21 21.31.09" loading="lazy"></a></figure>

</div>
</div>

## Time Intervals {#time-intervals}
- The $n^{\text{th}}$ time period is $\{t\ |\  n-1 \le t \le n\}$
	- The interest earned in this time period is $I_n = A(n) - A(n-1)$
	- "Final amount value minus initial amount value"

$$I_{[s, t]} = A(t) - A(s) = k(a(t)-a(s))$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.4</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 2.5</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;19]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-21-51-53.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-21-51-53.svg" alt="02 Accumulation and Amount Functions 2025-08-21 21.51.53" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.5</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 2.6</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;19]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-21-56-42.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-21-56-42.svg" alt="02 Accumulation and Amount Functions 2025-08-21 21.56.42" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.6</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 2.7</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;19]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-22-04-42.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-22-04-42.svg" alt="02 Accumulation and Amount Functions 2025-08-21 22.04.42" loading="lazy"></a></figure>

</div>
</div>

## Practice {#practice}

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.7</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.1</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;21]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-23-30-02.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-23-30-02.svg" alt="02 Accumulation and Amount Functions 2025-08-21 23.30.02" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.8</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.2</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;21]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-23-36-29.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-23-36-29.svg" alt="02 Accumulation and Amount Functions 2025-08-21 23.36.29" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.9</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.3</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;21]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-23-41-21.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-23-41-21.svg" alt="02 Accumulation and Amount Functions 2025-08-21 23.41.21" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.10</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.4</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;21]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-23-48-25.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-21-23-48-25.svg" alt="02 Accumulation and Amount Functions 2025-08-21 23.48.25" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.11">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.11</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.5</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;21]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-26-17-38-49.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-26-17-38-49.svg" alt="02 Accumulation and Amount Functions 2025-08-26 17.38.49" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.12">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.12</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.6</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;21]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-26-19-27-31.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-26-19-27-31.svg" alt="02 Accumulation and Amount Functions 2025-08-26 19.27.31" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.13">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.13</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.7</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;21]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-26-20-19-51.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-26-20-19-51.svg" alt="02 Accumulation and Amount Functions 2025-08-26 20.19.51" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.14">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.14</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.8</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;22]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-26-20-24-36.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-26-20-24-36.svg" alt="02 Accumulation and Amount Functions 2025-08-26 20.24.36" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.15">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.15</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.9</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;22]</span></cite> and <cite class="cite cite-quote"><q>Problem 2.10</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;22]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-26-21-52-50.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-26-21-52-50.svg" alt="02 Accumulation and Amount Functions 2025-08-26 21.52.50" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.16">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.16</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.11</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;22]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-26-22-10-49.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-26-22-10-49.svg" alt="02 Accumulation and Amount Functions 2025-08-26 22.10.49" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.17">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.17</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.12</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;22]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-26-22-19-04.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-26-22-19-04.svg" alt="02 Accumulation and Amount Functions 2025-08-26 22.19.04" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.18">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.18</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.13</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;22]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-05-48-05.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-05-48-05.svg" alt="02 Accumulation and Amount Functions 2025-08-27 05.48.05" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.19">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.19</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.14</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;23]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-06-25-11.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-06-25-11.svg" alt="02 Accumulation and Amount Functions 2025-08-27 06.25.11" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.20">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.20</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.15</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;23]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-09-31-02.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-09-31-02.svg" alt="02 Accumulation and Amount Functions 2025-08-27 09.31.02" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.21">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.21</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.16</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;23]</span></cite>)
(<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-09-45-46.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-09-45-46.svg" alt="02 Accumulation and Amount Functions 2025-08-27 09.45.46" loading="lazy"></a></figure>)

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.22">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.22</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.17</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;23]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-09-50-36.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-09-50-36.svg" alt="02 Accumulation and Amount Functions 2025-08-27 09.50.36" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.23">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.23</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.18</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;23]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-09-53-59.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-09-53-59.svg" alt="02 Accumulation and Amount Functions 2025-08-27 09.53.59" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.24">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.24</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.19</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;23]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-11-13-14.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-11-13-14.svg" alt="02 Accumulation and Amount Functions 2025-08-27 11.13.14" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.25">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.25</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.20</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;24]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-11-28-58.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-11-28-58.svg" alt="02 Accumulation and Amount Functions 2025-08-27 11.28.58" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.26">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.26</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.21</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;24]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-11-47-02.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-11-47-02.svg" alt="02 Accumulation and Amount Functions 2025-08-27 11.47.02" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.27">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.27</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 2.22</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;24]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-20-08-30.svg"><img src="/notes/excalidraw/02-accumulation-and-amount-functions-2025-08-27-20-08-30.svg" alt="02 Accumulation and Amount Functions 2025-08-27 20.08.30" loading="lazy"></a></figure>

</div>
</div>
