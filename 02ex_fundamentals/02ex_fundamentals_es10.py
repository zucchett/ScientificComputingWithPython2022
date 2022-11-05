"""
10. Class definition
Define a class polygon. The constructor has to take a tuple as input that contains the length of each side.
The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.
Create appropriate methods to get and set the length of each side
Create a method perimeter() that returns the perimeter of the polygon
Create a method getOrderedSides(increasing = True) that returns a tuple containing the length of the sides arranged in
increasing or decreasing order, depending on the argument of the method
Test the class by creating an instance and calling the perimeter() and getOrderedSides(increasing = True) methods
"""


class polygon:
    def __init__(self, list):
        self.list = list
        self.lene = len(list)
        if self.lene < 3:
            print("enter more than 3")
            return

    def perimeter(self):
        perimeter = sum(self.list)
        # print("first solv: ",self.list[0] * self.lene)
        print("sum: ", perimeter)

    def getOrderedSides(self, increasing=True):
        print(sorted(self.list))


x = polygon((3, 6, 7, 1))
x.perimeter()
x.getOrderedSides()

