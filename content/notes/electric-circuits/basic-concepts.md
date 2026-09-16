---
author: "Anish Goyal"
title: "Basic Concepts"
description: "Analyzing circuits is important to understand:"
tags:
  - "notes"
  - "electrical-engineering"
  - "electric-circuits"
date: 2025-06-12T15:15:34
modified: 2025-06-26T11:41:40
readingtime: "7"
course: "Fundamentals of Electric Circuits (Sadiku)"
course_slug: "electric-circuits"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 1
weight: 10
slug: "basic-concepts"
links: []
sources:
  - "Alexander & Sadiku, Fundamentals of Electric Circuits"
generated: true
---

## What is Circuit Analysis? {#what-is-circuit-analysis}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.1</span> <span class="theorem-callout-subtitle">(Electric Circuit)</span>.</div></div>
<div class="callout-content">

An interconnection of electrical elements

</div>
</div>

- Analyzing circuits is important to understand:
	- *How does it respond to a given input?*
	- *How do the interconnected elements and devices interact?*

## Charge and Current {#charge-and-current}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.2</span> <span class="theorem-callout-subtitle">(Electric Charge)</span>.</div></div>
<div class="callout-content">

An electrical property of the atomic particles of which matter consists, measured in coulombs (C)

</div>
</div>

- The fundamental charge $e$ is equal to -1.602e-19 C
- In 1 C of charge there are 1/(1.602e-19) = 6.24e18 electrons
- Charge is quantized and conserved

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.3</span> <span class="theorem-callout-subtitle">(Electric Current)</span>.</div></div>
<div class="callout-content">

The time rate of change of charge, measures in amperes (A) = 1 C/s

$$i = \frac{\mathrm{d}q}{\mathrm{d}t}$$

$$Q = \int_{t_{0}}^{t} i \, \mathrm{d}t$$

</div>
</div>

- Current that never reverses direction is **direct current** (DC)
- Current that changes direction is **alternating current** (AC)
- By convention, we take current to flow in the direction of positive charges

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.4</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 1.1</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;34]</span></cite>)
```py
In [1]: -1.602e-19*4.6e3
Out[1]: -7.3692e-16
```

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.5</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 1.1</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;34]</span></cite>)
```py
In [2]: 1.602e-19*10e9
Out[2]: 1.602e-09
```

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.6</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 1.2</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;34]</span></cite>)
```py
In [5]: diff(5*x*sin(4*pi*x))
Out[5]: 20⋅π⋅x⋅cos(4⋅π⋅x) + 5⋅sin(4⋅π⋅x)
In [18]: _.subs(x, 0.5)
Out[18]: 10.0⋅π
```

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.7</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 1.2</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;34]</span></cite>)
```py
In [19]: diff(20-15*x-10*exp(-3*x)).subs(x, 1)
Out[19]:-15 + 30*exp(-3)
In [3]: N(_)
Out[3]: -13.5063879489641
```

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.8</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 1.3</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;34]</span></cite>)
```py
In [4]: Q = Piecewise((8, (t<1)&(t>0)),(8*t**2, (t>1)))
In [5]: integrate(Q, (t, 0, 2))
Out[5]: 80/3
```

</div>
</div>

## Voltage {#voltage}
- Moving a point charge requires work
	- This work requires an *external electromotive force (emf)*, typically a battery
	- This emf is also known as **voltage** or **potential difference**
- The voltage $v_{ab}$ between two points $a$ and $b$ in a circuit is the work, in joules (J), needed to move a unit charge, in coulombs, from $b$ to $a$
	- Measured in volts (V) = 1 J/C = 1 Nm/C 

$$v_{ab} = \frac{\mathrm{d}w}{\mathrm{d}q}$$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.9</span> <span class="theorem-callout-subtitle">(Voltage/Potential Difference)</span>.</div></div>
<div class="callout-content">

The energy required to move a unit charge from GND (-) to VCC (+), measured in volts (V).

</div>
</div>

- $v_{ab}$ can be interpreted in two ways:
	1. Point $a$ is at a potential $v_{ab}$ higher than point $b$ (the voltage drops from $a$ to $b$)
	2. The electric potential at point $a$ with respect to point $b$ is $v_{ab}$
- It follows that $v_{ab} = -v_{ba}$

## Power and Energy {#power-and-energy}

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.10</span> <span class="theorem-callout-subtitle">(Power)</span>.</div></div>
<div class="callout-content">

The time rate of expending/absorbing energy, measured in watts (W) 

$$p = \frac{\mathrm{d}w}{\mathrm{d}t}$$

</div>
</div>

- It follows that $p = \frac{\mathrm{d}w}{\mathrm{d}t} = \frac{\mathrm{d}w}{\mathrm{d}q} \frac{\mathrm{d}q}{\mathrm{d}t} = vi$
	- If $p > 0$, power is delivered/absorbed by the element
	- If $p < 0$, power is being delivered by the element
- The voltage polarity and current direction must conform to the passive sign convention to be positive

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.11">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.11</span> <span class="theorem-callout-subtitle">(Passive Sign Convention)</span>.</div></div>
<div class="callout-content">

Satisfied when the current enters through the positive terminal of an element and $p = +vi$. If the current enters through the negative terminal, $p = -vi$.

</div>
</div>

- By the law of conservation of energy, the sum of power in a circuit must always be zero

$$\begin{align}
\sum p &= 0 \\
\text{Power Absorbed - Power Supplied} &= 0 \\
\text{Power Absorbed} &= \text{Power Supplied}
\end{align}
$$

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.12">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.12</span> <span class="theorem-callout-subtitle">(Energy)</span>.</div></div>
<div class="callout-content">

The capacity to do work, measured in joules (J).

</div>
</div>

- The energy absorbed/supplied by an element from time $t_0$ to time $t$ is

$$\begin{align}
w &= \int_{t_{0}}^{t} p \, \mathrm{d}t \\
&= \int_{t_{0}}^{t} vi \, \mathrm{d}t
\end{align}$$

- Power utility companies measure energy in watt-hours (Wh):

$$1 \text{Wh} = 3600 \text{J}$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.13">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.13</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Example 1.5</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;38]</span></cite>)
```py
In [6]: i_t = 5*cos(60*pi*t)

In [7]: v1 = 3*i_t

In [8]: v2 = 3*diff(i_t)

In [9]: (i_t * v1).subs(t, 3e-3)
Out[9]: 75*cos(0.18*pi)**2

In [10]: N(_)
Out[10]: 53.4667234336902

In [11]: (i_t * v2).subs(t, 3e-3)
Out[11]: -4500*pi*sin(0.18*pi)*cos(0.18*pi)

In [12]: N(_)
Out[12]: -6395.84554679224
```

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.14">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.14</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 1.5</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;39]</span></cite>)
```py
In [6]: i_t = 5*cos(60*pi*t)

In [13]: v1 = 6*i_t

In [14]: v2 = 6 + 10 * integrate(i_t, (t, 0, t))

In [15]: N((i_t * v1).subs(t, 5e-3))
Out[15]: 51.8237254218789

In [16]: N((i_t * v2).subs(t, 5e-3))
Out[16]: 18.2642465093081
```

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.15">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.15</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 1.6</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;40]</span></cite>)
Answer is interpreted as 33.12 kilowatt-hours
```py
In [18]: p = 12 * 115

In [19]: p * 24
Out[19]: 33120
```

</div>
</div>

## Circuit Elements {#circuit-elements}
- Active elements generate energy, do not
- There are two kinds of voltage/current sources: independent and dependent sources

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.16">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.16</span> <span class="theorem-callout-subtitle">(Ideal Independent Source)</span>.</div></div>
<div class="callout-content">

An active element that provides a specified voltage or current that is completely independent of other circuit elements.

</div>
</div>

- Ideal independent voltage source delivers whatever current is necessary to maintain its terminal voltage
	- And vice versa for ideal independent current source

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="01.17">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 01.17</span> <span class="theorem-callout-subtitle">(Ideal Dependent Source)</span>.</div></div>
<div class="callout-content">

An active element in which the source quantity is controlled by another voltage or current.

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="01.18">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 01.18</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 1.7</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;42]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/basic-concepts-2025-06-12-17-19-39.svg"><img src="/notes/excalidraw/basic-concepts-2025-06-12-17-19-39.svg" alt="Basic Concepts 2025-06-12 17.19.39" loading="lazy"></a></figure>

</div>
</div>
