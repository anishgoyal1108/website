---
author: "Anish Goyal"
title: "Electric Circuit Variables"
description: "A circuit is an interconnection of electrical elements linked together in a closed path so an electric current can flow"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2334"
date: 2025-01-16T09:35:10
modified: 2025-04-02T02:44:43
readingtime: "1"
course: "ENGR 2334"
course_slug: "engr-2334"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 1
weight: 10
slug: "electric-circuit-variables"
links:
  - "/notes/engr-2334/circuit/"
sources:
  - "Course slides, chapter 1: Electric Circuit Variables"
generated: true
---

## Electric Circuit {#electric-circuit}
- A <a class="internal-link" href="/notes/engr-2334/circuit/">circuit</a> is an interconnection of electrical elements linked together in a closed path so an electric current can flow
	- electrical elements: battery, resistor, capacitor, inductor (also called devices)
- A terminal of a circuit is also called a node

## Current {#current}
- We denote current, $\frac{\mathrm{d}q}{\mathrm{d}t}$, as $i$

### Direction Matters! {#direction-matters}
- Current is inverted depending on the direction
	- $i_{1} = -i_{2}$

### Types of Current {#types-of-current}
- The behavior of $i$ determines the type of current
- Direct current
	- monotonous current; straight line
- Alternating current
	- the current varies as a wave function
	- single tone, one frequency
	- come from alternators
- Rest are signal currents

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/electric-circuit-variables-2025-01-16-10-18-51.svg"><img src="/notes/excalidraw/electric-circuit-variables-2025-01-16-10-18-51.svg" alt="Electric Circuit Variables 2025-01-16 10.18.51" loading="lazy"></a></figure>

## Charge {#charge}

$$
q(t) = q(0) + \int_{0}^t i(\tau) \ \mathrm{d}\tau 
$$

## Sign Convention {#sign-convention}
- Used to describe the behavior of circuit elements

### Passive Sign Convention {#passive-sign-convention}
- The circuit element is dissipating/absorbing power
- $i$ goes into (+) terminal
- $\Delta V < 0$
<a class="zoom" href="/notes/img/passive-convention.png"><img src="/notes/img/passive-convention.png" alt="passive convention" loading="lazy"></a>

### Active Sign Convention {#active-sign-convention}
- The circuit element is supplying power
- $i$ goes into (-) terminal
- $\Delta V > 0$
<a class="zoom" href="/notes/img/active-convention.png"><img src="/notes/img/active-convention.png" alt="active convention" loading="lazy"></a>

### Example {#example}
<a class="zoom" href="/notes/img/sign-convention-example.png"><img src="/notes/img/sign-convention-example.png" alt="sign convention example" loading="lazy"></a>

## Power {#power}

$$P = \frac{\mathrm{d}w}{\mathrm{d}t} = \frac{\mathrm{d}q}{\mathrm{d}t}\frac{\mathrm{d}w}{\mathrm{d}q} = iV$$

## Net Energy {#net-energy}
- The net work/energy done by an element is

$$w = \int_{t_{1}}^{t_{2}} P \ \mathrm{d}{\tau}$$

### Example {#example-1}
<a class="zoom" href="/notes/img/circuit-net-energy-example.png"><img src="/notes/img/circuit-net-energy-example.png" alt="circuit net energy example" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Course slides, chapter 1: Electric Circuit Variables</span>
