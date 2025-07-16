def backtest(df, initial_capital=100000):
    capital = initial_capital
    position = 0
    entry_price = 0
    capital_over_time = []

    for i in range(1, len(df)):
        price = df.iloc[i]['Close']
        signal = df.iloc[i - 1]['Signal']

        # BUY
        if signal == 1 and capital > 0:
            position = capital / price
            entry_price = price
            capital = 0

        # SELL
        elif signal == -1 and position > 0:
            capital = position * price
            position = 0

        # Update portfolio value
        current_value = capital + (position * price if position > 0 else 0)
        capital_over_time.append(current_value)

    df = df.iloc[1:].copy()
    df.reset_index(drop=True, inplace=True)
    df['Portfolio_Value'] = capital_over_time
    return df
