# 11. Class Inheritance

class polygon:
    sides = []
    def __init__(self, sidesTuple) -> None:
        self.sides = list(sidesTuple)
    
    def getSide(self, index):
        return self.sides[index]
    
    def setSide(self, index, newValue):
        if index < len(self.sides):
            self.sides[index] = newValue

    def perimeter(self):
        return sum(self.sides)
    
    def getOrderedSides(self,increasing = True):
        self.sides.sort(reverse = not increasing)
        return tuple(self.sides)

class rectangle(polygon):

    def __init__(self, rectSides) -> None:
        if len(rectSides) == 2:
            self.sides = list(rectSides)
        else:
            print("Error! Not a Rectangle")
    
    def area(self):
        return self.sides[0] * self.sides[1]


testRectangle = rectangle((3,5,3))

print(testRectangle.area())       