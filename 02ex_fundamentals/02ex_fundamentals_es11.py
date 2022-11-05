"""
11. Class inheritance继承
Define a class rectangle that inherits from polygon. Modify the constructor, if necessary,
to make sure that the input data is consistent with the geometrical properties of a rectangle.
Create a method area() that returns the area of the rectangle.
Test the rectangle class by creating an instance and passing an appropriate input to the constructor.
"""


class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


shape = Rectangle(5, 6)
print(shape.area())
