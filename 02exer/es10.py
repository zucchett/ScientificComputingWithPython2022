#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import math
# Class definition
class polygon:
    # Definition of the class attributes, which are common for all instances of the same class
    x = ()   
    # Definition of the Constructor, a special method that is called every time a new object is created
    def __init__(self,n,components):
        if n < 3:
           raise ValueError('ERROR: Number of sides lower than 3  is not possible')
        else:
            self.x = components
                 
    # Definition of the methods    
    def getDimension(self): 
        return len(self.x)
     
    def perimeter(self):
        p = 0
        for i in range(len(self.x)):
            p += self.x[i]
        return p
    def getOrderedSides(self, increasing ):
        return tuple(sorted(self.x, reverse = increasing))
#############################################################
N = int(input("Set dimension of the polygon: "))
l=()
for i in range(N):
    element = float(input(""))
    l = l + (element,)
    
a = polygon(N,l)
print("Perimeter is: ",a.perimeter())
type = bool(input("Press <Enter> for increasing order and other charachters for decreasing order:"))
print(a.getOrderedSides(increasing = type))
