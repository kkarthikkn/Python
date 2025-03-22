# execute in jupy-notebook
import pandas as pd

df=pd.read_csv(r"D:\countries of the world.csv")

print(df.head(5))     # it shows the first '5' rows of the dataset(we can modify the num according to the need)
print()
print(df.tail(5))     # it retrieves the last '5' rows of the dataset

# refer the stats below for describe()
print(df.describe())      # by default only works for numerical columns.
                          # generate descriptive statistics of a DataFrame, information like count,min,max ....

df.describe(include='all')    # it includes all the columns(numeric & categorical) in the dataset with the new attributes like unique,top,freq

df.info()          # gives info about the dataset like no of rows & columns, column names, non-null values, datatypes...

print(df.shape)     # gives the dimensions(Rows * columns)

path=r"D:\car_dataset_india1.csv"
df.to_csv(path)    # to save the file

print(df.columns)   # retrieves col-names




''' pd.describe() :-

count: The number of non-null entries.
unique: The number of unique values in the column.
top: The most frequent value (the mode).
freq: The frequency of the most common value.
mean: The average of the values.
std: The standard deviation, which measures the spread of the data.
min: The smallest value in the column.
25%: The 25th percentile (Q1).
50%: The 50th percentile (Q2), also known as the median.
75%: The 75th percentile (Q3).
max: The largest value in the column.
'''