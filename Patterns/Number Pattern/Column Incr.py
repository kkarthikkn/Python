n = 6

for i in range(n):
    p = 1
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(i + 1):
        print(p, end=" ")
        p += 1

    print()

'''
            1 
          1 2 
        1 2 3 
      1 2 3 4 
    1 2 3 4 5 
  1 2 3 4 5 6 
'''
