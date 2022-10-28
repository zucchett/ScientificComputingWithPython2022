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


class rectangle(polygon):
    
    def __init__(self, vec):
        self.sides = list(vec)
        temp = sorted(self.sides)
        if not (isinstance(vec, tuple) and len(vec)==4 and temp[0]==temp[1] and temp[2] == temp[3] and all(item > 0 for item in temp)):
            raise ValueError(f"Not a proper rectangle")

    def area(self):

        temp = sorted(self.sides)
        return temp[0]*temp[2]


a = rectangle((1,2,2,1))
print(a.area())
a.setLen(1,3)
a.setLen(4,3)
print(a.area())
