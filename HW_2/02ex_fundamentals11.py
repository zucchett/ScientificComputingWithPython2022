import math


class Polygon:
    inp = []

    def __init__(self, sides, increasing):
        self.inp = sides
        self.increasing = increasing
        self.sides_length = None

    def get_sides(self):  # returns the no. of sides of the polygon
        return len(self.inp)

    def get_perimeter(self):
        return sum(self.inp)

    def get_Ordered_Sides(self):
        if self.increasing:
            inc = self.inp
            inc.sort()
            print("Arranged in Increasing order.")
            return inc
        else:
            decreasing = self.inp
            decreasing.sort(reverse=True)
            print("Arranged in Decreasing order.")
        return decreasing


Test01 = Polygon([10, 15, 7, 33], True)
print("The number of sides are :", Test01.get_sides())
print("The perimeter of the polygon is :", Test01.get_perimeter())
print("The ordered sides are :", Test01.get_Ordered_Sides())


class Rectangle(Polygon):
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def __str__(self):
        return "working"

    def area(self):
        return self.length * self.breadth


r = Rectangle(2, 3)
print("The area of the rectangle is: ", r.area())
