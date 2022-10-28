# 11. Class inheritance

# Define a class rectangle that inherits from polygon.
# Modify the constructor, if necessary, to make sure that
# the input data is consistent with the geometrical properties of a rectangle.

# Create a method area() that returns the area of the rectangle.
# Test the rectangle class by creating an instance and passing
# an appropriate input to the constructor.

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
                print(str(i+1) + "-th side added!")
            print("Polygon created!")
 
    # Definition of the destructor, but it is often omitted
    def __del__(self):
        print("Exercise done!")
    
    # Definition of the methods
    
    # This method allows to get the length of each side
    def getSideN(self, n): # the first argument is always 'self' for the methods of a class
        return self.sides[n-1]
    
    # This method allows to set the length of each side
    def setSideN(self, n_length, n): # n is the component index, and xi is the value
        if n <= len(self.sides):
            self.sides[n-1] = n_length
    
    def perimeter(self):
        sum = 0
        for s in self.sides:
            sum += s
        return sum

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

class Rectangle(Polygon): # class 'Rectangle' inherits from class 'Polygon'

    # The constructor here is optional, and can be inherited from the parent class if omitted
    def __init__(self, two_sides):
        if len(two_sides) == 2:
            for i in range(len(two_sides)):
                self.sides.append(two_sides[i]) # a tuple is expected as input
        else:
            print("Error: number of sides is not 2, so it is not a rectangle!")
    
    # New methods that only belong to the child class
    def area(self):
        return self.sides[0]*self.sides[1]

    def perimeter(self):
        sum = 0
        for s in self.sides:
            sum += s
        return sum*2


r = Rectangle((6,7))



print("The area of the rectangle is " + str(r.area()))

r.setSideN(4,1)

print("After changing the dimension of the 1-nd side now the sides (with decreasing order) are: " + str(r.getOrderedSides(increasing='False')))

print("The ordered sides are " + str(r.getOrderedSides()))

print("Perimeter is: " + str(r.perimeter()))