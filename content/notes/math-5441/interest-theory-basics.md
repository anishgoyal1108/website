---
author: "Anish Goyal"
title: "Interest Theory Basics"
description: "Interest problems typically involve four quantities:"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-08-20T21:33:53
modified: 2025-08-21T00:10:33
readingtime: "6"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 1
weight: 10
slug: "interest-theory-basics"
links: []
sources:
  - "Finan, A Basic Course in the Theory of Interest and Derivatives Markets"
generated: true
---

## Meaning of Interest {#meaning-of-interest}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.1</span> <span class="theorem-callout-subtitle">(Interest)</span>.</div></div>
<div class="callout-content">

**Interest** is an amount charged to a borrower for the use of the lender's money over a time period.
- The lender's monetary investment is increasing with time due to interest being added
	- This is why interest is also commonly referred to as the *time value of money*

</div>
</div>

- Interest problems typically involve four quantities:
	- The initial investment is the **principal** $(P)$
	- The final amount is the **amount value** $(A)$
	- The **interest gained** during the period of investment is $I = A-P$
	- The **interest rate** is interest expressed as a *percentage* of the principal
		- May be calculated using the percent change formula: $\frac{FV-IV}{IV} \cdot 100\%$
- Interest takes into account the risk of default (when the borrower cannot pay back the loan)
	- Risk may be reduced if the borrower promises to release one of their assets in the event of their default called **collateral**
- The unit with which the time of investment is measured is called the **measurement period**
- The **present value** is the principal that must be invested to obtain a future amount value at a specified time

## Types of Interest {#types-of-interest}

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

## Practice {#practice}

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.4</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 1.1</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;12]</span></cite>)

$$\frac{3294.08-3200}{3200} \cdot 100\% = 2.94\%$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.5</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 1.2</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;12]</span></cite>)
a. $12780-12000 = \$780$
b. $$\frac{12780-12000}{12000} \cdot 100\% = 6.5\%$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.6</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 1.3</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;12]</span></cite>)
$1000 \cdot 1.09 = \$1090$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.7</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 1.4</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;12]</span></cite>)
$A(t) = 1 + 0.01t$ (in dollars)

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.8</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 1.5</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;12]</span></cite>)

$$\frac{\frac{615}{500}-1}{2.5} \cdot 100\%=9.2\% \text{  annually}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.9</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 1.6</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;12]</span></cite>)

$$\frac{\frac{630}{500}-1}{\frac{7.8\%}{100\%}}=3.33 \text{ years}$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.10</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 1.7</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;12]</span></cite>)

$$10000\left(1 + \frac{5\%}{100\%} \right)^3 =\$ 11576.25$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.11">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.11</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 1.8</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;13]</span></cite>)
$\$4971.7673529829$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.12">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.12</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 1.9</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;13]</span></cite>)
$6.961037572506901\%$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.13">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.13</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 1.10</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;13]</span></cite>)
$55.4781076387804 \text{ years}$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.14">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.14</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 1.11</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;13]</span></cite>)
Reject the offer, since $\$22500 < A(1, 10) = \$25937.424601$.

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.15">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.15</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 1.12</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;13]</span></cite>)

$$P\prod_{k=1}^{n}(1+i_{k})$$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.16">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.16</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 1.13</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;13]</span></cite>)
$\$56.7426855718599$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.17">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.17</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 1.14</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;14]</span></cite>)
a. $\$1004.006004001$
b. $\$4.00600400099995$
c. $0.4006\%$

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.18">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.18</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Problem 1.15</q> <span class="cite-src">[Finan, <em>A Basic Course in the Theory of Interest and Derivatives Markets</em>, p.&nbsp;14]</span></cite>)
$\$100$

</div>
</div>
