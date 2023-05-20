import json
import pandas as pd
data=[
    {"Empno":9001, "Salary":3000},
    {"Empno":9002, "Salary":2800},
    {"Empno":9003, "Salary":2400}
]
json_data=json.dumps(data)
print(json_data)
salary=pd.read_json(json_data)
salary=salary.set_index('Empno')
new_salary=pd.Series({'Salary':3200}, name=9005)
salary=salary._append(new_salary)
#salary=salary._append({'Empno':9005, 'Salary':3200},ignore_index=True)
print(salary)



print(salary)

data=[
    ['9001','Jeff','sales'],
    ['9002','Jane','sales'],
    ['9003','Tom','sales']
]
emps=pd.DataFrame(data,columns=['Empno','Name','Job'])
column_type = {'Empno':int, 'Name': str, 'Job': str}
emps=emps.astype(column_type)
emps= emps.set_index('Empno')
new_emp= pd.Series({'Name':'John','Job':'sales'}, name=9004)
emps=emps._append(new_emp)
print(emps)
emps_salary=emps.join(salary,how='inner')
print(emps_salary)
#column_type = {'Empno':int, 'Name': str, 'Job': str, 'Salary':int}
#emps_salary=emps_salary.astype(column_type)

data=[
    [2608,9001,35],[2617,9001,35],[2620,9001,139],[2621,9002,95],
    [2626,9002,218]
]
orders=pd.DataFrame(data,columns=['Pono','Empno','Total'])
print(orders)
emps_orders=emps.merge(orders, how='right',left_on='Empno', right_on='Empno').set_index('Pono')
print(emps_orders)

print(orders.groupby(['Empno'])['Total'].mean())
print(orders.groupby(['Empno'])['Total'].sum())