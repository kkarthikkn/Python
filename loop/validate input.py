#input should be within 1-10

num = int(input("enter no: "))

#------ while Loop--------
while True:
    if 1<= num <=10:
        print(f"Num Validated by 'while' loop")
        break
    else:
        print(input("enter number within 1-10: "))
        break


#------ for Loop--------
for i in range(0,num):  #or -----for i in range(1):
    if 1<=num<=10:
        print("Num Validated by 'for' loop")
        break
    else:
        print(input("NOt Validated: "))
        break