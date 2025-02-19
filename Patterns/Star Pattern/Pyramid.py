n=5

for i in range(n):
    for j in range(n-i):
        print("  ",end="")
    for j in range(i+1):
        print("* ",end="")
    for j in range(i):      # coded 'range(i)' bcz if we have the range(i+1) we'll get two peak points @ top or we can
                            #   do vise_versa in above of this loop()
        print("* ",end="")

    print()