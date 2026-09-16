---
author: "Anish Goyal"
title: "AC Circuit Analysis"
description: "Assumptions for phasor analysis:"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3345"
date: 2025-06-24T11:29:58
modified: 2025-07-24T03:24:08
readingtime: "7"
course: "EENG 3345"
course_slug: "eeng-3345"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 3
weight: 30
slug: "ac-circuit-analysis"
links: []
sources:
  - "Course handout 3: Analysis of AC Circuits Using Phasor Approach"
generated: true
---

## Phasor Analysis of AC Circuits {#phasor-analysis-of-ac-circuits}
- Assumptions for phasor analysis:
  - The system is Linear Time-Invariant (LTI) with a sinusoidal input
  - The system has no switching behavior and has reached steady-state at $t=0$
- Therefore, the complete response is composed completely of the steady-state response

## AC Circuits {#ac-circuits}
- Current and voltage vary sinusoidally with time  

$$
\begin{align}
v(t) &= V_m \cos(\omega t + \phi) \\
i(t) &= I_m \cos(\omega t + \theta)
\end{align}
$$

## Phasor Analysis of AC Circuits {#phasor-analysis-of-ac-circuits-1}
- Steps:
  1. Convert time-domain sources to phasors
  2. Use Ohm's Law, KVL, KCL in phasor domain
  3. Solve for phasor voltages/currents
  4. Convert phasors back to time domain
- Shortcut: The source current is $i(t) = \frac{V_{m}}{|Z_{\text{eq}}|}\cos(\omega t+\phi+\theta)$ where
	- $\theta = \arg(Y_{\text{eq}})$ for parallel
	- $\theta = -\arg(Y_{\text{eq}})$ for series

### Current Through RL Series Circuit {#current-through-rl-series-circuit}

Given:  
$v(t) = V_m \cos(\omega t + \phi)$

Impedance:  
$Z = R + j\omega L$

Phasor voltage:  
$\tilde{V} = V_m \angle \phi$

Phasor current:  
$\tilde{I} = \frac{\tilde{V}}{Z} = \frac{V_m \angle \phi}{R + j\omega L}$

Convert to polar form:  
$|\tilde{I}| = \frac{V_m}{\sqrt{R^2 + (\omega L)^2}}$  
$\angle \tilde{I} = \phi - \tan^{-1} \left( \frac{\omega L}{R} \right)$

Time-domain current:  

$$
i(t) = \frac{V_m}{\sqrt{R^2 + (\omega L)^2}} \cos\left( \omega t + \phi - \tan^{-1} \left( \frac{\omega L}{R} \right) \right)
$$

```py
In [1]: R, V, L, ω, φ = symbols('R V L ω φ')
In [2]: i = symbols('i')
In [9]: eq = Eq(i, V/(sqrt(R**2 + (ω*L)**2))*cos(ω*t+φ-atan(ω*L/R)))
In [15]: eq.subs({V:100, ω:100, φ:rad(30), R:10, L:0.1})
Out[15]:
                        ⎛                            π⎞
i = 7.07106781186548⋅cos⎜100⋅t - 0.785398163397448 + ─⎟
                        ⎝                            6⎠
```

### Current Through RC Series Circuit {#current-through-rc-series-circuit}

Given:  
$v(t) = V_m \cos(\omega t + \phi)$

Impedance:  
$Z = R - j\frac{1}{\omega C}$

Phasor voltage:  
$\tilde{V} = V_m \angle \phi$

Phasor current:  
$\tilde{I} = \frac{\tilde{V}}{Z} = \frac{V_m \angle \phi}{R - j\frac{1}{\omega C}}$

Convert to polar form:  
$|\tilde{I}| = \frac{V_m}{\sqrt{R^2 + \left( \frac{1}{\omega C} \right)^2}}$  
$\angle \tilde{I} = \phi + \tan^{-1} \left( \frac{1}{\omega RC} \right)$

Time-domain current:  

$$
i(t) = \frac{V_m}{\sqrt{R^2 + \left( \frac{1}{\omega C} \right)^2}} \cos\left( \omega t + \phi + \tan^{-1} \left( \frac{1}{\omega RC} \right) \right)
$$

```py
In [1]: R, V, C, ω, φ = symbols('R V C ω φ')
In [2]: i = symbols('i')
In [9]: eq = Eq(i, V/(sqrt(R**2 + (1/(ω*C))**2)) * cos(ω*t + φ + atan(1/(ω*R*C))))
In [11]: eq.subs({V:100, ω:100, φ:rad(30), R:10, C:100e-6})
Out[11]:
                         ⎛        π                   ⎞
i = 0.995037190209989⋅cos⎜100⋅t + ─ + 1.47112767430373⎟
                         ⎝        6                   ⎠
```

### Current Through RLC Series Circuit {#current-through-rlc-series-circuit}

Given:  
$v(t) = V_m \cos(\omega t + \phi)$

Impedance:  
$Z = R + j\omega L - j\frac{1}{\omega C} = R + j \left( \omega L - \frac{1}{\omega C} \right)$

Phasor voltage:  
$\tilde{V} = V_m \angle \phi$

Phasor current:  
$\tilde{I} = \frac{V_m \angle \phi}{R + j \left( \omega L - \frac{1}{\omega C} \right)}$

Magnitude and phase:  
$|\tilde{I}| = \frac{V_m}{\sqrt{R^2 + \left( \omega L - \frac{1}{\omega C} \right)^2}}$  
$\angle \tilde{I} = \phi - \tan^{-1} \left( \frac{\omega L - \frac{1}{\omega C}}{R} \right)$

Time-domain current:  

$$
i(t) = \frac{V_m}{\sqrt{R^2 + \left( \omega L - \frac{1}{\omega C} \right)^2}} \cos\left( \omega t + \phi - \tan^{-1} \left( \frac{\omega L - \frac{1}{\omega C}}{R} \right) \right)
$$

```py
In [1]: R, V, L, C, ω, φ = symbols('R V L C ω φ')
In [2]: i = symbols('i')
In [3]: eq = Eq(i, V/(sqrt(R**2 + (ω*L - 1/(ω*C))**2)) * cos(ω*t + φ - atan((ω*L - 1/(ω*C))/R)))
In [6]: eq.subs({V:100, ω:100, φ:rad(30), R:10, L:0.1, C:100e-6})
Out[6]:
                        ⎛        π                 ⎞
i = 1.10431526074847⋅cos⎜100⋅t + ─ + 1.460139105621⎟
                        ⎝        6                 ⎠
```

### Current Through RL Parallel Circuit {#current-through-rl-parallel-circuit}

Given:  
$v(t) = V_m \cos(\omega t + \phi)$

Impedances:  
- Resistor: $Z_R = R$  
- Inductor: $Z_L = j\omega L$

Admittances:  
- $Y_R = \dfrac{1}{R}$  
- $Y_L = \dfrac{1}{j\omega L} = -j \dfrac{1}{\omega L}$

Total admittance:  

$$
Y_{eq} = Y_R + Y_L = \dfrac{1}{R} - j\dfrac{1}{\omega L}
$$

Phasor voltage:  
$\tilde{V} = V_m \angle \phi$

Phasor current:  

$$
\tilde{I} = \tilde{V}\,Y_{eq} = V_m \angle \phi \left( \dfrac{1}{R} - j\dfrac{1}{\omega L} \right)
$$

Magnitude and phase:  

$$
|\tilde{I}| = \dfrac{V_m}{\sqrt{\left(\dfrac{1}{R}\right)^2 + \left(\dfrac{1}{\omega L}\right)^2}} ,
\qquad
\angle \tilde{I} = \phi - \tan^{-1}\!\left( \dfrac{1}{\omega L R} \right)
$$

Time-domain current:  

$$
i(t) = \dfrac{V_m}{\sqrt{\left(\dfrac{1}{R}\right)^2 + \left(\dfrac{1}{\omega L}\right)^2}}
\cos\!\Bigl( \omega t + \phi - \tan^{-1}\!\left( \dfrac{1}{\omega L R} \right) \Bigr)
$$

---

### Current Through RC Parallel Circuit {#current-through-rc-parallel-circuit}

Given:  
$v(t) = V_m \cos(\omega t + \phi)$

Impedances:  
- Resistor: $Z_R = R$  
- Capacitor: $Z_C = -j\dfrac{1}{\omega C}$

Admittances:  
- $Y_R = \dfrac{1}{R}$  
- $Y_C = j\omega C$

Total admittance:  

$$
Y_{eq} = Y_R + Y_C = \dfrac{1}{R} + j\omega C
$$

Phasor voltage:  
$\tilde{V} = V_m \angle \phi$

Phasor current:  

$$
\tilde{I} = \tilde{V}\,Y_{eq} = V_m \angle \phi \left( \dfrac{1}{R} + j\omega C \right)
$$

Magnitude and phase:  

$$
|\tilde{I}| = \dfrac{V_m}{\sqrt{\left(\dfrac{1}{R}\right)^2 + (\omega C)^2}} ,
\qquad
\angle \tilde{I} = \phi + \tan^{-1}\!\bigl( \omega R C \bigr)
$$

Time-domain current:  

$$
i(t) = \dfrac{V_m}{\sqrt{\left(\dfrac{1}{R}\right)^2 + (\omega C)^2}}
\cos\!\Bigl( \omega t + \phi + \tan^{-1}\!\bigl( \omega R C \bigr) \Bigr)
$$

---

### Current Through RLC Parallel Circuit {#current-through-rlc-parallel-circuit}

Given:  
$v(t) = V_m \cos(\omega t + \phi)$

Impedances:  
- $Z_R = R$  
- $Z_L = j\omega L$  
- $Z_C = -j\dfrac{1}{\omega C}$

Admittances:  
- $Y_R = \dfrac{1}{R}$  
- $Y_L = -j\dfrac{1}{\omega L}$  
- $Y_C = j\omega C$

Total admittance:  

$$
Y_{eq} = \dfrac{1}{R} + j\!\left( \omega C - \dfrac{1}{\omega L} \right)
$$

Phasor voltage:  
$\tilde{V} = V_m \angle \phi$

Phasor current:  

$$
\tilde{I} = \tilde{V}\,Y_{eq} =
V_m \angle \phi
\left( \dfrac{1}{R} + j\!\left( \omega C - \dfrac{1}{\omega L} \right) \right)
$$

Magnitude and phase:  

$$
|\tilde{I}| = \dfrac{V_m}{
\sqrt{ \left(\dfrac{1}{R}\right)^2 + \left( \omega C - \dfrac{1}{\omega L} \right)^2 }
},
\qquad
\angle \tilde{I} = \phi + \tan^{-1}\!\Bigl( R \bigl( \omega C - \dfrac{1}{\omega L} \bigr) \Bigr)
$$

Time-domain current:  

$$
i(t) = \dfrac{V_m}{
\sqrt{ \left(\dfrac{1}{R}\right)^2 + \left( \omega C - \dfrac{1}{\omega L} \right)^2 }
}
\cos\!\Bigl(
\omega t + \phi + \tan^{-1}\!\Bigl( R \bigl( \omega C - \dfrac{1}{\omega L} \bigr) \Bigr)
\Bigr)
$$

## Impedance {#impedance}
- Equivalent of resistance for AC: $Z = \frac{V}{I}$
- Complex value: magnitude and phase

Resistor: $Z = R$  
Inductor: $Z = j \omega L$  
Capacitor: $Z = -j \frac{1}{\omega C}$  
Units: Ohms ($\Omega$)

## Admittance {#admittance}
- Reciprocal of impedance: $Y = \frac{1}{Z}$
- Used for parallel circuits: $I = YV$
- Units: Siemens (S)

## Resonant Frequency {#resonant-frequency}

In series RLC: resonance when net reactance is zero

$$
\omega_0 L = \frac{1}{\omega_0 C}
$$

Solve for $\omega_0$:

$$
\omega_0 = \frac{1}{\sqrt{LC}}
$$

In Hz:

$$
f_0 = \frac{\omega_0}{2\pi} = \frac{1}{2\pi \sqrt{LC}}
$$

At resonance:
- $Z = R$
- Current is maximized
- Inductor and capacitor voltages cancel

## Combo Circuit Analysis {#combo-circuit-analysis}

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.1</span>.</div></div>
<div class="callout-content">

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-ac-circuit-analysis-2025-06-25-10-39-29.svg"><img src="/notes/excalidraw/03-ac-circuit-analysis-2025-06-25-10-39-29.svg" alt="03 AC Circuit Analysis 2025-06-25 10.39.29" loading="lazy"></a></figure>

</div>
</div>

## AC Bridge Circuit {#ac-bridge-circuit}
- Bridge circuits are used to determine unknown impedances, with four impedances arranged in a bridge configuration
- The bridge is *balanced* when the ratio of impedances in one branch equals the ratio in the other branch
	- For the circuit below:

$$\frac{Z_{1}}{Z_{2}} = \frac{Z_{3}}{Z_{X}} \implies Z_{X} = Z_{3}\left(\frac{Z_{2}}{Z_{1}}\right)$$

<a class="zoom" href="/notes/img/ac-bridge-circuit-diagram.png"><img src="/notes/img/ac-bridge-circuit-diagram.png" alt="ac bridge circuit diagram" loading="lazy"></a>

### Unknown Impedance Derivation {#unknown-impedance-derivation}

$$\begin{align}
Z_{X} &= R_{3}\left(\frac{\frac{1-j\omega R_{2}C_{2}}{\omega C_{2}}}{R_{1}+j\omega L_{1}}\right) \\
&=R_{3}\left(\frac{1-j\omega R_{2}C_{2}}{\omega C_{2}R_{1}+j\omega^2C_{2}L_{1}}\right)
\end{align}$$

### Source Current Derivation {#source-current-derivation}

$$\begin{align}
V &= Z_{\text{total}}I \\
&=((Z_{1}+Z_{2}) \ || \ (Z_{3}+Z_{X}))I \\
&=\frac{(Z_{1}+Z_{2})(Z_{3}+Z_{X})}{Z_{1}+Z_{2}+Z_{3}+Z_{X}} \\
\implies I &= V\left(\frac{Z_{1}+Z_{2}+Z_{3}+Z_{X}}{(Z_{1}+Z_{2})(Z_{3}+Z_{X})}\right)
\end{align}$$

## Norton/Thevenin Equivalent Examples {#norton-thevenin-equivalent-examples}

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="03.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 03.2</span>.</div></div>
<div class="callout-content">

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/03-ac-circuit-analysis-2025-06-27-11-17-56.svg"><img src="/notes/excalidraw/03-ac-circuit-analysis-2025-06-27-11-17-56.svg" alt="03 AC Circuit Analysis 2025-06-27 11.17.56" loading="lazy"></a></figure>

</div>
</div>

## References {#references}
- <span class="cite cite-ref">Course handout 3: Analysis of AC Circuits Using Phasor Approach</span>
