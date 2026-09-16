---
author: "Anish Goyal"
title: "Varying Payment Amortizations"
description: "An interest-bearing security that pays a \"face value\" at a future maturity date"
tags:
  - "notes"
  - "mathematics"
  - "math-5441"
date: 2025-12-06T14:33:33
modified: 2025-12-09T12:04:39
readingtime: "1"
course: "MATH 5441"
course_slug: "math-5441"
subject: "mathematics"
kind: "lecture"
ordinal: 41
weight: 410
slug: "varying-payment-amortizations"
links: []
sources: []
generated: true
---

# Bonds {#bonds}

## Bonds {#bonds-1}
- An interest-bearing security that pays a "face value" at a future maturity date
	- Redemption value: the date you turn in the bond; usually the same as the maturity date
	- If the bond has a redemption date < maturity date, the bond is considered callable
		- You can turn in your money for it before it matures
		- The trade-off is that you may not get the entire face value
- Two types:
	- Accumulation bond
		- The interest is included in the redemption value
		- Like compound interest in a fund
	- Coupon bonds
		- Payments are received at various dates before redemption
		- Like an annuity but with a bank deposit
		- The minimal rate of return occurs when you cash in the bond earliest

### Coupon Bond {#coupon-bond}
- $P$: Price of the bond
	- Present value of all the coupons and redemption value
- $F$: Face value of the bond
- $C$: Redemption value of the bond
- $r$: coupon rate (percentage of the face value)
	- Coupon amount for each time period: $Fr$
- $i$: yield rate

### Premiums and Discount {#premiums-and-discount}
- $P > C$: premium
	- amortization of premium
		- Value is marked down to the "book value" after each payment
			- Book value is the PV of all future payments
- If $P < $C$: discount
	- accumulation of discount
		- The book value is "written up" at each coupon date
- 
