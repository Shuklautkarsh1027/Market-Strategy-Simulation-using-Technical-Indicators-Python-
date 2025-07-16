<img width="1919" height="1023" alt="image" src="https://github.com/user-attachments/assets/eeb43556-cdb7-463a-ae1b-d497fbd1be64" />

<img width="1919" height="1024" alt="image" src="https://github.com/user-attachments/assets/25ff832d-937e-4865-81c7-c63e803802aa" />



# Market Strategy Simulation — Quantitative Trading Project

This project demonstrates a simple rule-based trading strategy using technical indicators such as RSI and SMA, applied to synthetic stock market data. The goal is to simulate buy/sell decisions and track how a portfolio would perform over time, using Python.

## Project Objectives

- Simulate a trading strategy using historical stock data
- Apply technical indicators to generate trading signals
- Backtest the strategy and evaluate portfolio performance
- Visualize capital growth over time

---



---

## Strategy Logic

This is a rule-based trading strategy using two common indicators:

1. **RSI (Relative Strength Index)**  
   - Buy when RSI is below 30 (oversold condition) and price is above SMA  
   - Sell when RSI is above 70 (overbought condition) and price is below SMA  

2. **SMA (Simple Moving Average)**  
   - 20-day SMA is used to smooth out price trends and act as a confirmation signal

---

## Data

The dataset is fully synthetic but statistically realistic, covering the time period from **January 2021 to December 2024** for the following stocks:

- NIFTY50
- RELIANCE
- TCS
- INFY
- ICICIBANK
- HDFCBANK

Each row contains: Date, Ticker, Open, High, Low, Close, Volume.

