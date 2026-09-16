---
author: "Anish Goyal"
title: "Trapped-Ion Qubits"
description: "Optical qubit"
tags:
  - "notes"
  - "physics"
  - "phys-3571"
date: 2026-04-14T11:08:24
modified: 2026-04-28T12:47:21
readingtime: "4"
course: "PHYS 3571"
course_slug: "phys-3571"
subject: "physics"
kind: "lecture"
ordinal: 12
weight: 120
slug: "trapped-ion-qubits"
links: []
sources: []
generated: true
---

## Optical Vs Hyperfine Qubits {#optical-vs-hyperfine-qubits}
### The Ca+ Ion {#the-ca-ion}
- Optical qubit
- The ionization of Ca+ allows it to be manipulated via electromagnetic fields
- Structure of the electron shell orbitals is determined by the Pauling Diagram
	- The principal quantum numbers determine the electron configuration
- The bandgap between the ket vectors are in the 400~790 THz range in the visible light spectrum

### Hydrogen Atom {#hydrogen-atom}
- Hyperfine atom
- Dipole-dipole interactions create hyperfine splitting states which are natural Bell states
- Triplet state: the states are either aligned or symmetrically coupled (Bell state)
- The energy bandgap is only 1 THz; but a smaller energy difference corresponds to a higher coherence time due to the Heisenberg uncertainty principle!
	- 10 min coherence (vs 1 second)
	- Tradeoff: harder to manipulate individual atoms

## Trapped Ions as Qubits {#trapped-ions-as-qubits}

### Ion Lattice in a Paul Trap {#ion-lattice-in-a-paul-trap}
- Uses a static magnetic field to trap ions in the environment
- 4 qubits, with each having a ground state $\ket{g_{k}}$ and excited state $\ket{e_k}$
	- When $\Delta E$ is equal to the electronic transition energy, can become excited
- Quantized phonon modes
	- Allow as a "bus-qubit" allowing quantum information to travel across the chain of ions for quantum computation
	- Each phonon mode has a ground and excited state per ion
- The phonon state is conserved in carrier transition
- Edge case: the laser frequency is increased/decreased by a vibrational quantum
	- Produces blue/red sidebands
- The computational Hilbert space is typically only the first two phonon modes
- Phonon mediatead coupling
	- The red laser induces lowering of the electronic state when the phonon bus is at $\ket{0_p}$
	- This action depends entirely on whether the qubit is in its ground state or excited state
- This is the foundation for universal quantum gates and multi-qubit operations

### Preparation {#preparation}
- Initialize the ions to their ground state
- Ensure all the phonons have the same transition energy
- Sideband cooling

## Encoding, Initialization, and Readout {#encoding-initialization-and-readout}

### Encoding {#encoding}
- In Ca+, the states are atomic orbitals
	- In the ground state, the highest energy level is the $4S_{1/2}$ orbital and represented as $\ket{0}$
	- The excited $3D_{5/2}$ state is $\ket{1}$
	- There is technically another energy level higher than $3D_{5/2}$, but it has such a low lifetime of just 7 ns, but it does appear relatively frequently. 
		- Electron dipole transitions are much more common than quadrapoles and other dipole interactions on the outer shell, hence why we use $3D_{5/2}$ instead of that one

### Initialization {#initialization}
- How to initialize all the qubits to $\ket{0}$?
	- Optical pumping
		- Drive the Ca+ to an auxiliary state that decays to the $4S_{1/2}$ orbital; can be repeated to make sure

### Readout {#readout}
- If it jumps from $\ket{0}$ to the really high 4P state, there is a fluorescent light beam that emits; and vice-versa (no light) if it's from $\ket{1}$ to really high 4P
	- This fluorescent light can be easily detected, hence we have our readout

## Scalable Quantum Hardware Criteria {#scalable-quantum-hardware-criteria}
- (also known as DiVincenzo's Criteria)
1. Scalable qubits
2. Long coherence times
3. Universal quanntum gates
4. Qubit initialization
5. Qubit measurement with high accuracy

## More on Phonons (the instructor's Elaboration) {#more-on-phonons-dr-the instructor-s-elaboration}
- They have to do with vibrations
- There are equilibrium positions, but the objects oscillate around those equilibrium positions
- Similar to solid (strongly-coupled) state of matter!
	- In solids, you actually have a lattice of singly-charged ions that are constantly exchanging electrons with one another, effectively canceling each other out
	- Each constriction of those ions cause waves of constrictions felt throughout the lattice that are also felt by the electrons that are being exchanged
		- These vibrations are quantized and thus referred to as phonons
- You need to have a vacuum. You can't do these in the air
	- Air is mostly made of diatomic nitrogen/oxygen, which has an average speed of ~170 m/s, so it's not really measurable in that space. In the words of the instructor: "It's like hitting an ant with a truck"
- 

## References {#references}
- <a class="video-link" href="https://www.youtube.com/watch?v=5qpXdGSLWig">▶ Watch on YouTube</a>
