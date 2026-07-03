---
title: 1-3- What Are Decision Support Systems?
date: 2026-06-27T17:26:21.462Z
draft: false
description: An introduction to Decision Support Systems (DSS) and their role in algorithmic trading.
params:
    author: Mohammad Mahdi Masoumian
categories:
    - Basic Concepts
keywords:
    - Decision Support Systems
---

### Decision Support Systems

Decision Support Systems (DSS) are among the simplest yet most practical forms of algorithmic trading systems. Contrary to a common misconception, the objective of every trading algorithm is not to execute trades automatically. In many cases, the algorithm's role is limited to continuously monitoring the market, identifying potential trading opportunities, and notifying the trader, while the final decision to enter or exit a position remains entirely under human control.

In this type of system, the algorithm continuously scans a predefined set of financial instruments according to the rules of a trading strategy. Whenever the predefined entry or exit conditions are satisfied, the system generates a trading signal and delivers it to the trader. Notifications may be presented in various forms, such as the output of a live Python application, desktop or mobile notifications, or messages sent through communication platforms. A typical trading signal includes information such as the financial instrument, trade direction (long or short), entry price, target price, stop-loss level, and the recommended position size.

An important characteristic of Decision Support Systems is that they never execute trades automatically. Once a signal is generated, the trader has sufficient time to review current market conditions and decide whether the proposed trade should actually be executed. As a result, DSS can be viewed as a bridge between fully manual trading and fully automated trading. The algorithm improves the speed and accuracy of market analysis, while the responsibility for the final trading decision remains with the trader.

One of the greatest advantages of this approach is improved time efficiency. In manual trading, market participants often spend long hours monitoring charts to avoid missing profitable trading opportunities. With a Decision Support System, this responsibility is delegated to the algorithm. Consequently, traders only need to pay attention when a valid trading setup has been detected, allowing them to make much more efficient use of their time. This not only increases productivity but also significantly reduces the likelihood of missing high-quality trading opportunities due to the inability to monitor the market continuously. This advantage is particularly valuable for trading strategies that generate relatively few signals but exhibit a high success rate.

Another important benefit of this approach is its flexibility compared to fully automated trading systems. During periods of abnormal market behavior—such as major economic announcements, unexpected news events, or episodes of extreme volatility—a fully automated trading system may continue executing trades without recognizing the broader market context, potentially resulting in unnecessary losses. Decision Support Systems eliminate this risk because they never submit orders directly to the market. Instead, they simply provide trading recommendations, allowing the trader to recognize unusual market conditions and decide not to execute the suggested trade.

However, this approach is not without limitations. Since the final decision remains with the trader, many of the behavioral challenges associated with manual trading still exist. Psychological factors such as fear, greed, hesitation, abandoning a trading plan, or second-guessing a valid trading signal can still influence trading performance. In other words, while Decision Support Systems substantially reduce the operational burden of continuously monitoring the market, they cannot eliminate human behavioral biases.

Overall, Decision Support Systems are well suited for traders who wish to benefit from continuous market monitoring and automated signal generation while maintaining complete control over trade execution. For many market participants, they represent the first practical step toward algorithmic trading and are widely used in financial markets where human supervision remains an essential part of the decision-making process.

### Large Language Models

Recent advances in artificial intelligence, particularly the emergence of Large Language Models (LLMs), have significantly expanded the capabilities of Decision Support Systems. In addition to analyzing numerical market data, these models are capable of processing unstructured textual information such as financial news, corporate reports, regulatory announcements, and other market-related documents, enabling them to provide richer context for trading decisions. The integration of LLMs into algorithmic trading is an advanced topic and will be discussed in detail in later sections of this course.

### Summary

In essence, a Decision Support System acts as an intelligent market observer. It continuously monitors financial markets, detects potential trading opportunities, and alerts the trader whenever the predefined conditions of a trading strategy are satisfied. By automating market surveillance rather than trade execution, DSS improves the speed and consistency of strategy implementation, increases the number of opportunities that can be monitored simultaneously, and allows traders to spend significantly less time watching the market while still retaining full control over every trading decision.