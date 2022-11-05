# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:47:37 2022

@author: Federico
"""
import math

class polygon:
    
    p=()
    
    #constructor
    def __init__(self, components):
        if (len(components) >= 3 & components[i] >= 0 for i in range(len(components))):
            self.p = components # tuple as input
        else:
            print("At least three sides are needed to build a polygon!")
            
    #get and set sides
    def getSide(self, n): # n is the component index
        return self.p[n]
    
    def setSide(self, n, xi): # n is the component index, and xi is the value
        if n < len(self.x):
            self.p[n] = xi
    
    #perimeter
    def perimeter(self):
        perimeter=0
        for x in self.p: perimeter += x
        return perimeter
    
    def getOrderedSides(self, decreasing = True):
        if decreasing == True:
            p_copy = [i for i in self.p]
            p_copy.sort()
            tuple_poly = tuple(p_copy)
            return tuple_poly
        else:
            p_copy = [i for i in self.p]
            p_copy.sort(reverse=True)
            return tuple(p_copy)
            
        
class rectangle(polygon):
    
    #constructor
    def __init__(self, components):
        if len(components) == 4: 
            self.p = components
        else:
            print("That's not a rectangle")
    
    def area(self):
        prod = self.p[1]*self.p[2]*self.p[0]*self.p[3]
        return math.sqrt(prod)