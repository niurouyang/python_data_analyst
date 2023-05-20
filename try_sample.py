import yfinance as yf

# Download data for Apple from 2020-01-01 to 2021-12-31
data = yf.download('AAPL', start='2020-01-01', end='2021-12-31')

# Display the first few rows of the DataFrame
print(data.head())
