class Polygon:
    
    sides = []
    
    def __init__(self, s):
        if len(s) >= 3:
            self.sides = list(s)
        else:
            print("Input another tuple; the components must be at least 3")
        
    def getSide(self, i): 
        return self.sides[i]
    
    def setSide(self, i, si): # n is the component index
        if i < len(self.sides):
            self.sides[i] = si
            
    def perimeter(self):
        p = 0
        for i in range(len(self.sides)):
            p = p + self.sides[i]
        return p
    
    def getOrderedSides(self, increasing):
        sorted_sides = sorted(self.sides, reverse = not increasing)
        tuple_ordered = (*sorted_sides,) 
        return tuple_ordered

            

pol_sides = Polygon((8,9, 5, 3))

print("The perimeter of the chosen polygon is: ", pol_sides.perimeter())

print("The ordered sides lengths are: ", pol_sides.getOrderedSides(increasing = True))

class Rectangle(Polygon):
    
    def __init__(self, s):
        if len(s) == 4 and sorted(list(s))[0] == sorted(list(s))[1] and sorted(list(s))[2] == sorted(list(s))[3]:
            self.sides = list(s)
        else:
            print("This is not a rectangle, chose another tuple")
            
    
    def area(self):
        a = self.sides[0]*self.sides[2]
        return a
        
rect_sides = Rectangle((4, 3, 3, 4))
print("The area of the rectangle is: ", rect_sides.area())
