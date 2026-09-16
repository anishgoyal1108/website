---
author: "Anish Goyal"
title: "Methods of Analysis"
description: "A procedure for analyzing circuits using node voltages as variables"
tags:
  - "notes"
  - "electrical-engineering"
  - "electric-circuits"
date: 2025-06-21T19:33:13
modified: 2026-07-29T17:27:25
readingtime: "7"
course: "Fundamentals of Electric Circuits (Sadiku)"
course_slug: "electric-circuits"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 3
weight: 30
slug: "methods-of-analysis"
links: []
sources:
  - "Alexander & Sadiku, Fundamentals of Electric Circuits"
generated: true
---

## Nodal Analysis {#nodal-analysis}
- A procedure for analyzing circuits using node voltages as variables
- It's better to use node voltages instead of circuit elements because it reduces the number of equations
- Goal is to determine the node voltages using KCL, which are defined to be positive wrt ground
- Steps:
	1. Assign a ground node with $v = 0$ and $v_{i}$ for the remaining $n-1$ nodes
	2. Apply KCL to each $n-1$ nonreference node. Express the currents in terms of the node voltages
	3. Solve the resultant system
- Since current flows from a **higher** to **lower** potential in a resistor, the current is

$$i = \frac{v_{\text{higher}}-v_{\text{lower}}}{R} \ \text{or} \ G(v_{\text{higher}}-v_{\text{lower}})$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.1</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 3.1</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;109]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/methods-of-analysis-2025-06-21-20-13-28.svg"><img src="/notes/excalidraw/methods-of-analysis-2025-06-21-20-13-28.svg" alt="Methods of Analysis 2025-06-21 20.13.28" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.2</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 3.2</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;112]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/methods-of-analysis-2025-06-21-21-33-52.svg"><img src="/notes/excalidraw/methods-of-analysis-2025-06-21-21-33-52.svg" alt="Methods of Analysis 2025-06-21 21.33.52" loading="lazy"></a></figure>

</div>
</div>

### Nodal Analysis with Voltage Sources {#nodal-analysis-with-voltage-sources}
- When dealing with voltage sources, we must examine two cases:
	1. The voltage source is between ground and a nonreference node. Then, the voltage at the nonreference node is equal to the voltage of the voltage source
	2. The voltage source is between two nonreference nodes. Then, the two nodes form a *supernode*, and we must apply both KCL and KVL to determine the node voltages

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.3</span> <span class="theorem-callout-subtitle">(Supernode)</span>.</div></div>
<div class="callout-content">

Formed by enclosing a voltage source connected between two nonreference nodes and any elements connected in parallel with it. Has the following properties:
1. The enclosed voltage source provides a constraint equation, which is derived using KVL
2. Has no voltage of its own
3. Requires both KCL and KVL

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.4</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 3.3</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;114]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/methods-of-analysis-2025-06-22-00-09-00.svg"><img src="/notes/excalidraw/methods-of-analysis-2025-06-22-00-09-00.svg" alt="Methods of Analysis 2025-06-22 00.09.00" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.5</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 3.4</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;117]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/methods-of-analysis-2025-06-22-01-30-21.svg"><img src="/notes/excalidraw/methods-of-analysis-2025-06-22-01-30-21.svg" alt="Methods of Analysis 2025-06-22 01.30.21" loading="lazy"></a></figure>

</div>
</div>

## Mesh Analysis {#mesh-analysis}
- Use KVL to find unknown currents using mesh currents as circuit variables
- A mesh is a loop that does not contain any other loop within it
- Only applicable to planar circuits (no branches crossing one another)
- Steps:
	1. Assign mesh currents $i_{i}$ to the $n$ meshes
	2. Apply KVL to each mesh. Express the voltages in terms of the mesh currents
	3. Solve the resultant system
- For each KVL equation:
	- The coefficient of the mesh current being solved is positive and equal to the sum of all resistances in the mesh
	- The coefficient of any adjacent mesh current is the negative of the sum of resistances shared between the mesh and the shared mesh
	- All voltage rises may be summed and written on the RHS (*i.e.*, voltage sources)
- Use capital $I$ for branch currents and lowercase $i$ for mesh currents

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.6</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 3.5</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;120]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/methods-of-analysis-2025-06-22-22-43-11.svg"><img src="/notes/excalidraw/methods-of-analysis-2025-06-22-22-43-11.svg" alt="Methods of Analysis 2025-06-22 22.43.11" loading="lazy"></a></figure>

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.7</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 3.6</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;122]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/methods-of-analysis-2025-06-22-22-45-58.svg"><img src="/notes/excalidraw/methods-of-analysis-2025-06-22-22-45-58.svg" alt="Methods of Analysis 2025-06-22 22.45.58" loading="lazy"></a></figure>

</div>
</div>

### Mesh Analysis with Current Sources {#mesh-analysis-with-current-sources}
- When dealing with current sources, we must examine two cases:
	1. The current source is exclusive to one mesh. Then, the mesh current is equal to the current source
	2. The current source is shared between two meshes. Then, the two meshes form a *supermesh* by excluding the branch with the current node and any elements in series with it. Perform KVL on the supermesh and apply KCL to a node where the two meshes intersect

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="03.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 03.8</span> <span class="theorem-callout-subtitle">(Supermesh)</span>.</div></div>
<div class="callout-content">

Results when two meshes have a current source in common. Has the following properties:
1. The current source provides a constraint equation for the mesh currents using KCL
2. Has no current of its own
3. Requires both KVL and KCL

</div>
</div>

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.9</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 3.7</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;124]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/methods-of-analysis-2025-06-22-22-59-34.svg"><img src="/notes/excalidraw/methods-of-analysis-2025-06-22-22-59-34.svg" alt="Methods of Analysis 2025-06-22 22.59.34" loading="lazy"></a></figure>

</div>
</div>

## Analysis by Inspection {#analysis-by-inspection}

### Nodal Analysis by Inspection {#nodal-analysis-by-inspection}
- KCL not needed if all the sources are independent current sources; the resulting system is $$\mathbf{Gv = i}$$ with $\mathbf{G}$ being the conductance matrix, $\mathbf{v}$ being the output vector, and $\mathbf{i}$ being the current matrix/input vector
- For the conductance matrix:
	- The $i$th diagonal term is the sum of the conductances in branches connected to the $i$th node
	- The off-diagonal terms are the negatives of the sum of the conductance in the branches connected between two nodes $i$ and $j$
- For the current matrix:
	- The $n$th term is the sum of the currents entering the $n$th node
- If a circuit with independent current sources has $N$ nonreference nodes, the system in terms of the conductances is:

$$
\begin{bmatrix}
G_{11} & G_{12} & \dots & G_{1j} \\
G_{21} & G_{22} & \dots & G_{2j} \\
\vdots & \vdots  & \vdots & \vdots \\
G_{i 1} & G_{i 2} & \dots & G_{ij}
\end{bmatrix} \begin{bmatrix}
v_{1} \\ v_{2} \\ \vdots \\ v_{N}
\end{bmatrix} = \begin{bmatrix}
i_{1} \\ i_{2} \\ \vdots \\ i_{N}
\end{bmatrix}
$$

- Shortcut: there is symmetry along the diagonal, so all the off-diagonals across from one another should be equal

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.10</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 3.8</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;127]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/methods-of-analysis-2025-06-23-11-05-44.svg"><img src="/notes/excalidraw/methods-of-analysis-2025-06-23-11-05-44.svg" alt="Methods of Analysis 2025-06-23 11.05.44" loading="lazy"></a></figure>

</div>
</div>

### Mesh Analysis by Inspection {#mesh-analysis-by-inspection}
- Matrix is of the form $$\mathbf{Ri = v}$$ where:
	- $R_{ii}$ = Sum of resistances in mesh $i$
	- $R_{ij} = R_{ji} =$ Negative of sum of resistances in common with meshes $i$ and $j$
	- $i_{N}$ = Unknown mesh current up to the $N$th mesh
	- $v_{N}$ = Sum of all independent voltage sources up to the $N$th mesh
- Thus, the generalized matrix is:

$$
\begin{bmatrix}
R_{11} & R_{12} & \dots & R_{1j} \\
R_{21} & R_{22} & \dots & R_{2j} \\
\vdots & \vdots & \ddots & \vdots \\
R_{i1} & R_{i2} & \dots & R_{ij}
\end{bmatrix}
\begin{bmatrix}
i_1 \\ i_2 \\ \vdots \\ i_N
\end{bmatrix}
=
\begin{bmatrix}
v_1 \\ v_2 \\ \vdots \\ v_N
\end{bmatrix}
$$

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.11">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.11</span>.</div></div>
<div class="callout-content">

(<cite class="cite cite-quote"><q>Practice Problem 3.9</q> <span class="cite-src">[Alexander &amp; Sadiku, <em>Fundamentals of Electric Circuits</em>, 7th ed., p.&nbsp;128]</span></cite>)

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/methods-of-analysis-2025-06-23-16-42-01.svg"><img src="/notes/excalidraw/methods-of-analysis-2025-06-23-16-42-01.svg" alt="Methods of Analysis 2025-06-23 16.42.01" loading="lazy"></a></figure>

</div>
</div>
