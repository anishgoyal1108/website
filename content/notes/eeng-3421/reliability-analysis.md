---
author: "Anish Goyal"
title: "Reliability Analysis"
description: "Systems are built with chained processes"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-02-18T09:29:11
modified: 2026-02-18T09:29:21
readingtime: "1"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 6
weight: 60
slug: "reliability-analysis"
links: []
sources:
  - "Course lecture slides 9–10"
generated: true
---

## System Reliability {#system-reliability}
- Systems are built with chained processes
	- May be arranged in series or parallel
- Goal is to determine the overall probability/reliability of the system
- We assume that each process will succeed/fail without altering the probability of subsequent processes

## Chained Processes {#chained-processes}
- Series
	- Success only occurs when all processes work

$$P(W_1 W_2 \dots W_{n}) = p_{1} \times p_{2} \times \dots \times p_{n}$$

- Parallel
	- Success only occurs when all processes *don't* work

$$P(W) = 1 - P(W^c)$$

## References {#references}
- <span class="cite cite-ref">Course lecture slides 9–10</span>
