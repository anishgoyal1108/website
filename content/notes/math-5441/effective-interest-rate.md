---
author: "Anish Goyal"
title: "Effective Interest Rate"
description: "The current definition of interest (amount value minus principal) is not good for analyzing profitability"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-08-27T20:40:00
modified: 2025-10-01T12:14:19
readingtime: "8"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 3
weight: 30
slug: "effective-interest-rate"
links: []
sources:
  - "Finan, A Basic Course in the Theory of Interest and Derivatives Markets"
generated: true
---

## EIR {#eir}
- The current definition of interest (amount value minus principal) is not good for analyzing profitability
	- We need a better definition that uses $a(t)$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.1</span> <span class="theorem-callout-subtitle">(Effective Interest Rate)</span>.</div></div>
<div class="callout-content">

The amount that one unit invested at the beginning of a period will earn during the period, with interest paid at the end of the period.

$$i = a(1) - a(0) = a(1) - 1$$

Written in terms of $A(t)$:

$$\frac{A(1)-A(0)}{A(0)} = \frac{I}{A(0)}$$

</div>
</div>

- Alternative definition:
	- The amount of interest gained during a period divided by the principal at the beginning of the period
- For the $n$th time period:
	- Note: $I_n$ is the amount of growth in the period whereas $i_n$ is the rate of growth

$$i_{n} = \frac{A(n)-A(n-1)}{A(n-1)} = \frac{I_{n}}{A(n-1)}$$

- In terms of $a$:

$$i_{n} = \frac{a(n)-a(n-1)}{a(n-1)}$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.2</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 3.1</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;26]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-08-27-20-49-09.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-08-27-20-49-09.svg" alt="03 Effective Interest Rate 2025-08-27 20.49.09" loading="lazy"></a></figure>

</div>
</div>

- The fund at the end of the $n$th period equals the fund at the beginning of the period plus the interest earned during the period

$$A(n) = A(n-1) + i_{n}A(n-1)=(1+i_{n})A(n-1)$$

- This leads to:

$$A(n) = (1 + i_{1})(1+i_{2})\dots(1+i_{n})A(0)$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.3</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 3.2</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;26]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-09-30-26.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-09-30-26.svg" alt="03 Effective Interest Rate 2025-10-01 09.30.26" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.4</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 3.3</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;27]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-09-34-38.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-09-34-38.svg" alt="03 Effective Interest Rate 2025-10-01 09.34.38" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.5</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 3.4</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;27]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-09-42-26.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-09-42-26.svg" alt="03 Effective Interest Rate 2025-10-01 09.42.26" loading="lazy"></a></figure>

</div>
</div>

### Negative Interest Rates {#negative-interest-rates}
- $i$ can be $< 0$ if $a$ is decreasing (which also means $A$ is decreasing)

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.6</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 3.5</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;27]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-09-49-35.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-09-49-35.svg" alt="03 Effective Interest Rate 2025-10-01 09.49.35" loading="lazy"></a></figure>

</div>
</div>

## Practice {#practice}

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.7</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.1</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;29]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-09-51-00.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-09-51-00.svg" alt="03 Effective Interest Rate 2025-10-01 09.51.00" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.8</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.2</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;29]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-10-29.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-10-29.svg" alt="03 Effective Interest Rate 2025-10-01 10.10.29" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.9</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.3</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;29]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-15-33.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-15-33.svg" alt="03 Effective Interest Rate 2025-10-01 10.15.33" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.10</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.4</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;29]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-19-51.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-19-51.svg" alt="03 Effective Interest Rate 2025-10-01 10.19.51" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.11">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.11</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.5</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;29]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-23-31.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-23-31.svg" alt="03 Effective Interest Rate 2025-10-01 10.23.31" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.12">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.12</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.6</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;29]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-25-34.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-25-34.svg" alt="03 Effective Interest Rate 2025-10-01 10.25.34" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.13">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.13</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.7</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;29]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-29-48.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-29-48.svg" alt="03 Effective Interest Rate 2025-10-01 10.29.48" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.14">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.14</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.8</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;29]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-37-12.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-37-12.svg" alt="03 Effective Interest Rate 2025-10-01 10.37.12" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.15">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.15</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.9</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;30]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-44-28.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-44-28.svg" alt="03 Effective Interest Rate 2025-10-01 10.44.28" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.16">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.16</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.10</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;30]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-48-56.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-48-56.svg" alt="03 Effective Interest Rate 2025-10-01 10.48.56" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.17">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.17</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.11</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;30]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-50-43.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-50-43.svg" alt="03 Effective Interest Rate 2025-10-01 10.50.43" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.18">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.18</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.12</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;30]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-52-36.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-10-52-36.svg" alt="03 Effective Interest Rate 2025-10-01 10.52.36" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.19">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.19</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.13</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;30]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-17-55.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-17-55.svg" alt="03 Effective Interest Rate 2025-10-01 11.17.55" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.20">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.20</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.14</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;30]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-25-27.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-25-27.svg" alt="03 Effective Interest Rate 2025-10-01 11.25.27" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.21">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.21</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.15</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;31]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-27-38.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-27-38.svg" alt="03 Effective Interest Rate 2025-10-01 11.27.38" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.22">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.22</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.16</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;31]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-47-06.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-47-06.svg" alt="03 Effective Interest Rate 2025-10-01 11.47.06" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.23">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.23</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.17</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;31]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-49-18.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-49-18.svg" alt="03 Effective Interest Rate 2025-10-01 11.49.18" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.24">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.24</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.18</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;31]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-50-39.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-50-39.svg" alt="03 Effective Interest Rate 2025-10-01 11.50.39" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.25">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.25</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.19</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;31]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-52-39.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-52-39.svg" alt="03 Effective Interest Rate 2025-10-01 11.52.39" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.26">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.26</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.20</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;31]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-54-41.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-54-41.svg" alt="03 Effective Interest Rate 2025-10-01 11.54.41" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.27">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.27</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.21</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;31]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-56-25.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-11-56-25.svg" alt="03 Effective Interest Rate 2025-10-01 11.56.25" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.28">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.28</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 3.22</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;31]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-effective-interest-rate-2025-10-01-12-07-49.svg"><img src="/notes/excalidraw/03-effective-interest-rate-2025-10-01-12-07-49.svg" alt="03 Effective Interest Rate 2025-10-01 12.07.49" loading="lazy"></a></figure>

</div>
</div>
