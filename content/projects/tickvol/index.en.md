---
title: Indicator for Measuring Changes in Average Trading Volume
description: The Tick Volume Delta indicator in MQL5 calculates the difference between tick volume and its simple moving average and displays it as a histogram.
date: 2026-07-01T00:00:00Z
draft: false
tags:
    - algorithmic trading
    - financial modeling
    - Tick Volume Delta
    - indicator
keywords:
    - Tick Volume Delta
    - indicator
slug: tick-volume-delta-mql5
categories:
    - indicator
---

### [Tick Volume Delta Indicator (github)](https://github.com/MahdiMasoumian/TickVolDelta_Indicator)

The Tick Volume Delta indicator calculates the difference between the current tick volume and its simple moving average, and displays the result as either a positive or negative value. When the current volume is higher than its moving average, a positive value is generated; when it is lower, a negative value is produced. This difference can be used to detect abnormal increases or decreases in market activity, and more importantly, to identify potential trend shifts driven by relative changes in volume compared to its baseline level.

Formula:

\[
\Delta_t = V_t - \frac{1}{N} \sum_{i=0}^{N-1} V_{t-i}
\]

Where:
- \(V_t\): tick volume at time \(t\)
- \(N\): moving average period
- \(\Delta_t\): deviation of volume from its moving average

Positive and negative values are displayed separately as a histogram.