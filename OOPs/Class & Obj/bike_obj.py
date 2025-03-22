from bike_import import Bike  #'bike_import' is created module

bk1=Bike("Yamaha","FZ-X",150,155000,"Black")
bk2=Bike("RE","Classic 350",180,235000,"Silver")

#bk.color="Blue"

print(bk1.brand)
print(bk1.model)
print(bk1.top_speed)
print(bk1.price)
print(bk1.color)
print()
print(bk2.brand)
print(bk2.model)
print(bk2.top_speed)
print(bk2.price)
print(bk2.color)

print()
bk2.drive()
bk1.stop()
print()
bk2.describe()

if __name__=="__main__":
    print("\n",__name__)