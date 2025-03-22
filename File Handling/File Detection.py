import os

file=r"C:\Users\karth\OneDrive\Desktop\file_detection.txt"
dir_file=r"C:\Users\karth\OneDrive\Desktop"

if os.path.exists(dir_file):
    print("Exists ✅")

    if os.path.isfile(dir_file):
        print("This is file")
    elif os.path.isdir(dir_file):
        print("This is Directory")
else:
    print("Not Exists ❌")

print("---------------------")

if os.path.exists(file):
    print("Exists ✅")

    if os.path.isfile(file):    # to check whether file or not
        print("This is File")
    elif os.path.isdir(file):   # to check whether directory or not
        print("This is Directory")
else:
    print("Not Exist ❌")
