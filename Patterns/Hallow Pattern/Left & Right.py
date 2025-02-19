#know indexing before solving
#i ---> row
#j ---> column

n=4
for i in range(n):
    for j in range(n):
        if (j==0 or j==n-1): #left & right column.
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print()
'''
*        *  
*        *  
*        *  
*        *  
'''