---
title: 0-22- How Is Profit and Loss Calculated?
description: Learn how profit and loss (P/L) is calculated in trading, covering long and short positions, pip value, and a step-by-step example.
date: 2026-08-02T11:21:21.744Z
draft: false
slug: 0-22-profit-loss-calculation
categories:
    - Basic
tags:
    - profit and loss
    - P/L calculation
    - pip value
    - position sizing
    - trading basics
keywords:
    - profit and loss
author: Mohammad Mahdi Masoumian
homepage.showRecent: true
fmContentType: tutorials
---

### Why Profit and Loss Calculation Matters

Calculating **profit and loss (P/L)** correctly is one of the most basic skills every trader needs, whether trading spot markets, futures, or leveraged instruments. Without a clear understanding of how P/L is calculated, a trader cannot properly size positions, set stop-losses, or judge whether a strategy is actually profitable.

At its core, profit and loss is simply the difference between the price you entered a position at and the price you exited it at, multiplied by the size of your position.

---

### The Basic P/L Formula

For a **long position**:

`P/L = (Exit Price − Entry Price) × Position Size`

For a **short position**, the formula flips, since profit comes from a falling price:

`P/L = (Entry Price − Exit Price) × Position Size`

In both cases, position size represents how much of the asset you are trading — for example, the number of shares, lots, or units of the underlying instrument.

---

### Understanding Pip and Point Value

In many markets, especially forex, price movement is measured in **pips** rather than raw price units. A pip is typically the smallest standard price increment for a given instrument.

To calculate P/L using pips:

`P/L = Number of Pips Moved × Pip Value × Position Size`

Pip value itself depends on the instrument, the position size, and sometimes the account's base currency. Most trading platforms display this value automatically, but understanding where it comes from helps a trader sanity-check the numbers before entering a trade.

---

### The Effect of Leverage on P/L

As covered in earlier lessons, leverage doesn't change the underlying formula for profit and loss — it changes the **effective position size** relative to the trader's own capital.

A leveraged position of $50,000 controlled with $500 of margin still calculates P/L based on the full $50,000, not the $500. This is exactly why leverage magnifies both gains and losses: the P/L calculation applies to the full position size, while the trader's actual capital at risk is much smaller.

---

### A Step-by-Step Example

Suppose a trader opens a long position on gold at $2,000 per ounce, with a position size equivalent to 10 ounces.

1. Entry Price = $2,000
2. Exit Price = $2,020
3. Position Size = 10 ounces

`P/L = (2,020 − 2,000) × 10 = $200 profit`

If the trade had instead been a short position at the same prices:

`P/L = (2,000 − 2,020) × 10 = −$200 loss`

This simple example shows why direction matters just as much as price movement itself — the same price move produces a profit in one direction and a loss in the other.

---

### Gross P/L vs. Net P/L

The formulas above calculate **gross P/L** — the raw result of the price movement alone. In practice, a trader's actual return is the **net P/L**, which subtracts trading costs such as spread, commission, and any overnight financing fees (including funding rates on perpetual futures, covered earlier).

`Net P/L = Gross P/L − Trading Costs`

Ignoring this distinction is a common mistake among beginner traders — a strategy that looks profitable based on gross P/L alone may actually lose money once realistic trading costs are included.

---

### Conclusion

Profit and loss calculation is built on a simple formula — the difference between entry and exit price, multiplied by position size — but its real-world application requires understanding pip value, the effect of leverage on position size, and the difference between gross and net P/L. Mastering this calculation is a prerequisite for any serious position sizing or risk management decision.

### One-Sentence

Profit and loss is calculated as the price difference between entry and exit multiplied by position size, and understanding gross versus net P/L is essential once trading costs are factored in.