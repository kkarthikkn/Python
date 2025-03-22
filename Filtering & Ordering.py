import pandas as pd

df=pd.read_csv(r"D:\world_population.csv")

pd.set_option('display.max.columns',17)


print(df[df['Rank']<=20])
print("********************************************************************")

country_search=['Russia','Mexico']
print(df[df['Country'].isin(country_search)])
print("********************************************************************")

print(df[df['Country'].str.contains('United')])     # to return the values which contains the string declared
print(df[df['Country'].str.contains('Yemen')])
print("********************************************************************")

# axis=1 means it returns the values of the column(top-bottom). By default it is axis=1
# axis=0 means it returns the values of the rows(left-right)

df2=df.set_index('Country')     #index=row
print(df2)
print("********************************************************************")

print(df.filter(items=['Country'],axis=1))
print("********************************************************************")

print(df2.filter(items=['Continent','CCA3']))
print("********************************************************************")

print(df2.filter(items=['Yemen'],axis=0))
print("********************************************************************")

print(df2.filter(like='United',axis=0))
print("********************************************************************")

# loc & iloc
'''
loc[] ->  * label-based (row or column names)
          * includes the endpoint (ex: loc[0:4,3:7], includes 4th row & 7th column) 

iloc[] -> * position based (integer index)
          * excludes the endpoint (ex: iloc[0:4,5:7], includes till 3rd row & 6th column)

'''

# df.loc[rows,columns]
print(df.loc[1:4,['Country','Capital']])  # returns the data from row 1-4 and column "country & capital"
print("********************************************************************")

print(df2.loc['United States'])   # gives the data of the string which we are given)
print("********************************************************************")

print(df.loc[0:4])   # returns the data from 0-4th row
print(df.loc[5:7])
print(df.loc[8,'2022 Population'])    # returns the data from 8th row & '2022 population' column
print(df.loc[2:4,['Country','Continent']])    # returns the data from 2-4th row, 'country & continent' columns
print(df.loc[1:10,['Rank','2022 Population']])
print("********************************************************************")

print(df.iloc[0:4])  # returns the data from 0-3rd row
print(df.iloc[1:4,0:8])
print(df.iloc[2,7])   # returns the value in the position of  2nd row, 7th column
print(df.iloc[5:9,3:8])    # excludes 9th row, 7th column
print("********************************************************************")

print(df[df['Rank']<=10].sort_values(by='Rank',ascending=False))  # sort the values based on the given column based on asc or desc
print(df[df['Rank']<=10].sort_values(by='Rank',ascending=True))
print("********************************************************************")

print(df[df['Rank']<=10].sort_values(by=['Continent','Country'],ascending=[False,True]))   # first orders by 'Continent' in desc & 'Country' in asc
print("********************************************************************")

result=df[df['Rank']<=10].sort_values(by=['Continent','Country'],ascending=[False,True])
row_loc=result.loc[131,['Rank','Continent']]     # gives the data of 131 th row of 'rank & continent' column
print(row_loc)
print("********************************************************************")

result=df[df['Rank']<=10].sort_values(by=['Continent','Country'],ascending=[False,True])
row_iloc=result.iloc[1:4,2:7]     # returns data from 1-4th row (3 rows) & 2-7th col (5 col)
print(row_iloc)