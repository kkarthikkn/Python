n = 5
for i in range(n):
    for j in range(i + 1):
        print("  ", end="")
    for j in range(n - i):
        print("$ ", end="")

    for j in range(n - i - 1):  #  -1 to remove one column from pyramid, otherwise the end od the pyramid
                                #    will have two ends
        print("$ ", end="")
    print()