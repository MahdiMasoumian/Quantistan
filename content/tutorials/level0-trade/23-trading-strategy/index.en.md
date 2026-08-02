---
title: 0-23- What Is a Trading Strategy?
description: "Learn what a trading strategy really is: a clear, written, repeatable set of rules with no room for ambiguity, judgment, or subjective decisions."
date: 2026-08-02T11:29:06.265Z
draft: false
slug: 0-23-what-is-a-trading-strategy
categories:
    - Basic
tags:
    - trading strategy
    - rule-based trading
    - algorithmic trading
    - entry and exit rules
    - position sizing
keywords:
    - trading strategy
author: Mohammad Mahdi Masoumian
homepage.showRecent: true
fmContentType: tutorials
---

### Why the Trading Strategy Is the Core of Everything

A **trading strategy** is arguably the single most important concept in algorithmic trading. It doesn't matter whether the end goal is a fully automated system that executes trades on its own, a signal generator that flags opportunities, or a decision-support tool that suggests trades to a human — in every one of these scenarios, the trading strategy is the core, and everything else in the system must be built around it, not the other way around.

The execution method, the platform, the programming language — all of these are implementation details. The strategy is the actual substance of what's being built.

---

### What a Trading Strategy Actually Is

At its core, a **trading strategy** is a clear, written, repeatable set of instructions. It defines exactly when to enter a trade, when to exit, and how much to trade — with no room left for interpretation.

The critical test of a real trading strategy is simple: if you handed it to a completely different person, would they make exactly the same trading decisions you would, given the same market data? If the answer is yes, it's a strategy. If the answer depends on that person's mood, experience, or "feel" for the market, it isn't a strategy yet — it's still a set of ideas or preferences.

This means a trading strategy, by definition, cannot contain words like "maybe," "usually," "if it looks right," or "depending on the situation." Every one of those phrases represents a decision point that hasn't actually been defined yet.

---

### A Strategy Is Already an Algorithm

This is a point that's easy to miss: a well-written trading strategy is not something separate from an algorithm — it already **is** an algorithm. It's simply written in plain language instead of code.

A properly written strategy describes a step-by-step, repeatable process: given this specific market condition, take this specific action. That is precisely the definition of an algorithm. The job of turning a strategy into working code is not one of invention — it's one of **translation**. If the strategy itself contains ambiguity or contradiction, no amount of good coding can fix that; the resulting algorithm will simply inherit the same ambiguity.

This is why strategy development deserves as much rigor as the coding itself, if not more. A flawed strategy produces a flawed algorithm, no matter how well it's implemented.

---

### Every Component Must Be Internally Consistent

For a strategy to be translatable into code, every one of its components must work together without contradiction. There cannot be one rule that implies a long entry while another rule, under the same conditions, implies staying out of the market. Any such conflict has to be resolved and made explicit *before* implementation — not discovered and patched during coding, and never left to be decided arbitrarily by the person running the strategy.

---

### Position Sizing and Entry/Exit Logic Must Be Mathematically Defined

Beyond the general "when to buy or sell" logic, a complete trading strategy must also define two things with mathematical precision:

* **Position sizing:** exactly how much capital or how many units are allocated to a given trade, expressed as a precise formula or rule — not a rough estimate.
* **Entry and exit points:** the exact price levels, conditions, or triggers that define when a position is opened and when it is closed, again expressed in unambiguous, calculable terms.

Both of these must be defined with the same level of clarity as the rest of the strategy. A strategy that says "enter when the trend looks strong" is incomplete; a strategy that says "enter when a 20-period moving average crosses above a 50-period moving average" is implementable.

---

### The Cost of Ambiguity

Any part of a strategy left vague eventually has to be resolved by someone — and if it isn't resolved in the strategy document itself, it will be resolved arbitrarily, either by whoever writes the code, or worse, inconsistently every time the strategy is run manually. This defeats the entire purpose of having a strategy in the first place, which is repeatability and the removal of subjective judgment from the trading process.

---

### Conclusion

A trading strategy is the foundation that everything else in algorithmic trading is built on top of, regardless of whether the end system is fully automated, a signal generator, or a decision-support tool. It must be written clearly enough that any two people — or a person and a machine — would reach the exact same decision given the same data, with position sizing and entry/exit logic defined through precise, mathematical rules rather than subjective judgment.

### One-Sentence

A true trading strategy is a clear, written, internally consistent, and repeatable set of rules — with entry, exit, and position sizing defined in precise mathematical terms and no room left for subjective judgment.