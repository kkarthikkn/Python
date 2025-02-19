n = 4
p = 1

for i in range(n):
    for j in range(n - i):
        print(" ", end="  ")

    for j in range(i + 1):
        print(p, end="  ")

    for j in range(i):
        print(p, end="  ")
    p += 1
    print()

for i in range(n):
    for j in range(i + 1):
        print(" ", end="  ")

    for j in range(n - i - 1):
        print(p, end="  ")

    for j in range(n - i):
        print(p, end="  ")

    p += 1  # also decrement for another pattern.Try it (p-=1).
    print()

''' Output:
            1  
         2  2  2  
      3  3  3  3  3  
   4  4  4  4  4  4  4  
   5  5  5  5  5  5  5  
      6  6  6  6  6  
         7  7  7  
            8  
'''