#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 19:02:55 2022

@author: alessandra
"""

#%%es11
# Define a class rectangle that inherits from polygon. Modify the constructor,
# if necessary, to make sure that the input data is consistent with the
# geometrical properties of a rectangle.

# Create a method area() that returns the area of the rectangle.
# Test the rectangle class by creating an instance and passing an appropriate
# input to the constructor.

class Polygon:
    """This class takes a tuple as input that contains the
    length of each side of the polygon and calculates the
    perimeter and returns a tuple containing the length of
    the sides arranged in increasing or decreasing order"""
    
    def __init__(self):
        self.n = int(input("Type the number of sides: "))
        self.sides = [0 for i in range(self.n)]
        if self.n < 3:
            raise ValueError("Error: this is not a polygon")
        else:
            pass
    
    def inputSides(self):
        self.sides = tuple(float(input("Enter side "+str(i+1)+" and press <Enter>: ")) for i in range(self.n))
        for j in range(self.n):
            if self.sides[j] == 0:
                raise ValueError("Side's length not valid")
            else:
                pass
        print("The sides of the polygon are: ", self.sides)
        
    def perimeter(self):
        return sum(self.sides)
    
    def getOrderedSides(self, increasing):
        return tuple(sorted(self.sides, reverse = increasing))

class Rectangle(Polygon):
    """This class inherits Polygon and calculates the area"""
    
    def __init__(self):
        self.n = 4
        self.sides = [0 for i in range(self.n)]
    
    def inputSidesRect(self):
        Polygon.inputSides(self)
        if (self.sides[0] == self.sides[1] and self.sides[2] == self.sides[3]) or (self.sides[0] == self.sides[2] and self.sides[1] == self.sides[3]) or (self.sides[0] == self.sides[3] and self.sides[1] == self.sides[2]):
            pass
        else:
            raise ValueError("ERROR: This is not a rectangle")
        
    def area(self):
        if (self.sides[0] == self.sides[1] and self.sides[2] == self.sides[3]) or (self.sides[0] == self.sides[2] and self.sides[1] == self.sides[3]) or (self.sides[0] == self.sides[3] and self.sides[1] == self.sides[2]):
            if self.sides[0] != self.sides[1]:
                return self.sides[0]*self.sides[1]
            elif self.sides[0] != self.sides[2]:
                return self.sides[0]*self.sides[2]
            else:
                return self.sides[0]*self.sides[3]
        else:
            raise ValueError("Error: this is not a rectangle")
    
r = Rectangle()
r.inputSidesRect()
print("The perimeter is: ", r.perimeter())
print("The area is: ", r.area())
type_input = bool(input("Type <True> for decreasing order, press <Enter> for increasing order: "))
print("The lengths of the ordered sides are: ", r.getOrderedSides(increasing = type_input))
    