n=5

for i in range(n):
    for j in range(n):
        if (i==j or i+j==n-1):  #Know indexing before solving
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print()
'''
*           *  
   *     *     
      *        
   *     *     
*           *  
'''