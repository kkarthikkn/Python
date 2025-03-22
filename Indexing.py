import pandas as pd

df=pd.read_csv(r"D:\world_population.csv")
print(df)

df=pd.read_csv(r"D:\world_population.csv",index_col='Country')   # creates new index with the col 'Country'
print(df)

# 'inplace=True' Updates/modifies the dataset
df.reset_index(inplace=True)   # reset the index to normal dataset
print(df)

df.set_index('Country')  # it wont save the index
print(df)

df.set_index('Country',inplace=True)  # it will save the index
print(df)

print(df.loc['Albania'])

print(df.iloc[1])

df.reset_index(inplace=True)
print(df)

df.set_index(['Continent','Country'],inplace=True)

df.sort_index()

pd.set_option('display.max.rows',234)
print(df)

pd.reset_option('display.max.rows')
print(df)

# df.reset_index()
#
# df.set_index(['Continent','Country'],inplace=True)

pd.set_option('display.max.rows',235)
print(df)

df.sort_index(ascending=[False,True])  # sorts based on Continent first & Country later
                                       # { change the values of ascending to view different kinds of sorting }

print(df.loc['South America','Chile'])

print(df.iloc[1])    # indexing wont work in iloc
