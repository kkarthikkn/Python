import json

employees= {"name":"Bob",
            "age":35,
            "position":"Manager"}
path=r"C:\Users\karth\OneDrive\Desktop\emp_output_json.json"

# writing file
with open(path,"w") as file:
    json.dump(employees,file,indent=5)
    print("json File created")

# appending
with open(path,"a") as file:
    json.dump(employees,file,indent=5)
    print("Appended successfully")

# Exclusive creation
try:
    with open(path,"x") as file:
        file.write(employees+"\n")
        print("File Created")
except FileExistsError:     # this will rise an error,therefore using exception
    print("Already Exist")