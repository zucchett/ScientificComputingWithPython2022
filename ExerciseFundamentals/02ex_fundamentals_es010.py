"""
10.Class definition
Define a class polygon. The constructor has to take a tuple as input that contains the length of each side.
The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.
Create appropriate methods to get and set the length of each side
Create a method perimeter() that returns the perimeter of the polygon
Create a method getOrderedSides(increasing = True) that returns a tuple containing the length of the sides arranged in
increasing or decreasing order, depending on the argument of the method
Test the class by creating an instance and calling the perimeter() and getOrderedSides(increasing = True) methods.
"""


class Polygon:
    lengths = []

    def __init__(self, lengths):
        if len(lengths) > 2:
            self.lengths = lengths

    def getLengths(self):
        return self.lengths

    def getElement(self, index):
        if index < len(self.lengths):
            return self.lengths[index]

    def setLengths(self, index, element):
        if index < len(self.lengths):
            self.lengths[element] = element

    def perimeter(self):
        perimeter = 0
        for i in self.lengths:
            perimeter = perimeter + i
        return perimeter

    def getOrderedSides(self, increasing=True):
        OrderedList = self.lengths
        if increasing:
            OrderedList.sort()
        else:
            OrderedList.sort(reverse=True)
        return OrderedList


polygon = Polygon([5, 7, 1, 2, 0, 4, 3])
print("Polygon = ", polygon.lengths)
print("Perimeter of polygon = ", polygon.perimeter())
ordered_list = polygon.getOrderedSides()
print("Ordered list(increasing) = " + str(ordered_list))
ordered_list = polygon.getOrderedSides(increasing=False)
print("Ordered list(descending) = " + str(ordered_list))
