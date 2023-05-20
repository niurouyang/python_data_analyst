import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}, index=['X', 'Y', 'Z'])

print(df)
# Select a single value by label
value = df.loc['X', 'A']

print(value)
# Output: 1

# Select a row by label
row = df.loc['Y']

print(row)
# Output:
# A    2
# B    5
# C    8
# Name: Y, dtype: int64

# Select multiple rows and columns by label
slice_df = df.loc['X':'Y', 'A':'B']

print(slice_df)
# Output:
#    A  B
# X  1  4
# Y  2  5
