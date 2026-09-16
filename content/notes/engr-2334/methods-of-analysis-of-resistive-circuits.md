---
author: "Anish Goyal"
title: "Methods of Analysis of Resistive Circuits"
description: "A method to obtain element and node voltages in a circuit"
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2334"
date: 2025-02-06T19:09:50
modified: 2025-04-03T02:54:10
readingtime: "4"
course: "ENGR 2334"
course_slug: "engr-2334"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 4
weight: 40
slug: "methods-of-analysis-of-resistive-circuits"
links:
  - "/notes/engr-2334/current-law/"
sources:
  - "Course slides, chapter 4: Methods of Analysis of Resistive Circuits"
generated: true
---

## Nodal Analysis {#nodal-analysis}
- A method to obtain element and node voltages in a circuit
- One node is the *reference node*, which supplies GND and is taken to be 0 V
- For $n$ nodes, there are $n-1$ nodal equations

### Procedure {#procedure}
1. Choose a good reference node location
2. Draw the nodes for the locations you want to find
3. Express the voltage of each circuit element in terms of two node voltages
	- Which is just $\Delta v = v_{1} - v_{2}$, assuming the circuit element lies between $v_1$ and $v_2$ 
4. Rewrite this expression for current ($i = GV$ or $i = \frac{\Delta v}{R}$) using Ohm's Law
5. Apply <a class="internal-link" href="/notes/engr-2334/current-law/">Current Law</a> to each node (excluding reference node)
6. Solve the system of linear equations for each node voltage via substitution

### Example {#example}
<a class="zoom" href="/notes/img/nodal-analysis-example-1.png"><img src="/notes/img/nodal-analysis-example-1.png" alt="nodal analysis example 1" loading="lazy"></a>

### Independent Voltage Sources {#independent-voltage-sources}
- Adding a voltage source adds a voltage constraint to the system (one less KCL equation needed)
- Nodes directly in front of a voltage source have the same nodal voltage as that voltage source

#### Supernodes {#supernodes}
- If there exists a voltage source between two nodes, then they combine to form a **supernode**
- The supernode may be analyzed with KCL like normal reference nodes
	- However, the sum of the currents entering both reference nodes must equal the sum of the currents exiting both reference nodes

<a class="zoom" href="/notes/img/supernodes.png"><img src="/notes/img/supernodes.png" alt="supernodes" loading="lazy"></a>

##### Example {#example-1}

<a class="zoom" href="/notes/img/nodal-analysis-supernode-example-1.png"><img src="/notes/img/nodal-analysis-supernode-example-1.png" alt="nodal analysis supernode example 1" loading="lazy"></a>

#### Voltage Source Equation {#voltage-source-equation}
- Recall that voltages in series can be added together
- Therefore, the final voltage in a series of unknown voltages will equal the sum of voltages that came become it.
	- This is generalizable for any voltage source between two reference nodes; in the diagram below, $V_1 = V_2 + V_A$:
<a class="zoom" href="/notes/img/nodal-analysis.png"><img src="/notes/img/nodal-analysis.png" alt="nodal analysis" loading="lazy"></a>
- The resulting equation is known as the **constraint equation**

### Dependent Voltage Sources {#dependent-voltage-sources}
- When a **dependent** (or **controlled**) current or voltage source is present, an additional equation is needed to express the controlling variable in terms of node voltages

	1. If the dependent source is a **current source**, include it directly in the current matrix ($\mathbf{i}$)
	2. If the dependent source is a **voltage source**, it either:
	    - Creates a **supernode**, requiring an extra equation
	    - Adds a constraint equation relating node voltages

#### Example {#example-2}
<a class="zoom" href="/notes/img/nodal-analysis-dependent-source-example.png"><img src="/notes/img/nodal-analysis-dependent-source-example.png" alt="nodal analysis dependent source example" loading="lazy"></a>

### Matrix Method {#matrix-method}
- It is possible to solve for voltages **directly by inspection** using a **conductance matrix**
- For $n$ nodes, you will have an $n \times n$ symmetrical conductance matrix that is laid as follows:

$$
{\begin{pmatrix}G_{11}&G_{12}&\cdots &G_{1N}\\G_{21}&G_{22}&\cdots &G_{2N}\\\vdots &\vdots &\ddots &\vdots \\G_{N1}&G_{N2}&\cdots &G_{NN}\end{pmatrix}}{\begin{pmatrix}v_{1}\\v_{2}\\\vdots \\v_{N}\end{pmatrix}}={\begin{pmatrix}i_{1}\\i_{2}\\\vdots \\i_{N}\end{pmatrix}}
$$

or simply $\mathbf {Gv} =\mathbf {i}$, where:
	- G is the **conductance matrix**, constructed as:
	    - *Diagonal elements* $G_{kk}$​ are the sum of conductances connected to node $k$
	    - *Off-diagonal elements* $G_{kj}$​ are the **negative conductance** between nodes $k$ and $j$
	- $\mathbf{v}$ is the vector of unknown **node voltages**
	- $\mathbf{i}$ is the vector of known **current injections** at each node
- Thus, the final solution is $\mathbf{v}=\mathbf{G}^{-1}\mathbf{i}$
- *Cannot be used* when there is a voltage constraint or supernode; therefore, only good when there are independent current sources

## Mesh Analysis {#mesh-analysis}
- A mesh is a loop that has no loops within it
- For $N$ meshes, we write $N$ KVL equations
- Write voltage drops in terms of mesh currents and resistances

### Shared Loop Currents {#shared-loop-currents}
<a class="zoom" href="/notes/img/shared-loop-currents.png"><img src="/notes/img/shared-loop-currents.png" alt="shared loop currents" loading="lazy"></a>

### Examples {#examples}
<a class="zoom" href="/notes/img/mesh-analysis-system-of-equations-example.png"><img src="/notes/img/mesh-analysis-system-of-equations-example.png" alt="mesh analysis system of equations example" loading="lazy"></a>

<a class="zoom" href="/notes/img/mesh-analysis-system-of-equations-example-2.png"><img src="/notes/img/mesh-analysis-system-of-equations-example-2.png" alt="mesh analysis system of equations example 2" loading="lazy"></a>

<a class="zoom" href="/notes/img/voltmeter-mesh-analysis-simple-example.png"><img src="/notes/img/voltmeter-mesh-analysis-simple-example.png" alt="voltmeter mesh analysis simple example" loading="lazy"></a>

### Independent Current Sources {#independent-current-sources}
- For $N_c$ current sources, you have $N_c$ current equations relating the current source to 1 or more mesh currents

<a class="zoom" href="/notes/img/current-source-with-single-mesh-current.png"><img src="/notes/img/current-source-with-single-mesh-current.png" alt="current source with single mesh current" loading="lazy"></a>

#### Supermeshes {#supermeshes}
- If there exists a current source between two mesh currents, you have to construct a supermesh
- Total equations: $N-N_c$

<a class="zoom" href="/notes/img/current-source-with-two-mesh-currents-and-supermesh-definition.png"><img src="/notes/img/current-source-with-two-mesh-currents-and-supermesh-definition.png" alt="current source with two mesh currents and supermesh definition" loading="lazy"></a>

#### Examples {#examples-1}
<a class="zoom" href="/notes/img/mesh-analysis-with-current-source-no-supermesh-example.png"><img src="/notes/img/mesh-analysis-with-current-source-no-supermesh-example.png" alt="mesh analysis with current source no supermesh example" loading="lazy"></a>

<a class="zoom" href="/notes/img/mesh-analysis-with-current-source-supermesh-example.png"><img src="/notes/img/mesh-analysis-with-current-source-supermesh-example.png" alt="mesh analysis with current source supermesh example" loading="lazy"></a>

<a class="zoom" href="/notes/img/supermesh-example.png"><img src="/notes/img/supermesh-example.png" alt="supermesh example" loading="lazy"></a>

<a class="zoom" href="/notes/img/volmeter-mesh-analysis-with-current-source-no-supermesh-example.png"><img src="/notes/img/volmeter-mesh-analysis-with-current-source-no-supermesh-example.png" alt="volmeter mesh analysis with current source no supermesh example" loading="lazy"></a>

### Dependent Current Sources {#dependent-current-sources}
- Write the dependent source value in terms of the mesh currents
- Total equations: $N-N_c$ for $N_c$ sources

#### Examples {#examples-2}
<a class="zoom" href="/notes/img/mesh-analysis-dependent-source-example-1.png"><img src="/notes/img/mesh-analysis-dependent-source-example-1.png" alt="mesh analysis dependent source example 1" loading="lazy"></a>

<a class="zoom" href="/notes/img/mesh-analysis-dependent-source-example-2.png"><img src="/notes/img/mesh-analysis-dependent-source-example-2.png" alt="mesh analysis dependent source example 2" loading="lazy"></a>

<a class="zoom" href="/notes/img/mesh-analysis-dependent-sources-supermesh-example.png"><img src="/notes/img/mesh-analysis-dependent-sources-supermesh-example.png" alt="mesh analysis dependent sources supermesh example" loading="lazy"></a>

## References {#references}
- [Nodal analysis](https://en.wikipedia.org/wiki/Nodal_analysis)
- [Mesh analysis](https://en.wikipedia.org/wiki/Mesh_analysis)
- <span class="cite cite-ref">Course slides, chapter 4: Methods of Analysis of Resistive Circuits</span>
