class polygon:

    def __init__(self, vec):
        if not (isinstance(vec, tuple) and len(vec)>=3 and all(item > 0 for item in vec)):
            raise ValueError(f"A tuple with at least 3 elements is needed as input")
        self.sides = list(vec)
    
    def getLen(self,n):
        return self.sides[n-1]

    def setLen(self,n,x):
        self.sides[n-1] = x

    def perimeter(self):
        return sum(self.sides)

    def getOrderedSides(self,increasing = True):
        self.increasing = increasing
        if increasing:
            copy = sorted(self.sides)                       # in this way the sides variable of the object stays unordered
        else:
            copy = sorted(self.sides, reverse= True)
        
        return tuple(copy)



a = polygon((5,2,4))
print(a.perimeter())
print(a.getLen(2))
a.setLen(2,1)
print(a.getLen(2))
print(a.perimeter())
print(a.getOrderedSides(increasing = False))
print(a.getLen(2))