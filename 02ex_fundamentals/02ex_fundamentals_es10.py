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
    
    
t1 = (3, 9)
p = polygon(t1)

t2 = (4, 7, 14, 12)
p = polygon(t2)
print(p.perimeter())
print(p.getOrderedSides(False))
lengths = (78, 7, 10, 18)
p.setLengths(lengths)
print(p.getLengths())