""" Common File Modes:
    'w': Write mode (overwrites the file if it exists).
    'a': Append mode (adds to the end of the file).
    'x': Exclusive creation (creates a new file, raises an error if the file already exists).
    'r': Read mode (default).
    'wb': Write mode for binary files.
"""
'''
    * relative_file_path = "mydata.txt"
    * absolute_file_path = "c:/home/user/projects/data/mydata.txt"
'''


employees=['Alice','Bob','Tom','George']
path=r"C:\Users\karth\OneDrive\Desktop\emp_output.txt"

# writing file
with open(path,"w") as file:
    for emp in employees:
        file.write(emp+"\n")
    print("File created")

# appending
with open(path,"a") as file:
    file.write(emp+"\n")
    print("Appended successfully")

# Exclusive creation
try:
    with open(path,"x") as file:
        file.write(emp+"\n")
        print("File Created")
except FileExistsError:     # this will rise an error,therefore using exception
    print("Already Exist")