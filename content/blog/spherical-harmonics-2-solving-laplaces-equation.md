---
author: "Anish Goyal"
title: "The Beauty of Spherical Harmonics, Part 2: Solving Laplace's Equation"
slug: "spherical-harmonics-2-solving-laplaces-equation"
description: "Completeness, normalization, orthogonality, the eigenfunction expansion, the method of inversion and Fourier's trick, used to solve Laplace's equation on a sphere."
summary: "The diagonalized basis comes with the properties that find each coefficient. The eigenfunction expansion and the method of inversion solve Laplace's equation inside and outside a sphere, Fourier's trick fixes the constants, and a sphere held at V₀cos²θ puts it all together."
eyeCatcher: "But how do we actually determine $c_{\\ell m}$?"
tags: [spherical-harmonics, mathematics, physics, laplace-equation, electrostatics, fourier-series]
series: "The Beauty of Spherical Harmonics"
part: 2
readingtime: "21"
date: 2026-10-27T12:02:00-04:00
modified: 2026-10-27
---

[Last time](/blog/spherical-harmonics-1-building-the-basis/), we fully diagonalized $\hat{\Lambda}$, and each $\ell$-shell turned out to hold $2\ell+1$ degenerate modes. This time, we put that basis to work.

## What This Says About Our Basis

The basis is a choice. $-\ell(\ell+1)$ only pins down a $(2\ell+1)$-dimensional shell, and any orthonormal basis of it works. Ours also diagonalizes $\hat{L}_z$, i.e. we picked a $z$-axis, which is why it takes two labels ($\{\hat{\Lambda},\hat{L}_z\}$ is a [complete set of commuting observables](https://en.wikipedia.org/wiki/Complete_set_of_commuting_observables)). It's worth it when there's a symmetry axis: point $z$ along it, every $m\neq0$ term vanishes, and only the plain Legendre series in $\theta$ survives.

![The same azimuthally symmetric function with z along its axis (only m = 0 survives) and with z tilted (it spreads over every m of each ℓ-shell)|680](/images/spherical-harmonics/shell-rotation.svg)

## Towards Reconstructing $f$

Recall that we want to characterize any $f$ on the sphere as $\sum c_{\ell m}Y_{\ell m}$. *But how do we actually determine $c_{\ell m}$?*

*[Fourier's Trick](https://en.wikipedia.org/wiki/Generalized_Fourier_series):*

$$
\begin{align*}
c_{\ell m}&=\braket{\ell m}{f}\\
&= \int_{0}^{2\pi}\int_{0}^{\pi}\braket{\ell m}{\hat{n}}\braket{\hat{n}}{f}\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\psi\\
&=\int_{0}^{2\pi}\int_{0}^{\pi}Y_{\ell m}^*(\theta,\psi)\,f(\theta,\psi)\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\psi
\end{align*}
$$

It answers the question: *For any known function, what are the coefficients of that function in the eigenbasis?* It conveniently works for *any* choice of orthonormal basis. However, therein lies the [hamartia](https://en.wikipedia.org/wiki/Hamartia) of Fourier's Trick: in order to obtain the expansion coefficients of $f$, we simultaneously have to know what the hell $f$ *is.* And, under a general principle, we will never be given an analytical form of $f$ in a problem statement.

![Fourier's trick: multiply f by Y_ℓm point by point on the sphere, then integrate what is left|640](/images/spherical-harmonics/projection.svg)

Introducing: [*the eigenfunction expansion*](https://en.wikipedia.org/wiki/Sturm%E2%80%93Liouville_theory)

$$
\begin{align*}
\mel{\ell m}{\hat{\Lambda}}{\varphi}&=\sum_{\ell' m'}\underbrace{\mel{\ell m}{\hat{\Lambda}}{\ell' m'}}_{-\ell'(\ell'+1)\,\delta_{\ell\ell'}\delta_{mm'}}\\
&\qquad\times\braket{\ell' m'}{\varphi}\\
&=-\ell(\ell+1)\braket{\ell m}{\varphi}\\
&=-\ell(\ell+1)\,c_{\ell m}
\end{align*}
$$

It answers the question: *For an unknown function that we only know through an equation it satisfies, what does the operator in that equation do to the function's coefficients in that operator's eigenbasis?* The eigenfunction expansion allows us to find the expansion coefficients in the cases where Fourier's Trick fails, using the diagonal basis of some operator being applied to $\ket{\varphi}$.

We can see that $\hat{\Lambda}$ acting on $\ket{\varphi}$ in the diagonal basis multiplies $c_{\ell m}$ by $-\ell(\ell+1)$. This is no coincidence: since $\hat{\Lambda}$ is diagonal in $\ket{\ell m}$, it scales the $c_{\ell m}$ of $\ket{\varphi}$ by its eigenvalue. We can use this principle to find an analytical way to compute $c_{\ell m}$ (this will be done later).

## Important Properties

Now that we've diagonalized $\hat{\Lambda}$, its eigenbasis $\ket{\ell m}$ comes with a few special properties that allow us to actually find each $c_{\ell m}$ and reconstruct $f=\sum_{\ell m}c_{\ell m}Y_{\ell m}$.

### Completeness

[Summing over a basis](https://en.wikipedia.org/wiki/Orthonormal_basis) gives back *all* of $f$. In the case of the sphere, there are two completeness relations in play: one for the (rather inconvenient) position basis and the eigenbasis.

**Position basis (continuous).**

$$
\begin{align*}
\hat{1}&=\int_{0}^{2\pi}\int_{0}^{\pi}\ket{\hat{n}}\bra{\hat{n}}\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\psi\\
&=\underbrace{\int_{0}^{\pi}\ket{\theta}\bra{\theta}\sin\theta\,\mathrm{d}\theta}_{\hat{1}_\theta}\\
&\quad\otimes\underbrace{\int_{0}^{2\pi}\ket{\psi}\bra{\psi}\,\mathrm{d}\psi}_{\hat{1}_\psi}
\end{align*}
$$

With $\braket{\theta}{\ell}_{m}=P_{\ell}^{|m|}(\cos\theta)$ and $\braket{\psi}{m}=e^{im\psi}$, this is what turns every bra-ket in the sections below into an integral over the sphere.

**Spherical eigenbasis (discrete).**

$$
\hat{1}=\sum_{\ell=0}^{\infty}\sum_{m=-\ell}^{\ell}\ket{\ell m}\bra{\ell m}
$$

Implications: any two functions with the same $\braket{\ell m}{\cdot}$ are the same function. This is what allows for boundary condition matching, one mode at a time. We will use this property as a weapon later on.

Strategically inserting $\hat{1}$ into an inner product expresses it as a sum (or integral, in the case of continuous bases):

$$
\begin{align*}
f(\hat{n})&=\braket{\hat{n}}{f}\\
&=\sum_{\ell m}\braket{\hat{n}}{\ell m}\braket{\ell m}{f}\\
&=\sum_{\ell m}c_{\ell m}\,Y_{\ell m}(\hat{n})
\end{align*}
$$

We can now plainly see that we are *very close* to our original goal of expressing $f$ as a sum. There's just a couple of more things left to handle to get a more thorough, low entropy description of $f$.

### Normalization

Every basis ket gets scaled so that its inner product with itself is "one". For a discrete basis that's literally $1$; for a [continuous basis](https://en.wikipedia.org/wiki/Dirac_delta_function), it's $\delta(\cdot)$. An eigenvalue equation only fixes a ket up to a constant. Choosing that constant is what $N_{\ell m}$ does.

**Position basis (continuous).** Demand that $\hat{1}_\theta$ and $\hat{1}_\psi$ each hand back $f$:

$$
\begin{align*}
\theta:&\quad\braket{\theta'}{f}\\
&\quad=\int_{0}^{\pi}\braket{\theta'}{\theta}\braket{\theta}{f}\sin\theta\,\mathrm{d}\theta\\
&\quad\overset{!}{=}f(\theta')\\
&\quad\implies\braket{\theta'}{\theta}=\frac{\delta(\theta-\theta')}{\sin\theta}\\
\psi:&\quad\braket{\psi'}{f}\\
&\quad=\int_{0}^{2\pi}\braket{\psi'}{\psi}\braket{\psi}{f}\,\mathrm{d}\psi\\
&\quad\overset{!}{=}f(\psi')\\
&\quad\implies\braket{\psi'}{\psi}=\delta(\psi-\psi')
\end{align*}
$$

$$
\begin{align*}
\implies\braket{\hat{n}'}{\hat{n}}&=\braket{\theta'}{\theta}\braket{\psi'}{\psi}\\
&=\underbrace{\frac{1}{\sin\theta}}_{\text{"}N^2\text{"}}\delta(\theta-\theta')\,\underbrace{1}_{\text{"}N^2\text{"}}\delta(\psi-\psi')
\end{align*}
$$

The $\frac{1}{\sin\theta}$ plays the role of $N^2$ for the continuous kets. Where it lives is a choice: we put $\sin\theta$ in the measure of $\hat{1}_\theta$, so the inner product has to carry $\frac{1}{\sin\theta}$ to undo it.

**Spherical eigenbasis (discrete).** Recall that we wrote $Y_{\ell m}=N_{\ell m}P_{\ell}^{|m|}(\cos\theta)\,e^{im\psi}$ in [Part 1](/blog/spherical-harmonics-1-building-the-basis/), and I said "we would come back to finding $N_{\ell m}$ later." We can now use the [normalization property](https://en.wikipedia.org/wiki/Spherical_harmonics#Orthogonality_and_normalization) of $\ket{\ell m}$ to find $N_{\ell m}$:

$$
\begin{align*}
1=\braket{\ell m}{\ell m}&=N_{\ell m}^2\,\braket{m}{m}\;{}_{m}\!\braket{\ell}{\ell}_m\\
&=N_{\ell m}^2\underbrace{\int_{0}^{2\pi}\left|e^{im\psi}\right|^2\mathrm{d}\psi}_{2\pi}\\
&\quad\times\underbrace{\int_{0}^{\pi}\left[P_{\ell}^{|m|}(\cos\theta)\right]^2\sin\theta\,\mathrm{d}\theta}_{\frac{2}{2\ell+1}\frac{(\ell+|m|)!}{(\ell-|m|)!}}\\
\implies N_{\ell m}&=\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-|m|)!}{(\ell+|m|)!}}
\end{align*}
$$

![Raw P_3^|m|(cos θ)cos(mψ) on one shared colour scale balloons with |m|; multiplying by N_3m evens them out|560](/images/spherical-harmonics/raw-vs-normalized.svg)

<details>
<summary>Where ${}_{m}\!\braket{\ell}{\ell}_m=\frac{2}{2\ell+1}\frac{(\ell+|m|)!}{(\ell-|m|)!}$ comes from</summary>

Only $|m|$ enters, so take $m\geq0$ and write

$$
I_{\ell m}\equiv{}_{m}\!\braket{\ell}{\ell}_m=\int_{0}^{\pi}\left[P_{\ell}^{m}(\cos\theta)\right]^2\sin\theta\,\mathrm{d}\theta
$$

*Start at $m=0$.* Same substitution $x=\cos\theta$ as in the Legendre equation, then [Rodrigues](https://en.wikipedia.org/wiki/Rodrigues%27_formula) and $\ell$ integrations by parts (every boundary term still carries a factor of $x^2-1$, which vanishes at $x=\pm1$):

$$
\begin{align*}
I_{\ell 0}&=\int_{0}^{\pi}\left[P_{\ell}(\cos\theta)\right]^2\sin\theta\,\mathrm{d}\theta\\
&=\frac{1}{(2^\ell\ell!)^2}\int_{-1}^{1}\partial_{x}^{\ell}(x^2-1)^\ell\\
&\qquad\times\partial_{x}^{\ell}(x^2-1)^\ell\,\mathrm{d}x\\
&=\frac{(-1)^\ell}{(2^\ell\ell!)^2}\int_{-1}^{1}(x^2-1)^\ell\\
&\qquad\times\underbrace{\partial_{x}^{2\ell}(x^2-1)^\ell}_{(2\ell)!}\,\mathrm{d}x\\
&=\frac{(2\ell)!}{(2^\ell\ell!)^2}\int_{-1}^{1}(1-x^2)^\ell\,\mathrm{d}x\\
&=\frac{(2\ell)!}{(2^\ell\ell!)^2}\underbrace{\int_{0}^{\pi}\sin^{2\ell+1}\theta\,\mathrm{d}\theta}_{\text{Wallis: }\frac{2\,(2^\ell\ell!)^2}{(2\ell+1)!}}\\
&=\frac{2}{2\ell+1}
\end{align*}
$$

*Climb in $m$.* From

$$
P_{\ell}^{m}(\cos\theta)=(-1)^m\sin^m\theta\left.\partial_{x}^{m}P_{\ell}(x)\right\vert_{x=\cos\theta}
$$

and $\partial_{\theta}=-\sin\theta\,\partial_{x}$:

$$
P_{\ell}^{m+1}(\cos\theta)=\left(\partial_{\theta}-m\cot\theta\right)P_{\ell}^{m}(\cos\theta)
$$

Integrating by parts against $\sin\theta\,\mathrm{d}\theta$ (the boundary term carries $\sin\theta$ and dies at the poles), the adjoint of $\partial_{\theta}-m\cot\theta$ is $-\left(\partial_{\theta}+(m+1)\cot\theta\right)$. Their product, with $\cot^2\theta=\frac{1}{\sin^2\theta}-1$:

$$
\begin{align*}
&-\left(\partial_{\theta}+(m+1)\cot\theta\right)\\
&\quad\times\left(\partial_{\theta}-m\cot\theta\right)\\
&\quad=-\Big[\partial_{\theta}^2+\cot\theta\,\partial_{\theta}\\
&\qquad\quad+\frac{m}{\sin^2\theta}-m(m+1)\cot^2\theta\Big]\\
&\quad=-\Big[\underbrace{\partial_{\theta}^2+\cot\theta\,\partial_{\theta}-\frac{m^2}{\sin^2\theta}}_{\hat{D}_m}\Big]\\
&\qquad-m(m+1)
\end{align*}
$$

So:

$$
\begin{align*}
I_{\ell,m+1}&=\int_{0}^{\pi}P_{\ell}^{m}(\cos\theta)\\
&\qquad\times\left[-\hat{D}_m-m(m+1)\right]\\
&\qquad\times P_{\ell}^{m}(\cos\theta)\sin\theta\,\mathrm{d}\theta\\
&=\left[\ell(\ell+1)-m(m+1)\right]I_{\ell m}\\
&=(\ell-m)(\ell+m+1)\,I_{\ell m}
\end{align*}
$$

$\hat{D}_m$ shows up again, and its eigenvalue does all the work. Stacking the steps:

$$
\begin{align*}
I_{\ell m}&=\frac{2}{2\ell+1}\prod_{k=0}^{m-1}(\ell-k)(\ell+k+1)\\
&=\frac{2}{2\ell+1}\cdot\frac{\ell!}{(\ell-m)!}\cdot\frac{(\ell+m)!}{\ell!}\\
&=\frac{2}{2\ell+1}\frac{(\ell+m)!}{(\ell-m)!}
\end{align*}
$$

</details>

Implication: previously, with the raw kets $\ket{\ell}_m\ket{m}$, every result carried $\braket{m}{m}\;{}_{m}\!\braket{\ell}{\ell}_m=2\pi\cdot\frac{2}{2\ell+1}\frac{(\ell+|m|)!}{(\ell-|m|)!}$ around. Plugging in the actual values, that's exactly $\frac{1}{N_{\ell m}^2}$.

The diagonalized $\hat{\Lambda}$:

$$
\begin{align*}
\hat{\Lambda}&=\sum_{m}\sum_{\ell\geq|m|}-\ell(\ell+1)\,\frac{\ket{\ell}_m\,{}_{m}\!\bra{\ell}}{{}_{m}\!\braket{\ell}{\ell}_m}\\
&\qquad\otimes\frac{\ket{m}\bra{m}}{\braket{m}{m}}\\
&=\sum_{m}\sum_{\ell\geq|m|}-\ell(\ell+1)\,\frac{1}{2\pi}\cdot\frac{2\ell+1}{2}\frac{(\ell-|m|)!}{(\ell+|m|)!}\\
&\qquad\times\Big(\ket{\ell}_m\ket{m}\Big)\Big({}_{m}\!\bra{\ell}\bra{m}\Big)\\
&=\sum_{m}\sum_{\ell\geq|m|}-\ell(\ell+1)\left(\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-|m|)!}{(\ell+|m|)!}}\right)^2\\
&\qquad\times\Big(\ket{\ell}_m\ket{m}\Big)\Big({}_{m}\!\bra{\ell}\bra{m}\Big)\\
&=\sum_{m}\sum_{\ell\geq|m|}-\ell(\ell+1)\\
&\qquad\times\left(\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-|m|)!}{(\ell+|m|)!}}\,\ket{\ell}_m\ket{m}\right)\\
&\qquad\times\left(\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-|m|)!}{(\ell+|m|)!}}\,{}_{m}\!\bra{\ell}\bra{m}\right)\\
&\longrightarrow\;\sum_{\ell m}-\ell(\ell+1)\ket{\ell m}\bra{\ell m}
\end{align*}
$$

The matrix elements:

$$
\begin{align*}
&\left({}_{m'}\!\bra{\ell'}\otimes\bra{m'}\right)\hat{\Lambda}\left(\ket{\ell}_m\otimes\ket{m}\right)\\
&\quad=-\ell(\ell+1)\cdot2\pi\cdot\frac{2}{2\ell+1}\frac{(\ell+|m|)!}{(\ell-|m|)!}\\
&\qquad\times\delta_{\ell\ell'}\delta_{mm'}\\
&\left(\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-|m|)!}{(\ell+|m|)!}}\right)^2\\
&\quad\times\left({}_{m'}\!\bra{\ell'}\otimes\bra{m'}\right)\hat{\Lambda}\left(\ket{\ell}_m\otimes\ket{m}\right)\\
&\quad=-\ell(\ell+1)\left(\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-|m|)!}{(\ell+|m|)!}}\right)^2\\
&\qquad\times2\pi\cdot\frac{2}{2\ell+1}\frac{(\ell+|m|)!}{(\ell-|m|)!}\,\delta_{\ell\ell'}\delta_{mm'}\\
&\quad=-\ell(\ell+1)\,\frac{2\ell+1}{4\pi}\frac{(\ell-|m|)!}{(\ell+|m|)!}\\
&\qquad\times\frac{4\pi}{2\ell+1}\frac{(\ell+|m|)!}{(\ell-|m|)!}\,\delta_{\ell\ell'}\delta_{mm'}\\
&\longrightarrow\;\mel{\ell' m'}{\hat{\Lambda}}{\ell m}=-\ell(\ell+1)\,\delta_{\ell\ell'}\delta_{mm'}
\end{align*}
$$

The coefficients of $f$. In the raw modes, $f=\sum_{\ell m}a_{\ell m}P_{\ell}^{|m|}(\cos\theta)\,e^{im\psi}$:

$$
\begin{align*}
a_{\ell m}&=\frac{\left({}_{m}\!\bra{\ell}\otimes\bra{m}\right)\ket{f}}{\braket{m}{m}\;{}_{m}\!\braket{\ell}{\ell}_m}\\
&=\frac{1}{2\pi\cdot\frac{2}{2\ell+1}\frac{(\ell+|m|)!}{(\ell-|m|)!}}\\
&\quad\times\int_{0}^{2\pi}\int_{0}^{\pi}P_{\ell}^{|m|}(\cos\theta)\,e^{-im\psi}\\
&\qquad\times f(\theta,\psi)\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\psi
\end{align*}
$$

In the normalized modes:

$$
\begin{align*}
c_{\ell m}=\braket{\ell m}{f}&=\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-|m|)!}{(\ell+|m|)!}}\\
&\quad\times\int_{0}^{2\pi}\int_{0}^{\pi}P_{\ell}^{|m|}(\cos\theta)\,e^{-im\psi}\\
&\qquad\times f(\theta,\psi)\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\psi\\
&=\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-|m|)!}{(\ell+|m|)!}}\\
&\quad\times2\pi\cdot\frac{2}{2\ell+1}\frac{(\ell+|m|)!}{(\ell-|m|)!}\,a_{\ell m}\\
&=\sqrt{\frac{4\pi}{2\ell+1}\frac{(\ell+|m|)!}{(\ell-|m|)!}}\;a_{\ell m}\\
&\longrightarrow\;c_{\ell m}=\frac{a_{\ell m}}{N_{\ell m}}
\end{align*}
$$

### Orthogonality

A projection kills every term in the sum but one.

**Position basis (continuous).** This is just the normalization from before:

$$
\begin{align*}
\braket{\hat{n}'}{\hat{n}}&=\frac{\delta(\theta-\theta')}{\sin\theta}\,\delta(\psi-\psi')\\
&=0\qquad(\hat{n}'\neq\hat{n})
\end{align*}
$$

**Spherical eigenbasis (discrete).**

$$
\begin{align*}
\braket{\ell' m'}{\ell m}&=N_{\ell' m'}N_{\ell m}\underbrace{\int_{0}^{2\pi}e^{i(m-m')\psi}\,\mathrm{d}\psi}_{\braket{m'}{m}}\\
&\quad\times\underbrace{\int_{0}^{\pi}P_{\ell'}^{|m'|}(\cos\theta)\,P_{\ell}^{|m|}(\cos\theta)\sin\theta\,\mathrm{d}\theta}_{{}_{m'}\!\braket{\ell'}{\ell}_m}
\end{align*}
$$

$\psi$ slot: for $m\neq m'$, $\braket{m'}{m}=\frac{e^{2\pi i(m-m')}-1}{i(m-m')}=0$, since $m-m'\in\mathbb{Z}$.

$\theta$ slot (same $m$): previously, we had

$$
\hat{D}_m P_{\ell}^{|m|}(\cos\theta)=-\ell(\ell+1)P_{\ell}^{|m|}(\cos\theta)
$$

with $\hat{D}_m=\frac{1}{\sin\theta}\partial_{\theta}(\sin\theta\,\partial_{\theta})-\frac{m^2}{\sin^2\theta}$. So:

$$
\begin{align*}
&\left[\ell'(\ell'+1)-\ell(\ell+1)\right]{}_{m}\!\braket{\ell'}{\ell}_m\\
&\quad=\int_{0}^{\pi}\Big[P_{\ell'}^{|m|}(\cos\theta)\,\hat{D}_m P_{\ell}^{|m|}(\cos\theta)\\
&\qquad\quad-P_{\ell}^{|m|}(\cos\theta)\,\hat{D}_m P_{\ell'}^{|m|}(\cos\theta)\Big]\sin\theta\,\mathrm{d}\theta\\
&\quad=\Big[\sin\theta\Big(P_{\ell'}^{|m|}(\cos\theta)\,\partial_{\theta}P_{\ell}^{|m|}(\cos\theta)\\
&\qquad\quad-P_{\ell}^{|m|}(\cos\theta)\,\partial_{\theta}P_{\ell'}^{|m|}(\cos\theta)\Big)\Big]_{0}^{\pi}\\
&\quad=0
\end{align*}
$$

$\sin\theta$ vanishes at the poles, and $P_{\ell}^{|m|}(\cos\theta)$ is finite there. $Q_{\ell}^{m}(\cos\theta)$ would blow up and keep this term alive, which is the real reason we threw it out.

![Around a ring, cos(2ψ)cos(3ψ) has as much above zero as below, while cos²(2ψ) never dips|560](/images/spherical-harmonics/orthogonality-ring.svg)

Together with the normalization:

$$
\braket{\ell' m'}{\ell m}=\delta_{\ell\ell'}\delta_{mm'}
$$

Implications: each coefficient comes from its own projection, so adding more terms never changes the ones already found. The boundary conditions that quantized $m$ and $\ell$ (periodicity, finiteness at the poles) are the same ones that [make the basis orthogonal](https://en.wikipedia.org/wiki/Sturm%E2%80%93Liouville_theory).

### Eigenfunction Expansion

It finds the coefficients of an *unknown* function from an equation it satisfies. In the operator's eigenbasis, the operator only rescales each coefficient, so the equation splits mode by mode.

Example: [Laplace with boundary data](https://en.wikipedia.org/wiki/Dirichlet_problem). Given $\varphi\equiv V$ on $r=R$, and nothing else about $\varphi$ except $\hat{\nabla}^2\varphi=0$. With $\hat{\nabla}^2=\frac{1}{r^2}\partial_{r}(r^2\partial_{r})+\frac{1}{r^2}\hat{\Lambda}$, sandwich with $\bra{\ell' m'}$:

$$
\begin{align*}
\mel{\ell' m'}{\hat{\nabla}^2}{\varphi}&=\frac{1}{r^2}\partial_{r}\left(r^2\partial_{r}\braket{\ell' m'}{\varphi}\right)\\
&\quad+\frac{1}{r^2}\mel{\ell' m'}{\hat{\Lambda}}{\varphi}\\
&=0
\end{align*}
$$

$\bra{\ell' m'}$ has no $r$ in it, so only the $\hat{\Lambda}$ term cares about the basis. Previously, we had

$$
\mel{\ell' m'}{\hat{\Lambda}}{\varphi}=-\ell'(\ell'+1)\braket{\ell' m'}{\varphi}
$$

The $\delta$'s leave exactly one term. In the position basis there is no such luck:

$$
\mel{\hat{n}}{\hat{\Lambda}}{\varphi}\approx\frac{4}{\varepsilon^2}\left(\left<\varphi\right>_{\varepsilon}-\varphi(\hat{n})\right)
$$

As we saw before, each $\hat{n}$ is tied to its nearest neighbors (nonzero off-diagonals), so the equation never comes apart.

One equation per mode. Plug back in and drop the primes:

$$
\left[\frac{1}{r^2}\partial_{r}\left(r^2\partial_{r}\right)-\frac{\ell(\ell+1)}{r^2}\right]\braket{\ell m}{\varphi(r)}=0
$$

Every term scales the same way under $r\to\lambda r$, so try $\braket{\ell m}{\varphi(r)}\propto r^{k}$:

$$
\begin{align*}
&\left[k(k+1)-\ell(\ell+1)\right]r^{k-2}=0\\
&\implies k=\ell\ \text{ or }\ k=-(\ell+1)
\end{align*}
$$

Inside, $r^{-(\ell+1)}$ blows up at the origin $\implies\braket{\ell m}{\varphi(r)}=A_{\ell m}r^{\ell}$. Outside, $r^{\ell}$ blows up at infinity $\implies\braket{\ell m}{\varphi(r)}=B_{\ell m}r^{-(\ell+1)}$ (the Method of Inversion below hands this one over for free).

Match the boundary. $\varphi(R)=V\implies A_{\ell m}R^{\ell}=\braket{\ell m}{V}$:

$$
\braket{\ell m}{\varphi(r)}=\left(\frac{r}{R}\right)^{\ell}\braket{\ell m}{V}
$$

I said we would find an analytical way to compute $c_{\ell m}$ later; this is it. The left side comes out of the equation, and the only projection actually computed is $\braket{\ell m}{V}$, on the known $V$.

*Why not just Fourier's-trick $V$?* That only gives $\varphi$'s coefficients at $r=R$. The sandwiched equation says how each one evolves in $r$. Same split as in QM: Fourier's trick on $\psi(x,0)$ gives the starting values, and sandwiching the [Schrödinger equation](https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation) with $\bra{n}$ gives each one's $e^{-iE_nt}$. Laplace is second order in $r$, so it needs one more condition than Schrödinger: regularity at $0$ (inside) or at $\infty$ (outside).

![Shrinking toward the centre, (r/R)^ℓ⟨ℓm|V⟩ kills the high-ℓ wiggles first|480](/images/spherical-harmonics/radial-fade.svg)

Example: no leftover coordinate. For $\hat{\Lambda}\ket{u}=\ket{g}$, there's nothing to solve, only a division:

$$
\braket{\ell m}{u}=-\frac{\braket{\ell m}{g}}{\ell(\ell+1)}
$$

Equivalently, as an operator:

$$
\hat{\Lambda}^{-1}=\sum_{\ell\geq1}\sum_{m=-\ell}^{\ell}\frac{-1}{\ell(\ell+1)}\ket{\ell m}\bra{\ell m}
$$

$\hat{\Lambda}Y_{00}=0$, so $\braket{0\,0}{u}$ has to be supplied separately (the $+C$), and $\braket{0\,0}{g}$ has to vanish. E.g.

$$
g=-4Y_{10}-30Y_{21}\implies u=C\,Y_{00}+2Y_{10}+5Y_{21}
$$

Implication: the full solve is three moves: (1) sandwich the equation (eigenbasis only): one equation per coefficient of the unknown; (2) sandwich the known data (Fourier's trick, any orthonormal basis): fixes the constants; (3) sum the modes (completeness).

### Method of Inversion

Previously, inside the sphere we had

$$
\braket{\ell m}{\varphi_{\text{in}}(r)}=\left(\frac{r}{R}\right)^{\ell}\braket{\ell m}{V}
$$

Outside, the same $V$ needs the other root, $r^{-(\ell+1)}$. *Can the interior solution be recycled into the exterior one instead of solving again?*

Swap inside and outside while leaving the sphere fixed: reflect the radius through the sphere,

$$
r\;\longmapsto\;\frac{R^2}{r}
$$

$r<R\iff\frac{R^2}{r}>R$, the sphere $r=R$ stays put, and the center goes to infinity.

First guess: evaluate the interior solution at the reflected point,

$$
\varphi_{\text{out}}(r,\theta,\psi)\overset{?}{=}\varphi_{\text{in}}\!\left(\frac{R^2}{r},\theta,\psi\right)
$$

On $r=R$ this is $\varphi_{\text{in}}(R,\theta,\psi)=V(\theta,\psi)$, so the boundary is fine. *But does it solve Laplace?*

The reflection only touches $r$, and $\bra{\ell m}$ has no $r$ in it, so sandwich:

$$
\begin{align*}
\braket{\ell m}{\varphi_{\text{in}}(R^2/r)}&=\left(\frac{R^2/r}{R}\right)^{\ell}\braket{\ell m}{V}\\
&=\left(\frac{R}{r}\right)^{\ell}\braket{\ell m}{V}\\
&\propto r^{-\ell}
\end{align*}
$$

Previously, $r^{k}$ solves the radial equation only if $k(k+1)=\ell(\ell+1)$. At $k=-\ell$:

$$
(-\ell)(-\ell+1)=\ell(\ell-1)\neq\ell(\ell+1)
$$

*The guess fails.* It lands on $r^{-\ell}$, one power short of $r^{-(\ell+1)}$.

*Why one power short?* Complete the square:

$$
k(k+1)=\left(k+\tfrac{1}{2}\right)^2-\tfrac{1}{4}
$$

$k(k+1)$ only sees how far $k$ is from $-\frac{1}{2}$, and the two roots sit symmetrically about it: $\ell=-\frac{1}{2}+\left(\ell+\frac{1}{2}\right)$ and $-(\ell+1)=-\frac{1}{2}-\left(\ell+\frac{1}{2}\right)$. The reflection sends $r^{k}\mapsto r^{-k}$, a mirror about $0$. A mirror about $-\frac{1}{2}$ is $k\mapsto-1-k$: the same flip, followed by one extra factor of $r^{-1}$.

So multiply the guess by a power of $r$ and a constant, and let the equation pick them:

$$
\varphi_{\text{out}}(r,\theta,\psi)=C\,r^{p}\,\varphi_{\text{in}}\!\left(\frac{R^2}{r},\theta,\psi\right)
$$

$$
\begin{align*}
\braket{\ell m}{\varphi_{\text{out}}(r)}&=C\,r^{p}\left(\frac{R}{r}\right)^{\ell}\braket{\ell m}{V}\\
&\propto r^{p-\ell}\\
p-\ell&=-(\ell+1)\\
\implies p&=-1
\end{align*}
$$

The $\ell$ cancels: *one* power of $r$ fixes every mode at once, so the map acts on $\varphi_{\text{in}}$ as a whole, with no expansion needed.

The boundary fixes $C$. At $r=R$:

$$
\begin{align*}
\varphi_{\text{out}}(R,\theta,\psi)&=\frac{C}{R}\,\varphi_{\text{in}}(R,\theta,\psi)\\
&=\frac{C}{R}\,V(\theta,\psi)\\
&\overset{!}{=}V(\theta,\psi)\\
\implies C&=R
\end{align*}
$$

Together:

$$
\varphi_{\text{out}}(r,\theta,\psi)=\frac{R}{r}\,\varphi_{\text{in}}\!\left(\frac{R^2}{r},\theta,\psi\right)
$$

$\frac{1}{r}$ makes it solve Laplace; $R$ makes it equal $V$ on the sphere. This is the [Method of Inversion](https://en.wikipedia.org/wiki/Kelvin_transform). Mode by mode, it hands over the exterior solution with its constant already fixed, $B_{\ell m}=R^{\ell+1}\braket{\ell m}{V}$:

$$
\begin{align*}
\braket{\ell m}{\varphi_{\text{out}}(r)}&=\frac{R}{r}\left(\frac{R}{r}\right)^{\ell}\braket{\ell m}{V}\\
&=\left(\frac{R}{r}\right)^{\ell+1}\braket{\ell m}{V}
\end{align*}
$$

![r ↦ R²/r turns the ball inside out: (r/R)^ℓ P_ℓ(cos θ) inside and (R/r)^(ℓ+1) P_ℓ(cos θ) outside agree on the sphere r = R|720](/images/spherical-harmonics/inversion.svg)

Implication: solve the interior problem once, and the exterior one is a substitution away.

### Fourier's Trick

It finds the coefficients of a *known* function. Same $\delta$ collapse as before, but with no operator in the sandwich, so it works in *any* orthonormal basis.

**Position basis (continuous).** The $\delta$ from before collapses the integral, and the "coefficient" is just the value of $f$:

$$
\begin{align*}
\braket{\hat{n}'}{f}&=\int_{0}^{2\pi}\int_{0}^{\pi}\braket{\hat{n}'}{\hat{n}}\braket{\hat{n}}{f}\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\psi\\
&=f(\hat{n}')
\end{align*}
$$

**Spherical eigenbasis (discrete).**

$$
\begin{align*}
\braket{\ell' m'}{f}&=\sum_{\ell m}c_{\ell m}\underbrace{\braket{\ell' m'}{\ell m}}_{\delta_{\ell\ell'}\delta_{mm'}}\\
&=c_{\ell' m'}
\end{align*}
$$

To actually compute it, insert the position-basis completeness. Previously, we had

$$
\begin{align*}
c_{\ell m}&=\braket{\ell m}{f}\\
&=\int_{0}^{2\pi}\int_{0}^{\pi}Y_{\ell m}^*(\theta,\psi)\,f(\theta,\psi)\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\psi
\end{align*}
$$

So Fourier's trick is a change of basis: continuous components $f(\theta,\psi)$ in, discrete components $c_{\ell m}$ out.

*Can the double integral be done one slot at a time?* Yes: $\bra{\ell m}=N_{\ell m}\,{}_{m}\!\bra{\ell}\otimes\bra{m}$ splits along the same two slots we diagonalized, so the projection splits into the same two steps.

![Fourier's trick one slot at a time: a Fourier series around each latitude ring in ψ, then each f_m expanded in its own Legendre modes in θ|700](/images/spherical-harmonics/two-slots.svg)

Step 1 ($\psi$ slot): at fixed $\theta$, each latitude ring is periodic, so [Fourier-series](https://en.wikipedia.org/wiki/Fourier_series) it:

$$
\begin{align*}
f(\theta,\psi)&=\sum_{m}f_m(\theta)\,e^{im\psi}\\
f_m(\theta)&=\frac{\braket{m}{f}}{\braket{m}{m}}\\
&=\frac{1}{2\pi}\int_{0}^{2\pi}f(\theta,\psi)\,e^{-im\psi}\,\mathrm{d}\psi
\end{align*}
$$

Only $\psi$ gets integrated, so $f_m$ is still a function of $\theta$. Since $\hat{\Lambda}$ never mixes $m$'s, each $f_m$ is handled alone by $\hat{D}_m$.

Step 2 ($\theta$ slot): expand each $f_m$ in its own block's eigenfunctions:

$$
\begin{align*}
f_m(\theta)&=\sum_{\ell\geq|m|}a_{\ell m}\,P_{\ell}^{|m|}(\cos\theta)\\
a_{\ell m}&=\frac{{}_{m}\!\braket{\ell}{f_m}}{{}_{m}\!\braket{\ell}{\ell}_m}
\end{align*}
$$

Different $m$, different $\hat{D}_m$, different family of modes. The only boundary condition is finiteness at the poles.

Previously, we had $c_{\ell m}=\frac{a_{\ell m}}{N_{\ell m}}$, so the two steps reassemble $f$:

$$
\begin{align*}
f(\theta,\psi)&=\sum_{m}\sum_{\ell\geq|m|}a_{\ell m}\,P_{\ell}^{|m|}(\cos\theta)\,e^{im\psi}\\
&=\sum_{m}\sum_{\ell\geq|m|}c_{\ell m}\,Y_{\ell m}(\theta,\psi)
\end{align*}
$$

Example: Laplace with boundary data. Previously, inside the sphere we had $\braket{\ell m}{\varphi(r)}=\left(\frac{r}{R}\right)^{\ell}\braket{\ell m}{V}$. Summing the modes:

$$
\begin{align*}
\varphi(r,\theta,\psi)&=\sum_{\ell m}\left(\frac{r}{R}\right)^{\ell}\braket{\ell m}{V}\\
&\qquad\times Y_{\ell m}(\theta,\psi)
\end{align*}
$$

The only integral left is Fourier's trick on the known $V$:

$$
\braket{\ell m}{V}=\int_{0}^{2\pi}\int_{0}^{\pi}Y_{\ell m}^*(\theta,\psi)\,V(\theta,\psi)\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\psi
$$

With azimuthal symmetry and plain $P_{\ell}(\cos\theta)$ (the usual convention), the $\psi$ slot cancels and it's "overlap over length squared":

$$
\begin{align*}
\varphi(r,\theta)&=\sum_{\ell}A_{\ell}r^{\ell}P_{\ell}(\cos\theta)\\
A_{\ell}R^{\ell}&=\frac{\braket{\ell}{V}}{\braket{\ell}{\ell}}\\
&=\frac{2\ell+1}{2}\int_{0}^{\pi}V(\theta)\,P_{\ell}(\cos\theta)\sin\theta\,\mathrm{d}\theta
\end{align*}
$$

## Putting It Together: $V=V_0\cos^2\theta$

Previously, the full solve was three moves: sandwich the equation, sandwich the data, sum the modes. *What does that look like on an actual boundary?* Hold the sphere at $V(\theta)=V_0\cos^2\theta$ and find $\varphi$ inside and outside.

Sandwich the equation. Previously, we had, inside and (by inversion) outside:

$$
\begin{align*}
\braket{\ell m}{\varphi_{\text{in}}(r)}&=\left(\frac{r}{R}\right)^{\ell}\braket{\ell m}{V}\\
\braket{\ell m}{\varphi_{\text{out}}(r)}&=\left(\frac{R}{r}\right)^{\ell+1}\braket{\ell m}{V}
\end{align*}
$$

Sandwich the data. $V$ has no $\psi$, so only $m=0$ survives, and previously we had

$$
A_{\ell}R^{\ell}=\frac{2\ell+1}{2}\int_{0}^{\pi}V(\theta)\,P_{\ell}(\cos\theta)\sin\theta\,\mathrm{d}\theta
$$

With $\int_{0}^{\pi}\cos^{2k}\theta\,\sin\theta\,\mathrm{d}\theta=\frac{2}{2k+1}$:

$$
\begin{align*}
A_0&=\frac{1}{2}\int_{0}^{\pi}V_0\cos^2\theta\,\sin\theta\,\mathrm{d}\theta\\
&=\frac{V_0}{2}\cdot\frac{2}{3}\\
&=\frac{V_0}{3}
\end{align*}
$$

$$
\begin{align*}
A_2R^2&=\frac{5}{2}\int_{0}^{\pi}V_0\cos^2\theta\,\frac{3\cos^2\theta-1}{2}\,\sin\theta\,\mathrm{d}\theta\\
&=\frac{5V_0}{4}\left(3\cdot\frac{2}{5}-\frac{2}{3}\right)\\
&=\frac{2V_0}{3}
\end{align*}
$$

*What about every other $\ell$?* These two already rebuild $V$ exactly:

$$
\begin{align*}
&\frac{V_0}{3}P_0(\cos\theta)+\frac{2V_0}{3}P_2(\cos\theta)\\
&\quad=\frac{V_0}{3}+\frac{2V_0}{3}\cdot\frac{3\cos^2\theta-1}{2}\\
&\quad=\frac{V_0}{3}+V_0\cos^2\theta-\frac{V_0}{3}\\
&\quad=V_0\cos^2\theta
\end{align*}
$$

Each coefficient comes from its own projection, so nothing is left over for the rest: $A_{\ell}=0$ for $\ell\neq0,2$.

Sum the modes:

$$
\begin{align*}
\varphi_{\text{in}}(r,\theta)&=\frac{V_0}{3}\\
&\quad+\frac{2V_0}{3}\left(\frac{r}{R}\right)^{2}P_2(\cos\theta)\\
\varphi_{\text{out}}(r,\theta)&=\frac{V_0}{3}\,\frac{R}{r}\\
&\quad+\frac{2V_0}{3}\left(\frac{R}{r}\right)^{3}P_2(\cos\theta)
\end{align*}
$$

![Cross-section of φ for a sphere held at V₀cos²θ, with the interior and exterior solutions meeting on the sphere r = R|700](/images/spherical-harmonics/laplace-cutaway.svg)

Interpretation: each mode carries its piece of $V$ off the sphere by its own radial law, and $\varphi$ is just their sum. $\ell=0$: flat inside, $\frac{R}{r}$ outside. $\ell=2$: grows from $0$ as $r^2$ inside, dies as $r^{-3}$ outside. At the center every $\ell\geq1$ carries $r^{\ell}\to0$, so $\varphi(0)=\frac{V_0}{3}$: the average of $V$ over the sphere. Far away, $\left(\frac{R}{r}\right)^{3}$ dies first, so only $\varphi_{\text{out}}\approx\frac{V_0R}{3r}$ survives: from far away, the sphere looks like a [point charge](https://en.wikipedia.org/wiki/Multipole_expansion).

This is [the Goal from the top](/blog/spherical-harmonics-1-building-the-basis/#goal): decompose $V$ into $Y_{\ell m}$'s, and the decomposition solves Laplace mode by mode.

## Intuition

Previously, we had $\left< f \right>_{\varepsilon}-f\approx\frac{\varepsilon^2}{4}\mel{\hat{n}}{\hat{\Lambda}}{f}$. *What does that say about a single $Y_{\ell m}$?*

$$
\left< Y_{\ell m} \right>_{\varepsilon} - Y_{\ell m} \approx -\frac{\varepsilon^2}{4}\ell(\ell+1)Y_{\ell m}
$$

$\ell$ labels the eigenvalue of $\hat{\Lambda}$: *how wiggly* the pattern is. Bigger $\ell$ means every point differs more from its neighbors' average.

$m$ labels the eigenvalue of $\hat{L}_z=-i\partial_{\psi}$: how the pattern responds to spinning about $z$, i.e. how much of that wiggliness wraps around the $z$-axis. $m$ = number of full wavelengths around any circle of latitude.

![Gallery of real spherical harmonics for ℓ = 0 to 4, red positive and blue negative, with their nodal lines|720](/images/spherical-harmonics/harmonic-gallery.svg)

Nodal lines: the [real version](https://en.wikipedia.org/wiki/Spherical_harmonics#Real_form) combines $e^{\pm im\psi}$ into $\cos(m\psi)$ and $\sin(m\psi)$. Previously, we had

$$
\begin{align*}
P_{\ell}^{|m|}(\cos\theta)&=(-1)^{|m|}\sin^{|m|}\theta\sum_{k=0}^{\lfloor (\ell-|m|)/2 \rfloor }(-1)^k\\
&\quad\times\frac{(2\ell-2k)!}{2^\ell k! (\ell-k)! (\ell-2k-|m|)!}\\
&\quad\times\cos^{(\ell-2k-|m|)}\theta
\end{align*}
$$

The sum is a degree-$(\ell-|m|)$ polynomial in $\cos\theta$ with $\ell-|m|$ zeros, all in $\theta\in(0,\pi)$ ([standard fact for these orthogonal polynomials](https://en.wikipedia.org/wiki/Orthogonal_polynomials#Zeros)): $\ell-|m|$ latitude circles. $\sin^{|m|}\theta$ only vanishes at the poles, so no new lines. $\cos(m\psi)$ vanishes at $2|m|$ values of $\psi$, and each pair ($\psi$ and $\psi+\pi$) is one great circle through both poles: $|m|$ meridian great circles. Total: $\ell$ nodal lines.

![One harmonic with its ℓ − |m| latitude nodal circles and |m| meridian great circles|380](/images/spherical-harmonics/nodal-lines.svg)

Extremes. $m=0$: all latitude lines, no $\psi$ dependence, symmetric about $z$ (the plain $P_{\ell}(\cos\theta)$). $|m|=\ell$: all meridian lines; the sum is a constant, so $P_{\ell}^{\ell}(\cos\theta)\propto\sin^{\ell}\theta$ and the pattern hugs the equator.

Why $|m|\leq\ell$, intuitively: $m$ counts meridians, which are a *subset* of the $\ell$ nodal lines. There can't be more meridians than total lines. Algebraically: $P_{\ell}(\cos\theta)$ is a degree-$\ell$ polynomial in $\cos\theta$, so differentiating it $|m|>\ell$ times with respect to $\cos\theta$ leaves nothing.

## References

1. R. L. Herman, *An Introduction to Mathematical Physics via Oscillations*, Chapter 9, "Oscillations in Higher Dimensions," University of North Carolina Wilmington (2012). [PDF](https://people.uncw.edu/hermanr/phy311/MathPhysBook/3D.pdf), licensed [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/us/).
2. D. J. Griffiths, *Introduction to Electrodynamics*, 4th ed., Cambridge University Press (2017), Chapter 3.
3. J. D. Jackson, *Classical Electrodynamics*, 3rd ed., Wiley (1999), Chapter 3.
4. F. W. J. Olver *et al.*, eds., *NIST Digital Library of Mathematical Functions*, [§14.17, Integrals](https://dlmf.nist.gov/14.17) and [§14.30, Spherical and Spheroidal Harmonics](https://dlmf.nist.gov/14.30).
5. [Kelvin transform](https://en.wikipedia.org/wiki/Kelvin_transform), *Wikipedia*.

## `<EOF>`

Next time, we will see what happens when the sum has to stop, and then take the same moves to drums, laser beams, hydrogen, and point charges.
