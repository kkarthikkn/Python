food = []
price = []
total = 0

while True:
    fd = input("Enter the food item or (q-quit): ")
    if fd.lower() == "q":       # if the input is 'Q' it converts into 'q' & matches the condition.
        break
    else:
        prc = float(input(f"Enter the price of {fd}: $"))
        food.append(fd)
        price.append(prc)

print()
print("--- Your Cart Details ---")
for i in range(len(food)):
    print(f"{food[i]} : ${price[i]:.2f}")

print()
total = sum(price)
print(f"Total amount: ${total:.2f}")



