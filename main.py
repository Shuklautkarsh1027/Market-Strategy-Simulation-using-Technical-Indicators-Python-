
import pandas as pd
from src.indicators import calculate_sma, calculate_rsi
from src.strategy import generate_signals
from src.backtest import backtest
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/synthetic_financial_data_2021_2024.csv")
df = df[df['Ticker'] == 'RELIANCE'].copy()

# Calculate indicators
df['SMA20'] = calculate_sma(df, 20)
df['RSI'] = calculate_rsi(df)

# Generate signals
df = generate_signals(df)

# Run backtest
df = backtest(df)

# Plot
plt.plot(df['Date'], df['Portfolio_Value'])
plt.title("Portfolio Value Over Time — RELIANCE Strategy")
plt.xlabel("Date")
plt.ylabel("Capital")
plt.grid(True)
plt.tight_layout()
plt.show()
