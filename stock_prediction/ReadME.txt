# Intraday Stock Market Prediction Tool V_1


This project is a **real-time stock market prediction tool** designed for intraday trading. It fetches live stock data, predicts short-term market movements, and visualizes them with a dynamic line graph. The predictions are updated at 1-minute intervals to assist traders in making informed decisions.

---

## Features
- **Real-Time Data Fetching**: Fetches live market data using Yahoo Finance.
- **Short-Term Predictions**: Uses Linear Regression to predict stock prices for the next 5 minutes.
- **Dynamic Visualization**: Displays actual and predicted prices in a user-friendly line graph.
- **Market Hour Check**: Ensures data fetching only occurs during market hours (Indian stock market timings: 9:15 AM to 3:30 PM IST).

---

## How to Run

### Prerequisites
1. Python 3.7+
2. Required libraries:
   - `yfinance`
   - `pandas`
   - `numpy`
   - `matplotlib`
   - `scikit-learn`
   - `pytz`

Install dependencies using:
```bash
pip install yfinance pandas numpy matplotlib scikit-learn pytz
