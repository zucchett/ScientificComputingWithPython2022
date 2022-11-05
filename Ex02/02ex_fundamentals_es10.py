#10. Class Definition

class polygon:
    sides = []
    def __init__(self, sides) -> None:
        self.sides = list(sides)
    
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

poly = polygon((32,1,51,12))

print(poly.perimeter())

poly.getSide(3)

poly.setSide(3, 10)

print(poly.perimeter(), poly.getOrderedSides(increasing=True))
