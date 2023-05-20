import yfinance as yf

Google = yf.Ticker('GOOGL')
print(Google.actions)
#print(Google.dividends)
#print(Google.splits)
hist = Google.history(period='5d')
#hist=hist.drop('Dividends', axis=1)
#hist=hist.drop('Stock Splits', axis=1)
hist=hist.reset_index()
hist=hist.set_index('Date')

print(hist)
