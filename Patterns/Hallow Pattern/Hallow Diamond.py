n = 5

#upper part of diamond
for i in range(n - 1):
    for j in range(n - i):
        print("  ", end=" ")
    for j in range(i):
        if j == 0:          # for 1st column
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    for j in range(i + 1):
        if j == i:          # when column matches the row
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print()

#lower part of diamond
for i in range(n):
    for j in range(i + 1):
        print("  ", end=" ")
    for j in range(n - i):
        if j == 0:          # for 1st column
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    for j in range(i, n - 1):
        if j == n - 2:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print()