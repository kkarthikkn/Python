import pandas as pd

# csv file
df=pd.read_csv(r"D:\Sample Datas\iris.csv",names=["Sepal_len","Sepal_wid","Petal_len","PetaL_Wid","Species"])
print(df)
print("********************************************************************")

df=pd.read_csv(r"D:\countries of the world.txt",sep="\t")  # use 'sep' for separate
print(df)
print("********************************************************************")

# txt file

# pd.set_option('display.max.rows',228) -> displays all the rows
df3=pd.read_table(r"D:\countries of the world.txt")
print(df3)
print("********************************************************************")

# excel file

df4=pd.read_excel(r"D:\world_population_excel_workbook.xlsx")
print(df4)
print("********************************************************************")

# json file
# pd.set_option('display.max.columns',38)
df5=pd.read_json(r"D:\json_sample.json")
print(df5)
print("********************************************************************")


# to display all rows & columns use 'set_option'
# NOTE: first execute set_option() & again run the 'df' to display all the data

pd.set_option('display.max.rows',225)  # 255 -> its example, give number of rows in that parameter
pd.set_option('display.max.columns',38) # Similar for columns

# to retrieve the data from specific column
print(df3['Region'])
print("********************************************************************")

# to retrieve the data from the index(row)
print(df3.loc[226])      # data of 50th row from df3
print("********************************************************************")
