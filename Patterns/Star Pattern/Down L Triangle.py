n=int(input("Enter num: "))

for i in range(n):
    for j in range(n-i):
        print("$  ",end="")
    print()