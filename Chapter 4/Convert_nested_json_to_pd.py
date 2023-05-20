data=[{"Emp":"Jeff Russell",
       "POs":[{"Pono":2608, "Total":35},
              {"Pono":2617, "Total":35},
              {"Pono":2620, "Total":139}
              ]},
      {"Emp":"Jane Boorman",
       "POs":[{"Pono":2621, "Total":95},
              {"Pono":2626, "Total":218}
              ]}        

]

import json
import pandas as pd
df = pd.json_normalize(data,"POs","Emp").set_index(["Emp","Pono"])
# json normalize function, specify POs as the nested array to be flattened and
# Emp as the field to be used as part of the complext index in the resulting table.
# int the same line, set two columns as the index: Emp and Pono
print(df)


df=df.reset_index()
# drop the two column index of the dataframe to make Emp and Pono regular columns
# Convert the dataframe to a json
json_doc=(df.groupby(['Emp'], as_index=True)
          
          .apply(lambda x: x[['Pono', 'Total']].to_dict('records'))
          # apply a lambda function to each record in each group
          # in the lambda expression, specify the list of fields that you want to see in a
          # row of nested array associated with each Emp record.
          # use the dataframe.to_dict() method with the records parameter to format the fields
          # in the array as follows: [{column:value},...,{column:value}]
          # where each dictionary represents an order associated with a given employee
          .reset_index()
          .rename(columns={0:'POs'})
          .to_json(orient='records')
)
print(json_doc)

