---
title: 0-10- What is a Perpetual Futures Contract?
date: 2026-08-02T07:33:44.369Z
draft: false
description: Learn what perpetual futures contracts are, how funding rates keep them aligned with the spot market, and how they differ from standard futures.
tags:
  - perpetual futures
  - derivatives
  - funding rate
  - cryptocurrency trading
  - financial markets
categories:
  - Intermediate
keywords:
  - Perpetual Futures
  - Funding Rate
homepage:
  showRecent: true
author: Mohammad Mahdi Masoumian
slug: 0-10-perpetual-futures
---

### What Is a Perpetual Futures Contract?

A **perpetual futures contract** (often just called a "perpetual" or "perp") is a derivative contract that lets traders speculate on the price of an underlying asset without ever having to take delivery of it — and, unlike standard futures, without an expiration date.

Perpetuals are most widely used in cryptocurrency markets, where they have become one of the dominant instruments for both spot-price speculation and hedging.

---

### Perpetual vs. Standard Futures

A standard futures contract has a fixed expiration date. When that date arrives, the contract is settled, either through physical delivery of the asset or a cash settlement.

A perpetual futures contract removes this expiration entirely. Traders can hold a position open indefinitely, as long as they maintain the required margin. This design makes perpetuals behave more like a continuously rolling position than a dated contract.

---

### The Problem Perpetuals Had to Solve

Without an expiration date, a natural question arises: what keeps the price of a perpetual contract close to the price of the underlying asset in the spot market?

In a standard futures contract, the price converges to the spot price as expiration approaches, because the contract must eventually settle. A perpetual contract has no such settlement event to force this convergence.

To solve this, perpetual contracts use a mechanism called the **funding rate**.

---

### What Is the Funding Rate?

The funding rate is a periodic payment exchanged directly between traders holding long positions and traders holding short positions. It is not a fee paid to the exchange.

* When the perpetual contract's price trades **above** the spot price, long position holders pay short position holders.
* When the perpetual contract's price trades **below** the spot price, short position holders pay long position holders.

This payment is typically exchanged every 8 hours, though the exact interval depends on the exchange.

---

### How the Funding Rate Keeps Prices Aligned

The funding rate creates a financial incentive that pushes the contract's price back toward the spot price.

If the perpetual price rises well above the spot price, longs must pay a funding fee to shorts. This makes holding long positions more costly, which discourages new long positions and encourages some traders to close existing ones or open short positions instead — pushing the price back down toward spot.

The same mechanism works in reverse when the perpetual price falls below the spot price.

---

### Key Characteristics of Perpetual Futures

* No expiration date
* Positions can be held indefinitely, subject to margin requirements
* Price is kept close to the spot price through the funding rate mechanism
* Usually offer high leverage
* Commonly used with both long and short positions
* Widely available on cryptocurrency exchanges; less common in traditional regulated markets

---

### Practical Considerations

Funding payments can meaningfully affect the profitability of a position, especially when it is held open for an extended period. A position that is directionally correct can still lose money over time if funding payments accumulate against it.

For this reason, traders using perpetual contracts for longer-term positions need to account for funding costs, not just the price movement of the underlying asset.

---

### Conclusion

A perpetual futures contract is a derivative instrument that allows traders to hold a position with no expiration date, while a funding rate mechanism keeps its price aligned with the underlying spot market. Understanding how the funding rate works — and who pays whom, and when — is essential before using perpetual contracts in any trading strategy.

### One-Sentence

A perpetual futures contract has no expiration date and relies on a periodic funding rate exchanged between long and short traders to keep its price aligned with the spot market.