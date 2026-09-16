---
author: "Anish Goyal"
title: "Annuity Unknown Number of Payments"
description: "If the number of payments are unknown (or alternatively, the annuity will continue until sufficient payment is made), then a balloon payment shall be the…"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-10-26T21:55:19
modified: 2025-10-26T22:01:33
readingtime: "1"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 19
weight: 190
slug: "annuity-unknown-number-of-payments"
links: []
sources: []
generated: true
---

## Concept {#concept}
- If the number of payments are unknown (or alternatively, the annuity will continue until sufficient payment is made), then a **balloon payment** shall be the last payment
	- The balloon payment is the additional amount included in the last payment for payoff
	- Arises because of a fractional time value, so you would have to evaluate the floor of the time value for payoff, then find the FV at that time value, and subtract it from the accumulated value of the loan
	- You have to be careful, though, since the balloon payment also accrues interest

$$\text{PV} = X a_{\left< n \right> } + P(1+i)^{-n}$$

<a class="zoom" href="/notes/img/balloon-payment-example.png"><img src="/notes/img/balloon-payment-example.png" alt="balloon payment example" loading="lazy"></a>
