import math
n=int(input("Enter num rows: "))            # for no. of rows
p=int(input("Enter outer num of the pattern: "))     # for the outer number

for i in range(n):
    for j in range(n):
        minimum = p - min(min(i,j),min(n-i-1,n-j-1))  #subtracts 'p' from minimum from top,bottom,left,right
        print(minimum,end="  ")
    print()

'''
4  4  4  4  4  4  4  
4  3  3  3  3  3  4  
4  3  2  2  2  3  4  
4  3  2  1  2  3  4  
4  3  2  2  2  3  4  
4  3  3  3  3  3  4  
4  4  4  4  4  4  4  
'''