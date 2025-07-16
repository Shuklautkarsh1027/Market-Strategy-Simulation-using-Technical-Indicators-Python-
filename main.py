import pandas as pd
import matplotlib.pyplot as plt
from src.indicators import calculate_sma, calculate_rsi
from src.strategy import generate_signals
from src.backtest import backtest

# Step 1: Load and filter data
df = pd.read_csv("data/synthetic_financial_data_2021_2024.csv")
df = df[df['Ticker'] == 'RELIANCE'].copy()

# Step 2: Compute indicators
df['SMA20'] = calculate_sma(df, 20)
df['RSI'] = calculate_rsi(df)

# Step 3: Generate signals
df = generate_signals(df)

# Step 4: Backtest the strategy
df = backtest(df)
df.reset_index(drop=True, inplace=True)

# Step 5: Debug info (optional)
print(df['Signal'].value_counts())
print(df[df['Signal'] != 0][['Date', 'Close', 'RSI', 'SMA20', 'Signal']].head(10))

# Step 6: Plot price + signals
buy_signals = df[df['Signal'] == 1]
sell_signals = df[df['Signal'] == -1]

plt.figure(figsize=(14, 6))
plt.plot(df['Date'], df['Close'], label='Close Price', color='lightblue')
plt.plot(df['Date'], df['SMA20'], label='SMA20', color='orange')

plt.scatter(buy_signals['Date'], buy_signals['Close'], label='Buy Signal', color='green', marker='^', s=100)
plt.scatter(sell_signals['Date'], sell_signals['Close'], label='Sell Signal', color='red', marker='v', s=100)

plt.title("RELIANCE Price with Buy/Sell Signals")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 7: Export trades to CSV
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

# Save trades
trades_df = pd.DataFrame(trades)
trades_df.to_csv("output/trades.csv", index=False)
