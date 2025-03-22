
import csv

data=[["name","age","job"],
      ["Alice",28,"Manager"],
      ["Sandy",30,"Developer"],
      ["Bob",35,"CEO"],
      ["Tom",23,"Chef"]]
path=r"C:\Users\karth\OneDrive\Desktop\csv_Output.csv"

try:
    with open(path,"x",newline="") as file:
        writer=csv.writer(file)
        for i in data:
            writer.writerow(i)
        print("CSV file created")
except PermissionError as e:
    print(f"Permission Error: {e}")
except FileExistsError:
    print("File already exist")