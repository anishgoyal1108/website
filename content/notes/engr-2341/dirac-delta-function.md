---
author: "Anish Goyal"
title: "Dirac delta function"
description: "A limiting case of a rectangular pulse function, {}(t), as the width 0."
tags:
  - "notes"
  - "electrical-engineering"
  - "engr-2341"
date: 2025-01-14T08:47:51
modified: 2025-01-14T08:53:40
readingtime: "1"
course: "ENGR 2341"
course_slug: "engr-2341"
subject: "electrical-engineering"
kind: "concept"
weight: 9004
slug: "dirac-delta-function"
links: []
sources: []
generated: true
---

## Dirac Delta Function {#dirac-delta-function}
A limiting case of a rectangular pulse function, $\delta_{\Delta}(t)$, as the width $\Delta \rightarrow 0$.

### Rectangular Pulse Function {#rectangular-pulse-function}
- For $-\Delta \le t \le \Delta$, the rectangular pulse has a value of $\frac{1}{2\Delta}$
- Outside this range, the function is 0

### Normalization Property {#normalization-property}
- Regardless of the choice of $\Delta$, the area of $\delta_{\Delta} = 1$

$$\int_{-\Delta}^{\Delta}\frac{1}{2\Delta} \ \mathrm{d}t = 1$$

- This ensures that the height of the pulse increases proportionally as the width becomes narrower

### Dirac Delta as a Limit {#dirac-delta-as-a-limit}
- $\delta(t)$ is defined as the limit of this rectangular pulse as $\Delta \rightarrow 0$
