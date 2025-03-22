class Rectangle:
    def __init__(self,width,height):
        self._width=width       # ' _ ' indicates that width & height are protected.
                                # These attributes are accessible only inside the class
        self._height=height

    @property
    def width(self):
        return f"Width: {self._width:.1f} cm"       # accessed like attribute,
                                                    # bcz attribute 'width & height' are accessible inside the class

    @property
    def height(self):
        return f"Height: {self._height:.1f} cm"


    @width.setter           # setter ->allows to set the value of a protected or private attribute.
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width should be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height should be greater than 0")

    @width.deleter      # deletes the attribute & its value from the object
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")

    def area(self):
        return self._width * self._height

r1=Rectangle(4,10)

r1.height=5         # sets the new width & height.
r1.width = 10       # If the value is -ve it takes the previous value of the attribute(not updated)

print(r1.width)         # now we can access it indirectly
print(r1.height)

#  print(r1._width)        # Not Recommended (bcz its raw data), it is protected (only accessible inside the class)
#  print(r1._height)

print(f"Area of Rectangle: {r1.area()} cm^2")
print("--------------------------")
del r1.width
del r1.height

print(r1.height)  # it will raise an error bcz the width attribute has been deleted


# getter  -> to get the public/protected/private values
# setter  -> both public and protected/private attributes can be updated with new values
# deleter -> both public and protected/private attributes can be deleted