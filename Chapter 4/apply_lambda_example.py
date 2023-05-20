import pandas as pd

# Create a DataFrame object
df = pd.DataFrame({
    "Name": ["John", "Mary", "Peter"],
    "Age": [30, 25, 35]
})

# Apply a lambda function to the "Age" column
df["Age squared"] = df["Age"].apply(lambda x: x ** 2)

print(df)
# Output:
#     Name  Age  Age squared
# 0   John   30         900
# 1   Mary   25         625
# 2  Peter   35        1225

# Apply a lambda function to each row of the DataFrame
df["Sum"] = df.apply(lambda row: row["Age"] + len(row["Name"]), axis=1)

print(df)
# Output:
#     Name  Age  Age squared  Sum
# 0   John   30         900   34
# 1   Mary   25         625   29
# 2  Peter   35        1225   40


import pandas as pd

# Create a DataFrame object
df = pd.DataFrame({
    "Pono": [1, 2, 3],
    "Total": [10, 20, 30],
    "Extra": [100, 200, 300]
})

# Apply a lambda function to select only "Pono" and "Total" columns
df2 = df.apply(lambda x: x[['Pono', 'Total']], axis=1)

print(df2)
# Output:
#    Pono  Total
# 0     1     10
# 1     2     20
# 2     3     30
