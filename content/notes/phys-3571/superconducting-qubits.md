---
author: "Anish Goyal"
title: "Superconducting Qubits"
description: "Qubits: two-level quantum systems"
tags:
  - "notes"
  - "physics"
  - "phys-3571"
date: 2026-04-28T12:46:18
modified: 2026-04-30T18:09:45
readingtime: "2"
course: "PHYS 3571"
course_slug: "phys-3571"
subject: "physics"
kind: "lecture"
ordinal: 11
weight: 110
slug: "superconducting-qubits"
links: []
sources: []
generated: true
---

## Quantum Information Processing: The Challenge {#quantum-information-processing-the-challenge}
- Qubits: two-level quantum systems
- We would like to be able to control these qubits with single unitary gates
- We need a lot of qubits that can talk to each other via entanglement for computation with a readout step that completes the computation (qubit readout)
- Conflicting requirements: *long* coherence, *fast* control and readout
	- We need the readout apparatus to be strongly-coupled with the circuit without losing coherence (phase/gate flips)
- The solution: Artificial atoms!

## Artificial Atoms {#artificial-atoms}

### Natural Atoms {#natural-atoms}
- Natural atoms have *sharp* energy levels, and we can select two of those levels to be our basis set
	- The great thing about these energy levels is that their energy spacing is distinct, and they each correspond to some transition frequency $\hbar\omega$
	- We can control the internal states of these atoms by shining lasers tuned at the transition frequency; the dipole moment of the atom will couple to the electric field of the laser
	- The hyperfine levels of $^{9}Be_+$ have long relaxation and dephasing times
		- $T_1 \sim \text{a few years} \ \ \ T_2 \sim 10 \text{ s}$
	- Reasonably short $\pi$-pulse time (preparing the superposition) $\sim 5 \mu s$
	- Low error per gate: $\sim 0.48 \%$ 

### Our Toolkit for Artificial Atoms {#our-toolkit-for-artificial-atoms}
- Regular circuit elements: wires, inductors, capacitors (and resistors?)
- We ensure that we are using superconducting wires, inductors, and capacitors, as we don't want to lose any energy (as heat), which will collapse the quantum state of the system
- Considering an LC circuit:
	- The total energy Hamiltonian is the sum of the Coulomb energy (how much energy is charging the capacitor) and the flux linkage energy (how much magnetic flux is passing through the solenoid)

$$H = \frac{Q^2}{2C} + \frac{\Phi^2}{2L}$$

- The flux energy can be represented as a harmonic oscillator with the harmonic frequency $\frac{1}{\sqrt{ LC }}$ equal to the transition frequency from $\ket{0}$ to $\ket{1}$ when looking at the energy vs flux graph

## Circuit QED {#circuit-qed}
- 

## Implementing 2-Qubit Algorithms {#implementing-2-qubit-algorithms}
- 

## Future Direction/Challenges {#future-direction-challenges}
- 

## References {#references}
- <a class="video-link" href="https://www.youtube.com/watch?v=t5nxusm_Umk">▶ Watch on YouTube</a>
- <a class="video-link" href="https://www.youtube.com/watch?v=t5nxusm_Umk">▶ Watch on YouTube</a>
