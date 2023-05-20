import pandas as pd
import json

data = [
    {"Emp": "Jeff Russell",
     "Emp_email": "Jeff.russell",
     "POs": [{"Pono": 2608, "Total": 35},
             {"Pono": 2617, "Total": 35},
             {"Pono": 2620, "Total": 139}]
     },
    {"Emp": "Jane Boorman",
     "Emp_email": "Jane.boorman",
     "POs": [{"Pono": 2621, "Total": 95},
             {"Pono": 2626, "Total": 218}]
     }
]

df = pd.json_normalize(data, "POs", ["Emp", "Emp_email"]).set_index(["Emp", "Emp_email", "Pono"])

# Convert the DataFrame to a nested dictionary with string keys
json_dict = {}
for index, row in df.iterrows():
    emp, emp_email, pono = index
    if emp not in json_dict:
        json_dict[emp] = {}
    if emp_email not in json_dict[emp]:
        json_dict[emp][emp_email] = {"POs": []}
    json_dict[emp][emp_email]["POs"].append(row.to_dict())

# Convert the resulting dictionary to a JSON string and write it to a file named "output.json"
with open('output.json', 'w') as f:
    json.dump(json_dict, f, indent=2)
