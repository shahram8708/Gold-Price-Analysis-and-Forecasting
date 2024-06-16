import pandas as pd
import matplotlib.pyplot as plt

def plot_price_vs_events(df, events):
    plt.figure(figsize=(14, 7))
    plt.plot(df['Close'], label='Gold Price')
    
    for event in events:
        plt.axvline(x=event['date'], color='r', linestyle='--', lw=2)
        plt.text(event['date'], df['Close'].max(), event['description'], rotation=90, verticalalignment='bottom')
    
    plt.title('Gold Price and Significant Market Events')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.savefig('../results/market_sentiment_reports/price_vs_events.png')
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('../data/gold_prices.csv', parse_dates=['Date'], index_col='Date')
    events = [
        {'date': '2020-03-01', 'description': 'COVID-19 Pandemic'},
        {'date': '2016-11-08', 'description': 'US Presidential Election'},
    ]
    plot_price_vs_events(df, events)
