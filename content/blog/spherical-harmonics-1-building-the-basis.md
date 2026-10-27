---
author: "Anish Goyal"
title: "The Beauty of Spherical Harmonics, Part 1: Building the Basis"
slug: "spherical-harmonics-1-building-the-basis"
description: "Why I wrote this series, and building spherical harmonics from scratch: functions as vectors, the angular Laplacian, where ℓ and m come from, and diagonalizing it."
summary: "Functions on a sphere are vectors, so we pick the angular Laplacian and build its eigenbasis ab initio: separation of variables gives m and ℓ, the tensor-product split gives L_z and D_m, and the two slots get diagonalized one at a time."
eyeCatcher: "Functions on a sphere are vectors. Humor me for a minute."
tags: [spherical-harmonics, mathematics, physics, linear-algebra, legendre-polynomials]
series: "The Beauty of Spherical Harmonics"
part: 1
readingtime: "22"
date: 2026-10-27T12:03:00-04:00
modified: 2026-10-27
---

## Why I Made This

This series started as a note for my understanding of [Spherical Harmonics](https://en.wikipedia.org/wiki/Spherical_harmonics), so that I can always revisit this as a reference and understand what the hell I'm looking at. That's the chief reason. I really like to think of it from a physics pov, so I'm just gonna go with that.

There are a few other reasons, though. Spherical harmonics usually get handed to us as a finished formula that we're supposed to trust, and I wanted to derive every piece *ab initio* instead: where $\ell$ and $m$ come from, why the normalization constant looks the way it does, and why the basis is orthogonal in the first place. I also have a taste for what I call *low entropy* expressions, ones that are factored so that their physical meaning is immediately clear, and spherical harmonics turned out to be a great place to practice that. And the trick at the heart of all of this (diagonalize, then decouple) isn't just a sphere thing. It shows up in [drumheads](https://en.wikipedia.org/wiki/Vibration_of_a_circular_membrane), [laser modes](https://en.wikipedia.org/wiki/Transverse_mode), [the hydrogen atom](https://en.wikipedia.org/wiki/Hydrogen_atom), [maps of the cosmic microwave background](https://en.wikipedia.org/wiki/Cosmic_microwave_background), and [Earth's gravity field](https://en.wikipedia.org/wiki/Gravity_of_Earth), so it's worth understanding properly at least once.

I believe that art is a great way to communicate science, so I tried to really do the visualizations well. Every figure in this series is drawn in a hand-sketched style, but computed from the actual math, so the shapes are the real ones. The colors mean something: red is $+$, blue is $-$, and anything hidden behind a surface is dashed and faded.

I also want this to be clear to whoever reads it, not just future me. The only prerequisites are some linear algebra and calculus. I use [Dirac (bra-ket) notation](https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation) throughout, and every new idea gets introduced right where it's needed. Each post builds on the last one, so it's best read in order.

## Goal

We want to be able to decompose any function on the surface of a sphere into a summation of [eigenbases](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors). The sphere radius here is arbitrary and not super important for the purposes of our pedagogy. This follows from the fact that the eigenbases, or "modes" of a sphere, are completely independent of the radius of that sphere; which makes sense because the "shape" or "curvature" of the sphere is pretty much completely independent of a sphere's radius.

### Some Initial Terminology

Vectors and functions, as well as the operations between them, are [totally interchangeable](https://en.wikipedia.org/wiki/Hilbert_space). This is not mathematically rigorous at all... so there is probably [some edge case](https://en.wikipedia.org/wiki/Square-integrable_function) where this isn't true, but humor me for a minute. We can decompose vectors into functional forms as follows:

| Ordinary Vectors | Functions on a Sphere |
| --- | --- |
| $\displaystyle\vec{v}=\sum_{i}c_{i}\cdot \hat{e}_{i}$ | $\displaystyle f(\theta,\psi)=\sum_{\ell m}c_{\ell m}Y_{\ell m}(\theta,\psi)$ |
| $\displaystyle\vec{a} \cdot \vec{b} = \sum_{i}a_{i}b_{i}$ | $\displaystyle\left< f, g\right> = \langle f \vert g \rangle = \int_{0}^{2\pi}\int_{0}^{\pi} f^*g \sin \theta \,\mathrm{d}\theta \,\mathrm{d}\psi$ |
| $\displaystyle\hat{e}_{i} \cdot \hat{e}_{j} = \delta_{ij}$ | $\displaystyle\left< Y_{\ell' m'},Y_{\ell m} \right> = \langle \ell' m' \vert \ell m \rangle = \delta_{\ell \ell'}\delta_{m m'}$ |
| $\displaystyle c_{i}=\hat{e}_{i}\cdot \vec{v}$ | $\displaystyle c_{\ell m}=\left< Y_{\ell m}, f\right> = \langle \ell m \vert f \rangle$ |
| $\displaystyle\sum_{i}\hat{e}_{i}\,\hat{e}_{i}^{\mathsf{T}}=\hat{1}$ | $\displaystyle\int_{0}^{2\pi}\int_{0}^{\pi}\ket{\hat{n}}\bra{\hat{n}}\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\psi=\hat{1}$ |

Internalizing these beasties will allow us to truly understand how spherical harmonics work and how we can make money on them.

## Making Money on Ts

### Functions on a Sphere Are Vectors

Just really want to drive this point home. Functions on a sphere are synonymous with vectors and can be quantized as an expansion in the spherical eigenbasis! Suppose we have an arbitrary function $\ket{f}$ on a sphere. How is it characterized?

$$
\left< \hat{n} | f \right> = f(\hat{n}) = f(\theta,\psi)
$$

In other words, $\ket{f}$ is characterized by the "action" that it takes on a normal vector, $\hat{n}$ pointing outward from the sphere! The values $f(\hat{n})$ are the *continuous* components of $\ket{f}$, the same way the $c_{i}$ are the discrete components of $\vec{v}$:

$$
\begin{align*}
\ket{f}&=\hat{1}\ket{f}\\
&=\int_{0}^{2\pi}\int_{0}^{\pi}\ket{\hat{n}}\braket{\hat{n}}{f}\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\psi
\end{align*}
$$

![A sphere with needles sticking out of its surface, each needle's length set by the value of f in that direction|360](/images/spherical-harmonics/function-on-sphere.svg)

### Picking a Good Basis

So... what's a good basis for the sphere of $\ket{f}$? Using the principle of least sloth, we want the eigenvectors of some *operator* (call it $\hat{\Lambda}$) so that we can [diagonalize](https://en.wikipedia.org/wiki/Diagonalizable_matrix) $\hat{\Lambda}$ in its eigenbasis and have the eigenkets that expand $\ket{f}$!

Since we deal with [Laplace's equation](https://en.wikipedia.org/wiki/Laplace%27s_equation) in E&M pretty frequently, a good choice for $\hat{\Lambda}$ is $r^2$ times the *angular* term of $\hat{\nabla}^2=\frac{1}{r^2}\partial_{r}(r^2\partial_{r})+\frac{1}{r^2}\hat{\Lambda}$. As stated previously, since the eigenbasis itself is independent of $R$, we may discard the radial part of $\hat{\nabla}^2$. For a sphere of radius $R$, $\frac{1}{R^2}\hat{\Lambda}$ is the "[surface Laplacian](https://en.wikipedia.org/wiki/Laplace%E2%80%93Beltrami_operator)," which has the same eigenfunctions as $\hat{\Lambda}$, times the scale factor of $\frac{1}{R^2}$ for the eigenvalues.

$$
\begin{align*}
\hat{\Lambda}&=\frac{1}{\sin \theta}\partial_{\theta}(\sin \theta \partial_{\theta})\\
&\quad+\frac{1}{\sin^2 \theta}\partial_{\psi}^2
\end{align*}
$$

So, looking at this guy, what does it actually measure?

**Claim:** At each point on the spherical surface, $\langle \hat n|\hat\Lambda|f\rangle$ measures [how much the average](https://en.wikipedia.org/wiki/Laplace_operator) of $f(\hat{n}')$ over an infinitesimal circle around $\hat n$ exceeds $f(\hat n)$ itself. This is explained in more detail below, but the short version is $\left<f \right> -f \approx \frac{\varepsilon^2}{4}\mel{\hat{n}}{\hat{\Lambda}}{f}$.

![A point on a sphere with a small ring of radius epsilon around it, zoomed into a lifted patch where the ring rides on the height of f|640](/images/spherical-harmonics/neighbor-average.svg)

> *Proof.*
> Consider a small, geodesic patch with radius $\varepsilon$ centered at the point containing $\hat{n}$. Then,
>
> $$
> \begin{align*}
> &\left< f \right>_{\varepsilon}(\hat{n})\\
> &\quad=\frac{1}{2\pi}\int_{0}^{2\pi} f(\hat{n}'(\varepsilon,\psi')) \,\mathrm{d}\psi'.
> \end{align*}
> $$
>
> Define the *azimuthal average* of $f$ as:
>
> $$
> g(\theta)=\frac{1}{2\pi}\int_{0}^{2\pi} f(\theta,\psi) \, \mathrm{d}\psi,
> $$
>
> so that $\left< f \right>_{\varepsilon}(\hat{n})=g(\varepsilon)$ and $g(0)=\left< f \right>_{\text{pole}}=f(\text{pole})$.
>
> Indeed, it is valid to conclude that $\varepsilon$, which we initially defined as the small radius in an arbitrary geodesic patch (which is also equal to the *polar angle*, $\theta$, between $\hat{n}$ and $\hat{n}'$ within the integral) is **equivalent** to the *same* variation in $\theta$ measured from the north pole (which is measured by $g$). This follows from the *[rotational invariance](https://en.wikipedia.org/wiki/Rotational_invariance)* of the sphere, since you can just rotate the sphere and define $\hat{n}$ as the "new" north pole... which means that $g(0)=f(\hat{n})$.
>
> ![The point and its small ring carried by a rotation up to the north pole, where the ring becomes the latitude circle theta equals epsilon|560](/images/spherical-harmonics/rotate-to-pole.svg)
>
> Taking the [Taylor expansion](https://en.wikipedia.org/wiki/Taylor_series) of $g$, we have:
>
> $$
> \begin{align*}
> g(\varepsilon)-g(0)&=g'(0)\varepsilon + \frac{g''(0)}{2}\varepsilon^2\\
> &\quad+ \frac{g'''(0)}{6}\varepsilon^3 + \dots
> \end{align*}
> $$
>
> Applying $g(0)=f$ and evenness of $g$:
>
> $$
> \left< f \right> -f = \frac{g''(0)}{2}\varepsilon^2 + O(\varepsilon^4)
> $$
>
> Now, we determine $g''(0)$:
>
> $$
> g''(0)=\frac{1}{2\pi}\int_{0}^{2\pi}\partial_{\theta}^2 f(0, \psi) \, \mathrm{d}\psi
> $$
>
> And we form a connection with the following limit at the pole:
>
> $$
> \begin{align*}
> &(\hat{\Lambda} f_{\text{pole}})(\hat{n})\\
> &\quad= \lim_{ \theta \to 0 } \frac{1}{2\pi} \int_{0}^{2\pi} \hat{\Lambda} f(\theta, \psi) \,\mathrm{d}\psi \\
> &\quad= \lim_{ \theta \to 0 } [g''(\theta)+\cot \theta g'(\theta)] \\
> &\quad= 2g''(0)
> \end{align*}
> $$
>
> Therefore, $g''(0)=\frac{\hat{\Lambda}f(\hat{n})}{2}$, so we have:
>
> $$
> \begin{align*}
> \left< f \right> -f &\approx \frac{\hat{\Lambda}f(\hat{n})}{4}\varepsilon^2 \\
> &=\frac{\varepsilon^2}{4}\mel{\hat{n}}{\hat{\Lambda}}{f}
> \end{align*}
> $$
>
> $\blacksquare$

Since $\hat{\Lambda}$ is [Hermitian](https://en.wikipedia.org/wiki/Self-adjoint_operator), it can be [diagonalized in its own eigenbasis](https://en.wikipedia.org/wiki/Spectral_theorem):

$$
\begin{align*}
\hat{\Lambda} \ket{\ell m} &= -\ell(\ell+1)\ket{\ell m}\\
\braket{\hat{n}}{\ell m} &= Y_{\ell m}(\theta, \psi)
\end{align*}
$$

$Y_{\ell m}$ is just another way to write "components of basis $\ket{\ell m}$ for all $\hat{n}$ on the sphere".

## Where $\ell$ and $m$ Come From

I just *asserted* $\hat{\Lambda}\ket{\ell m} = -\ell(\ell+1)\ket{\ell m}$. Let's verify this is the case *ab initio* by formulating the eigenvalue problem as follows:

$$
\begin{align*}
\hat{\Lambda} \ket{\ell m} &= -\lambda\ket {\ell m} \\
\mel{\hat{n}}{\hat{\Lambda}}{\ell m} &= -\lambda \braket{\hat{n}}{\ell m} \\
\hat{\Lambda}\left< \hat{n} | \ell m \right> &= -\lambda \braket{\hat{n}}{\ell m} \\
\hat{\Lambda} Y_{\ell m}(\theta,\psi)&= - \lambda Y_{\ell m}(\theta,\psi)
\end{align*}
$$

The minus sign is because $\mel{f}{\hat{\Lambda}}{f} \leq 0$, which follows from [integrating by parts](https://en.wikipedia.org/wiki/Green%27s_identities) (not shown). A more hand-wavy explanation: on a closed sphere, $f$ must have a global maximum, and there it sits at or above its neighbors' average. Therefore, $\hat{\Lambda}$ can't push $f$ further in its own direction. Hence $\lambda$ itself must be $\geq 0$.

The third line where we pull $\hat{\Lambda}$ out of the braket would ordinarily be a mathematical tragedy, but it turns out there are a subset of operators for which you can pull the operator outside and let it act directly on the scalar function with no penalties. This is usually the case if the operator has a differential/multiplication representation in the basis defined by the bra, a principle known as *structural locality*. A convenient table for Hermitian observables is shown below (in [natural units](https://en.wikipedia.org/wiki/Natural_units)):

| Operator | Shorthand in position basis |
| --- | --- |
| Position ($\hat{x}$) | $\langle x \vert \hat{x} \vert f \rangle = \hat{x}\,\langle x \vert f \rangle = x\,f(x)$ |
| Function of position ($V(\hat{x})$) | $\langle x \vert V(\hat{x}) \vert f \rangle = V(\hat{x})\,\langle x \vert f \rangle = V(x)\,f(x)$ |
| Momentum ($\hat{p}$) | $\langle x \vert \hat{p} \vert f \rangle = \hat{p}\,\langle x \vert f \rangle = -i\,\partial_{x}f(x)$ |
| Momentum, 3D ($\hat{\vec{p}}$) | $\langle \vec{r} \vert \hat{\vec{p}} \vert f \rangle = \hat{\vec{p}}\,\langle \vec{r} \vert f \rangle = -i\vec{\nabla}f(\vec{r})$ |
| Laplacian ($\hat{\nabla}^2=-\hat{p}^2$) | $\langle \vec{r} \vert \hat{\nabla}^2 \vert f \rangle = \hat{\nabla}^2\,\langle \vec{r} \vert f \rangle = \nabla^2 f(\vec{r})$ |
| Hamiltonian ($\hat{H}=\frac{\hat{p}^2}{2\mu}+V(\hat{x})$) | $\langle x \vert \hat{H} \vert f \rangle = \hat{H}\,\langle x \vert f \rangle = \left[-\frac{1}{2\mu}\partial_{x}^2+V(x)\right]f(x)$ |
| Polar coordinate ($\cos\hat{\theta}$) | $\langle \hat{n} \vert \cos\hat{\theta} \vert f \rangle = \cos\hat{\theta}\,\langle \hat{n} \vert f \rangle = \cos\theta\,f(\theta,\psi)$ |
| $z$-angular momentum ($\hat{L}_z$) | $\langle \hat{n} \vert \hat{L}_z \vert f \rangle = \hat{L}_z\,\langle \hat{n} \vert f \rangle = -i\,\partial_{\psi}f(\theta,\psi)$ |
| Angular Laplacian ($\hat{\Lambda}=-\hat{L}^2$) | $\langle \hat{n} \vert \hat{\Lambda} \vert f \rangle = \hat{\Lambda}\,\langle \hat{n} \vert f \rangle = \left[\frac{1}{\sin\theta}\partial_{\theta}(\sin\theta\,\partial_{\theta})+\frac{1}{\sin^2\theta}\partial_{\psi}^2\right]f(\theta,\psi)$ |
| $\theta$-operator at fixed $m$ ($\hat{D}_m$) | $\langle \theta \vert \hat{D}_m \vert f \rangle = \hat{D}_m\,\langle \theta \vert f \rangle = \left[\frac{1}{\sin\theta}\partial_{\theta}(\sin\theta\,\partial_{\theta})-\frac{m^2}{\sin^2\theta}\right]f(\theta)$ |

We can now see that we need to solve the PDE in $Y$ and determine the eigenvalue $\lambda$. There is also the question of how we're actually going to express the original function, $f$, as a summation over the eigenbasis $\ket{\ell m}$, implying summation indices $\ell$ and $m$. *Where exactly do these discretization indices/quantum numbers come from?* Spoiler alert: We are going to use the fact that $Y$ is periodic-continuous to get $m$ and finite at the poles to get $\ell$.

### Separation of Variables

Let's use [separation of variables](https://en.wikipedia.org/wiki/Separation_of_variables) to solve for $Y$. We begin with the [ansatz](https://en.wikipedia.org/wiki/Ansatz) that $Y(\theta,\psi) = \Theta(\theta)\Phi(\psi)$. Plug in, multiply by $\frac{\sin^2\theta}{\Theta\Phi}$, and rearrange:

$$
\begin{align*}
&\frac{\sin \theta}{\Theta}\partial_{\theta}(\sin \theta\, \partial_{\theta}\Theta) + \lambda \sin^2 \theta\\
&\quad= -\frac{1}{\Phi}\partial_{\psi}^2\Phi
\end{align*}
$$

LHS depends only on $\theta$, RHS only on $\psi$, so both sides equal $+m^2$:

$$
\begin{align*}
\partial_{\psi}^2 \Phi &= -m^2\Phi \\
\implies \Phi(\psi) &= e^{im\psi}
\end{align*}
$$

Uniqueness implies $\Phi(\psi + 2\pi) = \Phi(\psi)$, so $e^{2\pi i m} = 1 (m \in \mathbb{Z})$. *This is our first quantum number!* We intentionally avoided $-m^2$ because then $\Phi = e^{\pm k\psi}$, which grows/decays monotonically and thus cannot be periodic-continuous.

![A ring carrying the wave e to the i m psi: integer m closes on itself after one trip around, while m equals five halves tears at the seam|560](/images/spherical-harmonics/periodicity.svg)

### The $\theta$ Equation in Nicer Variables

Apply the same separation of variables technique to $Y$, setting the LHS equal to $m^2$, and dividing by $\sin^2\theta$:

$$
\begin{align*}
&\frac{1}{\sin\theta}\partial_{\theta}(\sin\theta\,\partial_{\theta}\Theta)\\
&\quad+ \left(\lambda - \frac{m^2}{\sin^2\theta}\right)\Theta = 0
\end{align*}
$$

Using the substitution $x = \cos\theta$: $x = \pm1$ is the north/south pole, respectively, and we can also use the fact that $\sin^2\theta = 1 - x^2$.

$$
\begin{align*}
&\partial_{x}\left[(1-x^2)\partial_{x}\Theta\right]\\
&\quad+ \left(\lambda - \frac{m^2}{1-x^2}\right)\Theta = 0 \\
&\left[(1-x^2)\partial_{x}^2 - 2x\,\partial_{x} + \lambda-\frac{m^2}{1-x^2}\right]\Theta = 0
\end{align*}
$$

This is a famous ODE: **[the Legendre equation](https://en.wikipedia.org/wiki/Legendre_function)**. Setting $m = 0$ gives the *plain Legendre equation*:

$$
[(1-x^2)\partial_{x}^2 - 2x\,\partial_{x} + \lambda]\Theta = 0
$$

### Finding $\ell$ from Finite-Valuedness

The general solution to the *plain* Legendre equation follows a recurrence relation from the [power series](https://en.wikipedia.org/wiki/Power_series_solution_of_differential_equations) ansatz $\Theta(x)=\sum_{n=0}^{\infty}a_{n}x^n$ where $a_{n+2}=\frac{n(n+1)-\lambda}{(n+2)(n+1)}a_{n}$. However, this diverges at $|x|=1$. Fix: set $\lambda=\ell(\ell+1)$ for some $\ell \in \{0, 1, 2, \dots\}$, causing the recurrence numerator to vanish at $n=\ell$, causing $a_{n \ge \ell+2}=0$. Another caveat: you must also set $a_{1}=0$ so all the odd coefficients die immediately (you could have also fixed the even coefficients to zero).

This leads to the ODE $[\partial_{x}(1-x^2)\partial_{x} + \ell(\ell+1)]\Theta = 0$, which *also* simultaneously gives $\lambda=\ell(\ell+1)$. The solutions are the [Legendre polynomials](https://en.wikipedia.org/wiki/Legendre_polynomials):

$$
\begin{align*}
\left. \Theta(x)\right\vert_{m=0} &= P_{\ell}(x)\\
&=P_{\ell}(\cos \theta)\\
&=\left.\frac{1}{2^\ell \ell!}\partial_{x}^\ell(x^2 - 1)^\ell \right\vert_{x=\cos \theta}\\
&=\sum_{k=0}^{\lfloor \ell/2 \rfloor }(-1)^k\\
&\quad\times\frac{(2\ell-2k)!}{2^\ell k! (\ell-k)! (\ell-2k)!}\left.x^{\ell-2k}\right\vert_{x=\cos \theta} \\
&= \sum_{k=0}^{\lfloor \ell/2 \rfloor }(-1)^k\\
&\quad\times\frac{(2\ell-2k)!}{2^\ell k! (\ell-k)! (\ell-2k)!}\cos^{(\ell-2k)}\theta
\end{align*}
$$

For the *general* Legendre equation $(m \ne 0)$, we need to solve the ODE:

$$
\left[\partial_{x}(1-x^2)\partial_{x} + \ell(\ell+1)-\frac{m^2}{1-x^2}\right]\Theta = 0
$$

Which have linear combinations of the [*associated* Legendre functions](https://en.wikipedia.org/wiki/Associated_Legendre_polynomials), $P_{\ell}^m(x)$ and $Q_{\ell}^m(x)$, as solutions... *except* $Q_{\ell}^{m}(x)$ is ill-defined at $|x|=1$, so chuck it! And so, we have:

$$
\begin{align*}
\left. \Theta(x) \right\vert_{m \ne 0} &= P_{\ell}^m(x)\\
&=P_{\ell}^m(\cos \theta) \\
&=\left.(-1)^m (1-x^2)^{m/2}\,\partial_{x}^m P_{\ell}(x)\right\vert_{x=\cos \theta}\\
&=\frac{(-1)^m}{2^\ell \ell!}(1-x^2)^{m/2}\\
&\quad\times\left.\partial_{x}^{\ell+m}(x^2-1)^\ell\right\vert_{x=\cos \theta}\\
&=(-1)^m (1-x^2)^{m/2}\\
&\quad\times\sum_{k=0}^{\lfloor (\ell-m)/2 \rfloor }(-1)^k\\
&\quad\times\frac{(2\ell-2k)!}{2^\ell k! (\ell-k)! (\ell-2k-m)!}\\
&\quad\times\left.x^{\ell-2k-m}\right\vert_{x=\cos \theta} \\
&= (-1)^m \sin^m \theta\\
&\quad\times\sum_{k=0}^{\lfloor (\ell-m)/2 \rfloor }(-1)^k\\
&\quad\times\frac{(2\ell-2k)!}{2^\ell k! (\ell-k)! (\ell-2k-m)!}\cos^{(\ell-2k-m)} \theta
\end{align*}
$$

The associated Legendre functions are related to the Legendre polynomials by

$$
P_{\ell}^m(x)=(-1)^m(1-x^2)^{m/2} \partial_{x}^m P_{\ell}(x)
$$

![Surfaces of revolution over the sphere: P sub ell of cos theta stays finite at both poles, while Q sub ell of cos theta shoots off to infinity there|440](/images/spherical-harmonics/pole-finiteness.svg)

## Assembling $Y_{\ell m}$

Okay, that was a lot of math. The takeaway is that each eigenket $\ket{\ell m}$ is a [*tensor product*](https://en.wikipedia.org/wiki/Tensor_product_of_Hilbert_spaces) of a distinct pair of modes, each an eigenket of its own Hermitian 1D operator: the $m$-mode $\ket{m}=e^{im(\cdot)}$, eigenket of $\hat{L}_{z}$, and the Legendre mode $\ket{\ell}_{m}=P_{\ell}^{|m|}(\cos(\cdot))$, eigenket of $\hat{D}_m$. The "subscript $m$" just means the Legendre mode is for some fixed $m$. This makes sense because the associated Legendre function depends on your choice of $m$. More on $\hat{L}_{z}$ and $\hat{D}_{m}$ in the following section.

We can now construct our orthogonal basis!

$$
\begin{align*}
\braket{\hat{n}}{\ell m} &= Y_{\ell m}(\theta,\psi)\\
&= N_{\ell m}\,P_{\ell}^{|m|}(\cos\theta)\,e^{im\psi}
\end{align*}
$$

Claim: You can use $m \mapsto|m|$ for $\Theta$ because its ODE only has $m^2$. For all the masochists out there, you can still use the Legendre summation formula for $m \in [-\ell, 0]$ and get the same answer.

![A meridian wave times an equator wave paints Y₃₂|640](/images/spherical-harmonics/tensor-product.svg)

$N_{\ell m}$ is the normalization constant fixed by the inner product of eigenkets. We will come up with a [concrete way to calculate $N_{\ell m}$](/blog/spherical-harmonics-2-solving-laplaces-equation/#normalization) once we introduce $\hat{L}_{z}$ and $\hat{D}_{m}$ and discuss some additional properties of our chosen spherical basis that may be of use.

## Introducing $\hat{L}_{z}$ and $\hat{D}_{m}$

As mentioned previously, our chosen spherical eigenbasis also serves as the eigenkets of $\hat{\Lambda}$, *and* it is also the tensor product of the Legendre and $m$-modes $(\ket{\ell m}\equiv\ket{\ell}_{m} \otimes \ket{m})$ with their own respective quantum numbers. But what operators do those individual modes correspond to? And is there any relationship between those operators and $\hat{\Lambda}$? In this section, I hope to answer those questions with fidelity.

### Understanding $\bra{\hat{n}}$

First, let's closely examine the vector $\bra{\hat{n}}$. It's rather odd to have a unit-norm vector as a *label* within a bra (or ket for that matter). In fact, it's something that I hadn't seen before up until writing this (the benefits of making ts up as I go 😋). So what does $\bra{\hat{n}}$ really mean? Just like the eigenbasis $\ket{\ell m}$, $\bra{\hat{n}}$ is *also* just a tensor product of the input coordinate system:

$$
\bra{\hat{n}} = \bra{\theta} \otimes \bra{\psi}\equiv\bra{\theta \psi}
$$

![The ψ slot as a latitude ring, the θ slot as a meridian|360](/images/spherical-harmonics/bra-slots.svg)

This is important to keep in mind, since it turns out that $\bra{\theta \psi}$ serves as a basis for the [*dual space*](https://en.wikipedia.org/wiki/Dual_space) of $\ket{\ell m}$.

### Tensor-Product Decomposition of $\hat{\Lambda}$

Now, let's return back to our old friend $\hat{\Lambda}$. It turns out that *any* operator in a tensor-product Hilbert space can be expressed as a sum of tensor products of operators in each subspace, and we can use this fact to get $\hat{\Lambda}$ into a *lower entropy* form. Whenever I say "low entropy" in the context of problem-solving, I'm usually referring to an expression that is factored/structured in a certain way so that its physical meaning is immediately clear.

This pedagogical approach ties into how I viewed circuit theory in undergrad... essentially, it's possible to [convert any circuit into a matrix](https://en.wikipedia.org/wiki/Nodal_analysis) (even if it's nonlinearly defined in the case of microelectronics, as [the relationships are still linear](https://en.wikipedia.org/wiki/Small-signal_model)), but the raw output of these matrices are usually unorganized as some kind of massive polynomial ratio where the physical intuition is lost and it's not trivial to make approximations. As such, solving those kinds of systems usually has the tradeoff between *speed* and *explainability*.

$$
\begin{align*}
\hat{\Lambda}&=\left( \underbrace{\frac{1}{\sin\theta}\partial_{\theta}(\sin\theta\,\partial_{\theta})}_{\hat{A}} \otimes \hat{1}\right) \\
&\quad+ \left( \underbrace{\frac{1}{\sin^2\theta}}_{\hat{W}} \otimes \partial_{\psi}^2\right) \\
&= (\hat{A} \otimes \hat{1})+(\hat{W} \otimes \partial_{\psi}^2)
\end{align*}
$$

So which half of $\bra{\theta \psi} \equiv \bra{\theta}\otimes\bra{\psi}$ actually *reads* $\hat{A}$ and $\hat{W}$? When it comes to formulating tensor products as an "action" on an operator, you can think of each sub-ket/sub-bra combo as "slotting" one of the operators in place. Mathematically, this is described as follows:

$$
\begin{align*}
&\left(\bra{\theta}\otimes\bra{\psi}\right)\left(\hat{A}\otimes\hat{B}\right)\left(\ket{u}\otimes\ket{v}\right)\\
&\quad=\mel{\theta}{\hat{A}}{u}\mel{\psi}{\hat{B}}{v}
\end{align*}
$$

We can now sandwich $\hat{\Lambda}$ with the eigenket and eigenbra of the space:

$$
\mel{\theta \psi}{\hat{\Lambda}}{\ell m}
$$

*But isn't this just $-\lambda Y = -\ell(\ell+1) Y$? Why are we reinventing the wheel?* Good question. The main purpose is to use this tensor-product-decomposed form of $\Lambda$ to provide more insight into the structure of $Y$ (the low entropy form I was describing earlier). We proceed as follows:

$$
\begin{align*}
&\bra{\theta \psi} \hat{\Lambda}\ket{\ell m}\\
&\quad= \bra{\theta \psi}\left[(\hat{A} \otimes \hat{1})+(\hat{W} \otimes \partial_{\psi}^2)\right]\ket{\ell m} \\
&\quad= N_{\ell m}\Big[\left(\bra{\theta}\otimes\bra{\psi}\right)(\hat{A}\otimes\hat{1})\left(\ket{\ell}_m\otimes\ket{m}\right)\\
&\qquad+\left(\bra{\theta}\otimes\bra{\psi}\right)(\hat{W}\otimes\partial_{\psi}^2)\left(\ket{\ell}_m\otimes\ket{m}\right)\Big] \\
&\quad= N_{\ell m}\Big[\mel{\theta}{\hat{A}}{\ell}_m\braket{\psi}{m}\\
&\qquad+\mel{\theta}{\hat{W}}{\ell}_m\mel{\psi}{\partial_{\psi}^2}{m}\Big]
\end{align*}
$$

Notice that we have *three* slotted operators (well, technically four if you include the identity, but who gaf): $\hat{A}$, $\hat{W}$, $\partial_{\psi}^2$. Our job is to deal with these beasties one by one. Let's deal with $\partial_{\psi}^2$ first, since it already contains another, somewhat-well-known operator, encoded inside:

$$
\begin{align*}
\mel{\psi}{\partial_{\psi}^2}{m}&=\partial_{\psi}^2\braket{\psi}{m}\\
&=\partial_{\psi}^2e^{im\psi}=-m^2e^{im\psi}\\
&=-m^2\braket{\psi}{m}
\end{align*}
$$

Interpretation: $\ket{m}$ is an eigenket of $\partial_{\psi}^2$ with eigenvalue $-m^2$ (recall that $-m^2$ was our separation constant when we were doing separation of variables). We can use this to find the operator that is an eigenket of $\partial_{\psi}$ (tired of eigenvalue problems yet?). Since $\partial_{\psi}\ket{m}=im\ket{m}$, we have $-i\partial_{\psi}\ket{m}=m \ket{m}$. Call the left-acting operator $\hat{L}_z$:

$$
\begin{align*}
\hat{L}_z&\equiv-i\partial_{\psi}\\
\mel{\psi}{\hat{L}_z}{m}&=\hat{L}_z\braket{\psi}{m}\\
&=-i\partial_{\psi}e^{im\psi}=m\,e^{im\psi}\\
&=m\braket{\psi}{m}
\end{align*}
$$

It turns out that $\hat{L}_{z}$ is a well-known Hermitian operator, the [angular momentum operator](https://en.wikipedia.org/wiki/Angular_momentum_operator). It can also be thought of as the canonical operator that [*generates* rotations](https://en.wikipedia.org/wiki/Rotation_operator_%28quantum_mechanics%29) about $z$:

$$
e^{-i\alpha\hat{L}_z}f(\psi)=e^{-\alpha\partial_{\psi}}f(\psi)=f(\psi-\alpha)
$$

Since $\partial_{\psi}^2=-\hat{L}_z^2$, we have $\hat{\Lambda}=(\hat{A}\otimes\hat{1})-(\hat{W}\otimes\hat{L}_z^2)$. Since $\hat{L}_{z}^2$ is the only operator slotted into $\bra{\psi}$, my claim is that the eigenkets of $\hat{L}_z$ span the entire $\bra{\psi}$ sub-space (one of our coordinate labels in the spherical basis!).

Now, what about the two operators slotted into $\ket{\theta}$? Let's plug the $\bra{\psi}$ sucker back in:

$$
\begin{align*}
&\bra{\theta \psi} \hat{\Lambda}\ket{\ell m}\\
&\quad= N_{\ell m}\left[\hat{A}\braket{\theta}{\ell}_m-m^2\hat{W}\braket{\theta}{\ell}_m\right]\braket{\psi}{m} \\
&\quad= N_{\ell m}\left[\left(\underbrace{\hat{A}-m^2\hat{W}}_{\hat{D}_{m}}\right)\braket{\theta}{\ell}_m\right]\braket{\psi}{m}
\end{align*}
$$

Why was I able to pull out $\hat{A}$ and $\hat{W}$? Just like before, it's because of *structural locality.* Since $\hat{A}=\frac{1}{\sin\theta}\partial_{\theta}(\sin\theta\,\partial_{\theta})$ and $\hat{W}=\frac{1}{\sin^2\theta}$ are solely dependent on $\theta$, reading $\braket{\theta}{\ell}$ first and operating afterwards still yields the same result. In other words: if the operator's variable matches the bra label, you can bring it out of the sandwich!

From the result above, we can see that the operators slotted into $\bra{\theta}$ can be *further collapsed* into a single operator acting on the Legendre mode (call it $\hat{D}_{m}$). The "subscript $m$" is there because, similar to the Legendre modes, $\hat{D}_m$ only exists *after* the $\psi$ slot has handed over its eigenvalue. In other words: different $m$-mode, different $\hat{D}_m$.

Now, re-sandwich this beasty with the Legendre mode:

$$
\begin{align*}
\hat{D}_m\braket{\theta}{\ell}_m&=\mel{\theta}{\hat{D}_m}{\ell}_m\\
&=\Big[\frac{1}{\sin\theta}\partial_{\theta}(\sin\theta\,\partial_{\theta})\\
&\qquad-\frac{m^2}{\sin^2\theta}\Big]P_{\ell}^{|m|}(\cos\theta)\\
&=-\ell(\ell+1)P_{\ell}^{|m|}(\cos\theta)
\end{align*}
$$

*This is literally the $\theta$ equation we already solved!* So, $\ket{\ell}_m$ is the eigenket of $\hat{D}_m$ with eigenvalue $-\ell(\ell+1)$, and for each fixed $m$ the eigenkets of $\hat{D}_m$ span the entire $\theta$ slot (or the $\theta$ coordinate label). Finishing the sandwich:

$$
\begin{align*}
&\bra{\theta \psi} \hat{\Lambda}\ket{\ell m}\\
&\quad= N_{\ell m}\left[\hat{D}_m\braket{\theta}{\ell}_m\right]\braket{\psi}{m} \\
&\quad= -\ell(\ell+1)\,N_{\ell m}\braket{\theta}{\ell}_m\braket{\psi}{m} \\
&\quad= -\ell(\ell+1)\braket{\theta \psi}{\ell m} \\
&\quad= -\ell(\ell+1)\,Y_{\ell m}(\theta,\psi)
\end{align*}
$$

...and we obtain the aforementioned result, as desired!

## Diagonalizing $\hat{\Lambda}$

Now that we have the operators of each sub-space eigenket, we can proceed to diagonalize $\hat{\Lambda}$ in its eigenbasis, $\ket{\ell m}$. Recall that, in terms of the operators we just introduced:

$$
\hat{\Lambda}=(\hat{A}\otimes\hat{1})-(\hat{W}\otimes\hat{L}_z^2)
$$

$\hat{L}_z$ owns the $\psi$ slot, and $\hat{D}_m=\hat{A}-m^2\hat{W}$ owns the $\theta$ slot once an $m$ has been picked.

*What does "diagonalize" actually mean here?* Find the basis where feeding $\hat{\Lambda}$ a basis ket only spits out that same ket. Technically, we already know the answer: it's $\ket{\ell m}$. But the point here is to watch *how* each of the two slots get diagonalized.

Denote the diagonalization of $\hat{\Lambda}$ in terms of matrix elements as follows:

$$
\mel{\ell' m'}{\hat{\Lambda}}{\ell m}\propto\delta_{\ell\ell'}\delta_{mm'}
$$

$\bra{\ell' m'}$ picks a row and $\ket{\ell m}$ picks a column.

### Diagonalize the $\psi$ Slot with $\ket{m}$

Sandwich $\hat{\Lambda}$ with the $m$-mode basis ($e^{im(\cdot)}$):

$$
\begin{align*}
&\bra{m'}\hat{\Lambda}\ket{m}\\
&\quad=\hat{A}\braket{m'}{m}-\hat{W}\mel{m'}{\hat{L}_z^2}{m}\\
&\quad=\hat{A}\braket{m'}{m}-m^2\hat{W}\braket{m'}{m}\\
&\quad=\braket{m'}{m}\,\delta_{m'm}\left(\hat{A}-m^2\hat{W}\right)\\
&\quad=\braket{m}{m} \delta_{m'm}\hat{D}_m
\end{align*}
$$

As a matrix, every entry is *itself* the $\theta$-operator:

$$
\begin{array}{c|ccccc}
 & \cdots & \ket{-1} & \ket{0} & \ket{1} & \cdots \\ \hline
\vdots & \ddots & & & & \\
\bra{-1} & & \braket{-1}{-1}\,\hat{D}_{-1} & 0 & 0 & \\
\bra{0} & & 0 & \braket{0}{0}\,\hat{D}_{0} & 0 & \\
\bra{1} & & 0 & 0 & \braket{1}{1}\,\hat{D}_{1} & \\
\vdots & & & & & \ddots
\end{array}
$$

Reassemble with $\hat{1}_\psi=\sum_m\frac{\ket{m}\bra{m}}{\braket{m}{m}}$ on both sides:

$$
\begin{align*}
\hat{\Lambda}&=\hat{1}_\psi\,\hat{\Lambda}\,\hat{1}_\psi\\
&=\sum_{m,m'}\frac{\ket{m'}\bra{m'}\hat{\Lambda}\ket{m}\bra{m}}{\braket{m'}{m'}\braket{m}{m}}\\
&=\sum_m\hat{D}_m\otimes\frac{\ket{m}\bra{m}}{\braket{m}{m}}
\end{align*}
$$

We can see that $\hat{D}_{m}$ are the building blocks but of $\hat{\Lambda}$, but what are the building blocks of $\hat{D}_{m}$? *In order to fully diagonalize $\hat{\Lambda}$ in its eigenbasis, we must diagonalize each $\hat{D}_m$ separately.*

### Diagonalize $\hat{D}_{m}$ with $\ket{\ell}_m$

Each block is diagonal in its own Legendre modes:

$$
\begin{align*} {}_{m}\!\mel{\ell'}{\hat{D}_m}{\ell}_m&=-\ell(\ell+1)\;{}_{m}\!\braket{\ell'}{\ell}_m\\
&=-\ell(\ell+1)\;{}_{m}\!\braket{\ell}{\ell}_m\,\delta_{\ell\ell'}
\end{align*}
$$

As a matrix, e.g. the $m=1$ block (the Legendre modes start at $\ell=|m|$; more on why below):

$$
\begin{array}{c|ccccc}
 & \cdots & \ket{1}_1 & \ket{2}_1 & \ket{3}_1 & \cdots \\ \hline
\vdots & \ddots & & & & \\ {}_{1}\!\bra{1} & & -2\;{}_{1}\!\braket{1}{1}_1 & 0 & 0 & \\ {}_{1}\!\bra{2} & & 0 & -6\;{}_{1}\!\braket{2}{2}_1 & 0 & \\ {}_{1}\!\bra{3} & & 0 & 0 & -12\;{}_{1}\!\braket{3}{3}_1 & \\
\vdots & & & & & \ddots
\end{array}
$$

Reassemble with $\hat{1}_\theta=\sum_{\ell\geq|m|}\frac{\ket{\ell}_m\,{}_{m}\!\bra{\ell}}{{}_{m}\!\braket{\ell}{\ell}_m}$ on both sides:

$$
\begin{align*}
\hat{D}_m&=\hat{1}_\theta\,\hat{D}_m\,\hat{1}_\theta\\
&=\sum_{\ell,\ell'}\frac{\ket{\ell'}_m\;{}_{m}\!\mel{\ell'}{\hat{D}_m}{\ell}_m\;{}_{m}\!\bra{\ell}}{{}_{m}\!\braket{\ell'}{\ell'}_m\;{}_{m}\!\braket{\ell}{\ell}_m}\\
&=\sum_{\ell\geq|m|}-\ell(\ell+1)\,\frac{\ket{\ell}_m\,{}_{m}\!\bra{\ell}}{{}_{m}\!\braket{\ell}{\ell}_m}
\end{align*}
$$

![The matrix of Λ as isometric blocks: only the diagonal m blocks survive, and opening the m equals one block shows it is diagonal again|620](/images/spherical-harmonics/block-diagonal.svg)

Combine slot by slot:

$$
\begin{align*}
&\left({}_{m'}\!\bra{\ell'}\otimes\bra{m'}\right)\hat{\Lambda}\left(\ket{\ell}_m\otimes\ket{m}\right)\\
&\quad={}_{m'}\!\bra{\ell'}\left(\bra{m'}\hat{\Lambda}\ket{m}\right)\ket{\ell}_m\\
&\quad=\braket{m}{m}\,\delta_{m'm}\;{}_{m'}\!\mel{\ell'}{\hat{D}_m}{\ell}_m\\
&\quad=-\ell(\ell+1)\,\braket{m}{m}\;{}_{m}\!\braket{\ell}{\ell}_m\,\delta_{\ell\ell'}\delta_{mm'}
\end{align*}
$$

As a matrix, ordered by $\ell$ (each column is $\ket{\ell}_m\ket{m}$):

$$
\begin{array}{c|ccccc}
 & \ket{0}_0\ket{0} & \ket{1}_{-1}\ket{-1} & \ket{1}_0\ket{0} & \ket{1}_1\ket{1} & \cdots \\ \hline {}_{0}\!\bra{0}\bra{0} & 0 & 0 & 0 & 0 & \\ {}_{-1}\!\bra{1}\bra{-1} & 0 & -2\braket{-1}{-1}\;{}_{-1}\!\braket{1}{1}_{-1} & 0 & 0 & \\ {}_{0}\!\bra{1}\bra{0} & 0 & 0 & -2\braket{0}{0}\;{}_{0}\!\braket{1}{1}_0 & 0 & \\ {}_{1}\!\bra{1}\bra{1} & 0 & 0 & 0 & -2\braket{1}{1}\;{}_{1}\!\braket{1}{1}_1 & \\
\vdots & & & & & \ddots
\end{array}
$$

Plugging $\hat{D}_m$ back into the result of the first-order diagonalization gives us:

$$
\begin{align*}
\hat{\Lambda}&=\sum_m\hat{D}_m\otimes\frac{\ket{m}\bra{m}}{\braket{m}{m}}\\
&=\sum_{m=-\infty}^{\infty}\;\sum_{\ell\geq|m|}-\ell(\ell+1)\,\frac{\ket{\ell}_m\,{}_{m}\!\bra{\ell}}{{}_{m}\!\braket{\ell}{\ell}_m}\\
&\qquad\otimes\frac{\ket{m}\bra{m}}{\braket{m}{m}}
\end{align*}
$$

*We have fully diagonalized $\hat{\Lambda}$.* Each term is a [projector](https://en.wikipedia.org/wiki/Projection_%28linear_algebra%29) onto one basis ket, weighted by its eigenvalue $-\ell(\ell+1)$.

### What $\hat{D}_m$ Is Actually Doing

Why does the $\hat{D}_m$ block start at $\ell=|m|$? Take the [expectation value](https://en.wikipedia.org/wiki/Expectation_value_%28quantum_mechanics%29) of $\hat{D}_m$ in a Legendre mode, with $\left<\cdot\right>\equiv\frac{{}_{m}\!\mel{\ell}{\cdot}{\ell}_m}{{}_{m}\!\braket{\ell}{\ell}_m}$:

$$
\begin{align*}
\left<\hat{D}_m\right>=\left<\hat{A}\right>-m^2\left<\hat{W}\right>&=-\ell(\ell+1)\\
\implies\ell(\ell+1)&=\underbrace{\left<-\hat{A}\right>}_{\text{bending along }\theta}\\
&\quad+\underbrace{m^2\left<\hat{W}\right>}_{\text{winding around }z}
\end{align*}
$$

$\frac{m^2}{\sin^2\theta}$ is a [centrifugal barrier](https://en.wikipedia.org/wiki/Effective_potential): winding around a small ring near a pole costs more than winding around the equator. So $P_{\ell}^{|m|}(\cos\theta)\propto\sin^{|m|}\theta$ vanishes at the poles, which single-valuedness demands anyway (every $\psi$ is the same point there). This is the coupling hiding in $\hat{D}_m$'s subscript: $\hat{W}$ lives in the $\theta$ slot, but its $m^2$ comes from the $\psi$ slot.

![Spheres at fixed ell equals four with growing m: the pattern gets pushed off the poles toward the equator|640](/images/spherical-harmonics/centrifugal.svg)

The floor: $\left<-\hat{A}\right>\geq0$ and $\frac{1}{\sin^2\theta}\geq1\implies\left<\hat{W}\right>\geq1$, so $\ell(\ell+1)\geq m^2\implies\ell\geq|m|$. *Winding $m$ times around $z$ costs at least that much curvature.*

Same pairs, two orderings:

$$
\sum_{m=-\infty}^{\infty}\;\sum_{\ell\geq|m|}\;=\;\sum_{\ell=0}^{\infty}\;\sum_{m=-\ell}^{\ell}
$$

Left is by block (how we diagonalized); right is by eigenvalue (how it's usually written). Each $\ell$-shell holds $2\ell+1$ [degenerate](https://en.wikipedia.org/wiki/Degenerate_energy_levels) modes: [rotations about $x$ and $y$](https://en.wikipedia.org/wiki/Wigner_D-matrix) shuffle the $m$'s within a shell without changing $\hat{\Lambda}$.

![The fully diagonal Λ ordered by ell: towers of height ell times ell plus one, in shells of two ell plus one equal towers|600](/images/spherical-harmonics/skyline.svg)

## References

1. R. L. Herman, *An Introduction to Mathematical Physics via Oscillations*, Chapter 9, "Oscillations in Higher Dimensions," University of North Carolina Wilmington (2012). [PDF](https://people.uncw.edu/hermanr/phy311/MathPhysBook/3D.pdf), licensed [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/us/).
2. F. W. J. Olver *et al.*, eds., *NIST Digital Library of Mathematical Functions*, [Chapter 14: Legendre and Related Functions](https://dlmf.nist.gov/14), in particular [§14.30, Spherical and Spheroidal Harmonics](https://dlmf.nist.gov/14.30).
3. D. J. Griffiths and D. F. Schroeter, *Introduction to Quantum Mechanics*, 3rd ed., Cambridge University Press (2018), Chapter 4.
4. J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics*, 3rd ed., Cambridge University Press (2020), Chapter 3.
5. [Spherical harmonics](https://en.wikipedia.org/wiki/Spherical_harmonics), *Wikipedia*.

## `<EOF>`

*We have fully diagonalized $\hat{\Lambda}$*, one slot at a time. Next time, we will see what this says about our basis, work out how to actually find the coefficients $c_{\ell m}$ of any $f$, and use them to solve Laplace's equation on a sphere.
