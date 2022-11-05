
class polygon:
    def __init__(self , tup) -> None:
        self.tup = tup
        self.len = len(tup)
    
    def perimeter(self):
        p = self.tup[1] * self.len
        print(p)

    def getOrderedSides(self , increasing = True):
        print(sorted(self.tup))


tup = (1,2,2,1)
d = polygon(tup)
d.perimeter()
d.getOrderedSides()