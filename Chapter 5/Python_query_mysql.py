import mysql.connector
try:
    cnx=mysql.connector.connect(user='niurou', 
                                password='8228198Yang!', 
                                host='127.0.0.1', 
                                database='sampledb')
    cursor=cnx.cursor()
    query=("select * from emps where empno > %s")
    # %s is a parameter to be passed in later on, in this example is empno=9001
    empno=9001
    # The query includes a placeholder %s which is used to represent the value that 
    # will be passed in later. This placeholder expects a tuple or a list, even if 
    # it only contains a single value.
    cursor.execute(query,(empno,))
    # pass in the binding variable within a tuple as the second parameter

    for (empno,empname,job) in cursor:
        print("{},{},{}".format(empno,empname,job))
        # "{},{},{}" is a string with three placeholders separated by commas. 
        # The placeholders are represented by curly braces {}.
    cursor=cnx.cursor()
    empno=9001
    query=("""Select e.empno, e.empname, e.job, s.salary 
           from emps e join salary s on e.empno=s.empno where e.empno > %s"""
    )
    cursor.execute(query,(empno,))
    for (empno, empname, job, salary) in cursor:
        print("{},{},{},{}".format(empno,empname,job,salary))

except mysql.connector.Error as err:
    print("Error-code:", err.errno)
    print("Error-Message:{}".format(err.msg))
finally:
    cursor.close()
    cnx.close()            