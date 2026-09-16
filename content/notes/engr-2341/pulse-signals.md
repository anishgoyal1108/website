---
author: "Anish Goyal"
title: "pulse signals"
description: "Pulses are only non-zero between t1 and t2"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-01-15T15:53:08
modified: 2025-01-16T21:42:19
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "concept"
weight: 9016
slug: "pulse-signals"
links: []
sources: []
generated: true
---

## Pulse Signals {#pulse-signals}
- Pulses are only non-zero between $t_1$ and $t_2$
- Unit pulses have a height of 1
- Technically a difference of step signals

$$
p(t) = u(t-t_{1})-u(t-t_{2})=\begin{cases}
1 & t_{1} \le t \le t_{2} \\
0 & t \lt t_{1} \ \mathrm{or} \ \gt t_{2}
\end{cases}
$$

- Multiplying a function by a pulse gives us a finite duration signal

$$
x(t) = 5\cos(3\pi t) \cdot (u(t)-u(t-2))
$$

- This gives us a cosine wave with $f = 3 \pi$ rad/s and $A = 5$ for $t \in [0, 2]$ 
