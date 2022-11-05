from Polygon import Polygon


class Rectangle(Polygon):

    # Since a rectangle has 4 equal sides, we just need the size of one side
    def __init__(self, sideLength):
        sides_lengths = [sideLength for _ in range(4)]
        super().__init__(sides_lengths)

    def area(self):
        return self.sides_lengths[0] ** 2


sideSize = 5
rectangle = Rectangle(sideSize)
print("The area of rectangle with side size of %d is: %2.d " % (sideSize, rectangle.area()))
