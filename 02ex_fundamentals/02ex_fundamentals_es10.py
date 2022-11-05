#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:45:44 2022

@author: alessandra
"""

#%%es10
# Define a class polygon. The constructor has to take a tuple as input that 
# contains the length of each side. The (unordered) input list does not have
# to have a fixed length, but should contain at least 3 items.

# Create appropriate methods to get and set the length of each side

# Create a method perimeter() that returns the perimeter of the polygon

# Create a method getOrderedSides(increasing = True) that returns a tuple 
# containing the length of the sides arranged in increasing or decreasing 
# order, depending on the argument of the method

# Test the class by creating an instance and calling the perimeter() and 
# getOrderedSides(increasing = True) methods.

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
    
t = Polygon()
t.inputSides()
print("The perimeter is: ", t.perimeter())
type_input = bool(input("Type <True> for decreasing order, press <Enter> for increasing order: "))
print("The lengths of the ordered sides are: ", t.getOrderedSides(increasing = type_input))