---
author: "Anish Goyal"
title: "Effective Rate of Discount"
description: "Recall the effective rate of interest is equal to the amount of interest if it was just one installment at the end of the period"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-10-06T23:07:02
modified: 2025-10-06T23:39:31
readingtime: "2"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 8
weight: 80
slug: "effective-rate-of-discount"
links: []
sources: []
generated: true
---

## Effective Rate of Discount {#effective-rate-of-discount-1}
- Recall the effective rate of interest is equal to the amount of interest if it was just one installment at the end of the period
- The **effective rate of *discount*** is when the interest is paid at the beginning of the period
	- Useful for loans and treasury bills
- "A loan of $1200 is made for one year at an effective rate of discount of 5%"
	- The borrower pays $1200 \times 0.05 = 60$ (known as the *discount amount*) at the beginning to be able to use the money
	- The borrower pays back the $1200 loan after the year is over
- If $k$ is borrowed at a discount rate of $d$, the discount amount is $kd$ to receive the use of $k$
	- This means the borrower will only have $(k-kd) = k(1-d)$ to use from the loan amount after paying the interest upfront
- Effective rate of discount is therefore:
	- $A(n)$ is the amount at the end of the $n$th period
	- $D$ is the discount amount within the interval, which is just equal to $A(n)-A(n-1)$

$$d = \frac{D}{A(n)} = \frac{A(n)-A(n-1)}{A(n)}$$

## Interest Vs Discount Model {#interest-vs-discount-model}
- Interest model
	- Payment for loan is made at the end of the interest period
	- The borrower can make full use of the loan amount
	- The effective rate is calculated based on the initial balance
- Discount model
	- Payment for loan is upfront
	- Borrower can make use of $k(1-d)$ of the loan
	- Effective rate calculated from final balance

## Relationship Between Effective Rates {#relationship-between-effective-rates}

$$i = \frac{d}{1-d}$$ and $$d = \frac{i}{1+i}$$

- We can use this relationship to derive the following:

$$d = 1-\nu$$ and $$(1+i)(1-d) = 1$$ and $$i-d=id$$

## Compound Discount Function {#compound-discount-function}

$$A(t)(1-d)^{t} = A_{0}$$

- Theorem: $d_{n} = d$ for all $n \ge 1$

## Simple Discount Function {#simple-discount-function}

$$A(t)(1-dt) = A_{0}$$

- Theorem: $d_n$ is increasing until $t = \frac{1}{d}$ 

## Growth of Simple and Compound Discount Functions {#growth-of-simple-and-compound-discount-functions}
- $(1-d)^t < 1 - dt, t \in (0, 1)$
- $(1-d)^t = 1-dt, t \in \{0, 1\}$
- $(1-d)^t > 1-dt, t > 1$
