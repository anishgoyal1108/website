---
author: "Anish Goyal"
title: "SHM derivation"
description: "The restoring force of an ideal spring is Fs -ky(t). By Newton's 2nd Law:"
tags:
  - "notes"
  - "mathematics"
  - "math-4890"
date: 2024-10-19T13:59:27
modified: 2024-10-19T14:21:16
readingtime: "1"
course: "MATH 4890"
course_slug: "math-4890"
subject: "mathematics"
kind: "concept"
weight: 9002
slug: "shm-derivation"
links: []
sources: []
generated: true
---

### SHM Derivation {#shm-derivation}
The restoring force of an ideal spring is $F_s = -ky(t)$. By Newton's 2nd Law:

$$-ky(t) = my''(t)$$

Since $c = \sqrt{\frac{k}{m}}$, the second order ODE becomes:

$$y''(t)+c^2y(t)=0$$

with a general solution of:

$$y(t)=a\cos{ct} + b\sin{ct}$$

If we are given initial position and velocity ($y(0)$ and $y'(0)$), the unique solution is given by:

$$y(t) = y(0)\cos{ct} + \frac{y'(0)}{c}\sin{ct}$$

And there are constants $A > 0$ and $\gamma \in \mathbb{R}$ such that:

$$y(t) = a\cos{ct}+b\sin{ct} = A\cos({ct-\phi})$$

where:
- $A = \sqrt{a^2 + b^2}$ and is the amplitude
- $c$ is the frequency
- $\phi$ is the phase
- $\frac{2\pi}{c}$ is the period
