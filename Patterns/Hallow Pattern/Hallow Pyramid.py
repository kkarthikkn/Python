n = 5

for i in range(n):
    for j in range(n - i):
        print("  ", end=" ")
    for j in range(i):
        if (i == n - 1 or j == 0):      # i==n-1 ---> for last row
                                        # j==0 ---> for 1st column
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    for j in range(i + 1):
        if (i == n - 1 or j == i):      # i==n-1 ---> for last column.
                                        # j==i ---> for match the row index & column index
            print("* ", end=" ")
        else:
            print("  ", end=" ")

    print()
'''
               *  
            *     *  
         *           *  
      *                 *  
   *  *  *  *  *  *  *  *  *  
'''