---
author: "Anish Goyal"
title: "Rules of Inference and Valid Arguments"
description: "Definition of valid argument"
tags:
  - "notes"
  - "mathematics"
  - "math-2130"
date: 2025-02-17T14:31:26
modified: 2025-02-26T15:55:01
readingtime: "1"
course: "MATH 2130"
course_slug: "math-2130"
subject: "mathematics"
kind: "lecture"
ordinal: 5
weight: 50
slug: "rules-of-inference-and-valid-arguments"
links:
  - "/notes/math-2130/rules-of-inference/"
  - "/notes/math-2130/valid-argument/"
sources:
  - "Course slides §6.1: Rules of Inference and Valid Arguments"
generated: true
---

## Valid Arguments {#valid-arguments}
- Definition of <a class="internal-link" href="/notes/math-2130/valid-argument/">valid argument</a>
	- Can follow from previous statements due to <a class="internal-link" href="/notes/math-2130/rules-of-inference/">rules of inference</a>
 
## Rules of Inference {#rules-of-inference}

### Modus Ponens {#modus-ponens}

$$
\begin{align*}
P \rightarrow  \ &Q, \\
&P \\
\vdash &Q 
\end{align*}
$$

### Modus Tollens {#modus-tollens}

$$
\begin{align*}
P &\rightarrow Q, \\
&\neg Q \\
\vdash &\neg P 
\end{align*}
$$

### Hypothetical Syllogism {#hypothetical-syllogism}

$$
\begin{align*}
P &\rightarrow Q, \\
Q &\rightarrow R \\
\vdash P &\rightarrow R
\end{align*}
$$

### Disjunctive Syllogism {#disjunctive-syllogism}

$$
\begin{align*}
P \ \vee \ &Q, \\
\neg &P \\
\vdash &Q 
\end{align*}
$$

### Addition {#addition}

$$
\begin{aligned}
P \\
\vdash P \vee Q
\end{aligned}
$$

### Simplification {#simplification}

$$
\begin{aligned}
P \wedge Q \\
\vdash P 
\end{aligned}
$$

### Conjunction {#conjunction}

$$
\begin{align*}
&P, \\
&Q \\
\vdash \ P \wedge \ &Q
\end{align*}
$$

### Resolution {#resolution}

$$
\begin{align*}
P &\vee Q, \\
\neg P &\vee R \\
\vdash Q &\vee R
\end{align*}
$$

### Replacement {#replacement}
- Logically equivalent statements can replace each other
	- e.g. contrapositive

## References {#references}
<span class="cite cite-ref">Course slides §6.1: Rules of Inference and Valid Arguments</span>
