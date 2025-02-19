n = 5
for i in range(n):
    for j in range(i + 1):
        if (j == 0 or i == n - 1 or i == j):  # j==0  ---> for 1st column
                                              # i==n-1  ---> for last row
                                              # i==j  ---> when row index matches colum index

            print("* ", end=" ")
        else:
            print("  ", end=" ")

    print()
'''
*  
*  *  
*     *  
*        *  
*  *  *  *  *  
'''