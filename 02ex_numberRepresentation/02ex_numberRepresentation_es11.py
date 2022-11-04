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

class Rectangle(Polygon):
    def __init__(self, tuple):
        if len(tuple) == 4:
            if (tuple[0] == tuple[2] and tuple[1] == tuple[3]):
                self.tuple = tuple
            else:
                print("Error:It is not a Rectangle")
        else:
            print("Error: number of components is not 4")

    def getArea(self):
        return self.tuple[0] * self.tuple[1]

sample = Rectangle((3, 4, 3, 4))
sample.getArea()