import mysql.connector
# open a try/except block which provides a template for any database related
# operations you need to perform within your script
# You write the code for the operation in the try block, and if an error occurs when the 
# operation is carried out the execution is transferred to the except block
try:
    cnx=mysql.connector.connect(user='root', 
                                password='Shwa6163!', 
                                host='127.0.0.1', 
                                database='sampledb')
    # obtain a cursor object related to this connection.
    # the cursor object provides the means for statement execution as well as interface for
    # fetching the results
    cursor=cnx.cursor()
    #create a list of Tuples for emps table
    emps=[
      (9001, 'Jeff Russell','sales'),
      (9002, 'Jane Boorman','sales'),
      (9003, 'Tom Heints','sales')  
    ]
    #defining the query
    query_add_emp=("""INSERT INTO emps(empno, empname, job) VALUES (%s,%s,%s)""")
    #inserting the employee rows
    for emp in emps:
        cursor.execute(query_add_emp,emp)
    salary=[
        (9001,3000),
        (9002,2800),
        (9003,2500)
    ]
    query_add_salary=("""INSERT INTO salary(empno, salary) VALUES (%s,%s)""")
    
    for sal in salary:
        cursor.execute(query_add_salary,sal)
    
    orders=[
        (2608,9001,35),
        (2617,9001,35),
        (2620,9001,139),
        (2621,9002,95),
        (2626,9002,218),
    ]
    query_add_order=("""INSERT INTO orders(pono,empno, total) VALUES (%s,%s,%s)""")

    for order in orders:
        cursor.execute(query_add_order,order)
    # make all the insertions into the database permenent by using commit method
    cnx.commit()
except mysql.connector.Error as err:
    print("Error-code:", err.errno)
    print("Error-Message:{}".format(err.msg))
finally:
    cursor.close()
    cnx.close()    