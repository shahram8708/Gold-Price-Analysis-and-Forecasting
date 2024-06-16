import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

def prepare_features(df):
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    df['Day'] = df.index.day
    X = df[['Open', 'High', 'Low', 'Volume', 'Year', 'Month', 'Day']]
    y = df['Close']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_and_save_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, '../results/predictive_models/linear_regression_model.pkl')

def evaluate_model(X_test, y_test):
    model = joblib.load('../results/predictive_models/linear_regression_model.pkl')
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

if __name__ == "__main__":
    df = pd.read_csv('../data/gold_prices.csv', parse_dates=['Date'], index_col='Date')
    X_train, X_test, y_train, y_test = prepare_features(df)
    train_and_save_model(X_train, y_train)
    evaluate_model(X_test, y_test)
