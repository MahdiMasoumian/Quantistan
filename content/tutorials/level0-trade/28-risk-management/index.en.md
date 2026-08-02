---
title: 0-28- Risk and Money Management Basics
description: Learn what stop-loss and take-profit really mean, why risk should stay fixed at 1-2%, why averaging into losses is forbidden, and how trailing stops work.
date: 2026-08-02T13:25:33.348Z
draft: false
slug: 0-28-risk-and-money-management-basics
categories:
    - Intermediate
tags:
    - risk management
    - money management
    - stop loss
    - take profit
    - trailing stop
keywords:
    - risk management
    - stop-loss
author: Mohammad Mahdi Masoumian
homepage.showRecent: true
fmContentType: tutorials
---

### Why Stop-Loss and Take-Profit Exist

**Risk management** and **money management** define how much capital is put at risk on each trade and how a position is exited, both in profit and in loss. Two tools sit at the center of this: the **stop-loss** and the **take-profit**. Both must be defined with the same mathematical clarity discussed in the lesson on trading strategy — no vague judgment calls, only precise, pre-defined rules.

---

### What a Stop-Loss Actually Means

The most important philosophical point here: a **stop-loss** is not "the point where some candle left a wick" or "where some sloping line used to pass." A stop-loss marks the exact price at which the original trade analysis is **proven wrong** and has lost its validity. It may happen to coincide with a candle's shadow or a trendline, but its meaning is not that — its meaning is: "if price reaches here, my reason for entering this trade is no longer true." Confusing these two ideas is one of the most common mistakes new traders make.

---

### How Much to Risk: Fixed, Not Recalculated

A reasonable stop-loss risk is generally **1–2% of the initial capital** per trade. Among professional traders, the standard is usually kept **under 2%**; with smaller capital or higher risk tolerance, it can go up to a maximum of **5%** — but never beyond that. Past this point, trading starts resembling gambling rather than a managed activity.

Critically, this percentage must be **calculated once, from the original starting capital, and kept fixed** for the entire trading period — not recalculated after every trade based on the remaining balance. Continuously updating the risk amount based on current equity is a serious statistical mistake, and the resulting illusion of exponential capital growth is a naive one. This will be demonstrated rigorously with Monte Carlo simulation in a future article, but the rule itself must be stated clearly now: keep risk size fixed, calculated from starting capital.

---

### Take-Profit: Staged Exits

A common — though not universally mandatory — practice for managing profitable trades is using **multiple take-profit levels** instead of a single one, typically two or three. Rather than closing the entire position at once and later regretting not letting it run further, a trader can exit in stages — for example, closing one-third of the position at each level — while leaving the final portion open to capture as much of a strong move as possible.

Whether this fits a given strategy depends entirely on its nature; this is presented as common practice, not a strict requirement.

---

### Never Average Into a Losing Position

Unlike the take-profit guidance above, this next rule is **absolute**: never buy more of a losing position hoping it will "turn around soon." This is a genuinely dangerous habit, regardless of how it worked out in the past. There is no exception to this rule.

---

### Trailing Stop-Loss

As price moves favorably, a common technique is to move the stop-loss along with it — a **trailing stop**. This gradually pulls the stop-loss into profit territory, so that if price suddenly reverses, part of the gained profit is protected instead of being lost entirely.

Sometimes a small pullback triggers this trailing stop and closes the trade, only for price to resume in the original direction afterward. For this reason, maintaining a reasonable, consistent distance from price matters — commonly based on **ATR** (Average True Range), which reflects the average real volatility range over a recent period, or sometimes fixed at the same size as the initial stop-loss. The right logic varies by strategy, and the optimal distance should be determined through backtesting — a trailing stop does not automatically improve a strategy's expectancy; in some strategies, removing it entirely performs better.

A related technique is moving the stop-loss to the entry point (or just slightly beyond it, to cover spread and commission) once a trade is sufficiently in profit — commonly called making the trade **"risk-free,"** since a reversal from there no longer produces a loss.

---

### The One Rule That Is Never Optional

Moving a stop-loss in your favor is optional and strategy-dependent. Moving a stop-loss against your position — further into potential loss — is **never allowed, under any circumstance**. The stop-loss level must be decided at trade entry, based on sound mathematical logic confirmed through backtesting, and once set, it must never move in the unfavorable direction.

In short: moving a stop-loss favorably is optional; refusing to move it unfavorably is mandatory.

---

### Conclusion

These patterns — fixed risk sizing, a stop-loss defined by analysis invalidation rather than chart noise, staged take-profits, a strict ban on averaging into losses, and disciplined trailing-stop logic — represent the most common risk and money management practices for open positions. They aren't the only possible approaches; traders are free to develop their own methods through experience and backtesting, but the strictly prohibited actions must never be violated.

### One-Sentence

A stop-loss marks where your analysis becomes invalid, risk size should stay fixed at 1-2% (up to 5% max) of starting capital, averaging into losses is strictly forbidden, and a stop-loss may move favorably but must never move against your position.