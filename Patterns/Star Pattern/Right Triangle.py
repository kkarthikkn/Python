n=int(input("enter num: "))

for i in range(n):
    for j in range(n-i):
        print("   ",end="")
    for k in range(i+1):
        print("*  ",end="")
    print()



#                *
#             *  *
#          *  *  *
#       *  *  *  *
#    *  *  *  *  *