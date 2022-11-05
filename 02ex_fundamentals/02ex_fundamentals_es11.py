class Rectangle():
    def _init_(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


shape = Rectangle(5, 6)
print(shape.area())