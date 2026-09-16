---
author: "Anish Goyal"
title: "Introduction to Proofs"
description: "Informal (shorter) proofs are generally used:"
tags:
  - "notes"
  - "mathematics"
  - "math-2130"
date: 2025-02-24T14:35:10
modified: 2025-10-22T00:48:34
readingtime: "3"
course: "MATH 2130"
course_slug: "math-2130"
subject: "mathematics"
kind: "lecture"
ordinal: 6
weight: 60
slug: "introduction-to-proofs"
links:
  - "/notes/math-2130/axiom/"
  - "/notes/math-2130/conjecture/"
  - "/notes/math-2130/corollary/"
  - "/notes/math-2130/lemma/"
  - "/notes/math-2130/proof/"
  - "/notes/math-2130/propositions/"
  - "/notes/math-2130/theorem/"
sources: []
generated: true
---

## Proof {#proof}

- <div class="transclusion" data-source="04. Notes/Undergraduate Courses/MATH 2130/proof.md">
  <a class="transclusion-source" href="/notes/math-2130/proof/" title="Open proof"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  a valid argument that establishes the truth of a statement

  </div>

- **Informal (shorter) proofs** are generally used:
	- More than one rule of inference often used in a step
	- Steps may be skipped
	- Rules of inference may not be explicitly stated
	- Easier to understand but also easier to introduce errors

## Theorem {#theorem}

- <div class="transclusion" data-source="04. Notes/Undergraduate Courses/MATH 2130/theorem.md">
  <a class="transclusion-source" href="/notes/math-2130/theorem/" title="Open theorem"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  a statement that can be shown to be true using:
  - definitions
  - other theorems
  - <a class="internal-link" href="/notes/math-2130/axiom/">axioms</a>
  - rules of inference

  </div>

- <div class="transclusion" data-source="04. Notes/Undergraduate Courses/MATH 2130/lemma.md">
  <a class="transclusion-source" href="/notes/math-2130/lemma/" title="Open lemma"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  a "helping" <a class="internal-link" href="/notes/math-2130/theorem/">theorem</a> needed to prove the "main" theorem

  </div>

- <div class="transclusion" data-source="04. Notes/Undergraduate Courses/MATH 2130/corollary.md">
  <a class="transclusion-source" href="/notes/math-2130/corollary/" title="Open corollary"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  a result that follows directly from a theorem

  </div>

- <div class="transclusion" data-source="04. Notes/Undergraduate Courses/MATH 2130/propositions.md">
  <a class="transclusion-source" href="/notes/math-2130/propositions/" title="Open propositions"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  less important theorems

  </div>

- <div class="transclusion" data-source="04. Notes/Undergraduate Courses/MATH 2130/conjecture.md">
  <a class="transclusion-source" href="/notes/math-2130/conjecture/" title="Open conjecture"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a>

  - A statement being proposed to be true
  	- Once a proof is found, the conjecture becomes a theorem
  	- It may turn out to be false, though

  </div>

### Forms of theorems {#forms-of-theorems}
- Many theorems assert that a property holds for all elements in a domain
	- The universal quantifier is often omitted
- Many theorems have the form: $(*) \ \ \ \forall x (P(x) \implies Q(x))$
	- If for $c$, an arbitrary element in the domain, $P(c) \implies Q(c)$, then $(*)$ follows by universal generalization
	- So, we need to prove $p \implies q$... how do we do that?

### Proving conditional statements: $p \implies q$ {#proving-conditional-statements-p-q}
- No work needed if:
	- $q$ is true (trivial proof)
	- $p$ is false (vacuous proof)
- Otherwise, a proof needs to be constructed. Two options:
	- **Direct proof**: Assume $p$ is true; show that $q$ must be true as a result
	- **Proof by contraposition (indirect proof)**: Assume $q$ is false; show that $p$ is false as well
		- This is a direct proof of the contraposition. This is valid because the contrapositive is logically equivalent to the original statement

## References {#references}
- 
