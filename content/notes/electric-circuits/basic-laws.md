---
author: "Anish Goyal"
title: "Basic Laws"
description: "where is the resistivity in m, is length, and A is cross-sectional area."
tags:
  - "notes"
  - "electrical-engineering"
  - "electric-circuits"
date: 2025-06-12T17:37:17
modified: 2025-06-27T01:45:32
readingtime: "12"
course: "Fundamentals of Electric Circuits (Sadiku)"
course_slug: "electric-circuits"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 2
weight: 20
slug: "basic-laws"
links: []
sources:
  - "Alexander & Sadiku, Fundamentals of Electric Circuits"
generated: true
---

## Resistance and Ohm's Law {#resistance-and-ohm-s-law}
### Resistance {#resistance}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.1</span>.</div></div>
<div class="callout-content">

Resistance is the behavior of a material to resist the flow of electric charge, represented by

</div>
</div>

$$R = \rho \frac{\ell}{A},$$

where $\rho$ is the resistivity in $\Omega m$, $\ell$ is length, and $A$ is cross-sectional area.

#### Resistivities of Common Materials {#resistivities-of-common-materials}
| Material   | Resistivity (Ω·m)     | Usage          |
|------------|-----------------------|----------------|
| Silver     | 1.64 × 10⁻⁸           | Conductor      |
| Copper     | 1.72 × 10⁻⁸           | Conductor      |
| Aluminum   | 2.8 × 10⁻⁸            | Conductor      |
| Gold       | 2.45 × 10⁻⁸           | Conductor      |
| Carbon     | 4 × 10⁻⁵              | Semiconductor  |
| Germanium  | 47 × 10⁻²             | Semiconductor  |
| Silicon    | 6.4 × 10²             | Semiconductor  |
| Paper      | 10¹⁰                  | Insulator      |
| Mica       | 5 × 10¹¹              | Insulator      |
| Glass      | 10¹²                  | Insulator      |
| Teflon     | 3 × 10¹²              | Insulator      |

### The Resistor {#the-resistor}
- The simplest passive element
- Used to model the current-resisting behavior of a material
- $R$ is the resistance of the resistor

#### Types of Resistors {#types-of-resistors}
- Fixed resistors have constant $R$
- Variable resistors, such as potentiometers, have adjustable $R$

### Ohm's Law {#ohm-s-law}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.2</span> <span class="theorem-callout-subtitle">(Ohm's Law)</span>.</div></div>
<div class="callout-content">

The voltage $v$ across a resistor is directly proportional to the current $i$ through the resistor.

$$v \propto i$$

The proportionality constant for this relationship is the resistance, $R$. So, the equation becomes

$$v = iR.$$

</div>
</div>

- To obey the passive convention, the current direction and voltage polarity must flow from a high potential (VCC) to low potential (GND)
- Since $R \in [0, \infty]$, we must consider two extremal values of $R$:
	- When $R = 0$, there is a *short circuit*; the voltage is zero but the current can be anything
	- When $R = \infty$, there is an *open circuit*; the current is zero but the voltage can be anything

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.3</span> <span class="theorem-callout-subtitle">(Short Circuit)</span>.</div></div>
<div class="callout-content">

Any circuit element with $R \rightarrow 0$. In practice, this is a connecting wire between two points in the circuit, in which the charge carriers take the path of least resistance.

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.4</span> <span class="theorem-callout-subtitle">(Open Circuit)</span>.</div></div>
<div class="callout-content">

Any circuit element with $R \rightarrow \infty$. In practice, this is a literal gap in the circuit, since air is a perfect insulator.

</div>
</div>

### Conductance {#conductance}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.5</span> <span class="theorem-callout-subtitle">(Conductance)</span>.</div></div>
<div class="callout-content">

The ability of an element to conduct electric current; it is measured in mhos ($\mho$)/siemens (S).

</div>
</div>

- Ohm's Law under conductance may be expressed as:

$$ i = Gv$$

#### Power Dissipated by a Resistor {#power-dissipated-by-a-resistor}
- Nonlinear in terms of current or voltage 
- Can be expressed in terms of $R$:

$$p = i^2 R = \frac{v^2}{R}$$

- Or in terms of $G$:

$$p = v^2 G = \frac{i^2}{G}$$

- Since $R$ and $G$ are always positive, power dissipated is always positive; therefore, resistors always absorb power (adheres to the passive convention)

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.6</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 2.1</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;60]</span></cite>)
```py
In [1]: eq = Eq(110**2 / 15, x * 110)

In [2]: solve(eq, x)
Out[2]: [7.33333333333334]
```

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.7</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 2.2</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;61]</span></cite>)
```py
In [1]: v = 3e-3 * 10e3

In [2]: G = 1/10e3

In [3]: p = 3e-3**2 * 10e3

In [4]: v, G, p
Out[4]: (30.0, 0.0001, 0.09)
```

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.8</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 2.3</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;61]</span></cite>)
```py
In [2]: p = 30*cos(t)**2

In [3]: v = 15*cos(t)

In [4]: i = p / v

In [5]: R = v**2 / p

In [6]: i, R
Out[6]: (2⋅cos(t), 15/2)
```

</div>
</div>

## Nodes, Branches, and Loops {#nodes-branches-and-loops}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.9</span> <span class="theorem-callout-subtitle">(Branch)</span>.</div></div>
<div class="callout-content">

Any two-terminal element in a circuit, such as a power source or resistor. The number of branches equals the number of circuit elements.

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.10</span> <span class="theorem-callout-subtitle">(Node)</span>.</div></div>
<div class="callout-content">

The point of connection between two or more branches. 
- Typically indicated by a dot in a circuit
- If a short circuit connects two nodes, the two nodes may be treated as a single node

</div>
</div>

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.11">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.11</span> <span class="theorem-callout-subtitle">(Loop)</span>.</div></div>
<div class="callout-content">

Any closed path in a circuit.
- A "closed path" starts at a node, passes through a set of nodes, and returns to the starting node without passing through any node more than once.
- Is *independent* if it contains a branch that is not part of any other independent loop
	- Independent loops result in independent sets of equations

</div>
</div>

- A network with $b$ branches, $n$ nodes, and $l$ independent loops will satisfy the following relation (The Fundamental Theorem of Network Topology):

$$b = l + n - 1$$

- Two elements are in **series** if they exclusively share a single node
	- Consequently, they share the same current
- Two elements are in **parallel** if they are connected to the same two nodes
	- Consequently, they share the same voltage

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.12">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.12</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 2.4</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;63]</span></cite>)
- 5 elements, so 5 branches
- 3 nodes
- 4 $\Omega$ is in parallel with 10V
- 1 $\Omega$ is in parallel with 2 $\Omega$

</div>
</div>

## Kirchoff's Laws {#kirchoff-s-laws}

### Kirchoff's Current Law {#kirchoff-s-current-law}
- Based on the principle of conservation of charge

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.13">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.13</span> <span class="theorem-callout-subtitle">(Kirchoff's Current Law)</span>.</div></div>
<div class="callout-content">

The algebraic sum of currents entering/exiting a node is zero.

$$
\sum_{n=1}^{N} i_{n} = 0
$$

where $N$ is the number of branches connected to the node and $i_{n}$ is the $n$th current entering/exiting the node.

</div>
</div>

- Currents entering a node is positive, while leaving current is negative
- Alternative interpretation: the sum of currents entering a node is equal to the sum of the currents leaving the node
- KCL may also be applied to any closed boundary, since a node is a closed surface shrunk to a point
- A consequence of KCL is that a circuit cannot contain two different currents in series
- Another consequence is that current sources in parallel may be added together

### Kirchoff's Voltage Law {#kirchoff-s-voltage-law}
- Based on the principle of conservation of energy

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.14">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.14</span> <span class="theorem-callout-subtitle">(Kirchoff's Voltage Law)</span>.</div></div>
<div class="callout-content">

The algebraic sum of all voltages around a loop is zero.

$$
\sum_{m = 1}^{M} v_{m} = 0
$$

where $M$ is the number of branches in the loop and $v_{m}$ is the $m$th voltage.

</div>
</div>

- Can go clockwise or counterclockwise around the loop
- The sign on each voltage is the polarity of the terminal encountered first
- Alternative interpretation: the sum of voltage drops is equal to the sum of voltage rises
- A consequence of KVL is that a circuit cannot contain two different voltages in parallel
- Another consequence is that voltage sources in series may be added together

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.15">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.15</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 2.5</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;67]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/drawing-2025-06-18-14-08-05.svg"><img src="/notes/excalidraw/drawing-2025-06-18-14-08-05.svg" alt="Drawing 2025-06-18 14.08.05" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.16">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.16</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 2.6</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;67]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/basic-laws-2025-06-18-15-34-02.svg"><img src="/notes/excalidraw/basic-laws-2025-06-18-15-34-02.svg" alt="Basic Laws 2025-06-18 15.34.02" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.17">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.17</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 2.6</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;67]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/basic-laws-2025-06-20-16-40-09.svg"><img src="/notes/excalidraw/basic-laws-2025-06-20-16-40-09.svg" alt="Basic Laws 2025-06-20 16.40.09" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.18">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.18</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 2.7</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;68]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/basic-laws-2025-06-20-16-48-31.svg"><img src="/notes/excalidraw/basic-laws-2025-06-20-16-48-31.svg" alt="Basic Laws 2025-06-20 16.48.31" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.19">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.19</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 2.7</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;68]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/basic-laws-2025-06-20-16-52-56.svg"><img src="/notes/excalidraw/basic-laws-2025-06-20-16-52-56.svg" alt="Basic Laws 2025-06-20 16.52.56" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.20">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.20</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 2.8</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;69]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/basic-laws-2025-06-20-16-58-31.svg"><img src="/notes/excalidraw/basic-laws-2025-06-20-16-58-31.svg" alt="Basic Laws 2025-06-20 16.58.31" loading="lazy"></a></figure>

</div>
</div>

## Series Resistance {#series-resistance}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.21">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.21</span> <span class="theorem-callout-subtitle">(Equivalent Resistance of Series Resistors)</span>.</div></div>
<div class="callout-content">

The **equivalent resistance** $R_{\text{eq}}$ of any number of resistors connected in series is the sum of the individual resistances.

$$R_{\text{eq}} = \sum_{n=1}^{N} R_{n}$$

</div>
</div>

- Series resistors share the same current, but not the same voltage
- However, the total voltage across all the resistors (the equivalent resistor) can be calculated as $R_{\text{eq}} i$

### Voltage Division {#voltage-division}
- A voltage source connected to a network of resistors in series effectively *divides* up that voltage, known as a **voltage divider**
- The resistance of the $n$th resistor in the voltage divider is calculated as:

$$v_{n} = \frac{V_{s}R_{n}}{R_{\text{eq}}}$$

## Parallel Resistances {#parallel-resistances}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="02.22">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 02.22</span> <span class="theorem-callout-subtitle">(Equivalent Resistance of Parallel Resistors)</span>.</div></div>
<div class="callout-content">

The **equivalent resistance** of two parallel resistors is equal to the product of their resistances divided by their sum.

$$R_{\text{eq}} = \frac{R_{1}R_{2}}{R_{1}+R_{2}}$$

For $n$ resistors in parallel, the equivalent resistance is

$$R_{\text{eq}} = \left(\sum_{n=1}^{N} \frac{1}{R_{n}}\right)^{-1}.$$

</div>
</div>

- $R_{\text{eq}}$ is always less than the smallest resistor in parallel
- If all the resistances in the parallel network are the same, then:

$$R_{\text{eq}} = \frac{R}{N}$$

### Equivalent Conductance {#equivalent-conductance}
- Since $G = \frac{1}{R}$ by definition, it is possible to express parallel resistance in terms of conductance:

$$G_{\text{eq}} = \sum_{n=1}^{N}G_{n}$$

where $G_{\text{eq}}$ = $\frac{1}{R_{\text{eq}}}$
- The same may be done for series resistance:

$$G_{\text{eq}} = \left(\sum_{n=1}^{N}\frac{1}{G_{n}}\right)^{-1}$$

### Current Division {#current-division}
- The total current in a network of parallel elements is  effectively *divided* across those elements, known as **current division**
- The current of the $n$th resistor in the current divider is calculated as:

$$i_{n} = i_{s}\left(\frac{R_{\text{eq}}}{R_{n}}\right),$$

or using the conductance definition:

$$i_{n} = \frac{i_{s}G_{n}}{G_{\text{eq}}}$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.23">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.23</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 2.12</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;76]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/basic-laws-2025-06-21-10-08-47.svg"><img src="/notes/excalidraw/basic-laws-2025-06-21-10-08-47.svg" alt="Basic Laws 2025-06-21 10.08.47" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.24">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.24</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 2.13</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;77]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/basic-laws-2025-06-21-10-22-07.svg"><img src="/notes/excalidraw/basic-laws-2025-06-21-10-22-07.svg" alt="Basic Laws 2025-06-21 10.22.07" loading="lazy"></a></figure>

</div>
</div>

## Wye-Delta Transformations {#wye-delta-transformations}
- Resistive networks that aren't in series or parallel may be simplified to a three-terminal equivalent network
	- Either the Wye/Tee network or the Delta/Pi network

### Delta-Wye Conversion {#delta-wye-conversion}
- Superimpose Y onto $\Delta$ by adding an extra node $n$. Each resistor in Y is the product of the resistors in the two adjacent $\Delta$ branches divided by the sum of the three $\Delta$ resistors
- For the network below:

$$\begin{align}
R_{1} &= \frac{R_{b}R_{c}}{R_{a}+R_{b}+R_{c}} \\
R_{2} &= \frac{R_{c}R_{a}}{R_{a}+R_{b}+R_{c}} \\
R_{3} &= \frac{R_{a}R_{b}}{R_{a}+R_{b}+R_{c}}
\end{align}
$$

<a class="zoom" href="/notes/img/delta-wye-conversion-example.png"><img src="/notes/img/delta-wye-conversion-example.png" alt="delta wye conversion example" loading="lazy"></a>

### Wye-Delta Conversion {#wye-delta-conversion}
- Each resistor in the $\Delta$ network is the sum of all products of Y resistors divided by the opposite Y resistor
- For the superimposed network:

$$\begin{align}
R_{a} &= \frac{R_{1}R_{2}+R_{2}R_{3}+R_{3}R_{1}}{R_{1}} \\
R_{b} &= \frac{R_{1}R_{2}+R_{2}R_{3}+R_{3}R_{1}}{R_{2}} \\
R_{c} &= \frac{R_{1}R_{2}+R_{2}R_{3}+R_{3}R_{1}}{R_{3}}
\end{align}$$

### Balanced Condition {#balanced-condition}
- If all the Y resistances are equal AND all the $\Delta$ resistances are equal, then:

$$R_{Y} = \frac{R_{\Delta}}{3} \ \text{or} \ R_{\Delta}= 3R_{Y}$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.25">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.25</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 2.14</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;80]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/basic-laws-2025-06-21-11-14-16.svg"><img src="/notes/excalidraw/basic-laws-2025-06-21-11-14-16.svg" alt="Basic Laws 2025-06-21 11.14.16" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.26">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.26</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 2.15</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;83]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/basic-laws-2025-06-21-11-28-20.svg"><img src="/notes/excalidraw/basic-laws-2025-06-21-11-28-20.svg" alt="Basic Laws 2025-06-21 11.28.20" loading="lazy"></a></figure>

</div>
</div>
