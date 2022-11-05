# 11. Class inheritance
# Define a class `rectangle` that inherits from `polygon`. Modify the constructor, 
# if necessary, to make sure that the input data is consistent with the 
# geometrical properties of a rectangle.
# - Create a method `area()` that returns the area of the rectangle.
# Test the `rectangle` class by creating an instance and passing an appropriate 
# input to the constructor.

class Polygon:
    lengths = []

    def __init__(self, lengths):
        if len(lengths) > 2:
            self.lengths = lengths
        else:
            print("Component size should be greater than 2!")

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

    def getOrderedSides(self, increasing = True):
        ordered_list = self.lengths
        if increasing:
            ordered_list.sort()
        else:
            ordered_list.sort(reverse=True)
        return ordered_list

class Rectangle(Polygon):
    def __init__(self, lengths):
        if len(lengths) == 4:      
            lengths.sort()
            if (lengths[0] == lengths[1]) and (lengths[2] == lengths[3]):
                self.lengths = lengths
            else:
                print("Dimesions are not correct!")
        else:
            print("Component size should be 4!")

    def area(self):
        return self.lengths[0] * self.lengths[2]
        #in init function, the list is assigned sorted

rectangle = Rectangle([3,1,3,1])
print("Area = ", rectangle.area())