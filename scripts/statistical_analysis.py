import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_matrix(df):
    plt.figure(figsize=(10, 8))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix of Gold Prices')
    plt.savefig('../results/statistical_analysis_reports/correlation_matrix.png')
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('../data/gold_prices.csv', parse_dates=['Date'], index_col='Date')
    plot_correlation_matrix(df)
