# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 08:15:55 2022

@author: gozde
"""

class Polygon:
    lengths = []

    def __init__(self, lengths):
        if len(lengths) > 2:
            self.lengths = lengths
        else:
            print("size should be greater than 2")

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
        if len(lengths) == 2:   
            self.x = lengths
           
        else:
            print("size should be 2")

    def area(self):
        return self.x[0] * self.x[1]
        
rectangle = Rectangle([2,9])
print("Area = ", rectangle.area())