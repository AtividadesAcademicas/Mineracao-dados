import pandas as pd

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a', 'b', 'c'], index=['x', 'y', 'z'])

print(df.head())
print(df.columns)
print(df.index.to_list())

df.info()

print(df.describe())

#Retorna os valores unicos do data frame
print(df.nunique())

#Retorna os valores unicos de uma coluna do data frame
print(df['a'].unique())

print(df.shape)