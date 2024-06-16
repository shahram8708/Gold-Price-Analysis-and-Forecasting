import pandas as pd
import numpy as np

def simple_moving_average_strategy(df, short_window=40, long_window=100):
    signals = pd.DataFrame(index=df.index)
    signals['signal'] = 0.0

    signals['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   

    signals['positions'] = signals['signal'].diff()

    return signals

if __name__ == "__main__":
    df = pd.read_csv('../data/gold_prices.csv', parse_dates=['Date'], index_col='Date')
    signals = simple_moving_average_strategy(df)
    signals.to_csv('../results/trading_strategies/sma_strategy_signals.csv')
    print(signals.head())
