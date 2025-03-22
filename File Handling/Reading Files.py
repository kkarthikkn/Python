# try it with other file extension(.txt, .json, .csv)

txt_path=r"C:\Users\karth\OneDrive\Desktop\emp_output.txt"
json_path=r"C:\Users\karth\OneDrive\Desktop\emp_output_json.json"
csv_path=r"C:\Users\karth\OneDrive\Desktop\csv_Output.csv"

try:
    with open(csv_path,"r") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("File not found")