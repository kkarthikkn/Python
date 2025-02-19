n=5
for i in range(n):
    p=1                     # initialize p=5 for pattern_2
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print(p,end=" ")
        p+=1                # decr p-=1 for pattern_2
    for j in range(i+1):
        print(p,end=" ")
        p-=1                # incr p+=1 for pattern_2
    print()

'''   
          1 
        1 2 1 
      1 2 3 2 1 
    1 2 3 4 3 2 1 
  1 2 3 4 5 4 3 2 1 
'''

''' Pattern_2
          5 
        5 4 5 
      5 4 3 4 5 
    5 4 3 2 3 4 5 
  5 4 3 2 1 2 3 4 5 
'''