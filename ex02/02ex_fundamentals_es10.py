
class polygon:
    def __init__(self , tuple) -> None:
        self.tuple = tuple
        self.len = len(tuple)
    
    def perimeter(self):
        p = self.tuple[1] * self.len
        print(p)

    def getOrderedSides(self , increasing = True):
        print(sorted(self.tuple))


tuple = (1,9,2,9)
x = polygon(tuple)
x.perimeter()
x.getOrderedSides()