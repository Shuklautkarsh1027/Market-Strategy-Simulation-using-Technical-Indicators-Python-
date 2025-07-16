
def generate_signals(df):
    df['Signal'] = 0
    df.loc[(df['RSI'] < 30) & (df['Close'] > df['SMA20']), 'Signal'] = 1  # Buy
    df.loc[(df['RSI'] > 70) & (df['Close'] < df['SMA20']), 'Signal'] = -1  # Sell
    return df
