#factorial using while loop

num=int(input("enter no: "))
original_num = num    #to print the num, otherwise it will print '0' due to decrement of num.
fact=1

while num>0:
    fact*=num
    num-=1

print(f"factorial no of {original_num} is: {fact}")


#for_loop -----------------------------
n = int(input("enter no:"))
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)

