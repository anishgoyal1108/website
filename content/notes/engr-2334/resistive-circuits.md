---
author: "Anish Goyal"
title: "Resistive Circuits"
description: "Voltage division is applicable for elements in series"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2334"
date: 2025-01-30T09:38:31
modified: 2025-04-02T10:32:03
readingtime: "3"
course: "ENGR 2334"
course_slug: "engr-2334"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 3
weight: 30
slug: "resistive-circuits"
links:
  - "/notes/engr-2334/current-law/"
  - "/notes/engr-2334/voltage-law/"
sources:
  - "Course slides, chapter 3: Resistive Circuits"
generated: true
---

## Kirchoff's Laws {#kirchoff-s-laws}

<div class="transclusion" data-source="04. Notes/Undergraduate Courses/ENGR 2334/Voltage Law.md">
<a class="transclusion-source" href="/notes/engr-2334/voltage-law/" title="Open Voltage Law"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

### Voltage Law {#voltage-law-embed1}

$$\sum V_{\text{drop}}=\sum V_{\text{rise}}$$

- The sum of voltages sources and drops for any loop is zero
	- Find the voltage/current for elements in series
	- Based on the Law of Conservation of Energy

</div>

<div class="transclusion" data-source="04. Notes/Undergraduate Courses/ENGR 2334/Current Law.md">
<a class="transclusion-source" href="/notes/engr-2334/current-law/" title="Open Current Law"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

### Current Law {#current-law-embed2}

$$\sum i_{\text{in}} = \sum i_{\text{out}}$$

- The sum of currents entering a node is zero
	- Find the current for a loop
	- Based on the Law of Conservation of Charge

</div>

### Examples {#examples}
<a class="zoom" href="/notes/img/example-1-kvl.png"><img src="/notes/img/example-1-kvl.png" alt="example 1 kvl" loading="lazy"></a>

<a class="zoom" href="/notes/img/example-1-kcl.png"><img src="/notes/img/example-1-kcl.png" alt="example 1 kcl" loading="lazy"></a>

<a class="zoom" href="/notes/img/example-2-kcl.png"><img src="/notes/img/example-2-kcl.png" alt="example 2 kcl" loading="lazy"></a>

<a class="zoom" href="/notes/img/example-2-kvl.png"><img src="/notes/img/example-2-kvl.png" alt="example 2 kvl" loading="lazy"></a>

<a class="zoom" href="/notes/img/example-2-kvl-2.png"><img src="/notes/img/example-2-kvl-2.png" alt="example 2 kvl 2" loading="lazy"></a>

<a class="zoom" href="/notes/img/example-3-problem-statement.png"><img src="/notes/img/example-3-problem-statement.png" alt="example 3 problem statement" loading="lazy"></a>

<a class="zoom" href="/notes/img/example-3-kcl.png"><img src="/notes/img/example-3-kcl.png" alt="example 3 kcl" loading="lazy"></a>

<a class="zoom" href="/notes/img/example-3-kvl.png"><img src="/notes/img/example-3-kvl.png" alt="example 3 kvl" loading="lazy"></a>

## Voltage and Current Division {#voltage-and-current-division}

### Voltage Division {#voltage-division}
- Voltage division is applicable for elements in series

$$
V_{n} = V_{s}R_{n}\left(\sum_{i=1}^N R_{i}\right)^{-1}
$$

<a class="zoom" href="/notes/img/voltage-division.png"><img src="/notes/img/voltage-division.png" alt="voltage division" loading="lazy"></a>

#### Examples {#examples-1}
<a class="zoom" href="/notes/img/voltage-division-example.png"><img src="/notes/img/voltage-division-example.png" alt="voltage division example" loading="lazy"></a>

<a class="zoom" href="/notes/img/voltage-division-example-2.png"><img src="/notes/img/voltage-division-example-2.png" alt="voltage division example 2" loading="lazy"></a>

<a class="zoom" href="/notes/img/voltage-division-example-3.png"><img src="/notes/img/voltage-division-example-3.png" alt="voltage division example 3" loading="lazy"></a>

### Current Division {#current-division}
- Current division is applicable for elements in parallel

$$
i_{n} = i_{s}\left(\frac{1}{R_{n}}\right)\left(\sum_{i=1}^N \frac{1}{R_{i}}\right)^{-1}
$$

<a class="zoom" href="/notes/img/current-division.png"><img src="/notes/img/current-division.png" alt="current division" loading="lazy"></a>

#### Examples {#examples-2}
<a class="zoom" href="/notes/img/current-division-example-1-problem-statement.png"><img src="/notes/img/current-division-example-1-problem-statement.png" alt="current division example 1 problem statement" loading="lazy"></a>

<a class="zoom" href="/notes/img/current-division-example-1-part-1.png"><img src="/notes/img/current-division-example-1-part-1.png" alt="current division example 1 part 1" loading="lazy"></a>

<a class="zoom" href="/notes/img/current-division-example-1-part-2.png"><img src="/notes/img/current-division-example-1-part-2.png" alt="current division example 1 part 2" loading="lazy"></a>

<a class="zoom" href="/notes/img/current-division-example-1-part-3.png"><img src="/notes/img/current-division-example-1-part-3.png" alt="current division example 1 part 3" loading="lazy"></a>

## Conductance {#conductance}
- Ohm's Law for conductance

$$i = GV$$

- Current division across branches can be done with conductance values
	- Use the formula for voltage division, but replace the resistances with conductances and voltage with current

$$i_{n} = i_{s}G_{n}\left(\sum_{i=1}^N G_{i}\right)^{-1}$$

- Same applies for voltage division for conductors in series

$$V_{n} = V_{s}\left(\frac{1}{G_{n}}\right)\left(\sum_{i=1}^N \frac{1}{G_{i}}\right)^{-1}$$

## Equivalent Ideal Sources {#equivalent-ideal-sources}

### Voltage Sources {#voltage-sources}
- Voltage sources may only be configured in series with one another
- Voltage sources in series have the same current
- Voltage sources in series can be combined to form one equivalent voltage source

<a class="zoom" href="/notes/img/equivalent-voltage-sources.png"><img src="/notes/img/equivalent-voltage-sources.png" alt="equivalent voltage sources" loading="lazy"></a>

### Current Sources {#current-sources}
- Current sources may only be configured in parallel with one another
- Current sources in parallel have the same voltage
- Current sources in parallel can be combined to form one equivalent current source

<a class="zoom" href="/notes/img/equivalent-current-source.png"><img src="/notes/img/equivalent-current-source.png" alt="equivalent current source" loading="lazy"></a>

## References {#references}
- [What is voltage law](https://www.schoolofpe.com/blog/2023/05/what-is-voltage-law.html)
- [Kirchoff's Voltage law](https://www.electronics-tutorials.ws/dccircuits/kirchhoffs-voltage-law.html)
- [Kirchoff's Current law](https://www.electronics-tutorials.ws/dccircuits/kirchhoffs-current-law.html)
- [Current source and dependent current sources](https://www.electronics-tutorials.ws/dccircuits/current-source.html)
- [Voltage source as independent and dependent sources](https://www.electronics-tutorials.ws/dccircuits/voltage-source.html)
- <span class="cite cite-ref">Course slides, chapter 3: Resistive Circuits</span>
