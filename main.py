
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

df = generate_signals(df)
trades = []
capital = 100000
position = 0

for i in range(1, len(df)):
    price = df.iloc[i]['Close']
    signal = df.iloc[i - 1]['Signal']
    date = df.iloc[i]['Date']

    if signal == 1 and capital > 0:
        position = capital / price
        trades.append({'Date': date, 'Action': 'Buy', 'Price': price, 'Capital': capital})
        capital = 0

    elif signal == -1 and position > 0:
        capital = position * price
        trades.append({'Date': date, 'Action': 'Sell', 'Price': price, 'Capital': capital})
        position = 0
        
import pandas as pd
trades_df = pd.DataFrame(trades)
trades_df.to_csv("output/trades.csv", index=False)


print(df['Signal'].value_counts())

print(df[df['Signal'] != 0][['Date', 'Close', 'RSI', 'SMA20', 'Signal']].head(10))
