---
title: 0-13- What Is Margin, and What Is a Margin Call?
date: 2026-08-02T07:39:06.045Z
draft: false
description: Understand what margin actually is, how it differs from equity and balance, and why a sharp drop in margin level triggers what brokers call a margin call.
tags:
    - margin
    - equity
    - margin call
    - risk management
    - financial markets
categories:
    - Intermediate
keywords:
    - Margin
    - Margin Call
homepage:
    showRecent: true
author: Mohammad Mahdi Masoumian
slug: 0-13-margin-and-margin-call
---

### What Is Margin?

**Margin** is the amount of your own capital that you must set aside as collateral in order to open and maintain a leveraged position. It is not a fee and not spent — it is money that gets "locked" by the broker for as long as your position stays open.

If you open a position worth $10,000 using 1:100 leverage, your required margin is $100 — the remaining $9,900 is effectively covered by the leverage the broker provides.

---

### Margin vs. Balance vs. Equity

These three terms are frequently confused, but each means something different:

* **Balance:** the total amount of money in your account, not counting any open (unrealized) positions. If you have no open trades, balance and equity are the same.
* **Equity:** your balance adjusted for the current floating (unrealized) profit or loss of your open positions. Equity changes in real time as the market moves. `Equity = Balance + Floating P/L`
* **Margin (Used Margin):** the portion of your equity that is locked as collateral for your currently open positions.
* **Free Margin:** the portion of your equity that is *not* locked, and is therefore available to open new positions or absorb further floating losses. `Free Margin = Equity − Used Margin`

A useful way to think about it: **equity is what your account is actually worth right now**, margin is the part of that value being held as collateral, and free margin is your cushion.

---

### Margin Level

Brokers monitor a ratio called **margin level**, which shows how much of your equity is covered relative to the margin currently in use:

`Margin Level (%) = (Equity / Used Margin) × 100`

A high margin level means your account has a healthy buffer. A low margin level means your equity is getting dangerously close to the amount locked as collateral — in other words, your floating losses are eating into the money backing your open positions.

---

### What Is a Margin Call?

When your floating losses grow large enough that your margin level drops below a threshold set by the broker, the broker issues what is known as a **margin call**.

The name comes from the earlier days of trading, before electronic platforms existed: when a client's account reached this dangerous level, the broker would literally place a phone call to the trader, asking them to either deposit additional funds to restore the margin level, or close part of their position to reduce the exposure. That literal phone call is where the term "margin call" comes from — even today, when everything happens automatically through software, the name has stuck.

In modern trading platforms, a margin call is usually shown as a warning notification or account status change rather than an actual phone call, but the underlying meaning is identical: your equity is no longer sufficiently covering your open positions, and action is required.

---

### What Happens If Nothing Is Done?

A margin call is a warning, not the end of the story. If the trader takes no action and the market continues to move against the position, equity keeps shrinking further. If margin level falls below an even lower threshold — often called the **stop-out level** — the broker will begin to automatically close positions, starting usually with the most unprofitable one, without waiting for the trader's confirmation. This is done to prevent the account's equity from going negative and protect both the trader and the broker.

The exact margin call and stop-out percentages vary by broker and by asset class, so it's important to know these thresholds for your specific broker and account type.

---

### Conclusion

Margin is the portion of your capital locked as collateral for open positions, while equity reflects the real-time value of your entire account including floating profit or loss. A margin call occurs when losses push your equity dangerously close to your used margin — a warning, named after the literal phone calls brokers once made, that requires the trader to either add funds or reduce exposure before the broker steps in and closes positions automatically.

### One-Sentence

Margin is the collateral locked for your open positions, and a margin call is the broker's warning — originally a literal phone call — that your equity has dropped too close to that collateral.