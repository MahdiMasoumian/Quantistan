---
title: Lightweight Data Pipeline for Live Trading and ML/DL
description: A modular, bias-aware data pipeline for MT5 that performs feature engineering, calendar reconstruction, and gap filling for live trading and machine learning.
date: 2026-08-02T06:35:22.269Z
draft: false
slug: lightweight-data-pipeline-live-trading-financial-ml
categories:
  - PythonLib
tags:
  - Python
  - MetaTrader 5
  - data pipeline
  - algorithmic trading
  - financial machine learning
keywords:
  - Data Pipeline
  - MetaTrader 5
  - Feature Engineering
author: Mohammad Mahdi Masoumian
citation: https://doi.org/10.5281/zenodo.21695559
homepage:
  showRecent: true
fmContentType: projects
---
# Lightweight Data Pipeline for Live Trading and Financial Machine Learning
(Python 3.12.7)
### [**Download from GitHub**](https://github.com/MahdiMasoumian/MT5_Data_Pipeline/tree/main)
## Overview

This repository has a small, modular data pipeline for quantitative finance, algorithmic trading, and financial machine learning.

The pipeline pulls market data from MetaTrader 5, creates useful features, rebuilds a clear trading calendar, fills missing points with a strict backward-only method, and produces a clean dataset for both past study and live trading.

Unlike many research-focused prep pipelines, this tool is built first for live market use. Each step is designed to avoid look-ahead bias while staying light enough for steady use on trading servers with limited resources.

---

## Main Features

* Direct market data pull from MetaTrader 5
* Support for fixed date ranges and rolling-window (Len) downloads
* Multi-symbol dataset creation
* Automatic calendar rebuild
* Backward-only gap filling (no future leak)
* Configurable technical indicator creation
* Optional close-only dataset creation
* Automatic column prefixing for multi-asset datasets
* Lightweight design for live use
* Modular design for easy extension

---

## Pipeline Structure

The pipeline has five main modules.

### 1. fast_download_data()

Downloads OHLC, spread, and tick volume from MetaTrader 5.

Supports:

* Fixed historical date range
* Most recent N candles (rolling window)

---

### 2. add_indict()

Creates technical indicators from the options in `config.py`.

The current version includes:

* ATR
* SMA
* Rolling Standard Deviation
* Trend Moving Average
* Pivot & Distance to Pivot
* RSI
* Moving Average Cross
* Price Action Feature

Rows with missing indicator values are removed to avoid warm-up effects.

---

### 3. build_calendar()

Builds a full trading calendar based on the selected time frame.

Supports:

* M1
* M5
* M15
* H1
* H4
* D1

Weekends can be left out when needed, depending on the asset.

---

### 4. gap_fill()

Fills missing points after symbols are merged.

Rules:

* OHLC → previous close
* Spread → carried forward
* Tick Volume → zero
* Indicators → last available value

No future data are used in this process.

---

### 5. download_data()

Main workflow function.

It runs these steps in order:

1. Download data
2. Create indicators
3. Merge symbols
4. Build calendar
5. Fill gaps
6. Save the final dataset

---

## Configuration

All pipeline settings are controlled through `config.py`.

Main options include:

* Symbols
* Time frame
* Download mode
* Historical dates
* Rolling window length
* Indicator selection
* Indicator settings
* Calendar mode
* Output format
* Save options

No change to `DataPipeline.py` is needed for normal use.

---

## Download Modes

### Historical Mode

Downloads all available candles between a start and end date you choose.

Best for:

* Dataset building
* Research
* Backtesting

---

### Rolling Window Mode (Len)

Downloads the latest N candles for each symbol.

The calendar is built over the shared time period for all symbols, which helps avoid extra forward-filled rows caused by different market schedules.

Best for:

* Live trading
* Paper trading
* Ongoing model use

---

## Design Principles

The design follows a few key ideas.

* No look-ahead bias
* Works with live markets
* Light on compute
* Modular design
* Uses broker-native market data
* Lets you tune features
* Gives repeatable results

---

## Requirements

Python 3.12.7

Main libraries

* pandas 2.2.2
* MetaTrader5 5.0.5200
* ta 0.11.0

A working MetaTrader 5 terminal with access to the symbols you need is required.

---

## Example

```python
from DataPipeline import download_data

df = download_data()

print(df.head())
```

---

## Typical Applications

* Algorithmic trading
* Financial machine learning
* Time-series forecasting
* Cross-asset modeling
* Feature engineering
* Backtesting
* Live trading systems
* Explainable AI for finance

---

## Limitations

* Tick-by-tick market data are not supported.
* The pipeline depends on MetaTrader 5 as its data source.
* Fees, slippage, and swap are not modeled inside it.
* Assets with very different trading calendars should not be processed together in one run.

---

## Citation

If you use this repository in your work, please cite the archived version:

Masoumian, Mohammad Mahdi. (2026).  
*Design and Implementation of a Low-Resource, Bias-Aware Data Pipeline for Live Trading, Rule-Based Systems, and Financial Machine Learning*.  
Zenodo. https://doi.org/10.5281/zenodo.21695559

---

## License

This project is released under the MIT License.
