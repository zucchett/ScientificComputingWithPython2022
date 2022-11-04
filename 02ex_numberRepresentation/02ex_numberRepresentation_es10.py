class Polygon():
    def __init__(self, tuple):
        self.tuple = tuple
    
    def getLength(self, index):
        return self.tuple[index]

    def setLength(self, index, newValue):
        self.tuple[index] = newValue

    def perimeter(self):
        return sum(self.tuple)

    def getOrderedSides(self, isIncreasing):
        if isIncreasing:
            return sorted(self.tuple)
        else:
            return tuple(reversed(sorted(self.tuple)))
            
sample = Polygon((1, 2, 3))
print(sample.getLength(1))
print(sample.perimeter())
print(sample.getOrderedSides(False))

        