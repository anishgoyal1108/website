---
author: "Anish Goyal"
title: "Circuit Elements"
description: "Dissipate power from the circuit and obey passive sign convention"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2334"
date: 2025-02-10T15:24:20
modified: 2025-04-02T03:31:14
readingtime: "4"
course: "ENGR 2334"
course_slug: "engr-2334"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 2
weight: 20
slug: "circuit-elements"
links: []
sources:
  - "Course slides, chapter 2: Circuit Elements"
generated: true
---

## Types of Circuit Elements {#types-of-circuit-elements}

### Passive Elements {#passive-elements}
- Dissipate power from the circuit and obey passive sign convention
- Types:
	- Resistors (R)
	- Inductors (L)
	- Capacitors (C)
	- Diodes

### Active Elements {#active-elements}
- Supply power to the circuit and obey active sign convention
- Types:
	- Voltage sources
	- Current sources
	- Controlled sources
	- Op-amps

## Properties of Linear Elements {#properties-of-linear-elements}
- **Superposition**: Output is the sum of individual inputs

$$
\begin{align}
i_{1} &\rightarrow v_{1} \\
i_{2} &\rightarrow v_{2} \\
i_{1} + i_{2} &\rightarrow v_{1} + v_{2}
\end{align}
$$

- **Homogeneity/Scaling**: If input is scaled, output scales proportionally

$$
\begin{align}
i &\rightarrow v \\
ki &\rightarrow kv
\end{align}
$$

- Combining both properties:

$$
ki_{1} + ki_{2} \rightarrow kv_{1} + kv_{2}
$$

## Ohm's Law {#ohm-s-law}
- The potential difference across a resistor is proportional to the current, with a constant of proportionality (slope) being resistance

$$V = iR$$

- $V$ is dependent upon the direction of $i$

## Resistors and Resistance {#resistors-and-resistance}

### Resistance {#resistance}
- The physical property of an element or device that impedes current flow

$$R = \frac{\rho L}{A}$$

#### Example {#example}
<a class="zoom" href="/notes/img/circuit-resistance-example.png"><img src="/notes/img/circuit-resistance-example.png" alt="circuit resistance example" loading="lazy"></a>

### Linear Resistors {#linear-resistors}
- Since resistors are linear, $V$ will be a function of $i$ and $R$ will be independent of both $V$ and $i$
	- When two currents $i_1$ and $i_2$ flow through a resistor with resistance $R$ with corresponding voltages $V_1 = i_1R$ and $V_2 = i_2R$, the total voltage would be:

$$V = R(i_{1} + i_{2}) = V_{1} + V_{2}$$

### Power Dissipated by a Resistor {#power-dissipated-by-a-resistor}
- Substituting Ohm's Law into the power equation:

$$V = (iR)i = i^2 R$$

- Also expressed as:

$$P = \frac{V^2}{R}$$

<a class="zoom" href="/notes/img/power-dissipated-by-resistor-example.png"><img src="/notes/img/power-dissipated-by-resistor-example.png" alt="power dissipated by resistor example" loading="lazy"></a>

## Independent Sources {#independent-sources}
- Independent sources are ideal
	- This means they supply a voltage/current regardless of the current drawn or the potential difference across that source
	- In the real world, this is not the case, however

### Voltage Source {#voltage-source}
- Supplies a potential $V(t)$
- The resulting current is a result of the remainder of the circuit
- We usually draw voltage sources to obey the *active sign convention*, even though the image below obeys passive sign convention

<a class="zoom" href="/notes/img/voltage-source.png"><img src="/notes/img/voltage-source.png" alt="voltage source" loading="lazy"></a>

### Current Source {#current-source}
- Supplies a current $i(t)$
- The resulting voltage is a result of the remainder of the circuit
- In the real world, this is accomplished by adjusting the voltage to provide the desired current
- We usually draw current sources to obey the *active sign convention*, even though the image below obeys passive sign convention

<a class="zoom" href="/notes/img/current-source.png"><img src="/notes/img/current-source.png" alt="current source" loading="lazy"></a>

## Measuring Devices {#measuring-devices}
- Measures current or voltage when models can't be established
- Red lead goes to (+) terminal, black lead to (-)
	- Otherwise, device will read negative values

### Ammeter {#ammeter}
- Measures current in A
- Wired in series
- Assume resistance is zero
	- This creates a short circuit; current flows through the device but no potential difference exists

<a class="zoom" href="/notes/img/ammeter.png"><img src="/notes/img/ammeter.png" alt="ammeter" loading="lazy"></a>

### Voltmeter {#voltmeter}
- Measures potential difference in V
- Wired in parallel
- Assume resistance is infinite
	- This creates an open circuit; no current exists but there is still a potential difference 

<a class="zoom" href="/notes/img/voltmeter.png"><img src="/notes/img/voltmeter.png" alt="voltmeter" loading="lazy"></a>

## Dependent Sources {#dependent-sources}
- Used to model transistors and amplifiers
- $b=g=d=r \equiv k$ is the gain of the system

<a class="zoom" href="/notes/img/dependent-sources.png"><img src="/notes/img/dependent-sources.png" alt="dependent sources" loading="lazy"></a>

- Current-controlled sources are short circuits
	- This is because current sources don't restrict current
- Voltage-controlled sources are open circuits
	- This is because voltage sources shouldn't have voltages when control is removed

<a class="zoom" href="/notes/img/dependent-sources-short-and-open-circuit.png"><img src="/notes/img/dependent-sources-short-and-open-circuit.png" alt="dependent sources short and open circuit" loading="lazy"></a>

### Examples {#examples}
<a class="zoom" href="/notes/img/vcvs-example.png"><img src="/notes/img/vcvs-example.png" alt="vcvs example" loading="lazy"></a>

<a class="zoom" href="/notes/img/cccs-example.png"><img src="/notes/img/cccs-example.png" alt="cccs example" loading="lazy"></a>

<a class="zoom" href="/notes/img/cccs-example-2.png"><img src="/notes/img/cccs-example-2.png" alt="cccs example 2" loading="lazy"></a>

<a class="zoom" href="/notes/img/ccvs-example.png"><img src="/notes/img/ccvs-example.png" alt="ccvs example" loading="lazy"></a>

## Transducers {#transducers}
- Convert physical quantities to electrical signals

### Types {#types}
- **Potentiometer**: Converts rotational position to resistance with $a = \frac{\theta}{360^\circ}$
	- Two branches, one with $R = aR_p$ and the other with $R = (1-a)R_p$
- **Temperature Sensor**: Converts temperature to current, $i = kT$, where $k = 1 \frac{\mu A}{^\circ K}$

## Switches {#switches}
- Single-Pole Single-Throw is like a light switch and can be used to prevent momentary connection of old and new circuit paths (break before make)
- Single-Pole Double-Throw switches between two branches without ever seeing an open circuit (make before break)

<a class="zoom" href="/notes/img/switches.png"><img src="/notes/img/switches.png" alt="switches" loading="lazy"></a>

### Examples {#examples-1}
<a class="zoom" href="/notes/img/switches-example-1.png"><img src="/notes/img/switches-example-1.png" alt="switches example 1" loading="lazy"></a>

<a class="zoom" href="/notes/img/switches-example-2.png"><img src="/notes/img/switches-example-2.png" alt="switches example 2" loading="lazy"></a>

## References {#references}

- <span class="cite cite-ref">Course slides, chapter 2: Circuit Elements</span>
