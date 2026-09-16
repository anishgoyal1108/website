---
author: "Anish Goyal"
title: "Basic Counting Principles"
description: "Counting helps us determine the number of outcomes in a sample space"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3421"
date: 2026-02-09T09:23:32
modified: 2026-02-09T09:54:03
readingtime: "10"
course: "EENG 3421"
course_slug: "eeng-3421"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 5
weight: 50
slug: "basic-counting-principles"
links: []
sources:
  - "Course lecture slides 7"
  - "Course lecture slides 8"
  - "Course lecture slides 9–10"
generated: true
---

## Counting Methods {#counting-methods}
- Counting helps us determine the number of outcomes in a sample space

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="05.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 05.1</span> <span class="theorem-callout-subtitle">(Multiplication Principle)</span>.</div></div>
<div class="callout-content">

For any experiment containing $N$ sub-experiments with the $i$th sub-experiment having $k_i$ outcomes, the total number of outcomes, $k$, for the experiment is:

$$k = \prod_{i=1}^N k_{i}$$

</div>
</div>

## Permutations {#permutations}
- A *permutation* is an ordered sequence of distinguishable objects
	- Each such permutation is called a $k$-permutation, where you fix $k$ to be the number of objects in each permutation
	- $(n)_k$: the number of possible $k$-permutations for $n$ distinguishable objects

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="05.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 05.2</span> <span class="theorem-callout-subtitle">(Number of $k$-Permutations)</span>.</div></div>
<div class="callout-content">

$$(n)_{k} = \frac{n!}{(n-k)!}$$

</div>
</div>

### Application: Sampling Without Replacement (With Ordering) {#application-sampling-without-replacement-with-ordering}
- Permutations are really useful when evaluating the number of ways you can sample a group of objects without replacement
	- This is because counting the number of arrangements is *always* without replacement, since no two objects can exist in the same place at the same time, and you’re assuming all the objects are distinguishable to begin with

## Combinations {#combinations}
- A *combination* is an unordered set of objects taken from the sample space
	- Similar to permutations, the $k$-combination would be sets of length $k$
	- The unordered property is important! It means that all sets containing the same elements are identical, no matter what order they’re in
	- $n \choose k$: denotes the number of $k$-combinations for a collection of $n$ objects; also called “$n$ choose $k$”
- Different than permutation because the order doesn’t matter!
	- Also has a fewer number (for any fixed $n$ and $k$) than permutation, since you’re overcounting the number of sets that are the same in permutation (specifically by a factor of $k!$)

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="05.3">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 05.3</span> <span class="theorem-callout-subtitle">(Number of $k$-Combinations)</span>.</div></div>
<div class="callout-content">

$$\binom{n}{k} = \frac{(n)_{k}}{k!} = \frac{n!}{k!(n-k)!}$$

</div>
</div>

### Application: Sampling Without Replacement (And Without Ordering) {#application-sampling-without-replacement-and-without-ordering}
- Similar to permutation, combination is *also* good for sampling without replacement, but with the caveat that the order doesn’t matter
	- So, you could observe some sequence of events or objects, but ultimately, as long as they were the *same* objects, they are considered the same under the combination POV

## Binomial Coefficients {#binomial-coefficients}
- Combinations are also very useful in mathematics; we will show this in more detail below
- “$n$ choose $k$” is also called a Binomial coefficient (and is only defined for $k, n \gt 0$), and is written as: $\binom{n}{k}$
	- Also has this property: $\binom{n}{k} = \binom{n}{n-k}$
	- This is basically indicative of the *symmetry* of the combination formula; if you fix the number of objects in the experiment and iterate over $k$, you’ll notice that the values of $\binom{n}{k}$ will start to “mirror” the first half (before $n/2$)

## Independent Trials {#independent-trials}
- Sampling with replacement means you select an object, replace it, then repeat
- Each repetition is the same subexperiment
- The repetitions are independent trials

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="05.4">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 05.4</span> <span class="theorem-callout-subtitle">(Independent Trials)</span>.</div></div>
<div class="callout-content">

A sequential experiment formed by repeating the same subexperiment with replacement
Each trial has the same sample space $S_{\text{sub}}$
Outcomes across trials do not change the available outcomes on later trials

</div>
</div>

- Notation
	- $x_i$ outcome of trial $i$
	- Observation sequence $x_1x_2\cdots x_n$
	- Sample space $S$ is the set of all length $n$ observation sequences

### Application {#application}
- Laptop has USB slots $A$ and $B$
- Each slot uses one device type from $\{m,c,p\}$
- With replacement across slots since the same device type may be used twice

- Outcomes written as ordered pairs
	- First entry for slot $A$
	- Second entry for slot $B$
- Sample space

$$
S=\{mm,mc,mp,cm,cc,cp,pm,pc,pp\}
$$

- $|S|=9$

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="05.5">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 05.5</span> <span class="theorem-callout-subtitle">(Ordered Sampling With Replacement)</span>.</div></div>
<div class="callout-content">

Given $m$ distinguishable objects, the number of ordered samples of size $n$ with replacement is

$$
m^n
$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>
Each position in the ordered sample has $m$ choices
Apply the multiplication principle across $n$ positions
<span class="math-booster-end-proof"></span>

</blockquote>

### Binary Sequences {#binary-sequences}
- For a binary alphabet $\{0,1\}$
- Number of length $n$ sequences

$$
2^n
$$

- Example
	- $2^{10}=1024$

### Alphabet Words {#alphabet-words}
- For letters $A$ through $Z$
- Number of length $n$ words

$$
26^n
$$

- Example
	- $26^4=456{,}976$

### Repeated Testing Example {#repeated-testing-example}
- Subexperiment sample space

$$
S_{\text{sub}}=\{0,1\}
$$

- Record $x_i=0$ for failure and $x_i=1$ for success
- Testing four microprocessors gives a length $4$ observation sequence
- Sample space size

$$
|S|=2^4=16
$$

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="05.6">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 05.6</span> <span class="theorem-callout-subtitle">(Sequential Experiment Count)</span>.</div></div>
<div class="callout-content">

For $n$ repetitions of a subexperiment with sample space $S_{\text{sub}}=\{s_0,\dots,s_{m-1}\}$
the sample space $S$ of the sequential experiment has

$$
m^n
$$

outcomes

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>
Each trial contributes one symbol from $m$ possibilities
Apply the multiplication principle across $n$ trials
<span class="math-booster-end-proof"></span>

</blockquote>

## Grouping Outcomes by Counts {#grouping-outcomes-by-counts}
- Often the order in the observation sequence is not the object of interest
- The counts of each symbol is the object of interest
- Group sequences by how many times each symbol appears

### Binary Case {#binary-case}
- Subexperiment sample space

$$
S_{\text{sub}}=\{0,1\}
$$

- Run $n$ trials
- Let $n_0$ be the number of zeros
- Let $n_1$ be the number of ones
- Constraint

$$
n_0+n_1=n
$$

- Example
	- Five trials
	- $n_0=2$
	- $n_1=3$
	- The sequences are the length $5$ strings with two zeros and three ones

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="05.7">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 05.7</span> <span class="theorem-callout-subtitle">(Binary Count of Sequences)</span>.</div></div>
<div class="callout-content">

The number of observation sequences for $n$ trials with $S_{\text{sub}}=\{0,1\}$
with $0$ appearing $n_0$ times and $1$ appearing $n_1=n-n_0$ times is

$$
\binom{n}{n_1}=\binom{n}{n_0}
$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>
Choose the $n_1$ trial indices where a $1$ appears
The remaining indices contain $0$
<span class="math-booster-end-proof"></span>

</blockquote>

## Multigroup Case {#multigroup-case}
- Subexperiment sample space

$$
S_{\text{sub}}=\{s_0,s_1,\dots,s_{m-1}\}
$$

- Run $n$ trials
- Let $n_i$ be the number of occurrences of symbol $s_i$
- Constraint

$$
n=n_0+n_1+\cdots+n_{m-1}
$$

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="05.8">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 05.8</span> <span class="theorem-callout-subtitle">(Multigroup Count of Sequences)</span>.</div></div>
<div class="callout-content">

For $n$ trials with sample space $S_{\text{sub}}=\{s_0,\dots,s_{m-1}\}$
the number of length $n$ observation sequences with $s_i$ appearing $n_i$ times is

$$
\frac{n!}{n_0!n_1!\cdots n_{m-1}!}
$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>
Start with $n!$ permutations of $n$ labeled positions
Symbols of the same type are indistinguishable in the final sequence
Divide by $n_i!$ for each subgroup of identical symbols
<span class="math-booster-end-proof"></span>

</blockquote>

## Multinomial Coefficient {#multinomial-coefficient}
- The multigroup counting formula appears repeatedly
- Use a single notation for it

<div class="callout theorem-callout theorem-callout-definition theorem-callout-en theorem-callout-mathwiki" data-callout="definition" data-theorem-index="05.9">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 448 512"><use href="#cicon-fa-book"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Definition 05.9</span> <span class="theorem-callout-subtitle">(Multinomial Coefficient)</span>.</div></div>
<div class="callout-content">

For integers $n\ge 0$ and integers $n_i\ge 0$ with $\sum_{i=0}^{m-1}n_i=n$

$$
\binom{n}{n_0,n_1,\dots,n_{m-1}}
=
\frac{n!}{n_0!n_1!\cdots n_{m-1}!}
$$

and it is $0$ otherwise

</div>
</div>

- Interpretation
	- Number of permutations of $n$ objects grouped into $m$ subgroups
	- Subgroup $i$ has size $n_i$
	- Objects inside a subgroup are treated as identical

- Same formula as multigroup sequence counting
	- Both count arrangements of $n$ slots filled with repeated types
	- The only input is the subgroup sizes $n_i$

### Example {#example}
- Ten students
- Grade set $S_{\text{sub}}=\{A,B,C,F\}$
- A grade list for the class is an observation sequence of length $10$
- Total number of grade lists

$$
4^{10}=1{,}048{,}576
$$

- Curved distribution
	- $n_A=2$
	- $n_B=3$
	- $n_C=3$
	- $n_F=2$
- Number of grade lists matching the curve

$$
\binom{10}{2,3,3,2}
=
\frac{10!}{2!\,3!\,3!\,2!}
$$

## Independent Trials With Probabilities {#independent-trials-with-probabilities}
- Counting gives the number of sequences
- Probability assigns weight to each sequence
- For independent trials, multiply trial probabilities along the sequence

### Binary Outcome Trials {#binary-outcome-trials}
- Success probability

$$
p
$$

- Failure probability

$$
1-p
$$

- For a fixed sequence with $n_1$ successes and $n_0$ failures

$$
p^{n_1}(1-p)^{n_0}
$$

- Example
	- Five trials
	- Two failures and three successes
	- Each such sequence has probability

$$
(1-p)^2p^3
$$

- Number of such sequences

$$
\binom{5}{3}
$$

- Add the probabilities of all such sequences

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="05.10">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 05.10</span> <span class="theorem-callout-subtitle">(Probability of $n_0$ Failures and $n_1$ Successes)</span>.</div></div>
<div class="callout-content">

In $n=n_0+n_1$ independent trials with success probability $p$

$$
P[E_{n_0,n_1}]
=
\binom{n}{n_1}(1-p)^{n_0}p^{n_1}
=
\binom{n}{n_0}(1-p)^{n_0}p^{n_1}
$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>
Each sequence with $n_1$ successes has probability $p^{n_1}(1-p)^{n_0}$
The number of such sequences is $\binom{n}{n_1}$
Multiply
<span class="math-booster-end-proof"></span>

</blockquote>

### Binomial Coefficients as Counts {#binomial-coefficients-as-counts}
- $\binom{n}{n_1}$ counts the number of sequences with $n_1$ successes
- The probability formula is a count times a per-sequence probability
- When $p\ne \tfrac12$, outcomes with the same count still share the same probability
	- independence gives the same product for each arrangement of the same counts

### Information Bit Repetition Example {#information-bit-repetition-example}
- Transmit one bit five times
	- $0$ sent as $00000$
	- $1$ sent as $11111$
- Receiver decides correct bit if at least three of the five received symbols match
- Let $q$ be symbol error probability
- Let $p=1-q$ be symbol correct probability
- Error event occurs when number of correct symbols is less than $3$
	- $E_{5,0}$
	- $E_{4,1}$
	- $E_{3,2}$
- Error probability

$$
P[E]
=
P[E_{5,0}]+P[E_{4,1}]+P[E_{3,2}]
=
\binom{5}{5}q^5+\binom{5}{4}q^4p+\binom{5}{3}q^3p^2
$$

## Multigroup Independent Trials {#multigroup-independent-trials}
- Subexperiment sample space

$$
S_{\text{sub}}=\{s_0,\dots,s_{m-1}\}
$$

- Trial probabilities

$$
P[s_i]=p_i
$$

- In $n$ independent trials
	- count vector $(n_0,\dots,n_{m-1})$
	- with $\sum n_i=n$

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="05.11">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 05.11</span> <span class="theorem-callout-subtitle">(Multinomial Probability)</span>.</div></div>
<div class="callout-content">

For $n$ independent trials with $P[s_i]=p_i$
the probability of $n_i$ occurrences of $s_i$ for $i=0,\dots,m-1$ is

$$
P[E_{n_0,\dots,n_{m-1}}]
=
\binom{n}{n_0,\dots,n_{m-1}}
\prod_{i=0}^{m-1} p_i^{n_i}
$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>
Each fixed sequence with counts $(n_0,\dots,n_{m-1})$ has probability $\prod p_i^{n_i}$
The number of such sequences is the multinomial coefficient
Multiply
<span class="math-booster-end-proof"></span>

</blockquote>

### Equal Probability Grade Example {#equal-probability-grade-example}
- Grades $A,B,C,F$ equally likely

$$
p_A=p_B=p_C=p_F=\tfrac14
$$

- Event $E_{2,3,3,2}$

$$
P[E_{2,3,3,2}]
=
\binom{10}{2,3,3,2}
\left(\tfrac14\right)^{10}
$$

## Binomial Theorem {#binomial-theorem}
- Binomial coefficients appear in counting
- The same coefficients appear in algebraic expansions

<div class="callout theorem-callout theorem-callout-theorem theorem-callout-en theorem-callout-mathwiki" data-callout="theorem" data-theorem-index="05.12">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 512 512"><use href="#cicon-fa-magic"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Theorem 05.12</span> <span class="theorem-callout-subtitle">(Binomial Theorem)</span>.</div></div>
<div class="callout-content">

For integer $n\ge 0$

$$
(x+y)^n=\sum_{k=0}^n \binom{n}{k}x^{n-k}y^k
$$

</div>
</div>

<blockquote class="proof">

<span class="math-booster-begin-proof math-booster-begin-proof-en">Proof.</span>
Expand $(x+y)^n$ as a product of $n$ factors
A term $x^{n-k}y^k$ arises from choosing $k$ factors to contribute $y$
The number of such choices is $\binom{n}{k}$
<span class="math-booster-end-proof"></span>

</blockquote>

### Link to Independent Trials {#link-to-independent-trials}
- Substitute $x=1-p$ and $y=p$

$$
((1-p)+p)^n=1
$$

- Expansion

$$
1=\sum_{k=0}^n \binom{n}{k}(1-p)^{n-k}p^k
$$

- Terms match probabilities of $k$ successes in $n$ trials
- Sum over $k$ gives total probability $1$

### Binary Outcomes With $n$ Successes and $k$ Failures {#binary-outcomes-with-n-successes-and-k-failures}
- Total trials

$$
n+k
$$

- Event
	- successes $n$
	- failures $k$
- Probability

$$
P[E_{k,n}]
=
\binom{n+k}{n}(1-p)^k p^n
=
\binom{n+k}{k}(1-p)^k p^n
$$

## References {#references}
- <span class="cite cite-ref">Course lecture slides 7</span>
- <span class="cite cite-ref">Course lecture slides 8</span>
- <span class="cite cite-ref">Course lecture slides 9–10</span>
