---
title: A Framework for Evaluating Position Sizing Policies in Algorithmic Trading
description: Explore an open-source Monte Carlo framework for evaluating money-management policies in algorithmic trading, comparing fixed-dollar and percentage-of-equity position sizing under realistic transaction costs, with a cost-adjusted Kelly criterion.
date: 2026-09-03T00:00:00.000Z
draft: false
tags:
  - Algorithmic Trading
  - Risk Management
  - Position Sizing
  - Monte Carlo Simulation
  - Kelly Criterion
  - Quantitative Finance
citation: https://doi.org/10.2139/ssrn.7382618
author: Mohammad Mahdi Masoumian
keywords:
  - Algorithmic Trading
  - Risk Management
  - Position Sizing
  - Monte Carlo Simulation
  - Kelly Criterion
slug: position-sizing-policies-monte-carlo-algorithmic-trading
categories:
  - Preprint
  - Open Access
  - Risk Management
homepage:
  showRecent: true
---
<br>
full title:

## **A Framework for Evaluating Position Sizing Policies in Algorithmic Trading: A Monte Carlo Analysis of Compound Growth, Market Frictions, and the Opportunity Cost of Capital**

**Author:** Mohammad Mahdi Masoumian (Babol Noshirvani University of Technology)

**Publisher/Release date:** Posted: 3 Sep 2026 | Date Written: August 31, 2026

[**Download PDF**](https://doi.org/10.2139/ssrn.7382618)

**Abstract**

Comprehensive risk and performance evaluation of algorithmic trading strategies requires more than headline metrics such as cumulative return, the Sharpe ratio, or maximum drawdown; it demands rigorous treatment of position sizing, transaction costs, ruin probability, and drawdown dynamics under realistic trading conditions. A review of the literature reveals considerable heterogeneity in this regard: while some studies incorporate risk-controlled position sizing and transaction costs explicitly, others omit these elements entirely, producing backtests whose reported profitability can be substantially inflated. This study develops an open-source, Monte Carlo-based framework for evaluating money-management policies in algorithmic trading, moving from a frictionless theoretical expectancy criterion to a cost-adjusted, empirically simulated assessment of realized growth, drawdown, ruin probability, and capital utilization. Two competing position-sizing policies-fixed-dollar and percentage-of-equity-are compared, and a cost-adjusted Kelly criterion is derived to determine the optimal risk fraction. Applied to a representative reference strategy, the framework demonstrates that neglecting realistic transaction costs can overstate reported returns by a substantial margin, underscoring the risk of a false impression of profitability in cost-blind backtesting. All Python code underlying this framework has been released publicly in an open-source repository to support transparency and reproducibility in future research.

**Keywords:** Algorithmic Trading, Risk Management, Position Sizing, Monte Carlo Simulation, Kelly Criterion

citation:
> Masoumian, M. M. (2026). A Framework for Evaluating Position Sizing Policies in Algorithmic Trading: A Monte Carlo Analysis of Compound Growth, Market Frictions, and the Opportunity Cost of Capital. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.7382618