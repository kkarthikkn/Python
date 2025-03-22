import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(r"D:\Smpl Data Pd\world_population.csv")
df

pd.set_option('display.float_format', lambda x: '%.2f' % x)
df

df.info()
df.describe()

df.isnull().sum()  # checks for the null values

df.nunique()  # gives the unique values

df.sort_values(by='2022 Population', ascending=False).head(10)

df['Continent'].unique()  # returns the col values which are unique

df['Country'].unique()

df.corr(numeric_only=True)

# Heatmap
# correlation using heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True)   # annot=True: displays the correlation values inside the heatmap cells
plt.rcParams['figure.figsize']=(30,14)
plt.rcParams['font.size']=(28)
plt.show()

df.groupby('Continent').mean(numeric_only=True).sort_values(by='2022 Population', ascending=False)

df[df['Continent'].str.contains('Oceania')]

df.columns # returns the total col in the  dataset

# df2=df.groupby('Continent')[['1970 Population', '1980 Population', '1990 Population',
#        '2000 Population', '2010 Population', '2015 Population',
#        '2020 Population','2022 Population']].mean().sort_values(by="2022 Population", ascending=False)

# another way by giving the index values
# note: '[::-1]' for reversing the index as the year col will be in desc, so it converts into asc
df2=df.groupby('Continent')[df.columns[5:13][::-1]].mean(numeric_only=True).sort_values(by='2022 Population', ascending=False)
df2.plot()

print(df2)

df3=df2.transpose()  # flip the rows and columns of a DataFrame
df3

# Line Chart

# plt.rcParams['figure.figsize']=(20,14)  ---> another way of defining figsize & font size
# plt.rcParams['font.size']=(15)

df3.plot(figsize=(20,14),fontsize=(15))

# Box Plot
df.boxplot(figsize=(20,10),fontsize=(10))

# returns the data of selected dtype like object,float,number.....
df.select_dtypes(include='object')

# Pie
ax=df2.plot(y='2022 Population', kind='pie', figsize=(8,4),legend=False, fontsize=10)
ax.set_ylabel('')
plt.show()