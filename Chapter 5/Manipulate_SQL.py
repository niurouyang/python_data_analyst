import pandas as pd
import mysql.connector
try:
        cnx=mysql.connector.connect(user='niurou', 
                                password='8228198Yang!', 
                                host='127.0.0.1', 
                                database='sampledb')
        query_sql=("""select s.* from stocks as s
                        left join
                            (select distinct(ticker) from
                                (select price/lag(price) over(partition by ticker order by date) as dif,
                                ticker from stocks) as b
                            where dif< 0.99) as a
                        on a.ticker= s.ticker
                        where a.ticker is null;""")
        cursors=cnx.cursor()
        cursors.execute(query_sql)
        for df_stocks in cursors:
             print(df_stocks)
        #df_stocks=pd.read_sql(query_sql,con=cnx)
        #df_stocks=df_stocks.set_index(['ticker','date'])
        #print(df_stocks)
except mysql.connector.Error as err:
    print("Error-code:", err.errno)
    print("Error-Message:{}".format(err.msg))
finally:
    cnx.close()            