import yfinance as yf
data=[]
tickers=['TSLA','META','ORCL','AMZN']
for ticker in tickers:
    tkr=yf.Ticker(ticker)
    # return a ticker object
    hist=tkr.history(period='5d').reset_index()
    # history method returns stock data as a pandas dataframe with the Date as the index
    # remove Date column as index
    print(hist)
    records=hist[['Date','Close']].to_records(index=False)
    
    
    # take only Date and Close column, and convert them to a Numpy record array.
    records=list(records)
    # conver the data to a list of tuples
    records=[(ticker,str(elem[0])[:10],round(elem[1],2)) for elem in records]
    # reformat each tuple so that it can be inserted into the stocks database table as a row
    # taking only the first 10 characters of filed 0(elem[0])[:10]), you can extract 
    # just the year, month, and day.
    data=data+records
    print(data)

import mysql.connector
from mysql.connector import errorcode
try:
    cnx=mysql.connector.connect(user='niurou', 
                                password='8228198Yang!', 
                                host='127.0.0.1', 
                                database='sampledb')
    cursor=cnx.cursor()
    query_add_stock=("Insert into stocks(ticker, date,price) value (%s, %s, %s)")
    cursor.executemany(query_add_stock,data)
    cnx.commit()

except mysql.connector.Error as err:
    print("Error-code:", err.errno)
    print("Error-Message:{}".format(err.msg))
finally:
    cursor.close()
    cnx.close()      