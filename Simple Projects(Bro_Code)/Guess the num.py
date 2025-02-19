import random
ran=random.randint(1,6)
attempt=0
guess=int(input("Enter the number(1-6): "))

while guess!=ran:
    attempt+=1
    print(f"It's {ran}.Try Again")
    guess=int(input("enter the num: "))

print()
print(f"{ran} is correct guess!")
if attempt==0:
    print(f"You took 0 attempt to guess correct answer.")
else:
    print(f"You took {attempt} attempts to guess correct answer.")