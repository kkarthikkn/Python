n=int(input("Enter num: "))

for i in range(1,n+1):      # or -----  for i in range(1,n+1):
    for j in range(i):      # or -----  for j in range(i+1):
        print("*  ",end="")
    print()