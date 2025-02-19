n = 6

for i in range(n):
    p = 1
    for j in range(i):
        print(" ", end=" ")
    for j in range(n - i):
        print(p, end=" ")
        p += 1

    for j in range(n - i):
        p -= 1
        print(p, end=" ")

    print()