orders=[
    (9423517,'2022-02-04',9001),
    (4626232,'2022-02-04',9003),
    (9423534,'2022-02-04',9001),
    (9423679,'2022-02-05',9002),
    (4626377,'2022-02-05',9003),
    (4626412,'2022-02-05',9004),
    (9423783,'2022-02-06',9002),
    (4626490,'2022-02-06',9004)
]

import pandas as pd
df_orders= pd.DataFrame(orders,columns=['OrderNo','Date','Empno'])

details=[
    (9423517,'Jeans','Rip Curl', 87.0,1),
    (9423517,'Jacket','The North Face', 112.0,1),
    (4626232,'Socks','Vans', 15.0,1),
    (4626232,'Jeans','Quiksilver', 82.0,1),
    (9423534,'Socks','DC', 10.0,2),
    (9423534,'Socks','Quiksilver', 12.0,2),
    (9423679,'T-shirt','Patagonia', 35.0,1),
    (4626377,'Hoody','Animal', 38.0,1),
    (4626377,'Shirt','Volcom', 78.0,1),
    (9423783,'Boxer shorts','Superdry', 30.0,2),
    (9423783,'Shorts','Globe', 26.0,1),
    (4626490,'Cargo Shorts','Billabong', 54.0,1),
    (4626490,'Sweater','Dickies', 56.0,1)
]
df_details=pd.DataFrame(details,columns=['OrderNo','Item','Brand','Price','Quantity'])

emps=[
    (9001,'Jeff Russel','LA'),
    (9002,'Jane Boorman','San Francisco'),
    (9003,'Tom Heints','NYC'),
    (9004,'Maya Silver','Philadelphia')
]
df_emps=pd.DataFrame(emps,columns=['Empno','Empname','Location'])

locations=[
    ('LA','West'),
    ('San Francisco','West'),
    ('NYC','East'),
    ('Philadelphia','East')
]
df_locations=pd.DataFrame(locations,columns=['Location','Region'])


df_sales=df_orders.merge(df_details)
df_sales['Total']=df_sales['Price']*df_sales['Quantity']
df_sales=df_sales[['Date','Empno','Total']]
df_sale_emps=df_sales.merge(df_emps)
df_results=df_sale_emps.merge(df_locations)
df_results=df_results[['Date','Region','Total']]
#print(df_results)

df_date_region=df_results.groupby(['Date','Region']).sum()
#print(df_date_region[[True,False,False,False,False,False]])
# view specific aggregations by multiindex
#print(df_date_region.index.isin([('2022-02-05','West')]))
#print(df_date_region[df_date_region.index.isin([('2022-02-05','West')])])
#print(df_date_region[df_date_region.index.isin([('2022-02-05','West'),('2022-02-05','East')])])
#print(df_date_region[('2022-02-04','East'):('2022-02-05','West')])
# Slicing a range of Aggregated values
# should be the same as df_date_region[('2022-02-04'):('2022-02-05')]
#print(df_date_region.loc[slice('2022-02-05','2022-02-06'),slice(None), :])
# slice function, slice(start, stop, step). start, stop is the indexs where you want to start
# and stop.
# loc method, df.loc(row,column)
#:] means that you are using row labels rather than column labels.
# print(df_date_region.loc[('2022-02-05','2022-02-06'),('West','East'),:])

# Add a grand total
ps=df_date_region.sum()
#print(ps)
ps.name=('All','All')
df_date_region_total=df_date_region._append(ps)
#print(df_date_region_total)
#print(df_date_region_total[df_date_region_total.index.isin([('All','All')])])

# Add subtotal
ps1=df_date_region.groupby(['Date']).sum()
#ps1.name=('Date','All')
#print(ps1)
for ps1_date,ps1_data in ps1.iterrows():
    print(df_date_region[df_date_region.index.isin([(ps1_date,'')])])
    #print(ps1)
    print(ps1_data)

print(df_date_region_total)    