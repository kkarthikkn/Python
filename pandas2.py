import pandas as pd
import numpy as np

data="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df=pd.read_csv(data,header=None)
print("Last 5 rows:\n",df.head(5))
print("Last 5 rows:\n",df.tail(5))
df.describe(include="all")

print(df.columns)   # retrieves col-names

print(df.dtypes)   # retrieves the data types of col

df[[2,5,6]].describe()      # describes only the given columns
                            # (in this case numbers indicates col's bcz of no header is provided) otherwise col-name can be given within the ''

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)
df.columns = headers    # replace headers with new col-name
df.columns

df1=df.replace('?',np.nan)  # replace '?' with NaN(null) values      #

path=r"D:\ml_data.csv"
df.to_csv(path)     # to save the data_set