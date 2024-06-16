import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series(df):
    plt.figure(figsize=(14, 7))
    plt.plot(df['Close'], label='Close Price')
    plt.title('Gold Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.savefig('../results/time_series_visualizations/gold_price_over_time.png')
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('../data/gold_prices.csv', parse_dates=['Date'], index_col='Date')
    plot_time_series(df)
