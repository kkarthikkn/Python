#Last element will be same in decrement.
n=5
k=5

for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(k):
        print(k-j,end=" ")
    k-=1
    print()

''' output
5 4 3 2 1 
  4 3 2 1
    3 2 1 
      2 1
        1
'''