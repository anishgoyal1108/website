---
author: "Anish Goyal"
title: "Bipolar Junction Transistors"
description: "Three terminals emitter base collector"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3341"
date: 2025-11-02T09:18:24
modified: 2025-11-02T10:09:03
readingtime: "1"
course: "EENG 3341"
course_slug: "eeng-3341"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 7
weight: 70
slug: "bipolar-junction-transistors"
links: []
sources:
  - "Course slides, chapter 5: Bipolar Junction Transistors"
generated: true
---

## Structure and Symbols {#structure-and-symbols}
- Three terminals emitter base collector
- Types NPN PNP
- Emitter heavily doped
- Base thin and lightly doped
- Collector moderately doped larger area
- Arrow shows emitter conventional current for NPN out for PNP in
- Two pn junctions in series view

## Currents and Voltages {#currents-and-voltages}
- Define $i_E, i_B, i_C$ with $i_E = i_B + i_C$
- Node voltages $v_{BE} v_{BC} v_{CE}$
- Sign convention currents enter device terminals

## Core Exponential Law {#core-exponential-law}

$$i_C = I_S e^{\frac{v_{BE}}{V_T}}$$

- $V_T \approx 25\,\text{mV}$ at $300\,\text{K}$
- $I_S$ set by device geometry and temperature

## Current Gain Relations {#current-gain-relations}
- Common emitter gain $\beta_F = \frac{i_C}{i_B}$
- Common base gain $\alpha_F = \frac{i_C}{i_E} = \frac{\beta_F}{\beta_F + 1}$:

$$i_B = \frac{i_C}{\beta_F} \quad i_E = i_B + i_C$$

## Operating Regions {#operating-regions}
- Cutoff: Open Circuit in branches BE and CE
	- Condition when evaluating forward-active model: $i_B < 0$
	- $v_{BE} < 0.7$ 
	- $i_B = 0$ and $i_C = 0$

- Saturation: No current amplification; constant potential difference at the junctions
	- Condition when evaluating forward-active model (assuming $i_B > 0$): $V_{CE} \le 0.2$
	- $V_{BE} = 0.7$
	- $V_{CE} = 0.2$

- Forward active: Current is amplified
	- Condition when evaluating forward-active model (assuming $i_B > 0$): $V_{CE} \gt 0.2$
	- $V_{BE} = 0.7$
	- $i_C \approx \beta_F i_B$

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/07-bipolar-junction-transistors-2025-11-02-10-10-14.svg"><img src="/notes/excalidraw/07-bipolar-junction-transistors-2025-11-02-10-10-14.svg" alt="07 Bipolar Junction Transistors 2025-11-02 10.10.14" loading="lazy"></a></figure>

## Common Emitter Output Behavior {#common-emitter-output-behavior}
- Plot $i_C$ versus $v_{CE}$ for fixed $i_B$
- Flat $i_C$ in forward active for $v_{CE}$ above a knee
- $i_B = 0$ gives cutoff curve

## References {#references}
- <span class="cite cite-ref">Course slides, chapter 5: Bipolar Junction Transistors</span>
