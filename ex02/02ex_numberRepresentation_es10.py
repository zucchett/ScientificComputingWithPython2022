import math
import numpy as np
class Polygon:
    
    sides = []
    def __init__(self, n):
        self.n = n
        for ii in range(self.n):
            self.sides.append(float(input("Enter side "+str(ii+1)+" ")))      

    def perimeter(self):
        
        p = 0.
        for ii in range(self.n):
            p += self.sides[ii]
        
        print('perimeter is :', p)
        
    def getOrderedSides(self, increasing = True):
        
        self.increasing = increasing
        x =[]
        x = np.sort(self.sides) 
        print("sorted sides :", tuple(x))
            
instance = Polygon(3)
instance.perimeter()
instance.getOrderedSides()
