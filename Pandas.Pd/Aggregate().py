import pandas as pd

df = pd.read_csv(r"D:\Smpl Data Pd\Flavors.csv")
print(df)

df.agg({'Flavor Rating':['min','max','count','sum','mean'],'Texture Rating':['min','max','count','sum','mean']})

df.sort_values(by=['Base Flavor','Flavor'],ascending=[True,True])


grp_frame = df.groupby('Base Flavor')
print(grp_frame.mean(numeric_only=True))  # use numeric_only to perform mean, otherwise it will rise an error (bcz it also considers non-numeric values)

# alternate way (by giving col names)
print(grp_frame.mean(['Flavor Rating','Texture Rating','Total Rating']))

df.groupby('Base Flavor').count()

# based on the first col it perform min-max functions

df.groupby('Base Flavor').min() # in 'Flavor' col it returned the data using min by the alphabets

df.groupby('Base Flavor').max()  # in 'Flavor' col it returned the data using max by the alphabets

df.groupby('Base Flavor').sum(numeric_only=True)  # set numeric_only to True, otherwise it'll adds the non-numeric values

# performs aggregation on the given col with the given agg functions
df.groupby('Base Flavor').agg({'Flavor Rating':['min','max','count','sum','mean']})

# group by on multiple columns

df.groupby('Base Flavor').agg({'Flavor Rating':['min','max','count','sum','mean','std'],'Texture Rating':['min','max','count','sum','mean','std']})

df.groupby(['Base Flavor','Liked']).mean(numeric_only=True).round(2)

df.groupby(['Base Flavor','Liked']).describe()

df.groupby(['Base Flavor','Liked']).agg({'Flavor Rating':['min','max','mean','std','count']})
