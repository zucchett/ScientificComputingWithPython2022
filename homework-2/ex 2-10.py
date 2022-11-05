# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 08:06:38 2022

@author: gozde
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

    def getOrderedSides(self, increasing = True):
        ordered_list = self.lengths
        if increasing:
            ordered_list.sort()
        else:
            ordered_list.sort(reverse=True)
        return ordered_list

polygon = Polygon([5,7,1,2,0,4,3])
print("Polygon = ", polygon.lengths)
print("Perimeter of polygon = ",polygon.perimeter())
ordered_list = polygon.getOrderedSides()
print("increasing order: "+str(ordered_list))
ordered_list = polygon.getOrderedSides(increasing = False)
print("decrasing order:  "+str(ordered_list))