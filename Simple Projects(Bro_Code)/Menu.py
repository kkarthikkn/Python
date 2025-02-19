menus = {"popcorn": "10.53",
         "pizza": "15.35",
         "soda": "20.7",
         "lemonade": "5.89",
         "nachos": "3.15"}
cart = []
total = 0

print("----- MENU -----")
for key, value in menus.items():
    print(f"{key:9}: ${value}")

print()
while True:
    food = input("enter the food (q-quit): ")
    if food.lower() == 'q':
        break
    elif menus.get(food) is not None:
        cart.append(food)

print()
print("----- Your Cart -----")
for cart_items in cart:
    print(cart_items)
print("---------------------")
for food_items in cart:
    total += float(menus.get(food_items))  #.get() ---> used to reterive the values of the dictionary using keys
#print()
print(f"Total amount: ${total:.2f}")
print("---------------------")
