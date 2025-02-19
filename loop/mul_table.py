#multiplication table - skip the 5th iteration

num=int(input("Enter the num:"))

for i in range(1,11):
    if i==5:
        continue
    print(num,"x",i,"=",num*i)
