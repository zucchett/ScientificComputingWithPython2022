# Class definition
import math

class polygon:

    x = []
    
    def __init__(self, poly_sides):
        if len(poly_sides) >= 3:
            self.x = list(poly_sides)
        else:
            print("Sides of the polygon must be at least 3!")
            self.__del__
        
    def __del__(self):
        print("Destructor called")
        
    def getSide(self,n):
        return self.x[n]

    def setSide(self, n, new_value):
        self.x[n] = new_value

    def getSides(self):
        return len(self.x)
    
    def printPoly(self):
        return self.x

    def perimeter(self):
        perim_poly = 0
        for i in range(len(self.x)):
            perim_poly = perim_poly + self.x[i]
        return perim_poly
    
    def getOrderedSides(self,increasing_sides):
        return tuple(sorted(self.x,reverse = not increasing_sides))

# End of the class definition

a = polygon((5, 5, 1, 2))
print(a.printPoly())
a.setSide(0,10)
print(a.printPoly())
print(a.perimeter())

print(a.getOrderedSides(True))