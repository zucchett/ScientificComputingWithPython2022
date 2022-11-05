# 10. Class definition

# Define a class polygon. The constructor has to take
# a tuple as input that contains the length of each side.
# The (unordered) input list does not have to have a fixed
#  length, but should contain at least 3 items.

# Create appropriate methods to get and set the length of each side
# Create a method perimeter() that returns the perimeter of the polygon
# Create a method getOrderedSides(increasing = True) that returns a tuple
# containing the length of the sides arranged in increasing or decreasing order,
# depending on the argument of the method
# Test the class by creating an instance and calling the perimeter()
# and getOrderedSides(increasing = True) methods.

import math

class Polygon:
    '''This is a comment that is supposed to describe the purpose of the class'''
    
    # Definition of the class attributes, which are common for all instances of the same class
    sides = [] 
    
    # Definition of the Constructor, a special method that is called every time a new object is created
    # The first argument of the constructor (and also for all other methods in the class) is the instance itself
    def __init__(self, tuple_sides):
        if len(tuple_sides) < 3:
            print("It is not a polygon! We need at least 3 sides!")
        else:
            for i in range(len(tuple_sides)):
                self.sides.append(tuple_sides[i])
            print("Polygon created!")
 
    # Definition of the destructor
    def __del__(self):
        print("Goodbye, exercise done!")
    
    # Definition of the methods
    
    # This method allows to get the length of each side
    def getSideN(self, n): # the first argument is always 'self' for the methods of a class
        return self.sides[n-1]
    
    # This method allows to set the length of each side
    def setSideN(self, n_length, n): # n is the component index, and xi is the value
        if n <= len(self.sides):
            self.sides[n-1] = n_length

    # This method allows to compute the perimeter of the Polygon    
    def perimeter(self):
        sum = 0
        for s in self.sides:
            sum += s
        return sum

    # This method returns the sides of the Polygon ordered (with increasing or decreasing policy)
    def getOrderedSides(self, increasing = True):
        if increasing == True:
            p_copy = [i for i in self.sides]
            p_copy.sort()
            tuple_poly = tuple(p_copy)
            return tuple_poly
        else:
            p_copy = [i for i in self.sides]
            p_copy.sort(reverse=True)
            return tuple(p_copy)

# End of the class definition

p = Polygon((5,4,2))

print("The dimension of the 2-nd side is ", str(p.getSideN(2)))

print("Perimeter is: " + str(p.perimeter()))

p.setSideN(6,3)

print("After changing the dimension of the 3-rd side now the sides (with decreasing order) are: " + str(p.getOrderedSides(increasing='False')))

p.setSideN(9,1)

print("After changing the dimension of the 1-st side now the sides (with increasing order) are: " + str(p.getOrderedSides()))

