---
author: "Anish Goyal"
title: "Dollar-Weighted and Time-Weighted Rate of Return"
description: "If we make contributions and withdrawals at time points that are within one time interval, we can weight those dollar intervals to get the final balance in…"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-11-01T23:01:58
modified: 2025-12-06T07:24:16
readingtime: "1"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 33
weight: 330
slug: "dollar-weighted-and-time-weighted-rate-of-return"
links: []
sources: []
generated: true
---

## Concept {#concept}
- If we make contributions and withdrawals at time points that are within one time interval, we can weight those dollar intervals to get the final balance in the account at the end of the time period

## Solution {#solution}
### Dollar-Weighted RoR {#dollar-weighted-ror}
- It's just doing accumulated values but with negatives for account contributions
- Basically, it's just the IRR

<a class="zoom" href="/notes/img/dollar-weighted-rate-of-return.png"><img src="/notes/img/dollar-weighted-rate-of-return.png" alt="dollar-weighted rate of return" loading="lazy"></a>

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/33-dollar-weighted-and-time-weighted-rate-of-return-2025-11-01-23-10-55.svg"><img src="/notes/excalidraw/33-dollar-weighted-and-time-weighted-rate-of-return-2025-11-01-23-10-55.svg" alt="33 Dollar-Weighted and Time-Weighted Rate of Return 2025-11-01 23.10.55" loading="lazy"></a></figure>

<a class="zoom" href="/notes/img/dollar-weighted-ror-example.png"><img src="/notes/img/dollar-weighted-ror-example.png" alt="dollar-weighted ror example" loading="lazy"></a>

If given a table, it would be (for a linear approximation): $$\frac{I}{A + \sum C_{k}(1-t)}$$

### Time-Weighted RoR {#time-weighted-ror}
- The product of all the individual interests equals $(1+i)$
- To find the $j$'th interest from a table of balances and contributions: $$\frac{B_{t_{k}}}{B_{t_{k-1}}+C_{{t_{k-1}}}} -1$$

<a class="zoom" href="/notes/img/time-weighted-rate-of-return.png"><img src="/notes/img/time-weighted-rate-of-return.png" alt="time-weighted rate of return" loading="lazy"></a>
