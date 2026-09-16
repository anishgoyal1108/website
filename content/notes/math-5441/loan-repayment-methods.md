---
author: "Anish Goyal"
title: "Loan Repayment Methods"
description: "Two ways to repay a loan:"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-12-06T07:13:38
modified: 2025-12-06T14:33:27
readingtime: "2"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 37
weight: 370
slug: "loan-repayment-methods"
links: []
sources: []
generated: true
---

## Concept {#concept}
- Two ways to repay a loan:
	- Amortization
		- Taking the payment and splitting it up into parts---some goes towards the principal and part goes towards the interest
		- Always pay off the interest first and whatever is left over pays the principal
	- Sinking fund
		- Only the interest is paid off until the balance can be paid as a lump-sum
		- You would have to assume there's some balance in another account that's growing in order to pay off the balance on the loan

## Amortization {#amortization}

### Prospective Method {#prospective-method}
- The outstanding balance at $t=0$ is the present values of the remaining payments
- The loan amount is just the PV of all the payments 

### Retrospective Method {#retrospective-method}
- The outstanding balance at some non-zero $t$ is the accumulated loan amount (including interest) minus the accumulated value of all previous payments

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/37-loan-repayment-methods-2025-12-06-07-51-50.svg"><img src="/notes/excalidraw/37-loan-repayment-methods-2025-12-06-07-51-50.svg" alt="37 Loan Repayment Methods 2025-12-06 07.51.50" loading="lazy"></a></figure>

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/37-loan-repayment-methods-2025-12-06-08-53-53.svg"><img src="/notes/excalidraw/37-loan-repayment-methods-2025-12-06-08-53-53.svg" alt="37 Loan Repayment Methods 2025-12-06 08.53.53" loading="lazy"></a></figure>

## Amortization Schedules {#amortization-schedules}
- Splits up recurring payments into interest and principal
	- You will *always* have to pay off the interest, and then the rest goes towards the principal
- Create a table with the time value, payment, interest paid, principal paid, and outstanding balance
- Outstanding Balance for each payment:

$$OB_{t=k} = Pa_{\left< n - k \right> }$$

- Interest Paid for each payment:

$$I_{P_{t=k}} = i \cdot OB_{t=k-1}$$

- Principal Paid for each payment:
	- Basically whatever is left from the payment when you subtract the interest

$$A_{P_{t=k}} = P - I_{P_{t=k}}$$

- TOTALS at $t=n$:
	- $OB = 0$
	- $I_{P, \text{total}} =Pn - A_{P, \text{total}} = Pn - Pa_{\left< n \right>}$
	- $A_{P, \text{total}} =Pa_{\left< n \right>}$

<a class="zoom" href="/notes/img/amortization-schedule-example.png"><img src="/notes/img/amortization-schedule-example.png" alt="amortization schedule example" loading="lazy"></a>

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/37-loan-repayment-methods-2025-12-06-10-09-08.svg"><img src="/notes/excalidraw/37-loan-repayment-methods-2025-12-06-10-09-08.svg" alt="37 Loan Repayment Methods 2025-12-06 10.09.08" loading="lazy"></a></figure>

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/37-loan-repayment-methods-2025-12-06-11-36-32.svg"><img src="/notes/excalidraw/37-loan-repayment-methods-2025-12-06-11-36-32.svg" alt="37 Loan Repayment Methods 2025-12-06 11.36.32" loading="lazy"></a></figure>

- Per the examples above, my answers are off by a couple of decimal points, so I don't know 100% if I did them correctly. I will have to double-check in Academic GOAL whether this is the case via pure problem-solving

## Sinking Fund {#sinking-fund}
- All payments go towards your interest and then something else that builds towards the loan and accrues interest
- Since the loan is going to be paid off all at once at the end, there aren't gonna be any in-between payment contributions
	- Therefore, the interest payments will also remain the same
- You should be careful as the sinking fund interest rate may not be the same as the loan interest rate

<a class="zoom" href="/notes/img/sinking-fund-initial-setup-example.png"><img src="/notes/img/sinking-fund-initial-setup-example.png" alt="sinking fund initial setup example" loading="lazy"></a>

<a class="zoom" href="/notes/img/sinking-fund-schedule-values-example.png"><img src="/notes/img/sinking-fund-schedule-values-example.png" alt="sinking fund schedule values example" loading="lazy"></a>

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/37-loan-repayment-methods-2025-12-06-13-53-06.svg"><img src="/notes/excalidraw/37-loan-repayment-methods-2025-12-06-13-53-06.svg" alt="37 Loan Repayment Methods 2025-12-06 13.53.06" loading="lazy"></a></figure>

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/37-loan-repayment-methods-2025-12-06-14-12-59.svg"><img src="/notes/excalidraw/37-loan-repayment-methods-2025-12-06-14-12-59.svg" alt="37 Loan Repayment Methods 2025-12-06 14.12.59" loading="lazy"></a></figure>
