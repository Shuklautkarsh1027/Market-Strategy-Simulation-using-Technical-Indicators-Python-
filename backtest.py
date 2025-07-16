
def backtest(df, initial_capital=100000):
    capital = initial_capital
    position = 0
    capital_over_time = []

    for i in range(1, len(df)):
        if df.loc[i-1, 'Signal'] == 1:  # Buy
            position = capital / df.loc[i, 'Close']
            capital = 0
        elif df.loc[i-1, 'Signal'] == -1 and position > 0:  # Sell
            capital = position * df.loc[i, 'Close']
            position = 0
        capital_over_time.append(capital + (position * df.loc[i, 'Close'] if position else 0))

    df = df.iloc[1:]
    df['Portfolio_Value'] = capital_over_time
    return df
