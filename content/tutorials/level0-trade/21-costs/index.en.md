---
title: 0-21- What Are Trading Costs?
date: 2026-08-02T10:59:52.053Z
draft: false
description: Understand spread, commission, and slippage, why they matter, and how they affect algorithmic backtesting.
tags:
    - spread
    - commission
    - slippage
    - trading costs
    - backtesting
categories:
    - Intermediate
keywords:
    - commission
    - slippage
    - spread
    - trading costs
homepage:
    showRecent: true
author: Mohammad Mahdi Masoumian
slug: 0-21-what-are-trading-costs-spread-commission-slippage
---

Trading costs are far more important than most traders assume, and they play an especially critical role in algorithmic trading. Ignoring them during **backtesting** — the process of simulating how a strategy would have performed on historical data — can completely distort the results, turning an apparently profitable algorithm into a losing one once real costs are applied.

---

### Spread

The **spread** is the difference between the buy price (ask) and the sell price (bid) of an asset. It's most commonly seen in forex and commodity brokers — venues where you're trading against the broker itself rather than another trader. In these markets, the buy price is always higher than the sell price by the amount of the spread.

The spread isn't fixed — it naturally fluctuates. It can widen significantly during low-activity periods, such as near market close or around midnight UTC, and can shrink or even drop to zero at other times. This behavior is entirely a function of each broker's internal policy and varies from one broker to another. The one rule that always holds is simple: **sell price + spread = buy price.**

This cost affects every trade exactly once. On a long (buy) position, the effect shows up the moment you open the trade — you're immediately down a small amount, exactly equal to the spread, because the sell price is lower than what you paid to buy. On a short position, the spread instead applies when you close the trade, since closing a short means buying the asset back to return it to the broker — and that closing transaction is itself a buy, which is where the spread gets applied. Every one of these details needs to be modeled in a strategy's backtest, or the resulting performance numbers are little more than an illusion.

It's also worth noting that spreads typically don't exist in crypto exchanges or stock exchanges, because your counterparty there is another trader, not the platform itself — the price is set by matching two opposing orders from real participants. In these markets, a different cost takes the spread's place: **commission**.

---

### Commission

Unlike spread, commission exists in essentially every market — spot, futures, options, even binary options. Its exact amount is set by each broker's, exchange's, or brokerage's internal policy, varies from platform to platform, and can sometimes be zero. Commission is typically calculated as a small percentage of the total trade value.

In spot markets (stocks, crypto), commission is charged **twice** — once on the buy transaction and once on the sell transaction, because each is treated as an independent, formal transaction. In forex and commodity brokers, by contrast, commission is usually charged **only once**, when the trade is opened, with no additional charge when it's closed — though this, too, can vary between brokers.

Like spread, commission is one of the critical costs that must be included in any algorithmic backtest to produce a trustworthy picture of a strategy's real performance.

---

### Slippage

**Slippage** refers to the difference between the price you intended to trade at and the price your order actually executes at, caused by price movement happening in the brief moment your order is being filled. For example, if you're trying to buy 50 shares, the price at which the first share fills isn't necessarily the same as the price at which the 50th share fills.

Slippage tends to show up most in low-liquidity conditions, and is particularly common in stock and crypto markets; retail traders in forex or commodity markets typically experience it far less. Slippage is also considerably harder to model in code than spread or commission, because those two have well-defined, predictable values, while slippage depends entirely on live market conditions at the exact moment of execution — it can't be reliably predetermined in a backtest.

Because of this, slippage remains one of the reasons a backtest's results can never be trusted with full, 100% confidence. Still, factoring in spread and commission carefully can typically get a backtest's reliability well above 90%. One common (though not proven or universal) practice is to deliberately overestimate the commission rate slightly during testing, as a buffer that helps absorb some of the uncertainty slippage introduces — though this is a rough heuristic, not an established rule.

---

### Why This Matters So Much for Algorithmic Trading

The more precisely trading costs are incorporated into a simulation, the more trustworthy that simulation becomes — and without them, very little confidence can be placed in a strategy's apparent performance. This is comparable to how physics simplifies away air resistance and friction in introductory problems: leaving them out changes a great deal about the real-world outcome. The same is true for trading costs in algorithmic strategy testing — they're small individually, but their cumulative effect can be the difference between a strategy that looks profitable on paper and one that actually is.

---

### Summary

Spread, commission, and slippage are the three core trading costs every trader — and especially every algorithmic strategy — needs to account for. Spread applies mainly in broker-based markets like forex and commodities, commission applies almost universally and can be charged once or twice depending on the market, and slippage is the least predictable of the three, tied directly to live market conditions. Leaving any of these out of a backtest produces performance numbers that can't be trusted.

### One-Sentence

Trading costs — spread, commission, and slippage — are individually small but collectively critical, and any algorithmic strategy's backtest is only as trustworthy as how carefully these costs are modeled into it.