import pandas as pd

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)
    return df

if __name__ == "__main__":
    df = load_and_preprocess_data('../data/gold_prices.csv')
    print(df.head())
