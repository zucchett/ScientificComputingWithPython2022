class polygon:
    sides = ()
    def __init__(self, sides):
        if (len(sides) < 3):
            print("A polygon should have at list Three sides!!!")
            return
        else:
            self.sides = sides
    
    def getLengths (self):
        return self.sides
    
    def setLengths (self, lengths):
        if (len(lengths) != len(self.sides)):
            print("You should enter",len(self.sides),"number!!!")
            return
        else:
            self.sides = lengths
            
    def perimeter(self):
        return sum(self.sides)
    
    def getOrderedSides (self, increasing = True):
        self.sides = tuple(sorted(self.sides, reverse = not increasing))
        return self.sides

# define rectangle class
class rectangle (polygon):
    def __init__ (self, length, width):
        t = (length, width, length, width)
        polygon.__init__(self, t)
    
    def area (self):
        return self.sides[0] * self.sides[1]

b = rectangle(8, 4)
print(b.area())
print(b.getLengths())
print(b.getOrderedSides(True))