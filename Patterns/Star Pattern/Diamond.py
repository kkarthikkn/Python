#pyramid = upper pyramid + lower pyramid
n = 4

#upper pyramid
for i in range(n - 1):   # (n-1) bcz there will be another line after upper pyramid. So it won't look like diamond
    for j in range(n - i):
        print("  ", end="")
    for j in range(i + 1):
        print("* ", end="")
    for j in range(i):
        print("* ", end="")
    print()

#lower pyramid
for i in range(n):      # (n-1) won't work here bcz it will reduce one line from the bottom
    for j in range(i + 1):
        print("  ", end="")
    for j in range(n - i):
        print("* ", end="")
    for j in range(n - i - 1):
        print("* ", end="")

    print()