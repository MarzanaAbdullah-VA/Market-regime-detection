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

## Project Structure
