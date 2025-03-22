class Shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled

    def describe(self):
        print(f"It is {self.color} & {'filled' if self.is_filled else 'not filled'} ")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius

    def describe(self):
        super().describe()      # now it is able to access the parent class, using super()
        print(f"It is circle & it's area is {3.14*self.radius*self.radius}cm^2")  # it overrides the parent class method if child class method(bcz of same method name)

class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width=width

    def describe(self):
        super().describe()
        print(f"It is square & it's area is {self.width*self.width}cm^2")

class Triangle(Shape):
    def __init__(self,color,is_filled,height,width):
        super().__init__(color,is_filled)
        self.height=height
        self.width=width

    def describe(self):
        super().describe()
        print(f"It is triangle & it's area is {self.width*self.height/2}cm^2")

c1=Circle("Blue","True",5)
s1=Square("Black",False,10)
t1=Triangle("Green",True,3,9)

print(c1.color)
print(c1.is_filled)
print(f"Radius:{c1.radius}cm")
c1.describe()
print("----------------------")
print(s1.color)
print(s1.is_filled)
print(f"Width:{s1.width}cm")
s1.describe()
print("----------------------")
print(t1.color)
print(t1.is_filled)
print(f"Height:{t1.height}cm")
print(f"Width:{t1.width}cm")
t1.describe()

# __init__ method : Always use __init__ method to initialize attributes.
# super(): Use super().__init__() to call the parent class constructor when inheriting from another class.