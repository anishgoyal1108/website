---
author: "Anish Goyal"
title: "The Genesis of Fourier Analysis"
description: "Describes the behavior of basic oscillatory systems"
tags:
  - "notes"
  - "mathematics"
  - "math-4890"
date: 2024-10-17T17:41:17
modified: 2025-02-10T02:37:11
readingtime: "9"
course: "MATH 4890"
course_slug: "math-4890"
subject: "mathematics"
kind: "concept"
weight: 9003
slug: "the-genesis-of-fourier-analysis"
links:
  - "/notes/math-4890/d-alembert-s-formula/"
  - "/notes/math-4890/fundamental-tone/"
  - "/notes/math-4890/shm-derivation/"
  - "/notes/math-4890/wave-equation/"
sources: []
generated: true
---

## Simple Harmonic Motion {#simple-harmonic-motion}
- Describes the behavior of basic oscillatory systems
- A mass that is displaced from its initial equilibrium position and released undergoes **simple harmonic motion**.

<div class="transclusion" data-source="04. Notes/Undergraduate Courses/MATH 4190/SHM derivation.md">
<a class="transclusion-source" href="/notes/math-4890/shm-derivation/" title="Open SHM derivation"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

### SHM Derivation {#shm-derivation-embed1}
The restoring force of an ideal spring is $F_s = -ky(t)$. By Newton's 2nd Law:

$$-ky(t) = my''(t)$$

Since $c = \sqrt{\frac{k}{m}}$, the second order ODE becomes:

$$y''(t)+c^2y(t)=0$$

with a general solution of:

$$y(t)=a\cos{ct} + b\sin{ct}$$

If we are given initial position and velocity ($y(0)$ and $y'(0)$), the unique solution is given by:

$$y(t) = y(0)\cos{ct} + \frac{y'(0)}{c}\sin{ct}$$

And there are constants $A > 0$ and $\gamma \in \mathbb{R}$ such that:

$$y(t) = a\cos{ct}+b\sin{ct} = A\cos({ct-\phi})$$

where:
- $A = \sqrt{a^2 + b^2}$ and is the amplitude
- $c$ is the frequency
- $\phi$ is the phase
- $\frac{2\pi}{c}$ is the period

</div>

## Waves {#waves}
### Standing Wave {#standing-wave}
- Oscillate up and down
- Described by $y=u(x, t)=\phi(x)\psi(t)$, where:
	- $\phi(x)$ is the initial configuration of the wave
	- $\psi(t)$ is the amplifying factor of the wave, dependent on $t$
- Suggests separation of variables, since it's a product of two functions

<a class="zoom" href="/notes/img/standing-wave.gif"><img src="/notes/img/standing-wave.gif" alt="standing wave" loading="lazy"></a>

### Traveling Wave {#traveling-wave}
- Waves that move at a constant velocity, $c$, in a particular direction
- Represented by an initial profile $F(x)$ that is displaced by $ct$ units as $t$ grows
- $u(x, t) = F(x-ct)$

<a class="zoom" href="/notes/img/traveling-wave.gif"><img src="/notes/img/traveling-wave.gif" alt="traveling wave" loading="lazy"></a>

### The Vibrating String Problem {#the-vibrating-string-problem}
#### Background {#background}
Consider a vibrating string stretched from $x = 0$ to $x = L$ with a vertical displacement given by the function $y=u(x, t)$. The string has a tension coefficient $\tau$ and density coefficient $\rho$. Derive the differential equation that governs this function.

#### Deriving the Wave Equation {#deriving-the-wave-equation}
Divide the string into $N$ uniformly distributed particle masses. The $n^{th}$ particle has its $x$-coordinate at $x_{n} = \frac{nL}{N}$. The distance $h$ between particles is $\frac{L}{N}$. Each mass is connected to its neighbors by tension, linking their oscillations.

<a class="zoom" href="/notes/img/vibrating-string-masses.png"><img src="/notes/img/vibrating-string-masses.png" alt="vibrating string masses" loading="lazy"></a>

The mass of each particle is $\rho h$. By Newton's 2nd Law:

$$\Sigma F_{n} = \rho h y''_{n}(t)$$

where $\Sigma F_n$ is the vector sum of $F_{T, x+1}$ and $F_{T, x-1}$

Since $F_{T, x+1}$ is proportional to $\frac{(y_{n+1} - y_n)}{h}$, the slope, we may write it as:

$$F_{T, x+1} = \left(\frac{\tau}{h}\right)(y_{n+1}-y_{n})$$

Similarly, we may write $F_{T, x-1}$ as:

$$F_{T, x-1} = \left(\frac{\tau}{h}\right)(y_{n-1}-y_{n})$$

Therefore:

$$\rho h y''_{n}(t) = \frac{\tau}{h}(y_{n+1}(t)+y_{n-1}(t)-2y_{n}(t))$$

We can convert the functions of $y$ into functions of $u$:

$$\rho h y''_{n}(t) = \frac{\tau}{h}(u(x_{n}+h, t)+u(x_{n}-h, t)-2u(x_{n}, t))$$

The limit definition of the second derivative states that:

$$f''(x) = \lim_{ h \to 0 } \frac{f(x+h) + f(x-h) - 2f(x)}{h^2}$$

If we divide by $h$:

$$\rho y''_{n}(t) = \tau \frac{u(x_{n}+h, t)+u(x_{n}-h, t)-2u(x_{n}, t)}{h^2}$$

And let $h$ tend to $0$ (which means having infinite point masses):

$$\rho y''_{n}(t) = \tau \frac{\partial^2 u}{\partial x^2}$$

Since $N \to \infty$, the discrete second time derivative $y''_n(t)$ becomes the continuous second time derivative of the function $u(x,t)$:

$$\rho \frac{\partial^2 u}{\partial t^2} = \tau \frac{\partial^2 u}{\partial x^2}$$

And since $c = \sqrt{\frac{\tau}{\rho}}$:

$$\frac{1}{c^2}\frac{\partial^2 u}{\partial t^2} = \frac{\partial^2 u}{\partial x^2}$$

This is known as the **one-dimensional wave equation**, more simply the <a class="internal-link" href="/notes/math-4890/wave-equation/">wave equation</a>, where $c$ is the *velocity* of the motion.

#### Scaling {#scaling}
We can incorporate **scaling** to simplify the wave equation further:

1. We can replace $x$ with $x=aX$, changing the interval from $x \in [0, L]$ to $X \in \left[0, \frac{L}{a}\right]$, and replace $t$ with $bT$. 
2. If we set $U(X, T) = u(x, t)$ then $\frac{\partial^2 U}{\partial X^2} = a^2 \frac{\partial^2 u}{\partial x^2}$ and $\frac{\partial^2 U}{\partial T^2} = b^2 \frac{\partial^2 u}{\partial t^2}$. 

Therefore, there exist an $a$ and $b$ such that:

$$\frac{\partial^2 U}{\partial T^2} = \frac{\partial^2 U}{\partial X^2}$$

which is effectively setting $c = 1$.

Now, we can transform the interval from $x \in [0, L]$ to $X \in [0, \pi]$ (choosing $\pi$ for $L$ is usually a convenient substitution). This is accomplished by making $a = \frac{L}{\pi}$ and $b = \frac{L}{c\pi}$. Once the new equation is solved, we can return to the original equation by making the inverse change of variables.

## Solutions to the Wave Equation {#solutions-to-the-wave-equation}
Two ways to solve the <a class="internal-link" href="/notes/math-4890/wave-equation/">wave equation</a>:
- using traveling waves
- using the superposition of standing waves

### Using Traveling Waves {#using-traveling-waves}
If we assume $c = 1$ and $L = \pi$, the wave equation becomes:

$$\frac{\partial^2 u}{\partial t^2} = \frac{\partial^2 u}{\partial x^2}$$

If a traveling wave $F$ is continuous, then $F(x\pm t)$ are solutions to the wave equation.

Additionally, the wave equation is **linear**. This means that all linear combinations of particular solutions $u(x, t)$ and $v(x, t)$ are also particular solutions. Therefore:

$$u(x, t) = F(x + t) + G(x-t)$$

where $G$ is a continuous traveling wave in the opposite direction as $F$. *All solutions* take this form.

#### Applying Traveling Waves to Vibrating String Problem {#applying-traveling-waves-to-vibrating-string-problem}
If we extend the initial shape of the string to all of $\mathbb{R}$ by making it odd and periodic, then $u(x, 0) = f(x) \ \forall \  x \in \mathbb{R}$, and:

$$f(x) = F(x) + G(x)$$

Since there are infinite choices of $F$ and $G$ that satisfy this condition, we must impose another initial condition on $u$: the *initial velocity* of the string, $g(x)$:

$$\frac{\partial u}{\partial t}(x, 0) = g(x),$$

where $g(0) = g(\pi) = 0$. We similarly extend $g$ to $\mathbb{R}$. The two initial conditions of position and velocity create this system:

$$
\begin{cases}
F(x) + G(x) = f(x) \\
F'(x) - G'(x) = g(x)
\end{cases}
$$

Differentiate $f(x)$ and add/subtract $g(x)$ to obtain:

$$
\begin{align*}
2 F'(x) = f'(x) + g(x) \\
2 G'(x) = f'(x) - g(x)
\end{align*}
$$

Hence, there are constants $C_1$ and $C_2$ such that

$$F(x) = \frac{1}{2}\left[f(x) + \int_0^x g(y) \ \mathrm{d}y \right] + C_1$$

and

$$G(x) = \frac{1}{2}\left[f(x) - \int_0^x g(y) \ \mathrm{d}y \right] + C_2$$

Since $F(x) + G(x) = f(x)$, $C_1 + C_2 = 0$, and our final solution takes the form

$$u(x, t) = \frac{1}{2}[f(x+t) + f(x-t)] + \frac{1}{2}\int_{x-t}^{x+t}g(y) \ \mathrm{d}y$$

This is known as <a class="internal-link" href="/notes/math-4890/d-alembert-s-formula/">d&#x27;Alembert&#x27;s formula</a>. 

There also exists a **negative time solution** $u^-$ to the wave equation by setting $u^-(x, t) = u(x, -t)$.

#### Using Superposition of Standing Waves {#using-superposition-of-standing-waves}
We can use separation of variables to express the general solution of the wave equation as a sum of particular solutions in the form $u(x, t) = \phi(x)\psi(t)$.

In the case of the wave equation, we have:

$$\phi(x)\psi''(t) = \phi''(x)\psi(t)$$

and therefore

$$\frac{\psi''(t)}{\psi(t)} = \frac{\phi''(x)}{\phi(x)}$$

Since the LHS only depends on $t$ and the RHS only depends on $x$, both sides must equal a constant, $\lambda$:

$$
\begin{cases}
\psi''(t) - \lambda\psi(t) = 0 \\
\phi''(x) - \lambda\phi(x) = 0
\end{cases}
$$

For $\psi$ to oscillate with time, $\lambda \ge 0$. Therefore, we can write $\lambda = -m^2$ with the solution of the equation given by:

$$\psi(t) = A\cos{mt} + B\sin{mt}$$

The solution to the second solution is:

$$\phi(x) = \tilde{A}\cos{mx} + \tilde{B}\sin{mx}$$

Since the string is attached at $x=0$ and $x=\pi$, $\phi(0) = \phi(\pi) = 0$ and $\tilde{A} = 0$. If $\tilde{B} \ne 0$, then $m$ must be an integer. For each $m \ge 1$ the function

$$u_{m}(x, t) = (A_{m}\cos{mt} + B_{m}\sin{mt})\sin{mx}$$

is a solution to the wave equation and is a standing wave. You have to double check that $u_m$ solves the equation, since $\phi$ and $\psi$ sometimes vanish when being divided.

#### Harmonics {#harmonics}
Consider the wave function $u(x, t) = \cos{t}\sin{x}$ for a vibrating string.

The case $m = 1$ for a standing wave is the **first harmonic** of a vibrating string. This is also called the <a class="internal-link" href="/notes/math-4890/fundamental-tone/">fundamental tone</a> of the string.

When $m = 2$, $u(x, t) = \cos{2t}\sin{2x}$. This is the **first overtone** or **second harmonic**. This generalizes for all $m$. As $m$ increases, the frequency increases and the period $\frac{2\pi}{m}$ goes down.

<a class="zoom" href="/notes/img/fundamental-and-overtones.png"><img src="/notes/img/fundamental-and-overtones.png" alt="fundamental and overtones" loading="lazy"></a>

#### Superposition {#superposition}
Since all solutions to the wave equation are linear, we can construct more solutions by taking linear combinations of the standing waves $u_m$. This is known as **superposition**:

$$u(x, t) = \sum_{m=1}^\infty(A_{m}\cos{mt}+B_{m}\sin{mt})\sin{mx}$$

with the initial shape of the function $u(x, 0) = f(x)$ given by:

$$\sum_{m=1}^\infty A_{m}\sin{mx} = f(x)$$

The fundamental question becomes whether it is possible to find coefficients $A_m$ to make the above true.

## The Plucked String {#the-plucked-string}
Suppose we have a string from $[0, \pi]$ that satisfies the wave equation with $c = 1$. The string is plucked to height $h$ at $p$ between $0$ and $\pi$. The initial position of the string is given by the piecewise function

$$
f(x) = \begin{cases}
\frac{xh}{p} & 0 \le x \le p \\
\frac{h(\pi - x)}{\pi - p} & p \le x \le \pi
\end{cases}
$$

If we let $g(x) = 0$, we can compute $A_m$, the Fourier coefficients of $f$:

$$
\begin{align}
A_m &= \frac{2h}{\pi p} \int_{0}^{p} x \sin(mx) \,dx + \frac{2h}{\pi (\pi - p)} \int_{p}^{\pi} (\pi - x) \sin(mx) \,dx \\[10pt]
&= \frac{2h}{\pi p} \left( -\frac{p \cos(mp)}{m} + \frac{\sin(mp)}{m^2} \right) + \frac{2h}{\pi (\pi - p)} \left( \frac{(\pi - p) \cos(mp)}{m} + \frac{\sin(mp)}{m^2} \right) \\[10pt]
&= -\frac{2h \cos(mp)}{\pi m} + \frac{2h \sin(mp)}{\pi m^2 p} + \frac{2h \cos(mp)}{\pi m} + \frac{2h \sin(mp)}{\pi m^2 (\pi - p)} \\[10pt]
&= \frac{2h \sin(mp)}{\pi m^2 p} + \frac{2h \sin(mp)}{\pi m^2 (\pi - p)} \\[10pt]
&= \frac{2h \sin(mp)}{\pi m^2} \left( \frac{1}{p} + \frac{1}{\pi - p} \right) \\[10pt]
&= \frac{2h \sin(mp)}{\pi m^2} \cdot \frac{\pi}{p (\pi - p)} \\[10pt]
&= \frac{2h}{m^2} \frac{\sin(mp)}{p (\pi - p)}.
\end{align}
$$

When we put this into

$$
f(x) = \sum_{m=1}^\infty A_{m}\sin(mx)
$$

we get

$$
u(x, t) = \sum_{m}^\infty A_{m} \cos(mt) \sin(mx)
$$

which matches the solution obtained by <a class="internal-link" href="/notes/math-4890/d-alembert-s-formula/">d&#x27;Alembert&#x27;s formula</a>

## The Heat Equation {#the-heat-equation}

### Derivation {#derivation}
Consider a square plate $S$ in $\mathbb{R}^2$ centered at $(x_0, y_0)$ and side length $h$ with an initial heat profile at $t = 0$. Let the temperature at $(x, y)$ at $t$ be denoted by $u(x, y, t)$. The amount of heat energy in $S$ at $t$ is given by 

$$
H(t) = \sigma \int \int_{S}u(x,y,t) \ \mathrm{d}x \mathrm{d}y
$$

where $\sigma$ is the specific heat of $S$. Therefore, the heat flow is

$$
\frac{\partial H}{\partial t} = \sigma \int \int_{s} \frac{\partial u}{\partial t} \ \mathrm{d}x \mathrm{d}y
$$

which is approximately equal to

$$
\sigma h^2 \frac{\partial u}{\partial t}(x_{0}, y_{0}, t)
$$

since the area of $S$ is $h^2$
