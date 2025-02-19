n=5

for i in range(n):
    for j in range(n):
        if (i==n//2) | (j==n//2):   # for center row & column
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print()

'''
      *        
      *        
*  *  *  *  *  
      *        
      *        
'''

