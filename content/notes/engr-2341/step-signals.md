---
author: "Anish Goyal"
title: "step signals"
description: "Signals that are nonzero for t 0"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-01-15T14:01:39
modified: 2025-01-20T15:19:40
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "concept"
weight: 9019
slug: "step-signals"
links: []
sources: []
generated: true
---

## Step Signals {#step-signals}
- Signals that are nonzero for $t \ge 0$

$$
u(t) = \begin{cases}
0 & t \lt 0 \\
1 & t \ge 0
\end{cases}
$$

- Unit step signals have a height of 1
- Used to create one sided signals (usually right-sided)

$$ 
\begin{align}
x(t) &= 3.72e^{-12.8t} \\
x_{\mathrm{rs}}(t) &= 3.72e^{-12.8t} \cdot u(t)
\end{align}
$$

- Discontinuous at $t = 0$ due to the piecewise nature of the function
