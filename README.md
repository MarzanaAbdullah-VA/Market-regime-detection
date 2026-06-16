# Market Regime Detection and Risk Analysis System

## Overview

This project is a market regime detection system that analyzes stock time series data to identify different market states — **Bull, Bear, and Recovery regimes**. It uses engineered financial risk features and unsupervised machine learning to uncover hidden market structures.

The goal is to better understand how market behavior changes over time using data-driven techniques.

---

## Objective

- Identify market regimes using historical stock price data
- Analyze risk characteristics across different regimes
- Build interpretable financial insights using k-means clustering

---

## Methodology

### 1. Data Collection
Historical stock price data (Oracle stock used in this project) is loaded for analysis.

### 2. Feature Engineering
The following financial features are created:

- **Returns**: Daily percentage change in price  
- **Volatility (20-day)**: Rolling standard deviation of returns  
- **Momentum (20-day)**: 20-day percentage price change  
- **Drawdown**: Decline from historical peak  
- **Moving Average Ratio**: Trend indicator (MA20 / MA100)

---

### 3. Market Regime Detection

Unsupervised learning is applied using:

- **K-Means Clustering**
- Standardized feature scaling using `StandardScaler`

The model groups market conditions into 3 regimes:
- Bull Market
- Bear Market
- Recovery / High Volatility Regime

---

### 4. Risk Analysis

Each regime is analyzed using:
- Average returns
- Volatility levels
- Momentum behavior
- Drawdown severity

This helps interpret the financial meaning of each cluster.

---

### 5. Visualization

The system plots:
- Stock price over time
- Color-coded market regimes
- Trend behavior across different market states

---
[Plot](regimes_plot.png)


## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---


## Key Findings
Three distinct market regimes were identified using K-Means clustering based on returns, volatility, momentum, and drawdown characteristics.

- Bull Regime (Regime 0) exhibited the strongest average returns (1.41%) and highest momentum (0.21), indicating favorable market conditions. Although volatility was elevated, drawdowns remained significantly lower than those observed during bearish periods.
- Bear Regime (Regime 1) was characterized by negative average returns (-0.48%), negative momentum (-0.10), and the deepest drawdowns (-35.7%), reflecting sustained market weakness and increased downside risk.
- Recovery Regime (Regime 2) demonstrated the lowest volatility (1.76%), modest positive returns, and positive momentum, suggesting transitional market conditions consistent with a recovery phase following periods of market stress.

The analysis highlights how market environments can exhibit distinct risk and return profiles, providing insights that may support portfolio risk management, asset allocation decisions, and market monitoring.
The clustering approach revealed meaningful differences in market behavior that are not immediately apparent from price trends alone, demonstrating the value of unsupervised machine learning for financial market analysis.



