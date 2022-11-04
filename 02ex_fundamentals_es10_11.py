# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:49:57 2022

@author: Ruben
"""

class polygon:
    
    x=[]
    
    def __init__(self, sides):
        if len(sides)>2:
            self.x=sides
        else: 
            print("This is not a polygon!")
        return None
            
    #def __bool__(self):
        if len(self.x)>2:
            return True
        return False

    def getSIDE(self, n):
        return self.x[n]
    
    def setSIDE(self, n, xi):
        if n < len(self.x):
            self.x[n] = xi
            
    def perimeter(self):
        return sum(self.x)
            
    def getOrderedSides(self, increasing):
        self.x.sort(reverse = not increasing)
        return self.x
        
    
    
class rectangle(polygon):

    def __init__(self, sides):
        self.okay=False
        for i in range(len(sides)):
            check=sides.copy()
            check.remove(check[i])
            if sides[i] not in check:
                self.okay=True
        if len(sides) != 4 or self.okay==True:
            print("This is not a rectangle!")
        else:
            self.x=sides
            
    def area(self):
        a = self.x[0]
        for i in range(1,len(self.x)):
            if self.x[i] != a:
                b = self.x[i]
                break
        return a*b
    
            
p = rectangle([5,7,5,5])







        