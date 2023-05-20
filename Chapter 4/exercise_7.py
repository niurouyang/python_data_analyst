data=[{"Emp":"Jeff Russell",
       "Emp_email":"Jeff.russell",
       "POs":[{"Pono":2608, "Total":35},
              {"Pono":2617, "Total":35},
              {"Pono":2620, "Total":139}
       ]},
      {"Emp":"Jane Boorman",
        "Emp_email":"Jane.boorman",
        "POs":[{"Pono":2621, "Total":95},
               {"Pono":2626, "Total":218}
        ]}
]

import pandas as pd
import json

df=pd.json_normalize(data, "POs",["Emp","Emp_email"]).set_index(["Emp","Emp_email","Pono"])
# "POs" argument is a string that specifies the key you want to normallize
# ["Emp","Emp_email"] is a list of strings that specifies the keys you want to include 
# as additional columns in the dataframe.
print(df)

df=df.reset_index()

json_rev=(df.groupby(['Emp','Emp_email'], as_index=True)
            .apply(lambda x:x[['Pono','Total']].to_dict('records'))
            .reset_index()
            .rename(columns={0:'POs'})
            .to_json(orient="records", indent=2)
          
          )

print(json_rev)