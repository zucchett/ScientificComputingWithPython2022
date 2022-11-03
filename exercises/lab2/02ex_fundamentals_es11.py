# Class inheritance

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
        
class rectangle(polygon): # class 'Vector3D' inherits from class 'VectorND'

    # The constructor here is optional, and can be inherited from the parent class if omitted
    def __init__(self, components):
        if len(components) == 2:
            self.x.append(components[0])
            self.x.append(components[1])
            self.x.append(components[0])
            self.x.append(components[1])
        else:
            print("Rectangles must have 4 sides!")

    # New methods that only belong to the child class
    def area(self):
        return self.x[0]*self.x[1]

a = rectangle([5, 10])
print(a.printPoly())
print(a.area())