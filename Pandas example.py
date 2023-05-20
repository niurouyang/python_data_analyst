import pandas as pd
# use pandas series to create a dataframe
data = ['Niurou', 'Matthew', 'Emily']
data1=['46','10','12']
data2=['Male','Male','Female']
names = pd.Series(data)
names.name='Names'
ages= pd.Series(data1, name='Age')
gender=pd.Series(data2, name='Gender')

# pd.concat will concatenate(link) names, ages, gender together
# axis 0 row, 1 column
df=pd.concat([names,ages,gender],axis=1)

# df.set_index()
print(df)

