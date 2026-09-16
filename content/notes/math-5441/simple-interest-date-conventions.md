---
author: "Anish Goyal"
title: "Simple Interest Date Conventions"
description: "Only include one of the endpoint dates"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-10-01T13:46:15
modified: 2025-10-01T14:20:31
readingtime: "1"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 5
weight: 50
slug: "simple-interest-date-conventions"
links: []
sources: []
generated: true
---

# Date Conventions {#date-conventions}

## General Notes {#general-notes}
- Only include one of the endpoint dates
- Time must always be in years

## Exact Simple Interest {#exact-simple-interest}
- "actual/actual" method
- Include leap year days
- Include actual month days

## Ordinary Simple Interest {#ordinary-simple-interest}
- "30/360" method
- All months have 30 days and all years have 360 days
- Rules for changing dates
	- If any endpoint is 31, change it to 30
	- If any endpoint is 02/28 or 02/29, change it to 30
- The number of days $N$ is:

$$N = 360(Y_{2}-Y_{1})+30(M_{2}-M_{1})+(D_{2}-D_{1})$$

## Banker's Interest {#banker-s-interest}
- "actual/360" method
- Use the actual number of days but all years have 360 days
