---
author: "Anish Goyal"
title: "Introduction to Electronics"
description: "DC components have capital letters and subscripts"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3341"
date: 2025-08-20T08:10:38
modified: 2025-08-22T08:10:22
readingtime: "1"
course: "EENG 3341"
course_slug: "eeng-3341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 1
weight: 10
slug: "introduction-to-electronics"
links: []
sources:
  - "Course slides, chapter 1: Introduction to Electronics"
generated: true
---

## Notation {#notation}
- DC components have capital letters and subscripts
- Time-varying values have lowercase letters and subscripts
- Total quantities (sum of DC and time-varying) have lowercase letters and capital subscripts 
- Phasors use uppercase letter with lowercase subscript

## Thevenin Example in Class {#thevenin-example-in-class}

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-introduction-to-electronics-2025-08-20-08-13-52.svg"><img src="/notes/excalidraw/01-introduction-to-electronics-2025-08-20-08-13-52.svg" alt="01 Introduction to Electronics 2025-08-20 08.13.52" loading="lazy"></a></figure>

## Materials {#materials}
- Electronic materials fall into three categories based on their resistivity $(\rho)$
	- Conductors: $\rho < 1\text{e-3} \ \Omega \text{-cm}$
	- Semiconductors: $\rho \in [1\text{e-3},1\text{e5}]\ \Omega \text{-cm}$
	- Insulators: $\rho > 1\text{e5}\ \Omega \text{-cm}$

## Variability {#variability}
- All electronic components have manufacturing tolerances that vary with temperature and age
	- Resistor: $\pm$ 10%/5%/1%
	- Capacitor: Asymmetrical tolerances (such as +20% or -50%)
	- Power sources: 1%-10%

## Tolerance Modeling {#tolerance-modeling}
- Symmetrical variations

$$P_{\text{nom}} (1-\epsilon) \le P \le P_{\text{nom}}(1+\epsilon)$$ 

## Numeric Precision {#numeric-precision}
- More than three sig figs not needed

## References {#references}
- <span class="cite cite-ref">Course slides, chapter 1: Introduction to Electronics</span>
