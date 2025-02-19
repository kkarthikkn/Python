n = 5

for i in range(n):
    for j in range(n - i):
        print("  ", end="")

    for j in range(i + 1):
        if (i % 2 == 0):
            print("A ", end="")
        else:
            print("B ", end="")

    for j in range(i):
        if (i % 2 == 0):
            print("A ", end="")
        else:
            print("B ", end="")

    print()