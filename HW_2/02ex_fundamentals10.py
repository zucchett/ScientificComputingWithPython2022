import math


class Polygon:
    inp = []

    def __init__(self, sides, increasing):
        self.inp = sides
        self.increasing = increasing

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


Test01 = Polygon([10, 35, 20, 40], True)
print("The number of sides are :", Test01.get_sides())
print("The perimeter of the polygon is :", Test01.get_perimeter())
print("The ordered sides are :", Test01.get_Ordered_Sides())
